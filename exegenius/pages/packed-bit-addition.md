Packed selected-bit addition contributes one term to the [Cost table](cost-table.md) of the main theorem, which bounds exact multiplication of $n$-bit integers by $O(n(\lg n)^{1-\kappa})$. Packed selected-bit addition supplies the binary basis changes of the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md). Packed selected-bit addition performs its basis changes in each [Transform round](transform-round.md). Packed selected-bit addition adds selected bits by [Exclusive or](xor.md).

It acts on two disjoint blocks, each an [Address field](address-field.md) of $L=fK$ address bits, a source $\mathcal{X}$ and a target $\mathcal{W}$, and it XORs one selected bit of each segment of $\mathcal{X}$ into the same bit of $\mathcal{W}$ at every address. Packed selected-bit addition uses its third field as [Scratch storage](scratch-storage.md), $\mathcal{Z}$, whose initial value is arbitrary and must be restored.

Let $\rho$ be the position of the first selected bit, counted from $0$ at the least significant end, with $0\le\rho<K$; here $\rho$ is a position, not the role permutation. For $0\le i<f-1$, segment $i$ is the $K$ bits from position $\rho+iK$ upward; here $i$ numbers segments, not the imaginary unit. The lowest bit of a segment is its selected bit $a\in\{0,1\}$, and the other $K-1$ bits form its guard $\gamma$, with $0\le\gamma\le 2^{K-1}-1$. A segment has value $2\gamma+a$. Write $\xi$ for the value of a segment of $\mathcal{W}$ and $\eta$ for the value of the matching segment of $\mathcal{Z}$.

## Eight controlled updates

Adding $+1$ to $2\gamma$ flips $a$ from $0$ to $1$ without a carry, but flipping $1$ to $0$ needs $-1$. Eight updates supply that sign. Here $[P]$ is $1$ when $P$ holds and $0$ otherwise, and $u\equiv v \pmod 2$ means that $2$ divides $u-v$. For a segment whose control bit $\beta$ is the selected bit of $\mathcal{X}$, they run in order:

$$
\begin{aligned}
(1)&\ \xi\leftarrow\xi-\beta\,[\eta\equiv 0 \pmod 2], & (2)&\ \eta\leftarrow\eta-\beta\,[\xi\equiv 0 \pmod 2],\\
(3)&\ \xi\leftarrow\xi+\beta\,[\eta\equiv 0 \pmod 2], & (4)&\ \eta\leftarrow\eta+\beta\,[\xi\equiv 0 \pmod 2],\\
(5)&\ \eta\leftarrow\eta+\beta\,[\xi\equiv 1 \pmod 2], & (6)&\ \xi\leftarrow\xi+\beta\,[\eta\equiv 1 \pmod 2],\\
(7)&\ \eta\leftarrow\eta-\beta\,[\xi\equiv 1 \pmod 2], & (8)&\ \xi\leftarrow\xi-\beta\,[\eta\equiv 1 \pmod 2].
\end{aligned}
$$

So $[\eta\equiv 0 \pmod 2]$ is $1$ exactly when $\eta$ is even. Packed selected-bit addition has the form of an [Address shear](address-shear.md): each line adds a controlled $\pm1$ to one field according to a parity test on the other. <cite data-source="paper">The shift offset never depends on its</cite> target field, so each line is a bijection of addresses. Packed selected-bit addition updates its target field by a [Cyclic shift](cyclic-shift.md) controlled by the bits of the segments.

Lines (1) to (4) cycle the parity pair $(\xi \bmod 2,\ \eta \bmod 2)$ through $00\to01\to10\to00$ and fix $11$. Lines (5) to (8) cycle it through $01\to10\to11\to01$ and fix $00$. Together they give $(00\ 10)(01\ 11)$, which flips the parity of $\xi$ alone. <cite data-source="paper">both quotients under division by two are preserved, and the arbitrary auxiliary integer w is restored</cite>, where the paper's $w$ is our $\eta$. So the net effect is $\xi\mapsto\xi+\beta(1-2(\xi \bmod 2))$ with $\eta$ unchanged.

For example, take $\xi=4$, $\eta=5$, $\beta=1$. Line (1) changes nothing since $\eta$ is odd; (2) gives $\eta=4$; (3) gives $\xi=5$; (4) changes nothing; (5) gives $\eta=5$; (6) gives $\xi=6$; (7) changes nothing; (8) gives $\xi=5$. So the selected bit of $\mathcal{W}$ flips exactly when $\beta=1$, and the guard is unchanged: that is the XOR.

## Exceptional addresses

