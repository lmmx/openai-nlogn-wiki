# Gaussian resampling

Gaussian resampling is the step that replaces a [discrete Fourier transform](discrete-fourier-transform.md) of a length that is not a power of two by a transform whose axes all have power-of-two lengths. The idea is to move values between two grids of different sizes, so that the transform matches the wraparound structure of a [cyclic convolution](cyclic-convolution.md). The paper adapts the identity of Harvey and van der Hoeven.

Let $s < t$ be coprime integers. A length-$s$ grid and a length-$t$ grid are related by two coordinate permutations. The paper defines them as $(P_s u)_j = u_{tj}$ and $(P_t v)_k = v_{-sk}$, where indices are taken modulo the length. When $\gcd(s,t) = 1$, the map $j \mapsto tj \bmod s$ is a bijection.

For a small case, take $s = 3$ and $t = 4$. The map $j \mapsto 4j \bmod 3$ sends $0, 1, 2$ to $0, 1, 2$, so it is a permutation. The gcd condition is what makes this hold in general.

The resampling itself uses two [linear contractions](linear-contraction.md), $A : \mathbb{C}^s \to \mathbb{C}^t$ and $B_0 : \mathbb{C}^t \to \mathbb{C}^s$, which are approximations of exact maps between the two grids, with an error the paper bounds. The paper's analysis requires the ratio $t/s$ to be far enough from $1$ that the approximation error is small: the condition is $\theta = t/s - 1 > p/\alpha^4$, where $p$ is the precision and $\alpha$ is an auxiliary integer parameter. This is what allows the approximate resampling to use a fixed number of bits.

The payoff is that each source Fourier transform can be expressed through a transform whose axes have power-of-two lengths, together with these resampling maps. The remaining middle transform is then turned into a convolution by the [Bluestein chirp identity](bluestein-chirp-identity.md).

The paper proves that the two permutations need not be executed as separate full sorts. They can be left in the transform identity and cancelled later.

## Prerequisites

- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Linear contraction](linear-contraction.md)

## Used by

- [Transform identity](transform-identity.md)
- [Source and target permutations](target-permutation.md)
- [Middle transform](middle-transform.md)
- [Bluestein chirp identity](bluestein-chirp-identity.md)
- [Multiplication algorithm](multiplication-algorithm.md)

## Sources

> it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose
>
> — Integer multiplication below n log n (OpenAI, 2026)
