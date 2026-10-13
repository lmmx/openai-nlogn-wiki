Fixed-point precision and exact recovery is the step that turns approximate transform output into exact integers, and then into the digits of the product. It recovers the integer coefficients produced by the [Reduction of integer product to digit convolution](radix-digit-reduction.md).

Each complex coefficient is stored as a pair of integer numerators over $2^p$, where $p$ is the working precision in bits; a numerator $H$ represents $H/2^p$. Scalings by known factors are exact on numerators, so the only inexact steps are the transforms and truncations. The source takes $p=6b$.

Let $T$ be a power of two with $4n/b\le T<8n/b$, and let $S$ be the cyclic convolution length, with $T/2<S<T$. With $q=\lceil n/b\rceil$ digits per input, the product has degree $2q-2<T/2<S$, so cyclic convolution has no wraparound. Each coefficient $c_j$, for $0\le j<S$, sums at most $q$ products of digits below $2^b$, so $0\le c_j\le q(2^b-1)^2<2^{3b}$, since $q\le n\le 2^b$.

Let $u$ and $v$ be the digit lists of the two inputs, each entry divided by $2^{b+2}$, so every entry has magnitude below $1/4$. Let $\mathcal F$ be the forward transform of length $S$ and $\mathcal F^{+}$ its opposite. The source's chirp and permutation cancellation lemma gives $\mathcal F^{+}(\mathcal Fu\cdot\mathcal Fv)=(u*v)/S^2$, where $\cdot$ is entrywise product and $*$ is cyclic convolution. Multiplying by $S$ and then by $2^{2b+4}S$ gives $2^{2b+4}(u*v)$, whose entries are the $c_j$.

Let $L=\log_2 T$, and let $\gamma$ be the exponent of the source scale $2^{\gamma}$, with $\gamma\le b/4$ for large $b$. Each transform, product and truncation adds error below a constant times $2^{-p}$ per entry. Tracking these through the transforms and the pointwise product, the computed array after multiplication by $S$ lies within $28\cdot2^\gamma T^2L\cdot2^{-p}$ of $(u*v)/S$. The final scaling by $2^{2b+4}S$ gives a coefficient error below $2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}$, using $S<T<2^b$, $L<b$ and $\gamma\le b/4$. For large $b$ this bound is below $\tfrac12$ <cite data-source="paper">448b\,2^{-3b/4}<\frac12</cite>. So rounding each recovered value to the nearest integer returns $c_j$ exactly.

Carry propagation then gives the digits. Let $h_0=0$ and, for $0\le j<S$,
$$d_j=(c_j+h_j)\bmod 2^b,\qquad h_{j+1}=\left\lfloor\frac{c_j+h_j}{2^b}\right\rfloor.$$
Since $c_j+h_j=d_j+2^bh_{j+1}$, induction gives $\sum_{i<j}c_i2^{bi}=\sum_{i<j}d_i2^{bi}+h_j2^{bj}$. The final carry $h_S$ is zero: $2n<bS$, so $xy=\sum_{i<S}c_i2^{bi}<2^{2n}\le2^{bS}$, while the digit sum $\sum_{i<S}d_i2^{bi}$ is also below $2^{bS}$. Hence $d_0,\dots,d_{S-1}$ are the full radix-$2^b$ digits of the product.

Example, radix $10$ for $2^b$ and $c=(12,15,3)$:  $d_0=2$, $h_1=1$; $d_1=6$, $h_2=1$; $d_2=4$, $h_3=0$. The digits $4,6,2$ give $462=12+15\cdot10+3\cdot100$.
