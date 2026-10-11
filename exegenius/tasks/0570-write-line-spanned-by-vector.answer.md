A line spanned by a vector is the set of all scalar multiples of one nonzero vector, a one-dimensional subspace. The construction of the [subset-intersection network](subset-intersection-network.md) labels its edges with subspaces, chosen <cite data-source="paper">to make the changes of frame inexpensive</cite>, and its triple labels are lines of this kind.

Let $E$ be a vector space over $F$. Its definition is built from the vector spaces and scalar multiples of [Linear algebra basics](linear-algebra-basics.md). For a nonzero $x \in E$, the line spanned by $x$ is $\operatorname{span}\{x\} = \{cx : c \in F\}$, where $c$ is a scalar.

The line is a subspace: for scalars $c, d$, $cx+dx=(c+d)x$ and $c(dx)=(cd)x$ stay on it. It has dimension one, since $x$ spans it.

Take $F=\mathbb{R}$, $E=\mathbb{R}^2$ and $x=(1,2)$. Then $\operatorname{span}\{x\}=\{(c,2c): c\in\mathbb{R}\}$ is the line through the origin with slope 2. The point $(3,6)=3x$ lies on it, but $(1,3)$ does not: its first coordinate forces $c=1$, and then the second coordinate is $2$, not $3$.

Let $\langle\cdot,\cdot\rangle$ be a [bilinear form](bilinear-form.md) on $E$, linear in each argument. A subspace $U$ is nondegenerate when no nonzero vector of $U$ is orthogonal to every vector of $U$. For a line, nondegeneracy is decided by the [bilinear form](bilinear-form.md) on the single vector $x$. For scalars $c,d$, bilinearity gives $\langle cx,dx\rangle=cd\,\langle x,x\rangle$. So $cx$ is orthogonal to the whole line exactly when $c\langle x,x\rangle=0$, and a nonzero vector of the line has $c\neq0$. The line is nondegenerate exactly when $\langle x,x\rangle\neq0$.

The source paper, *Integer multiplication below $n\log n$*, gives no reason for nondegeneracy. A nondegenerate line $U$ meets only in zero its [orthogonal complement](orthogonal-complement.md) $U^\perp$: a vector in both is in $U$ and orthogonal to all of $U$, so it is zero. The paper needs this when it writes <cite data-source="paper">write PU for the projection onto U along U ⊥</cite> for nondegenerate $U$.

The construction labels the edges of a [linear network](linear-network-frames.md) with nondegenerate subspaces. The network is linear: <cite data-source="paper">A wire carries one scalar.</cite> <cite data-source="paper">A gate is a fixed linear map on a specified set of wires</cite>. <cite data-source="paper">On every edge one label will contain the other</cite>.

For a triple $T$ of the ground set $[h]$, the indicator vector $t_T$ has entry 1 in each of the three positions of $T$ and 0 elsewhere. For a choice $\sigma=(\sigma_1,\sigma_2,\sigma_3)$ of three triples, put $u_\sigma = t_{\sigma_1}\otimes t_{\sigma_2}\otimes t_{\sigma_3}$ and $U_\sigma = \operatorname{span}\{u_\sigma\}$. Each label $U_\sigma$ is spanned by the vector $u_\sigma$, a [tensor product](tensor-product.md) of three indicator vectors. The paper writes this as <cite data-source="paper">ua = ta1 ⊗ ta2 ⊗ ta3</cite>, using $a$ for $\sigma$.

The data banks $X_\sigma$ and $Y_\sigma$ are the two banks of data wires indexed by $\sigma$ that carry the label $U_\sigma$ between stages. <cite data-source="paper">At stage 1 they start at Ua on Xa and zero on Ya</cite>, and <cite data-source="paper">at stage 3 they end at F on Xa and Ua⊥ on Ya</cite>.

The bit network uses the form on $\mathbb{Q}^h$ given by <cite data-source="paper">⟨x, y⟩ = xT (I − J/9)y</cite>, where $J$ is the all-one matrix and $I$ the identity matrix. Each entry of $Jt_T$ is 3. So $t_T^{\mathsf T}Jt_T=9$, while $t_T^{\mathsf T}t_T=3$. Hence $\langle t_T,t_T\rangle = 3-9/9 = 2$, the value the paper reports: <cite data-source="paper">⟨tT , tT ⟩ = 2.</cite>

The form on a tensor power multiplies over the three factors, so $\langle u_\sigma,u_\sigma\rangle = 2^3 = 8 \neq 0$, and each label is nondegenerate. The paper concludes: <cite data-source="paper">Thus every triple line is nondegenerate</cite>.
