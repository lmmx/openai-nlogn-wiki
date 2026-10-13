Exact recovery by rounding and carries recovers the exact coefficients of a [Radix-digit convolution](radix-digit-convolution.md), then turns them into the exact binary product by rounding and carrying.

Each computed coefficient lies strictly within $1/2$ of its true integer $w_k$. So $w_k$ is the unique nearest integer, and rounding returns it exactly.

The step rounds the values of the [Gaussian dyadic numbers](gaussian-dyadic.md) that hold the coefficients, and only their real parts matter. Each real part is a dyadic rational $m/2^p$, where $p \ge 1$ is a fixed exponent shared by all of them, and $m$ is its integer numerator. The nearest integer to $m/2^p$ is $\lfloor (m + 2^{p-1})/2^p \rfloor$, which uses only integer arithmetic, so no rounding error occurs. <cite data-source="paper">Round the represented real values to the nearest integers.</cite>

The exact product is $R = \sum_k w_k\, 2^{bk}$, because the convolution evaluated at $2^b$ is the product of the two inputs. Carries convert this sum into digits in radix $2^b$. <cite data-source="paper">Propagate radix-$2^b$ carries in increasing coefficient order.</cite> Let $L$ be the number of positions, at least the number of coefficients, with $bL \ge 2n$; positions past the last coefficient hold zeros. At each position $k < L$, the carry from below is added to $w_k$, the remainder $e_k$ in $\{0,\dots,2^b-1\}$ is kept as the digit, and the quotient, rounded down so that negative values work, is passed upward.

For example, take $b = 2$ and coefficients $5, 3, -1$. Position 0: $5 = 1\cdot 4 + 1$ gives digit 1 and carry 1. Position 1: $3 + 1 = 4 = 1\cdot 4 + 0$ gives digit 0 and carry 1. Position 2: $-1 + 1 = 0$ gives digit 0 and carry 0. The digits $1, 0, 0$ represent $1$, which is $5 + 3\cdot 4 - 1\cdot 16$.

Let $T = \sum_{k<L} e_k\, 2^{bk}$ be the number the digits represent, and let $C$ be the carry left after position $L-1$. Each digit lies in $\{0,\dots,2^b-1\}$, so $0 \le T < 2^{bL}$. Summing each step's identity (coefficient plus carry in equals digit plus $2^b$ times carry out) with weights $2^{bk}$ telescopes to $R = T + C\,2^{bL}$. Since $R$ is a product of two $n$-bit integers, $0 \le R < 2^{2n} \le 2^{bL}$. So $R - T$ is a multiple of $2^{bL}$ strictly between $-2^{bL}$ and $2^{bL}$, hence zero: $C = 0$ and $T = R$. No carry is left over, so the digits are the exact product.

Writing each digit as $b$ bits gives the product, with zeros above its $2n$ bits dropped. <cite data-source="paper">output exactly $2n$ bits in most-significant-first order</cite>.
