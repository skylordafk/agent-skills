# Installing GitHub-Ops Skills

This guide explains how to add the github-ops skills to any project directory. It includes a prompt you can paste directly into your coding agent (Claude Code or Codex) to have it install the skills automatically.

## What You Get

Four skills for GitHub issue lifecycle management:

| Skill | What it does |
|-------|--------------|
| **audit** | Full-cycle issue triage and resolution with a summary report |
| **triage** | Classify `needs-triage` issues into ready-to-fix, deferred, or rejected |
| **fix-issues** | Resolve `ready-to-fix` issues with atomic commits and PRs |
| **review-pr** | Review pull requests, merge if approved, handle post-merge cleanup |

Plus five shared reference documents that the skills depend on (label taxonomy, severity definitions, quality dimensions, commit/PR format, operating principles).

## Prerequisites

- **`gh` CLI** — installed and authenticated (`gh auth status`)
- **`git`** — installed

## Agent-Executable Prompt

Copy the prompt below and paste it into your coding agent. It works in Claude Code, Codex, or any agent with shell access. The agent will clone the skill repository, copy the files into place, and clean up.

---

### Prompt: Install for both agents (Claude Code + Codex)

````
Install the github-ops AI agent skills into this project from https://github.com/skylordafk/agent-skills.git

These skills provide GitHub issue lifecycle management: audit, triage, fix-issues, and review-pr.

Follow these steps exactly:

1. Clone the repository to a temporary directory:
   ```
   git clone --depth 1 https://github.com/skylordafk/agent-skills.git /tmp/agent-skills-install
   ```

2. Create the required directories:
   ```
   mkdir -p .claude/skills .claude/references .agents/skills .agents/references
   ```

3. Copy Claude Code skills (each is a directory containing SKILL.md):
   ```
   cp -r /tmp/agent-skills-install/github-ops/claude/audit .claude/skills/audit
   cp -r /tmp/agent-skills-install/github-ops/claude/triage .claude/skills/triage
   cp -r /tmp/agent-skills-install/github-ops/claude/fix-issues .claude/skills/fix-issues
   cp -r /tmp/agent-skills-install/github-ops/claude/review-pr .claude/skills/review-pr
   ```

4. Copy Codex skills (each is a directory containing SKILL.md + agents/openai.yaml):
   ```
   cp -r /tmp/agent-skills-install/github-ops/codex/audit .agents/skills/audit
   cp -r /tmp/agent-skills-install/github-ops/codex/triage .agents/skills/triage
   cp -r /tmp/agent-skills-install/github-ops/codex/fix-issues .agents/skills/fix-issues
   cp -r /tmp/agent-skills-install/github-ops/codex/review-pr .agents/skills/review-pr
   ```

5. Copy shared references to BOTH agent directories (skills reference these via relative paths):
   ```
   cp /tmp/agent-skills-install/github-ops/references/*.md .claude/references/
   cp /tmp/agent-skills-install/github-ops/references/*.md .agents/references/
   ```

6. Clean up:
   ```
   rm -rf /tmp/agent-skills-install
   ```

7. Verify the installation by listing the installed files:
   ```
   echo "=== Claude Code ===" && ls -R .claude/skills/ .claude/references/
   echo "=== Codex ===" && ls -R .agents/skills/ .agents/references/
   ```

The final directory structure should look like:

```
.claude/
├── skills/
│   ├── audit/SKILL.md
│   ├── triage/SKILL.md
│   ├── fix-issues/SKILL.md
│   └── review-pr/SKILL.md
└── references/
    ├── commit-and-pr-format.md
    ├── four-dimensions.md
    ├── label-taxonomy.md
    ├── operating-principles.md
    └── severity-definitions.md

.agents/
├── skills/
│   ├── audit/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── triage/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   ├── fix-issues/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── review-pr/
│       ├── SKILL.md
│       └── agents/openai.yaml
└── references/
    ├── commit-and-pr-format.md
    ├── four-dimensions.md
    ├── label-taxonomy.md
    ├── operating-principles.md
    └── severity-definitions.md
```

Do not modify the skill files. The relative reference paths (../../references/) are already correct for this directory structure.
````

---

### Prompt: Install for Claude Code only

````
Install the github-ops AI agent skills for Claude Code into this project from https://github.com/skylordafk/agent-skills.git

Run these commands:
```
git clone --depth 1 https://github.com/skylordafk/agent-skills.git /tmp/agent-skills-install
mkdir -p .claude/skills .claude/references
cp -r /tmp/agent-skills-install/github-ops/claude/audit .claude/skills/audit
cp -r /tmp/agent-skills-install/github-ops/claude/triage .claude/skills/triage
cp -r /tmp/agent-skills-install/github-ops/claude/fix-issues .claude/skills/fix-issues
cp -r /tmp/agent-skills-install/github-ops/claude/review-pr .claude/skills/review-pr
cp /tmp/agent-skills-install/github-ops/references/*.md .claude/references/
rm -rf /tmp/agent-skills-install
```

Verify with: `ls -R .claude/skills/ .claude/references/`

Do not modify the skill files.
````

---

### Prompt: Install for Codex only

````
Install the github-ops AI agent skills for Codex into this project from https://github.com/skylordafk/agent-skills.git

Run these commands:
```
git clone --depth 1 https://github.com/skylordafk/agent-skills.git /tmp/agent-skills-install
mkdir -p .agents/skills .agents/references
cp -r /tmp/agent-skills-install/github-ops/codex/audit .agents/skills/audit
cp -r /tmp/agent-skills-install/github-ops/codex/triage .agents/skills/triage
cp -r /tmp/agent-skills-install/github-ops/codex/fix-issues .agents/skills/fix-issues
cp -r /tmp/agent-skills-install/github-ops/codex/review-pr .agents/skills/review-pr
cp /tmp/agent-skills-install/github-ops/references/*.md .agents/references/
rm -rf /tmp/agent-skills-install
```

Verify with: `ls -R .agents/skills/ .agents/references/`

Do not modify the skill files.
````

## Manual Installation

If you prefer to install manually without an agent:

```bash
# Clone the skill repository
git clone --depth 1 https://github.com/skylordafk/agent-skills.git /tmp/agent-skills-install

# Choose your agent(s) and run the appropriate commands above

# Clean up
rm -rf /tmp/agent-skills-install
```

## How the Reference Paths Work

Skills contain instructions like "Read `../../references/label-taxonomy.md`". The agent resolves this relative to the skill file's location:

```
.claude/skills/triage/SKILL.md
       ↑      ↑
       │      └─ first ../
       └─ second ../

Result: .claude/references/label-taxonomy.md
```

This is why references must be at `.claude/references/` (or `.agents/references/`), not inside the skills directory. The directory structure in this repo is designed so the relative paths work correctly after copying.

## Updating Skills

To update to the latest version, delete the installed skills and references, then re-run the installation prompt:

```bash
rm -rf .claude/skills/{audit,triage,fix-issues,review-pr} .claude/references/
rm -rf .agents/skills/{audit,triage,fix-issues,review-pr} .agents/references/
# Then re-run the installation prompt
```

## Using the Skills

Once installed, invoke skills by name in your agent:

**Claude Code:**
- `/audit` — run a full audit cycle
- `/triage` — classify open issues
- `/fix-issues` — fix ready-to-fix issues
- `/review-pr 123` — review a specific PR

**Codex:**
- Skills appear in the Codex skill picker
- Invoke by name when relevant to your task

All skills auto-detect the current repository via `gh repo view`. No per-project configuration is needed beyond the file installation.
