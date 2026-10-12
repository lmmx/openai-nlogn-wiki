The rank of a matrix is the largest number of linearly independent rows, which also equals the largest number of independent columns and the number of nonzero pivots from Gaussian elimination. The lower-triangular factorization uses it to count the ones of a partial permutation matrix, a 0-1 matrix with at most one 1 in each row and each column.

Let $M$ be a real matrix. Its rows are linearly independent when no nontrivial combination of them is the zero row, and the rank of $M$ is the largest number of such rows. For example, the matrix with rows $(1,2)$ and $(2,4)$ has rank 1, because the second row is twice the first.

Elimination computes rank because invertible row and column operations preserve it. Let $p$ be the nonzero pivot, the top-left entry after reordering rows and columns. Clearing its column below it and its row to the right gives
$$\begin{pmatrix}p&0\\0&S\end{pmatrix},$$
where $S$ is the smaller matrix left after deleting the pivot's row and column. The rows below the pivot have zero first entry, and their other entries are the rows of $S$. The pivot row is therefore independent of them, so $\operatorname{rank} M=1+\operatorname{rank} S$. Each pivot lowers the remaining rank by exactly one. <cite data-source="paper">Each step isolates a rank-one block and leaves the remaining rank in the active submatrix</cite>.

The same bookkeeping counts the ones. Each pivot leaves one 1 in the final partial permutation matrix, in a row and column that later steps never change. The final matrix therefore has as many ones as there are pivots, and since each pivot lowers the rank by one, that number is $\operatorname{rank} M$.
