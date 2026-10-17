Packed selected-bit addition XORs selected bits of chunk $x$ into chunk $y$, using chunk $z$ as restored scratch; the [simultaneous butterfly layer](simultaneous-layer.md), acting on up to $d$ chunks, needs it for changes of basis.

Let $c$ be a Boolean control and $u,w$ integers; do these eight additions in order:

$$\begin{array}{cccc} u\mathrel{-}=c[w\%2=0] & w\mathrel{-}=c[u\%2=0] & u\mathrel{+}=c[w\%2=0] & w\mathrel{+}=c[u\%2=0]\\ w\mathrel{+}=c[u\%2=1] & u\mathrel{+}=c[w\%2=1] & w\mathrel{-}=c[u\%2=1] & u\mathrel{-}=c[w\%2=1]\end{array}$$

For $c=1$ the first four induce the cycle $(00\ 01\ 10)$ on the parities of $(u,w)$ and the last four induce $(01\ 10\ 11),$ so their composition is $(00\ 10)(01\ 11):$ it flips the parity of $u$ and restores $w.$ Tracing $(0,0),(0,1),(1,0),(1,1)$ gives $(1,0),(1,1),(0,0),(0,1),$ since predicates depend only on parities, so the complete output is $(u',w')=(u+c(1-2(u\%2)),w):$ $u$ keeps its quotient by two and $w$ is restored.

A chunk has $L=fK$ bits: $f$ selected bits spaced $K$ apart, at positions $j_i=\rho+iK.$ Let $M$ be the number of addresses, $R$ the bits per record, $V=MR$ the volume, and $A_{\rm rect}$ the bit length of counters, $\log_2(2V)$ rounded up. The packed map performs its rotations as [controlled shifts](controlled-shifts.md) costing $O(V).$ It swaps chunks using the [chunk interchange](address-interchange.md), costing $O(VL^\tau)$ for fixed $\tau<1.$

For $0\le i<f-1,$ the $K$ bits of $y$ from position $j_i$ form a segment $u_i=2g_i+a_i,$ and those of $z$ give $w_i=2h_i+b_i,$ with bits $a_i,b_i.$ The guard values satisfy $0\le g_i,h_i<2^{K-1},$ and the control is $c_i=x_{j_i}.$

One line on all segments is a cyclic shift of a whole chunk by an offset independent of the target chunk, hence a bijection of the rectangle. Let $S_0$ be the eight lines' composition. It uses at most sixteen swaps and eight rotations <cite data-source="paper">There are at most sixteen swaps and eight rotations in $S_0$.</cite>

Let $\mathcal B$ be the addresses where a guard of $y$ or $z$ fails $10\le g\le2^{K-1}-11.$ Elsewhere each segment lies in $[20,2^K-21],$ so displacement eight stays in $[0,2^K-1]$ and no segment carries into or borrows from its neighbour. Then $S_0$ equals the ideal XOR map $T_0.$

There are exactly twenty excluded values for each guard among $2^{K-1}.$ A union bound over the $2(f-1)$ guards, with the same guard distribution at every choice of other coordinates, bounds the bad addresses. Hence $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\},$ whatever the records.

Both $T_0$ and $S_0$ are bijections agreeing off $\mathcal B,$ and $T_0$ preserves $\mathcal B,$ so $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B.$

The repair extracts the records at $\mathcal B$ with destination-rank keys, stably radix-sorts them, and reinserts them in one scan. The keys are distinct because $T_0S_0^{-1}$ permutes $\mathcal B.$

The time is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect})):$ movement costs $O(V(L^\tau+1)),$ record scans $O(MA_{\rm rect}^3+V),$ radix passes $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect})).$ With coefficient precision $p,$ dividing the extra terms by $V$ gives $A_{\rm rect}^3/R\to0$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)=o(1)$ when $A_{\rm rect}=O(p),$ $R$ exceeds every polynomial in $p,$ $f\le d\le p$ and $K/\log p\to\infty.$ So the cost is $O(V(L^\tau+1)).$
