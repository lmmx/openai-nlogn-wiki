The Chinese-remainder address map is a rearrangement that places a coefficient list on a product of distinct prime cyclic axes while preserving convolution. It is implemented by [fast address interchange](address-interchange.md) steps. It is the first step of the argument, since later transforms treat each axis separately.

A cyclic axis is a dimension whose indices are taken modulo its length. Let $N$ be the number of coefficients, and let $s$ be the number of axes. Each $p_i$ is the prime length of the $i$-th axis, for $i$ running from $1$ to $s$, so that $N = p_1 p_2 \cdots p_s$.

The map rests on the Chinese remainder theorem: because the $p_i$ are pairwise coprime, each tuple of residues, one modulo each $p_i$, comes from exactly one integer modulo $N$. Write $t$ for a position in the list, running from $0$ to $N-1$. The map sends $t$ to its residues $(t \bmod p_1, \dots, t \bmod p_s)$.

The map reduces a [cyclic convolution](cyclic-convolution.md) of length $N$ to a convolution over the $s$ axes. A cyclic convolution adds products of coefficients at two positions whose sum is $t$ modulo $N$. Two positions sum to $t$ modulo $N$ exactly when their residues add to those of $t$ on every axis, so the same sum, reindexed by residue tuples, is a convolution over the axes.

For example, with $N = 15 = 3 \cdot 5$, positions $7$ and $9$ have residues $(1, 2)$ and $(0, 4)$, which add to $(1, 1)$, the residues of $7 + 9 \equiv 1$.

The radix-digit coefficient list is placed on $s$ distinct prime axes <cite data-source="paper">by a Chinese-remainder map that preserves convolution</cite>. Controlled cyclic shifts, rotations by an amount set by a control value, and address interchanges make this reordering cheap.
