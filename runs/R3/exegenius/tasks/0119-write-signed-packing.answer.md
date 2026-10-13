Signed coefficient packing (Kronecker substitution) encodes a polynomial with integer coefficients of either sign as one integer, so that a polynomial product becomes an integer product, which an ordinary $O(n\log n)$ multiplier computes.

Let $p$ be the working precision of the fixed-point page, so each coefficient of an input polynomial is an integer of absolute value at most $2^p$. Let $B=2^{4p}$ be the block base. Let $u=\sum_{j=0}^{r-1}u_j y^j$ denote a polynomial in $\mathbb Z[y]$ with $|u_j|\le 2^p$; its packed integer is
$$u(B)=\sum_{j=0}^{r-1}u_jB^j.$$
Here $j$ and $t$ are coefficient positions; the sum may be negative.

On tapes, a carry $\gamma_j$ and a block digit $d_j$ satisfy $\gamma_0=0$, $0\le d_j<B$, $d_j\equiv u_j+\gamma_j \pmod B$, and $\gamma_{j+1}=(u_j+\gamma_j-d_j)/B$. Each $\gamma_j$ stays in $\{-1,0\}$, since $u_j+\gamma_j$ lies in $(-B,B)$. Telescoping gives $u(B)=\sum_j d_jB^j+\gamma_rB^r$. So the blocks are nonnegative digits, and the sign is the final carry $\gamma_r$. Each block is $4p$ bits wide <cite data-source="paper">Every block has $4p$ bits</cite>.

Evaluation respects products: let $v=\sum_{t=0}^{r-1}v_t y^t$ denote a second input polynomial with $|v_t|\le 2^p$. Then $u(B)\,v(B)=(uv)(B)$ exactly, where $uv$ is the ordinary product in $\mathbb Z[y]$. Signed coefficient packing computes its integer products by the [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md), an ordinary subroutine call that costs $O(n\log n)$.

Recovering the coefficients. Write $h=uv$, and $h_k$ for its coefficient of $y^k$, with $k$ running over $0,\dots,2r-2$. Each $h_k$ sums at most $r$ products $u_jv_t$, so $|h_k|\le r2^{2p}$. Recovery needs $|h_k|<B/2$, which holds because $r<2^p$: the ring degree is at most the padded length, $r\le T$ <cite data-source="paper">t_i\leq r\leq T</cite>, and $T<2^p$ for sufficiently large inputs by the choice of $p$ on the fixed-point page. Hence $|h_k|\le r2^{2p}<2^{3p}<B/2$. Since every $h_kB^k$ with $k\ge1$ is a multiple of $B$, $h(B)\equiv h_0 \pmod B$. As $|h_0|<B/2$, $h_0$ is the unique integer in $[-B/2,B/2)$ congruent to $h(B)$ modulo $B$. Subtracting it and dividing by $B$ leaves the same form for $h_1,h_2,\dots$.

Example with $B=12$. For $u=2-y$ and $v=1+3y$, $u(12)=-10$ and $v(12)=37$, so the packed product is $-370$. Recovery gives $h_0=2$, $h_1=5$, $h_2=-3$, so $uv=2+5y-3y^2$.

Gaussian products. A record is a polynomial of degree less than $r$ with complex fixed-point coefficients. A record $f=2^{-p}(a+\sqrt{-1}\,b)$ has real and imaginary components $a,b\in\mathbb Z[y]$. Records have norm at most one, so their parts lie in $[-1,1]$ <cite data-source="paper">A disk array has norm at most one.</cite>. Truncation puts each part on the grid $2^{-p}\mathbb Z$, so $2^p$ times each part is an integer, and its coefficients are at most $2^p$ in absolute value <cite data-source="paper">The truncated numerators have magnitude at most $2^p$</cite>. The second record $g=2^{-p}(c+\sqrt{-1}\,e)$ has components $c,e\in\mathbb Z[y]$, and the product is
$$(a+\sqrt{-1}\,b)(c+\sqrt{-1}\,e)=(ac-be)+\sqrt{-1}\,(ae+bc).$$
The four ordinary products $ac$, $be$, $ae$, $bc$ are each one packed product. Each is unpacked to exact coefficients before subtraction or addition, so the bound $|h_k|<B/2$ holds for each product, not for the sums.
