Carry propagation is the step that turns a list of integer coefficients into the binary digits of their value. It is the step of [Integer multiplication below n log n](main-theorem.md) that turns the recovered coefficients into the exact binary product.

Carry propagation takes its input from [Radix-digit convolution](radix-digit-convolution.md). That input is a list of integers, indexed by a position $t$ running over $0, 1, \dots$; the entry $c_t$ at position $t$ is the coefficient of $z^t$ in the product of the two digit polynomials.

Carry propagation takes its digit width $b = \lceil \log_2 n \rceil$ from the [base-2 logarithm](base-two-logarithm.md) of $n$. The paper sets $b$ this way for sufficiently large $n$: <cite data-source="paper">b = ⌈log2 n⌉</cite>. Carry propagation computes its digit count by the [ceiling function](ceiling-function.md): $N = \lceil n/b \rceil$ is the number of digits in each input (the paper writes $q$ for $N$).

The radix is $Q_0 = 2^b$, the number of values a digit can take, so each digit is written in base $Q_0$. The choice $b = \lceil \log_2 n \rceil$ gives $Q_0 \ge n$, because $2^{\lceil \log_2 n \rceil} \ge n$. For $n \ge 2$ we have $b \ge 1$, so $N = \lceil n/b \rceil \le n \le Q_0$. The bounds below use this inequality, and it is the reason for the choice of $b$.

Each $c_t$ is a sum of at most $N$ products of two digits, each at most $(Q_0-1)^2$, so $0 \le c_t \le N(Q_0-1)^2 < NQ_0^2 \le Q_0^3$. The paper states the same bound: <cite data-source="paper">0 ≤ cj ≤ q(2b − 1)2 < 23b</cite>.

Carry propagation rewrites the same sum digit by digit. For each position $t$, let $\sigma_t$ be the output digit at position $t$, which lies in $\{0, \dots, Q_0-1\}$, and let $\gamma_t$ be the carry into position $t$, the amount carried from the lower positions. Set $\gamma_0 = 0$ and, for $t \ge 0$,

$$\sigma_t = (c_t + \gamma_t) \bmod Q_0, \qquad \gamma_{t+1} = \left\lfloor \frac{c_t + \gamma_t}{Q_0} \right\rfloor,$$

where $w \bmod Q_0$ is the remainder of $w$ on division by $Q_0$. The paper writes $k_t$ for the carry. <cite data-source="paper">The value kj is the carry from the processed coefficients into the remaining positions.</cite> Division with remainder gives, at every position,

$$c_t + \gamma_t = \sigma_t + Q_0\,\gamma_{t+1}.$$

The value is kept by the identity, for every $\tau \ge 0$,

$$\sum_{t<\tau} c_t Q_0^t = \sum_{t<\tau} \sigma_t Q_0^t + \gamma_\tau Q_0^\tau,$$

where $\tau$ counts the low positions already processed. The identity says that the processed coefficients equal the processed digits plus the carry $\gamma_\tau$, which is still owed to the higher positions with weight $Q_0^\tau$. It holds at $\tau = 0$, where both sums are empty and $\gamma_0 = 0$. If it holds at $\tau$, add $c_\tau Q_0^\tau$ to both sides. Multiplying the division identity at $\tau$ by $Q_0^\tau$ gives $c_\tau Q_0^\tau + \gamma_\tau Q_0^\tau = \sigma_\tau Q_0^\tau + \gamma_{\tau+1} Q_0^{\tau+1}$, so the right side becomes $\sum_{t<\tau+1} \sigma_t Q_0^t + \gamma_{\tau+1} Q_0^{\tau+1}$, which is the identity at $\tau+1$.

The recurrence reads $c_t$ only after $\gamma_t$ is known, and $\gamma_t$ depends on all lower coefficients, so the positions must be processed from $t = 0$ upward. The paper gives the same order, to <cite data-source="paper">Propagate radix-2b carries in increasing coefficient order</cite>, and <cite data-source="paper">so this carry scan proceeds from least to most significant</cite>.

The carries stay small. If $0 \le \gamma_t \le N(Q_0-1)$, then $c_t + \gamma_t \le N(Q_0-1)^2 + N(Q_0-1) = NQ_0(Q_0-1)$, so $\gamma_{t+1} \le N(Q_0-1)$. Since $\gamma_0 = 0$, every carry satisfies $0 \le \gamma_t \le N(Q_0-1) < Q_0^2$, the last step because $N \le Q_0$. So each carry fits in $2b$ bits. <cite data-source="paper">The carries satisfy 0 ≤ kj ≤ q(Q0 − 1) < Q20</cite>. <cite data-source="paper">Carry storage and work per coefficient are O(b) bits and steps</cite>.

Coefficients vanish past the end. The product of two polynomials of degree $N-1$ has degree at most $2N-2$, so $c_t = 0$ for $t \ge 2N-1$. Then $\gamma_{2N-1} < Q_0^2$ gives $\gamma_{2N} \le Q_0-1$, and $\gamma_{2N+1} = 0$. The leftover carry is written out the same way: <cite data-source="paper">drain the final O(b)-bit carry in the same order</cite>. Its digits are $\sigma_{2N-1}$ and $\sigma_{2N}$, and $\sigma_t = 0$ for $t \ge 2N+1$, since then $c_t + \gamma_t = 0$. Taking $\tau = 2N+1$ in the identity, where every $c_t$ with $t \ge 2N+1$ is zero, gives $\sum_t c_t Q_0^t = \sum_t \sigma_t Q_0^t$. Each $\sigma_t$ lies in $\{0, \dots, Q_0-1\}$, so it is a $b$-bit block. Writing $\sigma_{2N}, \dots, \sigma_0$ from the top, each in $b$ bits, gives a binary string whose value is the product.

For $Q_0 = 4$ (so $b = 2$) and three coefficients $(c_0, c_1, c_2) = (5, 3, 7)$:

- $t=0$: $c_0 + \gamma_0 = 5$, so $\sigma_0 = 1$ and $\gamma_1 = 1$.
- $t=1$: $c_1 + \gamma_1 = 4$, so $\sigma_1 = 0$ and $\gamma_2 = 1$.
- $t=2$: $c_2 + \gamma_2 = 8$, so $\sigma_2 = 0$ and $\gamma_3 = 2$.
- $t=3$: $c_3 = 0$ and $\gamma_3 = 2 < 4$, so $\sigma_3 = 2$ and $\gamma_4 = 0$.

The digits $(\sigma_3, \sigma_2, \sigma_1, \sigma_0) = (2, 0, 0, 1)$ give $2 \cdot 4^3 + 0 \cdot 4^2 + 0 \cdot 4 + 1 = 129 = 5 + 3 \cdot 4 + 7 \cdot 16$. In binary, each digit takes two bits: $10\,00\,00\,01$.
