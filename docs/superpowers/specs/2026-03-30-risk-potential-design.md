# Risk Potential — Design Spec

**Date:** 2026-03-30

## Problem

The audit and triage skills currently evaluate issues on two axes: "is this real?" and "is this scoped enough to fix?" Issues that aren't broken today but represent structurally risky patterns or unnecessary constraints on the project's future get bounced as "over-engineered," "overkill," or "noise." With agents checking each other's work and sufficient token budgets to be thorough, there's an opportunity to catch these hazards proactively rather than waiting for them to manifest as bugs.

## Core Concept

An issue deserves attention not only when something is broken, but when a pattern **constrains what the project can become** — or when it's structurally likely to cause breakage as the codebase evolves.

This is a "risk trajectory" lens: not "is this failing a test?" but "is this the kind of thing that breeds failures, or that narrows options unnecessarily?"

## Deliverables

### 1. Shared Reference: `references/risk-potential.md`

A new reference document (alongside `four-dimensions.md`, `severity-definitions.md`, etc.) defining the framework.

#### Two Categories of Risk Potential

**Latent defects** — patterns that aren't failing now but have a known track record of producing bugs:
- Shared mutable state in concurrent paths
- Implicit ordering dependencies
- Unchecked type coercions
- Error-swallowing catch blocks
- Stringly-typed interfaces
- Silent fallbacks that mask failures

**Artificial constraints** — design choices that unnecessarily narrow future options:
- Hardcoded assumptions in core abstractions that don't need to be hardcoded
- Tight coupling between components with no inherent reason to be coupled
- Abstractions that lock into one approach when the domain doesn't demand it
- Patterns where a simpler, more natural design would also be more open

These are not about "make everything configurable" — they target choices where the less-constrained design is also the cleaner design.

#### Calibration Guide

Three questions to distinguish genuine risk from speculative over-engineering:

1. **Is the risk structural or speculative?** Shared mutable state in a concurrent path is structural. "This function could theoretically be called with bad input" is speculative. Structural risk warrants attention; speculative risk does not.

2. **Does the constraint actually constrain?** A hardcoded value in a throwaway script isn't a real constraint. The same hardcoded value in a core abstraction that everything depends on is. Evaluate based on the blast radius and centrality of the code.

3. **Is there a simpler alternative that's also more open?** If the less-constrained design is also the cleaner design, it's a clear win. If removing the constraint requires more complexity, the tradeoff needs to justify itself against a concrete (not hypothetical) future need.

### 2. Audit Skill Changes

#### A. New Disposition: HAZARD

Added to the classification system alongside ACTIONABLE, DEFER, REJECT, CONSOLIDATE:

> **HAZARD** — Not broken today, but the pattern is structurally fragile or unnecessarily constrains the project's future.
> - The risk is structural, not speculative (see risk-potential framework)
> - A simpler or more natural design would also be more open
> - Worth addressing proactively rather than waiting for it to bite

HAZARD issues enter the pipeline as real work. In Step 4 (selecting the working set), they slot into the priority order:

**security > correctness > hazard > reliability > architecture > maintainability > style**

#### B. Optional Proactive Phase: Risk Reconnaissance

A new phase between Phase 1 (Triage) and Phase 2 (Resolution), triggered by the `--risk-scan` flag.

**Scope:** The agent examines the areas of the codebase already touched by audit issues. If the audit sweep flagged three issues in `src/auth/`, the risk reconnaissance also examines `src/auth/` for latent defects and artificial constraints that the sweep missed. The audit sweep's coverage area becomes the search space — proactive but not unbounded.

**Output:** New findings become issues labeled `audit` + `needs-triage`, with a `risk:hazard` marker so triage knows their origin.

**When not flagged:** The `--risk-scan` phase is skipped entirely. Standard audit flow proceeds unchanged.

### 3. Triage Skill Changes

#### A. New Evaluation Question: "What's the risk trajectory?"

Added to Step 2's evaluation sequence, after "Does it matter?" and before "Is it actionable?":

> **What's the risk trajectory?**
> - Read `../../references/risk-potential.md` for the framework.
> - Is this a latent defect — a pattern with a known track record of producing bugs?
> - Is this an artificial constraint — a design choice that unnecessarily narrows future options?
> - If neither, move on. If either, this is a valid reason the issue deserves attention regardless of whether it's "broken" today.

#### B. Risk Potential as a Promotion Path

The existing disposition buckets (ready-to-fix, deferred, rejected) don't change. What changes is what qualifies for them:

- An issue that would otherwise be rejected as "over-engineered/overkill" or "too small/noise" can be promoted to `ready-to-fix` if it has genuine risk potential per the framework.
- The calibration criteria (structural vs. speculative, real constraint vs. theoretical) are the gatekeeper that prevents this from becoming a firehose.

#### C. No Auto-Triage for Hazard Issues

Hazard issues require judgment by nature — evaluating whether risk is real or theoretical cannot be automated. Issues with the `risk:hazard` marker always go through manual review regardless of severity level.

## Files Changed

| File | Change |
|------|--------|
| `references/risk-potential.md` | New file — shared risk potential framework |
| `claude/audit/SKILL.md` | Add HAZARD disposition, add `--risk-scan` phase |
| `codex/audit/SKILL.md` | Mirror changes for Codex variant |
| `claude/triage/SKILL.md` | Add risk trajectory evaluation, promotion path, no-auto-triage rule |
| `codex/triage/SKILL.md` | Mirror changes for Codex variant |
| `references/label-taxonomy.md` | Add `risk:hazard` label to taxonomy + bootstrap script |

## Out of Scope

- Standalone "risk scan" skill (could be a future evolution if `--risk-scan` proves valuable enough to run independently)
- Changes to fix-issues or review-pr skills (they already handle whatever triage promotes to ready-to-fix)
- New labels beyond `risk:hazard` (using existing label infrastructure)
