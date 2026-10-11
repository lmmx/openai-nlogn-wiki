The opposite transform $F_q^+$ is the sign-reversed form of the [Discrete Fourier transform](discrete-fourier-transform.md). It is applied to the result of a [pointwise product](pointwise-product.md) of forward transforms. It maps products back from the [frequency domain](frequency-domain.md) to coefficients, which makes it the step that recovers convolution coefficients on the way to exact integer multiplication below $n\log n$.

For a vector $u$ of $q$ complex numbers, with $\omega = e^{-2\pi i/q}$ as on the transform page, the opposite transform is
$$(F_q^+ u)_\ell = \frac{1}{q}\sum_{s=0}^{q-1} \omega^{-s\ell}\, u_s, \qquad 0 \le \ell \le q-1.$$
It is the forward transform with the sign of the exponent reversed. The source states this as <cite data-source="paper">conjugation changes the negative Fourier sign to the positive one</cite>.

The two transforms invert each other up to the factor $q$. Expanding the composition gives
$$(F_q^+F_q u)_\ell = \frac{1}{q^2}\sum_{s=0}^{q-1} u_s \sum_{\sigma=0}^{q-1}\omega^{\sigma(s-\ell)}.$$
The inner sum over the dummy index $\sigma$ is $q$ when $s=\ell$. Otherwise $\omega^{s-\ell}$ is a $q$-th root of unity different from $1$, since $\omega$ is primitive and $0<|s-\ell|<q$, so the geometric series in $\sigma$ vanishes. Hence $F_q^+F_q u=u/q$.

For $q=4$ and $u=(1,0,0,0)$, $F_4u=(\tfrac14,\tfrac14,\tfrac14,\tfrac14)$, and $(F_4^+F_4u)_\ell=\tfrac1{16}\sum_{\sigma=0}^{3} i^{\sigma\ell}$ is $\tfrac14$ at $\ell=0$ and $0$ at $\ell=1,2,3$. So $F_4^+F_4u=u/4$.

For a second vector $u'$ of $q$ complex numbers, let $u\ast u'$ be the cyclic convolution of $u$ and $u'$. Write $t$ for the input index of $u'$, running from $0$ to $q-1$, so that $(u\ast u')_\ell=\sum_{s+t\equiv\ell \pmod q}u_s u'_t$ with $s$ and $t$ over $0,\dots,q-1$. With $\odot$ the entrywise product,
$$F_q^+\bigl(F_q u\odot F_q u'\bigr)=\frac{1}{q^2}\,(u\ast u').$$
Expanding the left side gives $\frac{1}{q^3}\sum_{s,t}u_s u'_t\sum_{\sigma}\omega^{\sigma(s+t-\ell)}$, and by the argument above the sum over $\sigma$ is $q$ exactly when $s+t\equiv\ell \pmod q$.

For disk-grid ring arrays, <cite data-source="paper">Two normalized synthetic forwards, pointwise polynomial multiplication divided by r, and the normalized opposite transform give</cite> the normalized convolution of two such arrays. The frequency order must survive the pointwise product: <cite data-source="paper">forward synthetic transforms retain the same frequency order through their pointwise product</cite>, because <cite data-source="paper">the opposite transform consumes that order.</cite>

The opposite transform is applied along the axes of an [array](array.md), one axis at a time.
