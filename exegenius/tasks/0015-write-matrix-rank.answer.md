The rank of a matrix is the largest number of linearly independent rows of the matrix. It equals the largest number of linearly independent columns, and it equals the number of nonzero pivots that Gaussian elimination produces. The lower-triangular factorization argument uses it to count the ones in its final partial permutation matrix.

Let $M$ be a matrix with real entries. Its rows are linearly independent when no nontrivial linear combination of them is the zero row. Write $\operatorname{rank} M$ for the number of such rows in a maximal independent set.

Example. Take
$$M=\begin{pmatrix}1&2\\2&4\end{pmatrix}.$$
The second row is twice the first, so the rows are dependent and $\operatorname{rank} M\le 1$. Subtracting twice row 1 from row 2 gives a zero row, leaving one nonzero pivot, so $\operatorname{rank} M=1$.

Elimination computes the rank because row operations preserve it. After a nonzero pivot is used to clear its column and row, the matrix splits into the pivot and a smaller matrix, and the rank of the whole is one more than the rank of the smaller matrix. Each pivot therefore lowers the remaining rank by exactly one, and the process ends when no nonzero entries remain. <cite data-source="paper">Each step isolates a rank-one block and leaves the remaining rank in the active submatrix</cite>.

The proof counts the ones of the final partial permutation matrix this way. Because each pivot accounts for one unit of rank, the final matrix has as many ones as the rank of the original matrix. <cite data-source="paper">Thus the final partial permutation matrix has exactly $a$ ones</cite>.
