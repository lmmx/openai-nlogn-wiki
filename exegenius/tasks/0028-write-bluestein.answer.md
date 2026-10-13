Bluestein's chirp identity rewrites the [discrete Fourier transform](fourier-transform.md) of a vector. Bluestein's chirp identity computes its transform by a [cyclic convolution](cyclic-convolution.md) sandwiched between two pointwise multiplications by chirp sequences. In the multiplication algorithm, the middle transform, including its target permutation, becomes <cite data-source="paper">normalized cyclic convolution</cite>.

Let $q$ be the number of entries of the vector $u = (u_0, \dots, u_{q-1})$ being transformed. Let $j$ and $k$ be indices running from $0$ to $q-1$, with $j$ indexing the input and $k$ the output. The $k$-th output entry is $\frac{1}{q}\sum_{j} u_j \exp(-2\pi i jk/q)$.

The exponent $jk$ is a product, so the transform is not directly a convolution. The identity splits it. Write $c_m = \exp(-\pi i\, m^2/q)$ for the chirp value at an integer index $m$. Since $2jk = j^2 + k^2 - (k-j)^2$,

$$\exp\left(-\frac{2\pi i\, jk}{q}\right) = c_j\, c_k\, \overline{c_{k-j}}.$$

Substituting this and pulling $c_k$ out of the sum gives $q$ times the $k$-th output entry equal to $c_k \sum_j (u_j c_j)\,\overline{c_{k-j}}$. The sum is a convolution of the chirp-multiplied vector $(u_j c_j)$ with the sequence $(\overline{c_m})$. The factors $c_j$ before it and $c_k$ after it are pointwise multiplications.

The index $k-j$ can be negative, so it must wrap modulo $q$. This wrap is not free, because $c_{m+q} = (-1)^q c_m$. The source handles it in its multidimensional layout with a phase twist, which this page does not derive.
