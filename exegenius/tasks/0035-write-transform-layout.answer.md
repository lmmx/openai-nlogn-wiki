The tape layout rearranges the address bits of a [synthetic polynomial transform](synthetic-transform.md) and turns each round into one [simultaneous butterfly layer](simultaneous-layer.md).

Let $\ell=\log_2 r$ be the number of address bits within a record. Coefficients are [fixed-point Gaussian dyadic records](fixed-point.md) with parts multiples of $2^{-p}$, where $p$ is the precision in bits. The $D=d-1$ axes have lengths $t_i\in\{2^{\ell-1},2^\ell\}$, where $d$ is a size parameter with $d\ell=O(p)$. $M$, the product of the $t_i$, is the number of records and $T=rM$ the number of complex coefficients. Chunks are $K$ bits wide, $1\le K\le\ell-1$. The fixed exponents $\tau,\lambda'<1$ are those of chunk interchange and the layer.

Outputs come in bit-reversal order $B$, which the pointwise product keeps. The layout permutation $L$, built below, adds one record permutation to the [retained frequency order](frequency-order.md): the forward entry with frequency address $j$ is stored at $L(Bj)$.

A layer needs the selected bits of all participating axes at a common offset in consecutive $K$-bit chunks <cite data-source="paper">we must place the selected bits of the participating axes at a common</cite>.

Call an axis long if it has $\ell$ address bits and short if $\ell-1$; put $b=(\ell-1)\bmod K$ and $q=\lfloor(\ell-1)/K\rfloor$. Move to a prefix the top bit of each long axis and the $b$ lowest bits of each axis. Each axis then keeps $q$ consecutive $K$-bit chunks. At most $D(b+1)=O(dK)$ slots move, so the moves cost $O(TpdK)$ <cite data-source="paper">listed slots, so the moves cost $O(TpdK)$.</cite>

Scanning target positions left to right, the layout exchanges chunks by the [fast address-chunk interchange](address-interchange.md), each costing $O(TpK^\tau)$, to group equal-index chunks. At most $Dq-1$ exchanges are needed, even for nonadjacent chunks <cite data-source="paper">exchanges of width-$K$ address chunks, even when the chunks are</cite>. Since $DqK\le d\ell=O(p)$, they cost $O(Tp\,pK^{\tau-1})$. These moves define $L$; reversing them gives $L^{-1}$.

A round on a chunk group is one simultaneous layer, so at most $\ell$ rounds cost $O(Tp\ell d^{\lambda'})$ <cite data-source="paper">$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total.</cite> At most $b+1\le K$ rounds on prefix slots, each $O(Tpd)$, cost $O(TpdK)$.

Each round applies a contraction $\mathcal H$ and a signed coefficient permutation $J_E$, then truncates with $Q_p$ toward zero. Truncation is odd and acts on each real and imaginary part, so $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$: one truncation per round, after the exact contraction. Each round adds less than $\sqrt2\,2^{-p}$, so from zero error at most $\ell$ rounds give error below $\sqrt2\,\ell\,2^{-p}$; $L$ is an isometry.

Conjugation by $L$ gives the exact forward operator $LBF_{\boldsymbol t}^-$ and the exact opposite operator $F_{\boldsymbol t}^+B^{-1}L^{-1}$.

Adding the costs, both procedures cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\,\ell\,2^{-p}$.
