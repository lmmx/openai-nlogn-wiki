The ring of complex polynomials reduced modulo a fixed polynomial is the arithmetic in which this argument's transforms are computed. Here $y$ is the formal variable of the ring. Here $r$ is the number of complex coefficients in each polynomial record, which is a power of two. Products in $\mathbb C[y]/(y^r+1)$ are reduced modulo $y^r+1$. The ring has powers that act as [Root of unity](roots-of-unity.md), and their effect on coefficients is cheap.

The index $i$ runs from $0$ to $r-1$. An element $a_0+a_1y+\dots+a_{r-1}y^{r-1}$ is written as its coefficient list $(a_0,\dots,a_{r-1})$. The entry $a_i$ of this list is the coefficient of $y^i$, a complex number. The letter $a_i$ has a new meaning here, not the integer of the packing page.

Here $k$, with $0\le k<r$, is the number of places a coefficient is shifted. Reduction replaces $y^r$ with $-1$, so $y^{2r}=1$. Multiplying $a_i y^i$ by $y^k$ gives $a_i y^{i+k}$, which for $i+k\ge r$ becomes $-a_i y^{i+k-r}$. Thus multiplying by $y^k$ shifts each coefficient $k$ places towards higher index, and a coefficient pushed past position $r-1$ returns at position $i+k-r$ with its sign reversed.

For example, with $r=4$,
$$y\cdot(a_0+a_1y+a_2y^2+a_3y^3)=-a_3+a_0y+a_1y^2+a_2y^3,$$
since $y\cdot a_3y^3=a_3y^4=-a_3$.

The argument's transforms run over axes whose lengths are powers of two. After a further conversion to convolution, one coordinate of the array is stored as an element of this ring, that is, as a polynomial modulo $y^r+1$ <cite data-source="paper">is stored as the coefficient list of a polynomial modulo $y^r+1$</cite>. The other coordinates are the remaining axes. Since $y^{2r}=1$, every power of $y$ is a root of unity, so powers of $y$ serve as roots of unity on the remaining axes. A twiddle multiplication, which multiplies an entry of a transform by a root of unity, is therefore a signed shift of the coefficient list, with no complex multiplication needed.
