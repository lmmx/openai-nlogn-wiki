A transform round computes one stage of the [multidimensional transform](multidimensional-transform.md): every participating axis takes one butterfly step at once, then the twiddles are applied. It is the basic step of the transforms behind [convolution over the polynomial ring](polynomial-ring-convolution.md), and its claim is that a round is a contraction in the array norm.

A [butterfly](butterfly.md) replaces each pair of entries $u,v$ on one axis by $\left(\frac{u+v}{2},\frac{u-v}{2}\right)$, the map $H_0$. A *twiddle* is a power $y^k$ of $y$, the indeterminate of $\mathbb{C}[y]/(y^r+1)$, that multiplies a record after a butterfly. Since $y^r=-1$, we have $y^{2r}=1$.

Let $D$ be the number of participating axes, and let $i$ index them (the letter $i$ changes meaning here). Axis $i$ has current recursive length $\ell_i$, a power of two dividing $2r$. Let $\beta_i\in\{0,1\}$ be the branch bit the round writes on axis $i$ (the letter $\beta$ changes meaning here), and $\nu_i$ its twiddle index, an integer with $0\le\nu_i<\ell_i/2$.

Address bits are processed <cite data-source="paper">from most to least significant.</cite> The bit that receives $\beta_i$ is the highest unprocessed bit $h$ of axis $i$ (the letter $h$ changes meaning here). Let $x_v$ be the bit in still unprocessed slot $v$ of axis $i$; the twiddle index is $\nu_i=\sum_{v=0}^{h-1}2^v x_v$. <cite data-source="paper">Previously written branch bits do not enter k.</cite>

Here $\omega_\ell=y^{2r/\ell}$ for a power of two $\ell$ dividing $2r$. It is a primitive $\ell$-th root of unity: $y^k=\pm y^{k\bmod r}\ne1$ for $0<k<2r$, so $y$ has order $2r$, and $(y^{2r/\ell})^j=1$ exactly when $\ell\mid j$. <cite data-source="paper">Multiply the b = 1 output by ωt−k</cite>: the branch-1 output of axis $i$ is multiplied by $\omega_{\ell_i}^{-\nu_i}$. Hence axis $i$ contributes $y^{-(2r/\ell_i)\beta_i\nu_i}$ at each address.

<cite data-source="paper">A round applies one current H0 on each participating axis.</cite> The twiddle for axis $i$ depends only on <cite data-source="paper">that axis’s address bits.</cite> The two entries paired by another axis's butterfly share their axis-$i$ address, so they receive the same twiddle $c$. Since $H_0(cu,cv)=c\,H_0(u,v)$, the factor moves past that butterfly. The axis steps may therefore be grouped: <cite data-source="paper">may be grouped as a parallel butterfly H, followed by one recordwise monomial operation JE</cite>.

The parallel butterfly $\mathcal{B}$ applies $H_0$ on every participating axis. A transform round computes its butterfly by the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), which applies $\mathcal{B}$ in one pass. Since $y^a y^b=y^{a+b}$, the per-axis factors multiply. The twiddle exponent at an address is $\eta$, given by

$$
\eta = -\sum_{i} \frac{2r}{\ell_i}\,\beta_i\,\nu_i \pmod{2r},
$$

summed over the $D$ participating axes. The monomial operation $\mathcal{M}_\eta$ multiplies each record by $y^\eta$ at its address.

Let $e$ be the integer quotient of $\eta$ by $r$, the number of whole multiples of $r$ in $\eta$ (the letter $e$ changes meaning here). Likewise $\delta$ is the remainder (the letter $\delta$ changes meaning here), so $\eta=er+\delta$ with $0\le\delta<r$. Since $y^r=-1$, $y^\eta=(-1)^e y^\delta$. Multiplying by $y^\delta$ moves each coefficient $c_j$ of $y^j$ to position $j+\delta$; one passing position $r-1$ wraps to position $j+\delta-r$ with its sign negated. The sign $(-1)^e$ applies to the whole record.

Take $r=4$, $D=2$, $\ell_1=\ell_2=4$, $\beta_1=1$, $\nu_1=1$, $\beta_2=0$, $\nu_2=1$. Then $\eta=-(2+0)\bmod 8=6=1\cdot4+2$, so $y^6=-y^2$, and the record $c_0+c_1y+c_2y^2+c_3y^3$ becomes $c_2+c_3y-c_0y^2-c_1y^3$.

A *contraction* is a linear map that does not increase the array norm $\|X\|$, the largest modulus of any coefficient of any record: <cite data-source="paper">the same notation denotes the maximum over all coefficients in all entries.</cite> An *isometry* preserves it. A coefficient of $(u\pm v)/2$ has modulus at most $\max(|u|,|v|)\le\|X\|$, so each axis step is a contraction, and applying the axis steps in turn gives $\mathcal{B}$, also a contraction. Multiplying by $y^\eta$ <cite data-source="paper">permutes the coefficients and changes some signs; consequently it is an isometry for this norm.</cite> <cite data-source="paper">Each H is a contraction and each JE is an isometry</cite>, so the round is a contraction: $\|\mathcal{M}_\eta\mathcal{B}X\|\le\|\mathcal{B}X\|\le\|X\|$.
