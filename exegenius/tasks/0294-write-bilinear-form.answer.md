A bilinear form decides when two vectors are orthogonal. The [subspace labels](subspace-labels.md) of the networks that follow are subspaces of one fixed bilinear space: <cite data-source="paper">A label is a nondegenerate subspace of a fixed bilinear</cite> space.

Let $E$ be a vector space over the field $F$ of scalars. The letters $\xi$ and $\eta$ denote vectors of $E$ here, not the ring elements of earlier pages. A bilinear form on $E$ is a special case of a [bilinear map](bilinear-map.md): it takes two vectors $\xi$ and $\eta$ of $E$ and returns the scalar $\langle \xi,\eta\rangle$ in $F$, linear in each argument when the other is fixed. A vector space with such a form is a *bilinear space*.

Two vectors are *orthogonal* when $\langle \xi,\eta\rangle=0$. Let $U$ be a subspace of $E$. Its orthogonal complement $U^\perp$ is the set of vectors $\xi$ in $E$ with $\langle \xi,\eta\rangle=0$ for every $\eta$ in $U$. The form is *nondegenerate* when $E^\perp=\{0\}$: $0$ is the only vector orthogonal to all of $E$.

For example, let $E=\mathbb{Q}^2$, and write $\xi_1$ and $\xi_2$ for the first and second coordinates of $\xi$, and $\eta_1$ and $\eta_2$ for those of $\eta$. The form $\langle \xi,\eta\rangle=\xi_1\eta_1+\xi_2\eta_2$ is nondegenerate, since $\langle \xi,(1,0)\rangle=\xi_1$ and $\langle \xi,(0,1)\rangle=\xi_2$ vanish only when $\xi=0$.

Fix a basis $e_1,\dots,e_m$ of $E$, where $m$ is the dimension of $E$, and write $e_i$ for its $i$-th vector. The form is written with the matrices of [linear algebra basics](linear-algebra-basics.md). Here $\xi^{\mathsf T}$ is the transpose of $\xi$, the row of its coordinates. Let $A$ be the $m\times m$ matrix with entries $A_{ij}=\langle e_i,e_j\rangle$, so that $\langle \xi,\eta\rangle=\xi^{\mathsf T}A\eta$.

A vector $\xi$ is orthogonal to every vector exactly when $\xi^{\mathsf T}A\eta=0$ for all $\eta$, which means $A^{\mathsf T}\xi=0$. So the form is nondegenerate exactly when $A^{\mathsf T}\xi=0$ forces $\xi=0$. A square matrix has this property when it is invertible, and $A^{\mathsf T}$ is invertible exactly when $A$ is, so the form is nondegenerate exactly when $A$ is invertible.

The form below is the setting for the paper's [bit network](bit-network.md). <cite data-source="paper">For the bit network, let F = Qh with bilinear form</cite> on $E=\mathbb{Q}^h$, with <cite data-source="paper">h = 100</cite>. Let $J$ be the all-one $h\times h$ matrix. <cite data-source="paper">where J is the all-one matrix.</cite> In the standard basis, $A=I-J/9$.

Since $J=\mathbf 1\mathbf 1^{\mathsf T}$, where $\mathbf 1$ is the column of $h$ ones, $J$ has [eigenvalues](eigenvalue.md) $h$ on $\mathbf 1$ and $0$ on vectors whose coordinates sum to $0$. Hence $A$ has eigenvalues $1-h/9=-91/9$ and $1$, and nondegeneracy is decided by the [eigenvalues](eigenvalue.md) of $A$: neither is zero. <cite data-source="paper">This form has eigenvalues 1 and 1−h/9 = −91/9, so it is nondegenerate.</cite>

For a triple $T$, a three-element subset of $[h]$, let $t_T$ be its [indicator vector](indicator-vector.md). Then $t_T^{\mathsf T}t_T=3$, and $t_T^{\mathsf T}Jt_T=(\mathbf 1^{\mathsf T}t_T)^2=9$, since $\mathbf 1^{\mathsf T}t_T$ counts the ones in $t_T$. So $\langle t_T,t_T\rangle=3-9/9=2$, as the paper records: <cite data-source="paper">⟨tT , tT ⟩ = 2.</cite>

For another triple $T'$, $t_T^{\mathsf T}t_{T'}=|T\cap T'|$, the shared count, and $t_T^{\mathsf T}Jt_{T'}=3\cdot 3=9$. Hence $\langle t_T,t_{T'}\rangle=|T\cap T'|-1$, the paper's <cite data-source="paper">⟨tS , tT ⟩ = |S ∩ T | − 1</cite>.
