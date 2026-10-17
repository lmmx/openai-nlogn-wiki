Packed selected-bit addition XORs selected bits of one address chunk into another, with a third chunk as restored scratch, using a constant number of cyclic shifts of whole chunks plus a repair of a few exceptional addresses; the [simultaneous butterfly layer](simultaneous-layer.md) needs it for its binary changes of basis.

Each address holds a record of $R$ bits ($R$ is not a scalar ring or row count). An address contains three chunks $x,y,z$ ($y$ is not the ring variable), each $L=fK$ bits wide ($L$ is not a dimension loss), where $f$ is the number of selected bits per chunk and $K\ge6$ their spacing ($K$ is not a tensor line). Let $M$ be the number of addresses (not a vertex matrix), $V=MR$ the total bits, and $A_{\rm rect}=\lceil\log_2(2V)\rceil$ a bound on counter lengths. The selected positions are $j_i=\rho+iK$ for $0\le i<f$, with $\rho$ an offset (not a role map). Other coordinates are spectators, and $q$ denotes an address (not a radix). The goal is $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ for all $i$.

## Eight parity-conditioned additions

Let $c\in\{0,1\}$ be a control bit (not a scaling integer), let $u,w$ be integers (not a DFT sequence, chunk width or wire index), and let $c[P]$ be $c$ if condition $P$ holds and $0$ otherwise. Perform in order
$$\begin{array}{llll}
(1)\ u\leftarrow u-c[w\bmod2=0] & (2)\ w\leftarrow w-c[u\bmod2=0] & (3)\ u\leftarrow u+c[w\bmod2=0] & (4)\ w\leftarrow w+c[u\bmod2=0]\\
(5)\ w\leftarrow w+c[u\bmod2=1] & (6)\ u\leftarrow u+c[w\bmod2=1] & (7)\ w\leftarrow w-c[u\bmod2=1] & (8)\ u\leftarrow u-c[w\bmod2=1]
\end{array}$$
For $c=1$, substituting the four parity pairs of $(u,w)$ shows that lines 1 to 4 permute them by the cycle $(00\ 01\ 10)$ and lines 5 to 8 by $(01\ 10\ 11)$, composing to $(00\ 10)(01\ 11)$, which flips the parity of $u$ and restores that of $w$. For example, $(u,w)=(4,6)$ becomes $(4,7)$ after line 4 and $(5,6)$ after line 8. So the output is $(u',w')=(u+c(1-2(u\bmod2)),w)$: $u$ flips parity exactly when $c=1$, both quotients by two are preserved, and the arbitrary integer $w$ is restored.

## Packing into chunks

Omit $j_{f-1}$ for now; it is XORed last by a linear scan. For $0\le i<f-1$ the $K$ bits of $y$ from position $j_i$ form a segment of value $u_i=2g_i+a_i$, and those of $z$ one of value $w_i=2h_i+b_i$, with $a_i,b_i\in\{0,1\}$. These segments are disjoint, and the guard values satisfy $g_i,h_i\in\{0,\dots,2^{K-1}-1\}$ ($g$ is a guard, not a gap). The control of the pair is $c_i=x_{j_i}$. Line (1) applied to all segments at once is
$$y\leftarrow y-\sum_{i=0}^{f-2}2^{j_i}[x_{j_i}=1][z_{j_i}=0]\pmod{2^L}.$$
The offset never depends on the target chunk $y$, so this is one cyclic shift of the whole chunk, a bijection of the addresses; the others vary sign, parity or roles. Let $S_0$ be the composition of the eight.

Let $\mathcal B$, the exceptional addresses, be those where some guard in $y$ or $z$ fails $10\le g\le2^{K-1}-11$. Away from $\mathcal B$ each segment lies in $[20,2^K-21]$, so even displacement eight stays inside $[0,2^K-1]$: no segment carries into or borrows from its neighbour, and $S_0$ equals the ideal map $T_0$ that performs the XORs at $j_0,\dots,j_{f-2}$.

There are exactly twenty excluded values for each guard <cite data-source="paper">There are exactly twenty excluded values for each guard in</cite>. At fixed spectator coordinates $y$ and $z$ range over all values, so each guard has the same distribution. A union bound over the $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, independently of record values.

## Repair

$T_0$ preserves guards, hence $\mathcal B$. Both $T_0$ and $S_0$ are bijections agreeing off $\mathcal B$, so $S_0(\mathcal B^c)=T_0(\mathcal B^c)=\mathcal B^c$ and $S_0(\mathcal B)=\mathcal B$. Thus $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$: a record at an exceptional address $q$ belongs at $q'=T_0S_0^{-1}(q)$.

The correction scans the stream, counting each record's rank (its index), recovers chunk values and strides (records per unit step of a chunk) by division, and extracts the records of $\mathcal B$. It computes $q'$ by undoing the eight additions and applying the XORs directly. The destination rank is the current rank plus, per chunk, the signed value change times the stride; it is attached as a key and the vacated place is marked as a hole. A stable radix sort touches only the extracted records. Since $T_0S_0^{-1}$ permutes $\mathcal B$, the keys are distinct and equal the ranks of the holes, so one forward scan reinserts the sorted records, implementing $T_0$ everywhere. Finally the omitted position $j_{f-1}$ is XORed in $O(V)$.

## Cost

A rotation needs its target after its controls: swap it rightmost, rotate, undo the swap. There are at most sixteen swaps and eight rotations in $S_0$ <cite data-source="paper">There are at most sixteen swaps and eight rotations in $S_0$.</cite>. Rotations use [Controlled shifts and rational scalings](controlled-shifts.md) in $O(V)$ time, and swaps use [Fast address-chunk interchange](address-interchange.md) in $O(VL^\tau)$ time, with $\tau<1$ fixed.

The movement costs $O(V(L^\tau+1))$ <cite data-source="paper">The movement costs $O(V(L^\tau+1))$.</cite>. A fixed number of record scans costs $O(MA_{\rm rect}^3+V)$ <cite data-source="paper">costs $O(MA_{\rm rect}^3+V)$, and the at most $A_{\rm rect}$ radix passes cost</cite>, since schoolbook arithmetic on $O(A_{\rm rect})$-bit counters costs $O(A_{\rm rect}^3)$ per record. The radix passes cost $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$ <cite data-source="paper">$O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$; skip them when the extracted bank is empty.</cite>. With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$ the time of the procedure is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$.

Dividing by $V$, the extra terms are $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. Under $A_{\rm rect}=O(p)$, $R$ above every polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$, the first tends to zero and the second is $o(1)$ <cite data-source="paper">the first tends to zero, and the second is</cite>, so the cost is $O(V(L^\tau+1))$.
