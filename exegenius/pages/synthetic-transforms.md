A synthetic polynomial transform is based on the [Discrete Fourier transform](discrete-fourier-transform.md): it has the same form, but its roots of unity are powers of a ring variable, so that multiplying by a root is a signed shift of coefficients. It is the transform used in the convolution step of the multiplier, where it replaces ordinary complex roots of unity.

Let $r$ be a power of two, the number of complex coefficients in a record. A record is a polynomial of degree less than $r$ with complex coefficients. Let $y$ be the variable of the ring $\mathbb{C}[y]/(y^r+1)$, in which $y^r$ is identified with $-1$.

Hence $y^{2r}=1$, and $y^{m}\ne 1$ for $0<m<2r$: for $0<m<r$, $y^m$ is a monomial other than 1, and for $r\le m<2r$, $y^m=-y^{m-r}\ne 1$. Take a transform length $q$, the number of values in one transform, that divides $2r$. Then $\omega = y^{2r/q}$ is a primitive $q$-th root of unity in this ring: $\omega^q=y^{2r}=1$, and $\omega^m=1$ only when $q$ divides $m$.

Write $p=(p_0,\dots,p_{q-1})$ for the input vector of $q$ records. The transform is
$$\hat p_k=\frac{1}{q}\sum_{j=0}^{q-1}\omega^{jk}p_j, \qquad 0\le k<q,$$
where $\hat p_k$ is the transformed record at frequency index $k$. The opposite transform uses $\omega^{-jk}$ in place of $\omega^{jk}$.

For example, with $r=4$,
$$y\,(p_0+p_1y+p_2y^2+p_3y^3)=-p_3+p_0y+p_1y^2+p_2y^3,$$
because $y\cdot y^3=y^4=-1$. The coefficients move one place and the one that wraps around changes sign. Multiplying by a root is therefore a signed shift, not a complex multiplication, so the transform reduces to address rearrangements, signed shifts and two-point butterflies. <cite data-source="paper">In this representation, the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations.</cite>

Entry $k$ of each transform sits at frequency $\omega^k$, so the frequency order is $k$. Both forward transforms use the same $\omega$, so the pointwise product keeps entry $k$ at frequency $\omega^k$.

Together, the two forward transforms, the pointwise product and the opposite transform compute a [cyclic convolution](cyclic-convolution.md) of records.
