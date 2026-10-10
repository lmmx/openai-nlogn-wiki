A synthetic polynomial transform is a discrete Fourier-type transform whose roots of unity are powers of $y$ in the [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md). Multiplying by $y^k$ only shifts coefficients and changes some signs, so each stage of the transform is made of address rearrangements, signed shifts, and two-point butterfly operations.

The paper credits this construction to Nussbaumer and to Quandalle and Nussbaumer. Its role here is to evaluate the transforms of the convolution on the axes that carry a polynomial coordinate.

Take $r = 4$ and a coefficient list $(a_0, a_1, a_2, a_3)$. Multiplying by $y$ gives $(-a_3, a_0, a_1, a_2)$, as in the ring page. Multiplying by $y^2$ applies this twice, giving $(-a_2, -a_3, a_0, a_1)$. Both are a shift followed by sign changes, which costs no multiplications.

A butterfly on two records $u$ and $v$ has the form $(u + v, u - v)$, possibly with a shift applied to one input first. Combining shifts and butterflies in layers gives a transform of polynomial length, and the same layers run in reverse to invert it.

In the paper, the transform is computed in simultaneous layers on a tape. The cost of each layer is governed by the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) procedure, which is the reason these transforms can be applied on a fixed number of tapes.
