# Tools reference - Claude Code Docs

> Source: https://code.claude.com/docs/en/tools-reference

[Skip to main content](https://code.claude.com/docs/en/tools-reference#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Reference

Tools reference

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

On this page

- [Bash tool behavior](https://code.claude.com/docs/en/tools-reference#bash-tool-behavior)
- [PowerShell tool](https://code.claude.com/docs/en/tools-reference#powershell-tool)
- [Enable the PowerShell tool](https://code.claude.com/docs/en/tools-reference#enable-the-powershell-tool)
- [Shell selection in settings, hooks, and skills](https://code.claude.com/docs/en/tools-reference#shell-selection-in-settings-hooks-and-skills)
- [Preview limitations](https://code.claude.com/docs/en/tools-reference#preview-limitations)
- [See also](https://code.claude.com/docs/en/tools-reference#see-also)

Claude Code has access to a set of tools that help it understand and modify your codebase. The tool names below are the exact strings you use in [permission rules](https://code.claude.com/docs/en/permissions#tool-specific-permission-rules), [subagent tool lists](https://code.claude.com/docs/en/sub-agents), and [hook matchers](https://code.claude.com/docs/en/hooks).

| Tool | Description | Permission Required |
| --- | --- | --- |
| `Agent` | Spawns a [subagent](https://code.claude.com/docs/en/sub-agents) with its own context window to handle a task | No |
| `AskUserQuestion` | Asks multiple-choice questions to gather requirements or clarify ambiguity | No |
| `Bash` | Executes shell commands in your environment. See [Bash tool behavior](https://code.claude.com/docs/en/tools-reference#bash-tool-behavior) | Yes |
| `CronCreate` | Schedules a recurring or one-shot prompt within the current session (gone when Claude exits). See [scheduled tasks](https://code.claude.com/docs/en/scheduled-tasks) | No |
| `CronDelete` | Cancels a scheduled task by ID | No |
| `CronList` | Lists all scheduled tasks in the session | No |
| `Edit` | Makes targeted edits to specific files | Yes |
| `EnterPlanMode` | Switches to plan mode to design an approach before coding | No |
| `EnterWorktree` | Creates an isolated [git worktree](https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees) and switches into it | No |
| `ExitPlanMode` | Presents a plan for approval and exits plan mode | Yes |
| `ExitWorktree` | Exits a worktree session and returns to the original directory | No |
| `Glob` | Finds files based on pattern matching | No |
| `Grep` | Searches for patterns in file contents | No |
| `ListMcpResourcesTool` | Lists resources exposed by connected [MCP servers](https://code.claude.com/docs/en/mcp) | No |
| `LSP` | Code intelligence via language servers. Reports type errors and warnings automatically after file edits. Also supports navigation operations: jump to definitions, find references, get type info, list symbols, find implementations, trace call hierarchies. Requires a [code intelligence plugin](https://code.claude.com/docs/en/discover-plugins#code-intelligence) and its language server binary | No |
| `NotebookEdit` | Modifies Jupyter notebook cells | Yes |
| `PowerShell` | Executes PowerShell commands on Windows. Opt-in preview. See [PowerShell tool](https://code.claude.com/docs/en/tools-reference#powershell-tool) | Yes |
| `Read` | Reads the contents of files | No |
| `ReadMcpResourceTool` | Reads a specific MCP resource by URI | No |
| `Skill` | Executes a [skill](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill) within the main conversation | Yes |
| `TaskCreate` | Creates a new task in the task list | No |
| `TaskGet` | Retrieves full details for a specific task | No |
| `TaskList` | Lists all tasks with their current status | No |
| `TaskOutput` | (Deprecated) Retrieves output from a background task. Prefer `Read` on the task’s output file path | No |
| `TaskStop` | Kills a running background task by ID | No |
| `TaskUpdate` | Updates task status, dependencies, details, or deletes tasks | No |
| `TodoWrite` | Manages the session task checklist. Available in non-interactive mode and the [Agent SDK](https://code.claude.com/docs/en/headless); interactive sessions use TaskCreate, TaskGet, TaskList, and TaskUpdate instead | No |
| `ToolSearch` | Searches for and loads deferred tools when [tool search](https://code.claude.com/docs/en/mcp#scale-with-mcp-tool-search) is enabled | No |
| `WebFetch` | Fetches content from a specified URL | Yes |
| `WebSearch` | Performs web searches | Yes |
| `Write` | Creates or overwrites files | Yes |

Permission rules can be configured using `/permissions` or in [permission settings](https://code.claude.com/docs/en/settings#available-settings). Also see [Tool-specific permission rules](https://code.claude.com/docs/en/permissions#tool-specific-permission-rules).

## [​](https://code.claude.com/docs/en/tools-reference\#bash-tool-behavior)  Bash tool behavior

The Bash tool runs each command in a separate process with the following persistence behavior:

- Working directory persists across commands. Set `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1` to reset to the project directory after each command.
- Environment variables do not persist. An `export` in one command will not be available in the next.

Activate your virtualenv or conda environment before launching Claude Code. To make environment variables persist across Bash commands, set [`CLAUDE_ENV_FILE`](https://code.claude.com/docs/en/env-vars) to a shell script before launching Claude Code, or use a [SessionStart hook](https://code.claude.com/docs/en/hooks#persist-environment-variables) to populate it dynamically.

## [​](https://code.claude.com/docs/en/tools-reference\#powershell-tool)  PowerShell tool

On Windows, Claude Code can run PowerShell commands natively instead of routing through Git Bash. This is an opt-in preview.

### [​](https://code.claude.com/docs/en/tools-reference\#enable-the-powershell-tool)  Enable the PowerShell tool

Set `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` in your environment or in `settings.json`:

```
{
  "env": {
    "CLAUDE_CODE_USE_POWERSHELL_TOOL": "1"
  }
}
```

Claude Code auto-detects `pwsh.exe` (PowerShell 7+) with a fallback to `powershell.exe` (PowerShell 5.1). The Bash tool remains registered alongside the PowerShell tool, so you may need to ask Claude to use PowerShell.

### [​](https://code.claude.com/docs/en/tools-reference\#shell-selection-in-settings-hooks-and-skills)  Shell selection in settings, hooks, and skills

Three additional settings control where PowerShell is used:

- `"defaultShell": "powershell"` in [`settings.json`](https://code.claude.com/docs/en/settings#available-settings): routes interactive `!` commands through PowerShell. Requires the PowerShell tool to be enabled.
- `"shell": "powershell"` on individual [command hooks](https://code.claude.com/docs/en/hooks#command-hook-fields): runs that hook in PowerShell. Hooks spawn PowerShell directly, so this works regardless of `CLAUDE_CODE_USE_POWERSHELL_TOOL`.
- `shell: powershell` in [skill frontmatter](https://code.claude.com/docs/en/skills#frontmatter-reference): runs ``!`command``` blocks in PowerShell. Requires the PowerShell tool to be enabled.

### [​](https://code.claude.com/docs/en/tools-reference\#preview-limitations)  Preview limitations

The PowerShell tool has the following known limitations during the preview:

- Auto mode does not work with the PowerShell tool yet
- PowerShell profiles are not loaded
- Sandboxing is not supported
- Only supported on native Windows, not WSL
- Git Bash is still required to start Claude Code

## [​](https://code.claude.com/docs/en/tools-reference\#see-also)  See also

- [Permissions](https://code.claude.com/docs/en/permissions): permission system, rule syntax, and tool-specific patterns
- [Subagents](https://code.claude.com/docs/en/sub-agents): configure tool access for subagents
- [Hooks](https://code.claude.com/docs/en/hooks-guide): run custom commands before or after tool execution

Was this page helpful?

YesNo

[Environment variables](https://code.claude.com/docs/en/env-vars) [Interactive mode](https://code.claude.com/docs/en/interactive-mode)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.