A binary change of basis is an invertible linear change of coordinates on a block of [selected address bits](address-field.md), built over the [binary field](binary-field.md). It puts the directions of a [rank-saving recursion](rank-saving-recursion.md) into coordinate positions.

A residual basis of directions is a basis $v_1,\dots,v_\rho$ of an edge's residual, a subspace of $\mathbb F_2^m$ (here $v$ and $\rho$ are not vertices or role permutations). <cite data-source="paper">For an edge e, write Be for its residual basis</cite>.

Let $m$ count the selected bits and $\sigma=(\sigma_1,\dots,\sigma_m)$ the column of their values, each $\sigma_i\in\mathbb F_2$. A binary change of basis is specified by an invertible matrix in [Linear algebra basics](linear-algebra-basics.md): a matrix $M$ with inverse $M^{-1}$, $M^{-1}M=I$. The change acts on an [address field](address-field.md), sending $\sigma$ to $M\sigma$.

For an invertible $m\times m$ matrix $M$ over $\mathbb F_2$, $P_M$ is the address permutation that moves the value at each address $\alpha\in\mathbb F_2^m$ to $M\alpha$, so $(P_M f)(\alpha)=f(M^{-1}\alpha)$, with $f$ mapping addresses to values. Choose $M$ with first columns $v_1,\dots,v_\rho$, so $M\zeta_j=v_j$, where $\zeta_j$ has a 1 in position $j$ and 0 elsewhere. Conjugation by $P_M$ turns the shift by $v_j$ into the shift by $\zeta_j$, changing only bit $j$.

Over $\mathbb F_2$ the only nonzero scalar is 1, so elimination uses no scaling. The matrix stays invertible, so each pivot column has a 1 at or below the pivot row: swap it up, then clear the column by adding the pivot row. The steps $\mathcal E_1,\dots,\mathcal E_k$ satisfy $\mathcal E_k\cdots\mathcal E_1M=I$. Each row addition is its own inverse over $\mathbb F_2$, since adding a row twice gives 0, so $M=\mathcal E_1\cdots\mathcal E_k$. A swap is three additions: $b$ to $a$, $a$ to $b$, $b$ to $a$.

<cite data-source="paper">Gaussian elimination expresses any M ∈ GL(m, F2 ) as a product of at most m(m − 1) + 3m</cite> row additions: at most $m-1$ clearing additions per pivot, and at most one swap per pivot. For $m=3$ this is at most $6+9=15$ row additions.
