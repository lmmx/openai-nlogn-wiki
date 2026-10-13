The Chinese-remainder axis map is a bijection that places the coefficients of a [cyclic convolution](cyclic-convolution.md) on the axes of a product of cyclic rings, so that the convolution becomes multidimensional. The radix-digit coefficient list is laid out this way, with each axis of distinct prime length.

Let $d$ be the number of axes. Let $s_i$ be the length of axis $i$, a count of positions on that axis, and assume $s_1,\ldots,s_d$ are pairwise coprime. Let $S=s_1s_2\cdots s_d$ be the total number of coefficients. Let $x$ be the variable of the ring $\mathbb C[x]/(x^S-1)$.

Let $P_i=s_1\cdots s_{i-1}$ be the product of the lengths before axis $i$, with $P_1=1$. Let $\mu_i$ be the inverse of $P_i$ modulo $s_i$, so that $\mu_iP_i\equiv1\pmod{s_i}$; it exists because $P_i$ is coprime to $s_i$.

Let $\Phi$ be the algebra map sending $x$ to $\prod_i x_i^{\mu_i}$. It maps $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1)$. Since each $\mu_i$ is a unit modulo $s_i$, the Chinese remainder theorem makes the exponents of $\Phi(x)^0,\ldots,\Phi(x)^{S-1}$ pairwise distinct, so these powers run through all $S$ target monomials once. Hence $\Phi$ is an isomorphism. The map $\Phi$ is an isomorphism that preserves [cyclic convolution](cyclic-convolution.md), so a product of two lists is computed axis by axis.

Let $k$ be a coefficient index with $0\le k<S$. It has a unique mixed-radix expansion $k=\sum_{j=1}^d a_jP_j$ with $0\le a_j<s_j$, and $a_j$ is the mixed-radix digit of $k$ on axis $j$. Let $b_i$ be the exponent of $x_i$ in $\Phi(x^k)$, reduced so that $0\le b_i<s_i$. Then $b_i\equiv a_i+\mu_i\sum_{j<i}a_jP_j \pmod{s_i}$. This follows from $\mu_ik=\sum_j\mu_ia_jP_j$: terms with $j>i$ are multiples of $s_i$, and $\mu_iP_i\equiv1\pmod{s_i}$.

Take $S=6$, $s_1=2$, $s_2=3$. Then $P_1=1$, $P_2=2$, $\mu_1=1$, $\mu_2=2$, so $\Phi(x)=x_1x_2^2$. For $k=3=1+1\cdot2$, the digits are $a_1=1$ and $a_2=1$, giving $b_1=1$ and $b_2\equiv1+2\cdot1\equiv0\pmod 3$. Directly, $(x_1x_2^2)^3=x_1^3x_2^6=x_1$ in the target ring.

This is the Chinese-remainder split of Agarwal and Cooley <cite data-source="paper">Agarwal and Cooley used the Chinese remainder</cite>. Its point is that reordering the coefficients becomes a sequence of controlled cyclic shifts on the axes.
