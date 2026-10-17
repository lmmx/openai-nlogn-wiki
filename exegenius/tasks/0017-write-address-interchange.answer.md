Fast address-chunk interchange swaps two disjoint $u$-bit address fields of an array with $V$ entries (volume) in time $O(Vu^\tau)$ <cite data-source="paper">Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$.</cite>, with $\tau=1-2^{-50}$ fixed.

With radix-$q$ digits, $q$ a fixed prime, let $H,D$ be the chunk values. Then $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ sends $(H,D)$ to $(D,H)$; only the middle shear needs the network.

Let chunks have $e=m^k$ digits ($m$ fields, $k$ levels), each field $b=e/m$ digits, so $H,D$ are vectors over $\mathbb Z/q^b\mathbb Z$. Each shear is performed by [Matrix shear by triangular factorization](matrix-shear.md): rank $\alpha$ costs $\alpha$ interchanges of $b$-digit fields <cite data-source="paper">An edge matrix of rank $a$ will require $a$ smaller interchanges.</cite>. The [exchange network](exchange-network.md) has $W$ wires and edge matrices $A_\epsilon$ of total rank $s<Wm$ (a [rank deficit](subspace-labels.md)), with $s/W<m^\tau$.

Split whole rows cyclically into $W$ role streams within each prefix; row $r=Wg+(w-1)$ goes to stream $w$ as row $g$. Each stream has volume $V/W$ and row count divisible by $W^{k-1}$; streams are split and merged by [stream scans](stream-ops.md).

A [frame](array-frames.md) at a vertex with matrix $M$ is the address permutation $\Phi_M$, $(H,D)\mapsto(H+MD,D)$; edges change it by $\Phi_{M'-M}$, and a common address permutation commutes with every pointwise bit gate. Each edge applies $\Phi_{A_\epsilon}$ to its role stream as above.

By the endpoint contract the physical output is $f'_{\sigma(w)}=\Phi_{M_{\mathrm{out}(\sigma(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$ ($f_w$ is wire $w$'s input, $\sigma(w)$ its role, $M_{\mathrm{in}(w)},M_{\mathrm{out}(\sigma(w))}$ the frame matrices). Merging rows back undoes $\sigma$; so $H\gets H+D$ holds on every original row, scratch rows included.

The calls number exactly $s$, the sum of the edge ranks <cite data-source="paper">The number of recursive calls is the sum of the edge ranks, exactly $s$.</cite>, each on volume $V/W$; other work costs $O(V)$. With $F_k$ the bound on time per unit volume at width $m^k$, $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$, so it satisfies the recurrence of [Recursive power saving](rank-recurrence.md).

Then $F_k=O(\sum_{j=0}^k a^j)$, $a=s/W<m^\tau$. If $a\le1$, the sum is at most $k+1=O(m^{k\tau})$. If $a>1$, it is $O(a^k)$ with $a^k<m^{k\tau}$. So $F_k=O(e^\tau)$. Only rank deficit saves, so $\tau$ is barely below $1$.

In general the permutation is $(p,h,g,d,z)\mapsto(p,d,g,h,z)$ (prefix $p$, chunks $h,d$, gap $g$, suffix $z$), one-bit payloads included <cite data-source="paper">In particular, $B=1$ is allowed.</cite>. Put $k=\lceil\log_m e\rceil$ (a new meaning) and $\rho=\lceil k\log W/(2\log q)\rceil$, so $q^{2\rho}\ge W^k$. Interchange and join the top $\rho$ digits: the high parts form a row field of range $R=q^{2\rho}\ge W^k$ before both remaining chunks. Pad with zero rows to $R'=W^k\lceil R/W^k\rceil<2R$ rows.

Write $e-\rho=\sum_{j=0}^k a_jm^j$, $0\le a_j<m$, and interchange corresponding pieces ($a_j$ pieces of width $m^j$) by the power-width case. The cost $O(V)\sum_j a_jm^{j\tau}=O(Ve^\tau)$ is geometric since $a_j<m$ and $m^k<me$. Padding $[2^u]$ to $[q^e]$ costs a fixed factor and gives $O(Vu^\tau)$ <cite data-source="paper">Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$.</cite>.
