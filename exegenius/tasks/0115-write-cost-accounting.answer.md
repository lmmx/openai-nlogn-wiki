Cost accounting totals the running time of every step of [The multiplication algorithm](multiplication-algorithm.md) and shows that it is $O(n(\lg n)^{1-\kappa})$, where $\kappa=2^{-182}$ is the saved exponent.

Let $V=Tp=\Theta(n)$ be the volume: $T$ coefficients of $p$ bits each. Write $d$ for the number of axes, $K$ for the chunk width in bits, $\ell$ for the number of address bits of the longest axis, $\alpha$ for the Gaussian width and $t_i$ for the length of axis $i$. The fixed exponents of [Parameter and prime-length choice](parameter-choice.md) are $\epsilon=2^{-75}$, $c=2^{-56}$, $\delta=1/16$, $\tau=1-2^{-50}$ and $\lambda'=1-2^{-54}$, giving $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $\alpha=\Theta(p^{1/4+\epsilon/2})$.

Dividing each cost by $V$, seven operations dominate. Each is a power $p^{1-g_i}$ of $p$, where $g_i>0$ is its margin below one.

| Operation | Cost$/V$ | Power of $p$ | Margin |
|---|---|---|---|
| Prefix moves and single rounds | $dK$ | $\epsilon(1+c)$ | $g_1=1-\epsilon(1+c)$ |
| Chunk exchanges | $pK^{\tau-1}$ | $1-\epsilon c(1-\tau)$ | $g_2=\epsilon c(1-\tau)$ |
| Simultaneous rounds | $\ell d^{\lambda'}$ | $1-\epsilon(1-\lambda')$ | $g_3=\epsilon(1-\lambda')$ |
| Axis layouts | $d^2(1+\ell^\tau)$ | $\tau+\epsilon(2-\tau)$ | $g_4=1-\tau-\epsilon(2-\tau)$ |
| Gaussian lines | $dp^{1/2+\delta}\alpha$ | $3/4+\delta+3\epsilon/2$ | $g_5=1/4-\delta-3\epsilon/2$ |
| Chirps | $dp^\delta$ | $\epsilon+\delta$ | $g_6=1-\delta-\epsilon$ |
| Products | $\log(rp)$ | $1-\epsilon$ | $g_7=\epsilon$ |

Final scaling, input and output are smaller and absorbed. Each row follows from a lemma.

- Moving prefix slots (address fields placed ahead of each record) and single butterfly rounds are $O(dK)$ linear scans of the array, each costing $O(V)$, as in [Tape layout for synthetic transforms](transform-layout.md). This gives $dK=p^{\epsilon(1+c)}$.
- The layout needs $O(p/K)$ chunk exchanges, because $d\ell=O(p)$, and each costs $O(VK^\tau)$ by [Fast address-chunk interchange](address-interchange.md). The total is $O(p/K)K^\tau=O(pK^{\tau-1})$.
- Each of at most $\ell$ simultaneous rounds costs $O(Vd^{\lambda'})$ by [Simultaneous butterfly layer](simultaneous-layer.md).
- The [Chinese-remainder address map](crt-map.md) needs $O(d^2)$ adjacent axis moves. When two widths differ by one, peel the excess bit, exchange the equal-width parts by a chunk exchange of $O(V\ell^\tau)$, and restore the bit; each move costs $O(V(1+\ell^\tau))$ <cite data-source="paper">Each costs $O(V(1+\ell^\tau))$: peel a single excess bit when widths</cite>. Since $d^2\ell^\tau=p^{2\epsilon}p^{(1-\epsilon)\tau}$, the power is $\tau+\epsilon(2-\tau)$.
- In [Gaussian resampling](gaussian-resampling.md), axis $i$ has at most $T/t_i$ lines, each costing $O(t_ip^{3/2+\delta}\alpha)$. Summing over axes gives $O(dTp^{3/2+\delta}\alpha)$, which is $dp^{1/2+\delta}\alpha$ per unit volume.
- A chirp numerator of the [Bluestein chirp identity](chirp.md) has $O(p)$ bits and is a sum of $d$ terms. Squaring and multiplying them with the [Established O(n log n) multiplier](hvdh-multiplier.md), which takes $O(N\log 2N)$ for $N$-bit inputs, costs $O(dp^{1+\delta})$ per entry. An entry has $p$ bits, so the cost per unit volume is $dp^\delta$.
- The pointwise ring product has $T/r$ records. Each needs four integer products on $O(rp)$ bits after [Signed packing](signed-packing.md), using the same established multiplier on length $o(n)$, so the improved algorithm is not called. The total is $O(Tp\log(rp))$, and $\log(rp)=O(p^{1-\epsilon})$.

Substituting the rationals gives $g_1>1/2$, $g_2=2^{-75}2^{-56}2^{-50}=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$, so the smallest margin is $2^{-181}=2\kappa$ <cite data-source="paper">Thus $\min_i g_i=2^{-181}=2\kappa$.</cite>

Setup is separate. A visit is a node, round or group invocation of the recursions, which have constant branching and depth $O(\log p)$. Fix exponents $A$ and $C$ so that there are at most $p^A$ visits, each with setup of at most $p^C$ steps. The total $p^{A+C}$ is $o(Tp)$ <cite data-source="paper">costs at most $p^{A+C}=o(Tp)$.</cite> Per-record and per-line setup is $o(Tp)$ too, because $T\ge r$ and $r$ exceeds every fixed power of $p$. Exceptional addresses, where the packed shifts of [Packed selected-bit addition](packed-bit-addition.md) fail, are a fraction $O(d2^{-K})$ of all addresses and are repaired by sorting a compact stream. Summed over visits this costs $O(Vp^{O(1)}2^{-K})=o(V)$, since $K=\Theta(p^{\epsilon c})$ makes $2^{-K}$ smaller than any power of $p$. Global setup and prime search are also $o(V)$.

Each of the seven powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually. The total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ <cite data-source="paper">O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}).</cite> Schoolbook multiplication below a fixed cutoff is absorbed into the constant <cite data-source="paper">many smaller lengths are included by enlarging the implicit constant.</cite> So one machine runs in $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.

The exponent is only $2^{-182}$ below one because $g_2$ is a product of three small numbers: $\epsilon$ (few axes), $c$ (narrow chunks) and $1-\tau$ (the exchange beats a full pass only by $K^{-(1-\tau)}$). Taking the margin to be $2\kappa$ leaves room for the remaining powers of $\log p$.
