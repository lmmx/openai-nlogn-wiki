The discrete Fourier transform is the linear map that turns a vector into its Fourier coefficients. The argument needs it because multiplying two polynomials is a cyclic convolution, and the transform turns cyclic convolution into entrywise products.

Let $u = (u_0, u_1, \dots, u_{q-1})$ be a vector of complex numbers, and let $q$ be its length, the number of entries of $u$ and of its transform. The index $j$ runs over the entries of $u$ and the index $k$ runs over the entries of its transform, both from $0$ to $q-1$. The number $\omega = \exp(-2\pi i/q)$ is the [primitive $q$-th root of unity](roots-of-unity.md), so $\omega^q = 1$.

The transform of $u$ is the vector $\hat u$ whose $k$-th entry is

$$\hat u_k = \frac{1}{q}\sum_{j=0}^{q-1} u_j\,\omega^{jk}, \qquad k = 0, 1, \dots, q-1.$$

Since $\omega^{jk} = \exp(-2\pi i jk/q)$, this is the map sending $u$ to the vector whose $k$-th entry is $\frac{1}{q}\sum_j u_j \exp(-2\pi i jk/q)$.

For $q = 2$, $\omega = \exp(-\pi i) = -1$, so $\hat u_0 = (u_0 + u_1)/2$ and $\hat u_1 = (u_0 - u_1)/2$.

Computed directly, the transform takes about $q^2$ multiplications, because each of the $q$ entries is a sum of $q$ products. For power-of-two lengths, fast algorithms compute it in $O(q \log q)$ operations. The argument needs fast transforms for lengths $q$ that are prime, and the [Gaussian resampling](gaussian-resampling.md) reduction handles this by rewriting such a transform through transforms whose axis lengths are powers of two.
