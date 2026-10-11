A binary change of basis is an invertible linear change of coordinates on a block of selected address bits, built over the [binary field](binary-field.md). On the way to the main result it is the step that puts a residual basis of directions into coordinate positions, which the [rank-saving recursion](rank-saving-recursion.md) then uses. The paper describes this step as <cite data-source="paper">The next step puts those directions into coordinate positions without performing a general transpose.</cite>

Let $m$ be the number of selected address bits the change acts on. Write $\mathbf b=(b_1,\dots,b_m)$ for the column of those bits, each $b_i\in\mathbb F_2$. A binary change of basis is specified by an invertible matrix in [Linear algebra basics](linear-algebra-basics.md): a matrix $M$ with an inverse $M^{-1}$, so that $M^{-1}M=I$. We write $\mathrm{GL}(m,\mathbb F_2)$ for the set of invertible $m\times m$ matrices over $\mathbb F_2$. The change sends the bits $\mathbf b$ to $M\mathbf b$. Only invertibility is needed: <cite data-source="paper">The matrix M need not preserve the dot product: equation (15) only uses its invertibility.</cite>

Here $\mathbf a\in\mathbb F_2^m$ denotes an address of the $m$ selected bits. For $M\in\mathrm{GL}(m,\mathbb F_2)$, $P_M$ is the address permutation that moves the value at each address $\mathbf a$ to $M\mathbf a$. The paper's wording is <cite data-source="paper">permutation that moves the value at x to M x.</cite>

**Elementary row additions.** The basic move is adding one row of $M$ to another. For example, take $m=3$ and
$$M=\begin{pmatrix}1&1&0\\0&1&0\\0&0&1\end{pmatrix}.$$
This is the identity with an extra 1 in row 1, column 2, so it adds the second bit into the first. For $\mathbf b=(1,1,0)$,
$$M\mathbf b=(1\oplus 1,\;1,\;0)=(0,1,0).$$
Adding row 2 to row 1 a second time restores the original matrix, so $M^{-1}=M$.

Every $M\in\mathrm{GL}(m,\mathbb F_2)$ is a product of row additions. <cite data-source="paper">Gaussian elimination expresses any M ∈ GL(m, F2 ) as a product of at most m(m − 1) + 3m elementary row additions</cite>. For $m=3$ this is at most $15$ row additions. The inverse of such a product is the same row additions in reverse order: <cite data-source="paper">Reversing the elimination gives the required product since each row addition is an involution.</cite>
