Gaussian resampling is an identity that rewrites a Fourier transform of prime length as a transform over several power-of-two axes. An axis is one index dimension of an array; a transform over several axes applies a one-dimensional transform along each axis in turn.

The integer product needs transform lengths that are pairwise coprime <cite data-source="paper">The transform lengths needed for the integer product are pairwise coprime</cite>, while synthetic transforms need powers of two. Gaussian resampling operates on the axes produced by the [Chinese-remainder address map](chinese-remainder-address-map.md).

Let $q$ be a prime, the length of a sequence $z=(z_0,\dots,z_{q-1})$ of complex numbers. Gaussian resampling rewrites the normalized [discrete Fourier transform](fourier-transform.md) $F_q$ of length $q$ as a transform over power-of-two axes. Its values are
$$(F_q z)_k=\frac1q\sum_{j=0}^{q-1}z_j e^{-2\pi i jk/q}, \qquad 0\le k<q.$$

Let $s<t$ be integers, the lengths of the source and target transforms, with $\gcd(s,t)=1$ and $t$ a power of two; these letters change meaning here. Let $F_s$ and $F_t$ be their normalized transforms, and let $P_s$ and $P_t$ be the source and target coordinate permutations, which reorder the outputs of $F_s$ and $F_t$. Let $c$ be a power of two, the same for all $s$ and $t$ <cite data-source="paper">The constant is uniform</cite>. Here $L_1:\mathbb C^s\to\mathbb C^t$ and $L_2:\mathbb C^t\to\mathbb C^s$ are linear contractions, maps that do not increase the size of a vector. Such contractions exist <cite data-source="paper">There are linear contractions</cite>, and the identity is
$$P_sF_s=c\,L_2\,P_tF_t\,L_1.$$

The identity keeps $P_s$ and $P_t$ as factors, so the reordering they describe is not run as a separate full sort. The approximate maps for $L_1$ and $L_2$ take and return entries in increasing coordinate order <cite data-source="paper">occur in increasing coordinate order</cite>.

Gaussian resampling is carried over by [Tensor product](tensor-product.md) to several axes: tensor products give the same identity for multidimensional transforms.

Power-of-two axes are cheap because of the [polynomial ring modulo $y^r+1$](polynomial-ring-y.md), where $r$ is a power of two. Since $y^r=-1$, $y^{j+r}=-y^j$, so multiplying a coefficient list by $y^j$ shifts it $j$ places, with wrapped coefficients changing sign. For $r=4$, the list $(w_0,w_1,w_2,w_3)$ multiplied by $y$ becomes $(-w_3,w_0,w_1,w_2)$. Since $y^{2r}=1$, the powers of $y$ are roots of unity of order $2r$, and multiplying by them is a signed shift.
