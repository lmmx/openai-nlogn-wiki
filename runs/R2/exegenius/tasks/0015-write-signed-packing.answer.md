Signed coefficient packing (Kronecker substitution) encodes a polynomial with integer coefficients of either sign as one integer, so that a polynomial product becomes an integer product, which an ordinary $O(n\log n)$ multiplier computes. The page's polynomial products are carried out this way on the way to the main result.

Let $p$ be a precision exponent such that every coefficient of the input polynomials has absolute value at most $2^p$. Let $B=2^{4p}$ be the block base. For a polynomial $u=\sum_{j=0}^{r-1}u_j y^j$ in $\mathbb Z[y]$ with $|u_j|\le 2^p$, the packed integer is
$$u(B)=\sum_{j=0}^{r-1}u_jB^j.$$
Evaluating $u$ at $B$ means substituting $B$ for $y$. Negative coefficients need no special treatment as integers: the sum is an ordinary integer, possibly negative. On tapes the integer is stored as $r$ blocks, with carries chosen so that each block is a digit in $[0,B)$ and the sign sits at the top. Each block is $4p$ bits wide. <cite data-source="paper">Every block has $4p$ bits</cite>.

Evaluation at $B$ respects products: $u(B)\,v(B)=(uv)(B)$ exactly, where $uv$ is the ordinary product in $\mathbb Z[y]$, before reduction modulo $y^r+1$. One integer product of two packed integers therefore yields all coefficients of the polynomial product at once. Signed coefficient packing computes its integer products by the [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md), an ordinary subroutine call that costs $O(n\log n)$.

Recovering the coefficients. Write $h=uv$ and $h_j$ for its coefficients. They satisfy $|h_j|\le r2^{2p}<B/2$, because $r<2^p$. Under this bound, each coefficient is the centered residue of what remains, and the centered range makes that residue unique. <cite data-source="paper">this strict bound identifies the next coefficient by its centered residue modulo $B_0$</cite>. Concretely, let $h_0$ be the unique integer in $[-B/2,B/2)$ congruent to $h(B)$ modulo $B$, subtract it, divide by $B$, and repeat to obtain $h_1,h_2,\dots$.

Example. Take $B=12$, $u=2-y$ and $v=1+3y$. Then $u(12)=-10$ and $v(12)=37$, so the packed product is $-370$. Modulo 12, $-370\equiv 2$, and $2\in[-6,6)$, so $h_0=2$ and $(-370-2)/12=-31$. Next, $-31\equiv 5$, so $h_1=5$ and $(-31-5)/12=-3=h_2$. Thus $uv=2+5y-3y^2$, which agrees with direct expansion.

In the main argument, each Gaussian-integer product of polynomial records is formed by packing its component polynomials, multiplying the resulting integers with the ordinary multiplier, and unpacking the signed results.
