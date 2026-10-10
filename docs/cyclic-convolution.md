# Cyclic convolution

For two sequences $a = (a_0, \dots, a_{S-1})$ and $b = (b_0, \dots, b_{S-1})$, the cyclic convolution $c = a * b$ is defined by

$$c_j = \sum_{\substack{k, l \\ k + l \equiv j \pmod S}} a_k b_l, \qquad 0 \le j < S.$$

Equivalently, $c$ is the product of the polynomials $a(x)$ and $b(x)$ reduced modulo $x^S - 1$. The indices wrap around modulo $S$, so the term $x^{S}$ becomes $1$ and the term $x^{S+k}$ becomes $x^k$.

Take $S = 3$, $a = (1, 2, 0)$, and $b = (0, 1, 1)$. The linear product is $(1 + 2x)(x + x^2) = x + 3x^2 + 2x^3$. Reducing with $x^3 = 1$ turns $2x^3$ into $2$, giving $c = (2, 1, 3)$. The sum formula gives the same: for example $c_2$ collects $a_0 b_2 + a_1 b_1 + a_2 b_0 = 1 + 2 + 0 = 3$.

If the linear product has degree below $S$, no term wraps, and the cyclic convolution equals the ordinary product. The paper uses this to avoid wraparound: for radix-digit polynomials of degree at most $2q - 2$, where $q$ is the number of digits of each input, the condition $2q - 2 < S$ means there is no nonzero wraparound.

Cyclic convolution is the operation that the [radix-digit reduction](radix-digit-convolution.md) produces, and the [discrete Fourier transform](discrete-fourier-transform.md) is the standard way to compute it.

## Prerequisites

- Polynomials (assumed known)

## Used by

- [Gaussian resampling](gaussian-resampling.md)
- [Chinese-remainder address map](chinese-remainder-map.md)
- [Bluestein chirp identity](bluestein-chirp-identity.md)
- [Radix-digit convolution](radix-digit-convolution.md)

## Sources

> convolution modulo xS − 1 has no nonzero wraparound
>
> — Integer multiplication below n log n (OpenAI, 2026)
