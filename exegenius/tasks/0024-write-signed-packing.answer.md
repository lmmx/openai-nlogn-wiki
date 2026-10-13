Signed coefficient packing is the encoding that turns a polynomial with signed integer coefficients into one integer, so that a polynomial product becomes an integer product. It is a form of Kronecker substitution <cite data-source="paper">Signed coefficient packing is a form of Kronecker substitution</cite>, and it lets the polynomial products of the transform method run on an integer multiplier.

Let $A(x)=\sum_{i=0}^{m-1} a_i x^i$ be the polynomial whose integer coefficient of $x^i$ is $a_i$, where $x$ is a formal variable, $m$ is the number of coefficients, and $b$ is the width in bits of each slot. Each coefficient satisfies $|a_i|<2^{b-1}$.

The packed integer of $A$ is $N_A=A(2^b)$, the sum below with coefficient $a_i$ at bit offset $bi$:

$$N_A=\sum_{i=0}^{m-1} a_i\,2^{bi}.$$

Because the coefficients are signed, the binary digits of $N_A$ do not show them directly, since a negative $a_i$ borrows from the slot above. Decoding reads each slot as the integer in $[-2^{b-1},2^{b-1})$ congruent to the remaining value modulo $2^b$, subtracts it, and divides by $2^b$ to move to the next slot.

For a second polynomial $B$ with packed integer $N_B$, the identity $N_A N_B=(AB)(2^b)$ holds for every $b$. The integer product $N_A N_B$ is the packed form of $AB$ when every coefficient of $AB$ also lies in $[-2^{b-1},2^{b-1})$. The integer product is then formed by the [Established fast multiplier](multiplier-subroutine.md), used as a subroutine. Its size is about $mb$ bits, so one integer product of that size computes the whole polynomial product.

For example, take $m=3$ and $b=4$, with $A(x)=1-2x+3x^2$ and $B(x)=2+x$. Then $N_A=737$, $N_B=18$, and $N_AN_B=13266$. The product is $AB=2-3x+4x^2+3x^3$, whose coefficients lie in $[-8,8)$, and $2-3\cdot 16+4\cdot 256+3\cdot 4096=13266$, so the integer product is the packed form of $AB$.
