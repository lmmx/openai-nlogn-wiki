Carry propagation is the final arithmetic step that turns integer coefficients into the exact binary product, so it is what gives the output of [Integer multiplication below n log n](main-theorem.md) its value.

Carry propagation takes its input from [Radix-digit convolution](radix-digit-convolution.md): the output is the list of integer coefficients $c_0, c_1, \dots$ of the product of the two digit polynomials.

Let $n$ be the bit length of each input. Let $b$ be the number of bits in one radix digit, and let $q = \lceil n/b \rceil$ be the number of digits in each input. The radix is $Q_0 = 2^b$, the base in which each digit is written. Each input is then a polynomial in $Q_0$ with $q$ digit coefficients. The index $j$ runs over the positions of the coefficient list, from $0$ upward. The integer coefficient $c_j$ is the coefficient of $Q_0^j$ in the product of the two digit polynomials. Each product coefficient obeys $0 \le c_j \le q(Q_0-1)^2 < Q_0^3$ <cite data-source="paper">Every product coefficient obeys</cite>.

The digit $d_j$ is the $j$th base-$Q_0$ digit of the output, so $0 \le d_j < Q_0$. The sum $\sum_j c_j Q_0^j$ is the product, but the $c_j$ are not digits, because they can exceed $Q_0 - 1$. Carry propagation rewrites the same sum with digits $d_j$. The carry $k_j$ is the amount carried into position $j$ from the lower positions. These are defined by

$$k_0 = 0, \qquad d_j = (c_j + k_j) \bmod Q_0, \qquad k_{j+1} = \left\lfloor \frac{c_j + k_j}{Q_0} \right\rfloor,$$

where $x \bmod Q_0$ is the remainder of $x$ on division by $Q_0$, and $\lfloor x \rfloor$ is the largest integer not above $x$. At each position, the number $c_j + k_j$ is split into its remainder $d_j$, which stays at position $j$, and its quotient $k_{j+1}$, which moves to position $j+1$. Hence

$$c_j + k_j = d_j + Q_0 k_{j+1}.$$

Summing this relation over the positions shows what the carries do. For every $j$,

$$\sum_{h<j} c_h Q_0^h = \sum_{h<j} d_h Q_0^h + k_j Q_0^j.$$

This holds at $j = 0$, where both sides are $0$ because $k_0 = 0$. If it holds at $j$, add $c_j Q_0^j$ to the left side and $d_j Q_0^j + k_{j+1} Q_0^{j+1}$ to the right side. Multiplying the split relation by $Q_0^j$ gives $c_j Q_0^j + k_j Q_0^j = d_j Q_0^j + k_{j+1} Q_0^{j+1}$, so the identity holds at $j+1$. The carry $k_j$ is therefore exactly the value that the lower positions pass upward: <cite data-source="paper">The value kj is the carry from the processed coefficients into the remaining positions.</cite>

Once all coefficients are processed, the leftover carry is written out the same way, one digit at a time, until it is zero: <cite data-source="paper">drain the final O(b)-bit carry in the same order</cite>. Taking $j$ past the last coefficient, where every $c_h$ and the remaining carry are zero, the identity gives $\sum_j c_j Q_0^j = \sum_j d_j Q_0^j$. Each $d_j$ is a block of $b$ bits, and the digits are base-$Q_0$ digits, so the digit string written from the top digit down is the binary representation of the product.

The recurrence reads $c_j$ only after $k_j$ is known, so the positions must be processed from least significant to most significant. The carries also stay small. If $0 \le k_j \le q(Q_0-1)$, then $c_j + k_j \le q(Q_0-1)^2 + q(Q_0-1) = qQ_0(Q_0-1)$, so $k_{j+1} \le q(Q_0-1)$ as well. <cite data-source="paper">Carry storage and work per coefficient are O(b) bits and steps.</cite>

For $Q_0 = 4$ (so $b = 2$) and coefficients $(c_0, c_1, c_2) = (5, 3, 7)$:

- $j=0$: $c_0 + k_0 = 5$, so $d_0 = 1$ and $k_1 = 1$.
- $j=1$: $c_1 + k_1 = 4$, so $d_1 = 0$ and $k_2 = 1$.
- $j=2$: $c_2 + k_2 = 8$, so $d_2 = 0$ and $k_3 = 2$.
- The leftover carry $2 < 4$ becomes $d_3 = 2$, with $k_4 = 0$.

The digits $(d_3, d_2, d_1, d_0) = (2, 0, 0, 1)$ give $2 \cdot 64 + 0 \cdot 16 + 0 \cdot 4 + 1 = 129$, which equals $5 + 3 \cdot 4 + 7 \cdot 16 = 129$. Written in binary, each digit takes two bits: $10\,00\,00\,01$.
