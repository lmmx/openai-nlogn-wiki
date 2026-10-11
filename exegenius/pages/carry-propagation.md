Carry propagation is the step that turns a list of integer coefficients into the binary digits of the number they jointly represent. It is the step of [Integer multiplication below n log n](main-theorem.md) that turns the recovered coefficients into the exact binary product.

Carry propagation takes its input from [Radix-digit convolution](radix-digit-convolution.md). That input is a list of integers $c_0, c_1, \dots$. Here $m$ is the position index: it counts the positions of the list from $0$ at the least significant end. The entry $c_m$ is the coefficient of $\xi^m$ in the product of the two digit polynomials. This page uses $m$ for that position index, not for the bit count of [Integer](integer.md).

Carry propagation takes its digit width from the [base-2 logarithm](base-two-logarithm.md) of $n$: $b = \lceil \log_2 n \rceil$. The paper sets $b$ this way for sufficiently large $n$: <cite data-source="paper">b = ⌈log2 n⌉</cite>. Carry propagation computes its digit count by the [ceiling function](ceiling-function.md): $J = \lceil n/b \rceil$. So $J$ is the number of digits in each input, as on [Radix-digit convolution](radix-digit-convolution.md).

The radix is $Q_0 = 2^b$, the number of values a digit can take, so each digit is a $b$-bit block. For $n \ge 2$ we have $b \ge 1$, so $J \le n$, and $2^b \ge n$ by the choice of $b$; hence $J \le Q_0$. A coefficient is not itself a digit. Each $c_m$ is a sum of at most $J$ products of two digits, each at most $(Q_0-1)^2$, so $0 \le c_m \le J(Q_0-1)^2 < JQ_0^2 \le Q_0^3$. The paper states the same bound: <cite data-source="paper">0 ≤ cj ≤ q(2b − 1)2 < 23b</cite>. The coefficients therefore overflow a digit. Because the two digit polynomials take the values of the inputs at $2^b$, the product is $\sum_m c_m Q_0^m$, and carry propagation turns this sum into binary digits by moving each overflow to the next position.

Let $\gamma_m$ be the carry into position $m$, the amount carried from the lower positions. Let $\sigma_m$ be the output digit at position $m$, which lies in $\{0, \dots, Q_0-1\}$. Set $\gamma_0 = 0$ and, for $m \ge 0$,

$$\sigma_m = (c_m + \gamma_m) \bmod Q_0, \qquad \gamma_{m+1} = \left\lfloor \frac{c_m + \gamma_m}{Q_0} \right\rfloor,$$

where $w \bmod Q_0$ is the remainder of $w$ on division by $Q_0$. The paper writes $k_j$ for the carry: <cite data-source="paper">The value kj is the carry from the processed coefficients into the remaining positions.</cite> Division with remainder gives, at every position,

$$c_m + \gamma_m = \sigma_m + Q_0\,\gamma_{m+1}.$$

Summing these identities gives the invariant. Here $h$ is the summation index, running over the positions below $m$. For every $m \ge 0$,

$$\sum_{h<m} c_h Q_0^h = \sum_{h<m} \sigma_h Q_0^h + \gamma_m Q_0^m.$$

The invariant says that the processed coefficients equal the processed digits plus the carry $\gamma_m$, which is still owed to the higher positions with weight $Q_0^m$. It holds at $m = 0$, where both sums are empty and $\gamma_0 = 0$. If it holds at $m$, add $c_m Q_0^m$ to both sides. The division identity at $m$, multiplied by $Q_0^m$, shows that $c_m Q_0^m + \gamma_m Q_0^m = \sigma_m Q_0^m + \gamma_{m+1} Q_0^{m+1}$. Substituting this turns the right side into the invariant at $m+1$.

The recurrence reads $c_m$ only after $\gamma_m$ is known, and $\gamma_m$ depends on all lower coefficients, so the positions must be processed from $m = 0$ upward. The paper gives the same order: <cite data-source="paper">Propagate radix-2b carries in increasing coefficient order</cite>, and <cite data-source="paper">this carry scan proceeds from least to most significant</cite>.

The carries stay small. Suppose $0 \le \gamma_m \le J(Q_0-1)$. Then $c_m + \gamma_m \le J(Q_0-1)^2 + J(Q_0-1) = JQ_0(Q_0-1)$, so $\gamma_{m+1} \le J(Q_0-1)$. Since $\gamma_0 = 0$, every carry satisfies $0 \le \gamma_m \le J(Q_0-1) < Q_0^2$, the last step because $J \le Q_0$. So each carry fits in $2b$ bits. The paper states the same carry bound: <cite data-source="paper">The carries satisfy 0 ≤ kj ≤ q(Q0 − 1) < Q20</cite>. It also gives the same storage cost: <cite data-source="paper">Carry storage and work per coefficient are O(b) bits and steps</cite>.

The coefficients vanish past the end. The product of two polynomials of degree $J-1$ has degree at most $2J-2$, so $c_m = 0$ for $m \ge 2J-1$. Then $\gamma_{2J-1} < Q_0^2$ gives $\gamma_{2J} \le Q_0-1$, and $\gamma_{2J+1} = 0$. The paper drains this leftover carry in the same order: <cite data-source="paper">drain the final O(b)-bit carry in the same order</cite>. Hence $\sigma_m = 0$ for $m \ge 2J+1$. Taking $m = 2J+1$ in the invariant, where every $c_h$ with $h \ge 2J+1$ is zero, gives $\sum_h c_h Q_0^h = \sum_{h \le 2J} \sigma_h Q_0^h$. Each $\sigma_h$ is a $b$-bit block, so writing $\sigma_{2J}, \dots, \sigma_0$ from the top gives a binary string whose value is the product. The top blocks may be zero, and the paper removes such padding to output exactly $2n$ bits: <cite data-source="paper">Remove only those zero padding bits and retain leading zeros as needed to produce exactly 2n bits</cite>.

For $Q_0 = 4$ (so $b = 2$) and coefficients $(c_0, c_1, c_2) = (5, 3, 7)$ with $c_3 = 0$, the carry scan runs as follows.

- $m=0$: $c_0 + \gamma_0 = 5$, so $\sigma_0 = 1$ and $\gamma_1 = 1$.
- $m=1$: $c_1 + \gamma_1 = 4$, so $\sigma_1 = 0$ and $\gamma_2 = 1$.
- $m=2$: $c_2 + \gamma_2 = 8$, so $\sigma_2 = 0$ and $\gamma_3 = 2$. The coefficient 7 exceeds the digit range, and the carry 2 passes to position 3.
- $m=3$: $c_3 + \gamma_3 = 2$, so $\sigma_3 = 2$ and $\gamma_4 = 0$.

The digits $(\sigma_3, \sigma_2, \sigma_1, \sigma_0) = (2, 0, 0, 1)$ give $2 \cdot 4^3 + 0 \cdot 4^2 + 0 \cdot 4 + 1 = 129 = 5 + 3 \cdot 4 + 7 \cdot 16$. In binary, each digit takes two bits: $10\,00\,00\,01$, which is $129$.
