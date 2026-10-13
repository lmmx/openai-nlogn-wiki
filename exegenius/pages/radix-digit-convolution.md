Radix-digit convolution is a way of writing the product of two $n$-bit integers as a product of two polynomials with small nonnegative coefficients, the first step toward integer products on a fixed-tape machine.

Fix a digit width $\beta$, the number of bits in each radix digit. The exact-recovery page calls this width $b$, but this page writes $\beta$ throughout. Let $m = \lceil n/\beta \rceil$ be the number of digits in each input. The digit $u_i$, for $0 \le i \le m-1$, is the $i$-th radix digit of the first input, and $v_i$ is the $i$-th radix digit of the second input, each in $\{0,\dots,2^\beta-1\}$. Let $t$ be a formal variable marking coefficient positions. The polynomial $U(t)$ has the digits of the first input as coefficients, and $V(t)$ has those of the second: $U(t) = \sum_{i=0}^{m-1} u_i t^i$ and $V(t) = \sum_{i=0}^{m-1} v_i t^i$.

Evaluating at $t = 2^\beta$ gives back each input, and evaluation turns a product of polynomials into a product of values. Let $W(t) = U(t)V(t)$ be the product polynomial, so the integer product is $U(2^\beta)V(2^\beta) = W(2^\beta)$. Its $k$-th coefficient $w_k$ is the sum of $u_i v_j$ over $i+j=k$, a convolution of the two digit lists.

Each $w_k$ sums at most $m$ products, each below $2^{2\beta}$, so $0 \le w_k < m\,2^{2\beta}$.

Zero padding, which extends each list with zeros to length $S \ge 2m-1$, keeps every index $i+j \le 2m-2$ below the length, so no term wraps around. Computing $W$ from the digit lists is a [Cyclic convolution](cyclic-convolution.md) of length $S$, so the integer product is reduced to a cyclic convolution.

For example, take $\beta = 4$ and $n = 8$, so $m = 2$. The integers $75 = 11 + 4\cdot 16$ and $38 = 6 + 2\cdot 16$ have digits $u_0 = 11$, $u_1 = 4$, $v_0 = 6$, $v_1 = 2$, so $W(t) = 66 + 46t + 8t^2$, and at $t = 16$ this equals $2850 = 75 \cdot 38$.

The carries are handled afterwards by [Exact recovery by rounding and carries](exact-recovery.md).
