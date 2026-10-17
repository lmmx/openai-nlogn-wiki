The negacyclic ring is a way of storing a list of complex numbers so that multiplying by a root of unity costs only a signed rotation of the list, with no arithmetic; this is what lets the later transforms avoid complex multiplications.

Write $\mathcal R_r=\mathbb C[y]/(y^r+1)$ for it, where $y$ is the ring variable, the indeterminate of the polynomials, and $r$ is the record length, the number of complex coefficients in a polynomial of the ring, always a power of two with $r\geq 2$. An element is
$$z=\sum_{k=0}^{r-1}z_k y^k,\qquad z_k\in\mathbb C,$$
so it is just a record of $r$ complex numbers. Addition is coefficientwise. Multiplication is ordinary polynomial multiplication followed by the rule $y^r=-1$, that is, $y^{r+j}=-y^j$: any term of degree $r$ or more wraps around to the front with its sign flipped. This is arithmetic modulo $y^r+1$, and for that reason the ring is also called the negacyclic ring. We always keep the representative of degree below $r$.

## Powers of $y$ are signed shifts

Multiplying by $y$ moves each coefficient up one place and sends the top coefficient $z_{r-1}$ to the bottom as $-z_{r-1}$. For $r=4$:
$$y\,(z_0+z_1y+z_2y^2+z_3y^3)=-z_3+z_0y+z_1y^2+z_2y^3 .$$
Since $y^r=-1$, we get $y^{2r}=1$, so $y$ is a $2r$-th root of unity and $y^a$ depends only on $a$ modulo $2r$. Multiplying by $y^a$ for any integer $a$ rotates the coefficient list by $a$ places and negates the coefficients that wrap past the end, and also negates everything if $a \bmod 2r\geq r$. It permutes the coefficients and changes some signs, so it is a linear-time pass over the list.

The size of an element is measured by the largest coefficient modulus,
$$\|z\|_\infty=\max_{0\leq k<r}|z_k|.$$
A signed permutation of coefficients leaves this maximum unchanged, so multiplication by $y^a$ is an isometry for this norm <cite data-source="paper">some signs; consequently it is an isometry for this norm.</cite> Shifts therefore add no rounding error when coefficients are stored at fixed precision.

## Why this ring

Taking one coordinate of a multidimensional array to be a record in $\mathcal R_r$ makes powers of $y$ available as roots of unity in the remaining axes, where a multiplication by such a root is a signed shift of the coefficient list <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>. Transforms built this way are described on [Synthetic polynomial transform](synthetic-transform.md). The ring also receives ordinary cyclic data once its coefficients are twisted by phases, as explained on [Phase twist](phase-twist.md).
