# Commit and PR Format

## Commit Format

Each commit must be atomic — one logical change:

```
fix(<scope>): concise description

Resolves #<issue-number>

- What: specific code change
- Why: the defect or risk resolved
- How verified: test, build, or inspection
```

Rules:
- One logical change per commit
- Always reference the issue number
- Never use generic messages ("fix issues", "cleanup")
- Include `Resolves #N` to trigger GitHub's auto-close

## PR Template

```
## Summary
Brief description of what this PR addresses and why.

## Issues Resolved
- Closes #<number> — one-line description

## Issues Reviewed but Not Addressed
- #<number> — DEFER/REJECT — rationale

## Changes
For each file changed:
- **File:** `path/to/file` — What changed

## Verification
- [x] Latest code pulled
- [x] Tests pass
- [x] Build succeeds
- [x] No unrelated changes

## Risk
What could this break? Edge cases, deployment considerations.

## Notes for Reviewer / Future Agents
Tradeoffs considered, alternatives rejected, limitations.
```

For smaller fix PRs, the "Issues Reviewed but Not Addressed", "Risk", and "Notes" sections are optional.
