The butterfly operation is the two-point map that serves as the basic step of a fast transform: a transform on many values is carried out in layers, and each layer applies the butterfly to pairs of values.

Let $u$ and $v$ be two input values, and let $H_0$ denote the butterfly map, so that $H_0(u,v)=\left(\frac{u+v}{2},\frac{u-v}{2}\right)$. On column vectors this is multiplication by the matrix
$$H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$
For example, $H_0(3,1)=(2,1)$.

The butterfly is not its own inverse. Squaring the matrix gives $H_0^2=\frac14\begin{pmatrix}2&0\\0&2\end{pmatrix}=\frac12 I$, where $I$ denotes the $2\times 2$ identity matrix. So applying the butterfly twice returns the pair divided by two: $H_0(H_0(u,v))=\left(\frac u2,\frac v2\right)$. Check with the example: $H_0(2,1)=\left(\frac32,\frac12\right)$, which is $\frac12(3,1)$.

The butterfly is a scaled length-2 case of the [discrete Fourier transform](fourier-transform.md). The length-2 transform uses the root of unity $-1$ and returns the unscaled sums $u+v$ and $u-v$; the butterfly divides both by $2$. The factor $\frac12$ keeps magnitudes from growing across layers: $\left|\frac{u\pm v}{2}\right|\le\max(|u|,|v|)$, since $|u\pm v|\le|u|+|v|\le 2\max(|u|,|v|)$.

The paper's transform calculation uses address rearrangements (moving stored values to other addresses), signed shifts (multiplying a value by a signed power of two), and the butterfly steps <cite data-source="paper">two-point butterfly operations</cite>.

Each butterfly touches only two values, so the cost of a level is set by how many pairs it processes. A [simultaneous butterfly layer](simultaneous-butterfly-layer.md) applies the same butterfly to one address bit of every stored record at once.
