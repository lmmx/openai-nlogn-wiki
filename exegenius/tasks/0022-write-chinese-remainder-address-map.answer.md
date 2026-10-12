The Chinese-remainder address map is a rearrangement that places a coefficient list on a product of distinct prime cyclic axes while preserving convolution. It is implemented by [fast address interchange](address-interchange.md) steps, and it is the first step of the argument: once the coefficients sit on these axes, later transforms can treat each axis separately.

A cyclic axis is a dimension whose indices are taken modulo its length. Write $N = p_1 p_2 \cdots p_k$ for the number of coefficients, where $p_1, \dots, p_k$ are distinct primes and $k$ is their count. Each $p_i$ is the length of the $i$-th axis.

The map rests on the Chinese remainder theorem: if $p_1, \dots, p_k$ are pairwise coprime, each tuple of residues modulo them comes from exactly one integer modulo $N$. Write $m$ for a position in the list; it is sent to its residues $(m \bmod p_1, \dots, m \bmod p_k)$. Adding positions modulo $N$ adds these residues componentwise, so the map reduces a [cyclic convolution](cyclic-convolution.md) of length $N$ to a convolution over the $k$ axes.

For example, with $N = 15 = 3 \cdot 5$, position $7$ goes to $(1, 2)$ and position $9$ goes to $(0, 4)$. Their sum $7 + 9 \equiv 1 \pmod{15}$ goes to $(1, 1)$, which is the componentwise sum $(1+0, 2+4) \bmod (3, 5)$.

The radix-digit coefficient list is placed on $k$ distinct prime axes <cite data-source="paper">by a Chinese-remainder map that preserves convolution</cite>. Controlled cyclic shifts and address interchanges make this reordering cheap, which is why the split is worth making.
