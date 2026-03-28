# Explore the context window - Claude Code Docs

> Source: https://code.claude.com/docs/en/context-window

[Skip to main content](https://code.claude.com/docs/en/context-window#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Core concepts

Explore the context window

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

Claude Code’s context window holds everything Claude knows about your session: your instructions, the files it reads, its own responses, and content that never appears in your terminal. The timeline below walks through what loads and when. See [the written breakdown](https://code.claude.com/docs/en/context-window#what-the-timeline-shows) for the same content as a list.

This interactive timeline works best on a larger screen. See [the written breakdown below](https://code.claude.com/docs/en/context-window#what-the-timeline-shows) for the same concepts.

Explore the context window

A simulated session showing what enters context and what it costs

~0tokens

/ 200K · illustrative

System

CLAUDE.md

Memory

Skills

MCP

Rules

You

Files

Output

Claude

Hooks

= appears in your terminal

$claude

▶Start session

Watch what loads into context, from the moment you run `claude` through a full conversation.

👁

Hover or click any event

Hover to preview. Click to pin so you can scroll.

Key takeaway

A lot loads before you type anything. CLAUDE.md, memory, skills, and MCP tools are all in context before your first prompt.

In your terminal you see

The input box, waiting for your first message. Everything above loads silently before you type anything.

▶

0%⛶

## [​](https://code.claude.com/docs/en/context-window\#what-the-timeline-shows)  What the timeline shows

The session walks through a realistic flow with representative token counts:

- **Before you type anything**: CLAUDE.md, auto memory, MCP tool names, and skill descriptions all load into context. Your own setup may add more here, like an [output style](https://code.claude.com/docs/en/output-styles) or text from [`--append-system-prompt`](https://code.claude.com/docs/en/cli-reference), which both go into the system prompt the same way.
- **As Claude works**: each file read adds to context, [path-scoped rules](https://code.claude.com/docs/en/memory#path-specific-rules) load automatically alongside matching files, and a [PostToolUse hook](https://code.claude.com/docs/en/hooks-guide) fires after each edit.
- **The follow-up prompt**: a [subagent](https://code.claude.com/docs/en/sub-agents) handles the research in its own separate context window, so the large file reads stay out of yours. Only the summary and a small metadata trailer come back.
- **At the end**: `/compact` replaces the conversation with a structured summary. Most startup content reloads automatically. The [skill](https://code.claude.com/docs/en/skills) listing is the one exception.

## [​](https://code.claude.com/docs/en/context-window\#check-your-own-session)  Check your own session

The visualization uses representative numbers. To see your actual context usage at any point, run `/context` for a live breakdown by category with optimization suggestions. Run `/memory` to check which CLAUDE.md and auto memory files loaded at startup.

## [​](https://code.claude.com/docs/en/context-window\#related-resources)  Related resources

For deeper coverage of the features shown in the timeline, see these pages:

- [Extend Claude Code](https://code.claude.com/docs/en/features-overview): when to use CLAUDE.md vs skills vs rules vs hooks vs MCP
- [Store instructions and memories](https://code.claude.com/docs/en/memory): CLAUDE.md hierarchy and auto memory
- [Subagents](https://code.claude.com/docs/en/sub-agents): delegate research to a separate context window
- [Best practices](https://code.claude.com/docs/en/best-practices): managing context as your primary constraint
- [Reduce token usage](https://code.claude.com/docs/en/costs#reduce-token-usage): strategies for keeping context usage low

Was this page helpful?

YesNo

[Explore the .claude directory](https://code.claude.com/docs/en/claude-directory) [Store instructions and memories](https://code.claude.com/docs/en/memory)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.