Cyclic convolution is the product of two sequences of equal length in which an index that runs past the end wraps around to the start. The paper's algorithm for [Integer multiplication below n log n](main-theorem.md) uses it to lay out coefficients on several cyclic axes and to compute its middle transform.

For sequences $a = (a_0, \dots, a_{n-1})$ and $b = (b_0, \dots, b_{n-1})$, indices are read modulo $n$, so $b_{-1}$ means $b_{n-1}$. The cyclic convolution $a \ast b$ has entries

$$(a \ast b)_t = \sum_{s=0}^{n-1} a_s \, b_{(t-s) \bmod n}, \qquad 0 \le t < n,$$

where $s$ is the summation index, the position in $a$ of each summand. A negative $t-s$ wraps around to the end of $b$.

Identify $a$ with $a(w) = \sum_{s=0}^{n-1} a_s w^s$, where $w$ is a formal variable (a symbol, not a number). Then $a \ast b$ is the product in the [polynomial ring](polynomial-ring.md) $\mathbb{C}[w]/(w^n-1)$: multiply $a(w)$ by $b(w)$, replace each $w^e$ with $e \ge n$ by $w^{e-n}$, and read off the coefficients. This works because $w^n = 1$ in the quotient.

Take $n = 4$, $a = (1, 2, 3, 4)$ and $b = (1, 1, 0, 0)$. Their ordinary product is $1 + 3w + 5w^2 + 7w^3 + 4w^4$, and replacing $w^4$ by $1$ gives $a \ast b = (5, 3, 5, 7)$.

A cyclic convolution of length $n$ is split by the [Chinese remainder theorem](chinese-remainder-theorem.md) into a $D$-dimensional cyclic convolution when $n = n_1 \cdots n_D$ with $n_1, \dots, n_D$ pairwise coprime (no common factor above 1). Here $\kappa$ is an axis index, not the constant $\kappa$ of the time bound, and axis $\kappa$ has length $n_\kappa$, the number of values its coordinate takes. The paper attributes this split to Agarwal and Cooley: <cite data-source="paper">Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional</cite> cyclic convolution. The paper's map uses this split <cite data-source="paper">with coordinate powers that make the change of order a sequence of controlled cyclic shifts</cite>.

The layout relies on a [Modular inverse](modular-inverse.md) modulo $n_\kappa$ for each multiplier $\mu_\kappa$, which is a positive integer. Let $\nu_\kappa$ be the variable of axis $\kappa$, with $\nu_\kappa^{n_\kappa} = 1$, and let $\Phi$ be the map that sends $w$ to $\prod_\kappa \nu_\kappa^{\mu_\kappa}$. A monomial is a product of powers of the $\nu_\kappa$. Since $n_\kappa \mid n$ for every $\kappa$, $\Phi(w)^n = 1$, so $\Phi$ is a ring homomorphism (a map preserving sums and products) from $\mathbb{C}[w]/(w^n-1)$ to $\mathbb{C}[\nu_1,\dots,\nu_D]/(\nu_1^{n_1}-1,\dots,\nu_D^{n_D}-1)$.

Then $\Phi(w^t) = \prod_\kappa \nu_\kappa^{\mu_\kappa t \bmod n_\kappa}$, so index $t$ lands on the monomial with exponents $\mu_\kappa t \bmod n_\kappa$. These $n$ monomials are distinct for $0 \le t < n$. If two indices $t, t'$ gave the same monomial, then $n_\kappa \mid \mu_\kappa(t-t')$ for every $\kappa$, so $n_\kappa \mid t-t'$ because $\mu_\kappa$ is invertible modulo $n_\kappa$. The $n_\kappa$ are pairwise coprime, so $n \mid t-t'$ and $t = t'$. The target contains $n_1 \cdots n_D = n$ monomials, so $\Phi$ carries the basis $1, w, \dots, w^{n-1}$ onto the monomial basis and is a bijection. The paper concludes: <cite data-source="paper">Hence Φ is an isomorphism and preserves cyclic</cite> convolution. An isomorphism is a bijective ring homomorphism, so $\Phi(a \ast b) = \Phi(a)\Phi(b)$. Multiplying two monomials adds their exponents modulo each $n_\kappa$, so the convolution becomes a cyclic convolution along each axis.

Let $q$ be an even transform length, $\omega = e^{-2\pi i/q}$, and let $F_q$ be the discrete Fourier transform, $(F_q u)_\ell = \sum_{s=0}^{q-1} \omega^{s\ell} u_s$ for $0 \le \ell < q$. The paper states that <cite data-source="paper">The factor QFt in (35) can be computed from a cyclic convolution and two pointwise phase</cite> multiplications. The identity below shows how a length-$q$ transform becomes one cyclic convolution with two pointwise phase multiplications.

Let $\phi_s = e^{-\pi i s^2/q}$ and $\psi_\delta = e^{\pi i \delta^2/q}$ for integers $s$ and $\delta$; here $\phi$ and $\psi$ are local names, used only in this section. Since $2s\ell = s^2 + \ell^2 - (\ell-s)^2$, we have $\omega^{s\ell} = \phi_s\,\phi_\ell\,\psi_{\ell-s}$. Since $q$ is even, $\psi_{\delta+q} = \psi_\delta$, so $\psi$ has period $q$. Write $\phi$ and $\psi$ also for the vectors $(\phi_0,\dots,\phi_{q-1})$ and $(\psi_0,\dots,\psi_{q-1})$, and $\cdot$ for the coordinatewise product of vectors. Then

$$F_q u = \phi \cdot \big((\phi \cdot u) \ast \psi\big).$$

The $\ell$-th entry of the right side is $\phi_\ell \sum_s \phi_s u_s \psi_{(\ell-s) \bmod q}$, which equals $\sum_s \omega^{s\ell} u_s$ by the identity. For $q = 2$, $\omega = -1$, $\phi = (1, -i)$ and $\psi = (1, i)$, and the formula gives $(u_0 + u_1, u_0 - u_1)$.
