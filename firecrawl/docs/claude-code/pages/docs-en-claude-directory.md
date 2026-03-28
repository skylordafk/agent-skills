# Explore the .claude directory - Claude Code Docs

> Source: https://code.claude.com/docs/en/claude-directory

[Skip to main content](https://code.claude.com/docs/en/claude-directory#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Core concepts

Explore the .claude directory

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

Claude Code reads instructions, settings, skills, subagents, and memory from your project directory and from `~/.claude` in your home directory. Commit project files to git to share them with your team; files in `~/.claude` are personal configuration that applies across all your projects.Most users only edit `CLAUDE.md` and `settings.json`. The rest of the directory is optional: add skills, rules, or subagents as you need them.This page is an interactive explorer: click files in the tree to see what each one does, when it loads, and an example. For a quick reference, see the [file reference table](https://code.claude.com/docs/en/claude-directory#file-reference) below.

The interactive explorer works best on a larger screen. See the [file reference table](https://code.claude.com/docs/en/claude-directory#file-reference) below, or show the explorer anyway.

ProjectGlobal (~/)⊞⛶

CLAUDE.md

{}.mcp.json

.worktreeinclude

▾.claude/

{}settings.json

{}settings.local.json

▾rules/

testing.md

api-design.md

▾skills/

▾security-review/

SKILL.md

checklist.md

▾commands/

fix-issue.md

▸output-styles/

▾agents/

code-reviewer.md

▾agent-memory/

▾<agent-name>/

MEMORY.md

CLAUDE.md selected

your-project / CLAUDE.md

CLAUDE.md

Project instructions Claude reads every session

committed

When it loads

Loaded into context at the start of every session

Project-specific instructions that shape how Claude works in this repository. Put your conventions, common commands, and architectural context here so Claude operates with the same assumptions your team does.

Tips

●Target under 200 lines. Longer files still load in full but may reduce adherence

●CLAUDE.md loads into every session. If something only matters for specific tasks, move it to a [skill](https://code.claude.com/docs/en/skills) or a path-scoped [rule](https://code.claude.com/docs/en/memory#organize-rules-with-claude/rules/) so it loads only when needed

●List the commands you run most, like build, test, and format, so Claude knows them without you spelling them out each time

●Run `/memory` to open and edit CLAUDE.md from within a session

●Also works at `.claude/CLAUDE.md` if you prefer to keep the project root clean

This example is for a TypeScript and React project. It lists the build and test commands, the framework conventions Claude should follow, and project-specific rules like export style and file layout.

CLAUDE.mdCopy

```
# Project conventions

## Commands
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint`

## Stack
- TypeScript with strict mode
- React 19, functional components only

## Rules
- Named exports, never default exports
- Tests live next to source: `foo.ts` -> `foo.test.ts`
- All API routes return `{ data, error }` shape
```

[Full docs →](https://code.claude.com/docs/en/memory)

## [​](https://code.claude.com/docs/en/claude-directory\#what%E2%80%99s-not-shown)  What’s not shown

The explorer covers the files you’ll interact with most. A few things live elsewhere:

| File | Location | Purpose |
| --- | --- | --- |
| `managed-settings.json` | System-level, varies by OS | Enterprise-enforced settings that you can’t override. See [server-managed settings](https://code.claude.com/docs/en/server-managed-settings). |
| `CLAUDE.local.md` | Project root | Your private preferences for this project, loaded alongside CLAUDE.md. Create it manually and add it to `.gitignore`. |

## [​](https://code.claude.com/docs/en/claude-directory\#file-reference)  File reference

This table lists every file the explorer covers. Project-scope files live in your repo under `.claude/` (or at the root for `CLAUDE.md`, `.mcp.json`, and `.worktreeinclude`). Global-scope files live in `~/.claude/` and apply across all projects.

Several things can override what you put in these files:

- [Managed settings](https://code.claude.com/docs/en/server-managed-settings) deployed by your organization take precedence over everything
- CLI flags like `--permission-mode` or `--settings` override `settings.json` for that session
- Some environment variables take precedence over their equivalent setting, but this varies: check the [environment variables reference](https://code.claude.com/docs/en/env-vars) for each one

See [settings precedence](https://code.claude.com/docs/en/settings#settings-precedence) for the full order.

Click a filename to open that node in the explorer above.

| File | Scope | Commit | What it does | Reference |
| --- | --- | --- | --- | --- |
| [`CLAUDE.md`](https://code.claude.com/docs/en/claude-directory#ce-claude-md) | Project and global | ✓ | Instructions loaded every session | [Memory](https://code.claude.com/docs/en/memory) |
| [`rules/*.md`](https://code.claude.com/docs/en/claude-directory#ce-rules) | Project and global | ✓ | Topic-scoped instructions, optionally path-gated | [Rules](https://code.claude.com/docs/en/memory#organize-rules-with-claude/rules/) |
| [`settings.json`](https://code.claude.com/docs/en/claude-directory#ce-settings-json) | Project and global | ✓ | Permissions, hooks, env vars, model defaults | [Settings](https://code.claude.com/docs/en/settings) |
| [`settings.local.json`](https://code.claude.com/docs/en/claude-directory#ce-settings-local-json) | Project only |  | Your personal overrides, auto-gitignored | [Settings scopes](https://code.claude.com/docs/en/settings#settings-files) |
| [`.mcp.json`](https://code.claude.com/docs/en/claude-directory#ce-mcp-json) | Project only | ✓ | Team-shared MCP servers | [MCP scopes](https://code.claude.com/docs/en/mcp#mcp-installation-scopes) |
| [`.worktreeinclude`](https://code.claude.com/docs/en/claude-directory#ce-worktreeinclude) | Project only | ✓ | Gitignored files to copy into new worktrees | [Worktrees](https://code.claude.com/docs/en/common-workflows#copy-gitignored-files-to-worktrees) |
| [`skills/<name>/SKILL.md`](https://code.claude.com/docs/en/claude-directory#ce-skills) | Project and global | ✓ | Reusable prompts invoked with `/name` or auto-invoked | [Skills](https://code.claude.com/docs/en/skills) |
| [`commands/*.md`](https://code.claude.com/docs/en/claude-directory#ce-commands) | Project and global | ✓ | Single-file prompts; same mechanism as skills | [Skills](https://code.claude.com/docs/en/skills) |
| [`output-styles/*.md`](https://code.claude.com/docs/en/claude-directory#ce-output-styles) | Project and global | ✓ | Custom system-prompt sections | [Output styles](https://code.claude.com/docs/en/output-styles) |
| [`agents/*.md`](https://code.claude.com/docs/en/claude-directory#ce-agents) | Project and global | ✓ | Subagent definitions with their own prompt and tools | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| [`agent-memory/<name>/`](https://code.claude.com/docs/en/claude-directory#ce-agent-memory) | Project and global | ✓ | Persistent memory for subagents | [Persistent memory](https://code.claude.com/docs/en/sub-agents#enable-persistent-memory) |
| [`~/.claude.json`](https://code.claude.com/docs/en/claude-directory#ce-claude-json) | Global only |  | App state, OAuth, UI toggles, personal MCP servers | [Global config](https://code.claude.com/docs/en/settings#global-config-settings) |
| [`projects/<project>/memory/`](https://code.claude.com/docs/en/claude-directory#ce-global-projects) | Global only |  | Auto memory: Claude’s notes to itself across sessions | [Auto memory](https://code.claude.com/docs/en/memory#auto-memory) |
| [`keybindings.json`](https://code.claude.com/docs/en/claude-directory#ce-keybindings) | Global only |  | Custom keyboard shortcuts | [Keybindings](https://code.claude.com/docs/en/keybindings) |

## [​](https://code.claude.com/docs/en/claude-directory\#check-what-loaded)  Check what loaded

The explorer shows what files can exist. To see what actually loaded in your current session, use these commands:

| Command | Shows |
| --- | --- |
| `/context` | Token usage by category: system prompt, memory files, skills, MCP tools, and messages |
| `/memory` | Which CLAUDE.md and rules files loaded, plus auto-memory entries |
| `/agents` | Configured subagents and their settings |
| `/hooks` | Active hook configurations |
| `/mcp` | Connected MCP servers and their status |
| `/skills` | Available skills from project, user, and plugin sources |
| `/permissions` | Current allow and deny rules |
| `/doctor` | Installation and configuration diagnostics |

Run `/context` first for the overview, then the specific command for the area you want to investigate.

## [​](https://code.claude.com/docs/en/claude-directory\#related-resources)  Related resources

- [Manage Claude’s memory](https://code.claude.com/docs/en/memory): write and organize CLAUDE.md, rules, and auto memory
- [Configure settings](https://code.claude.com/docs/en/settings): set permissions, hooks, environment variables, and model defaults
- [Create skills](https://code.claude.com/docs/en/skills): build reusable prompts and workflows
- [Configure subagents](https://code.claude.com/docs/en/sub-agents): define specialized agents with their own context

Was this page helpful?

YesNo

[Extend Claude Code](https://code.claude.com/docs/en/features-overview) [Explore the context window](https://code.claude.com/docs/en/context-window)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.