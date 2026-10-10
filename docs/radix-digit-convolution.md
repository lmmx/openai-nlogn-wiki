# Radix-digit convolution

To multiply two integers $x, y$ as in [exact integer multiplication](exact-integer-multiplication.md), let $b \ge 1$ be a digit width and write both inputs in radix $2^b$. Each input has $q = \lceil n/b \rceil$ digits, so $x = \sum_{k} a_k 2^{bk}$ and $y = \sum_{l} b_l 2^{bl}$, with each digit in $[0, 2^b)$. The digits are the coefficient lists of two polynomials in a variable $z$ with $z = 2^b$.

The product of the inputs is then the product of two polynomials evaluated at $z = 2^b$. The coefficients of the product polynomial form the [linear convolution](linear-convolution.md) of the digit lists:

$$c_j = \sum_{k + l = j} a_k b_l,$$

and $xy = \sum_j c_j 2^{bj}$. Each $c_j$ is an integer with $0 \le c_j \le q(2^b - 1)^2$. With $b = \lceil \log_2 n \rceil$ we have $q \le n \le 2^b$, which gives $c_j < 2^{3b}$, so every coefficient fits in $3b$ bits.

A small example uses $b = 2$, so the radix is $4$. Take $x = 13 = 3 \cdot 4 + 1$ and $y = 11 = 2 \cdot 4 + 3$. Written least-significant digit first, the digits are $(1, 3)$ and $(3, 2)$. The convolution gives $c_0 = 1 \cdot 3 = 3$, $c_1 = 1 \cdot 2 + 3 \cdot 3 = 11$, and $c_2 = 3 \cdot 2 = 6$. Then $3 + 11 \cdot 4 + 6 \cdot 16 = 143 = 13 \cdot 11$.

The coefficients $c_j$ can exceed $2^b$, so the final integer is obtained by propagating carries from low to high coefficients. The convolution has length at most $2q - 1$, so it can be computed as a [cyclic convolution](cyclic-convolution.md) of any length $S \ge 2q - 1$ without wraparound. This is the reduction that the rest of the algorithm accelerates.

## Prerequisites

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Linear convolution](linear-convolution.md)

## Used by

- [Precision and exact recovery](precision-and-rounding.md)
- [Multiplication algorithm](multiplication-algorithm.md)

## Sources

> Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.
>
> — Integer multiplication below n log n (OpenAI, 2026)
