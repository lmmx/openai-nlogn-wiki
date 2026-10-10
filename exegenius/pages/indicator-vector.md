Let $U$ be a finite set, often called the ground set. For a subset $A \subseteq U$, its indicator vector is the vector $\mathbf{1}_A$ indexed by the elements of $U$, with entry $1$ at each element of $A$ and $0$ at each element not in $A$.

For example, if $U = \{1, 2, 3, 4\}$ and $A = \{2, 4\}$, then $\mathbf{1}_A = (0, 1, 0, 1)$. For two subsets $A$ and $B$, the dot product of their indicator vectors is $\mathbf{1}_A \cdot \mathbf{1}_B = |A \cap B|$, the number of common elements. Take $B = \{4\}$ as an example: $\mathbf{1}_A \cdot \mathbf{1}_B = 0 \cdot 0 + 1 \cdot 0 + 0 \cdot 0 + 1 \cdot 1 = 1$, which is $|A \cap B| = |\{4\}| = 1$.

This identity is why indicator vectors are useful for intersections. Counting common elements becomes an inner product, which is a linear-algebra computation.

The paper uses indicator vectors of three-element subsets of a ground set. It notes that orthogonality of these vectors is what permits the subspace assignments of the [subset-intersection construction](subspace-intersection-network.md).
