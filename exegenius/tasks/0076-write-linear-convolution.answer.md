The linear convolution of two coefficient lists $a = (a_0, \dots, a_{m-1})$ and $b = (b_0, \dots, b_{q-1})$ is the list $c$ of coefficients of the ordinary product of the polynomials $a(x) = \sum_k a_k x^k$ and $b(x) = \sum_l b_l x^l$. Its entries are $c_j = \sum_{k+l=j} a_k b_l$, with no index wrapping, and its length is $m + q - 1$.

As an example, take $a = (1, 2)$ and $b = (0, 1, 1)$. The product is $(1 + 2x)(x + x^2) = x + 3x^2 + 2x^3$, so the linear convolution is $c = (0, 1, 3, 2)$, a list of length $4 = 2 + 3 - 1$.

Linear convolution is the operation the multiplication of integers needs before any wraparound is removed. The [cyclic convolution](cyclic-convolution.md) of length $S$ agrees with the linear convolution whenever the linear result has length at most $S$, because no term then wraps around. The paper uses this to avoid wraparound: its radix-digit polynomials have degree at most $2q - 2$, which is below the cyclic length $S$.

The [radix-digit convolution](radix-digit-convolution.md) is a linear convolution of this kind applied to the digits of the two integers.
