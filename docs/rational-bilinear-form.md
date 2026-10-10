# Rational bilinear form

A bilinear form is a function $B(x, y)$ of two vectors that is linear in each argument separately. Linearity in $x$ means $B(\alpha x + \beta x', y) = \alpha B(x, y) + \beta B(x', y)$, and similarly in $y$. A bilinear form is *rational* when its coefficients are rational numbers.

For example, on pairs of numbers, $B((x_1, x_2), (y_1, y_2)) = 2x_1y_1 + x_1y_2 - \tfrac{1}{2}x_2y_2$ is a rational bilinear form. Fixing $y$ makes it a linear function of $x$, and fixing $x$ makes it a linear function of $y$.

Such forms are a natural way to express a count that depends on two sets of data at once. Evaluating a bilinear form on the indicator vectors of two subsets gives a value that depends on how the subsets relate, which is the kind of quantity the paper needs.

The paper uses a rational bilinear form to express the second of the two intersection formulas in its variant of the [Frankl–Wilson construction](frankl-wilson-construction.md). Because the form has rational coefficients, its values can be computed exactly on a tape.

## Used by

- [Frankl–Wilson construction](frankl-wilson-construction.md)

## Sources

> We change the ground-set size and express the second pairing through a rational bilinear form.
>
> — Integer multiplication below n log n (OpenAI, 2026)
