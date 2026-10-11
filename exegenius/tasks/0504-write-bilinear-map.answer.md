A bilinear map takes one vector from each of two vector spaces and returns a vector in a third, linear in each argument while the other is held fixed. The paper's error analysis uses one to bound the error of a product of two approximate values, one operand at a time.

A bilinear map is defined through the linear maps of [Linear algebra basics](linear-algebra-basics.md): fixing one argument must give a linear map in the other. Here $U$ and $V$ are the argument spaces and $W$ is the output space, over the scalar field $F$. Let $\pi\colon U\times V\to W$ send each pair $(\xi,\zeta)$, with $\xi\in U$ and $\zeta\in V$, to a vector $\pi(\xi,\zeta)$ in $W$. The map $\pi$ is *bilinear* when $\xi\mapsto\pi(\xi,\zeta)$ is linear for each fixed $\zeta$, and $\zeta\mapsto\pi(\xi,\zeta)$ is linear for each fixed $\xi$.

Let $U=V=\mathbb{C}^2$ and $W=\mathbb{C}$, and let $\pi$ send a pair of vectors to the sum of their coordinatewise products. Then $\pi\big((1,2),(3,4)\big)=1\cdot 3+2\cdot 4=11$, and doubling the first argument doubles the output: $\pi\big((2,4),(3,4)\big)=22$. Adding a constant breaks bilinearity: $(\xi,\zeta)\mapsto\pi(\xi,\zeta)+1$ sends $(0,\zeta)$ to $1$, but a linear map in $\xi$ must send $0$ to $0$.

In the paper, $U$, $V$, and $W$ are spaces of [Array](array.md) values, so a bilinear map is applied to arrays. A bilinear map is a *bilinear contraction* when it is bounded in the [Array norm](array-norm.md): $\|\pi(\xi,\zeta)\|\le\|\xi\|\,\|\zeta\|$. For arrays whose entries are records (polynomials in $y$ modulo $y^r+1$), the norm is the largest coefficient modulus: <cite data-source="paper">over Rr , the same notation denotes the maximum over all coefficients in all entries.</cite> A *disk array* is an array of norm at most one, so every entry has modulus at most one.

The paper's error analysis works with an exact bilinear map $P$: the pointwise product, which multiplies the two entries at each address, with products of records taken modulo $y^r+1$ and then divided by $r$. <cite data-source="paper">The exact map P is bilinear and satisfies</cite> the bound $\|P(\xi,\zeta)\|\le\|\xi\|\,\|\zeta\|$, <cite data-source="paper">by the coefficient bound in</cite> Lemma 17, so $P$ is a bilinear contraction.

Let $\xi'$ and $\zeta'$ be computed approximations of $\xi$ and $\zeta$, and suppose all four are disk arrays. With one operand fixed, linearity gives $\pi(\xi',\zeta)-\pi(\xi,\zeta)=\pi(\xi'-\xi,\zeta)$, and if $\zeta$ is a disk array, $\|\pi(\xi'-\xi,\zeta)\|\le\|\xi'-\xi\|$. So <cite data-source="paper">replacing one operand changes the output by at most the norm</cite> of the difference.

Splitting the change into two single-operand changes,
$$\pi(\xi',\zeta')-\pi(\xi,\zeta)=\pi(\xi'-\xi,\zeta')+\pi(\xi,\zeta'-\zeta).$$
The first term is bounded using the disk bound on $\zeta'$: $\|\pi(\xi'-\xi,\zeta')\|\le\|\xi'-\xi\|\,\|\zeta'\|\le\|\xi'-\xi\|$. The second is bounded by the disk bound on $\xi$: $\|\pi(\xi,\zeta'-\zeta)\|\le\|\xi\|\,\|\zeta'-\zeta\|\le\|\zeta'-\zeta\|$. Adding them gives
$$\|\pi(\xi',\zeta')-\pi(\xi,\zeta)\|\le\|\xi'-\xi\|+\|\zeta'-\zeta\|.$$
<cite data-source="paper">When all four operands are in the disk, their two errors therefore add.</cite>
