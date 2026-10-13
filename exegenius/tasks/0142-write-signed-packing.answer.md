Signed coefficient packing encodes a polynomial with signed integer coefficients as one integer, so that a polynomial product becomes an integer product. This is also called Kronecker substitution <cite data-source="paper">Signed coefficient packing is a form of Kronecker substitution</cite>. Signed coefficient packing turns the polynomial products of the [synthetic polynomial transform](synthetic-transform.md) into integer products, so they run on an integer multiplier.

Let $P(x)=\sum_{i=0}^{M-1}\gamma_i x^i$ be a polynomial in $x$, where $M$ is the number of coefficients of $P$ and $\gamma_i$ is the integer coefficient of $x^i$. Each slot has width $\sigma$, the number of bits it holds, and each $|\gamma_i|<2^{\sigma-1}$.

The packed integer of $P$ is $N_P=P(2^\sigma)=\sum_{i=0}^{M-1}\gamma_i 2^{\sigma i}$, so coefficient $\gamma_i$ sits at bit offset $\sigma i$. Because a negative $\gamma_i$ borrows from the slot above, the binary digits of $N_P$ do not show the signs. Decoding reads each slot as the integer in $[-2^{\sigma-1},2^{\sigma-1})$ congruent to the remaining value modulo $2^\sigma$, subtracts it, and divides by $2^\sigma$.

Let $Q$ be a second polynomial, with packed integer $N_Q=Q(2^\sigma)$. Evaluating at $2^\sigma$ turns products into products, so $N_P N_Q=(PQ)(2^\sigma)$. Decoding $N_P N_Q$ recovers $PQ$ when every coefficient of $PQ$ also lies in $[-2^{\sigma-1},2^{\sigma-1})$.

Each of $N_P$ and $N_Q$ has about $M\sigma$ bits, since each is a sum of $M$ slots of $\sigma$ bits. The packed form of $PQ$ has $2M-1$ slots, so at most $2M\sigma$ bits, and the product of two $M\sigma$-bit integers has at most $2M\sigma$ bits. So one integer product has room for every slot of $PQ$, and one integer product computes the whole polynomial product. The product $N_P N_Q$ is computed by the [established fast multiplier](multiplier-subroutine.md) as an ordinary subroutine call.

For example, take $M=3$ and $\sigma=4$, with $P(x)=1-2x+3x^2$ and $Q(x)=2+x$. Then $N_P=737$, $N_Q=18$ and $N_PN_Q=13266$. The product $PQ=2-3x+4x^2+3x^3$ has coefficients in $[-8,8)$, and $2-3\cdot 16+4\cdot 256+3\cdot 4096=13266$, so the integer product is the packed form of $PQ$.
