Let $q$ be the transform length, the number of coordinates of each vector the transform acts on, a positive integer. The discrete Fourier transform of length $q$ is the map that sends a list of $q$ complex numbers to $q$ weighted sums of that list, normalized by $1/q$. The discrete Fourier transform is needed for [convolution](convolution.md). The paper computes convolutions with its normalized form, and later pages replace these transforms by [Gaussian resampling](gaussian-resampling.md) and by [synthetic polynomial transforms](synthetic-transforms.md).

A $q$-th root of unity is a complex number whose $q$-th power is $1$. The imaginary unit is written $\sqrt{-1}$, so that $i$ keeps its meaning on the earlier pages. Write $\omega = e^{-2\pi\sqrt{-1}/q}$ for the primitive $q$-th root of unity. Then $\omega^q = 1$, and $\omega^\mu \ne 1$ for each integer exponent $\mu$ with $0 < \mu < q$, so no smaller positive power of $\omega$ equals $1$.

Let $f = (f_0, f_1, \ldots, f_{q-1})$ be a vector of $q$ complex numbers, and let $s$ and $\ell$ be integer indices running over $0, 1, \ldots, q-1$, where $s$ labels an input coordinate $f_s$ and $\ell$ labels an output coordinate. The discrete Fourier transform of length $q$ is the map $F_q$ sending $f$ to the vector $F_q f$ with coordinates

$$
(F_q f)_\ell = \frac{1}{q} \sum_{s=0}^{q-1} f_s\, \omega^{s\ell} = \frac{1}{q} \sum_{s=0}^{q-1} f_s\, e^{-2\pi\sqrt{-1}\, s\ell/q}.
$$

Each output is a weighted sum of all $q$ inputs, with weights $\omega^{s\ell}$, times $1/q$. The discrete Fourier transform $F_q$ is built on [linear algebra basics](linear-algebra-basics.md): it is a linear map, since each output is a fixed combination of the inputs. The exponent has a negative sign, and the paper uses the same sign: <cite data-source="paper">The first identity uses the negative Fourier sign in our definition of Fq</cite>.

$F_q^+$ denotes the same map with the positive sign, $(F_q^+ f)_\ell = \frac{1}{q} \sum_{s=0}^{q-1} f_s\, \omega^{-s\ell}$, which replaces $\omega$ by $\omega^{-1}$. To see that $F_q^+$ undoes $F_q$ up to the factor $q$, take a second dummy index $\sigma$ running over $0, 1, \ldots, q-1$. For each $\ell$,

$$
\begin{aligned}
(F_q^+ F_q f)_\ell &= \frac{1}{q} \sum_{s=0}^{q-1} (F_q f)_s\, \omega^{-s\ell} && \text{(definition of } F_q^+ \text{)} \\
&= \frac{1}{q^2} \sum_{s=0}^{q-1} \sum_{\sigma=0}^{q-1} f_\sigma\, \omega^{\sigma s}\, \omega^{-s\ell} && \text{(substituting the definition of } F_q f \text{ with index } \sigma \text{)} \\
&= \frac{1}{q^2} \sum_{\sigma=0}^{q-1} f_\sigma \sum_{s=0}^{q-1} \omega^{s(\sigma-\ell)} && \text{(exchanging the two sums)}.
\end{aligned}
$$

Let $\rho = \sigma - \ell$, an integer with $-q < \rho < q$. If $\sigma = \ell$, every term of the inner sum is $1$, so the inner sum is $q$. Otherwise $\omega^\rho \ne 1$: for $\rho > 0$ this is the primitivity above, and for $\rho < 0$, $\omega^\rho = \omega^{\rho+q}$ with $0 < \rho + q < q$. Since $(\omega^\rho)^q = 1$, the geometric sum is

$$
\sum_{s=0}^{q-1} (\omega^\rho)^s = \frac{(\omega^\rho)^q - 1}{\omega^\rho - 1} = 0.
$$

So only $\sigma = \ell$ survives, and $(F_q^+ F_q f)_\ell = \frac{1}{q^2} \cdot q \cdot f_\ell = f_\ell / q$.

Write $\|f\|$ for the [array norm](array-norm.md) of $f$, the largest modulus of its coordinates, where $|z|$ is the modulus of a complex number $z$. A linear map $K$ on $q$-vectors is a contraction when $\|Kf\| \le \|f\|$ for every $f$. The paper gives the reason for the normalization: <cite data-source="paper">normalized Fourier transform above is a contraction, since each output averages inputs multiplied</cite> by complex numbers of modulus one. Since $|\omega^{s\ell}| = 1$,

$$
|(F_q f)_\ell| \le \frac{1}{q} \sum_{s=0}^{q-1} |f_s| \le \max_s |f_s| = \|f\|.
$$

Without the factor $1/q$, the same estimate gives only $q\|f\|$, so repeated unnormalized transforms could multiply the largest entry by up to $q$ at each step.

Worked example. Take $q = 4$. Then $\omega = e^{-2\pi\sqrt{-1}/4} = -\sqrt{-1}$, so $\omega^0 = 1$, $\omega^1 = -\sqrt{-1}$, $\omega^2 = -1$ and $\omega^3 = \sqrt{-1}$. For $f = (1, 2, 3, 4)$,

$$
(F_4 f)_0 = \tfrac{1}{4}(1+2+3+4) = \tfrac{5}{2}, \qquad (F_4 f)_1 = \tfrac{1}{4}(1-2\sqrt{-1}-3+4\sqrt{-1}) = \tfrac{-1+\sqrt{-1}}{2},
$$

$$
(F_4 f)_2 = \tfrac{1}{4}(1-2+3-4) = -\tfrac{1}{2}, \qquad (F_4 f)_3 = \tfrac{1}{4}(1+2\sqrt{-1}-3-4\sqrt{-1}) = \tfrac{-1-\sqrt{-1}}{2}.
$$
