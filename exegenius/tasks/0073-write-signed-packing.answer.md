Signed coefficient packing encodes a polynomial with signed integer coefficients as one integer, so that a polynomial product becomes an integer product. It is a form of Kronecker substitution <cite data-source="paper">Signed coefficient packing is a form of Kronecker substitution</cite>, which lets the polynomial products of the transform method run on an integer multiplier.

Let $A$ be a polynomial in a formal variable $x$, and let $m$ be its number of coefficients. Write $A(x)=\sum_{i=0}^{m-1} a_i x^i$, where $i$ indexes the coefficients and $a_i$ is the integer coefficient of $x^i$. Each slot has width $b$, the number of bits it holds, and each $|a_i|<2^{b-1}$. The letters $a$, $b$ and $m$ take these meanings only on this page.

The packed integer of $A$ is $N_A=A(2^b)$, the sum below with coefficient $a_i$ at bit offset $bi$:

$$N_A=\sum_{i=0}^{m-1} a_i\,2^{bi}.$$

Because a negative $a_i$ borrows from the slot above, the binary digits of $N_A$ do not show the signs. Decoding reads each slot as the integer in $[-2^{b-1},2^{b-1})$ congruent to the remaining value modulo $2^b$, subtracts it, and divides by $2^b$.

For a second polynomial $B$ with packed integer $N_B$, evaluating at $2^b$ turns products into products, so $N_A N_B=(AB)(2^b)$ for every $b$. Decoding $N_A N_B$ recovers $AB$ when every coefficient of $AB$ also lies in $[-2^{b-1},2^{b-1})$.

The size is the step to check. Each of $N_A$ and $N_B$ has about $mb$ bits, since each is a sum of $m$ slots of $b$ bits. The packed form of $AB$ has $2m-1$ slots, so about $2mb$ bits. The product of two $mb$-bit integers has about $2mb$ bits, enough for every slot of $AB$. So one integer product of the operands computes the whole polynomial product. The integer product $N_A N_B$ is computed by the [Established fast multiplier](multiplier-subroutine.md), used as a subroutine.

For example, take $m=3$ and $b=4$, with $A(x)=1-2x+3x^2$ and $B(x)=2+x$. Then $N_A=737$, $N_B=18$, and $N_AN_B=13266$. The product $AB=2-3x+4x^2+3x^3$ has coefficients in $[-8,8)$, and $2-3\cdot 16+4\cdot 256+3\cdot 4096=13266$, so the integer product is the packed form of $AB$.
