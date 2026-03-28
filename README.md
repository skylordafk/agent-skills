# agent-skills

Reusable AI agent skill files for Claude Code and Codex (OpenAI). Designed to be cloned once per machine and symlinked into individual project repositories.

## Structure

```
<category>/
├── claude/          # Claude Code skills (.claude/skills/ format)
│   └── <skill>/SKILL.md
└── codex/           # Codex skills (.agents/skills/ format)
    └── <skill>/
        ├── SKILL.md
        └── agents/openai.yaml
```

## Categories

### `github-ops/`

GitHub issue lifecycle skills — audit, triage, fix, and review.

| Skill | Purpose |
|-------|---------|
| `audit` | Full-cycle: triage all open audit issues, resolve actionable ones, produce report |
| `triage` | Classify `needs-triage` issues into ready-to-fix, deferred, or rejected |
| `fix-issues` | Resolve `ready-to-fix` issues with atomic commits and PRs |
| `review-pr` | Review PRs, merge if approved, handle post-merge hygiene |

## Installation

See the **[Installation Guide](docs/installation.md)** for full instructions, including a **copy-paste prompt** you can give to your coding agent to have it install the skills automatically.

**Quick start — paste this into your agent:**

> Install the github-ops AI agent skills into this project from https://github.com/skylordafk/agent-skills.git — clone it to /tmp, copy Claude Code skills to .claude/skills/, Codex skills to .agents/skills/, and shared references to both .claude/references/ and .agents/references/. Then clean up the clone and verify with ls -R.

### Repository auto-detection

Skills use `gh repo view --json nameWithOwner` to detect the current repository at runtime. No per-project configuration needed — just install and go.

## Adding new skills

1. Create a new category directory (or use an existing one)
2. Add `claude/` and/or `codex/` subdirectories
3. Write `SKILL.md` files following each agent's format conventions
4. For Codex skills, include `agents/openai.yaml` with invocation policy

## Agent format differences

| Feature | Claude Code | Codex |
|---------|-------------|-------|
| Location | `.claude/skills/<name>/SKILL.md` | `.agents/skills/<name>/SKILL.md` |
| Frontmatter | `name`, `description`, `argument-hint`, `allowed-tools`, `disable-model-invocation` | `name`, `description` |
| Arguments | `$ARGUMENTS` variable | Passed via invocation context |
| Config sidecar | None | `agents/openai.yaml` |
