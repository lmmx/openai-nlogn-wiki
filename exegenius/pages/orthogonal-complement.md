The orthogonal complement $U^\perp$ of a subspace $U$ (a subset closed under addition and under multiplication by scalars) is defined by a [bilinear form](bilinear-form.md): it is the set of vectors that the form sends to zero against every vector of $U$. The argument relies on it in building the [subset-intersection network](subset-intersection-network.md), a linear network on the three-element subsets of a ground set.

Let $\mathcal V$ be a vector space over $F$ with a bilinear form $\langle\cdot,\cdot\rangle$ on $\mathcal V$. For a subspace $U\subseteq\mathcal V$,

$$U^\perp=\{\zeta\in\mathcal V:\ \langle\xi,\zeta\rangle=0 \text{ for all } \xi\in U\}.$$

$U^\perp$ is itself a subspace: if $\zeta$ and $\zeta'$ lie in $U^\perp$ and $\gamma$ is a scalar, then $\langle\xi,\zeta+\gamma\zeta'\rangle=\langle\xi,\zeta\rangle+\gamma\langle\xi,\zeta'\rangle=0$ for every $\xi\in U$, because the form is linear in its second argument.

The network takes its subspaces from this construction. <cite data-source="paper">A label is a nondegenerate subspace of a fixed bilinear space.</cite> Here nondegenerate means that the only vector of the subspace orthogonal to the whole subspace is zero. Edges of the network join labels, and <cite data-source="paper">On every edge one label will contain the other.</cite> For such an edge, write $U\subseteq\mathcal L$, where $U$ is the smaller label and $\mathcal L$ the larger. The orthogonal residual is <cite data-source="paper">the orthogonal complement of the smaller label inside the larger one</cite>, that is, $\mathcal L\cap U^\perp$: the vectors of $\mathcal L$ orthogonal to every vector of $U$.

Take $\mathcal V=\mathbb{Q}^2$ with $\langle\xi,\zeta\rangle=\xi_1\zeta_1+\xi_2\zeta_2$, and let $U=\{\gamma(1,1):\gamma\in\mathbb{Q}\}$, the [line spanned by a vector](line-spanned-by-vector.md) through $(1,1)$. Since $\langle\gamma(1,1),\zeta\rangle=\gamma(\zeta_1+\zeta_2)$ is zero for every $\gamma$ exactly when $\zeta_1+\zeta_2=0$, a vector $\zeta$ lies in $U^\perp$ exactly then. So $U^\perp=\{\gamma(1,-1):\gamma\in\mathbb{Q}\}$, the line through $(1,-1)$.
