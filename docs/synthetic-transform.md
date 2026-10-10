# Synthetic polynomial transform

A synthetic polynomial transform is a discrete Fourier-type transform whose roots of unity are powers of $y$ in the [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md). Multiplying by $y^k$ only shifts coefficients and changes some signs, so each stage of the transform is made of address rearrangements, signed shifts, and two-point butterfly operations.

The paper credits this construction to Nussbaumer and to Quandalle and Nussbaumer. Its role here is to evaluate the transforms of the convolution on the axis that is stored as a polynomial modulo $y^r + 1$, so that the roots of unity on that axis are shifts.

Take $r = 4$ and a coefficient list $(a_0, a_1, a_2, a_3)$. Multiplying by $y$ gives $(-a_3, a_0, a_1, a_2)$, as in the ring page. Multiplying by $y^2$ applies this twice, giving $(-a_2, -a_3, a_0, a_1)$. Both are a shift followed by sign changes, which costs no multiplications.

A butterfly on two records $u$ and $v$ has the form $(u + v, u - v)$, up to a scaling by $1/2$. Combining shifts and butterflies in layers gives a transform of polynomial length. Each butterfly is invertible, since $(s, t) \mapsto (s + t, s - t)$ undoes $(u, v) \mapsto (u+v, u-v)$ up to a factor of $2$, so the layers can be undone in reverse order.

In the paper, the transform is computed in simultaneous layers on a tape. The cost of each layer is governed by the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) procedure, which controls how these transforms are applied on a fixed number of tapes.

## Prerequisites

- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)

## Used by

- [Precision and exact recovery](precision-and-rounding.md)
- [Multiplication algorithm](multiplication-algorithm.md)

## Sources

> These are the synthetic polynomial transforms of Nussbaumer and Quandalle and
>
> — Integer multiplication below n log n (OpenAI, 2026)
