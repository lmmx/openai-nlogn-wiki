Packed selected-bit addition adds one selected bit position across several [address chunks](address-field.md) at once, using [cyclic shifts](cyclic-shift.md) and a small deterministic correction for exceptional addresses. Packed selected-bit addition supplies the binary basis changes of the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md). Packed selected-bit addition performs its basis changes in each [transform round](transform-round.md). Packed selected-bit addition contributes one term to the [cost table](cost-table.md) of the theorem.

Packed selected-bit addition acts on two disjoint [address fields](address-field.md) of equal width, the source $\mathcal{X}$ and the target $\mathcal{W}$. Packed selected-bit addition uses its third chunk as [scratch storage](scratch-storage.md), $\mathcal{T}$, whose initial value is arbitrary and must be restored.

Each chunk has width $\lambda$ bits, cut into $\nu$ segments of $\mu$ bits, so $\lambda = \nu\mu$. Let $\rho$ be the position of the first selected bit, counted from $0$ at the least significant end. The selected bit of segment $\sigma$ is its lowest bit, at position $\rho+\sigma\mu$ for $0\le\sigma<\nu$, where $\sigma$ is a segment index. The other $\mu-1$ bits of a segment form its guard, whose value $\gamma$ lies between $0$ and $2^{\mu-1}-1$.

Packed selected-bit addition adds selected bits by [exclusive or](xor.md), so each selected bit of $\mathcal{W}$ is XORed with the selected bit of $\mathcal{X}$ in the same segment. Packed selected-bit addition updates its target chunk by controlled [cyclic shifts](cyclic-shift.md). A segment's value is $2\gamma$ plus its selected bit. For a control bit $\beta\in\{0,1\}$, a cyclic shift of $\mathcal{W}$ by $\pm 2^{\rho+\sigma\mu}$ adds $\pm 1$ to the value of segment $\sigma$, with sign $-1$ when the selected bit is $1$ and $+1$ when it is $0$. For example, with $\mu=3$, $3=011_2$ becomes $2=010_2$.

One shift cannot test the selected bit of $\mathcal{W}$, so the sign depends on it. For a segment of $\mathcal{W}$ with value $\xi$ and the corresponding segment of $\mathcal{T}$ with value $\eta$, the construction uses eight controlled updates. <cite data-source="paper">We first construct eight rotations</cite> that have the required effect away from a small set of addresses. Here $[P]$ is $1$ when $P$ holds and $0$ otherwise, and the updates run in order (1) to (8):

$$
\begin{aligned}
(1)&\ \xi\leftarrow\xi-\beta\,[\eta\equiv 0 \pmod 2], & (2)&\ \eta\leftarrow\eta-\beta\,[\xi\equiv 0 \pmod 2],\\
(3)&\ \xi\leftarrow\xi+\beta\,[\eta\equiv 0 \pmod 2], & (4)&\ \eta\leftarrow\eta+\beta\,[\xi\equiv 0 \pmod 2],\\
(5)&\ \eta\leftarrow\eta+\beta\,[\xi\equiv 1 \pmod 2], & (6)&\ \xi\leftarrow\xi+\beta\,[\eta\equiv 1 \pmod 2],\\
(7)&\ \eta\leftarrow\eta-\beta\,[\xi\equiv 1 \pmod 2], & (8)&\ \xi\leftarrow\xi-\beta\,[\eta\equiv 1 \pmod 2].
\end{aligned}
$$

Packed selected-bit addition uses updates like the [Address shear](address-shear.md). If $\beta=1$, the parities $(\xi \bmod 2,\ \eta \bmod 2)$ run through the cycle $(00\ 01\ 10)$ under lines (1) to (4) and $(01\ 10\ 11)$ under lines (5) to (8). Together they give $(00\ 10)(01\ 11)$, which flips the parity of $\xi$ alone, and <cite data-source="paper">the arbitrary auxiliary integer w is restored</cite>. So $\xi$ becomes $\xi+\beta(1-2(\xi \bmod 2))$. <cite data-source="paper">Each coordinate is updated four times by at most one</cite>.

The top selected bit is left out of this stage: <cite data-source="paper">Omit the most significant selected position</cite> temporarily. A guard with $10\le\gamma\le 2^{\mu-1}-11$ gives a segment value in $[20,\,2^\mu-21]$, so a change of size at most eight stays inside the segment. Let $\mathcal{B}$ be the set of addresses at which some guard of the first $\nu-1$ segments of $\mathcal{W}$ or $\mathcal{T}$ lies outside this range. Off $\mathcal{B}$ it gives exactly the required XORs.

Each guard has exactly twenty excluded values, $0,\dots,9$ and $2^{\mu-1}-10,\dots,2^{\mu-1}-1$: <cite data-source="paper">There are exactly twenty excluded values for each guard in (23).</cite> <cite data-source="paper">Indeed, the complete y, z ranges give the same guard distribution</cite>, so each guard takes each of its $2^{\mu-1}$ values equally often, and one is excluded from a fraction $20/2^{\mu-1}$ of addresses. Packed selected-bit addition bounds its exceptional set by a [union bound](union-bound.md) over the $2(\nu-1)$ guards, so $\mathcal{B}$ holds at most a fraction $80(\nu-1)/2^{\mu}$ of all addresses.

The records on $\mathcal{B}$ are corrected. <cite data-source="paper">The correction depends only on addresses, so the time bound is worst-case</cite> over all payloads. Packed selected-bit addition is correct for every [payload](payload.md) it carries. Packed selected-bit addition computes the [destination rank](destination-rank.md) of each extracted record, its position in the final order after the move. Packed selected-bit addition sorts the extracted records by a [stable radix sort](stable-radix-sort.md) on these ranks, and reinserts each at its rank.

The top selected bit is XORed in afterwards by a two-bit permutation of the two chunks. On the pair of top selected bits, one from $\mathcal{X}$ and one from $\mathcal{W}$, the map $(a,b)\mapsto(a,\,a\oplus b)$ fixes $00$ and $01$ and swaps $10$ and $11$, so it XORs the first bit into the second. <cite data-source="paper">Lemma 3 applies any fixed permutation to the two-bit value at two specified address</cite> positions in $O(V)$ time.

Packed selected-bit addition exchanges its chunks by the [Address-field interchange](address-interchange.md) to bring a target chunk beside its controls. Each exchange costs $O(V\lambda^\tau)$, with $\tau$ the width exponent of the interchange, and each shift costs $O(V)$. <cite data-source="paper">The movement costs O(V (Lτ + 1))</cite> in total.

Here $R$ is the number of bits in each record, and $\zeta=\lceil\log_2(2V)\rceil$ counts the bits of a stream position. The extra time is small relative to $V$ under <cite data-source="paper">When Arect = O(p), R exceeds every fixed polynomial in p, f ≤ d ≤ p, and K/ log p → ∞</cite>, since $\zeta$ is polynomial in the family parameter, $R$ outgrows every polynomial, and $\mu$ outgrows its logarithm.
