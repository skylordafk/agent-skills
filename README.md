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

## Usage

### Symlink into a project

```bash
# Claude Code
ln -s /path/to/agent-skills/github-ops/claude/triage /path/to/project/.claude/skills/triage

# Codex
ln -s /path/to/agent-skills/github-ops/codex/triage /path/to/project/.agents/skills/triage
```

### Repository auto-detection

Skills use `gh repo view --json nameWithOwner` to detect the current repository at runtime. No per-project configuration needed — just symlink and go.

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
