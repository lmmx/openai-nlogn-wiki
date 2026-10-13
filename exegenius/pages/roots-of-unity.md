A root of unity is a number some positive integer power of which equals one. Here $r$ is the number of complex coefficients of a reduced polynomial, a power of two. Here $y$ is the formal variable of the [polynomial ring modulo $y^r+1$](polynomial-ring.md), changing meaning from the neighbouring vertex of earlier pages.

A root of unity is characterised by the [order of an element](order-of-element.md) it has, the least positive power that equals one. A *primitive* root of unity is one whose powers are all distinct until the first one equals one.

A reduced polynomial is one of degree less than $r$, the remainder on division by $y^r+1$. Every polynomial has one such remainder, so $1, y, \dots, y^{r-1}$ span the ring. They are independent, because a nonzero combination of them has degree less than $r$ and so is not a multiple of $y^r+1$.

In this ring $y^r=-1$, so $y^{2r}=1$. For $0<k<2r$, $y^k$ is plus or minus a basis element, so by uniqueness of expansion it is not $1=y^0$. Hence $y$ has order $2r$ and is a primitive root of unity.

For a power of two $q$ dividing $2r$, let $\zeta$ denote $y^{2r/q}$. Then $\zeta^q=1$, and $\zeta^k=y^{2rk/q}$ is not $1$ for $0<k<q$, because $0<2rk/q<2r$. So $\zeta$ is a primitive $q$-th root of unity, and $\zeta^{q/2}=y^r=-1$.

Here $p$ is an exponent with $0\le p<r$, the letter $p$ changing meaning from the fractional bit count. Every power of $y$ is $\pm y^p$ for a unique $p$. Multiplying by $y^p$ moves each coefficient up $p$ places, and a coefficient passing position $r-1$ re-enters negated. So each such multiplication is a signed shift of the coefficient list. <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>

A root of unity supplies the twiddle factors of a [discrete Fourier transform](fourier-transform.md) of length $q$. Its fast form splits the input into even and odd entries; that split, for $q\ge 2$, uses only $\zeta^q=1$ and $\zeta^{q/2}=-1$, so every twiddle product in this ring is a signed shift.
