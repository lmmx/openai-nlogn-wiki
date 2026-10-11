The opposite transform $F_q^+$ is the sign-reversed form of the [Discrete Fourier transform](discrete-fourier-transform.md). It is applied to the result of a [pointwise product](pointwise-product.md) of forward transforms, and it maps products in the [frequency domain](frequency-domain.md) back to coefficients.

For a vector $u$ of $q$ complex numbers, indexed by $j$ and $\ell$ from $0$ to $q-1$,
$$(F_q^+ u)_\ell = \frac{1}{q}\sum_{j=0}^{q-1} \omega^{-j\ell}\, u_j, \qquad \omega = e^{-2\pi i/q}.$$
The forward transform $F_q$ uses $\omega^{j\ell}$ in its place, with the same factor $1/q$. The source states this as <cite data-source="paper">conjugation changes the negative Fourier sign to the positive one</cite>.

The two transforms invert each other up to the factor $q$. In the sums below, $m$ and $n$ are summation indices, each running from $0$ to $q-1$, and they name input positions.
$$(F_q^+ F_q u)_\ell = \frac{1}{q^2}\sum_{m=0}^{q-1} u_m \sum_{j=0}^{q-1} \omega^{j(m-\ell)}.$$
The inner sum is $q$ when $m=\ell$. Otherwise it is a geometric series with ratio $z=\omega^{m-\ell}\ne 1$ and $z^q=1$, so it vanishes. Hence $F_q^+F_qu=u/q$.

For $q=4$ and $u=(1,0,0,0)$, $F_4u=(\tfrac14,\tfrac14,\tfrac14,\tfrac14)$, and $(F_4^+F_4u)_\ell=\frac{1}{16}\sum_{j=0}^{3} i^{j\ell}$ is $\tfrac14$ at $\ell=0$ and $0$ at $\ell=1,2,3$.

The transform is the last step of a convolution. For vectors $u$ and $u'$ of $q$ complex numbers, let $u\ast u'$ be their cyclic convolution, $(u\ast u')_\ell=\sum_{m+n\equiv\ell \pmod q}u_m u'_n$, and let $\cdot$ be the entrywise product. Then
$$F_q^+\bigl(F_q u\cdot F_q u'\bigr)=\frac{1}{q^2}\,(u\ast u').$$
Expanding the left side gives $\frac{1}{q^3}\sum_{m,n}u_m u'_n\sum_{j}\omega^{j(m+n-\ell)}$, and the inner sum is $q$ exactly when $m+n\equiv\ell \pmod q$.

The paper, *Integer multiplication below n log n*, uses the same sign convention for its synthetic transforms, whose entries are <cite data-source="paper">short polynomials in a quotient where the required roots of unity act by exact signed permutations</cite>. It writes the roots as <cite data-source="paper">define ωt = y 2r/t</cite>.

Let $f$ and $g$ be two [disk-grid ring arrays](array.md), whose entries are polynomials of degree less than $r$. The synthetic opposite transform acts on each [array](array.md) along its axes. Write $M$ for the number of cyclic addresses of each array; the letter $M$ changes meaning here. Here $f\ast g$ is the cyclic convolution along each axis, with wrap-around past $y^r$ contributing a sign. The paper states the result as two normalized synthetic forwards, pointwise <cite data-source="paper">polynomial multiplication divided by r, and the normalized opposite transform give</cite> $(f\ast g)/(rM^2)$.

The product must keep the frequency order, which is the order in which a transform stores its entries by frequency. <cite data-source="paper">forward synthetic transforms retain the same frequency order through their pointwise product</cite>, because <cite data-source="paper">the opposite transform consumes that order.</cite>
