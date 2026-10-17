Retained frequency order is the bit-reversed order in which the forward transform leaves its outputs, kept by the pointwise product and consumed by the opposite transform, so no reordering is executed.

It orders the outputs of the [synthetic polynomial transform](synthetic-transform.md) $F_t^-$ over $\mathcal R_r$, where $t$ is the transform length and $a=\log_2t$ the number of rounds. For $z\in\mathcal R_r^t$,

$$(F_t^-z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{-jk}z_k,\qquad (F_t^+z)_j=\frac1t\sum_{k=0}^{t-1}\omega_t^{jk}z_k.$$

For $t$ a power of two dividing $2r$, define $\omega_t=y^{2r/t}$; every power of $\omega_t$ is an isometry, so each entry is an average of $t$ isometric images and both normalized transforms are contractions.

The ring has zero divisors, so one cannot divide by $\omega_t^j-1$; instead $\sum_{k=0}^{t-1}\omega_t^{jk}$ equals $t$ if $t\mid j$ and $0$ otherwise. Hence $F_t^+F_t^-=t^{-1}I$. For $t\nmid j$, write $j=2^vj_0$ with $j_0$ odd. Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies the sum $S$ by $y^{rj_0}=-1$. Hence the sum is zero, since the additive group of $\mathcal R_r$ has no two-torsion <cite data-source="paper">Hence the sum is zero, since the additive group of</cite>.

Decimation in frequency pairs $z_k$ with $z_{k+t/2}$. Writing the output index as $2h+b$, $b\in\{0,1\}$, and using $\omega_t^{t/2}=-1$,

$$(F_t^-z)_{2h+b}=\frac1{t/2}\sum_{k=0}^{t/2-1}(\omega_t^2)^{-hk}\,\omega_t^{-bk}\,\frac{z_k+(-1)^bz_{k+t/2}}2 .$$

With $H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ the two-point butterfly, apply $H_0$ to each pair, multiply the $b=1$ output by $\omega_t^{-k}$, and recurse on the two length-$t/2$ branches.

After all $a$ rounds the named slots from high to low hold the frequency bits from low to high, so $(F_t^-z)_j$ is stored at slot $\operatorname{rev}_a(j)$, where $\operatorname{rev}_a$ reverses the $a$ binary digits. Let $B_t$ be the permutation moving the entry at $j$ to $\operatorname{rev}_a(j)$ <cite data-source="paper">Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$.</cite> The pointwise product acts slotwise, keeping this order <cite data-source="paper">retain the same frequency order through their pointwise product</cite>.

The opposite procedure runs the levels backwards; since $H_0^2=I/2$, each reversed level is half the inverse of the forward level, over $a=\log_2t$ levels. The reverse procedure composed with $B_tF_t^-$ is $2^{-a}I=I/t$, and as $F_t^+B_t^{-1}B_tF_t^-=F_t^+F_t^-=I/t$ by character cancellation, the two reverse operators agree. So the two exact procedures implement $B_tF_t^-$ and $F_t^+B_t^{-1}$.

With several axes, a round applies $H_0$ on every axis at once, one parallel butterfly $\mathcal H$. Each axis's twiddle depends only on its own address bits, so twiddles commute with the other axes' butterflies and group into one recordwise monomial $J_E$ that multiplies the record by $y^E$, with

$$E=-\sum_i\frac{2r}{u_i}\,b_ik_i\pmod{2r}.$$

Here $u_i$ is axis $i$'s current length, $b_i$ its new branch bit and $k_i$ the index encoded by its unprocessed slots, so $E$ depends on the address, not on coefficient values. Each $\mathcal H$ is a contraction and each $J_E$ an isometry, so every completed round is a contraction.
