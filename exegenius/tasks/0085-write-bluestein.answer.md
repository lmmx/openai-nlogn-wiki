Bluestein's chirp identity rewrites the [discrete Fourier transform](fourier-transform.md) of a vector. It computes its transform by a [cyclic convolution](cyclic-convolution.md) sandwiched between two pointwise multiplications by chirp sequences.

Bluestein's chirp identity acts on the middle transform of the paper's multiplication algorithm, including its [target permutation](gaussian-resampling.md). It turns that transform into <cite data-source="paper">normalized cyclic convolution</cite>.

The $k$-th entry of the transform is $\frac{1}{q}\sum_j u_j \exp(-2\pi i jk/q)$. The exponent $jk$ is a product, so this sum is not a convolution as written. The chirp is $c_p = \exp(-\pi i\, p^2/q)$, the chirp value at an integer $p$. Since $2jk = j^2 + k^2 - (k-j)^2$,

$$\exp\left(-\frac{2\pi i\, jk}{q}\right) = c_j\, c_k\, \overline{c_{k-j}}.$$

Substituting this gives $q$ times the $k$-th entry equal to $c_k \sum_j (u_j c_j)\,\overline{c_{k-j}}$. The factors $c_j$ and $c_k$ are pointwise multiplications, before and after the sum. The sum is a convolution over integer indices, and the wrap of $k-j$ is handled next.

The index $k-j$ can be negative. Since $c_{p+q} = (-1)^q c_p$, for even $q$ the sign is $1$, so $\overline{c_{k-j}} = \overline{c_{(k-j)\bmod q}}$ and the sum becomes
$$\sum_j (u_j c_j)\,\overline{c_{(k-j)\bmod q}},$$
which is the cyclic convolution of $(u_j c_j)_j$ with $(\overline{c_p})_{p=0}^{q-1}$. For odd $q$ the sign $(-1)^q$ does not vanish. The source removes it with a phase twist, which changes the last cyclic coordinate, and <cite data-source="paper">its negative wrap gives precisely the original cyclic wrap after the twist is removed</cite>. This page does not derive that step.
