Linear algebra over a field is the theory of vector spaces, linear maps, invertible operators, subspaces and rank, taken over an arbitrary field rather than only the reals. The network uses invertible linear operators to change how each array is stored from one gate to the next, so this page sets out the facts it needs.

Let $F$ be a field, the set of scalars; the reader's cases are the real numbers and the field of two elements $F_2$.

A vector space over $F$ is a set $V$ of vectors with an addition and with multiplication by scalars from $F$, obeying the usual rules, such as $a(u+v)=au+av$. A subspace of $V$ is a subset that contains $0$ and is closed under addition and under multiplication by scalars; it is a vector space in its own right.

Let $T\colon V\to V$ be a linear map of $V$ into itself. It satisfies $T(u+v)=T(u)+T(v)$ and $T(au)=aT(u)$ for vectors $u,v$ and scalars $a$. Its image $T(V)$ is a subspace, and the rank of $T$ is the dimension of this image, the number of vectors in a basis of it. For a matrix, the rank is the largest number of linearly independent columns.

The map $T$ is invertible when some linear map $S\colon V\to V$ satisfies $ST=TS=\mathrm{id}$; then $S$ is the inverse, written $T^{-1}$. On a finite-dimensional space, $T$ is invertible exactly when its rank equals $\dim V$. A composite of invertible maps is invertible, and $(ST)^{-1}=T^{-1}S^{-1}$, so the intermediate factors in a product of invertible maps can cancel against their inverses.

Example: over $F_2$, the map on $F_2^2$ given by the matrix $A=\begin{pmatrix}1&1\\0&1\end{pmatrix}$ has columns $(1,0)$ and $(1,1)$, which are linearly independent. So $A$ has rank $2=\dim F_2^2$ and is invertible. Since $A^2=\begin{pmatrix}1&0\\0&1\end{pmatrix}$ over $F_2$, we have $A^{-1}=A$.
