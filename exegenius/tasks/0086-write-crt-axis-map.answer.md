The Chinese-remainder axis map is a bijection that places the coefficients of a [cyclic convolution](cyclic-convolution.md) on the axes of a product of cyclic rings, so that the convolution becomes multidimensional.

Let $d$ be the number of axes and $s_i$ the length of axis $i$, with $s_1,\ldots,s_d$ pairwise coprime. Let $S=s_1\cdots s_d$ be the number of coefficients, and let $x$ be the variable of $\mathbb C[x]/(x^S-1)$.

Let $P_i=s_1\cdots s_{i-1}$, so $P_1=1$. Since $P_i$ is coprime to $s_i$, it has an inverse $\mu_i$ modulo $s_i$, so $\mu_iP_i\equiv1\pmod{s_i}$.

Let $x_i$ be the variable of axis $i$, and let $\Phi$ be the algebra map (a function respecting sums, products and complex scalars) with $\Phi(x)=\prod_i x_i^{\mu_i}$, from $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1)$. Since each $s_i$ divides $S$, $\Phi(x)^S=1$ in the target, so $\Phi$ is well defined.

For $0\le k<S$, let $b_i$ be the exponent of $x_i$ in $\Phi(x^k)$, reduced so that $0\le b_i<s_i$; then $b_i\equiv\mu_ik\pmod{s_i}$. If $k$ and $k'$ give the same $b_i$ for every $i$, each $s_i$ divides $k-k'$. By the Chinese remainder theorem, which says that congruences with pairwise coprime moduli combine into one modulo their product, $S$ divides $k-k'$, so $k=k'$. Hence the powers $\Phi(x)^0,\ldots,\Phi(x)^{S-1}$ reach each of the $S$ target monomials once. So $\Phi$ is an isomorphism: a bijective algebra map whose inverse is also one.

Because $\Phi$ is an isomorphism, it preserves [cyclic convolution](cyclic-convolution.md): the product of two lists in the source maps to the product of their images. In the target, multiplying monomials adds exponents on each axis modulo $s_i$, so the convolution becomes a $d$-dimensional cyclic convolution.

Let $k$ be a coefficient index with $0\le k<S$. Its mixed-radix expansion $k=\sum_{j=1}^d a_jP_j$, with $0\le a_j<s_j$, is unique, and $a_j$ is the digit of $k$ on axis $j$. Then $b_i\equiv a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, because $\mu_ik=\sum_j\mu_ia_jP_j$, terms with $j>i$ are multiples of $s_i$, and $\mu_iP_i\equiv1\pmod{s_i}$.

So for fixed earlier digits, the map sends $a_i$ to $b_i$ by a cyclic shift of axis $i$ by $\mu_i\sum_{j<i}a_jP_j$, an amount controlled by earlier axes. Applying these controlled cyclic shifts from axis $d$ down to axis $1$ reorders the coefficients.

Take $S=6$, $s_1=2$, $s_2=3$. Then $\mu_1=1$, $\mu_2=2$, so $\Phi(x)=x_1x_2^2$. For $k=3=1+1\cdot2$, the digits are $a_1=1$ and $a_2=1$, giving $b_1=1$ and $b_2\equiv0\pmod 3$. Directly, $(x_1x_2^2)^3=x_1$ in the target ring.

This is the Chinese-remainder split of Agarwal and Cooley <cite data-source="paper">Agarwal and Cooley used the Chinese remainder</cite>.
