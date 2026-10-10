# Chinese-remainder address map

The Chinese remainder theorem says that if $s_1, \dots, s_d$ are pairwise coprime and $S = s_1 \cdots s_d$, then the map $k \mapsto (k \bmod s_1, \dots, k \bmod s_d)$ is a bijection from $\mathbb{Z}/S\mathbb{Z}$ to $\prod_i \mathbb{Z}/s_i\mathbb{Z}$. Its consequence here is that a [cyclic convolution](cyclic-convolution.md) of length $S$ can be relabelled as a multidimensional cyclic convolution with one axis of length $s_i$ for each factor.

Take $S = 6 = 2 \cdot 3$. The map sends each index to a pair of residues:

$$0 \mapsto (0,0),\quad 1 \mapsto (1,1),\quad 2 \mapsto (0,2),\quad 3 \mapsto (1,0),\quad 4 \mapsto (0,1),\quad 5 \mapsto (1,2).$$

For example, $5 \bmod 2 = 1$ and $5 \bmod 3 = 2$. Under this relabelling, a sum over $k + l \equiv j \pmod 6$ becomes a sum over pairs of residues that add componentwise modulo $2$ and modulo $3$. So the product of two sequences of length $6$ is the same as a two-dimensional cyclic convolution of size $2 \times 3$.

The paper's map $\Phi$ from $\mathbb{C}[x]/(x^S - 1)$ to $\mathbb{C}[x_1, \dots, x_d]/(x_1^{s_1} - 1, \dots, x_d^{s_d} - 1)$ uses this split. Its constants are $P_i = \prod_{j < i} s_j$ and $\mu_i = P_i^{-1} \bmod s_i$. The paper implements the change of order as controlled cyclic shifts of the coefficient stream.

Its purpose in the algorithm is to put the radix-digit coefficients on axes whose lengths are pairwise coprime. The lengths $s_i$ are the source lengths of the transform, and the [parameter choice](parameter-choice.md) then fixes them.

## Prerequisites

- [Cyclic convolution](cyclic-convolution.md)

## Used by

- [Parameter choice](parameter-choice.md)
- [Multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting](cost-accounting.md)

## Sources

> Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution
>
> — Integer multiplication below n log n (OpenAI, 2026)
