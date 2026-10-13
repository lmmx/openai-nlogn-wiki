The order of an element $\gamma$ of a multiplicative group is the least positive integer $N$ with $\gamma^N=1$, when such $N$ exists. A multiplicative group is a set with an associative product, an identity $1$ and inverses. The argument uses the order of one element to list all of its powers.

For example, in the nonzero residues modulo $7$ under multiplication, $3$ has order $6$: its powers $3,2,6,4,5,1$ are distinct.

If $\gamma$ has order $N$, the powers $1,\gamma,\dots,\gamma^{N-1}$ are distinct. Indeed, if $\gamma^\alpha=\gamma^\beta$ with $0\le\alpha<\beta<N$, then multiplying by the inverse of $\gamma^\alpha$ gives $\gamma^{\beta-\alpha}=1$ with $0<\beta-\alpha<N$, contradicting the minimality of $N$.

Now let $\nu$ be the number of pairwise coprime lengths $s_1,\dots,s_\nu$ of the source, where $s_\eta$ is the $\eta$-th length, and let $S=\prod_\eta s_\eta$. Let $\mu_\eta$ be the inverse of $\prod_{\zeta<\eta}s_\zeta$ modulo $s_\eta$, so $\mu_\eta$ is coprime to $s_\eta$.

Let $G$ be the set of monomials $y_1^{\theta_1}\cdots y_\nu^{\theta_\nu}$ with $0\le\theta_\eta<s_\eta$ in the ring $\mathbb C[y_1,\dots,y_\nu]/(y_1^{s_1}-1,\dots,y_\nu^{s_\nu}-1)$. Multiplying monomials adds the exponents of each $y_\eta$ modulo $s_\eta$, so $G$ is a multiplicative group with $S$ elements. Put $\gamma=\prod_\eta y_\eta^{\mu_\eta}$.

Let $\rho$ be a positive integer. Then $\gamma^\rho=\prod_\eta y_\eta^{\mu_\eta\rho}$ equals $1$ exactly when $s_\eta\mid\mu_\eta\rho$ for every $\eta$. Since each $\mu_\eta$ is coprime to $s_\eta$, this means $s_\eta\mid\rho$ for every $\eta$, and since the lengths are pairwise coprime, $S\mid\rho$. So $\gamma$ has order $S$ <cite data-source="paper">the image of $x$ has order $S$</cite>.

Hence $\gamma^0,\dots,\gamma^{S-1}$ are $S$ distinct elements of $G$, so they list every monomial of $G$ exactly once.

The order is applied to [Cyclic convolution](cyclic-convolution.md) by sending $x^\rho$ to $\gamma^\rho$ for $0\le\rho<S$. The powers $1,x,\dots,x^{S-1}$ form a basis of $\mathbb C[x]/(x^S-1)$, so this map is a bijection between the two monomial bases.
