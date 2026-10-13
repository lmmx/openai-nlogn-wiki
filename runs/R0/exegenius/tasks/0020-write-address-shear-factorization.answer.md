An address shear is a linear update of two blocks of address fields. The address shear is the endpoint operator of the bit network, a [Finite linear network with roles and frames](linear-network-roles.md). A lower-triangular factorization reduces its rational generalization, the frame change of a network edge, to interchanges plus linear-cost updates.

Let $m$ be the number of fields in each vector. Let $H=(H_1,\ldots,H_m)$ and $D=(D_1,\ldots,D_m)$ be two vectors of address fields. Each field is a $b$-digit block of radix $q$, so it ranges over $\mathbb Z/q^b\mathbb Z$, where $q$ is a fixed odd prime and $b$ is the number of radix-$q$ digits in a field.

For a rational $m\times m$ matrix $A$, the shear by $A$ is $(H,D)\mapsto(H+AD,D)$. With $A=I$ it is the address shear $(H,D)\mapsto(H+D,D)$. Let $a$ be the rank of $A$ over $\mathbb Q$, the number of linearly independent rows of $A$.

Every such $A$ factors as $A=E_1\Pi E_2$, where $E_1$ and $E_2$ are invertible lower-triangular rational matrices and $\Pi$ is a partial permutation matrix with $a$ ones, at most one in each row and column. This is Grigor'ev's singular-matrix Bruhat factorization with coordinate order reversed (Grigor'ev 1982, Appendix A.2). Elimination proves it: take the topmost nonzero row and its rightmost nonzero entry as pivot, clear the entries to its left by right multiplication and the entries below it by left multiplication with lower-triangular elementary matrices, and scale the pivot to one. Repeat on the rest.

Example: for $m=2$ and $A=\begin{pmatrix}1&1\\0&0\end{pmatrix}$, $a=1$ and $A=\Pi E_2$ with $\Pi=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ and $E_2=\begin{pmatrix}1&0\\1&1\end{pmatrix}$, where $E_1=I$.

Transform $D$ by $E_2$ and $H$ by $E_1^{-1}$. For each one of $\Pi$ in position $(i,j)$, update $H_i\gets H_i+D_j$. Transform $H$ by $E_1$ and $D$ by $E_2^{-1}$. Then $H$ ends as $H+E_1\Pi E_2D=H+AD$, and $D$ is unchanged. Here $V$ is the stored bit volume. The triangular stages cost $O(V)$: with $m$ fixed, one sweep in descending coordinate order updates each coordinate from earlier coordinates that still hold their original values. Each update $H_i\gets H_i+D_j$ is one interchange with two linear-cost additions. So the shear needs $a$ interchanges, not $m$.

Over the whole network, the interchange count is the sum of the edge ranks, less than the number of wires times $m$, which saves a power of the chunk width. <cite data-source="paper">The number of recursive calls is the sum of the edge ranks, exactly $s$.</cite>
