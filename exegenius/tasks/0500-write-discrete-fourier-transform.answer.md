The discrete Fourier transform is needed for [convolution](convolution.md). The paper *Integer multiplication below n log n* (OpenAI, 2026) uses its normalized form, also called the normalized Fourier transform, to compute convolutions. Later pages replace these transforms by [Gaussian resampling](gaussian-resampling.md) and by [synthetic polynomial transforms](synthetic-transforms.md).

Let $q$ be the transform length, the number of coordinates of each vector the transform acts on, a positive integer. Here $i$ is the imaginary unit, not the input position $i$ of the convolution page. A $q$-th root of unity is a complex number whose $q$-th power is $1$. Write $\omega = e^{-2\pi i/q}$ for the primitive $q$-th root of unity: $\omega^q = 1$, and $\omega^\rho \ne 1$ for each integer exponent $\rho$ with $0 < \rho < q$, so no smaller positive power of $\omega$ equals $1$.

Let $f = (f_0, f_1, \ldots, f_{q-1})$ be a vector of $q$ complex numbers, and let $s$ and $\ell$ be integer indices running over $0, 1, \ldots, q-1$, where $s$ labels an input coordinate $f_s$ and $\ell$ labels an output coordinate. The discrete Fourier transform of length $q$ is the map $F_q$ sending $f$ to the vector $F_q f$ with coordinates

$$
(F_q f)_\ell = \frac{1}{q} \sum_{s=0}^{q-1} f_s\, \omega^{s\ell} = \frac{1}{q} \sum_{s=0}^{q-1} f_s\, e^{-2\pi i\, s\ell/q}.
$$

Each output is a weighted sum of all $q$ inputs, with weights $\omega^{s\ell}$, times $1/q$. The discrete Fourier transform $F_q$ is a linear map under the definitions of [linear algebra basics](linear-algebra-basics.md). The exponent has a negative sign, and the paper uses the same sign: <cite data-source="paper">The first identity uses the negative Fourier sign in our definition of Fq</cite>.

$F_q^+$ denotes the same map with the positive sign, $(F_q^+ f)_\ell = \frac{1}{q} \sum_{s=0}^{q-1} f_s\, \omega^{-s\ell}$, which replaces $\omega$ by $\omega^{-1}$. To see that $F_q^+$ undoes $F_q$ up to the factor $q$, take a second dummy index $\sigma$ running over $0, 1, \ldots, q-1$. For each $\ell$,

$$
\begin{aligned}
(F_q^+ F_q f)_\ell &= \frac{1}{q} \sum_{s=0}^{q-1} (F_q f)_s\, \omega^{-s\ell} && \text{(definition of } F_q^+ \text{)} \\
&= \frac{1}{q^2} \sum_{s=0}^{q-1} \sum_{\sigma=0}^{q-1} f_\sigma\, \omega^{\sigma s}\, \omega^{-s\ell} && \text{(substituting the definition of } F_q f \text{ with index } \sigma \text{)} \\
&= \frac{1}{q^2} \sum_{\sigma=0}^{q-1} f_\sigma \sum_{s=0}^{q-1} \omega^{s(\sigma-\ell)} && \text{(exchanging the two sums; } \omega^{\sigma s}\omega^{-s\ell} = \omega^{s(\sigma-\ell)} \text{)}.
\end{aligned}
$$

Let $\rho = \sigma - \ell$, an integer with $-q < \rho < q$. If $\sigma = \ell$, every term of the inner sum is $1$, so the inner sum is $q$. Otherwise $\omega^\rho \ne 1$. For $\rho > 0$ this is the primitivity above. For $\rho < 0$, $\omega^\rho = \omega^{\rho+q}$ because $\omega^q = 1$, and $0 < \rho + q < q$, so again $\omega^\rho \ne 1$. Since $(\omega^\rho)^q = 1$, the geometric sum is

$$
\sum_{s=0}^{q-1} (\omega^\rho)^s = \frac{(\omega^\rho)^q - 1}{\omega^\rho - 1} = 0.
$$

So only $\sigma = \ell$ survives, and $(F_q^+ F_q f)_\ell = \frac{1}{q^2} \cdot q \cdot f_\ell = f_\ell / q$.

The vector norm is $\|f\| = \max_s |f_s|$, the largest modulus of a coordinate. A linear map $K$ on $q$-vectors is a contraction when $\|Kf\| \le \|f\|$ for every $f$. The paper gives the reason for the normalization: <cite data-source="paper">normalized Fourier transform above is a contraction, since each output averages inputs multiplied</cite> by complex numbers of modulus one. Since $|\omega^{s\ell}| = 1$,

$$
|(F_q f)_\ell| \le \frac{1}{q} \sum_{s=0}^{q-1} |f_s| \le \max_s |f_s| = \|f\|.
$$

Without the factor $1/q$, the same estimate would give only $q\|f\|$.

Worked example. Take $q = 4$. Then $\omega = e^{-2\pi i/4} = -i$, so $\omega^0 = 1$, $\omega^1 = -i$, $\omega^2 = -1$ and $\omega^3 = i$. For $f = (1, 2, 3, 4)$,

$$
(F_4 f)_0 = \tfrac{1}{4}(1+2+3+4) = \tfrac{5}{2}, \qquad (F_4 f)_1 = \tfrac{1}{4}(1-2i-3+4i) = \tfrac{-1+i}{2},
$$

$$
(F_4 f)_2 = \tfrac{1}{4}(1-2+3-4) = -\tfrac{1}{2}, \qquad (F_4 f)_3 = \tfrac{1}{4}(1+2i-3-4i) = \tfrac{-1-i}{2}.
$$
