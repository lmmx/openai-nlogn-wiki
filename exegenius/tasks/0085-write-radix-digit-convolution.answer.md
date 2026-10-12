Radix-digit convolution reduces [exact integer multiplication](exact-integer-multiplication.md) to a convolution of short integer digit lists, which is the first step toward a fast product.

Fix a digit width $d$, the number of bits in each digit, and a digit count $L$, the number of digits in each input, with $Ld \ge n$ so that both inputs fit. Here $x$ and $y$ denote the integers $\mathrm{val}(x)$ and $\mathrm{val}(y)$, not the binary strings. Write them in radix $2^d$:

$$x = \sum_{j=0}^{L-1} x_j 2^{dj}, \qquad y = \sum_{j=0}^{L-1} y_j 2^{dj}.$$

The digit $x_j$ is the $j$-th radix-$2^d$ digit of $x$, an integer in $[0, 2^d)$, with $x_0$ the least significant; $y_j$ is defined the same way from $y$.

Digits become the coefficients of polynomials in a new indeterminate $t$, $P(t) = \sum_{j} x_j t^j$ and $Q(t) = \sum_{j} y_j t^j$, so that $P(2^d) = x$ and $Q(2^d) = y$. The product $P(t)Q(t) = \sum_j e_j t^j$ has coefficients $e_j = \sum_{i+l=j} x_i y_l$, the convolution of the two digit lists, and so $xy = P(2^d)Q(2^d) = \sum_j e_j 2^{dj}$.

The convolution is computed by [transforms](discrete-fourier-transform.md) quickly on a fixed layout, which is why the reduction stops at this form rather than at the integer product. The paper's starting point is this reduction <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>.

Each $e_j$ is a sum of at most $L$ products, each below $2^{2d}$, so it may exceed a digit, and $\sum_j e_j 2^{dj}$ is not yet a binary string. [Carry propagation](carry-propagation.md) adds each coefficient to the carry from the previous position to give the binary product.

Take $x = 11$ and $y = 6$ with $d = 2$ and $L = 2$. Their digits are $x_0 = 3$, $x_1 = 2$, $y_0 = 2$ and $y_1 = 1$, so $e_0 = 3 \cdot 2 = 6$, $e_1 = 3 \cdot 1 + 2 \cdot 2 = 7$ and $e_2 = 2 \cdot 1 = 2$. Then $6 + 7 \cdot 4 + 2 \cdot 16 = 66 = 11 \cdot 6$. The coefficient $e_1 = 7$ exceeds the largest digit $2^d - 1 = 3$, so it must be carried.
