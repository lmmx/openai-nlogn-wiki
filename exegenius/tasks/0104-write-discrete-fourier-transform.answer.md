The discrete Fourier transform is needed for [convolution](convolution.md). The argument uses its normalized form: <cite data-source="paper">We now implement the normalized Fourier transforms needed for convolution</cite>. The page on [Gaussian resampling](gaussian-resampling.md) replaces these transforms by transforms whose lengths are powers of two, and the page on [Synthetic polynomial transforms](synthetic-transforms.md) replaces their roots of unity by powers of a polynomial variable.

Let $q$ be the length of the transform, the number of coordinates of each vector it acts on. A $q$-th root of unity is a complex number whose $q$-th power is $1$. Let $\omega = e^{-2\pi i/q}$ be the primitive $q$-th root of unity, a complex number with $\omega^q = 1$ and no smaller positive power of it equal to $1$.

Let $u = (u_0, u_1, \ldots, u_{q-1})$ be a vector of $q$ complex numbers. Let $j$, $\ell$ and $m$ be integer indices running over $0, 1, \ldots, q-1$, where $j$ and $m$ index input coordinates and $\ell$ indexes output coordinates. The discrete Fourier transform of length $q$ is the map $F_q$ sending $u$ to the vector $F_q u$ with coordinates

$$
(F_q u)_\ell = \frac{1}{q} \sum_{j=0}^{q-1} u_j\, \omega^{j\ell} = \frac{1}{q} \sum_{j=0}^{q-1} u_j\, e^{-2\pi i\, j\ell/q}.
$$

The discrete Fourier transform $F_q$ is a [linear map](linear-algebra-basics.md) of $q$-vectors. Each output $(F_q u)_\ell$ is a weighted sum of all $q$ inputs, with weights $\omega^{j\ell}$ of modulus one, and the factor $1/q$ is the normalization. The exponent carries a negative sign. The paper *Integer multiplication below n log n* uses the same sign: <cite data-source="paper">The first identity uses the negative Fourier sign in our definition of Fq</cite>.

$F_q^+$ is the same map with the positive sign, which replaces $\omega$ by $\omega^{-1}$. Applying it after $F_q$ returns the input divided by $q$:

$$
(F_q^+ F_q u)_\ell = \frac{1}{q^2} \sum_{m=0}^{q-1} u_m \sum_{j=0}^{q-1} \omega^{j(m-\ell)} = \frac{u_\ell}{q}.
$$

The inner sum over $j$ is $q$ when $m = \ell$. Otherwise $\omega^{m-\ell} \ne 1$, since $m-\ell$ is a nonzero integer that is not a multiple of $q$. Also $(\omega^{m-\ell})^q = 1$, so the geometric sum $\sum_{j=0}^{q-1} (\omega^{m-\ell})^j = \frac{(\omega^{m-\ell})^q - 1}{\omega^{m-\ell} - 1}$ is $0$.

The vector norm used for bounds is <cite data-source="paper">The vector norm is the maximum modulus</cite> of its coordinates, so $\|u\| = \max_j |u_j|$. A linear map $L$ is a contraction when $\|Lu\| \le \|u\|$ for every $u$. The paper gives the reason for the normalized transforms: <cite data-source="paper">normalized Fourier transform above is a contraction, since each output averages inputs multiplied</cite> by complex numbers of modulus one. Concretely, $|(F_q u)_\ell| \le \frac{1}{q}\sum_j |u_j| \le \max_j |u_j|$.

Worked example. Take $q = 4$. Then $\omega = e^{-2\pi i/4} = -i$, so $\omega^0 = 1$, $\omega^1 = -i$, $\omega^2 = -1$ and $\omega^3 = i$. For $u = (1, 2, 3, 4)$,

$$
(F_4 u)_0 = \tfrac{1}{4}(1+2+3+4) = \tfrac{5}{2}, \qquad (F_4 u)_1 = \tfrac{1}{4}(1-2i-3+4i) = \tfrac{-1+i}{2},
$$

$$
(F_4 u)_2 = \tfrac{1}{4}(1-2+3-4) = -\tfrac{1}{2}, \qquad (F_4 u)_3 = \tfrac{1}{4}(1+2i-3-4i) = \tfrac{-1-i}{2}.
$$
