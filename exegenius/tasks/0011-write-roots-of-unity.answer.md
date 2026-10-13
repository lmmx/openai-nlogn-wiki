A root of unity is a number some positive integer power of which equals one; for example $-1$ is a root of unity because $(-1)^2 = 1$. The *order* of a root of unity is the smallest positive power of it that equals one. This is the sense of "primitive root of unity" used below.

Here a root of unity is taken in the [polynomial ring modulo $y^r+1$](polynomial-ring.md), where it is a power of $y$. In $\mathbb C[y]/(y^r+1)$ the element $y$ satisfies $y^r = -1$, so $y^{2r} = (y^r)^2 = 1$. No smaller positive power equals one: the powers $y^0, \dots, y^{r-1}$ are distinct basis monomials, $y^r = -1 \ne 1$, and $y^{r+j} = -y^j$ for $0 < j < r$. So $y$ has order $2r$. For $r = 4$, $y$ has order $8$, and $y^2$ has order $4$, since $(y^2)^2 = y^4 = -1 \ne 1$ and $(y^2)^4 = y^8 = 1$.

Multiplying by $y^j$ moves each coefficient up $j$ places. A coefficient that passes position $r-1$ re-enters with a minus sign, because $y^r = -1$. Multiplication by $y^j$ is therefore a signed shift of the coefficient list <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>.

This is why these roots are useful here. A discrete Fourier transform multiplies by a root of unity at each twiddle step, which is a general complex product. With powers of $y$ as roots, each such product is only a shift, so the transform's inner multiplications become cheap.
