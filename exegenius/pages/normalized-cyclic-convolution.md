A normalized cyclic convolution is a scaling of the [Cyclic convolution](cyclic-convolution.md) $f \ast g$ by the reciprocal of the sequence length. It is the form in which a Fourier transform turns convolution into pointwise products, the step [Bluestein's chirp identity](bluestein-chirp-identity.md) relies on.

Let $s$ be the sequence length, the number of entries in each complex sequence $f$ and $g$. For $0 \le k \le s-1$,
$$(f \ast g)_k = \sum_{j=0}^{s-1} f_j\, g_{(k-j) \bmod s},$$
where $k$ is an output position, $f_j$ is the entry of $f$ at position $j$, and $(k-j) \bmod s$ is the remainder of $k-j$ on division by $s$. The normalized cyclic convolution $f \circledast g$ is the convolution divided by $s$: $f \circledast g = \frac{1}{s}(f \ast g)$.

A normalized cyclic convolution is turned into pointwise products by the [Discrete Fourier transform](discrete-fourier-transform.md) $F_s$ of length $s$, with $(F_s u)_k = \frac{1}{s}\sum_{j=0}^{s-1} u_j\,\omega^{jk}$. The transform $F_s$ takes its weights from powers of $\omega$, a primitive $s$-th [Root of unity](root-of-unity.md): a complex number with $\omega^s = 1$ whose smaller positive powers are not 1.

The source states the rule for length $S$: <cite data-source="paper">The normalized convolution rule is Fs (u ∗ v) = S(Fs u) · (Fs v), while Fs+ Fs = I/S.</cite> With $S = s$ it reads $F_s(f \ast g) = s\,(F_s f)(F_s g)$. Let $\ell$, $0 \le \ell \le s-1$, index the entries of $f \ast g$. A pair $j$ of $f$ and $j'$ of $g$ contributes $f_j g_{j'}$ to entry $\ell = (j+j') \bmod s$, and $\omega^s = 1$ gives $\omega^{\ell k} = \omega^{(j+j')k}$. Hence
$$F_s(f \ast g)_k = \frac{1}{s}\sum_{j,\,j'} f_j\,g_{j'}\,\omega^{(j+j')k} = s\,(F_s f)_k\,(F_s g)_k,$$
the last step because $(F_s f)_k (F_s g)_k = \frac{1}{s^2}\sum_{j,\,j'} f_j g_{j'}\,\omega^{(j+j')k}$. Dividing by $s$ gives $F_s(f \circledast g)_k = (F_s f)_k (F_s g)_k$.

Take $s = 2$, so $\omega = -1$, with $f = (1, 2)$ and $g = (3, 4)$. Then $f \ast g = (11, 10)$, so $f \circledast g = (11/2,\ 5)$. Here $(F_2 u)_0 = (u_0+u_1)/2$ and $(F_2 u)_1 = (u_0-u_1)/2$, so $F_2 f = (3/2,\ -1/2)$ and $F_2 g = (7/2,\ -1/2)$. Their entrywise product is $(21/4,\ 1/4)$, which equals $F_2(f \circledast g) = ((11/2+5)/2,\ (11/2-5)/2)$.

The paper's middle transform $QFt$ is the Fourier-type factor of its equation (35), and <cite data-source="paper">The factor QFt in (35) can be computed from a cyclic convolution and two pointwise phase</cite> multiplications. <cite data-source="paper">Bluestein’s chirp identity converts the middle transform, including its target permutation,</cite> into normalized cyclic convolution.

For the chirp form, let $s$ be even, take $\omega = e^{-2\pi i/s}$, and for each integer $m$ (a free integer here) let $\chi_m = e^{\pi i m^2/s}$. Since $(m+s)^2 = m^2 + 2ms + s^2$ and $e^{\pi i s} = 1$, $\chi_{m+s} = \chi_m$, so $\chi$ has period $s$. Also $jk = \tfrac12\big(j^2 + k^2 - (k-j)^2\big)$ gives $\omega^{jk} = \overline{\chi_j}\,\overline{\chi_k}\,\chi_{k-j}$, so, writing $\overline{\chi}\cdot u$ for the entrywise product, with entries $\overline{\chi_j}\,u_j$,
$$(F_s u)_k = \overline{\chi_k}\,\big((\overline{\chi}\cdot u)\circledast \chi\big)_k, \qquad 0 \le k \le s-1.$$

A normalized cyclic convolution is evaluated through [Gaussian resampling](gaussian-resampling.md), which moves between coprime lengths and powers of two. <cite data-source="paper">Gaussian resampling connects these two shapes.</cite> A normalized cyclic convolution is computed by applying the [Transform identity with retained permutations](transform-identity.md), which keeps the source and target permutations in the formula so that they cancel across the convolution.
