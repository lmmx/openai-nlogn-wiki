The paper describes its tape procedures with linear algebra: each step applies an invertible linear operator to an array of values, and that operator can be undone exactly. This page defines the vector spaces, linear maps, matrices and inverses that this description uses.

Fix a field $F$, a set with addition and multiplication in which every nonzero element has a multiplicative inverse. Examples are the rational numbers $\mathbb{Q}$, the complex numbers, and the two-element field $\mathbb{F}_2$ of integers modulo 2, whose elements are $0$ and $1$ with $1+1=0$.

A vector space over $F$ is a set of vectors with an addition of vectors and a multiplication of vectors by scalars from $F$, satisfying the usual axioms. Write $x$ and $y$ for vectors and $c$ for a scalar in $F$. The axioms include $c(x+y)=cx+cy$, $(c+d)x=cx+dx$ and $1x=x$. The standard example is $F^m$, the set of $m$-tuples of elements of $F$ with componentwise addition and scalar multiplication, where $m$ is the number of coordinates in each vector.

## Linear maps and matrices

A linear map $T$ from one vector space over $F$ to another satisfies $T(x+y)=Tx+Ty$ and $T(cx)=cT(x)$ for all vectors $x,y$ and scalars $c$. A linear map from a vector space to itself is called an operator.

An $m\times m$ matrix $A$ with entries in $F$ determines a linear map from $F^m$ to itself, sending $x$ to $Ax$, where $(Ax)_i=\sum_j A_{ij}x_j$. Here $I$ is the identity matrix, with ones on the diagonal and zeros elsewhere.

A matrix $A$ is invertible when some matrix $B$ satisfies $AB=BA=I$. For example, over $\mathbb{Q}$ take
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.$$
$A$ sends $(x_1,x_2)$ to $(x_1+x_2,\,x_2)$, and $AB=BA=I$, so $A$ is invertible with inverse $B$. Over $\mathbb{F}_2$ we have $-1=1$, so the same $A$ satisfies $B=A$ and $A^2=I$. Whether a matrix is invertible depends on the field.

## Invertible operators and inverses

A linear operator $T$ is invertible when some linear map $S$ satisfies $ST=TS=\mathrm{id}$, where $\mathrm{id}$ sends every vector to itself. Such an $S$ is unique and is called the inverse of $T$, written $T^{-1}$. If $T$ is invertible, applying $T$ and then $T^{-1}$ returns every vector to where it started, so no information is lost.

## Use in the paper

In the paper, each vertex $v$ of the network carries a frame $D_v$, an invertible linear operator on arrays. <cite data-source="paper">choose an invertible linear operator Dv on the space of arrays indexed by the common address set.</cite> When the logical array is $g$, the stored array is $D_v g$, and on an edge from $u$ to $v$ the change of representation is the composite operator $D_vD_u^{-1}$. <cite data-source="paper">the operator Dv Du−1 changes the stored array</cite>

Frames can also come from matrices. For a matrix $M$, the frame $\Phi_M$ acts on array entries by a shear of their address pairs. <cite data-source="paper">Hence ΦM is an invertible F2 -linear permutation of array entries</cite>, so each such frame has an inverse, as the definition of a frame requires. The network built from these frames is the subject of [Linear networks and frames](linear-network-frames.md).
