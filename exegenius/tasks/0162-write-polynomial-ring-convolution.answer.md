Convolution over the polynomial ring is the [cyclic product](cyclic-convolution.md) of two arrays of records, and it is the step that convolves the axes left after the earlier reductions. Convolution over the polynomial ring takes its records from the [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md), in which $y^r = -1$.

Let $a$ and $b$ be arrays of $q$ records, where $q$ is the number of records in each array and is a power of two dividing $2r$. Let $c$ be their convolution,
$$c_k = \sum_{\substack{0 \le i,j < q \\ i+j \equiv k \pmod{q}}} a_i b_j,$$
so $c_k$ sums the products $a_i b_j$ over pairs whose indices add to $k$ modulo $q$. Computing $c$ directly takes $q^2$ record products. The method below replaces them by $q$ record products in the transform domain, which is the point of the method.

Let $\rho = y^{2r/q}$, the synthetic root of unity of order $q$, so that $\rho^q = 1$. The index $\ell$ runs from $0$ to $q-1$ and labels the frequency of an entry. Let $T$ be the forward transform, $T(a)_\ell = \sum_j a_j\rho^{j\ell}$, and let $S$ be the opposite transform, $S(X)_k = \frac{1}{q}\sum_\ell X_\ell\,\rho^{-k\ell}$, which uses the inverse root $\rho^{-1}$ and divides by $q$. The two forward transforms keep the same frequency order, so one index $\ell$ pairs $T(a)_\ell$ with $T(b)_\ell$. <cite data-source="paper">The two forward synthetic transforms retain the same frequency order</cite>.

$$c = S\big(T(a) \odot T(b)\big).$$

Here $\odot$ multiplies two arrays entrywise in the ring. Both inputs must be transformed, and the pointwise product needs only $q$ record products. The $k$-th entry of the right side expands to
$$\frac{1}{q}\sum_{\ell=0}^{q-1}\Big(\sum_i a_i\rho^{i\ell}\Big)\Big(\sum_j b_j\rho^{j\ell}\Big)\rho^{-k\ell} = \sum_{i,j} a_i b_j\,\frac{1}{q}\sum_{\ell=0}^{q-1}\rho^{p\ell},$$
where $p = i+j-k$ is the offset of a pair $(i,j)$ from $k$. The inner sum is $q$ when $q$ divides $p$, which is exactly the condition $i+j \equiv k \pmod{q}$. Otherwise $(\rho^p-1)\sum_\ell \rho^{p\ell} = \rho^{pq}-1 = 0$. Evaluating at the $r$ distinct roots of $y^r+1$ is an isomorphism onto $\mathbb{C}^r$, and since $q$ is a power of two, $\rho^p-1$ is nonzero at every such root when $q$ does not divide $p$. So $\rho^p-1$ is invertible, and the inner sum is $0$. Only pairs with $i+j \equiv k$ survive, each with weight $1$, so $c$ is exact.

Take $q=2$, so $\rho = y^r = -1$. Then $T(a) = (a_0+a_1,\ a_0-a_1)$, and $T(b)$ is the same with $b$. Their pointwise product is $\big((a_0+a_1)(b_0+b_1),\ (a_0-a_1)(b_0-b_1)\big)$. With $S(u,v) = \big(\tfrac{u+v}{2}, \tfrac{u-v}{2}\big)$, where $u$ and $v$ are the two entries of the argument pair, this gives $c_0 = a_0b_0 + a_1b_1$ and $c_1 = a_0b_1 + a_1b_0$, the cyclic product for $q=2$.

Multiplying by a power of $y$ is a signed shift of coefficients. Convolution over the polynomial ring computes its transforms with [Synthetic polynomial transforms](synthetic-transforms.md), so the transforms need only signed shifts and additions.

The pointwise products are polynomial products. Convolution over the polynomial ring computes its products with [Signed coefficient packing](signed-packing.md), which turns each record product into one integer product, computed by the [established $O(n\log n)$ multiplier](established-multiplier.md).
