Radix-digit convolution reduces [exact integer multiplication](exact-integer-multiplication.md) to a convolution of short integer coefficients, which is the form that the later transforms act on.

Fix a digit width $k$, the number of bits in each digit, and a digit count $m$, the number of digits in each input, with $mk \ge n$. Write the first input in radix $2^k$ as $x = \sum_{j=0}^{m-1} x_j 2^{kj}$, where each digit $x_j$ is an integer in $[0, 2^k)$ and $x_0$ is the least significant digit. The second input $y$ is written in the same way, with digits $y_j$.

Digits become the coefficients of polynomials in an indeterminate $t$: $X(t) = \sum_j x_j t^j$ and $Y(t) = \sum_j y_j t^j$, with $x = X(2^k)$ and $y = Y(2^k)$. The product of these polynomials has coefficients $c_j = \sum_{i+l=j} x_i y_l$, the convolution of the two digit lists, and so $xy = \sum_j c_j 2^{kj}$. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients</cite>

The convolution is the object that transforms can compute quickly on a fixed layout, which is why the reduction stops at this form rather than at the integer product. Each $c_j$ is less than $m 2^{2k}$, so it may be larger than a digit, and the sum $\sum_j c_j 2^{kj}$ is not yet a binary string. The coefficients must be combined by [carry propagation](carry-propagation.md) to give the binary product.

Take $x = 11$ and $y = 6$ with $k = 2$ and $m = 2$. Their digits are $x_0 = 3$, $x_1 = 2$, $y_0 = 2$ and $y_1 = 1$, so $c_0 = 3 \cdot 2 = 6$, $c_1 = 3 \cdot 1 + 2 \cdot 2 = 7$ and $c_2 = 2 \cdot 1 = 2$. Then $6 + 7 \cdot 4 + 2 \cdot 16 = 66 = 11 \cdot 6$. The coefficient $c_1 = 7$ exceeds the largest digit $2^k - 1 = 3$, so it must be carried.
