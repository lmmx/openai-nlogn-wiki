Schönhage–Strassen to Harvey–van der Hoeven multiplication is a chain of multitape algorithms that lowers the cost of multiplying two integers from $O(n\log n\log\log n)$ to $O(n\log n)$. The main theorem's power saving is measured against the ends of this chain. Here $n$ is the number of bits in each integer being multiplied.

Schönhage and Strassen showed that two $n$-bit integers can be multiplied <cite data-source="paper">in $O(n\log n\log\log n)$ time on a multitape Turing machine</cite>. Each algorithm in the chain computes its transforms by the [Discrete Fourier transform and butterflies](dft-fft.md), evaluating its coefficient lists at roots of unity in a suitable ring.

The method splits each integer into $q$ digits of $b$ bits, so the product is a convolution of two digit lists with $q$ entries each. That linear convolution has $2q-1$ coefficients. Padding the lists to a power of two $S \ge 2q-1$ makes the cyclic convolution of length $S$ equal to the linear one, because no coefficient wraps around. Transform both padded lists, multiply the transforms entry by entry, and invert the transform. The entrywise products are products of shorter integers, handled by the same method; this recursion produces the extra $\log\log n$ factor. Their proof is in Schönhage and Strassen's paper.

Later algorithms keep this scheme and change the ring. Fürer's 2007 bound replaces the factor $\log\log n$ by $2^{O(\log^* n)}$. Later improvements reduced the exponential factor to $8^{\log^* n}$ and then $4^{\log^* n}$. Harvey and van der Hoeven removed it, obtaining an unconditional algorithm with running time $O(n\log n)$ <cite data-source="paper">reached the unconditional $O(n\log n)$ upper bound</cite>.

In the ring modulo $y^r+1$, $y$ is a root of unity of order $2r$, since $y^r=-1$, and multiplying by a power of $y$ is a cyclic shift with sign changes. This is why the later stages use such rings.

The $O(n\log n)$ bound matches the order Schönhage and Strassen proposed, but as an upper bound it does not show that $n\log n$ is optimal. The chain's cost is measured against the [The n log n optimality conjecture](nlogn-conjecture.md).
