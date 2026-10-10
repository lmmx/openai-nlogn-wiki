# Discrete Fourier transform

Let $N \ge 1$ and let $\omega$ be a primitive $N$-th root of unity, so $\omega^N = 1$ and $\omega^k \ne 1$ for $0 < k < N$. The discrete Fourier transform (DFT) of a sequence $(a_0, \dots, a_{N-1})$ is the sequence $(\hat a_0, \dots, \hat a_{N-1})$ with

$$\hat a_k = \sum_{j=0}^{N-1} a_j\, \omega^{jk}.$$

Each output is a linear combination of the inputs, so the DFT is a linear map. Computed directly it costs about $N^2$ operations. Fast algorithms reduce this to about $N\log N$.

The reason the DFT matters here is the convolution theorem. The cyclic convolution of two sequences, defined in [cyclic convolution](cyclic-convolution.md), becomes a pointwise product after the DFT. So one can convolve by transforming both inputs, multiplying coefficient by coefficient, and applying the inverse transform.

A small example has $N = 2$ and $\omega = -1$. The DFT is $(a_0, a_1) \mapsto (a_0 + a_1, \ a_0 - a_1)$. Applying it twice gives $(2a_0, 2a_1)$, so the inverse is the same map followed by division by $N = 2$.

Multiplication by $\omega$ is an ordinary complex multiplication. In the paper, the DFTs needed for multiplication are replaced by transforms whose axis lengths are powers of two, and the transforms are evaluated with roots of unity that are powers of $y$ in a polynomial ring. For such roots, multiplying a coefficient list by a root is a shift with sign changes, which is cheap on a tape; the [synthetic transform](synthetic-transform.md) page explains this.

## Prerequisites

- Complex numbers (assumed known)

## Used by

- [Gaussian resampling](gaussian-resampling.md)
- [Middle transform](middle-transform.md)

## Sources

> Fourier transforms needed for this convolution
>
> — Integer multiplication below n log n (OpenAI, 2026)
