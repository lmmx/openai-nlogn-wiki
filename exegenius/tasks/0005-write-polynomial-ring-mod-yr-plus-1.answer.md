Fix a power of two $r$. The ring $R_r = \mathbb{C}[y]/(y^r + 1)$ consists of the polynomials in $y$ with complex coefficients, where any power $y^r$ is replaced by $-1$. Every element can be written uniquely as $c_0 + c_1 y + \dots + c_{r-1} y^{r-1}$, so it is stored as a list of $r$ complex coefficients.

Multiplication works as ordinary polynomial multiplication followed by reduction. Since $y^r = -1$, the reduction rule is $y^{r+k} = -y^k$ for $0 \le k < r$. This is called a negacyclic wrap: a term that overflows past degree $r-1$ comes back with a minus sign.

For example, with $r = 4$, the reduction rules are $y^4 = -1$, $y^5 = -y$, and $y^6 = -y^2$. Then $y^3 \cdot y^2 = y^5 = -y$, so the wrapped term changes sign.

Since $y^r = -1$, we have $y^{2r} = 1$. So $y$ is a $2r$-th root of unity in this ring, and its powers $1, y, \dots, y^{2r-1}$ serve as roots of unity for transforms. Multiplying a coefficient list by $y$ is a cyclic shift in which the coefficient that moves past position $r-1$ is negated. With $r = 4$, $y \cdot (a_0, a_1, a_2, a_3) = (-a_3, a_0, a_1, a_2)$.

This is the structure that the [synthetic polynomial transform](synthetic-transform.md) and the [signed packing](signed-packing.md) use. The ring is a polynomial ring with the sign rule built in, so no further reduction step is needed on each product.
