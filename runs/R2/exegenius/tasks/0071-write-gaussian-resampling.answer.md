Gaussian resampling is the reduction of Harvey and van der Hoeven that replaces each prime-length Fourier transform needed for a convolution <cite data-source="paper">by multidimensional transforms whose axis lengths are powers of two</cite>. It lets the fast machinery of the main theorem work only on power-of-two axes.

A standard FFT of length $2m$ splits into two transforms of length $m$, where $m$ is the number of points in each half. A prime-length transform has no such split, so each prime axis would otherwise need its own fast algorithm.

Write $F_L$ for the discrete Fourier transform of a list with $L$ entries, which evaluates the list at the $L$-th roots of unity, and $P_L$ for a fixed reordering of its $L$ coordinates. Here $L$ is the number of entries in the list.

Let $p_j$ be one of the prime axis lengths, and let $t$ be a power of two, the number of points in the power-of-two transform, chosen slightly above $p_j$. The identity is

$$P_{p_j}F_{p_j}=2^{e}\,J\,P_tF_t\,G,$$

where $G$ maps lists of length $p_j$ to lists of length $t$, $J$ maps back, and $e$ is a fixed integer exponent. $G$ and $J$ are linear contractions, maps that do not increase the largest modulus of an entry. Harvey and van der Hoeven prove the identity and the inverse bound <cite data-source="paper">The exact Gaussian identity and inverse estimate proved in</cite>.

Why it holds: $G$ and $J$ are sums weighted by Gaussians that move values between the two grids. The Fourier transform maps a Gaussian to a Gaussian, so transforming on one grid agrees with transforming the Gaussian-weighted list on the other. The compensated map from one grid to the other is within less than one half of the identity in norm, so it can be inverted, and $J$ is built from that inverse.

To evaluate $F_{p_j}$ on a list, apply $G$, then $P_tF_t$, then $J$. Multiplying by $2^{e}$ and undoing the permutation $P_{p_j}$ gives the prime transform of the same list.

Gaussian resampling acts on the axes placed by the [Chinese-remainder map to prime cyclic axes](crt-address-map.md), removing the prime-length transform along each one. Gaussian resampling thus computes its transforms by the butterfly layers of [Discrete Fourier transform and butterflies](dft-fft.md), since a transform of length $t$ has $\lg t$ layers, each linear in the array size. So the later butterfly and address-move speedups apply to these transforms.
