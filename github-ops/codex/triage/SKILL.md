---
name: triage
description: Classify GitHub issues tagged needs-triage into ready-to-fix, deferred, or rejected. Quality gate between audit sweep and fix pipeline.
---

# Issue Triage — Classification & Routing

Review issues tagged `needs-triage` and classify them. You are the quality gate between audit sweep and fix pipeline.

## Repository Detection

Determine the target repository:

```bash
REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
```

If the project spans multiple repos, identify them from the project structure and triage both unless a specific repo is requested.

## Process

1. **Fetch issues:**
   ```bash
   gh issue list --repo "$REPO" --label needs-triage --state open --json number,title,body,labels
   ```

2. **Evaluate each issue:**
   - Is this real? (verify by reading the referenced code — don't trust the audit agent blindly)
   - Does it matter? (which dimension: shipability, reliability, navigability, security)
   - Is it actionable? (specific fix, completable in ~1 hour)
   - Is it a duplicate or symptom of something larger?
   - **Calibration:** assess project stage — reject theoretical risks, style nits in admin scripts, and anything requiring env compromise to exploit

3. **Classify into one disposition:**

   **→ `ready-to-fix`** — Real, scoped, actionable.
   Remove `needs-triage`, add `ready-to-fix`. Add acceptance criteria if missing.

   **→ `deferred`** — Valid but not now.
   Remove `needs-triage`, add `deferred`. Comment with reason and unblock criteria.

   **→ Close (reject)** — Not real, intentional behavior, duplicate, or style nit.
   Close with rationale comment. Add `audit-rejected`.

4. **Auto-triage rules** (apply without manual review):
   - CRITICAL + `fix` → `ready-to-fix`
   - HIGH + `fix` → `ready-to-fix`
   - Exact title match with closed issue → close as duplicate

5. **Output summary** with disposition counts and pattern notes.

## Principles

- You are the quality gate. Don't let junk into `ready-to-fix`.
- Rejection is a feature. Bad issues waste fix time.
- When in doubt, defer.
- Surface patterns — if the same low-value issue keeps appearing, note it.
- Connect the dots — group symptoms under umbrella issues.
