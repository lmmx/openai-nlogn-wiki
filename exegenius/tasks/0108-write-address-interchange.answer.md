Fast address-chunk interchange swaps two disjoint $u$-bit address fields of a bit array of $V$ stored bits (the volume) in $O(Vu^\tau)$ time on a fixed number of tapes <cite data-source="paper">Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$.</cite>, with $\tau=1-2^{-50}$. It is one of the two tape primitives whose power saving the main result needs. The result is an exact permutation, yet intermediate steps XOR data together, so it is performed by a circuit.

An address is $(p,h,g,d,z)$: prefix $p$, chunks $h$ and $d$, gap $g$, suffix $z$. The goal is $(p,h,g,d,z)\mapsto(p,d,g,h,z)$. Letters reused from earlier pages ($p,h,d,k,b,R$) change meaning here. Digits are radix $q$, a fixed prime.

## Reduction to a shear

Let $H,D$ be the values of the chunks. The updates $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ send $(H,D)$ to $(H,D-H)$, then $(D,D-H)$, then $(D,H)$. Only the middle shear $H\gets H+D$ needs the circuit; the others are linear scans.

## Chunks of $e=m^k$ digits

Here $e$ is the number of digits per chunk and $k$ the number of levels. Cut each chunk into $m$ fields of $b=e/m$ digits, so $H,D$ are vectors over $\mathbb Z/q^b\mathbb Z$. The [exchange network](exchange-network.md) has $W$ wires. Each terminal and gate carries a rational $m\times m$ matrix $M$, and edge $i$ carries $A_i=M_{\mathrm{head}(i)}-M_{\mathrm{tail}(i)}$. Put $s=\sum_i\operatorname{rank}A_i$. The shear contract says wire $w$ ends at output role $\rho(w)$ with $M_{\mathrm{out}(\rho(w))}-M_{\mathrm{in}(w)}=I_m$ ($I_m$ the identity), and $s<Wm$ (a [rank deficit](subspace-labels.md)); take $\tau$ with $s/W<m^\tau$.

Let $\Phi_M$ move the entry at address $(H,D)$ to $(H+MD,D)$. Added matrices add, so $\Phi_{M'}\Phi_M=\Phi_{M'+M}$ and $\Phi_{-M}$ is the inverse. The [frame](array-frames.md) at a vertex with matrix $M$ is $\Phi_M$; an edge to a vertex with matrix $M'$ changes it by $\Phi_{M'-M}=\Phi_{A_i}$. A common address permutation commutes with every pointwise bit gate, so gates run unchanged. Each edge shear is performed by [Matrix shear by triangular factorization](matrix-shear.md): rank $a$ costs $a$ interchanges of $b$-digit fields <cite data-source="paper">An edge matrix of rank $a$ will require $a$ smaller interchanges.</cite>.

Suppose a row field ahead of both chunks has length divisible by $W^k$. Within each prefix, row $Wx+w-1$ goes to role stream $w$ as row $x$, by [stream scans](stream-ops.md). Each stream has volume $V/W$ and row count divisible by $W^{k-1}$, the hypothesis for the smaller interchanges.

Wire $w$'s physical input $f_w$ is read as the logical array $\Phi_{-M_{\mathrm{in}(w)}}f_w$, with no tape work. Its physical output $f'_{\rho(w)}$ is $\Phi_{M_{\mathrm{out}(\rho(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$, by the composition rule and the contract. Merging rows back undoes $\rho$, so $H\gets H+D$ holds on every original row, scratch rows included.

There are exactly $s$ smaller calls <cite data-source="paper">The number of recursive calls is the sum of the edge ranks, exactly $s$.</cite>, each on volume $V/W$. Splitting, merging, gates and scheduling move $O(V)$ symbols at the node <cite data-source="paper">Each push, pop, copy, positioning operation, or erasure moves $O(V)$ symbols at a parent node.</cite>. With $F_k$ the time per unit volume at width $m^k$, $F_0=O(1)$ and $F_k\le(s/W)F_{k-1}+O(1)$, the recurrence of [Recursive power saving](rank-recurrence.md), which gives a power saving. Unrolling, $F_k=O(\sum_{j=0}^k (s/W)^j)$. If $s/W\le1$ the sum is at most $k+1=O(m^{k\tau})$. If $s/W>1$ it is $O((s/W)^k)$, below $m^{k\tau}$. Hence $F_k=O(e^\tau)$. Since $s$ is only a few rank units below $Wm$, $s/W$ is barely below $m$, and so $\tau$ is barely below $1$.

## Arbitrary width

Small $e$ are handled by $e$ single-digit interchanges. For large $e$, put $k'=\lceil\log_m e\rceil$ and $\nu=\lceil k'\log W/(2\log q)\rceil$, so $q^{2\nu}\ge W^{k'}$, $1\le\nu<e$ and $\nu=O(\log 2e)$. Write each chunk as its top $\nu$ digits and the rest, $h^+,h^-$ and $d^+,d^-$. Interchange the high digits one pair at a time and move $h^+$ next to $d^+$: the order $(h^+,h^-,g,d^+,d^-)$ becomes $(d^+,h^+,h^-,g,d^-)$. Now $d^+,h^+$ form a row field of range $R=q^{2\nu}\ge W^{k'}$ before both remaining chunks. Pad with zero rows, within each prefix, to $R'=W^{k'}\lceil R/W^{k'}\rceil<2R$ rows, so the volume stays below $2V$ and the row count is divisible by every needed $W^j$.

Write $e-\nu=\sum_{j=0}^{k'}a_jm^j$ with $0\le a_j<m$. Split each remaining chunk into $a_j$ consecutive pieces of width $m^j$ and interchange corresponding pieces by the power-width case, all with the same row field. The total is $O(V)\sum_ja_jm^{j\tau}=O(Ve^\tau)$, a geometric sum since $a_j<m$ and $m^{k'}<me$. This gives $(d^+,h^+,d^-,g,h^-)$. Scan away the padded rows and reverse the joining move, giving $(d^+,d^-,g,h^+,h^-)$. That movement costs $O(V\nu)=O(Ve^\tau)$.

For $u$-bit chunks, pad the range $[2^u]$ to $[q^e]$ with the least $e$ having $q^e\ge2^u$, a volume factor below $q^2$, and scan the padding away afterwards. Since $e=O(u)$, the cost is $O(Vu^\tau)$ <cite data-source="paper">Since $e=O(u)$ for fixed $q$, the bound is $O(Vu^\tau)$.</cite>, including one-bit payloads.
