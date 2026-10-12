Signed Kronecker packing maps each element of [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md) to a single integer, by evaluating it at a large power of two. Its purpose here is to turn products in the ring into integer products, which the established $O(n\log n)$ multiplier can then compute as an ordinary subroutine.

Signed Kronecker packing is an instance of [Multiplication as convolution of digits](convolution-reduction.md): the coefficients play the role of digits, and the evaluation point plays the role of the radix. Signed packing is a form of Kronecker substitution, the name for this evaluation trick <cite data-source="paper">Signed coefficient packing is a form of Kronecker substitution</cite>.

The index $j$ runs over the $r$ coefficient positions, $0 \le j < r$. Take elements $f$ and $g$ of the ring with integer coefficients $f_j$ and $g_j$. Let $M$ be a bound on the absolute value of every such coefficient.

Fix a power of two $B$ with $B > 2rM^2$, and call $B$ the packing base. The packed integer of $f$ is $F = \sum_j f_j B^j$, which may be negative because the digits are signed. Packing $g$ in the same way gives the integer $G = \sum_j g_j B^j$.

Let $h = fg$ be the unreduced product, with coefficients $h_k = \sum_j f_j g_{k-j}$, summed over all valid $j$, where $k$ is the power of $y$. Each $h_k$ is a sum of at most $r$ products, each at most $M^2$ in absolute value, so $|h_k| \le rM^2 < B/2$.

Evaluation at $B$ respects products, so $FG = h(B) = \sum_k h_k B^k$. Because every $|h_k| < B/2$, this signed base-$B$ expansion is unique, so the coefficients can be read back from the integer $FG$. Take its remainder modulo $B$ in the range $(-B/2, B/2]$, subtract it, divide by $B$, and repeat.

For example, take $r=2$, $B=100$, $f=3-2y$ and $g=1+4y$. Here $M=4$ and $B > 2rM^2 = 64$. Then $h = 3+10y-8y^2$ and $FG = (-197)(401) = -78997$. Reading the remainders gives $3$, then $10$, then $-8$, which are the coefficients of $h$.

Finally, since $y^r = -1$ in the ring, the coefficient $h_{k+r}$ is folded into $h_k$ with a minus sign. So $fg$ modulo $y^r+1$ has coefficients $h_k - h_{k+r}$ for $0 \le k < r$, and these are recovered exactly from the packed product.
