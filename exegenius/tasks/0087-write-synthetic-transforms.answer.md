A synthetic polynomial transform is based on the [Discrete Fourier transform](discrete-fourier-transform.md): it has the same form, but its roots of unity are powers of a ring variable, so that multiplying by a root is a signed shift of coefficients.

Let $r$ be a power of two, the number of complex coefficients in a record. A record is a polynomial of degree less than $r$ with complex coefficients. Let $y$ be the variable of the ring $\mathbb{C}[y]/(y^r+1)$, in which $y^r$ is identified with $-1$.

Hence $y^{2r}=1$. The order of an element is the least positive power of it that equals 1. The order of $y$ is exactly $2r$: for $0<k<r$, $y^k$ is a monomial other than 1, and for $r\le k<2r$, $y^k=-y^{k-r}\ne 1$.

Take a transform length $q$, the number of values in one transform, that divides $2r$. Then $\omega = y^{2r/q}$ is a primitive $q$-th root of unity in this ring. Its order is $q$: $\omega^q = y^{2r} = 1$, and $\omega^m = y^{2rm/q}$ equals 1 only when $2r$ divides $2rm/q$, that is, when $q$ divides $m$.

Write $a=(a_0,\dots,a_{q-1})$ for the input vector of $q$ records; the letter $a$ changes meaning from the cyclic convolution page. The transform is
$$\hat a_j=\frac{1}{q}\sum_{k=0}^{q-1}\omega^{jk}a_k, \qquad 0\le j<q.$$
Here $\hat a_j$ is the transformed record at frequency index $j$. The opposite transform uses $\omega^{-jk}$ in place of $\omega^{jk}$.

For example, with $r=4$,
$$y\,(a_0+a_1y+a_2y^2+a_3y^3)=-a_3+a_0y+a_1y^2+a_2y^3,$$
because $y\cdot y^3=y^4=-1$. The coefficients move one place and the one that wraps around changes sign. The transform therefore reduces to address rearrangements, signed shifts and two-point butterflies. <cite data-source="paper">In this representation, the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations.</cite>

Entry $j$ of each transform sits at frequency $\omega^j$, so the frequency order is $j$. Both forward transforms use the same $\omega$, so the pointwise product keeps entry $j$ at frequency $\omega^j$.

Together, the two forward transforms, the pointwise product and the opposite transform compute a [cyclic convolution](cyclic-convolution.md) of records.
