A synthetic polynomial transform is a Fourier-type transform whose roots of unity are powers of a single variable in a polynomial ring, so that multiplying by a root is a signed shift of coefficients. It is the transform used in the reduction below, in place of the ordinary Fourier transforms.

A synthetic polynomial transform is based on the [Discrete Fourier transform](discrete-fourier-transform.md): it has the same form, but its roots of unity are powers of a ring variable.

Let $r$ be a power of two, the number of complex coefficients in a record. Let $y$ be the variable of the ring $\mathbb{C}[y]/(y^r+1)$, in which $y^r$ is identified with $-1$. Hence $y^{2r}=1$, so $y$ has order $2r$.

Take a transform length $q$, the number of values in one transform, that divides $2r$. Then $\omega = y^{2r/q}$ is a primitive $q$-th root of unity in this ring, since $\omega^q = y^{2r} = 1$.

The transform of a vector $(a_0,\dots,a_{q-1})$ of records is
$$\hat a_j=\frac{1}{q}\sum_{k=0}^{q-1}\omega^{jk}a_k, \qquad 0\le j<q.$$
The opposite transform uses $\omega^{-jk}$ in place of $\omega^{jk}$.

Multiplying a record by a power of $\omega$ needs no multiplication of coefficients. For example, with $r=4$,
$$y\,(a_0+a_1y+a_2y^2+a_3y^3)=-a_3+a_0y+a_1y^2+a_2y^3,$$
because $y\cdot y^3=y^4=-1$. The coefficients move one place and the one that wraps around changes sign. Every power $y^k$ with $0\le k<r$ is the same kind of signed shift by $k$ places. The transform therefore reduces to address rearrangements, signed shifts and two-point butterflies. <cite data-source="paper">In this representation, the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations.</cite>

Both forward transforms in a convolution use the same $\omega$ and the same frequency order, so their pointwise product keeps that order.
