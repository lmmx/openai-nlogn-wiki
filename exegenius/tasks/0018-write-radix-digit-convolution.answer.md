A radix-digit convolution computes a product of two integers as a polynomial convolution. Radix-digit convolution reduces [exact integer multiplication](exact-integer-multiplication.md) to a polynomial product whose coefficients are short integers.

Let $B = 2^k$ be the radix, the base in which each integer is written, with $k$ the number of bits in each radix digit. Let $d$ be the number of radix digits of each input. Let $x$ and $y$ be the two inputs, nonnegative integers below $B^d$. Let $a = (a_0, \dots, a_{d-1})$ be the coefficient list of $x$, its radix digits, so that $x = \sum_{i=0}^{d-1} a_i B^i$ with $0 \le a_i < B$. Let $z$ be a formal variable, a placeholder for the powers of a polynomial. Then $x$ is the value at $z = B$ of the polynomial $a(z) = \sum_i a_i z^i$. The input $y$ has the coefficient list $b$ in the same way.

The convolution $c = a * b$ is the coefficient list of the product $a(z)b(z)$, with $c_m = \sum_{i+l=m} a_i b_l$. Since $a(B) = x$ and $b(B) = y$, we have $xy = \sum_m c_m B^m$, so carrying the $c_m$ in base $B$ gives the binary representation of $xy$. Each $c_m$ is a sum of at most $d$ products of digits, so $c_m < dB^2$: the coefficients are short integers even when $x$ and $y$ are long.

For example, take $B = 4$, $d = 2$, $x = 13$ and $y = 11$. Then $13 = 3\cdot 4 + 1$ and $11 = 2\cdot 4 + 3$, so $a = (1, 3)$ and $b = (3, 2)$. The convolution is $c = (3, 11, 6)$, since $c_0 = 1\cdot 3$, $c_1 = 1\cdot 2 + 3\cdot 3$ and $c_2 = 3\cdot 2$, and $3 + 11\cdot 4 + 6\cdot 16 = 143 = 13\cdot 11$.

Computing this convolution directly takes about $d^2$ multiplications of digits. Radix-digit convolution is computed by [Fourier transforms](discrete-fourier-transform.md) of length at least $2d-1$: transform $a$ and $b$, multiply pointwise, and invert.

The sources start from this reduction. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>. After [Gaussian resampling](gaussian-resampling.md), the convolution is computed with transforms of [axis lengths](axis-length.md) that are powers of two.
