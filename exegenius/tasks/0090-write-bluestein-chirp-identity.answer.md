Bluestein's chirp identity rewrites a [Discrete Fourier transform](discrete-fourier-transform.md) so that it can be computed with convolution. It computes its transforms by a [Cyclic convolution](cyclic-convolution.md) multiplied by chirp factors.

Let $q$ be the length of the transform, and let $\omega = e^{2\pi i/q}$ be the primitive $q$-th root of unity it uses. Let $w = e^{\pi i/q}$ be the number whose square is $\omega$, so that $w^2 = \omega$. The indices $j$ and $k$ run over $\{0,\ldots,q-1\}$.

The identity is
$$\omega^{jk} = w^{j^2}\, w^{k^2}\, w^{-(k-j)^2}.$$

It holds because $j^2 + k^2 - (k-j)^2 = 2jk$, so the right side is $w^{2jk} = \omega^{jk}$. Substituting into the normalized transform $X_k = \frac{1}{q}\sum_j x_j\,\omega^{jk}$ gives
$$X_k = \frac{w^{k^2}}{q}\sum_{j} a_j\, w^{-(k-j)^2}, \qquad a_j = x_j\, w^{j^2}.$$

The sum is a cyclic convolution. Take $q$ even. For any integer $s$, $w^{-(s+q)^2} = w^{-s^2}\, w^{-2sq}\, w^{-q^2} = w^{-s^2}$, since $w^{-2sq} = \omega^{-sq} = 1$ and $w^{-q^2} = (-1)^q = 1$. So the chirp depends only on $(k-j) \bmod q$. Define $b_t = w^{-t^2}$ for $t \in \{0,\ldots,q-1\}$, where $t$ is the reduced index $(k-j) \bmod q$. The sum becomes $\sum_j a_j b_t$ over pairs with $j + t \equiv k \pmod q$, which is the $k$-th entry of the cyclic convolution $a \ast b$. So $X_k = \frac{w^{k^2}}{q}\,(a \ast b)_k$.

For example, take $q=2$, $\omega=-1$ and $w=i$. For $j=k=1$ the right side is $i\cdot i\cdot 1=-1=\omega^{1}$, as the identity requires.

In the paper, Bluestein's chirp identity turns the middle transform, including its target permutation, into normalized cyclic convolution. <cite data-source="paper">converts the middle transform, including its target permutation, into normalized cyclic convolution</cite> The permutation stays inside the transform identity.
