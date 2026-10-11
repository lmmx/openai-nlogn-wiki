An eigenvalue is a scalar at which a linear operator stretches some nonzero vector without turning it. The paper uses eigenvalues once, to check that a bilinear form is nondegenerate, because its labels must be nondegenerate subspaces of that form.

An eigenvalue is defined in the language of [Linear algebra basics](linear-algebra-basics.md). Here $U$ is a vector space and $T$ a linear operator on $U$. A scalar $\lambda$ is an eigenvalue of $T$ when $Tv=\lambda v$ for some nonzero vector $v$ in $U$, and $v$ is then an eigenvector. These letters take these meanings on this page only: $\lambda$ and $v$ have other meanings on earlier pages.

Here $\mathbb{Q}^m$ is the set of vectors with $m\ge2$ rational entries. A bilinear form $\langle x,y\rangle$ on $\mathbb{Q}^m$ is linear in each argument. Vectors $x,y$ are orthogonal when $\langle x,y\rangle=0$, and the form is nondegenerate when no nonzero $x$ is orthogonal to every $y$.

Eigenvalues test the nondegeneracy of a [symmetric matrix](symmetric-matrix.md) $A$. Take $\langle x,y\rangle=x^{\mathsf T}Ay$ with $A^{\mathsf T}=A$. Then $\langle x,y\rangle=(Ax)^{\mathsf T}y$. If $Ax=0$ for some $x\ne0$, then $x$ is orthogonal to every $y$. Conversely, if $x$ is orthogonal to every $y$, take $y=Ax$: then $\sum_j (Ax)_j^2=0$, so $Ax=0$, because a sum of rational squares is zero only when every term is. So the form is degenerate exactly when $0$ is an eigenvalue of $A$.

Write $\mathbf 1$ for the all-ones vector, so the all-one matrix $J$ is $\mathbf 1\mathbf 1^{\mathsf T}$. For the bit network, the paper's form is <cite data-source="paper">⟨x, y⟩ = xT (I − J/9)y</cite>, <cite data-source="paper">where J is the all-one matrix</cite>. The paper's coordinate count $h$ is $m$ here, and $A=I-\tfrac19\mathbf 1\mathbf 1^{\mathsf T}$, which is symmetric.

Every $x\in\mathbb{Q}^m$ splits as $x=\gamma\mathbf 1+x_0$, where $\gamma$ is the average entry of $x$ and $x_0$ has entries summing to zero. The sum of the entries of $x$ is $m\gamma$, so $\mathbf 1\mathbf 1^{\mathsf T}x=m\gamma\mathbf 1$ and $Ax=\gamma\left(1-\tfrac m9\right)\mathbf 1+x_0$.

Comparing parts of $Ax=\lambda x$ gives $\gamma\left(1-\tfrac m9\right)=\lambda\gamma$ and $x_0=\lambda x_0$. So $\lambda=1-\tfrac m9$ when $\gamma\ne0$, and $\lambda=1$ when $x_0\ne0$. The vector $\mathbf 1$ has eigenvalue $1-\tfrac m9$. For $m\ge2$, the vector $(1,-1,0,\dots,0)$ has $\gamma=0$ and eigenvalue $1$. So the eigenvalues are exactly $1$ and $1-\tfrac m9$.

For the paper's $h=100$, so $m=100$, the eigenvalues are $1$ and $-\tfrac{91}{9}$. Both are nonzero, so $0$ is not an eigenvalue and the form is nondegenerate. The paper states this: <cite data-source="paper">This form has eigenvalues 1 and 1−h/9 = −91/9, so it is nondegenerate.</cite>
