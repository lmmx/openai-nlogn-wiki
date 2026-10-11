The orthogonal complement $U^\perp$ of a subspace $U$ (a subset closed under addition and under multiplication by scalars) is defined by a [bilinear form](bilinear-form.md): it is the set of vectors that the form sends to zero against every vector of $U$. The argument relies on it in building the [subset-intersection network](subset-intersection-network.md), a linear network on the three-element subsets of a ground set.

Let $X$ be a vector space over $F$, with a bilinear form $\langle\cdot,\cdot\rangle$ on $X$. For a subspace $U\subseteq X$,

$$U^\perp=\{\eta\in X:\ \langle\xi,\eta\rangle=0 \text{ for all } \xi\in U\}.$$

The set $U^\perp$ is itself a subspace: if $\eta$ and $\eta'$ lie in $U^\perp$ and $c$ is a scalar, then $\langle\xi,\eta+c\eta'\rangle=\langle\xi,\eta\rangle+c\langle\xi,\eta'\rangle=0$ for every $\xi\in U$, because the form is linear in its second argument.

<cite data-source="paper">A label is a nondegenerate subspace of a fixed bilinear space.</cite> Here nondegenerate means that the only vector of the subspace orthogonal to the whole subspace is zero. <cite data-source="paper">On every edge one label will contain the other.</cite> For such an edge, write $U\subseteq W$, where $U$ is the smaller label and $W$ the larger. The orthogonal residual is <cite data-source="paper">the orthogonal complement of the smaller label inside the larger one</cite>, that is, $W\cap U^\perp$: the vectors of $W$ orthogonal to every vector of $U$.

Take $X=\mathbb{Q}^2$ with $\langle\xi,\eta\rangle=\xi_1\eta_1+\xi_2\eta_2$, and let $U=\{c(1,1): c\in\mathbb{Q}\}$, the [line spanned by a vector](line-spanned-by-vector.md) through $(1,1)$. Since $\langle c(1,1),\eta\rangle=c(\eta_1+\eta_2)$ is zero for every $c$ exactly when $\eta_1+\eta_2=0$, a vector $\eta$ lies in $U^\perp$ exactly then. So $U^\perp=\{c(1,-1): c\in\mathbb{Q}\}$, the line through $(1,-1)$.
