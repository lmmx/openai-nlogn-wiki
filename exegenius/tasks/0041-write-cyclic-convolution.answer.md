Cyclic convolution is an operation on two vectors of the same length that combines them like polynomial multiplication, except that positions past the end wrap around to the start. It is the operation that the transform identities later in the argument turn into a pointwise product.

Let $u$ and $v$ be vectors of $q$ values, with coordinates indexed by $0, 1, \ldots, q-1$. We write $u \ast v$ for the cyclic convolution of $u$ and $v$. It is again a vector of $q$ values, whose $k$-th coordinate, for $k = 0, \ldots, q-1$, is

$$(u \ast v)_k = \sum_{j=0}^{q-1} u_j \, v_{(k-j) \bmod q}.$$

Here $(k-j) \bmod q$ is the remainder of $k-j$ after division by $q$, so an index that falls below $0$ or past $q-1$ is taken modulo $q$. Each pair of positions $j$ and $k-j$ contributes one product, and the products landing on the same output position $k$ are added.

Ordinary polynomial multiplication of two length-$q$ vectors would produce $2q-1$ values. Cyclic convolution folds the extra values back onto the start: the products that would fall at positions $q, \ldots, 2q-2$ are added to positions $0, \ldots, q-2$.

For a small example take $q = 3$, $u = (1, 2, 0)$ and $v = (0, 1, 1)$. The ordinary product has coefficients $(0, 1, 3, 2, 0)$. The entry at position $3$ wraps onto position $0$, and the entry at position $4$ wraps onto position $1$, giving

$$u \ast v = (0+2,\; 1+0,\; 3) = (2, 1, 3).$$

Direct evaluation of the sum for $k=0$ gives the same value, $u_1 v_2 = 2$, as the only nonzero product.
