Bluestein's chirp identity rewrites a [Discrete Fourier transform](discrete-fourier-transform.md) so that the transform can be computed with convolution, which the multiplication reduction needs. It computes its transforms by a [Cyclic convolution](cyclic-convolution.md) multiplied by chirp factors.

Let $q$ be the length of the transform, and let $\omega = e^{2\pi i/q}$ be the primitive $q$-th root of unity it uses. Let $w = e^{\pi i/q}$ be the number whose square is $\omega$, so that $w^2 = \omega$. The indices $j$ and $k$ run over $\{0,\ldots,q-1\}$, and $q$ is even.

The identity is
$$\omega^{jk} = w^{j^2}\, w^{k^2}\, w^{-(k-j)^2}.$$

The factors $w^{j^2}$, $w^{k^2}$ and $w^{-(k-j)^2}$ are called chirps: their phases are quadratic in the index. The identity holds because $j^2 + k^2 - (k-j)^2 = 2jk$, so the right side is $w^{2jk} = \omega^{jk}$. Substituting into the normalized transform $X_k = \frac{1}{q}\sum_j x_j\,\omega^{jk}$ gives
$$X_k = \frac{w^{k^2}}{q}\sum_{j} a_j\, w^{-(k-j)^2}, \qquad a_j = x_j\, w^{j^2}.$$

The sum is a cyclic convolution. For any integer $p$, $w^{-(p+q)^2} = w^{-p^2}$, because $w^{-2pq} = \omega^{-pq} = 1$ and $w^{-q^2} = (-1)^q = 1$. So the chirp depends only on $(k-j) \bmod q$. Define $b_\ell = w^{-\ell^2}$ for $\ell \in \{0,\ldots,q-1\}$, where $\ell$ is the reduced index $(k-j) \bmod q$, an integer from 0 to $q-1$. Then the sum is $\sum_j a_j b_\ell$ over the pairs with $j+\ell \equiv k \pmod q$, which is the $k$-th entry of the cyclic convolution $a \ast b$, so
$$X_k = \frac{w^{k^2}}{q}\,(a \ast b)_k.$$

For example, take $q=2$, $\omega=-1$ and $w=i$. For $j=k=1$, $w^{j^2}w^{k^2}w^{-(k-j)^2} = i\cdot i\cdot 1 = -1 = \omega^{1}$, as the identity requires.

The paper applies this identity to the middle transform of its reduction. <cite data-source="paper">converts the middle transform, including its target permutation, into normalized cyclic convolution</cite> The target permutation stays inside the transform identity, so it is not executed as a separate sort.
