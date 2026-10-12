Gaussian resampling is an identity that rewrites a Fourier transform of prime length as a transform over several power-of-two axes. An axis is one index dimension of an array; a transform over several axes applies a one-dimensional transform along each axis in turn.

The integer product needs transform lengths that are pairwise coprime <cite data-source="paper">The transform lengths needed for the integer product are pairwise coprime</cite>, while synthetic transforms need powers of two. Gaussian resampling operates on the prime axes produced by the [Chinese-remainder address map](chinese-remainder-address-map.md).

Let $q$ be a prime, the number of entries of the sequence $z=(z_0,\dots,z_{q-1})$. Gaussian resampling rewrites the normalized [discrete Fourier transform](fourier-transform.md) $F_q$ of length $q$ as a transform over power-of-two axes, where $(F_q z)_k=\frac1q\sum_{j=0}^{q-1}z_j e^{-2\pi i jk/q}$ for $0\le k<q$.

Let $s$ and $t$ be integers, the lengths of the source and target transforms, with $\gcd(s,t)=1$, $t$ a power of two, and $t/s$ close to one. Let $F_s$ and $F_t$ be the normalized transforms of these lengths, let $P_s$ and $P_t$ be the source and target permutations of output indices, and let $c$ be a fixed power of two. Then there are linear contractions $L_1:\mathbb C^s\to\mathbb C^t$ and $L_2:\mathbb C^t\to\mathbb C^s$, maps that do not increase the maximum modulus of a vector, such that
$$P_sF_s=c\,L_2\,P_tF_t\,L_1.$$
The permutations stay inside the identity <cite data-source="paper">source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts</cite>.

Tensor products give the same identity for multidimensional transforms.

Power-of-two axes are cheap because of the [polynomial ring modulo $y^r+1$](polynomial-ring-y.md), where $r$ is a power of two. Since $y^r=-1$, $y^{j+r}=-y^j$, so multiplying a coefficient list by $y^j$ shifts it $j$ places, with wrapped coefficients changing sign. For $r=4$, let $w=(w_0,w_1,w_2,w_3)$ be the coefficients of $w_0+w_1y+w_2y^2+w_3y^3$; then $y$ times $w$ is $(-w_3,w_0,w_1,w_2)$. Since $y^{2r}=1$, the powers $y^0,\dots,y^{2r-1}$ are roots of unity, and a transform using them needs only signed shifts and additions.
