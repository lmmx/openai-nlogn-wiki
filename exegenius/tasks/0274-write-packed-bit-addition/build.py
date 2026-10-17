import json,re
body = r'''Packed selected-bit addition XORs selected bits of an address chunk $x$ into chunk $y$, restoring a scratch chunk $z$, using shifts of whole chunks plus a repair of few exceptional addresses; the [simultaneous butterfly layer](simultaneous-layer.md) needs it for its binary changes of basis.

For a control bit $c$ (not a scaling integer) and integers $u,w$ (not a DFT sequence, a chunk width or a wire index), $c[P]$ is $c$ if $P$ holds, else $0$. Perform in order
$$\begin{array}{llll}
(1)\ u\leftarrow u-c[w\bmod2=0] & (2)\ w\leftarrow w-c[u\bmod2=0] & (3)\ u\leftarrow u+c[w\bmod2=0] & (4)\ w\leftarrow w+c[u\bmod2=0]\\
(5)\ w\leftarrow w+c[u\bmod2=1] & (6)\ u\leftarrow u+c[w\bmod2=1] & (7)\ w\leftarrow w-c[u\bmod2=1] & (8)\ u\leftarrow u-c[w\bmod2=1]
\end{array}$$
For $c=1$, substituting the four parity pairs shows lines 1 to 4 permute the parities of $(u,w)$ by $(00\ 01\ 10)$ and lines 5 to 8 by $(01\ 10\ 11)$, composing to $(00\ 10)(01\ 11)$. So $(u',w')=(u+c(1-2(u\bmod2)),w)$: $u$ flips parity iff $c=1$, quotients by two persist, $w$ is restored. Each variable moves at most four.

Each address holds an $R$-bit record ($R$ is neither the scalar ring nor a row count) and three chunks $x,y,z$ ($y$ is not the ring variable) of $L=fK$ bits ($L$ is not a dimension loss), with $K\ge6$ the segment spacing ($K$ is not a tensor line) and $f$ the number of selected bits; other coordinates are spectators. Let $M$ count addresses ($M$ is not a vertex matrix), $V=MR$, and $A_{\rm rect}=\lceil\log_2(2V)\rceil$ bound counter lengths. Selected positions are $j_i=\rho+iK$, $0\le i<f$, with offset $0\le\rho<K$ ($\rho$ is not a role map); the goal is $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$.

Omit $j_{f-1}$, XORed last by a linear scan. For $0\le i<f-1$ the $K$ bits of $y$ from $j_i$ form a disjoint segment of value $u_i=2g_i+a_i$, and those of $z$ one of value $w_i=2h_i+b_i$, with bits $a_i,b_i$ and guard values $g_i,h_i\in\{0,\dots,2^{K-1}-1\}$, written $g$ for either ($g$ is a guard, not a gap). The control is $c_i=x_{j_i}$. Line (1) on all segments at once is
$$y\leftarrow y-\sum_{i=0}^{f-2}2^{j_i}[x_{j_i}=1][z_{j_i}=0]\pmod{2^L},$$
a cyclic shift of the whole chunk $y$ by an offset independent of $y$, hence a bijection of addresses. The others vary sign, parity or roles. Let $S_0$ compose the eight.

Let $\mathcal B$, the exceptional addresses, be those where some guard fails $10\le g\le2^{K-1}-11$. Off $\mathcal B$ each segment lies in $[20,2^K-21]$, so displacement eight stays in $[0,2^K-1]$: no carry or borrow between segments, so $S_0$ equals the ideal map $T_0$ doing the XORs at $j_0,\dots,j_{f-2}$.

Ten values are excluded at each end, twenty per guard <cite data-source="paper">There are exactly twenty excluded values for each guard in</cite>. At fixed spectator coordinates $y$ and $z$ range over all $2^L$ values, so each guard takes every value equally often and a fraction $20/2^{K-1}$ fail it. A union bound over the $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$, $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$.

$T_0$ preserves guards, hence $\mathcal B$; bijections agreeing off $\mathcal B$ give $S_0(\mathcal B^c)=T_0(\mathcal B^c)=\mathcal B^c$ and $S_0(\mathcal B)=\mathcal B$. After $S_0$, the record at address $q$ ($q$ is not a radix or sequence length) came from $S_0^{-1}(q)$ and belongs at $q'=T_0S_0^{-1}(q)$, which fixes $\mathcal B^c$ and permutes $\mathcal B$.

Scan, counting each record's rank (stream index); dividing by the fixed field lengths gives the values of $x,y,z$ and their strides (records per unit step). Extract the records of $\mathcal B$ and compute $q'$ by undoing the eight shifts in reverse, then applying the XORs directly. The destination's rank is the current rank plus, per chunk, the signed value change times the stride. Attach it as a key; mark the vacated place, a hole. Stable radix sort touches only extracted records. As $q'$ permutes $\mathcal B$, keys are distinct and equal the holes' ranks, so one scan refilling holes in order applies $T_0$. Counters have $O(A_{\rm rect})$ bits and schoolbook operations cost $O(A_{\rm rect}^2)$ each, over $f\le A_{\rm rect}$ positions: $O(A_{\rm rect}^3)$ per record.

A rotation needs its target after its controls: swap it rightmost, rotate, undo the swap. That is at most sixteen swaps and eight rotations <cite data-source="paper">There are at most sixteen swaps and eight rotations in $S_0$.</cite>. It rotates chunks by [Controlled shifts and rational scalings](controlled-shifts.md) in $O(V)$ time and swaps by [Fast address-chunk interchange](address-interchange.md) in $O(VL^\tau)$, for $\tau<1$.

Movement costs $O(V(L^\tau+1))$ <cite data-source="paper">The movement costs $O(V(L^\tau+1))$.</cite>. Scans cost $O(MA_{\rm rect}^3+V)$ <cite data-source="paper">costs $O(MA_{\rm rect}^3+V)$, and the at most $A_{\rm rect}$ radix passes cost</cite>, and radix passes $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$ <cite data-source="paper">$O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$; skip them when the extracted bank is empty.</cite>, so the time is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$ <cite data-source="paper">With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, its time is</cite>. Per $V$ the extra terms are $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$, both tending to zero when $A_{\rm rect}=O(p)$, $R$ exceeds every polynomial in $p$, $f\le d\le p$, $K/\log p\to\infty$; the cost is $O(V(L^\tau+1))$.
'''
open('/home/user/e2e-run/exegenius/tasks/0274-write-packed-bit-addition.answer.md','w').write(body)
t=body
def S(a,b=None):
    i=t.index(a)
    if b is None: return a
    j=t.index(b,i)+len(b)
    return t[i:j]
