Convolution over the polynomial ring is the cyclic product of two arrays of records, in the sense of [Cyclic convolution](cyclic-convolution.md). It is the step that convolves the axes left after the earlier reductions. Convolution over the polynomial ring takes its records from the [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md), in which $y^r = -1$.

Let $a$ and $b$ be arrays of $q$ records, where $q$, the number of records in each array, is a power of two dividing $2r$. Their convolution is
$$c_k = \sum_{\substack{0 \le i,j < q \\ i+j \equiv k \pmod{q}}} a_i b_j,$$
so $c_k$ sums the products $a_i b_j$ over pairs whose indices add to $k$ modulo $q$. Computed directly, this takes $q^2$ record products.

Let $\rho = y^{2r/q}$, a synthetic root of unity: since $y$ has order $2r$, $\rho^q = 1$. The index $\lambda$ runs from $0$ to $q-1$ and labels the frequency of an entry. Let $\Phi$ be the forward transform, $\Phi(a)_\lambda = \sum_j a_j\rho^{j\lambda}$, and let $\Psi$ be the opposite transform, which takes an array $Y$ of $q$ records to $\Psi(Y)_k = \frac{1}{q}\sum_\lambda Y_\lambda\rho^{-k\lambda}$, dividing by $q$ and using the inverse root $\rho^{-1}$. Both forward transforms keep the same frequency order, so one index $\lambda$ pairs $\Phi(a)_\lambda$ with $\Phi(b)_\lambda$ <cite data-source="paper">The two forward synthetic transforms retain the same frequency order</cite>.

The method is
$$c = \Psi\big(\Phi(a) \odot \Phi(b)\big).$$
Here $\odot$ multiplies two arrays entrywise in the ring, the pointwise product. This is the convolution theorem for these transforms: transforming turns the cyclic sum into a pointwise product, and the opposite transform brings the result back. The pointwise product needs only $q$ record products, not $q^2$.

Expanding the $k$-th entry shows that this is exact:
$$\Psi\big(\Phi(a)\odot\Phi(b)\big)_k = \sum_{i,j} a_i b_j\,\frac{1}{q}\sum_{\lambda=0}^{q-1}\rho^{\delta\lambda},$$
where $\delta = i+j-k$ is the offset of the pair $(i,j)$ from $k$. If $q$ divides $\delta$, every term of the inner sum is $1$, so the sum is $q$. Otherwise $(\rho^{\delta}-1)\sum_\lambda \rho^{\delta\lambda} = \rho^{\delta q}-1 = 0$. The factor $\rho^{\delta}-1$ is invertible: the ring is isomorphic to $\mathbb{C}^r$ by evaluation at the $r$ distinct roots of $y^r+1$, each of order $2r$, and at each such root $\rho^{\delta}$ equals $1$ only if $q$ divides $\delta$. So the inner sum is $0$. Only pairs with $i+j \equiv k \pmod{q}$ survive, each with weight $1$, which gives $c_k$.

Take $q=2$, so $\rho = y^r = -1$. Then $\Phi(a) = (a_0+a_1,\ a_0-a_1)$, and $\Phi(b)$ is the same with $b$. Their pointwise product $Y$ has entries $Y_0 = (a_0+a_1)(b_0+b_1)$ and $Y_1 = (a_0-a_1)(b_0-b_1)$, and $\Psi(Y)_0 = \frac{Y_0+Y_1}{2}$, $\Psi(Y)_1 = \frac{Y_0-Y_1}{2}$. These give $c_0 = a_0b_0 + a_1b_1$ and $c_1 = a_0b_1 + a_1b_0$, the cyclic product for $q=2$.

Convolution over the polynomial ring computes its transforms with [Synthetic polynomial transforms](synthetic-transforms.md), so the transforms need only signed shifts and additions, because multiplying by a power of $y$ is a signed shift of coefficients.

The pointwise products are polynomial products. Convolution over the polynomial ring computes its products with [Signed coefficient packing](signed-packing.md). Packing turns each record product into one integer product, which the [Established O(n log n) multiplier](established-multiplier.md) computes as an ordinary subroutine.
