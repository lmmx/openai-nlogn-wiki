The forward transform is built from the [Discrete Fourier transform](discrete-fourier-transform.md) by taking the standard sign in its exponent, and it is applied first to both inputs of a convolution. The paper's exact multiplication method starts with this step, and the pages on rank-saving recursion and Gaussian resampling rely on it.

For a length $q$ with $\omega = e^{-2\pi i/q}$, the forward transform of a vector $u$ of $q$ complex numbers has entries

$$(F_q u)_\ell = \frac{1}{q}\sum_{s=0}^{q-1} \omega^{s\ell}\, u_s, \qquad 0 \le \ell < q.$$

Since $\omega^{s\ell} = e^{-2\pi i\, s\ell/q}$, the exponent carries the minus sign. The positive-sign transform $F_q^+$ has $\omega^{-s\ell}$ in the same sum, and it undoes $F_q$ up to the factor $q$.

For example, take $q = 4$ and $u = (1, 2, 3, 4)$. Here $\omega = -i$, so the powers $\omega^0, \omega^1, \omega^2, \omega^3$ are $1, -i, -1, i$. The coordinate $\ell = 1$ is

$$(F_4 u)_1 = \tfrac14\,(1 - 2i - 3 + 4i) = -\tfrac12 + \tfrac12 i,$$

and the full transform is $F_4 u = \left(\tfrac52,\ -\tfrac12 + \tfrac12 i,\ -\tfrac12,\ -\tfrac12 - \tfrac12 i\right)$.

The reason to use this transform is the convolution rule. Let $a$ and $b$ be two sequences of length $q$, and let $c$ be their cyclic convolution, $c_k = \sum_{i=0}^{q-1} a_i\, b_{(k-i) \bmod q}$. Expanding the transform and using $\omega^{\ell k} = \omega^{\ell(i+j)}$ when $k \equiv i + j \pmod q$ gives $\sum_k \omega^{\ell k} c_k = \left(\sum_i \omega^{\ell i} a_i\right)\left(\sum_j \omega^{\ell j} b_j\right)$. Therefore

$$(F_q c)_\ell = q\,(F_q a)_\ell\,(F_q b)_\ell,$$

so the cyclic convolution becomes an entrywise product of the two forward transforms. The paper states the same rule for its synthetic arrays, where the transform acts on records: <cite data-source="paper">Ft− (f ∗ g) = M (Ft− f )(Ft− g).</cite>

The inverse step uses the positive-sign transform. Writing $F_q^+F_q = I/q$ for the identity $I$, the paper's version of this identity is <cite data-source="paper">Ft+ Ft− = t−1 I.</cite> Applying the forward transform to both inputs, multiplying entrywise, and then applying $F_q^+$ recovers the cyclic convolution up to the factor $q$ that the normalization leaves.
