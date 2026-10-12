Signed Kronecker packing maps each element of [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md) to a single integer, by evaluating it at a large power of two. It turns products in the ring into integer products, which the established $O(n\log n)$ multiplier computes as an ordinary subroutine.

Signed Kronecker packing is an instance of [Multiplication as convolution of digits](convolution-reduction.md): the coefficients act as digits and the evaluation point as the radix. This evaluation trick is called Kronecker substitution, and signed packing is a form of it <cite data-source="paper">Signed coefficient packing is a form of Kronecker substitution</cite>.

The index $j$ runs over the $r$ coefficient positions, $0 \le j < r$. Let $f$ and $g$ be ring elements with integer coefficients $f_j$ and $g_j$. Let $M$ be a bound on the absolute value of every such coefficient. Here $k$ also indexes coefficient positions, not transform positions.

Fix a power of two $B$ with $B > 2rM^2$, and call $B$ the packing base. The packed integer of $f$ is $F = \sum_j f_j B^j$, which may be negative because the digits are signed. Packing $g$ the same way gives the packed integer $G = \sum_j g_j B^j$.

Let $w = fg$ be the unreduced product, that is, before reduction modulo $y^r+1$, with coefficients $w_k = \sum_j f_j g_{k-j}$, where $k$ is the power of $y$ and the sum runs over $0 \le k-j < r$. Each $w_k$ is a sum of at most $r$ products, each at most $M^2$ in absolute value, so $|w_k| \le rM^2 < B/2$.

Evaluation at $B$ respects sums and products, so $FG = w(B) = \sum_k w_k B^k$. The integer product thus carries the product $w$, and the question is how to read its digits back.

Uniqueness. If $\sum_k e_k B^k = \sum_k e'_k B^k$ with integers satisfying $|e_k|, |e'_k| < B/2$, then $e_k = e'_k$ for all $k$. Each difference $e_k - e'_k$ has absolute value below $B$. Let $m$ be the least index with $e_m \ne e'_m$. Then $e_m - e'_m = -B\sum_{k>m} (e_k - e'_k) B^{k-m-1}$ is divisible by $B$, impossible since $0 < |e_m - e'_m| < B$.

Read-back. $FG - w_0 = B\sum_{k\ge 1} w_k B^{k-1}$ is divisible by $B$, and $|w_0| < B/2$. Since $B$ is even, $(-B/2, B/2]$ holds exactly one integer from each residue class modulo $B$, so $w_0$ is the balanced remainder of $FG$ modulo $B$. Subtracting $w_0$ and dividing by $B$ leaves an expansion of the same form, so repeating the step gives $w_1, w_2, \dots$; uniqueness shows no other digits could give $FG$.

For example, take $r=2$, $B=128$, $f=3-2y$ and $g=1+4y$. Then $M=4$ and $B>2rM^2=64$, $w=3+10y-8y^2$, and $FG=(-253)(513)=-129789$. The balanced remainders are $3$, $10$, $-8$, since $-129789=3+128\bigl(10+128\cdot(-8)\bigr)$.

Finally, $y^r=-1$ gives $y^{k+r}=-y^k$, so $fg$ modulo $y^r+1$ has coefficients $w_k-w_{k+r}$ for $0\le k<r$, where $w_m=0$ for $m>2r-2$. These are recovered exactly from the packed product.