ders=[
("S1.6.3.1",S("so the time is $O(V(L^\\tau+1)+MA_{\\rm rect}^3+","(R+A_{\\rm rect}))$")),
("S1.6.3.2",S("For $c=1$, substituting","$(00\\ 10)(01\\ 11)$.")),
("S1.6.3.3",S("So $(u',w')=","is restored.")),
("S1.6.3.4",S("with bits $a_i,b_i$ and guard values","for either")),
("S1.6.3.5",S("a cyclic shift of the whole chunk","bijection of addresses.")),
("S1.6.3.6",S("Off $\\mathcal B$ each segment","$j_0,\\dots,j_{f-2}$.")),
("S1.6.3.7",S("Ten values are excluded at each end, twenty per guard")),
("S1.6.3.8",S("so each guard takes every value equally often","A union bound over the $2(f-1)$ guards gives")),
("S1.6.3.9",S("A union bound over the $2(f-1)$ guards gives","\\min\\{1,80(f-1)2^{-K}\\}$.")),
("S1.6.3.10",S("$T_0$ preserves guards","permutes $\\mathcal B$.")),
("S1.6.3.11",S("A rotation needs its target","eight rotations")),
("S1.6.3.12",S("The destination's rank is","applies $T_0$.")),
("S1.6.3.13",S("Movement costs $O(V(L^\\tau+1))$")),
("S1.6.3.14",S("Per $V$ the extra terms are","$O(V(L^\\tau+1))$.")),
]
sym=lambda s,n,m,r,q:{"symbol":s,"name":n,"meaning":m,"relation":r,"quote":q}
rel=[
{"prerequisite":"controlled-shifts","predicate":"rotates chunks by","quote":S("It rotates chunks by [Controlled shifts","for $\\tau<1$.")},
{"prerequisite":"address-interchange","predicate":"swaps by","quote":S("It rotates chunks by [Controlled shifts","for $\\tau<1$.")},
]
json.dump({"symbols":[],"relations":rel,"derivations":[{"step":a,"quote":b} for a,b in ders]},open('/home/user/e2e-run/exegenius/tasks/0274-write-packed-bit-addition.answer.json','w'),indent=1)
u=re.sub(r'<cite.*?</cite>','',body,flags=re.S);u=re.sub(r'\$\$.*?\$\$','',u,flags=re.S);u=re.sub(r'\$.*?\$','',u)
print(len(u.split()))
