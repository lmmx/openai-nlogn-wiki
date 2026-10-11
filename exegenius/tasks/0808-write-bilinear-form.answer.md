A bilinear form is the pairing that decides when two vectors are orthogonal. It is the setting of the [subspace labels](subspace-labels.md) of the networks below, which are nondegenerate subspaces of one fixed form: <cite data-source="paper">A label is a nondegenerate subspace of a fixed bilinear space</cite>.

Let $E$ be a vector space over the field $F$ of scalars. A bilinear form on $E$ is a special case of a [bilinear map](bilinear-map.md) whose two arguments both come from $E$. It assigns to vectors $x$ and $y$ of $E$ a scalar $\langle x,y\rangle$ in $F$, and it is linear in $x$ when $y$ is fixed and linear in $y$ when $x$ is fixed. Vectors $x$ and $y$ are *orthogonal* when $\langle x,y\rangle=0$.

A *subspace* $\mathcal S$ of $E$ is a subset closed under addition and scalar multiplication. Its *orthogonal complement* $\mathcal S^\perp$ is the set of vectors $x$ in $E$ with $\langle x,y\rangle=0$ for every $y$ in $\mathcal S$. The form is *nondegenerate* when $E^\perp=\{0\}$, so that $0$ is the only vector orthogonal to all of $E$.

Fix a basis $e_1,\dots,e_m$ of $E$, where $m$ is the dimension of $E$ and $e_j$ is the $j$-th basis vector; the letter $e$ here does not name an eigenvector. In coordinates, a bilinear form is written with the matrices of [linear algebra basics](linear-algebra-basics.md). Let $\mathcal M$ be the $m\times m$ matrix with entries $\mathcal M_{ij}=\langle e_i,e_j\rangle$. The transpose $x^{\top}$ of a column $x$ is the row with the same entries. Writing vectors as columns, linearity in each argument gives $\langle x,y\rangle=x^{\top}\mathcal M y=(\mathcal M^{\top}x)^{\top}y$.

So $x$ is orthogonal to all of $E$ exactly when $\mathcal M^{\top}x=0$. The form is nondegenerate exactly when $\mathcal M^{\top}x=0$ forces $x=0$, that is, when $\mathcal M^{\top}$ is invertible. Nondegeneracy is tested through the [eigenvalues](eigenvalue.md) of $\mathcal M$, since the determinant is their product and so $\mathcal M$ is invertible exactly when none of them is zero.

The example form below supplies the label space of the paper's [bit network](bit-network.md). There the space is $E=\mathbb{Q}^h$, which the paper writes as $F$: <cite data-source="paper">For the bit network, let F = Qh with bilinear form</cite>. The paper sets <cite data-source="paper">h = 100</cite>, and the rule is
$$\langle x,y\rangle=x^{\top}(I-J/9)\,y,$$
<cite data-source="paper">where J is the all-one matrix.</cite> Here $J$ has every entry $1$, so $\mathcal M=I-J/9$.

Let $\mathbf 1$ be the all-ones column of $h$ entries. Each row of $J$ sums to $h$, so $J\mathbf 1=h\mathbf 1$. If the entries of $x$ sum to $0$, then $Jx=\mathbf 1(\mathbf 1^{\top}x)=0$, so $\mathcal Mx=x$. These vectors together with $\mathbf 1$ span $\mathbb Q^h$, and $\mathcal M\mathbf 1=(1-h/9)\mathbf 1$. So $\mathcal M$ has eigenvalues $1$ and $1-h/9$, which is $-91/9$ when $h=100$. Neither is zero, so the form is nondegenerate: <cite data-source="paper">This form has eigenvalues 1 and 1−h/9 = −91/9, so it is nondegenerate.</cite>

For a three-element subset $\sigma$ of $[h]=\{1,\dots,h\}$, its *indicator vector* $\mathbf 1_\sigma$ has entry $1$ at each element of $\sigma$ and $0$ elsewhere. Then $\mathbf 1^{\top}\mathbf 1_\sigma=3$, and $\mathbf 1_\sigma^{\top}\mathbf 1_{\sigma'}=|\sigma\cap\sigma'|$ counts the common elements. Since $J=\mathbf 1\mathbf 1^{\top}$, the form equals $x^{\top}y-\tfrac19(\mathbf 1^{\top}x)(\mathbf 1^{\top}y)$, so
$$\langle \mathbf 1_\sigma,\mathbf 1_{\sigma'}\rangle=|\sigma\cap\sigma'|-\tfrac{3\cdot 3}{9}=|\sigma\cap\sigma'|-1.$$
For $\sigma'=\sigma$ this is $3-1=2$, as the paper records: <cite data-source="paper">⟨tT , tT ⟩ = 2.</cite>
