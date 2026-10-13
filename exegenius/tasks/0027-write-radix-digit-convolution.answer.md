Radix-digit convolution rewrites the product of two $n$-bit integers as a product of two polynomials with small nonnegative coefficients, which is the first step toward computing integer products on a fixed-tape machine.

Fix a digit width $b$, the number of bits in each radix digit. Let $m = \lceil n/b \rceil$ be the number of digits in each input. The digit $u_i$, for $0 \le i \le m-1$, is the $i$-th radix digit of the first input, and $v_i$ is the $i$-th radix digit of the second input, each in $\{0,\dots,2^b-1\}$. Let $t$ be a formal variable. The polynomial $U(t)$ has the digits of the first input as coefficients. The polynomial $V(t)$ has the digits of the second input as coefficients, so that $U(t) = \sum_{i=0}^{m-1} u_i t^i$ and $V(t) = \sum_{i=0}^{m-1} v_i t^i$.

Evaluating at $t = 2^b$ recovers the inputs, since $U(2^b) = \sum_i u_i 2^{bi}$, and evaluation respects products. The product of the inputs is therefore $U(2^b)V(2^b) = W(2^b)$, where the product polynomial is $W(t) = U(t)V(t)$. Its $k$-th coefficient $w_k$ is the sum of $u_i v_j$ over $i+j=k$, which is a convolution of the two digit lists.

Each $w_k$ is a sum of at most $m$ products $u_i v_j$, each below $2^{2b}$, so $0 \le w_k < m\,2^{2b}$. The coefficients are therefore short nonnegative integers whose bound depends only on $b$ and $m$.

Computing $W$ from the two digit lists is a [Cyclic convolution](cyclic-convolution.md) of length at least $2m-1$ with zero padding, so the integer product is reduced to a cyclic convolution.

For example, take $b = 4$ and $n = 8$, so $m = 2$. The integers $75 = 11 + 4\cdot 16$ and $38 = 6 + 2\cdot 16$ give $U(t) = 11 + 4t$ and $V(t) = 6 + 2t$, so $W(t) = 66 + 46t + 8t^2$. At $t = 16$ this gives $66 + 736 + 2048 = 2850 = 75 \cdot 38$, and every coefficient lies below $m\,2^{2b} = 512$.

The point of the reduction is that a convolution of short coefficients can be computed by transforms, and the carries are handled afterwards by [Exact recovery by rounding and carries](exact-recovery.md).
