Matrix rank is the number of linearly independent rows of a matrix. The paper uses it to count the interchanges needed to apply one matrix shear on address fields, and that count is what saves a power of the chunk width below $n \log n$.

Matrix rank is defined using the vector spaces and linear maps of [Linear algebra basics](linear-algebra-basics.md).

Let $\mathbb{Q}$ be the rational numbers, the fractions $p/q$ with integers $p$ and $q \neq 0$. Here $m$ is the number of rows of a square matrix, which is also its number of columns. Let $M$ be a rational matrix with $m$ rows and $m$ columns. Each row of $M$ is a vector of $m$ rational numbers.

The rank of $M$ over $\mathbb{Q}$ is the largest number of its rows that are linearly independent over $\mathbb{Q}$, written $\operatorname{rank}_{\mathbb{Q}}(M)$. It is also called the rational rank. The largest number of linearly independent columns is the same number, so $\operatorname{rank}_{\mathbb{Q}}(M) \le m$, with equality exactly when $M$ is invertible. Row reduction computes it: each pivot that elimination finds is one independent row, and the number of pivots is the rank.

For example, take $m = 2$ and $M = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$. The second row is twice the first, so only one row is independent and $\operatorname{rank}_{\mathbb{Q}}(M) = 1$. The $2 \times 2$ identity matrix has rank 2.

The paper's factorization lemma applies to every such matrix: <cite data-source="paper">Every rational m × m matrix A of rank a has a</cite> factorization into lower triangular factors and a partial permutation matrix, and <cite data-source="paper">Π has exactly a entries equal to</cite> one, so the number of ones is the rank. The paper writes the rank as $a$ there.

The rank is also the cost. An edge change given by a matrix of rank $a$ is implemented <cite data-source="paper">with one smaller interchange per unit of its rational rank.</cite> The lemma on matrix shears then states that the shear for a rational matrix of rank $a$ <cite data-source="paper">can be performed with exactly a interchanges of pairs of b-digit fields</cite>. <cite data-source="paper">Because the sum of these ranks is less than the number of wires</cite> times $m$, the total number of interchanges is below the number of wires times $m$, and the recurrence saves a power of the chunk width.
