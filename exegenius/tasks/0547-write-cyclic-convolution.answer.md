Cyclic convolution is the product of two sequences of equal length in which an index that runs past the end wraps around to the start. The paper's algorithm for [Integer multiplication below n log n](main-theorem.md) needs it for its layout and its middle transform.

For sequences $f = (f_0, \dots, f_{n-1})$ and $g = (g_0, \dots, g_{n-1})$, indices are read modulo $n$, so $g_{-1}$ means $g_{n-1}$. Write $k$ for the output position and $j$ for the position in $f$ of each summand. The cyclic convolution $f \ast g$ has entries

$$(f \ast g)_k = \sum_{j=0}^{n-1} f_j \, g_{(k-j) \bmod n}, \qquad 0 \le k < n.$$

A negative $k-j$ wraps around to the end of $g$.

Identify $f$ with $f(w) = \sum_{j=0}^{n-1} f_j w^j$, where $w$ is a formal variable of this page. Then $f \ast g$ is the product in the [polynomial ring](polynomial-ring.md) $\mathbb{C}[w]/(w^n-1)$: form $f(w)g(w)$, replace each $w^e$ with $e \ge n$ by $w^{e-n}$, and read off the coefficients. This works because $w^n = 1$ in the quotient.

Take $n = 4$, $f = (1, 2, 3, 4)$ and $g = (1, 1, 0, 0)$. Their ordinary product is $1 + 3w + 5w^2 + 7w^3 + 4w^4$. Replacing $w^4$ by $1$ gives $f \ast g = (5, 3, 5, 7)$.

The first step is the coefficient layout, which follows Agarwal and Cooley's split. Write $d$ for the number of axes, and let axis $\kappa$, $1 \le \kappa \le d$, have length $n_\kappa$. A cyclic convolution of length $n = n_1 \cdots n_d$, with pairwise coprime $n_1, \dots, n_d$ (no common factor above 1), is split by the [Chinese remainder theorem](chinese-remainder-theorem.md) into a $d$-dimensional cyclic convolution. The paper notes that <cite data-source="paper">Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional</cite> cyclic convolution. Its layout is motivated by the step <cite data-source="paper">we first place the ordinary coefficient stream in its tensor order</cite>, with coordinate powers that <cite data-source="paper">make the change of order a sequence of controlled cyclic shifts</cite>.

The layout is built from positive integers $\mu_\kappa$, each of which has a [Modular inverse](modular-inverse.md) modulo $n_\kappa$. Let $\nu_\kappa$ be the variable of axis $\kappa$, and let $\Phi$ send $w$ to $\prod_\kappa \nu_\kappa^{\mu_\kappa}$, a map into $\mathbb{C}[\nu_1,\dots,\nu_d]/(\nu_\kappa^{n_\kappa}-1)$. It is well defined because $\Phi(w)^n = 1$, each $n_\kappa$ dividing $n$.

Then $\Phi(w^k) = \prod_\kappa \nu_\kappa^{\mu_\kappa k \bmod n_\kappa}$, so index $k$ lands at the position with axis exponents $\mu_\kappa k \bmod n_\kappa$. These positions are distinct for $0 \le k < n$. If $k$ and $k'$ collided, then $n_\kappa$ divides $\mu_\kappa(k-k')$ for every $\kappa$. Invertibility of $\mu_\kappa$ gives $k \equiv k' \pmod{n_\kappa}$ for every $\kappa$, and since the $n_\kappa$ are pairwise coprime, the Chinese remainder theorem gives $k \equiv k' \pmod n$, hence $k = k'$. So the $n$ images are distinct, there are $n = \prod_\kappa n_\kappa$ target monomials, and $\Phi$ is bijective. The paper concludes: <cite data-source="paper">Hence Φ is an isomorphism and preserves cyclic</cite> convolution.

A ring isomorphism sends products to products, so $\Phi(f \ast g) = \Phi(f)\Phi(g)$. Multiplying monomials adds exponents modulo each $n_\kappa$, a cyclic convolution along each axis.

The second step is the middle transform. Write $t$ for the even transform length, so $t$ counts the entries of each sequence transformed. Let $\omega = e^{2\pi i/t}$, and let $F_t u$ have entries $\sum_{j=0}^{t-1} \omega^{jk} u_j$. The paper's middle factor $QFt$ in equation (35) is a Fourier-type transform, and <cite data-source="paper">The factor QFt in (35) can be computed from a cyclic convolution</cite> with two pointwise phase multiplications. On one axis, that is the following identity.

Since $2jk = j^2 + k^2 - (k-j)^2$, we have $\omega^{jk} = \sigma_j \sigma_k \rho(k-j)$, where $\sigma_j = e^{\pi i j^2/t}$ and $\rho(\delta) = e^{-\pi i \delta^2/t}$ for an integer $\delta$. Because $t$ is even, $\rho(\delta+t) = \rho(\delta)$, so $\rho$ is a sequence of length $t$ read modulo $t$. Hence $F_t u = \sigma \cdot \big((\sigma \cdot u) \ast \rho\big)$, where $\cdot$ is the coordinatewise product: two pointwise phase multiplications around one cyclic convolution of length $t$.
