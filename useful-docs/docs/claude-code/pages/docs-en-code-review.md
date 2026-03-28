# Code Review - Claude Code Docs

> Source: https://code.claude.com/docs/en/code-review

[Skip to main content](https://code.claude.com/docs/en/code-review#content-area)

[Claude Code Docs home page![light logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/light.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=78fd01ff4f4340295a4f66e2ea54903c)![dark logo](https://mintcdn.com/claude-code/c5r9_6tjPMzFdDDT/logo/dark.svg?fit=max&auto=format&n=c5r9_6tjPMzFdDDT&q=85&s=1298a0c3b3a1da603b190d0de0e31712)](https://code.claude.com/docs/en/overview)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

Ctrl KAsk AI

Search...

Navigation

Code review & CI/CD

Code Review

[Getting started](https://code.claude.com/docs/en/overview) [Build with Claude Code](https://code.claude.com/docs/en/sub-agents) [Deployment](https://code.claude.com/docs/en/third-party-integrations) [Administration](https://code.claude.com/docs/en/setup) [Configuration](https://code.claude.com/docs/en/settings) [Reference](https://code.claude.com/docs/en/cli-reference) [Resources](https://code.claude.com/docs/en/legal-and-compliance)

On this page

- [How reviews work](https://code.claude.com/docs/en/code-review#how-reviews-work)
- [Severity levels](https://code.claude.com/docs/en/code-review#severity-levels)
- [Check run output](https://code.claude.com/docs/en/code-review#check-run-output)
- [What Code Review checks](https://code.claude.com/docs/en/code-review#what-code-review-checks)
- [Set up Code Review](https://code.claude.com/docs/en/code-review#set-up-code-review)
- [Manually trigger reviews](https://code.claude.com/docs/en/code-review#manually-trigger-reviews)
- [Customize reviews](https://code.claude.com/docs/en/code-review#customize-reviews)
- [CLAUDE.md](https://code.claude.com/docs/en/code-review#claude-md)
- [REVIEW.md](https://code.claude.com/docs/en/code-review#review-md)
- [View usage](https://code.claude.com/docs/en/code-review#view-usage)
- [Pricing](https://code.claude.com/docs/en/code-review#pricing)
- [Related resources](https://code.claude.com/docs/en/code-review#related-resources)

Code Review is in research preview, available for [Teams and Enterprise](https://claude.ai/admin-settings/claude-code) subscriptions. It is not available for organizations with [Zero Data Retention](https://code.claude.com/docs/en/zero-data-retention) enabled.

Code Review analyzes your GitHub pull requests and posts findings as inline comments on the lines of code where it found issues. A fleet of specialized agents examine the code changes in the context of your full codebase, looking for logic errors, security vulnerabilities, broken edge cases, and subtle regressions.Findings are tagged by severity and don’t approve or block your PR, so existing review workflows stay intact. You can tune what Claude flags by adding a `CLAUDE.md` or `REVIEW.md` file to your repository.To run Claude in your own CI infrastructure instead of this managed service, see [GitHub Actions](https://code.claude.com/docs/en/github-actions) or [GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd).This page covers:

- [How reviews work](https://code.claude.com/docs/en/code-review#how-reviews-work)
- [Setup](https://code.claude.com/docs/en/code-review#set-up-code-review)
- [Triggering reviews manually](https://code.claude.com/docs/en/code-review#manually-trigger-reviews) with `@claude review` and `@claude review once`
- [Customizing reviews](https://code.claude.com/docs/en/code-review#customize-reviews) with `CLAUDE.md` and `REVIEW.md`
- [Pricing](https://code.claude.com/docs/en/code-review#pricing)

## [​](https://code.claude.com/docs/en/code-review\#how-reviews-work)  How reviews work

Once an admin [enables Code Review](https://code.claude.com/docs/en/code-review#set-up-code-review) for your organization, reviews trigger when a PR opens, on every push, or when manually requested, depending on the repository’s configured behavior. Commenting `@claude review` [starts reviews on a PR](https://code.claude.com/docs/en/code-review#manually-trigger-reviews) in any mode.When a review runs, multiple agents analyze the diff and surrounding code in parallel on Anthropic infrastructure. Each agent looks for a different class of issue, then a verification step checks candidates against actual code behavior to filter out false positives. The results are deduplicated, ranked by severity, and posted as inline comments on the specific lines where issues were found. If no issues are found, Claude posts a short confirmation comment on the PR.Reviews scale in cost with PR size and complexity, completing in 20 minutes on average. Admins can monitor review activity and spend via the [analytics dashboard](https://code.claude.com/docs/en/code-review#view-usage).

### [​](https://code.claude.com/docs/en/code-review\#severity-levels)  Severity levels

Each finding is tagged with a severity level:

| Marker | Severity | Meaning |
| --- | --- | --- |
| 🔴 | Important | A bug that should be fixed before merging |
| 🟡 | Nit | A minor issue, worth fixing but not blocking |
| 🟣 | Pre-existing | A bug that exists in the codebase but was not introduced by this PR |

Findings include a collapsible extended reasoning section you can expand to understand why Claude flagged the issue and how it verified the problem.

### [​](https://code.claude.com/docs/en/code-review\#check-run-output)  Check run output

Beyond the inline review comments, each review populates the **Claude Code Review** check run that appears alongside your CI checks. Expand its **Details** link to see a summary of every finding in one place, sorted by severity:

| Severity | File:Line | Issue |
| --- | --- | --- |
| 🔴 Important | `src/auth/session.ts:142` | Token refresh races with logout, leaving stale sessions active |
| 🟡 Nit | `src/auth/session.ts:88` | `parseExpiry` silently returns 0 on malformed input |

Each finding also appears as an annotation in the **Files changed** tab, marked directly on the relevant diff lines. Important findings render with a red marker, nits with a yellow warning, and pre-existing bugs with a gray notice.The check run always completes with a neutral conclusion so it never blocks merging through branch protection rules. If you want to gate merges on Code Review findings, read the severity breakdown from the check run output in your own CI. The last line of the Details text is a machine-readable comment your workflow can parse with `gh` and jq:

```
gh api repos/OWNER/REPO/check-runs/CHECK_RUN_ID \
  --jq '.output.text | split("bughunter-severity: ")[1] | split(" -->")[0] | fromjson'
```

This returns a JSON object with counts per severity, for example `{"normal": 2, "nit": 1, "pre_existing": 0}`. The `normal` key holds the count of Important findings; a non-zero value means Claude found at least one bug worth fixing before merge.

### [​](https://code.claude.com/docs/en/code-review\#what-code-review-checks)  What Code Review checks

By default, Code Review focuses on correctness: bugs that would break production, not formatting preferences or missing test coverage. You can expand what it checks by [adding guidance files](https://code.claude.com/docs/en/code-review#customize-reviews) to your repository.

## [​](https://code.claude.com/docs/en/code-review\#set-up-code-review)  Set up Code Review

An admin enables Code Review once for the organization and selects which repositories to include.

1

[Navigate to header](https://code.claude.com/docs/en/code-review#)

Open Claude Code admin settings

Go to [claude.ai/admin-settings/claude-code](https://claude.ai/admin-settings/claude-code) and find the Code Review section. You need admin access to your Claude organization and permission to install GitHub Apps in your GitHub organization.

2

[Navigate to header](https://code.claude.com/docs/en/code-review#)

Start setup

Click **Setup**. This begins the GitHub App installation flow.

3

[Navigate to header](https://code.claude.com/docs/en/code-review#)

Install the Claude GitHub App

Follow the prompts to install the Claude GitHub App to your GitHub organization. The app requests these repository permissions:

- **Contents**: read and write
- **Issues**: read and write
- **Pull requests**: read and write

Code Review uses read access to contents and write access to pull requests. The broader permission set also supports [GitHub Actions](https://code.claude.com/docs/en/github-actions) if you enable that later.

4

[Navigate to header](https://code.claude.com/docs/en/code-review#)

Select repositories

Choose which repositories to enable for Code Review. If you don’t see a repository, make sure you gave the Claude GitHub App access to it during installation. You can add more repositories later.

5

[Navigate to header](https://code.claude.com/docs/en/code-review#)

Set review triggers per repo

After setup completes, the Code Review section shows your repositories in a table. For each repository, use the **Review Behavior** dropdown to choose when reviews run:

- **Once after PR creation**: review runs once when a PR is opened or marked ready for review
- **After every push**: review runs on every push to the PR branch, catching new issues as the PR evolves and auto-resolving threads when you fix flagged issues
- **Manual**: reviews start only when someone [comments `@claude review` or `@claude review once` on a PR](https://code.claude.com/docs/en/code-review#manually-trigger-reviews); `@claude review` also subscribes the PR to reviews on subsequent pushes

Reviewing on every push runs the most reviews and costs the most. Manual mode is useful for high-traffic repos where you want to opt specific PRs into review, or to only start reviewing your PRs once they’re ready.

The repositories table also shows the average cost per review for each repo based on recent activity. Use the row actions menu to turn Code Review on or off per repository, or to remove a repository entirely.To verify setup, open a test PR. If you chose an automatic trigger, a check run named **Claude Code Review** appears within a few minutes. If you chose Manual, comment `@claude review` on the PR to start the first review. If no check run appears, confirm the repository is listed in your admin settings and the Claude GitHub App has access to it.

## [​](https://code.claude.com/docs/en/code-review\#manually-trigger-reviews)  Manually trigger reviews

Two comment commands start a review on demand. Both work regardless of the repository’s configured trigger, so you can use them to opt specific PRs into review in Manual mode or to get an immediate re-review in other modes.

| Command | What it does |
| --- | --- |
| `@claude review` | Starts a review and subscribes the PR to push-triggered reviews going forward |
| `@claude review once` | Starts a single review without subscribing the PR to future pushes |

Use `@claude review once` when you want feedback on the current state of a PR but don’t want every subsequent push to incur a review. This is useful for long-running PRs with frequent pushes, or when you want a one-off second opinion without changing the PR’s review behavior.For either command to trigger a review:

- Post it as a top-level PR comment, not an inline comment on a diff line
- Put the command at the start of the comment, with `once` on the same line if you’re using the one-shot form
- You must have owner, member, or collaborator access to the repository
- The PR must be open

Unlike automatic triggers, manual triggers run on draft PRs, since an explicit request signals you want the review now regardless of draft status.If a review is already running on that PR, the request is queued until the in-progress review completes. You can monitor progress via the check run on the PR.

## [​](https://code.claude.com/docs/en/code-review\#customize-reviews)  Customize reviews

Code Review reads two files from your repository to guide what it flags. Both are additive on top of the default correctness checks:

- **`CLAUDE.md`**: shared project instructions that Claude Code uses for all tasks, not just reviews. Use it when guidance also applies to interactive Claude Code sessions.
- **`REVIEW.md`**: review-only guidance, read exclusively during code reviews. Use it for rules that are strictly about what to flag or skip during review and would clutter your general `CLAUDE.md`.

### [​](https://code.claude.com/docs/en/code-review\#claude-md)  CLAUDE.md

Code Review reads your repository’s `CLAUDE.md` files and treats newly-introduced violations as nit-level findings. This works bidirectionally: if your PR changes code in a way that makes a `CLAUDE.md` statement outdated, Claude flags that the docs need updating too.Claude reads `CLAUDE.md` files at every level of your directory hierarchy, so rules in a subdirectory’s `CLAUDE.md` apply only to files under that path. See the [memory documentation](https://code.claude.com/docs/en/memory) for more on how `CLAUDE.md` works.For review-specific guidance that you don’t want applied to general Claude Code sessions, use [`REVIEW.md`](https://code.claude.com/docs/en/code-review#review-md) instead.

### [​](https://code.claude.com/docs/en/code-review\#review-md)  REVIEW.md

Add a `REVIEW.md` file to your repository root for review-specific rules. Use it to encode:

- Company or team style guidelines: “prefer early returns over nested conditionals”
- Language- or framework-specific conventions not covered by linters
- Things Claude should always flag: “any new API route must have an integration test”
- Things Claude should skip: “don’t comment on formatting in generated code under `/gen/`”

Example `REVIEW.md`:

```
# Code Review Guidelines

## Always check
- New API endpoints have corresponding integration tests
- Database migrations are backward-compatible
- Error messages don't leak internal details to users

## Style
- Prefer `match` statements over chained `isinstance` checks
- Use structured logging, not f-string interpolation in log calls

## Skip
- Generated files under `src/gen/`
- Formatting-only changes in `*.lock` files
```

Claude auto-discovers `REVIEW.md` at the repository root. No configuration needed.

## [​](https://code.claude.com/docs/en/code-review\#view-usage)  View usage

Go to [claude.ai/analytics/code-review](https://claude.ai/analytics/code-review) to see Code Review activity across your organization. The dashboard shows:

| Section | What it shows |
| --- | --- |
| PRs reviewed | Daily count of pull requests reviewed over the selected time range |
| Cost weekly | Weekly spend on Code Review |
| Feedback | Count of review comments that were auto-resolved because a developer addressed the issue |
| Repository breakdown | Per-repo counts of PRs reviewed and comments resolved |

The repositories table in admin settings also shows average cost per review for each repo.

## [​](https://code.claude.com/docs/en/code-review\#pricing)  Pricing

Code Review is billed based on token usage. Each review averages $15-25 in cost, scaling with PR size, codebase complexity, and how many issues require verification. Code Review usage is billed separately through [extra usage](https://support.claude.com/en/articles/12429409-extra-usage-for-paid-claude-plans) and does not count against your plan’s included usage.The review trigger you choose affects total cost:

- **Once after PR creation**: runs once per PR
- **After every push**: runs on each push, multiplying cost by the number of pushes
- **Manual**: no reviews until someone comments `@claude review` on a PR

In any mode, commenting `@claude review` [opts the PR into push-triggered reviews](https://code.claude.com/docs/en/code-review#manually-trigger-reviews), so additional cost accrues per push after that comment. To run a single review without subscribing to future pushes, comment `@claude review once` instead.Costs appear on your Anthropic bill regardless of whether your organization uses AWS Bedrock or Google Vertex AI for other Claude Code features. To set a monthly spend cap for Code Review, go to [claude.ai/admin-settings/usage](https://claude.ai/admin-settings/usage) and configure the limit for the Claude Code Review service.Monitor spend via the weekly cost chart in [analytics](https://code.claude.com/docs/en/code-review#view-usage) or the per-repo average cost column in admin settings.

## [​](https://code.claude.com/docs/en/code-review\#related-resources)  Related resources

Code Review is designed to work alongside the rest of Claude Code. If you want to run reviews locally before opening a PR, need a self-hosted setup, or want to go deeper on how `CLAUDE.md` shapes Claude’s behavior across tools, these pages are good next stops:

- [Plugins](https://code.claude.com/docs/en/discover-plugins): browse the plugin marketplace, including a `code-review` plugin for running on-demand reviews locally before pushing
- [GitHub Actions](https://code.claude.com/docs/en/github-actions): run Claude in your own GitHub Actions workflows for custom automation beyond code review
- [GitLab CI/CD](https://code.claude.com/docs/en/gitlab-ci-cd): self-hosted Claude integration for GitLab pipelines
- [Memory](https://code.claude.com/docs/en/memory): how `CLAUDE.md` files work across Claude Code
- [Analytics](https://code.claude.com/docs/en/analytics): track Claude Code usage beyond code review

Was this page helpful?

YesNo

[JetBrains IDEs](https://code.claude.com/docs/en/jetbrains) [GitHub Actions](https://code.claude.com/docs/en/github-actions)

Ctrl+I

Assistant

Responses are generated using AI and may contain mistakes.