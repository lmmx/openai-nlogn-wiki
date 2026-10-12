Lower-triangular factorization writes a rational matrix as a product of two invertible lower-triangular matrices and a partial permutation matrix. It is used for the [Address shear](address-shear.md), which is performed with as many pairwise interchanges as the rank of the matrix.

Let $A$ be a rational $m\times m$ matrix, where $m$ is the number of rows of $A$. Rational means every entry is a rational number.

The factorization is $A=E_1\Pi E_2$, where $E_1$ and $E_2$ are invertible lower-triangular matrices, with zeros above the diagonal and nonzero diagonal entries, and $\Pi$ is a partial permutation matrix: each row and column holds at most one $1$, and all other entries are $0$.

The number $a$ of ones in $\Pi$ is set by the [Matrix rank](matrix-rank.md) of $A$.

For example, let $A=\begin{pmatrix}1&0\\1&0\end{pmatrix}$, which has $m=2$ and rank $a=1$. Take $\Pi=\begin{pmatrix}1&0\\0&0\end{pmatrix}$, $E_1=\begin{pmatrix}1&0\\1&1\end{pmatrix}$ and $E_2=I$. Then $E_1\Pi=\begin{pmatrix}1&0\\1&0\end{pmatrix}=A$, so $A=E_1\Pi E_2$ with $\Pi$ holding one $1$.

Every rational $m\times m$ matrix has such a factorization. <cite data-source="paper">Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization</cite>.
