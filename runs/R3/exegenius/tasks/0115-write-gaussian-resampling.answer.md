Gaussian resampling is the reduction of Harvey and van der Hoeven that replaces each prime-length Fourier transform needed for a convolution <cite data-source="paper">by multidimensional transforms whose axis lengths are powers of two</cite>. A standard FFT of length $2m$ splits into two transforms of length $m$. A prime-length transform has no such split.

Let $p$ be the length of a prime axis, the number of entries in a list on that axis, and let $Q$ be a power of two, the number of entries in the list that replaces it, chosen slightly above $p$. Let $F_p$ and $F_Q$ be the normalized discrete Fourier transforms, $(F_p f)_k=\frac1p\sum_{j=0}^{p-1}f_j e^{-2\pi i jk/p}$ and likewise $F_Q$. Let $\pi_p$ and $\pi_Q$ be the coordinate reorderings used in the paper's identity. A contraction is a linear map that does not increase the largest modulus of an entry. Each normalized transform is a contraction <cite data-source="paper">since each output averages inputs multiplied by complex numbers of modulus one</cite>.

For an integer $\alpha$ with $2\le\alpha<\sqrt p$, the identity is
$$\pi_pF_p=2^{2\alpha^2}\,K\,\pi_QF_Q\,U,$$
where $U$ maps lists of length $p$ to lists of length $Q$, $K$ maps back, and $\alpha$ is the width parameter of the Gaussian weights below.

Both $U$ and $K$ are built from two Gaussian-weighted sums $\mathsf S$ and $\mathsf T$, each mapping lists of length $p$ to lists of length $Q$:
$$(\mathsf S f)_k=\frac1\alpha\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-pk/Q)^2}f_j,\qquad(\mathsf T f)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(Qj/p-k)^2}f_j,$$
where entries $f_j$ are read modulo $p$, and $j$ and $k$ are entry indices. Each weight is a Gaussian centred on a point of the other grid. Harvey and van der Hoeven prove the Gaussian identity
$$\mathsf T\pi_pF_p=\pi_QF_Q\mathsf S$$
(their Theorem 4.2). It holds because the Fourier transform maps a Gaussian to a Gaussian.

$\mathsf T$ alone is not invertible, so we compensate. Put $\theta=Q/p-1$, which is assumed to satisfy $\theta>p/\alpha^4$. Let $z_j$ be the integer nearest $Qj/p$ and $\beta_j=Qj/p-z_j$. Let $R$ read the entries $z_j$ from a list of length $Q$, let $\Lambda$ multiply entry $j$ by $e^{\pi\alpha^2\beta_j^2}$, and set $\Phi=R\,\mathsf T\,\Lambda$, a map from length $p$ to length $p$. Entry $j$ of $\Phi f$ contains $f_j$ exactly, since $\Lambda$ cancels the Gaussian weight at $z_j$. The paper's Lemma 4.6 gives $\|\Phi-I\|<2^{-\alpha^2\theta}$. Since $\alpha^2\theta>p/\alpha^2>1$, we have $\|\Phi-I\|<1/2$, so $\Phi$ is invertible by the Neumann series $\Phi^{-1}=\sum_{\nu\ge0}(I-\Phi)^\nu$.

Since $R\mathsf T=\Phi\Lambda^{-1}$, the map $\Lambda\Phi^{-1}R$ is a left inverse of $\mathsf T$. Applying it to the Gaussian identity gives $\Lambda\Phi^{-1}R\,\pi_QF_Q\mathsf S=\pi_pF_p$. Set $U=\frac12\mathsf S$ and $K=2^{1-2\alpha^2}\Lambda\Phi^{-1}R$. Then $2^{2\alpha^2}K\pi_QF_QU=\pi_pF_p$, which is the identity.

The paper's Proposition 4.7(i) bounds $\|U\|<3/4$, $\|\tfrac12\Phi^{-1}\|<7/8$ and $\|2^{2-2\alpha^2}\Lambda\|<1$. Since $\|R\|=1$, $U$ and $K$ are contractions. Contractions keep composed approximation errors from growing.

To evaluate $F_p$ on a list $f$, apply $U$, then $\pi_QF_Q$, then $K$, multiply by $2^{2\alpha^2}$, and undo $\pi_p$.

Gaussian resampling acts on the axes placed by the [Chinese-remainder map to prime cyclic axes](crt-address-map.md). Gaussian resampling thus computes its transforms by the butterfly layers of [Discrete Fourier transform and butterflies](dft-fft.md), since a transform of length $Q$ has $\lg Q$ layers, each linear in the array size. The speedups of [Fast simultaneous butterfly layers](fast-butterfly-layers.md) and [Fast interchange of address fields](fast-address-interchange.md) therefore apply to these transforms.
