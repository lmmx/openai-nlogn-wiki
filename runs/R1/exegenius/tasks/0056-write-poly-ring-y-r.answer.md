The polynomial ring modulo a power-of-two wrap is the ring of complex polynomials in one variable in which the variable's wrap power is identified with $-1$. It is the coefficient ring in which the root multiplications of the remaining transform axes become cheap signed shifts.

Let $y$ be the ring variable, the polynomial variable whose powers act as roots of unity. Let $r$ be the ring degree, the number of complex coefficients in each element, a power of two. In the paper, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$ <cite data-source="paper">with $r$ a power of two</cite>.

An element is a polynomial in $y$ of degree below $r$, stored as its $r$ coefficients from $y^0$ up to $y^{r-1}$. Multiplication is the ordinary product, then the rule $y^{r+j}=-y^j$ for $0\le j<r$, where $j$ indexes the coefficient that $y^{r+j}$ reduces to. The ring is the quotient of $\mathbb{C}[y]$ by the ideal $(y^r+1)$, the set of all multiples of $y^r+1$ by polynomials.

Let $k$ be a shift exponent, not the output index of the convolution page: multiplying by $y^k$, with $0\le k<r$, is a signed shift of the coefficient list. A coefficient pushed past position $r-1$ re-enters at the bottom with its sign reversed. For $r=4$, multiplying $1+2y+3y^2+4y^3$ by $y^3$ gives $-2-3y-4y^2+y^3$, the list $(-2,-3,-4,1)$.

Since $y^r=-1$, we have $y^{2r}=1$, and no smaller positive power equals $1$. So $y$ is a primitive $2r$-th root of unity.

The remaining axes are the other transform coordinates <cite data-source="paper">whose axis lengths are powers of two</cite>. Let $L$ be the length of such an axis, dividing $2r$. Its root $y^{2r/L}$ is a power of $y$. A power of $y$ below $y^r$ is a shift, and a power between $y^r$ and $y^{2r}$ is minus a shift, so every root multiplication on that axis is a signed shift. Powers of $y$ <cite data-source="paper">serve as roots of unity in the remaining axes</cite>.

A fast transform is built from butterflies, each multiplying one entry by a root and adding and subtracting it from another, plus address rearrangements. So a transform whose roots are powers of $y$ needs only signed shifts, address rearrangements, and additions and subtractions, with no general complex multiplication.
