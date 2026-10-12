The butterfly operation is the two-point map that serves as the basic step of a fast transform: a transform on many values is assembled from layers that apply it to pairs of values.

Write $u$ and $v$ for two input values; the two-point butterfly $H_0$ maps them to $\left(\frac{u+v}{2}, \frac{u-v}{2}\right)$. In matrix form on column vectors,
$$H_0=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$
For example, $H_0(3,1)=(2,1)$. Since $H_0^2=I$, applying the butterfly twice returns the original pair.

The butterfly is a scaled length-2 case of the [discrete Fourier transform](fourier-transform.md). The length-2 transform uses the root of unity $-1$ and returns the unscaled sums $u+v$ and $u-v$. The factor $\frac12$ keeps magnitudes from growing across layers, since $\left|\frac{u\pm v}{2}\right|\le\max(|u|,|v|)$.

The paper's transform calculation uses address rearrangements, signed shifts, and the butterfly steps <cite data-source="paper">two-point butterfly operations</cite>. Its number of levels is logarithmic because each level halves the block size: a transform on $n$ values is built from two transforms on $n/2$ values, followed by one layer that combines them pairwise, and this splitting repeats until each block holds a single value. For $n$ a power of two this gives exactly $\log_2 n$ levels. Here $\Theta(\log n)$ denotes a count lying between two positive constant multiples of $\log n$.

Each butterfly touches only two values, so the cost of a level is set by how many pairs it processes. A [simultaneous butterfly layer](simultaneous-butterfly-layer.md) applies the same butterfly to one address bit of every record at once.
