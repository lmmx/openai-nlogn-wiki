The concept is a chain of multiplication algorithms, from Schönhage and Strassen (1971) to Harvey and van der Hoeven, that multiplies two integers on a multitape Turing machine and whose cost is measured in bits. The main theorem gives a power saving in the logarithmic factor, so the reader needs this chain's starting and ending bounds and the method they share.

Here $n$ is the number of bits in each integer being multiplied.

Schönhage and Strassen showed that two $n$-bit integers can be multiplied <cite data-source="paper">in $O(n\log n\log\log n)$ time on a multitape Turing machine</cite>. They proposed $n\log n$ as the optimal order of growth.

Each algorithm in the chain computes its transforms by the [Discrete Fourier transform and butterflies](dft-fft.md), which evaluates a coefficient list at roots of unity using logarithmically many levels of two-point butterfly operations. Convolution then becomes a pointwise product of two transforms followed by an inverse transform, so the digit convolution of an integer product is handled in the same way.

The later steps of the chain work over rings in which roots of unity are cheap to multiply by. In the ring modulo $y^r+1$, the variable $y$ is a root of unity of order $2r$, and multiplying by a power of $y$ is a cyclic shift with sign changes.

After a sequence of improvements, Harvey and van der Hoeven reached an unconditional algorithm with running time $O(n\log n)$ <cite data-source="paper">reached the unconditional $O(n\log n)$ upper bound</cite>. This is an upper bound. It matches the order Schönhage and Strassen proposed, but it does not by itself show that $n\log n$ is optimal. Its cost is measured against the [The n log n optimality conjecture](nlogn-conjecture.md).
