The discrete Fourier transform is the map that replaces a vector of complex numbers by weighted sums of its entries, normalized by the reciprocal of the vector's length. The discrete Fourier transform is needed for [convolution](convolution.md). The paper's argument uses its normalized form: <cite data-source="paper">We now implement the normalized Fourier transforms needed for convolution</cite>. Later pages replace these transforms: [Gaussian resampling](gaussian-resampling.md) uses power-of-two lengths, and [Synthetic polynomial transforms](synthetic-transforms.md) use powers of a polynomial variable as roots of unity.

Let $q$ be the length of the transform, the number of coordinates of each vector it acts on. Here $q$ is not the address $q$ of the destination-rank page. Here $i$ is the imaginary unit, not the input position $i$ of the convolution page. A $q$-th root of unity is a complex number whose $q$-th power is $1$. Let $\omega = e^{-2\pi i/q}$ be the primitive $q$-th root of unity, with $\omega^q = 1$ and no smaller positive power equal to $1$.

Let $u = (u_0, u_1, \ldots, u_{q-1})$ be a vector of $q$ complex numbers. Let $s$ and $\ell$ be integer indices running over $0, 1, \ldots, q-1$, where $s$ indexes input coordinates and $\ell$ indexes output coordinates. The discrete Fourier transform of length $q$ is the map $F_q$ sending $u$ to the vector $F_q u$ with coordinates

$$
(F_q u)_\ell = \frac{1}{q} \sum_{s=0}^{q-1} u_s\, \omega^{s\ell} = \frac{1}{q} \sum_{s=0}^{q-1} u_s\, e^{-2\pi i\, s\ell/q}.
$$

The discrete Fourier transform $F_q$ is a [linear map](linear-algebra-basics.md) of $q$-vectors. Each output is a weighted sum of all $q$ inputs, with weights $\omega^{s\ell}$ of modulus one, times the normalization $1/q$. The exponent carries a negative sign. The paper *Integer multiplication below n log n* uses the same sign: <cite data-source="paper">The first identity uses the negative Fourier sign in our definition of Fq</cite>.

$F_q^+$ is the transform with the positive sign in the exponent, $(F_q^+ v)_\ell = \frac{1}{q}\sum_{s=0}^{q-1} v_s\, \omega^{-s\ell}$. Applying it after $F_q$ returns the input divided by $q$. Let $\nu$ be a second input index, running over $0, 1, \ldots, q-1$:

$$
(F_q^+ F_q u)_\ell = \frac{1}{q^2} \sum_{\nu=0}^{q-1} u_\nu \sum_{s=0}^{q-1} \omega^{s(\nu-\ell)} = \frac{u_\ell}{q}.
$$

The inner sum over $s$ is $q$ when $\nu = \ell$. Otherwise $\nu-\ell$ is a nonzero integer strictly between $-q$ and $q$, so $\omega^{\nu-\ell} \ne 1$. Since $(\omega^{\nu-\ell})^q = 1$, the geometric sum $\sum_{s=0}^{q-1} (\omega^{\nu-\ell})^s = \frac{(\omega^{\nu-\ell})^q - 1}{\omega^{\nu-\ell} - 1}$ is $0$.

The vector norm is the maximum modulus of the coordinates, so $\|u\| = \max_s |u_s|$. A linear map $K$ on $q$-vectors is a contraction when $\|Ku\| \le \|u\|$ for every $u$. The paper gives the reason for the normalization: <cite data-source="paper">normalized Fourier transform above is a contraction, since each output averages inputs multiplied</cite> by complex numbers of modulus one. Each $|\omega^{s\ell}| = 1$, so $|(F_q u)_\ell| \le \frac{1}{q}\sum_s |u_s| \le \max_s |u_s| = \|u\|$. The factor $1/q$ is what gives this bound: without it, the same estimate gives only $q\|u\|$.

Worked example. Take $q = 4$. Then $\omega = e^{-2\pi i/4} = -i$, so $\omega^0 = 1$, $\omega^1 = -i$, $\omega^2 = -1$ and $\omega^3 = i$. For $u = (1, 2, 3, 4)$,

$$
(F_4 u)_0 = \tfrac{1}{4}(1+2+3+4) = \tfrac{5}{2}, \qquad (F_4 u)_1 = \tfrac{1}{4}(1-2i-3+4i) = \tfrac{-1+i}{2},
$$

$$
(F_4 u)_2 = \tfrac{1}{4}(1-2+3-4) = -\tfrac{1}{2}, \qquad (F_4 u)_3 = \tfrac{1}{4}(1+2i-3-4i) = \tfrac{-1-i}{2}.
$$
