# Precision and exact recovery

The algorithm computes the [radix-digit convolution](radix-digit-convolution.md) only approximately, using fixed-precision complex arithmetic with $p$ fractional bits. Recovering the exact product requires showing that each integer coefficient is determined by its approximation.

Let $c_j$ be the exact integer coefficient and let $\tilde c_j$ be the approximated value that the algorithm computes for it. If $|\tilde c_j - c_j| < 1/2$ for every $j$, then rounding each $\tilde c_j$ to the nearest integer returns $c_j$ exactly. The paper proves this bound for its procedure: the recovered coefficient error is strictly below $1/2$. The error accumulates from truncation at each stage, so the proof tracks the precision $p$ through every transform layer. The [synthetic transform](synthetic-transform.md) stages contribute error that the paper bounds layer by layer.

Once the coefficients are integers, the integer product is obtained by carry propagation in radix $2^{b}$, the same radix as the digits of the split. Here is a worked example with the coefficients $(c_0, c_1, c_2) = (3, 11, 6)$ and radix $4$, so $b = 2$:

- Position 0: the digit is $3 \bmod 4 = 3$, carry $0$.
- Position 1: $11 = 2 \cdot 4 + 3$, so the digit is $3$ and the carry is $2$.
- Position 2: $6 + 2 = 8 = 2 \cdot 4 + 0$, so the digit is $0$ and the carry is $2$.
- Position 3: the carry $2$ is the final digit.

The digits $(3, 3, 0, 2)$ read most significant first give $2\cdot 64 + 0 + 3\cdot 4 + 3 = 143$, which is $13 \cdot 11$.

The paper's output step writes the carries and then exactly $2n$ bits in most-significant-first order, so the output has the length required by [exact integer multiplication](exact-integer-multiplication.md).

## Prerequisites

- [Radix-digit convolution](radix-digit-convolution.md)
- [Synthetic polynomial transform](synthetic-transform.md)

## Used by

- [Parameter choice](parameter-choice.md)
- [Multiplication algorithm](multiplication-algorithm.md)

## Sources

> proves that the recovered coefficient error is strictly below 1/2
>
> — Integer multiplication below n log n (OpenAI, 2026)
