The phase twist converts a cyclic convolution in one coordinate into a convolution in the [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md). It is used after the [Bluestein chirp identity](bluestein-chirp-identity.md), which leaves a cyclic convolution in its last coordinate.

Let $r$ be a power of two and put $\zeta = e^{\pi i / r}$. Define the map $\Theta$ that sends the cyclic variable $x_d$, with $x_d^r = 1$, to $\zeta y$:

$$x_d \mapsto \zeta y.$$

This is well defined, because $(\zeta y)^r = \zeta^r y^r = (-1)(-1) = 1$. On the bases $(x_d^k)$ and $(y^k)$ for $0 \le k < r$, it multiplies the $k$-th coefficient by $\zeta^k$. It is therefore an isomorphism, and its inverse multiplies coefficient $k$ by $\zeta^{-k}$.

The reason this helps is the wraparound check. Suppose a product term has exponents $k + l$, and write $k + l = j + hr$ with $h \in \{0, 1\}$. In the cyclic ring $x_d^r = 1$, so this term lands at position $j$ with no sign. In the twisted ring, the term has factor $\zeta^{k+l}(-1)^h$ after the negacyclic reduction $y^r = -1$. Using $\zeta^r = -1$, this equals $\zeta^{j}(\zeta^r)^h(-1)^h = \zeta^{j}$.

So multiplying by $\zeta^{-k}$ after the product untwists the coefficients, and recovers the cyclic result with the correct sign. The paper states this as: untwisting recovers the cyclic coefficient with the correct sign. The map preserves the sup norm of coefficients.
