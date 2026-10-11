A transform round is one stage of the [multidimensional transform](multidimensional-transform.md): every participating axis takes one butterfly step at once, then the twiddles are applied. It is the basic step of the transforms behind [convolution over the polynomial ring](polynomial-ring-convolution.md). Its claim is that the round is a contraction in the array norm $\|X\|$ of an array $X$, the largest modulus of its entries.

A *butterfly* on one axis takes each pair of entries $u,v$ that differ only in one address bit to $\left(\frac{u+v}{2},\frac{u-v}{2}\right)$, their half-sum and half-difference, the two-point map $H_0$. A *twiddle* is a power of $y$ by which a record is multiplied after a butterfly.

Let $D$ be the number of participating axes, and let $i$ index them (the letter changes meaning here). Let $\ell_i$ be the current recursive length of axis $i$, the entries it holds at the level processed. Let $\beta_i\in\{0,1\}$ be the branch bit the round writes on axis $i$. Let $\nu_i$ be the index of the twiddle on axis $i$, with $0\le\nu_i<\ell_i/2$.

Address bits are processed <cite data-source="paper">from most to least significant.</cite> The bit receiving $\beta_i$ is the highest unprocessed bit $h$. <cite data-source="paper">Writing xv for the bit in a still unprocessed slot v, the index used by its twiddle is</cite> $\nu_i=\sum_{v=0}^{h-1}2^v x_v$, where $x_v$ is the bit at position $v$. <cite data-source="paper">Previously written branch bits do not enter k.</cite>

At current length $\ell$, the branch-1 output is multiplied by $\omega_\ell^{-\nu}$, where $\omega_\ell=y^{2r/\ell}$ is a primitive $\ell$-th root of unity in $\mathbb{C}[y]/(y^r+1)$. <cite data-source="paper">Multiply the b = 1 output by ωt−k</cite>. <cite data-source="paper">The twiddle for axis i depends only on</cite> <cite data-source="paper">that axis’s address bits.</cite> So axis $i$ contributes $y^{-(2r/\ell_i)\beta_i\nu_i}$ at each address.

<cite data-source="paper">A round applies one current H0 on each participating axis.</cite> <cite data-source="paper">The two entries paired by another axis’s butterfly have the same axis-i</cite> <cite data-source="paper">address, so that twiddle commutes with the other butterfly.</cite> Since $H_0(cu,cv)=c\,H_0(u,v)$, a factor common to the pair moves past the butterfly. Hence the individual axis steps <cite data-source="paper">may be grouped as a parallel butterfly H, followed by one recordwise monomial operation JE</cite>.

The parallel butterfly $\mathcal{H}$ applies $H_0$ on every participating axis. A transform round computes its butterfly by the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), which applies $\mathcal{H}$ in one pass. The letter $\eta$ changes meaning here: it is the twiddle exponent at each address, an integer taken modulo $2r$, given by

$$
\eta = -\sum_{i} \frac{2r}{\ell_i}\,\beta_i\,\nu_i \pmod{2r},
$$

summed over the $D$ participating axes. <cite data-source="paper">The exponent depends on the address, not on</cite> <cite data-source="paper">coefficient values.</cite> The monomial operation $\mathcal{J}_\eta$ multiplies each record by $y^\eta$ at its address.

Write $\eta=er+\delta$ with $0\le\delta<r$, where $e$ is the integer quotient of $\eta$ by $r$, the number of whole multiples of $r$ in $\eta$ (the letter $e$ changes meaning here), and $\delta$ is the remainder. Since $y^r=-1$, $y^\eta=(-1)^e\,y^\delta$. Multiplying by $y^\delta$ shifts coefficients up $\delta$ places, negating those that pass the top. The source does this by <cite data-source="paper">put its tail before its head, negate the moved tail, and apply the common sign</cite>.

Take $r=4$, $D=2$, $\ell_1=\ell_2=4$, $\beta_1=1$, $\nu_1=1$, $\beta_2=0$, $\nu_2=1$. Then $\eta=-(2\cdot1\cdot1+2\cdot0\cdot1)\bmod 8=6$, and $y^6=-y^2$ modulo $y^4+1$. With the record $c_0+c_1y+c_2y^2+c_3y^3$, where $c_j$ is the coefficient of $y^j$, the coefficient list $(c_0,c_1,c_2,c_3)$ becomes $(c_2,c_3,-c_0,-c_1)$.

A *contraction* is a linear map that does not increase the array norm, and an *isometry* preserves it. A single $H_0$ sends $(u,v)$ to values of modulus at most $\max(|u|,|v|)$, so $H_0$, and hence $\mathcal{H}$, is a contraction. Multiplying by $y^\eta$ only moves coefficients and changes signs, so $\mathcal{J}_\eta$ is an isometry. <cite data-source="paper">Each H is a contraction and each JE is an isometry</cite>, so the round is a contraction.
