An eigenvalue is a scalar for which a linear operator maps some nonzero vector to a multiple of itself. The sources use eigenvalues once, to check that a bilinear form is nondegenerate.

An eigenvalue is defined in the language of [Linear algebra basics](linear-algebra-basics.md). Here $V$, $\theta$ and $e$ denote a vector space, an eigenvalue and an eigenvector, whatever they denote elsewhere. A linear operator $T$ on $V$ has eigenvalue $\theta$ when $Te=\theta e$ for some nonzero $e$ in $V$.

Here $\mathbb{Q}$ denotes the rational numbers, $\mathbb{Q}^h$ the vectors with $h$ rational entries, and $h\ge 2$ their number of coordinates. A bilinear form on $\mathbb{Q}^h$ assigns to vectors $x,y$ a number $\langle x,y\rangle$, linear in each argument. It is nondegenerate when no nonzero $x$ is orthogonal to every $y$, where $x,y$ are orthogonal when $\langle x,y\rangle=0$.

Here $x^{\mathsf T}$ is the row with the entries of $x$. Eigenvalues test the nondegeneracy of a [symmetric matrix](symmetric-matrix.md) $A$. With $A^{\mathsf T}=A$, the form $\langle x,y\rangle = x^{\mathsf T}Ay$ is nondegenerate exactly when $0$ is not an eigenvalue of $A$, viewed as the operator $x\mapsto Ax$.

Since $A$ is symmetric, $\langle x,y\rangle=(Ax)^{\mathsf T}y$. If $Ax=0$ for some $x\ne0$, then $x$ is orthogonal to every $y$. Conversely, if $x$ is orthogonal to every $y$, take $y=Ax$: then $\sum_j (Ax)_j^2=0$, so $Ax=0$. So the form is degenerate exactly when $0$ is an eigenvalue.

Let $J$ be the $h\times h$ matrix with every entry $1$. The paper's form has $A=I-J/9$. <cite data-source="paper">For the bit network, let F = Qh with bilinear form</cite> $\langle x,y\rangle = x^{\mathsf T}(I - J/9)y$, <cite data-source="paper">where J is the all-one matrix</cite>. $A$ is symmetric, as $J$ is.

Let $\mathbf 1$ be the all-ones vector. Every $x$ in $\mathbb{Q}^h$ splits uniquely as $x=c\mathbf 1+x_0$, with $c$ the average entry of $x$ and $x_0$ summing to zero. Each entry of $Jx$ is the sum of the entries of $x$, so $Ax=c(1-h/9)\mathbf 1+x_0$.

Comparing parts of $Ax=\theta x$ with $x\ne0$ gives $c(1-h/9)=\theta c$ and $x_0=\theta x_0$. So $\theta=1-h/9$ with $c\ne0$, or $\theta=1$ with $x_0\ne0$. $\mathbf 1$ has eigenvalue $1-h/9$, and for $h\ge2$ the vector $(1,-1,0,\dots,0)$ has eigenvalue $1$. So the eigenvalues are exactly $1$ and $1-h/9$.

For $h=100$, both eigenvalues are nonzero, so the form is nondegenerate: <cite data-source="paper">This form has eigenvalues 1 and 1−h/9 = −91/9, so it is nondegenerate.</cite>
