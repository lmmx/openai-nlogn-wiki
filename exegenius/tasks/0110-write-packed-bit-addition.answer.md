Packed selected-bit addition XORs chosen bits of a chunk $x$ into chunk $y$ (chunk names, not the ring variable), restoring a scratch chunk $z$; the [simultaneous butterfly layer](simultaneous-layer.md) on $d$ axes needs it.

Records have $R$ bits (a bit count here). Chunks have $L=fK$ bits, with $K\ge6$ and $f$ the number of selected bits, at positions $j_i=\rho+iK$ for $0\le i<f$ with offset $\rho<K$; the goal is $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$. Let $M$ count addresses, $V=MR$, and $A_{\rm rect}=\lceil\log_2(2V)\rceil$ be the bit length of counters.

For a Boolean control $c$ and integers $u,w$, $c[P]$ means $c$ if the predicate $P$ holds, else $0$. Do these eight additions in order (congruences mod $2$):

$$\begin{array}{llll}
(1)\ u\leftarrow u-c[w\equiv0] & (2)\ w\leftarrow w-c[u\equiv0] & (3)\ u\leftarrow u+c[w\equiv0] & (4)\ w\leftarrow w+c[u\equiv0]\\
(5)\ w\leftarrow w+c[u\equiv1] & (6)\ u\leftarrow u+c[w\equiv1] & (7)\ w\leftarrow w-c[u\equiv1] & (8)\ u\leftarrow u-c[w\equiv1]
\end{array}$$

For $c=1$, substituting the four parity pairs shows lines (1)-(4) induce the cycle $(00\ 01\ 10)$ on the parities of $(u,w)$ and (5)-(8) induce $(01\ 10\ 11)$, composing to $(00\ 10)(01\ 11)$: it flips the parity of $u$ and restores $w$'s. So the complete output is $(u',w')=(u+c(1-2(u\bmod2)),w)$: $u$ keeps its quotient by two. Each variable changes four times by at most one, so moves at most four; eight suffices below.

Omit position $j_{f-1}$ for now. For $0\le i<f-1$, the $K$ bits of $y$ from $j_i$ form a segment $u_i=2g_i+a_i$, those of $z$ form $w_i=2h_i+b_i$, with bits $a_i,b_i$; the guard values satisfy $g_i,h_i\in\{0,\dots,2^{K-1}-1\}$, and the control is $c_i=x_{j_i}$. Line (1) on all segments at once is
$$y\leftarrow y-\sum_{i=0}^{f-2}2^{j_i}[x_{j_i}=1][z_{j_i}=0]\pmod{2^L}.$$
Other lines change sign and tested parity, or exchange $y,z$. Each line is thus a cyclic shift of a whole chunk by an offset independent of the target chunk, hence a bijection of the addresses. Let $S_0$ compose the eight.

Let $\mathcal B$, the exceptional addresses, be those where some guard in $y$ or $z$ fails $10\le g\le2^{K-1}-11$. Elsewhere each segment lies in $[20,2^K-21]$, so even displacement eight stays in $[0,2^K-1]$: no segment carries into or borrows from its neighbour, and $S_0$ equals the ideal map $T_0$ XORing at $j_0,\dots,j_{f-2}$.

Ten values lie below the interval and ten above, disjoint as $2^{K-1}\ge32$: twenty excluded values per guard <cite data-source="paper">There are exactly twenty excluded values for each guard in</cite>. Each guard has the same distribution at every spectator choice, so a union bound over the $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, whatever the records.

$T_0$ flips only the bits $a_i$, preserving guards and so $\mathcal B$. Two bijections agreeing off $\mathcal B$ give $S_0(\mathcal B^c)=T_0(\mathcal B^c)=\mathcal B^c$ and $S_0(\mathcal B)=\mathcal B$, so $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$.

A scan extracts the records at $\mathcal B$, computing each destination $T_0S_0^{-1}$ by reversing the eight additions. The destination's rank, the current rank plus signed chunk differences times strides, is the record's key; the vacated position is marked. Since $T_0S_0^{-1}$ permutes $\mathcal B$, the keys are exactly the ranks of the marked holes: a stable radix sort and one scan refilling holes in order apply $T_0$. Finally $j_{f-1}$ is XORed by an [elementary stream operation](stream-ops.md) in $O(V)$; for $f=1$ that is everything.

Movement uses at most eight rotations and sixteen swaps <cite data-source="paper">There are at most sixteen swaps and eight rotations in $S_0$.</cite>. Each rotation is a [controlled shift](controlled-shifts.md) costing $O(V)$, and each swap is a [chunk interchange](address-interchange.md) costing $O(VL^\tau)$ for fixed $\tau<1$. Schoolbook arithmetic on $O(A_{\rm rect})$-bit counters costs $O(A_{\rm rect}^3)$ per record; keys give at most $A_{\rm rect}$ radix passes over $|\mathcal B|$ records of $R+A_{\rm rect}$ bits. The time is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$ <cite data-source="paper">With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, its time is</cite>.

Dividing the extra terms by $V$ leaves $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. With $p$ the precision bits, both vanish when $A_{\rm rect}=O(p)$, $R$ exceeds every polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$, so the cost is $O(V(L^\tau+1))$.
