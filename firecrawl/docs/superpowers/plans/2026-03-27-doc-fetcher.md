# Doc Fetcher Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a Python script that uses Firecrawl to map and scrape documentation sites, saving results as individual markdown files per page plus a concatenated full file per source.

**Architecture:** Single script (`fetch_docs.py`) with a source config dict at the top. Uses Firecrawl SDK's `map()` to discover URLs, then `scrape()` to pull each page as markdown. Results stored in `docs/{source}/pages/` with a manifest and concatenated file.

**Tech Stack:** Python 3.9+, `firecrawl` SDK (v4.21+), `python-dotenv` for env loading.

---

### Task 1: Install dependencies and create requirements.txt

**Files:**
- Create: `requirements.txt`

- [ ] **Step 1: Create requirements.txt**

```
firecrawl>=4.21
python-dotenv>=1.0
```

- [ ] **Step 2: Install dependencies**

Run: `pip3 install -r requirements.txt`
Expected: Both packages install successfully (firecrawl already installed, dotenv may be new).

- [ ] **Step 3: Verify imports**

Run: `python3 -c "from firecrawl import Firecrawl; from dotenv import load_dotenv; print('ok')"`
Expected: `ok`

- [ ] **Step 4: Commit**

```bash
git add requirements.txt
git commit -m "chore: add requirements for doc fetcher"
```

---

### Task 2: Build fetch_docs.py — config, CLI args, and map functionality

**Files:**
- Create: `fetch_docs.py`

- [ ] **Step 1: Create fetch_docs.py with config, CLI parsing, and map logic**

```python
#!/usr/bin/env python3
"""Fetch documentation from configured sources using Firecrawl."""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

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
    },
    "codex": {
        "url": "https://developers.openai.com/codex",
        "description": "OpenAI Codex documentation",
    },
    "openclaw": {
        "url": "https://docs.openclaw.ai/",
        "description": "OpenClaw AI agent platform documentation",
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


def map_source(client: Firecrawl, name: str, config: dict, dry_run: bool = False) -> list:
    """Map a source URL to discover all doc pages. Returns list of URL strings."""
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Mapping {name}: {config['url']}")

    if dry_run:
        # In dry-run mode, try to load existing manifest
        manifest_path = DOCS_DIR / name / "manifest.json"
        if manifest_path.exists():
            with open(manifest_path) as f:
                data = json.load(f)
            print(f"  Would re-map. Existing manifest has {len(data['urls'])} URLs.")
            return data["urls"]
        else:
            print("  Would map (no existing manifest).")
            return []

    result = client.map(url=config["url"])
    urls = [link.url for link in result.links]
    print(f"  Found {len(urls)} URLs (1 credit used)")

    # Save manifest
    source_dir = DOCS_DIR / name
    source_dir.mkdir(parents=True, exist_ok=True)
    manifest = {"source": name, "base_url": config["url"], "urls": urls, "mapped_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
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
        total_credits += 0 if args.dry_run else 1

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
```

- [ ] **Step 2: Verify the script parses and --list works**

Run: `python3 fetch_docs.py --list`
Expected:
```
Available sources:
  claude-code: Claude Code CLI documentation (https://code.claude.com/docs/en/overview)
  codex: OpenAI Codex documentation (https://developers.openai.com/codex)
  openclaw: OpenClaw AI agent platform documentation (https://docs.openclaw.ai/)
```

- [ ] **Step 3: Verify --dry-run works without spending credits**

Run: `python3 fetch_docs.py --dry-run`
Expected: Shows "[DRY RUN]" messages, no API calls, no credits spent.

- [ ] **Step 4: Commit**

```bash
git add fetch_docs.py
git commit -m "feat: add doc fetcher script with Firecrawl map+scrape"
```

---

### Task 3: Test with a single source using --map-only

This is a live API test. Costs 1 credit.

- [ ] **Step 1: Map one source to verify the API connection works**

Run: `python3 fetch_docs.py openclaw --map-only`
Expected: Prints found URLs, creates `docs/openclaw/manifest.json`.

- [ ] **Step 2: Inspect the manifest**

Run: `cat docs/openclaw/manifest.json | python3 -m json.tool | head -20`
Expected: JSON with `urls` array containing discovered doc page URLs.

- [ ] **Step 3: Review URL count to estimate credit cost**

Check how many URLs were discovered. If >200 for a single source, consider adding `limit` to the map call or filtering URLs before scraping.

---

### Task 4: Test full scrape on a small source

Pick the source with fewest URLs from Task 3's manifest. Scrape it fully to validate the end-to-end flow.

- [ ] **Step 1: Run full fetch on the smallest source**

Run: `python3 fetch_docs.py <smallest-source>`
Expected: Maps + scrapes all pages, creates `docs/<source>/pages/*.md` and `docs/<source>/<source>-full.md`.

- [ ] **Step 2: Verify output structure**

Run: `ls -la docs/<source>/pages/ | head -20` and `wc -l docs/<source>/<source>-full.md`
Expected: Individual .md files in pages/, concatenated file with substantial content.

- [ ] **Step 3: Spot-check a page file**

Run: `head -30 docs/<source>/pages/<any-file>.md`
Expected: Markdown with title header, source URL, and meaningful doc content.

- [ ] **Step 4: Commit**

```bash
git add fetch_docs.py docs/
git commit -m "feat: verified doc fetcher with live API test"
```

---

### Task 5: Fetch remaining sources

- [ ] **Step 1: Map remaining sources to check URL counts**

Run: `python3 fetch_docs.py --map-only`
Expected: Manifests created for all three sources. Check total URL count stays within credit budget (~497 remaining after Task 3-4).

- [ ] **Step 2: Scrape all sources**

Run: `python3 fetch_docs.py`
Expected: All three sources mapped and scraped. Full output structure under `docs/`.

- [ ] **Step 3: Verify all outputs**

Run: `find docs/ -name "*-full.md" -exec wc -l {} \;`
Expected: Three full files with substantial line counts.

- [ ] **Step 4: Add docs/ to .gitignore (optional) or commit docs**

Decide: should fetched docs be committed to git or regenerated on demand? If committing:

```bash
git add docs/ fetch_docs.py
git commit -m "feat: fetch initial documentation for all sources"
```

If not committing docs (regenerate on demand):

Create `.gitignore`:
```
docs/claude-code/
docs/codex/
docs/openclaw/
```
