Packed selected-bit addition XORs selected bits of an address chunk $x$ into chunk $y$, restoring a third chunk $z$ as scratch; the [simultaneous butterfly layer](simultaneous-layer.md) needs it for its binary changes of basis. Whole-chunk shifts are cheap on tapes, bit selection is not, so the XOR is done by additions on all selected bits at once, and the few addresses where one would carry are repaired.

Each address holds an $R$-bit record (not the scalar ring) and three chunks $x,y,z$ of $L=fK$ bits, with $K\ge6$ the segment spacing and $f$ the number of selected bits; other coordinates are spectators. Let $M$ count addresses, $V=MR$, and $A_{\rm rect}=\lceil\log_2(2V)\rceil$ bound counter lengths. The selected positions are $j_i=\rho+iK$, $0\le i<f$, $0\le\rho<K$; the goal is $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$.

For a control bit $c$ and integers $u,w$, $c[P]$ is $c$ if $P$ holds, else $0$. Perform in order
$$\begin{array}{llll}
(1)\ u\leftarrow u-c[w\bmod2=0] & (2)\ w\leftarrow w-c[u\bmod2=0] & (3)\ u\leftarrow u+c[w\bmod2=0] & (4)\ w\leftarrow w+c[u\bmod2=0]\\
(5)\ w\leftarrow w+c[u\bmod2=1] & (6)\ u\leftarrow u+c[w\bmod2=1] & (7)\ w\leftarrow w-c[u\bmod2=1] & (8)\ u\leftarrow u-c[w\bmod2=1]
\end{array}$$
For $c=1$, substituting the four parity pairs shows lines 1 to 4 permute the parities of $(u,w)$ by $(00\ 01\ 10)$ and lines 5 to 8 by $(01\ 10\ 11)$, composing to $(00\ 10)(01\ 11)$. So $(u',w')=(u+c(1-2(u\bmod2)),w)$: $u$ flips parity iff $c=1$, quotients by two persist, $w$ is restored. Each variable moves at most four.

Omit $j_{f-1}$ for now. For $0\le i<f-1$ the $K$ bits of $y$ from $j_i$ form a disjoint segment of value $u_i=2g_i+a_i$, and those of $z$ one of value $w_i=2h_i+b_i$, with bits $a_i,b_i$ and guard values $g_i,h_i\in\{0,\dots,2^{K-1}-1\}$. The control is $c_i=x_{j_i}$. Line (1) on all segments at once is
$$y\leftarrow y-\sum_{i=0}^{f-2}2^{j_i}[x_{j_i}=1][z_{j_i}=0]\pmod{2^L},$$
a cyclic shift of the whole chunk by an offset independent of the target, hence a bijection of addresses. Other lines vary sign, parity or roles of $y,z$. Let $S_0$ compose the eight.

Let $\mathcal B$, the exceptional addresses, be those where some guard $g$ (any $g_i$, $h_i$) fails $10\le g\le2^{K-1}-11$. Off $\mathcal B$ each segment lies in $[20,2^K-21]$, so displacement eight stays in $[0,2^K-1]$: no carry or borrow between segments, and $S_0$ equals the ideal map $T_0$ doing the XORs at $j_0,\dots,j_{f-2}$.

Exactly twenty values are excluded per guard <cite data-source="paper">There are exactly twenty excluded values for each guard in</cite>. At fixed spectator coordinates $y$ and $z$ range over all $2^L$ values, so each guard takes every value equally often and a fraction $20/2^{K-1}$ of addresses fail it. A union bound over $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$, $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, whatever the records hold.

$T_0$ keeps guards, so preserves $\mathcal B$; bijections agreeing off $\mathcal B$ give $S_0(\mathcal B^c)=T_0(\mathcal B^c)=\mathcal B^c$ and $S_0(\mathcal B)=\mathcal B$. After $S_0$, the record at $q$ came from $S_0^{-1}(q)$ and belongs at $q'=T_0S_0^{-1}(q)$, which fixes $\mathcal B^c$ and permutes $\mathcal B$.

Scan with a record-rank counter (stream position); dividing by the fixed field lengths gives the values of $x,y,z$ and their strides (records per unit step of a chunk). Extract the records of $\mathcal B$; compute $q'$ by undoing the eight shifts in reverse, then applying the XORs directly. Its rank is the current rank plus, per chunk, the signed value change times the stride. Attach this key and mark the vacated place, a hole. Stable radix sort by key touches only extracted records. As $q'$ permutes $\mathcal B$, keys are distinct and equal the holes' ranks, so one scan refilling holes in order applies $T_0$. Counters have $O(A_{\rm rect})$ bits, schoolbook operations cost $O(A_{\rm rect}^2)$, and $f\le A_{\rm rect}$ positions are handled: $O(A_{\rm rect}^3)$ per record. An [elementary stream operation](stream-ops.md) XORs $j_{f-1}$.

A rotation needs its target after its two control chunks, so swap it rightmost, rotate, and undo the swap: at most two swaps per rotation, so at most sixteen swaps and eight rotations <cite data-source="paper">There are at most sixteen swaps and eight rotations in $S_0$.</cite>. It rotates chunks by [Controlled shifts and rational scalings](controlled-shifts.md) in $O(V)$ time. It swaps chunks by [Fast address-chunk interchange](address-interchange.md) in $O(VL^\tau)$ time, fixed $\tau<1$.

Movement costs $O(V(L^\tau+1))$, scans $O(MA_{\rm rect}^3+V)$, and at most $A_{\rm rect}$ radix passes $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$: time $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$ <cite data-source="paper">With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, its time is</cite>. Per $V$ the extra terms are $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$, both $o(1)$ when $A_{\rm rect}=O(p)$, $R$ exceeds every polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$, so the cost is $O(V(L^\tau+1))$.
