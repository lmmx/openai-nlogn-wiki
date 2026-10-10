# Simultaneous butterfly layer

A two-point butterfly acts on a pair of values $u, v$ by the map

$$H_0(u, v) = \left(\frac{u + v}{2},\ \frac{u - v}{2}\right).$$

For example, $H_0(3, 1) = (2, 1)$. The map is linear, and its inverse is $(s, t) \mapsto (s + t, s - t)$, so applying it twice gives back the original pair up to a factor of $2$.

On a [multitape Turing machine](turing-machine-model.md), a butterfly layer applies $H_0$ to many pairs at once. In the paper, a pair is selected by fixing one address bit: the two entries whose addresses differ only in that bit are combined. A *simultaneous* layer selects the same bit position in each of at most $d$ equal-width address chunks, and applies the butterfly to all selected pairs in one pass over the data.

The cost of a single simultaneous layer on an array of logical bit volume $V$ (the number of stored data bits) is $O(V d^{\lambda'})$, for a fixed exponent $\lambda' < 1$. Separate butterfly factors, applied one at a time, would need a whole-array pass for each factor. The simultaneous layer avoids that, and this is what makes the layered transform fast.

The values are not stored as bits. Each [record](record.md) is a polynomial with complex fixed-point coefficients, and $H_0$ acts on each coefficient. Intermediate values are exact [Gaussian dyadic numbers](gaussian-dyadic.md), and a single rounding (truncation) happens after the complete layer. The paper bounds the resulting coefficient error by about $2\sqrt{2}\cdot 2^{-p}$, where $p$ is the number of fractional bits kept in each coefficient.

The layer is the arithmetic primitive used in the [synthetic transform](synthetic-transform.md). It is implemented by the same [linear network](linear-network-frames.md) technique as the [address-field interchange](address-interchange.md).

## Prerequisites

- [Multitape Turing machine](turing-machine-model.md)
- Complex numbers (assumed known)
- [Gaussian dyadic numbers](gaussian-dyadic.md)

## Used by

- [Multiplication algorithm](multiplication-algorithm.md)
- [Recursive rank saving](rank-saving-recursion.md)

## Sources

> The second procedure applies
>
> — Integer multiplication below n log n (OpenAI, 2026)
