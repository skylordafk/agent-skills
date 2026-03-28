---
name: fix-issues
description: Resolve triaged GitHub audit issues tagged ready-to-fix. Implements fixes with atomic commits and submits a PR. Do not invoke implicitly.
---

# Fix Issues — Audit Issue Resolution

You are resolving GitHub issues from automated code audits. Work surgically, document thoroughly.

## Repository Detection

```bash
REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
```

Use `$REPO` for all `gh` commands below.

## Step 1: Find Issues

```bash
gh issue list --repo "$REPO" --label ready-to-fix --state open --json number,title,body,labels
```

If no `ready-to-fix` issues exist, check `needs-triage`:
```bash
gh issue list --repo "$REPO" --label needs-triage --state open --json number,title,body,labels
```

## Step 2: Select 3–5 Issues

- **Group related issues** affecting the same file/module into one PR
- **Prioritize:** security > reliability > shipability > navigability
- **Confidence matters.** If you're not sure about the fix, skip it.
- **Check for dependencies.** If issue A must be fixed before B, take A.

## Step 3: Implement

**Branch:**
```bash
git checkout -b fix/issue-<NUM>-<short-desc>
```

**Commits — atomic, one logical change each:**
```
fix(scope): description (#<issue-number>)

- What: specific code change
- Why: the defect or risk resolved
- How verified: test, build, or inspection
```

Rules:
- One logical change per commit
- Reference the issue number in every commit
- Never use generic messages ("fix issues", "cleanup")

**Build check:**
```bash
npm run build
```
Fix any errors before proceeding.

## Step 4: Submit PR

```bash
gh pr create --repo "$REPO" \
  --title "[Audit Fix] <concise summary>" \
  --body "## Summary
What this PR addresses. Dimension improved: <shipability/reliability/navigability/security>.

## Issues Resolved
- Closes #<number> — one-line description

## Changes
For each file:
- **File:** \`path/to/file\`
- **What changed:** Description

## Verification
- [x] \`npm run build\` succeeds
- [x] No unrelated changes
- [x] All resolved issues have \`Closes #XX\`

## Notes for Reviewer
Tradeoffs, alternatives rejected, limitations."
```

## Step 5: Update Labels

```bash
gh issue edit <NUMBER> --repo "$REPO" --add-label in-progress --remove-label ready-to-fix
```

## Standards

### Severity
- **critical** — data loss, security breach, total breakage possible now
- **high** — breaks under real usage or blocks shipping
- **medium** — degrades quality or blocks future work
- **low** — cleanup, nice-to-have

### The Four Dimensions (Ideal State)
1. **Shipability** — can you add a feature in one session?
2. **Reliability** — is anything silently broken?
3. **Navigability** — can agents navigate the codebase?
4. **Security** — does protection match exposure?

## Principles

1. **Fewer, better fixes.** 3 solid fixes beat 10 sloppy ones.
2. **If not confident, skip it.** A wrong fix is worse than an open issue.
3. **Document for the next agent.** They've never seen this codebase.
4. **Every fix moves toward ideal state.** Say which dimension.
