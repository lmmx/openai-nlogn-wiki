The Chinese-remainder map to prime cyclic axes is the rearrangement that places a coefficient list on a product of cyclic axes whose lengths are distinct primes. It is the first representation change in the multiplication argument, and it prepares the list for the transforms on those axes.

Let $N$ be the number of coefficients in the list, and write $N = p_1 p_2 \cdots p_k$ with $p_1, \dots, p_k$ distinct primes. The index $i \in \{0, \dots, N-1\}$ of a coefficient is sent to the tuple of its residues $(i \bmod p_1, \dots, i \bmod p_k)$. Each $\mathbb{Z}_{p_j}$ is the set of residues modulo $p_j$, so the tuple lies in the product $\mathbb{Z}_{p_1} \times \cdots \times \mathbb{Z}_{p_k}$, whose $j$-th axis has length $p_j$.

Because the $p_j$ are pairwise coprime, the Chinese remainder theorem makes this map a bijection between the $N$ indices and the $N$ tuples. Reduction modulo each $p_j$ respects addition, so an index that wraps modulo $N$ becomes a residue that wraps separately on each axis.

For example, take $N = 15 = 3 \cdot 5$. Index $7$ goes to $(1, 2)$ and index $8$ goes to $(2, 3)$. Their sum $15 \equiv 0$ goes to $(0, 0)$, which is the componentwise sum $(1+2, 2+3)$ reduced modulo $(3, 5)$.

This map preserves [convolution](convolution.md) on the axes, so a cyclic product of two lists on $\mathbb{Z}_N$ becomes a product on the prime axes. The map is applied to the radix-digit coefficient list produced by [reduction of integer product to digit convolution](radix-digit-reduction.md). The paper places it on <cite data-source="paper">distinct prime cyclic axes</cite>, which lets the next step, [Gaussian resampling](gaussian-resampling.md), express each Fourier transform on these axes through transforms with power-of-two lengths.

The map's axis moves are costed in the [fixed-tape machine model and stream operations](fixed-tape-model.md). The paper implements the map through <cite data-source="paper">triangular controlled shifts and charged axis moves</cite>, so each move is counted as data movement.
