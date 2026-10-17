Packed selected-bit addition XORs chosen bits of a chunk $x$ into chunk $y$ (chunks here), restoring a scratch chunk $z$; the [simultaneous butterfly layer](simultaneous-layer.md) on $d$ address chunks needs it.

Records have $R$ bits (a count here). A chunk has $L=fK$ bits, $K\ge6$; the $f$ selected bits lie at $j_i=\rho+iK$, $0\le i<f$, with offset $\rho<K$; the goal is $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$. Let $M$ count addresses, $V=MR$, and $A_{\rm rect}=\lceil\log_2(2V)\rceil$ bound counter lengths.

For a Boolean $c$ and integers $u,w$, $c[P]$ is $c$ if $P$ holds, else $0$. Do, in order:

$$\begin{array}{llll}
(1)\ u\leftarrow u-c[w\bmod2=0] & (2)\ w\leftarrow w-c[u\bmod2=0] & (3)\ u\leftarrow u+c[w\bmod2=0] & (4)\ w\leftarrow w+c[u\bmod2=0]\\
(5)\ w\leftarrow w+c[u\bmod2=1] & (6)\ u\leftarrow u+c[w\bmod2=1] & (7)\ w\leftarrow w-c[u\bmod2=1] & (8)\ u\leftarrow u-c[w\bmod2=1]
\end{array}$$

For $c=1$, substituting the four parity pairs shows the first four lines induce $(00\ 01\ 10)$ on the parities of $(u,w)$ and the last four induce $(01\ 10\ 11)$, composing to $(00\ 10)(01\ 11)$: it flips the parity of $u$ and restores $w$'s. So $(u',w')=(u+c(1-2(u\bmod2)),w)$, keeping quotients by two. Each variable is changed four times by at most one, so moves at most four, hence eight.

Omit $j_{f-1}$ first. For $0\le i<f-1$, the $K$ bits of $y$ from $j_i$ give a segment $u_i=2g_i+a_i$ and those of $z$ give $w_i=2h_i+b_i$, with bits $a_i,b_i$, guard values $g_i,h_i\in\{0,\dots,2^{K-1}-1\}$, and control $c_i=x_{j_i}$. Line (1) on all segments is
$$y\leftarrow y-\sum_{i=0}^{f-2}2^{j_i}[x_{j_i}=1][z_{j_i}=0]\pmod{2^L}.$$
Other lines vary the sign, tested parity or roles of $y,z$. Each is a cyclic shift of a whole chunk by an offset independent of the target chunk, hence a bijection of the addresses; $S_0$ composes the eight.

Let $\mathcal B$ (exceptional addresses) be those where a guard of $y$ or $z$ fails $10\le g\le2^{K-1}-11$. Off $\mathcal B$ each segment lies in $[20,2^K-21]$, so displacement eight stays in $[0,2^K-1]$: no segment carries into or borrows from a neighbour, and $S_0$ equals the ideal map $T_0$ XORing at $j_0,\dots,j_{f-2}$.

Ten values fall on each side of the interval ($2^{K-1}\ge32$): twenty per guard <cite data-source="paper">There are exactly twenty excluded values for each guard in</cite>. Guards are equidistributed at every spectator choice, so a union bound over $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$.

$T_0$ flips only the bits $a_i$, preserving guards and so $\mathcal B$. Two bijections agreeing off $\mathcal B$ give $S_0(\mathcal B^c)=T_0(\mathcal B^c)=\mathcal B^c$ and $S_0(\mathcal B)=\mathcal B$, so $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$.

A scan extracts records at $\mathcal B$, computing each destination $T_0S_0^{-1}$ by reversing the eight additions; its rank (current rank plus signed chunk differences times strides) is the key, and the vacated position is marked. As $T_0S_0^{-1}$ permutes $\mathcal B$, the keys are exactly the holes' ranks, so a stable radix sort and one scan refilling holes in order apply $T_0$. $j_{f-1}$ is then XORed by an [elementary stream operation](stream-ops.md), $O(V)$.

$S_0$ has at most eight rotations and sixteen swaps <cite data-source="paper">There are at most sixteen swaps and eight rotations in $S_0$.</cite>. A rotation is a [controlled shift](controlled-shifts.md) costing $O(V)$, a swap a [chunk interchange](address-interchange.md) costing $O(VL^\tau)$ for fixed exponent $\tau<1$. Schoolbook arithmetic on counters costs $O(A_{\rm rect}^3)$ per record; at most $A_{\rm rect}$ radix passes sort $|\mathcal B|$ records of $R+A_{\rm rect}$ bits. The time is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$ <cite data-source="paper">With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, its time is</cite>.

Per $V$ the extra terms are $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. With $p$ the precision bits, both vanish when $A_{\rm rect}=O(p)$, $R$ exceeds every polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$, so the cost is $O(V(L^\tau+1))$.
