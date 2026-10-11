A normalized cyclic convolution is a scaling of the [Cyclic convolution](cyclic-convolution.md) $f \ast g$ by the reciprocal of the sequence length. It is the form that lets a transform turn convolution into products, and [Bluestein's chirp identity](bluestein-chirp-identity.md) uses it to rewrite the middle transform (the Fourier-type factor of the paper's transform) as one such convolution.

Let $s$ be the number of entries in each of the sequences $f$ and $g$. The entries of $f \ast g$ are
$$(f \ast g)_k = \sum_{j=0}^{s-1} f_j\, g_{(k-j) \bmod s}, \qquad 0 \le k \le s-1,$$
where $f_j$ is the entry of $f$ at position $j$, and the index $(k-j) \bmod s$ wraps around modulo $s$. We write $f \circledast g$ for the normalized cyclic convolution of $f$ and $g$, the cyclic convolution $f \ast g$ divided by $s$:
$$f \circledast g = \frac{1}{s}\,(f \ast g).$$

Let $F_s$ denote the normalized discrete Fourier transform of length $s$, with entries $(F_s u)_k = \frac{1}{s}\sum_{j=0}^{s-1} u_j\,\omega^{jk}$, where $\omega$ is the primitive $s$-th root of unity, so $\omega^s = 1$. A normalized cyclic convolution is turned into pointwise products by the [Discrete Fourier transform](discrete-fourier-transform.md) $F_s$, as the rule below states. The source states this rule for the unnormalized product, with length $S$: <cite data-source="paper">The normalized convolution rule is Fs (u ∗ v) = S(Fs u) · (Fs v), while Fs+ Fs = I/S.</cite>

With $S = s$ this says $F_s(f \ast g) = s\,(F_s f)(F_s g)$. To check it, note that each pair $j, j'$ contributes $f_j g_{j'}$ to entry $(j+j') \bmod s$ of $f \ast g$, and $\omega^s = 1$ makes $\omega^{\ell k}=\omega^{(j+j')k}$ there, so
$$F_s(f \ast g)_k = \frac{1}{s}\sum_{j,\,j'} f_j\,g_{j'}\,\omega^{(j+j')k} = s\,(F_s f)_k\,(F_s g)_k.$$
Dividing by $s$ gives the form used here:
$$F_s(f \circledast g)_k = (F_s f)_k\,(F_s g)_k, \qquad 0 \le k \le s-1.$$

Take $s = 2$, $f = (1, 2)$ and $g = (3, 4)$. Then $f \ast g = (11, 10)$, so $f \circledast g = (11/2,\ 5)$. Also $F_2 f = (3/2,\ -1/2)$ and $F_2 g = (7/2,\ -1/2)$. Their entrywise product is $(21/4,\ 1/4)$, which equals $F_2(f \circledast g)$.

Let $q$ be even and $\omega = e^{2\pi i/q}$. For integers $m$, let $\chi_m = e^{\pi i m^2/q}$, the chirp phase at $m$; for even $q$, $\chi$ has period $q$. Since $jk = \frac{j^2 + k^2 - (k-j)^2}{2}$, we get $\omega^{jk} = \chi_j\,\chi_k\,\overline{\chi_{k-j}}$, and substituting this into $(F_q u)_k$ gives
$$(F_q u)_k = \chi_k\,\big((\chi \cdot u) \circledast \overline{\chi}\big)_k,$$
where $\cdot$ is entrywise multiplication. The transform is thus two pointwise phase multiplications around one normalized cyclic convolution, as the paper states: <cite data-source="paper">The factor QFt in (35) can be computed from a cyclic convolution and two pointwise phase multiplications.</cite>

A normalized cyclic convolution is computed with permutations kept in the [transform identity with retained permutations](transform-identity.md), so that they cancel across the convolution. A normalized cyclic convolution is computed on power-of-two axes, which [Gaussian resampling](gaussian-resampling.md) provides.
