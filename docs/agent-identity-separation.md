# Agent Identity Separation on GitHub

## Problem

Agents inherit the human operator's `gh` auth. GitHub can't distinguish human from agent actions. This breaks PR self-review restrictions, branch protection, CODEOWNERS, and audit trails.

## Goal

- Agent reviews come from a **different identity** than the PR author
- Contribution credit (green squares) stays with the **human operator**
- Different agents (Claude Code, Codex) are **distinguishable**

## Recommended Approach: GitHub Actions as Review Identity

**Commits**: Human = author (green squares). Agent name in committer field for `git blame` differentiation.

**PRs**: Created under human identity as normal.

**Reviews**: Agent triggers a `workflow_dispatch` GitHub Action. The action posts the review via `GITHUB_TOKEN`, appearing as `github-actions[bot]`. Review body includes a banner identifying the agent.

**Why this works**: Author/PR-creator = human (contribution credit). Reviewer = `github-actions[bot]` (branch protection satisfied). Per-agent differentiation via review body and committer field.

### What's needed

1. One reusable workflow YAML (`agent-review.yml`) that accepts review body + verdict as inputs
2. Skills updated to trigger `gh workflow run` instead of `gh pr review` directly
3. Committer env vars (`GIT_COMMITTER_NAME`) set per agent in skill wrappers

### Upgrade path

If per-agent **visual identity** in GitHub UI matters later, register GitHub Apps per agent type. Each shows as `agent-name[bot]` with its own avatar. The workflow YAML becomes the app's handler — incremental migration, not a rewrite.

## Alternatives Considered

| Approach | Pros | Cons |
|----------|------|------|
| Dedicated bot account | Full API separation | Consumes a seat, co-author credit less prominent |
| Per-agent GitHub Apps | True per-agent identity, no seats | Complex setup, token refresh, overkill for solo dev |
| Platform-level agent identity | Most seamless | Doesn't exist yet (as of early 2026) |
