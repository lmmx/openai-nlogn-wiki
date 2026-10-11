A bilinear map is the form of product whose error the paper's convolution analysis bounds, one operand at a time. Two later pages rely on this bound.

A bilinear map is defined through the linear maps of [Linear algebra basics](linear-algebra-basics.md): fixing one argument must give a linear map in the other. Let $J_1$ be the space of first arguments, $J_2$ the space of second arguments, and $\Psi$ the output space, all over the field $F$. Let $\pi\colon J_1\times J_2\to\Psi$ send each pair $(\xi,\zeta)$, with $\xi\in J_1$ and $\zeta\in J_2$, to a vector $\pi(\xi,\zeta)$ in $\Psi$. The map $\pi$ is *bilinear* when $\xi\mapsto\pi(\xi,\zeta)$ is linear for each fixed $\zeta$, and $\zeta\mapsto\pi(\xi,\zeta)$ is linear for each fixed $\xi$.

Let $J_1=J_2=\mathbb{C}^2$ and $\Psi=\mathbb{C}$, and let $\pi$ send a pair of vectors to the sum of their coordinatewise products. Then $\pi\big((1,2),(3,4)\big)=1\cdot 3+2\cdot 4=11$, and doubling the first argument doubles the output: $\pi\big((2,4),(3,4)\big)=22$. Adding a constant breaks bilinearity: $(\xi,\zeta)\mapsto\pi(\xi,\zeta)+1$ sends $(0,\zeta)$ to $1$, but a linear map in $\xi$ must send $0$ to $0$.

In the paper, $J_1$, $J_2$, and $\Psi$ are spaces of [Array](array.md) values, so a bilinear map acts on arrays. A bilinear map is a *bilinear contraction* when it is bounded in the [Array norm](array-norm.md): $\|\pi(\xi,\zeta)\|\le\|\xi\|\,\|\zeta\|$. For arrays whose entries are records (polynomials in $y$ modulo $y^r+1$), <cite data-source="paper">over Rr , the same notation denotes the maximum over all coefficients in all entries.</cite> A *disk array* is an array of norm at most one. <cite data-source="paper">A disk array has norm at most one.</cite> Every entry of a disk array therefore has modulus at most one.

The paper's error analysis works with an exact bilinear map $P$, the pointwise product that multiplies the two entries at each address, with products of records taken modulo $y^r+1$ and divided by $r$. <cite data-source="paper">Let P (u, v) denote the exact pointwise product uv/r</cite>. <cite data-source="paper">The exact map P is bilinear and satisfies ∥P (x, y)∥∞ ≤ ∥x∥∞ ∥y∥∞</cite>, so $P$ is a bilinear contraction.

Let $\pi$ be a bilinear contraction. Let $\xi'$ and $\zeta'$ be computed approximations of $\xi$ and $\zeta$, with all four operands disk arrays. Linearity gives $\pi(\xi',\zeta)-\pi(\xi,\zeta)=\pi(\xi'-\xi,\zeta)$, and since $\zeta$ is a disk array, <cite data-source="paper">replacing one operand changes the output by at most the norm distance between its two values.</cite>

Splitting the change into two single-operand changes,
$$\pi(\xi',\zeta')-\pi(\xi,\zeta)=\pi(\xi'-\xi,\zeta')+\pi(\xi,\zeta'-\zeta).$$
The first term is bounded using the disk bound on $\zeta'$: $\|\pi(\xi'-\xi,\zeta')\|\le\|\xi'-\xi\|\,\|\zeta'\|\le\|\xi'-\xi\|$. The second is bounded by the disk bound on $\xi$: $\|\pi(\xi,\zeta'-\zeta)\|\le\|\xi\|\,\|\zeta'-\zeta\|\le\|\zeta'-\zeta\|$. Adding them gives
$$\|\pi(\xi',\zeta')-\pi(\xi,\zeta)\|\le\|\xi'-\xi\|+\|\zeta'-\zeta\|.$$
<cite data-source="paper">When all four operands are in the disk, their two errors therefore add.</cite>
