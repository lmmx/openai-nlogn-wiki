Packed selected-bit addition acts on two disjoint [address fields](address-field.md) of equal width, the source $\mathcal{X}$ and the target $\mathcal{W}$. It XORs selected bits of $\mathcal{X}$ into the same bits of $\mathcal{W}$ at every address, and it supplies the binary basis changes of the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md). It contributes one term to the [cost table](cost-table.md) of the main theorem, which bounds exact multiplication of $n$-bit integers by $O(n(\lg n)^{1-\kappa})$ for a fixed $\kappa>0$. Packed selected-bit addition performs its basis changes in each [transform round](transform-round.md).

Packed selected-bit addition uses its third field as [scratch storage](scratch-storage.md), $\mathcal{T}$, whose initial value is arbitrary and must be restored. Each field has $L=fK$ address bits.

Let $\rho$ be the position of the first selected bit, counted from $0$ at the least significant end. Let $i$ index the $f-1$ segments, $0\le i<f-1$, so segment $i$ starts at the selected position $\rho+iK$ and occupies $K$ bits, where $K$ is the segment width. The lowest bit of a segment is its selected bit, and the other $K-1$ bits form its guard, whose value $\gamma$ lies between $0$ and $2^{K-1}-1$. As an integer, a segment has value $2\gamma$ plus its selected bit.

Packed selected-bit addition adds selected bits by [exclusive or](xor.md), so each selected bit of $\mathcal{W}$ is XORed with the selected bit of $\mathcal{X}$ in the same segment. A shift adds its offset to the field's integer value. Packed selected-bit addition updates its target field by controlled [cyclic shifts](cyclic-shift.md). <cite data-source="paper">The shift offset never depends on its target chunk</cite>, so a shift cannot test the selected bit of the field it changes.

Shifting $\mathcal{W}$ by $2^{\rho+iK}$ adds $1$ to the value $2\gamma+a$ of segment $i$, where $a$ is its selected bit. The carry stays inside the segment while the value stays in $[0,2^K-1]$. Adding $+1$ flips a selected bit $0$ to $1$, but flipping a $1$ to $0$ needs $-1$. The eight updates below supply that sign.

For a segment of $\mathcal{W}$ with value $\xi$ and the corresponding segment of $\mathcal{T}$ with value $\eta$, the procedure applies eight controlled updates. Each is controlled by a bit $\beta\in\{0,1\}$, the selected bit of $\mathcal{X}$ in that segment. Here $[P]$ is $1$ when $P$ holds and $0$ otherwise, and the updates run in order (1) to (8):

$$
\begin{aligned}
(1)&\ \xi\leftarrow\xi-\beta\,[\eta\equiv 0 \pmod 2], & (2)&\ \eta\leftarrow\eta-\beta\,[\xi\equiv 0 \pmod 2],\\
(3)&\ \xi\leftarrow\xi+\beta\,[\eta\equiv 0 \pmod 2], & (4)&\ \eta\leftarrow\eta+\beta\,[\xi\equiv 0 \pmod 2],\\
(5)&\ \eta\leftarrow\eta+\beta\,[\xi\equiv 1 \pmod 2], & (6)&\ \xi\leftarrow\xi+\beta\,[\eta\equiv 1 \pmod 2],\\
(7)&\ \eta\leftarrow\eta-\beta\,[\xi\equiv 1 \pmod 2], & (8)&\ \xi\leftarrow\xi-\beta\,[\eta\equiv 1 \pmod 2].
\end{aligned}
$$

Each line changes one value by $\pm\beta$ and tests the parity of the other value, its selected bit, so it is one controlled shift. Packed selected-bit addition uses updates like the [Address shear](address-shear.md).

If $\beta=1$, the parity pairs $(\xi \bmod 2,\ \eta \bmod 2)$ cycle through $(00\ 01\ 10)$ under lines (1) to (4) and through $(01\ 10\ 11)$ under lines (5) to (8). Together these give $(00\ 10)(01\ 11)$, which flips the parity of $\xi$ alone. Both quotients by two are preserved, and $\eta$ returns to its start: <cite data-source="paper">the arbitrary auxiliary integer w is restored</cite>. So $\xi\mapsto\xi+\beta(1-2(\xi \bmod 2))$. The selected bit of $\mathcal{W}$ flips exactly when $\beta=1$, and the guard is unchanged, which is the XOR. <cite data-source="paper">Each coordinate is updated four times by at most one</cite>.

