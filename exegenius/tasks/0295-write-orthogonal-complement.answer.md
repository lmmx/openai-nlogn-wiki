The orthogonal complement of a subspace $U$ is the set of vectors that a form sends to zero against every vector of $U$. It is the tool the paper uses to split one label into a part that is kept and a part that is removed, and the argument relies on it in the construction of the [subset-intersection network](subset-intersection-network.md), a linear network on the three-element subsets of a ground set that exchanges two banks of values and restores its scratch wires. On an edge where one label contains the other, the residual is <cite data-source="paper">the orthogonal complement of the smaller label inside the larger one</cite>.

The orthogonal complement $U^\perp$ is defined by the [bilinear form](bilinear-form.md) $\langle\cdot,\cdot\rangle$ on $X$. Here a subspace is a subset of $X$ closed under addition and under multiplication by scalars, and $U^\perp$ is the set of all $\eta \in X$ with $\langle \xi,\eta\rangle = 0$ for every $\xi \in U$:

$$U^\perp=\{\eta\in X:\ \langle\xi,\eta\rangle=0 \text{ for all } \xi\in U\}.$$

Each such $\eta$ is orthogonal to $U$. The set $U^\perp$ is itself a subspace, because the condition is linear in $\eta$.

Take $X=\mathbb{Q}^2$ with the form $\langle\xi,\eta\rangle=\xi_1\eta_1+\xi_2\eta_2$, and let $U$ be the [line spanned by a vector](line-spanned-by-vector.md) through $(1,1)$. A vector $\eta=(\eta_1,\eta_2)$ lies in $U^\perp$ exactly when $\langle(1,1),\eta\rangle=\eta_1+\eta_2=0$. So $U^\perp$ consists of the multiples of $(1,-1)$, which is a line. Here $\dim U=1$ and $\dim U^\perp=1$, where the dimension of a subspace is the number of vectors in one of its bases.

When the form is nondegenerate, meaning no nonzero vector is orthogonal to all of $X$, and $X$ is finite-dimensional, the dimension count $\dim U^\perp=\dim X-\dim U$ holds in general. This is standard background. In the example it reads $1=2-1$.
