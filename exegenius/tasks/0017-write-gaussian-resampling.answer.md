Gaussian resampling is the step that replaces a [discrete Fourier transform](discrete-fourier-transform.md) of a length that is not a power of two by a transform whose axes all have power-of-two lengths. The paper adapts the identity of Harvey and van der Hoeven.

The idea is to move values between two grids of different sizes, so that the transform matches the wraparound structure of a [cyclic convolution](cyclic-convolution.md). Let $s < t$ be coprime integers. A length-$s$ grid and a length-$t$ grid are related by two coordinate permutations. The paper defines them as $(P_s u)_j = u_{tj}$ and $(P_t v)_k = v_{-sk}$, where indices are taken modulo the length. When $\gcd(s,t) = 1$, the map $j \mapsto tj \bmod s$ is a bijection.

For a small case, take $s = 3$ and $t = 4$. The map $j \mapsto 4j \bmod 3$ sends $0, 1, 2$ to $0, 1, 2$, so it is a permutation. The gcd condition is what makes this hold in general.

The resampling itself uses linear contractions $A : \mathbb{C}^s \to \mathbb{C}^t$ and $B_0 : \mathbb{C}^t \to \mathbb{C}^s$, which approximate a Gaussian-weighted interpolation. The Gaussian window makes the error small when $t/s - 1$ is large compared with the precision parameter, and this is what allows an approximate resampling with a fixed number of bits of precision.

The payoff is that each source Fourier transform can be expressed through a transform whose axes have power-of-two lengths, together with these resampling maps. The remaining middle transform is then turned into a convolution by the [Bluestein chirp identity](bluestein-chirp-identity.md).

The paper proves that the two permutations need not be executed as separate full sorts. They can be left in the transform identity and cancelled later.
