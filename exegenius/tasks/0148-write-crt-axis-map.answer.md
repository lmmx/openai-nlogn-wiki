The Chinese-remainder axis map is a bijection that places the coefficients of a [Cyclic convolution](cyclic-convolution.md) on the axes of a product of cyclic rings, so that the convolution becomes multidimensional.

Let $d$ be the number of axes, with $i$ and $j$ running from $1$ to $d$ as axis indices (not list positions), and let $s_i$ be the length of axis $i$, with $s_1,\ldots,s_d$ pairwise coprime. Let $S=s_1\cdots s_d$ be the number of coefficients, and let $x$ be the variable of $\mathbb C[x]/(x^S-1)$.

Let $P_i=s_1\cdots s_{i-1}$, so $P_1=1$. Since $P_i$ is coprime to $s_i$, it has an inverse $\mu_i$ modulo $s_i$, so $\mu_iP_i\equiv1\pmod{s_i}$. Let $x_i$ be the variable of axis $i$, and let $\mathcal R=\mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1)$ be the target ring.

Let $\Phi$ be the algebra map (respecting sums, products and scalars) with $\Phi(x)=\prod_i x_i^{\mu_i}$ that maps $\mathbb C[x]/(x^S-1)$ into the [Quotient ring by several relations](quotient-ring.md) $\mathcal R$.

A map sending $x$ to an element $g$ of a ring kills $x^S-1$, and so descends to the quotient, exactly when $g^S=1$. Here $\Phi(x)^S=\prod_i x_i^{\mu_iS}=1$, because each $s_i$ divides $S$.

For a coefficient index $k$ with $0\le k<S$ (the position of a coefficient in the list), $\Phi(x^k)=\prod_i x_i^{\mu_ik}$ is a monomial whose exponent on $x_i$ is $b_i$, where $0\le b_i<s_i$ and $b_i\equiv\mu_ik\pmod{s_i}$. The monomials $x_1^{e_1}\cdots x_d^{e_d}$ with $0\le e_i<s_i$ are a basis of $\mathcal R$, and there are $S$ of them. If $k$ and $k'$ (another index with $0\le k'<S$) give the same $b_i$ for every $i$, then each $s_i$ divides $k-k'$. The Chinese remainder theorem says that congruences with pairwise coprime moduli combine into one modulo their product, so $S\mid k-k'$ and $k=k'$. Thus the $S$ powers $\Phi(x)^0,\ldots,\Phi(x)^{S-1}$ reach $S$ distinct basis monomials, which are all of them. So $\Phi$ is a bijective algebra map, an isomorphism.

Because $\Phi$ is an isomorphism, it preserves [Cyclic convolution](cyclic-convolution.md): products of lists map to products of images. In $\mathcal R$, multiplying monomials adds exponents on each axis modulo $s_i$, so the convolution becomes a $d$-dimensional cyclic convolution.

Each $k$ has a unique expansion $k=\sum_{j=1}^d a_jP_j$ with $0\le a_j<s_j$. Here $a_j$ is the digit of $k$ on axis $j$, and $a_i$ means the same with $i$ in place of $j$. Then
$$b_i\equiv a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i},$$
since $\mu_ik=\sum_j\mu_ia_jP_j$, the terms with $j>i$ are multiples of $s_i$, and $\mu_iP_i\equiv1$.

So for fixed earlier digits, $a_i\mapsto b_i$ is a cyclic shift of axis $i$ by an amount that depends only on axes $j<i$. The shifts must run from axis $d$ down to axis $1$. A shift of axis $i$ reads the digits $a_j$ with $j<i$, which stay unchanged until their own shift. Shifting axis $1$ first would change $a_1$ before the shift on axis $2$ reads it. The result moves the coefficient at $(a_1,\ldots,a_d)$ to position $(b_1,\ldots,b_d)$.

Take $S=6$, $s_1=2$, $s_2=3$. Then $\mu_1=1$, $\mu_2=2$, and $\Phi(x)=x_1x_2^2$. For $k=3=1\cdot1+1\cdot2$, the digits are $a_1=1$, $a_2=1$, giving $b_1=1$ and $b_2\equiv1+2\cdot1\equiv0\pmod 3$. Directly, $(x_1x_2^2)^3=x_1^3x_2^6=x_1$ in $\mathcal R$.

This is the Chinese-remainder split used by <cite data-source="paper">Agarwal and Cooley used the Chinese remainder</cite>.
