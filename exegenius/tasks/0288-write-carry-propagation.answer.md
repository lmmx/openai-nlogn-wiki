Carry propagation is the final arithmetic step that turns a list of integer coefficients into the binary digits of their value. It gives the output of [Integer multiplication below n log n](main-theorem.md) its exact binary form.

Carry propagation takes its input from [Radix-digit convolution](radix-digit-convolution.md), whose output is the list of integer coefficients $c_0, c_1, \dots$ of the product of the two digit polynomials.

Carry propagation takes its digit width $b = \lceil \log_2 n \rceil$ from the [base-2 logarithm](base-two-logarithm.md) of $n$, the bit length of the inputs. Carry propagation computes its digit count by the [ceiling function](ceiling-function.md): $m = \lceil n/b \rceil$ is the number of digits in each input. The radix is $Q_0 = 2^b$, the number of values a digit can take, which is the base in which each digit is written. The paper uses this choice for large $n$: <cite data-source="paper">b = ⌈log2 n⌉,</cite> so that $Q_0 \ge n$. The index $t$ runs over the positions $0, 1, \dots$ of the list of coefficients, so $\sum_t c_t Q_0^t$ is the product.

Each $c_t$ is a sum of at most $m$ products of two digits, each at most $(Q_0-1)^2$, so $0 \le c_t \le m(Q_0-1)^2$. Since $m \le n \le Q_0$, this is below $Q_0^3$, as the paper also states: <cite data-source="paper">0 ≤ cj ≤ q(2b − 1)2 < 23b</cite>.

Carry propagation rewrites the same sum with digits. The digit $d_t$ is the $t$th base-$Q_0$ digit of the output, so $0 \le d_t < Q_0$. The carry $e_t$ is the amount carried into position $t$ from the lower positions. <cite data-source="paper">The value kj is the carry from the processed coefficients into the remaining positions.</cite> Set $e_0 = 0$ and, for $t \ge 0$,

$$d_t = (c_t + e_t) \bmod Q_0, \qquad e_{t+1} = \left\lfloor \frac{c_t + e_t}{Q_0} \right\rfloor,$$

where $w \bmod Q_0$ is the remainder of $w$ on division by $Q_0$, and $\lfloor w \rfloor$ is the largest integer not above $w$. Division with remainder gives, at every position,

$$c_t + e_t = d_t + Q_0\, e_{t+1}.$$

Why this keeps the value: in the identity below, $\tau$ counts the low positions already processed, so the sums run over $t < \tau$. For every $\tau \ge 0$,

$$\sum_{t<\tau} c_t Q_0^t = \sum_{t<\tau} d_t Q_0^t + e_\tau Q_0^\tau.$$

The identity says that the processed coefficients have the same value as the processed digits plus the carry $e_\tau$, which is still owed to the higher positions. It holds at $\tau = 0$, where both sides are $0$. If it holds at $\tau$, add $c_\tau Q_0^\tau$ to the left side. Multiplying $c_\tau + e_\tau = d_\tau + Q_0 e_{\tau+1}$ by $Q_0^\tau$ gives $c_\tau Q_0^\tau + e_\tau Q_0^\tau = d_\tau Q_0^\tau + e_{\tau+1} Q_0^{\tau+1}$, so the left side becomes $\sum_{t<\tau+1} d_t Q_0^t + e_{\tau+1} Q_0^{\tau+1}$, which is the identity at $\tau+1$.

The recurrence reads $c_t$ only after $e_t$ is known, and $e_t$ depends on all lower coefficients, so the positions must be processed from $t = 0$ upward. <cite data-source="paper">so this carry scan proceeds from least to most significant.</cite>

The carries stay small. If $0 \le e_t \le m(Q_0-1)$, then $c_t + e_t \le m(Q_0-1)^2 + m(Q_0-1) = mQ_0(Q_0-1)$, so $e_{t+1} \le m(Q_0-1)$. Since $e_0 = 0$, every carry obeys this bound. <cite data-source="paper">The carries satisfy 0 ≤ kj ≤ q(Q0 − 1) < Q20</cite>. Since $m \le Q_0$, the bound is below $Q_0^2$, so each carry fits in $2b$ bits. <cite data-source="paper">Carry storage and work per coefficient are O(b) bits and steps.</cite>

Coefficients vanish past the end. The product of two polynomials of degree $m-1$ has degree at most $2m-2$, so $c_t = 0$ for $t \ge 2m-1$, and there $e_{t+1} = \lfloor e_t / Q_0 \rfloor$. The carry $e_{2m-1}$ is below $Q_0^2$, so $e_{2m} \le Q_0 - 1$ and $e_{2m+1} = 0$. The leftover carry is written out the same way, one digit at a time: <cite data-source="paper">drain the final O(b)-bit carry in the same order</cite>. Its digits are $d_t = e_t \bmod Q_0$ for $t = 2m-1, 2m$, and $d_t = 0$ beyond. Taking $\tau = 2m+1$ in the identity, where every $c_t$ with $t \ge 2m+1$ is zero and $e_{2m+1} = 0$, gives $\sum_t c_t Q_0^t = \sum_t d_t Q_0^t$. Each $d_t$ is a $b$-bit block, so the product is the binary string formed by writing $d_{2m}, \dots, d_0$ from the top down, each in $b$ bits.

For $Q_0 = 4$ (so $b = 2$) and three coefficients $(c_0, c_1, c_2) = (5, 3, 7)$:

- $t=0$: $c_0 + e_0 = 5$, so $d_0 = 1$ and $e_1 = 1$.
- $t=1$: $c_1 + e_1 = 4$, so $d_1 = 0$ and $e_2 = 1$.
- $t=2$: $c_2 + e_2 = 8$, so $d_2 = 0$ and $e_3 = 2$.
- The leftover carry $e_3 = 2 < 4$ gives $d_3 = 2$ and $e_4 = 0$.

The digits $(d_3, d_2, d_1, d_0) = (2, 0, 0, 1)$ give $2 \cdot 64 + 0 \cdot 16 + 0 \cdot 4 + 1 = 129 = 5 + 3 \cdot 4 + 7 \cdot 16$. In binary, each digit takes two bits: $10\,00\,00\,01$.
