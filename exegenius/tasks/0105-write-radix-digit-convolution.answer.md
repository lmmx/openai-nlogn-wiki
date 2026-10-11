Radix-digit convolution is a reduction of [exact integer multiplication](exact-integer-multiplication.md) that writes each input as a polynomial in a power of two whose coefficients are its digits, so that the product becomes a convolution of short integer coefficients. It is the first step of the argument for [Integer multiplication below n log n](main-theorem.md): the [Chinese-remainder map](chinese-remainder-map.md) and [carry propagation](carry-propagation.md) pages build on the coefficients it produces.

The paper states the reduction in one sentence: <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite>

**Digits.** Let $x$ and $y$ be the two binary strings, each of $n$ bits. Fix a digit width $b \ge 1$. The digit width is the number of bits in each digit. Cut each input into blocks of $b$ bits, counting from the least significant end and padding the last block with leading zeros. Each block is a digit in base $2^b$, the radix. Let $m = \lceil n/b \rceil$ be the number of digits in each input.

The paper takes <cite data-source="paper">b = ⌈log2 n⌉</cite>, so that $2^b \ge n$.

Let $i$ be the position of a digit, running from $0$ to $m-1$. Let $x_i$ be the digit of $x$ at position $i$, with weight $(2^b)^i$, so that $x = \sum_{i=0}^{m-1} x_i (2^b)^i$. The digits $y_i$ of $y$ are defined the same way.

**Polynomials.** Let $z$ be a formal variable. Write $X(z) = \sum_{i=0}^{m-1} x_i z^i$ and $Y(z) = \sum_{i=0}^{m-1} y_i z^i$. Substituting $z = 2^b$ returns the inputs: $X(2^b) = x$ and $Y(2^b) = y$.

Let $t$ be the position of a product coefficient, running from $0$ to $2m-2$. Let $c_t$ be the integer coefficient of $z^t$ in the product $X(z)Y(z)$. Then
$$c_t = \sum_i x_i\, y_{t-i},$$
summed over the $i$ with $0 \le i \le m-1$ and $0 \le t-i \le m-1$. This sum is the convolution of the digit sequences $(x_i)$ and $(y_i)$. Substituting $z = 2^b$ gives $xy = \sum_t c_t (2^b)^t$, so the product is recovered from the $c_t$. The $c_t$ are not yet binary digits, since a coefficient can exceed $2^b-1$.

**Coefficient size.** Each $c_t$ is a sum of at most $m$ products $x_i y_{t-i}$, and each product is at most $(2^b-1)^2$. So $0 \le c_t \le m(2^b-1)^2$. <cite data-source="paper">Every product coefficient obeys</cite> this bound, and it gives $c_t < 2^{3b}$. Because $b \ge 1$ and $n$ is an integer, $m = \lceil n/b \rceil \le n \le 2^b$. Hence $c_t \le 2^b \cdot (2^b)^2 = 2^{3b}$, and the strict inequality holds because $(2^b-1)^2 < 2^{2b}$. Each coefficient therefore fits in $3b$ bits. Since $b = \lceil \log_2 n \rceil < \log_2 n + 1$, each coefficient has $O(\log n)$ bits.

**Example.** Take $n = 4$. Then $b = 2$ and $m = 2$. Let $x = 1101$ (value 13) and $y = 1011$ (value 11). Splitting into base-4 digits from the least significant end gives $x_0 = 1$, $x_1 = 3$, $y_0 = 3$ and $y_1 = 2$. The coefficients are $c_0 = x_0 y_0 = 3$, $c_1 = x_0 y_1 + x_1 y_0 = 2 + 9 = 11$ and $c_2 = x_1 y_1 = 6$. Check: $3 + 11 \cdot 4 + 6 \cdot 16 = 143 = 13 \cdot 11$. The coefficient $c_1 = 11$ is larger than a digit, so the sequence is not yet the binary product. [Carry propagation](carry-propagation.md) converts it into one.

**Why the split lowers cost.** Arithmetic on one coefficient is cheap, since it works on $O(\log n)$-bit numbers. The cost lies in moving data. The $2m-1$ coefficients occupy $(2m-1) \cdot 3b$ stored bits. Since $m \ge n/b$ and $m \le n/b + 1$, this is between $6n - 3b$ and $6n + 3b$ bits, which is $\Theta(n)$ because $b = O(\log n)$.

The convolution is computed with [Fourier transforms](discrete-fourier-transform.md). A transform proceeds in transform levels, where each level is one pass of address rearrangements and butterfly operations over the whole array. On a tape, a pass reads the array in order and writes each entry back at its new address, so one level costs time proportional to the stored bits. Each level therefore scans all $\Theta(n)$ stored bits, even though each coefficient is small. The paper's count of this cost is that <cite data-source="paper">Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n).</cite> <cite data-source="paper">We therefore need savings in both movement and arithmetic.</cite>
