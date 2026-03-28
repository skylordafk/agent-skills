#!/usr/bin/env python3
"""Fetch documentation from configured sources using Firecrawl."""

import argparse
import json
import os
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv
from firecrawl import Firecrawl

load_dotenv()

# ---------------------------------------------------------------------------
# Source configuration — add new sources here
# ---------------------------------------------------------------------------
SOURCES = {
    "claude-code": {
        "url": "https://code.claude.com/docs/en/overview",
        "description": "Claude Code CLI documentation",
        # Firecrawl map can't discover SPA pages; use sitemap instead
        "sitemap": "https://code.claude.com/docs/sitemap.xml",
        "include": ["/docs/en/"],  # English pages only
    },
    "codex": {
        "url": "https://developers.openai.com/codex",
        "description": "OpenAI Codex documentation",
    },
}

DOCS_DIR = Path(__file__).parent / "docs"


def get_client() -> Firecrawl:
    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        print("Error: FIRECRAWL_API_KEY not set in environment or .env")
        sys.exit(1)
    return Firecrawl(api_key=api_key)


def slugify(url: str) -> str:
    """Turn a URL path into a filename-safe slug."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        path = "index"
    # Replace path separators and special chars with hyphens
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", path).strip("-").lower()
    return slug or "index"


def urls_from_sitemap(sitemap_url: str) -> list:
    """Fetch and parse a sitemap.xml, returning all <loc> URLs."""
    resp = requests.get(sitemap_url, timeout=30)
    resp.raise_for_status()
    root = ET.fromstring(resp.content)
    # Handle XML namespace
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [loc.text for loc in root.findall(".//sm:loc", ns)]
    if not urls:
        # Try without namespace
        urls = [loc.text for loc in root.findall(".//{*}loc")]
    return urls


def filter_urls(urls: list, include: list = None, exclude: list = None) -> list:
    """Filter URLs by include/exclude substring patterns."""
    if include:
        urls = [u for u in urls if any(pat in u for pat in include)]
    if exclude:
        urls = [u for u in urls if not any(pat in u for pat in exclude)]
    return urls


def map_source(client: Firecrawl, name: str, config: dict, dry_run: bool = False) -> list:
    """Map a source URL to discover all doc pages. Returns list of URL strings."""
    use_sitemap = "sitemap" in config

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Mapping {name}: {config['url']}")
    if use_sitemap:
        print(f"  Using sitemap: {config['sitemap']}")

    if dry_run:
        manifest_path = DOCS_DIR / name / "manifest.json"
        if manifest_path.exists():
            with open(manifest_path) as f:
                data = json.load(f)
            print(f"  Would re-map. Existing manifest has {len(data['urls'])} URLs.")
            return data["urls"]
        else:
            print("  Would map (no existing manifest).")
            return []

    # Discover URLs via sitemap or Firecrawl map
    if use_sitemap:
        urls = urls_from_sitemap(config["sitemap"])
        print(f"  Sitemap has {len(urls)} URLs (0 credits)")
    else:
        result = client.map(url=config["url"])
        urls = [link.url for link in result.links]
        print(f"  Found {len(urls)} URLs (1 credit used)")

    # Apply include/exclude filters
    urls = filter_urls(urls, config.get("include"), config.get("exclude"))
    print(f"  After filtering: {len(urls)} URLs")

    # Save manifest
    source_dir = DOCS_DIR / name
    source_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "source": name,
        "base_url": config["url"],
        "discovery": "sitemap" if use_sitemap else "firecrawl-map",
        "urls": urls,
        "mapped_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    with open(source_dir / "manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"  Manifest saved to docs/{name}/manifest.json")

    return urls


def scrape_source(client: Firecrawl, name: str, urls: list, dry_run: bool = False):
    """Scrape all URLs for a source and save as markdown files."""
    if not urls:
        print(f"  No URLs to scrape for {name}.")
        return

    source_dir = DOCS_DIR / name
    pages_dir = source_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Scraping {name}: {len(urls)} pages")

    if dry_run:
        estimated = len(urls)
        print(f"  Would scrape {estimated} pages ({estimated} credits)")
        for url in urls[:5]:
            print(f"    {url} -> pages/{slugify(url)}.md")
        if len(urls) > 5:
            print(f"    ... and {len(urls) - 5} more")
        return

    all_content = []
    for i, url in enumerate(urls, 1):
        slug = slugify(url)
        print(f"  [{i}/{len(urls)}] {url}")

        try:
            doc = client.scrape(url, formats=["markdown"])
            markdown = doc.markdown or ""
            title = doc.metadata.title if doc.metadata and doc.metadata.title else slug

            # Save individual page
            page_path = pages_dir / f"{slug}.md"
            page_header = f"# {title}\n\n> Source: {url}\n\n"
            with open(page_path, "w") as f:
                f.write(page_header + markdown)

            # Collect for concatenated file
            all_content.append(f"---\n\n# {title}\n\n> Source: {url}\n\n{markdown}")

        except Exception as e:
            print(f"    Error: {e}")
            all_content.append(f"---\n\n# ERROR: {url}\n\nFailed to scrape: {e}")

    # Write concatenated file
    full_path = source_dir / f"{name}-full.md"
    header = f"# {SOURCES[name]['description']}\n\nGenerated: {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}\nPages: {len(urls)}\n\n"
    with open(full_path, "w") as f:
        f.write(header + "\n".join(all_content))
    print(f"  Full doc saved to docs/{name}/{name}-full.md")


def main():
    parser = argparse.ArgumentParser(description="Fetch documentation using Firecrawl")
    parser.add_argument("sources", nargs="*", help="Source names to fetch (default: all)")
    parser.add_argument("--map-only", action="store_true", help="Only map URLs, don't scrape")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without spending credits")
    parser.add_argument("--list", action="store_true", help="List available sources")
    args = parser.parse_args()

    if args.list:
        print("Available sources:")
        for name, config in SOURCES.items():
            print(f"  {name}: {config['description']} ({config['url']})")
        return

    # Determine which sources to process
    targets = args.sources if args.sources else list(SOURCES.keys())
    for name in targets:
        if name not in SOURCES:
            print(f"Error: Unknown source '{name}'. Use --list to see available sources.")
            sys.exit(1)

    client = None if args.dry_run else get_client()

    total_credits = 0
    for name in targets:
        config = SOURCES[name]
        urls = map_source(client, name, config, dry_run=args.dry_run)
        if not args.dry_run and "sitemap" not in config:
            total_credits += 1

        if not args.map_only:
            scrape_source(client, name, urls, dry_run=args.dry_run)
            if not args.dry_run:
                total_credits += len(urls)

    if not args.dry_run:
        print(f"\nDone. Estimated credits used: {total_credits}")
    else:
        print(f"\n[DRY RUN] No credits spent.")


if __name__ == "__main__":
    main()
