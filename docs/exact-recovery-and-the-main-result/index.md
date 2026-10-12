# Exact recovery and the main result

This part closes the argument. [Rounding recovery](../rounding-recovery.md "The step in which the approximate convolution coefficients are rounded to integers, provided the error is strictly below 1/2, and carries are then propagated to give the exact binary product.") shows that the coefficient error is below $1/2$, so rounding and carries give the exact binary product. [The target page](../integer-multiplication-target.md "A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.") then assembles the earlier pages into the $O(n(\lg n)^{1-\kappa})$ bound and states the result in full.

## Pages

1. [Exact recovery by rounding](../rounding-recovery.md "The step in which the approximate convolution coefficients are rounded to integers, provided the error is strictly below 1/2, and carries are then propagated to give the exact binary product.") — The step in which the approximate convolution coefficients are rounded to integers, provided the error is strictly below 1/2, and carries are then propagated to give the exact binary product.
2. [Integer multiplication in O(n(lg n)^(1-κ)) time](../integer-multiplication-target.md "A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.") — A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.

## Map

Arrows point from a page to the pages that build on it.

```mermaid
flowchart LR
  n0["Exact recovery by rounding"]
  click n0 href "../rounding-recovery/" "The step in which the approximate convolution coefficients are rounded to integers, provided the error is strictly below 1/2, and carries are then propagated to give the exact binary product."
  n1["Integer multiplication in O(n(lg n)^(1-κ)) time"]
  click n1 href "../integer-multiplication-target/" "A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model."
  n0 --> n1
```
