Convolution over the polynomial ring is the cyclic product of two arrays of records, and it is the step that computes convolution on the remaining axes by transforms and one pointwise product. Convolution over the polynomial ring takes its records from the [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md).

Let $a = (a_0, \dots, a_{N-1})$ and $b = (b_0, \dots, b_{N-1})$ be arrays of records, where $N$ is the number of records in each array. The convolution is the array $c$ with
$$c_k = \sum_{\substack{0 \le i,j < N \\ i + j \equiv k \pmod{N}}} a_i\, b_j$$
up to a known scalar normalization. Each product $a_i b_j$ is taken in the ring, where wrap-around in the exponent of $y$ flips a sign, while the index sum wraps modulo $N$. Computing $c$ directly takes $N^2$ record products.

Let $F$ be the forward synthetic transform and $G$ the opposite transform, both acting on arrays of $N$ records. Then
$$c = G\big(F(a) \odot F(b)\big),$$
where $\odot$ multiplies entrywise in the ring, and the normalization is applied at the end. Both inputs must be transformed, because the product needs $F(a)$ and $F(b)$ together. The pointwise product needs only $N$ record products.

A transform turns cyclic convolution into entrywise products only if entry $k$ of $F(a)$ and entry $k$ of $F(b)$ belong to the same frequency, and $G$ reads the product back in that order. Here the two forward transforms keep the same frequency order <cite data-source="paper">through their pointwise product</cite>, and $G$ reads that order back.

Take $N = 2$, with root of unity $-1 = y^r$. Then $F(a) = (a_0 + a_1,\ a_0 - a_1)$, and $F(b)$ is the same with $b$. The pointwise product is $\big((a_0+a_1)(b_0+b_1),\ (a_0-a_1)(b_0-b_1)\big)$. The opposite transform $G(u,v) = \big(\tfrac{u+v}{2}, \tfrac{u-v}{2}\big)$ gives $c_0 = a_0 b_0 + a_1 b_1$ and $c_1 = a_0 b_1 + a_1 b_0$, which is the cyclic product for $N = 2$.

Multiplying by a power of $y$ is a signed shift of coefficients, so the transforms are cheap. Convolution over the polynomial ring computes its transforms with [Synthetic polynomial transforms](synthetic-transforms.md), so the transforms need only signed shifts and additions.

The pointwise products are polynomial products. Convolution over the polynomial ring computes its products with [Signed coefficient packing](signed-packing.md), which turns each record product into one integer product. That integer product is computed by the [established $O(n\log n)$ multiplier](established-multiplier.md) as an ordinary subroutine.
