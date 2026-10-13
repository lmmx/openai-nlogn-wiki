Signed coefficient packing (Kronecker substitution) encodes a polynomial with integer coefficients of either sign as one integer, so that a polynomial product becomes an integer product, which an ordinary $O(n\log n)$ multiplier computes.

Let $p$ be a precision exponent, a quantity different from the working precision of earlier pages, such that every coefficient of the input polynomials has absolute value at most $2^p$, and let $B=2^{4p}$ be the block base. For $u=\sum_{j=0}^{r-1}u_j y^j$ in $\mathbb Z[y]$ with $|u_j|\le 2^p$, the packed integer is
$$u(B)=\sum_{j=0}^{r-1}u_jB^j.$$
Here $j$ and $t$ are coefficient positions, and $r$ is the number of coefficients. The sum may be negative. Reused letters are defined at first use.

On tapes, a carry $\gamma_j$ and a block digit $d_j$ satisfy $\gamma_0=0$, $0\le d_j<B$, $d_j\equiv u_j+\gamma_j \pmod B$, and $\gamma_{j+1}=(u_j+\gamma_j-d_j)/B$. Each $\gamma_j$ stays in $\{-1,0\}$, since $u_j+\gamma_j$ lies in $(-B,B)$. Telescoping gives $u(B)=\sum_j d_jB^j+\gamma_rB^r$. So the blocks are nonnegative digits, and the sign is the final carry $\gamma_r$, a sign extension above the top block. Each block is $4p$ bits wide <cite data-source="paper">Every block has $4p$ bits</cite>.

Evaluation respects products: for a second input polynomial $v=\sum_{t=0}^{r-1}v_t y^t$ with $|v_t|\le 2^p$, $u(B)\,v(B)=(uv)(B)$ exactly, where $uv$ is the ordinary product in $\mathbb Z[y]$. Signed coefficient packing computes its integer products by the [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md), an ordinary subroutine call that costs $O(n\log n)$.

Recovering the coefficients. Write $h=uv$ for that product, and $h_k$ for its coefficient of $y^k$, with $k$ running over $0,\dots,2r-2$. Each $h_k$ sums at most $r$ products $u_jv_t$, so $|h_k|\le r2^{2p}$. The packing lemma assumes $r<2^p$ with $p\ge 2$ <cite data-source="paper">Let $r=2^\ell<2^p$ with integers $\ell\geq1$ and $p\geq2$</cite>, so $|h_k|<2^{3p}\le B/2$. Since every $h_kB^k$ with $k\ge1$ is a multiple of $B$, $h(B)\equiv h_0 \pmod B$. As $|h_0|<B/2$, $h_0$ is the unique integer in $[-B/2,B/2)$ congruent to $h(B)$ modulo $B$. Subtracting it and dividing by $B$ leaves the same form for $h_1,h_2,\dots$.

Example with $B=12$. For $u=2-y$ and $v=1+3y$, $u(12)=-10$ and $v(12)=37$, so the packed product is $-370$. Since $-370\equiv 2 \pmod{12}$ and $2\in[-6,6)$, $h_0=2$ and $(-370-2)/12=-31$. Then $-31\equiv 5$, so $h_1=5$ and $h_2=-3$, giving $uv=2+5y-3y^2$.

Gaussian products. A polynomial record is a polynomial of degree less than $r$ with complex fixed-point coefficients, stored on a tape. A record $f=2^{-p}(a+\sqrt{-1}\,b)$ has real and imaginary components $a,b\in\mathbb Z[y]$, whose coefficients are at most $2^p$ in absolute value <cite data-source="paper">The truncated numerators have magnitude at most $2^p$</cite>. The second record $g=2^{-p}(c+\sqrt{-1}\,e)$ has components $c,e\in\mathbb Z[y]$, and the product is
$$(a+\sqrt{-1}\,b)(c+\sqrt{-1}\,e)=(ac-be)+\sqrt{-1}\,(ae+bc).$$
The four ordinary products $ac$, $be$, $ae$, $bc$ are each one packed product. Each is unpacked to exact coefficients before subtraction or addition, so the bound $|h_k|<B/2$ holds for each product, not for the sums.