Let $\mathcal{E}$ be the set of addresses at which some guard of a segment of $\mathcal{W}$ or $\mathcal{Z}$ lies outside $[10,\,2^{K-1}-11]$. Off $\mathcal{E}$, each segment value lies in $[20,\,2^K-21]$. <cite data-source="paper">Each coordinate is updated four times by at most one</cite>, so each value stays in $[0,\,2^K-1]$ and no carry crosses a segment.

Each guard takes each of its $2^{K-1}$ values equally often over the addresses, since the addresses are a product of chunk ranges. Exactly twenty values are excluded: $0$ to $9$ and $2^{K-1}-10$ to $2^{K-1}-1$. Packed selected-bit addition bounds its exceptional set by a [Union bound](union-bound.md) over the $2(f-1)$ guards: $|\mathcal{E}|\le\delta M$, where $M$ is the number of records and $\delta=\min\{1,\,80(f-1)2^{-K}\}$.

## Correcting the exceptions

Let $\mathcal{R}$ be the composition of the eight lines over all segments, and let $\mathcal{Q}$ be the ideal map that XORs each selected bit of $\mathcal{X}$ into $\mathcal{W}$ and fixes everything else. They agree off $\mathcal{E}$, and both are bijections. $\mathcal{Q}$ preserves every guard, so it maps $\mathcal{E}$ onto itself. Then $\mathcal{R}$ maps the complement onto itself and hence $\mathcal{E}$ onto itself. So $\pi=\mathcal{Q}\mathcal{R}^{-1}$ fixes every address off $\mathcal{E}$ and permutes $\mathcal{E}$.

The procedure scans the [Stream](stream.md) of all $M$ records with a rank counter. Here $\operatorname{rank}(q)$ is the number of addresses before $q$ in stream order, counted from $0$. Each record at an address $q\in\mathcal{E}$ is removed, leaving a hole, and its destination $q'=\pi(q)$ is computed by reversing the eight lines with negated offsets and then applying the XORs. Since $\pi$ permutes $\mathcal{E}$, the destinations are distinct and fill exactly the holes.

Packed selected-bit addition computes the [Destination rank](destination-rank.md) of each extracted record: $\operatorname{rank}(q')=\operatorname{rank}(q)+\sum_h (q'_h-q_h)\sigma_h$, summed over the three fields $h$. Here $\sigma_h$ is the record stride of $h$. The procedure sorts the extracted records by a [Stable radix sort](stable-radix-sort.md) on these ranks. The keys are distinct, so one forward scan reinserts each record into its hole. Packed selected-bit addition is correct for every [Payload](payload.md) it carries, because records move whole.

The top selected bit is XORed by a separate step, since when $\rho>0$ its segment has no room for a guard above it. On two bits $e_1$ of $\mathcal{X}$ and $e_2$ of $\mathcal{W}$, the map $(e_1,e_2)\mapsto(e_1,\,e_1\oplus e_2)$ fixes $00$ and $01$ and swaps $10$ and $11$, so it XORs $e_1$ into $e_2$. <cite data-source="paper">Lemma 3 applies any fixed permutation to the two-bit value at two specified address</cite> positions in $O(V)$ time.

## Cost

Packed selected-bit addition exchanges its fields by the [Address-field interchange](address-interchange.md). Lemma 12 exchanges two disjoint <cite data-source="paper">address chunks of equal width L in O(V Lτ ) time</cite>, with $V=MR$. Each line first moves the target to the rightmost chunk position if needed, and moves it back. <cite data-source="paper">There are at most sixteen swaps and</cite> eight rotations, each costing $O(V)$. <cite data-source="paper">The movement costs O(V (Lτ + 1))</cite> in total.

The correction is one stream scan with $O(A_{\rm rect}^3)$ arithmetic per record, where $A_{\rm rect}=\lceil\log_2(2V)\rceil$ bounds every integer involved. Its radix sort makes at most $A_{\rm rect}$ passes over $\delta M$ records of $R+A_{\rm rect}$ bits, with $R$ the payload bits of a record. The total is

$$
O\bigl(V(L^{\tau}+1)+MA_{\rm rect}^3+\delta\,MA_{\rm rect}(R+A_{\rm rect})\bigr).
$$

Packed selected-bit addition has its bound stated along a [Family parameter](family-parameter.md) $p\to\infty$, the index of that family. There $A_{\rm rect}=O(p)$, $f\le p$, $K/\log p\to\infty$, and <cite data-source="paper">R exceeds every fixed polynomial in p</cite>. Dividing by $V=MR$ leaves $A_{\rm rect}^3/R$ and $\delta A_{\rm rect}(1+A_{\rm rect}/R)=O(p^2 2^{-K})(1+A_{\rm rect}/R)$. Both tend to zero, since $2^{-K}$ is smaller than every power of $p$. So the time is $O(V(L^{\tau}+1))$.
