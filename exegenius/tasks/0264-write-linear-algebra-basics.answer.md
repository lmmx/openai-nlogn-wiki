The paper's tape procedures apply invertible linear operators that act on an [array](array.md) of values, so each step can be undone exactly. This page defines the vector spaces, linear maps, matrices and inverses it uses.

Fix a field $F$, a set with addition and multiplication in which every nonzero element has a multiplicative inverse. Examples include the two-element field $\mathbb{F}_2$ of integers modulo 2, with $1+1=0$.

A vector space over $F$ is a set of vectors with an addition and a multiplication by scalars from $F$, satisfying the usual axioms. The letters $x$ and $y$ denote vectors over $F$, and $c$ and $d$ denote scalars in $F$; these letters change meaning from earlier pages. The axioms include $(c+d)x=cx+dx$. The standard example is $F^m$, the $m$-tuples of elements of $F$ with componentwise operations, where $m$ is the number of coordinates in each vector. The $j$-th coordinate of $x$ is $x_j$, where $j$ runs from 1 to $m$.

## Linear maps and matrices

A linear map $T$ between vector spaces over $F$ satisfies $T(x+y)=Tx+Ty$ and $T(cx)=cT(x)$ for all vectors $x,y$ and scalars $c$. A linear map from a vector space to itself is an operator.

An $m\times m$ matrix $A$ with entries in $F$ determines a linear map from $F^m$ to itself, sending $x$ to $Ax$. In the formula $(Ax)_i=\sum_j A_{ij}x_j$, the index $i$ labels a coordinate of $Ax$, and the sum runs over the $m$ coordinates of $x$. The identity matrix $I$ has ones on the diagonal and zeros elsewhere.

A matrix $A$ is invertible when some matrix $B$ satisfies $AB=BA=I$. Over $\mathbb{Q}$ take
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.$$
Here $A$ sends $(x_1,x_2)$ to $(x_1+x_2,\,x_2)$, and $AB=BA=I$, so $B$ is the inverse of $A$. Over $\mathbb{F}_2$, $-1=1$, so $B=A$ and $A^2=I$: the inverse depends on the field.

## Invertible operators and inverses

A linear operator $T$ is invertible when some linear map $S$ satisfies $ST=TS=\mathrm{id}$, where $\mathrm{id}$ sends every vector to itself. Such an $S$ is unique. If $S'$ also satisfies $S'T=TS'=\mathrm{id}$, then $S=S\,\mathrm{id}=S(TS')=(ST)S'=\mathrm{id}\,S'=S'$. The unique such $S$ is the inverse of $T$, written $T^{-1}$.

## Use in the paper

The paper's network is a directed graph, and an edge from vertex $u$ to vertex $v$ is a directed connection between them. Each vertex $v$ carries a frame $D_v$, an invertible linear operator on arrays, and $D_u$ is the frame of vertex $u$ in the same way. <cite data-source="paper">choose an invertible linear operator Dv on the space of arrays indexed by the common address set.</cite> The paper calls $g$ the logical array, the array the computation means, and the stored array is $D_v g$. <cite data-source="paper">the stored array is Dv g when the logical array is g</cite>

An edge from $u$ to $v$ changes the stored array from $D_u g$ to $D_v g$, and the change of representation is the operator $D_vD_u^{-1}$: $D_vD_u^{-1}(D_u g)=D_v g$, since $D_u^{-1}D_u$ is the identity. <cite data-source="paper">the operator Dv Du−1 changes the stored array</cite>

For a matrix $M$, the frame $\Phi_M$ acts on array entries by a shear of their address pairs. Here $H$ and $K$ are binary address chunks, and the shear sends $(H,K)$ to $(H+MK,K)$. Take $M=1$: applying the shear twice gives $(H+K+K,K)=(H,K)$, since $1+1=0$ in $\mathbb{F}_2$, so the shear is its own inverse. <cite data-source="paper">Hence ΦM is an invertible F2 -linear permutation of array entries</cite>, so each such frame has an inverse, as the definition of a frame requires.
