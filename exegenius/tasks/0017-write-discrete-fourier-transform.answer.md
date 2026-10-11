The discrete Fourier transform of length $q$, with $q$ the number of coordinates of each vector it acts on, maps a vector of $q$ complex numbers to another vector of $q$ complex numbers, each output being a weighted sum of all the inputs with weights that are powers of a root of unity. The argument needs these transforms for convolution <cite data-source="paper">We now implement the normalized Fourier transforms needed for convolution</cite>. The page on [Gaussian resampling](gaussian-resampling.md) replaces them by transforms whose lengths are powers of two, and the page on [Synthetic polynomial transforms](synthetic-transforms.md) replaces their roots of unity by powers of a polynomial variable.

A $q$-th root of unity is a complex number $z$ with $z^q = 1$. Write $\omega = e^{-2\pi i/q}$ for the primitive $q$-th root of unity: a complex number with $\omega^q = 1$ and $\omega^m \neq 1$ for $0 < m < q$.

Let $u = (u_0, u_1, \ldots, u_{q-1})$ be a vector of $q$ complex numbers. The indices $j$ and $k$ run over $0, 1, \ldots, q-1$. The discrete Fourier transform of length $q$ is the map $F_q$ sending $u$ to the vector $F_q u$ with coordinates

$$
(F_q u)_k = \frac{1}{q} \sum_{j=0}^{q-1} u_j\, \omega^{jk} = \frac{1}{q} \sum_{j=0}^{q-1} u_j\, e^{-2\pi i\, jk/q}.
$$

Each output $(F_q u)_k$ is a weighted sum of all $q$ inputs, with weights $\omega^{jk}$ of modulus one, and the factor $1/q$ is the normalization. The exponent carries a negative sign. The source uses the same sign: <cite data-source="paper">The first identity uses the negative Fourier sign in our definition of Fq</cite>.

$F_q^+$ is the same map with the positive sign, which replaces $\omega$ by $\omega^{-1}$. Applying it after $F_q$ returns the input divided by $q$:

$$
(F_q^+ F_q u)_k = \frac{1}{q^2} \sum_{m=0}^{q-1} u_m \sum_{j=0}^{q-1} \omega^{j(m-k)} = \frac{u_k}{q}.
$$

The inner sum is $q$ when $m = k$. Otherwise $x = \omega^{m-k} \neq 1$ satisfies $x^q = 1$, so the geometric sum $\sum_{j=0}^{q-1} x^j = (x^q - 1)/(x - 1)$ is $0$.

The vector norm used for bounds is the maximum modulus of the coordinates: <cite data-source="paper">The vector norm is the maximum modulus of its coordinates.</cite> A linear map $L$ is a contraction when $\|Lu\| \le \|u\|$ for every $u$. <cite data-source="paper">Each normalized Fourier transform above is a contraction, since each output averages inputs multiplied by complex numbers of modulus one.</cite>

Worked example. Take $q = 4$. Then $\omega = e^{-2\pi i/4} = -i$, so $\omega^0 = 1$, $\omega^1 = -i$, $\omega^2 = -1$ and $\omega^3 = i$. For $u = (1, 2, 3, 4)$,

$$
(F_4 u)_0 = \tfrac{1}{4}(1+2+3+4) = \tfrac{5}{2}, \qquad (F_4 u)_1 = \tfrac{1}{4}(1-2i-3+4i) = \tfrac{-1+i}{2},
$$

$$
(F_4 u)_2 = \tfrac{1}{4}(1-2+3-4) = -\tfrac{1}{2}, \qquad (F_4 u)_3 = \tfrac{1}{4}(1+2i-3-4i) = \tfrac{-1-i}{2}.
$$