Let $\mathcal{E}$ be the set of addresses at which some guard of the $f-1$ segments of $\mathcal{W}$ or of $\mathcal{T}$ lies outside $[10,\,2^{K-1}-11]$. Off $\mathcal{E}$, each segment value lies in $[20,\,2^K-21]$, so a displacement of at most eight keeps it in $[0,\,2^K-1]$. No carry crosses a segment, and the stage gives exactly the required XORs.

Each guard takes each of its $2^{K-1}$ values equally often over the addresses, and exactly twenty values are excluded, so the excluded fraction is $20/2^{K-1}$. The procedure bounds its exceptional set by a [union bound](union-bound.md) over the $2(f-1)$ guards, giving $|\mathcal{E}|\le 80(f-1)2^{-K}M$, where $M$ counts the records.

<cite data-source="paper">The correction depends only on addresses, so the time bound is worst-case</cite> over all payloads. Packed selected-bit addition is correct for every [payload](payload.md) it carries. The procedure scans the [stream](stream.md) of all $M$ records with a rank counter to find the records at addresses in $\mathcal{E}$. For a record at address $q$, reverse the eight updates with negated offsets and apply the XORs to find $q'$.

The procedure computes the [destination rank](destination-rank.md) of each extracted record. Its value is $\operatorname{rank}(q')=\operatorname{rank}(q)+\sum_h (q'_h-q_h)\sigma_h$, summed over $h\in\{\mathcal{X},\mathcal{W},\mathcal{T}\}$, where $\sigma_h$ is the record stride of field $h$. The procedure sorts the extracted records by a [stable radix sort](stable-radix-sort.md) on these ranks. The map sends $\mathcal{E}$ onto itself, so the ranks are distinct and are exactly the holes left by the extraction. One forward scan then reinserts each record at its rank.

The top selected bit is XORed in last. On two bits, $e_1$ from $\mathcal{X}$ and $e_2$ from $\mathcal{W}$, the map $(e_1,e_2)\mapsto(e_1,\,e_1\oplus e_2)$ fixes $00$ and $01$ and swaps $10$ and $11$, so it XORs the first bit into the second. <cite data-source="paper">Lemma 3 applies any fixed permutation to the two-bit value at two specified address</cite> positions in $O(V)$ time.

The procedure exchanges its fields by the [Address-field interchange](address-interchange.md). <cite data-source="paper">Lemma 12 exchanges two disjoint address chunks of equal width L in O(V Lτ ) time</cite>, with $\tau$ the fixed exponent of the interchange. It uses at most sixteen exchanges and eight shifts, each shift costing $O(V)$. <cite data-source="paper">The movement costs O(V (Lτ + 1))</cite> in total.

Each address holds a record of $R$ bits, so $V=MR$. The correction adds $O(MA_{\mathrm{rect}}^3+\delta MA_{\mathrm{rect}}(R+A_{\mathrm{rect}}))$ time, where $A_{\mathrm{rect}}=\lceil\log_2(2V)\rceil$ bounds the bit size of every integer involved, and $\delta=80(f-1)2^{-K}$. The total time is

$$
O\bigl(V(L^{\tau}+1)+MA_{\mathrm{rect}}^3+\delta\,MA_{\mathrm{rect}}(R+A_{\mathrm{rect}})\bigr).
$$

The bound is stated along a [family parameter](family-parameter.md) that tends to infinity. Along that family $A_{\mathrm{rect}}$ grows at most linearly, $R$ outgrows every polynomial, and $K$ outgrows the logarithm, so the extra terms, which are $A_{\mathrm{rect}}^3/R$ and $\delta A_{\mathrm{rect}}(1+A_{\mathrm{rect}}/R)$ after dividing by $V=MR$, tend to zero. So the time is $O(V(L^{\tau}+1))$.
