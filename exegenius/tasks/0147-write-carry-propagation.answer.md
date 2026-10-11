Carry propagation is the final arithmetic step that turns a list of integer coefficients into the binary digits of their value. It is what gives the output of [Integer multiplication below n log n](main-theorem.md) its exact binary form.

Carry propagation takes its input from [Radix-digit convolution](radix-digit-convolution.md): the output is the list of integer coefficients $c_0, c_1, \dots$ of the product of the two digit polynomials. Let $q = \lceil n/b \rceil$ be the number of digits in each input, as on that page. The radix is $Q_0 = 2^b$, the number of values a digit can take, which is the base in which each digit is written. The index $j$ runs over the positions $0, 1, \dots$ of the coefficient list, so $\sum_j c_j Q_0^j$ is the product.

The $c_j$ are not digits. Each $c_j$ is a sum of at most $q$ products of two digits, each at most $(Q_0-1)^2$, so $0 \le c_j \le q(Q_0-1)^2 < Q_0^3$. <cite data-source="paper">0 ≤ cj ≤ q(2b − 1)2 < 23b</cite> The paper takes $b = \lceil \log_2 n \rceil$ for large $n$ <cite data-source="paper">b = ⌈log2 n⌉,</cite>, so $Q_0 \ge n \ge q$, and then $q(Q_0-1)^2 < qQ_0^2 \le Q_0^3$. 
Carry propagation rewrites the same sum with digits. The digit $d_j$ is the $j$th base-$Q_0$ digit of the output, so $0 \le d_j < Q_0$. The carry $\gamma_j$ is the amount carried into position $j$ from the lower positions. <cite data-source="paper">The value kj is the carry from the processed coefficients into the remaining positions.</cite> Set $\gamma_0 = 0$ and, for $j \ge 0$,

$$d_j = (c_j + \gamma_j) \bmod Q_0, \qquad \gamma_{j+1} = \left\lfloor \frac{c_j + \gamma_j}{Q_0} \right\rfloor,$$

where $w \bmod Q_0$ is the remainder of $w$ on division by $Q_0$, and $\lfloor w \rfloor$ is the largest integer not above $w$. Division with remainder gives, at every position,

$$c_j + \gamma_j = d_j + Q_0\,\gamma_{j+1}.$$

Why this keeps the value: here $h$ is a summation index, the position of an already processed coefficient, running over $0 \le h < j$. For every $j \ge 0$,

$$\sum_{h<j} c_h Q_0^h = \sum_{h<j} d_h Q_0^h + \gamma_j Q_0^j.$$

The identity says that the processed coefficients have the same value as the processed digits plus the carry, which is still owed to the higher positions. It holds at $j=0$, where both sides are $0$. If it holds at $j$, add $c_j Q_0^j$ to the left side, which gives $\sum_{h<j} c_h Q_0^h + c_j Q_0^j$. Substituting $\sum_{h<j} d_h Q_0^h + \gamma_j Q_0^j$ for the first sum, and then multiplying the split relation by $Q_0^j$ to get $c_j Q_0^j + \gamma_j Q_0^j = d_j Q_0^j + \gamma_{j+1} Q_0^{j+1}$, the left side equals $\sum_{h<j+1} d_h Q_0^h + \gamma_{j+1} Q_0^{j+1}$. So the identity holds at $j+1$.

The recurrence reads $c_j$ only after $\gamma_j$ is known, so the positions must be processed from $0$ upward. The carries also stay small. If $0 \le \gamma_j \le q(Q_0-1)$, then $c_j + \gamma_j \le q(Q_0-1)^2 + q(Q_0-1) = qQ_0(Q_0-1)$, so $\gamma_{j+1} \le q(Q_0-1)$. Since $\gamma_0 = 0$, every carry obeys this bound, and fits in $2b$ bits. <cite data-source="paper">Carry storage and work per coefficient are O(b) bits and steps.</cite>

Coefficients vanish past the end. The product of two polynomials of degree $q-1$ has degree at most $2q-2$, so $c_j = 0$ for $j \ge 2q-1$. For such $j$, $\gamma_{j+1} = \lfloor \gamma_j / Q_0 \rfloor$. The carry $\gamma_{2q-1}$ is below $Q_0^2$, so $\gamma_{2q} \le Q_0 - 1$ and $\gamma_{2q+1} = 0$. The leftover carry is written out the same way, one digit at a time: <cite data-source="paper">drain the final O(b)-bit carry in the same order</cite>. Its digits are $d_j = \gamma_j \bmod Q_0$ for $2q-1 \le j \le 2q$, and $d_j = 0$ beyond. Taking $j = 2q+1$ in the identity, with $\gamma_{2q+1} = 0$ and every $c_h = 0$ for $h \ge 2q+1$, gives $\sum_j c_j Q_0^j = \sum_j d_j Q_0^j$. Each $d_j$ is a $b$-bit block, so the product is the binary string formed by writing $d_{2q}, \dots, d_0$ from the top down, each in $b$ bits.

For $Q_0 = 4$ (so $b = 2$) and three coefficients $(c_0, c_1, c_2) = (5, 3, 7)$:

- $j=0$: $c_0 + \gamma_0 = 5$, so $d_0 = 1$ and $\gamma_1 = 1$.
- $j=1$: $c_1 + \gamma_1 = 4$, so $d_1 = 0$ and $\gamma_2 = 1$.
- $j=2$: $c_2 + \gamma_2 = 8$, so $d_2 = 0$ and $\gamma_3 = 2$.
- The leftover carry $\gamma_3 = 2 < 4$ gives $d_3 = 2$ and $\gamma_4 = 0$.

The digits $(d_3, d_2, d_1, d_0) = (2, 0, 0, 1)$ give $2 \cdot 64 + 0 \cdot 16 + 0 \cdot 4 + 1 = 129 = 5 + 3 \cdot 4 + 7 \cdot 16$. Written in binary, each digit takes two bits: $10\,00\,00\,01$.
