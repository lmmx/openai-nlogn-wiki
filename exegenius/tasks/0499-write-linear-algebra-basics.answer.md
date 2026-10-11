This page defines the operators that act on an [array](array.md) of values: the paper's tape procedures, which are fixed procedures that a multitape Turing machine runs on its tapes, apply such operators, so each step can be undone exactly.

Fix a field $F$, a set with addition and multiplication in which every nonzero element has a multiplicative inverse. Examples include the two-element field $\mathbb{F}_2$ of integers modulo 2, where $1+1=0$, and the field $\mathbb{Q}$ of rational numbers. Several letters are reused here with new meanings, as defined below.

A vector space over $F$ is a set of vectors with an addition and a multiplication by scalars, satisfying the usual axioms. The letters $x$ and $y$ denote vectors in a vector space. The letters $\gamma$ and $\eta$ denote scalars in $F$. The standard example is $F^m$, the $m$-tuples of elements of $F$ with componentwise operations, where $m$ is the number of coordinates in each vector. The $j$-th coordinate of $x\in F^m$ is $x_j$, where $j$ runs from 1 to $m$.

A linear map $T$ between vector spaces over $F$ satisfies $T(x+y)=Tx+Ty$ and $T(\gamma x)=\gamma Tx$. A linear map from a vector space to itself is an operator. The letter $S$ denotes a linear map as well. The composition $ST$ means $(ST)x=S(Tx)$, and composition is associative: $(ST)S'=S(TS')$, because both send $x$ to $S(T(S'x))$.

An $m\times m$ matrix $A$ with entries in $F$ is a square array of $m$ rows and $m$ columns of elements of $F$, and its entry in row $i$ and column $j$ is $A_{ij}$, where $i$ and $j$ run from 1 to $m$. The letter $B$ denotes another such matrix. The product $AB$ of two such matrices has entry $(AB)_{il}=\sum_{j}A_{ij}B_{jl}$ in row $i$ and column $l$, where $l$ labels a column. The matrix $A$ sends $x$ to $Ax$, where $(Ax)_i=\sum_j A_{ij}x_j$. The identity matrix $I$ has ones on the diagonal and zeros elsewhere.

A matrix $A$ is invertible when some matrix $B$ satisfies $AB=BA=I$. Over $\mathbb{Q}$ take $m=2$ and
$$A=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad B=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.$$
Checking entries, $(AB)_{12}=1\cdot(-1)+1\cdot 1=0$ and $(BA)_{12}=1\cdot 1+(-1)\cdot 1=0$, and the other entries check the same way, so $B$ is the inverse of $A$. Over $\mathbb{F}_2$, $-1=1$, so $B=A$ and $A^2=I$: the inverse depends on the field.

A linear operator $T$ is invertible when some linear map $S$ satisfies $ST=TS=\mathrm{id}$, where $\mathrm{id}$ is the identity map, which sends every vector to itself. Such an $S$ is unique. If $S'$ also satisfies $S'T=TS'=\mathrm{id}$, then $S=S\,\mathrm{id}=S(TS')=(ST)S'=\mathrm{id}\,S'=S'$. The unique such $S$ is the inverse of $T$, written $T^{-1}$.

The paper's network is a [directed graph](directed-graph.md), and the paper assigns invertible operators to vertices of it. The letters $u$ and $v$ denote vertices here. Each vertex $v$ carries a frame $D_v$, an invertible linear operator on arrays. <cite data-source="paper">choose an invertible linear operator Dv on the space of arrays indexed by the common address set.</cite>

The letter $g$ denotes the logical array, the array the computation means. The stored array at $v$ is $D_v g$. <cite data-source="paper">the stored array is Dv g when the logical array is g</cite>

An edge from $u$ to $v$ changes the stored array from $D_u g$ to $D_v g$ by the operator $D_vD_u^{-1}$, since $D_vD_u^{-1}(D_ug)=D_vg$. <cite data-source="paper">the operator Dv Du−1 changes the stored array</cite>

For a matrix $M$ over $\mathbb{F}_2$, the frame $\Phi_M$ acts on array entries by a shear of their address pairs. The letters $H$ and $K$ denote the two bit blocks of an address, each a vector over $\mathbb{F}_2$. The shear sends $(H,K)$ to $(H+MK,K)$, adding $MK$ to the first block. <cite data-source="paper">Hence ΦM is an invertible F2 -linear permutation of array entries</cite>. The reason is short: applying the shear twice adds $MK$ twice, and $MK+MK=0$ over $\mathbb{F}_2$, so $\Phi_M(\Phi_M(H,K))=(H,K)$. Thus $\Phi_M$ is its own inverse, and every such frame has an inverse, as the definition of a frame requires.
