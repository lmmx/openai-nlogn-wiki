Exact recovery by rounding and carries is the last step that turns the approximate output of a convolution into the exact binary product. It recovers the exact coefficients of the [Radix-digit convolution](radix-digit-convolution.md) from computed real values, and then writes them as bits.

The computed values carry a small error. This step assumes that each computed coefficient lies strictly within $1/2$ of the true integer coefficient. A real number at distance less than $1/2$ from an integer has that integer as its unique nearest integer, so rounding to the nearest integer returns the true coefficient exactly.

The step rounds the values of the [Gaussian dyadic numbers](gaussian-dyadic.md) to the nearest integers, which is exact arithmetic on power-of-two denominators. <cite data-source="paper">Round the represented real values to the nearest integers.</cite>

After rounding, the coefficients are integers, possibly negative. Here $b$ is the number of bits in each radix digit, so the radix is $2^b$. The integers $c_0, c_1, \dots$ (lowest position first) represent the product as $\sum_k c_k\, 2^{bk}$. Carries convert this sum into ordinary digits in radix $2^b$. <cite data-source="paper">Propagate radix-$2^b$ carries in increasing coefficient order.</cite> At each position, the carry from the position below is added to the coefficient, the remainder modulo $2^b$ is kept as the digit, and the quotient is passed upward as the next carry.

For example, take $b = 2$, so the radix is 4, and the coefficients $5, 3, -1$. They represent $5 + 3\cdot 4 - 1\cdot 16 = 1$. Position 0: $5 = 1\cdot 4 + 1$, so the digit is 1 and the carry is 1. Position 1: $3 + 1 = 4 = 1\cdot 4 + 0$, so the digit is 0 and the carry is 1. Position 2: $-1 + 1 = 0$, so the digit is 0 and the carry is 0. The digits $1, 0, 0$ represent 1, the exact value.

Because every coefficient is recovered exactly, the carried digits are the exact binary product.
