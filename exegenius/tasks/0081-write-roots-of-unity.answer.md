A root of unity is a number some positive integer power of which equals one. A *primitive* root of unity is one whose powers are all distinct until the first one equals one.

Here $r$ is the number of complex coefficients of a reduced polynomial, a power of two. Here $y$ is the formal variable of the [polynomial ring modulo $y^r+1$](polynomial-ring.md), changing meaning from the neighbouring vertex of earlier pages. The roots below are powers of $y$.

Division with remainder by $y^r+1$ gives every polynomial a unique remainder of degree less than $r$, so $1, y, \dots, y^{r-1}$ span the ring. They are independent: a nonzero combination of them has degree less than $r$, so it is not a multiple of $y^r+1$. Hence they form a basis, and each element has exactly one expansion in them.

In this ring $y^r = -1$, so $y^{2r} = (y^r)^2 = 1$. Here $p$ is an exponent with $0 < p < r$. No smaller positive power equals one: $y^p$ is a basis monomial other than $1 = y^0$, $y^r = -1 \ne 1$, and $y^{r+p} = -y^p$ is a nonzero multiple of such a monomial. So $y$ has order $2r$ and is a primitive root of unity.

Multiplying by $y^p$ moves each coefficient up $p$ places, and a coefficient that passes position $r-1$ re-enters with a minus sign, because $y^r = -1$. So multiplication by $y^p$ is a signed shift of the coefficient list. <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>

A [discrete Fourier transform](fourier-transform.md) multiplies by a root of unity at each [twiddle step](fourier-transform.md), a general complex product. With powers of $y$ as roots, each such product is a signed shift.
