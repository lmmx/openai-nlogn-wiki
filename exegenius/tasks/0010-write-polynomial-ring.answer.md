This concept is a ring of complex polynomials in one formal variable, with products reduced modulo a fixed polynomial, and it is the arithmetic in which this argument's transforms are computed. Its powers act as roots of unity, and their effect on coefficients is cheap.

Here $y$ is the formal variable whose powers act as roots of unity on the remaining axes. Here $r$ is the number of complex coefficients in each polynomial record, which is a power of two.

The ring $\mathbb C[y]/(y^r+1)$ consists of the complex polynomials of degree less than $r$, where a product is formed as an ordinary polynomial product and then reduced by replacing $y^r$ with $-1$. One coordinate is stored as an element of this ring, with $r$ a power of two. <cite data-source="paper">is stored as the coefficient list of a polynomial modulo $y^r+1$</cite>

An element $a_0+a_1y+\dots+a_{r-1}y^{r-1}$ is written as its coefficient list $(a_0,\dots,a_{r-1})$. The entry $a_i$ of this list is the coefficient of $y^i$.

Reduction uses $y^r=-1$, so $y^{2r}=1$, and a term $a_i y^j$ with $i+j\ge r$ becomes $-a_i y^{i+j-r}$. Hence multiplying by $y^k$, for $0\le k<r$, shifts each coefficient $k$ places towards higher index, and a coefficient pushed past position $r-1$ returns at position $i+k-r$ with its sign reversed.

For example, with $r=4$,
$$y\cdot(a_0+a_1y+a_2y^2+a_3y^3)=-a_3+a_0y+a_1y^2+a_2y^3,$$
since $y\cdot a_3y^3=a_3y^4=-a_3$.

The transforms of this argument use roots of unity. A synthetic transform is a discrete Fourier transform whose roots of unity are powers of $y$, so each twiddle multiplication is a signed shift of the $r$ coefficients rather than a complex multiplication.
