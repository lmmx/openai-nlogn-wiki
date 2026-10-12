Convolution over the polynomial ring is the [cyclic product](cyclic-convolution.md) of two arrays of records, and it computes convolution on the remaining axes by transforms and one pointwise product. Convolution over the polynomial ring takes its records from the [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md).

Let $a = (a_0, \dots, a_{N-1})$ and $b = (b_0, \dots, b_{N-1})$ be arrays of $N$ records, where $N$ is the number of records in each array. Here $a$, $b$ and $c$ are arrays of records. The indices $i$, $j$ and $k$ run from $0$ to $N-1$. The convolution is the array $c$ with
$$c_k = \sum_{\substack{0 \le i,j < N \\ i + j \equiv k \pmod{N}}} a_i\, b_j,$$
so $c_k$ sums the products $a_i b_j$ over pairs whose indices add to $k$ modulo $N$. Computing $c$ directly takes $N^2$ record products.

Let $\omega = y^{2r/N}$, the synthetic root of unity of order $N$, so that $\omega^N = 1$. Let $F$ be the forward synthetic transform, $F(a)_m = \sum_j a_j\,\omega^{jm}$, and let $G$ be the opposite transform, $G(X)_k = \frac{1}{N}\sum_m X_m\,\omega^{-km}$, which uses the inverse root $\omega^{-1}$ and divides by $N$. Here $F$ and $G$ are transforms. The index $m$ labels the frequency of an entry. The two forward transforms keep the same frequency order <cite data-source="paper">through their pointwise product</cite>, so one index $m$ pairs $F(a)_m$ with $F(b)_m$.

$$c = G\big(F(a) \odot F(b)\big).$$

Here $\odot$ multiplies two arrays entrywise in the ring. Both inputs must be transformed, and the pointwise product needs only $N$ record products. The $k$-th entry of the right side is
$$\frac{1}{N}\sum_{m=0}^{N-1}\Big(\sum_i a_i\omega^{im}\Big)\Big(\sum_j b_j\omega^{jm}\Big)\omega^{-km} = \sum_{i,j} a_i b_j\cdot\frac{1}{N}\sum_{m=0}^{N-1}\omega^{(i+j-k)m}.$$
The inner sum is $N$ when $i+j \equiv k \pmod{N}$. Otherwise $t = i+j-k$ is not a multiple of $N$, so $\omega^t - 1$ is nonzero at every root of $y^r+1$ and invertible in the ring. Multiplying the inner sum by $\omega^t-1$ gives $\omega^{tN}-1 = 0$, so the sum is $0$. Only pairs with $i+j \equiv k$ survive, and the factor $1/N$ in $G$ is the normalization, so $c$ is exact.

Take $N = 2$, so $\omega = y^r = -1$. Then $F(a) = (a_0+a_1,\ a_0-a_1)$, and $F(b)$ is the same with $b$. Their pointwise product is $\big((a_0+a_1)(b_0+b_1),\ (a_0-a_1)(b_0-b_1)\big)$. With $G(u,v) = \big(\tfrac{u+v}{2}, \tfrac{u-v}{2}\big)$, where $u$ and $v$ are the two entries of the argument pair, this gives $c_0 = a_0 b_0 + a_1 b_1$ and $c_1 = a_0 b_1 + a_1 b_0$, the cyclic product for $N=2$.

Multiplying by a power of $y$ is a signed shift of coefficients. Convolution over the polynomial ring computes its transforms with [Synthetic polynomial transforms](synthetic-transforms.md), so the transforms need only signed shifts and additions.

The pointwise products are polynomial products. Convolution over the polynomial ring computes its products with [Signed coefficient packing](signed-packing.md), which turns each record product into one integer product, computed by the [established $O(n\log n)$ multiplier](established-multiplier.md).
