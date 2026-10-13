A synthetic polynomial transform is a discrete Fourier transform whose roots of unity are powers of $y$, so that each multiplication by a root is a signed shift rather than a true multiplication. It is the transform used to compute normalized [Cyclic convolution](cyclic-convolution.md) on the power-of-two axes. The motivation is that an ordinary Fourier transform multiplies by complex roots of unity at every butterfly, and here those multiplications become shifts.

The transform is computed over the [Polynomial ring modulo yʳ + 1](polynomial-ring.md), with $r$ a power of two, so each element is a coefficient list of length $r$. Multiplication by $y$ uses $y^r=-1$. For $r=4$,
$$y\,(a+by+cy^2+dy^3) = -d + ay + by^2 + cy^3.$$

The transform is built from the powers of $y$, and $y$ is a [Root of unity](roots-of-unity.md) of order $2r$. The twiddle factors, the roots of unity by which a butterfly multiplies one of its inputs, are therefore powers $y^j$. Multiplying by $y^j$ is a signed shift of the coefficient list: entries that wrap past position $r-1$ change sign. <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>.

The transform is computed by successive layers of [Simultaneous butterfly layer H₀](butterfly-layer.md). Each layer applies $H_0$ to pairs of records whose indices differ in one selected bit, after multiplying one record of each pair by a twiddle factor. Since the twiddle factors are signed shifts, each layer costs only additions, subtractions and shifts of coefficient lists.
