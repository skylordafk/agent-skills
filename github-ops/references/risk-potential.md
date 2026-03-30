# Risk Potential

An issue deserves attention not only when something is broken, but when a pattern **constrains what the project can become** — or when it's structurally likely to cause breakage as the codebase evolves.

## Two Categories

### Latent Defects

Patterns that aren't failing now but have a known track record of producing bugs:

- Shared mutable state in concurrent paths
- Implicit ordering dependencies
- Unchecked type coercions
- Error-swallowing catch blocks
- Stringly-typed interfaces
- Silent fallbacks that mask failures

### Artificial Constraints

Design choices that unnecessarily narrow future options:

- Hardcoded assumptions in core abstractions that don't need to be hardcoded
- Tight coupling between components with no inherent reason to be coupled
- Abstractions that lock into one approach when the domain doesn't demand it
- Patterns where a simpler, more natural design would also be more open

These are not about "make everything configurable" — they target choices where the less-constrained design is also the cleaner design.

## Calibration

Three questions to distinguish genuine risk from speculative over-engineering:

1. **Is the risk structural or speculative?** Shared mutable state in a concurrent path is structural. "This function could theoretically be called with bad input" is speculative. Structural risk warrants attention; speculative risk does not.

2. **Does the constraint actually constrain?** A hardcoded value in a throwaway script isn't a real constraint. The same hardcoded value in a core abstraction that everything depends on is. Evaluate based on blast radius and centrality.

3. **Is there a simpler alternative that's also more open?** If the less-constrained design is also the cleaner design, it's a clear win. If removing the constraint requires more complexity, the tradeoff needs to justify itself against a concrete — not hypothetical — future need.
