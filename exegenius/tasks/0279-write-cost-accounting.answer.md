Cost accounting totals the running time of every operation of [The multiplication algorithm](multiplication-algorithm.md) and shows that it is $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$, which is the main result.

Let $V=Tp=\Theta(n)$ be the volume, the number of stored bits of $T$ coefficients of $p$ bits (here $V$ is a volume, not a label). Since $p=\Theta(\log n)$, a bound $O(V p^{1-\kappa})$ is the target. The fixed rational parameters of [Parameter and prime-length choice](parameter-choice.md) are $\epsilon=2^{-75}$, $c=2^{-56}$, $\delta=1/16$, $\tau=1-2^{-50}$ and $\lambda'=1-2^{-54}$. They give the sizes $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $\alpha=\Theta(p^{1/4+\epsilon/2})$. Dividing a cost by $V$ turns it into a power of $p$, so costs are compared by their exponents.

Dividing by $V$, seven operations dominate, each costing $p^{1-g_i}$, where $g_i>0$ is its margin below one (not a guard value).

| Operation | Cost$/V$ | Power of $p$ | Margin |
|---|---|---|---|
| Prefix moves, single rounds | $dK$ | $\epsilon(1+c)$ | $g_1=1-\epsilon(1+c)$ |
| Chunk exchanges | $pK^{\tau-1}$ | $1-\epsilon c(1-\tau)$ | $g_2=\epsilon c(1-\tau)$ |
| Simultaneous rounds | $\ell d^{\lambda'}$ | $1-\epsilon(1-\lambda')$ | $g_3=\epsilon(1-\lambda')$ |
| Axis layouts | $d^2(1+\ell^\tau)$ | $\tau+\epsilon(2-\tau)$ | $g_4=1-\tau-\epsilon(2-\tau)$ |
| Gaussian lines | $dp^{1/2+\delta}\alpha$ | $3/4+\delta+3\epsilon/2$ | $g_5=1/4-\delta-3\epsilon/2$ |
| Chirps | $dp^\delta$ | $\epsilon+\delta$ | $g_6=1-\delta-\epsilon$ |
| Products | $\log(rp)$ | $1-\epsilon$ | $g_7=\epsilon$ |

Final scaling and rounding cost $p^\delta$, and input, padding, carries and output cost $1$, so both are absorbed by the rows above.

## Where each row comes from

Prefix moves and single butterfly rounds are $O(d K)$ linear scans, each $O(V)$, in [Tape layout for synthetic transforms](transform-layout.md). That layout needs $O(p/K)$ chunk exchanges, because $d\ell=O(p)$, and each costs $O(VK^\tau)$ by [Fast address-chunk interchange](address-interchange.md), so the total is $O(p/K)K^\tau=O(pK^{\tau-1})$ per unit volume. Its at most $\ell$ simultaneous rounds each cost $O(Vd^{\lambda'})$ by [Simultaneous butterfly layer](simultaneous-layer.md). The [Chinese-remainder address map](crt-map.md) needs $O(d^2)$ adjacent axis moves, each costing $O(V(1+\ell^\tau))$, and $d^2\ell^\tau=p^{2\epsilon}p^{(1-\epsilon)\tau}$. In [Gaussian resampling](gaussian-resampling.md), axis $i$ has at most $T/t_i$ lines of cost $O(t_ip^{3/2+\delta}\alpha)$, which sum to $O(dTp^{3/2+\delta}\alpha)$. A chirp numerator of the [Bluestein chirp identity](chirp.md) has $O(p)$ bits and sums $d$ terms. The [Established O(n log n) multiplier](hvdh-multiplier.md) forms the squares and products in $O(dp^{1+\delta})$ per entry, which is $dp^\delta$ per bit. Finally the $T/r$ records of the pointwise ring product each need four products on $O(rp)$ bits after [Signed packing](signed-packing.md). This gives $O(Tp\log(rp))$ in total, with $\log(rp)=O(p^{1-\epsilon})$ since $\log r=\ell$. These calls use the established multiplier on records of length $o(n)$, not the algorithm being built.

## Margins

Substituting the parameters gives $g_1>1/2$, $g_2=2^{-75}2^{-56}2^{-50}=2^{-181}$, $g_3=2^{-75}2^{-54}=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$. The least is $2^{-181}=2\kappa$ <cite data-source="paper">Thus $\min_i g_i=2^{-181}=2\kappa$.</cite>

This margin is that small because $g_2$ is a product of three small numbers: $\epsilon$ (few axes, so few chunk exchanges per axis), $c$ (narrow chunks, $K=p^{\epsilon c}$) and $1-\tau$ (one exchange of width $K$ saves only the factor $K^{-(1-\tau)}$). Doubling the minimum margin leaves room for any remaining fixed power of $\log p$ <cite data-source="paper">This explicit slack will cover</cite>.

## Setup is negligible

A visit is a node of the layer or address-layout recursions, or one round or group invocation inside them. These recursions have constant branching, depth $O(\log p)$ and polynomially many rounds. Fix a visit exponent $A$ (not a matrix or space of earlier pages) so that the total number of visits is at most $p^A$, and a setup exponent $C$ so that descriptor setup per visit takes at most $p^C$ steps. Setup then costs at most $p^{A+C}=o(Tp)$. Setup repeated for each record or line is a fixed power of $p$ for each of about $T/r$ items, and $r$ exceeds every fixed power of $p$, so it is also $o(Tp)$. Exceptional addresses, where the packed shifts of [Packed selected-bit addition](packed-bit-addition.md) fail, are a fraction $O(d2^{-K})$ of all addresses. Let $V_{\rm call}$ be the volume of one packed change of basis. Its compact stream of exceptional records has length $O\left(\frac{V_{\rm call}}{rp}d2^{-K}(rp+p)\right)=O(V_{\rm call}d2^{-K})$. Stable bit sorting makes $O(p)$ scans of this stream. Over at most $p^A$ visits and with $d=O(p^\epsilon)$, the repair costs $O(Vp^{O(1)}2^{-K})=o(V)$, because $K=\Theta(p^{\epsilon c})$ beats every power of $p$. Global setup and the prime search for the axis lengths are likewise $o(V)$.

## Total

Each of the seven powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually. The total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ <cite data-source="paper">O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}).</cite> Use schoolbook multiplication below a fixed cutoff beyond all the size and precision conditions. The finitely many smaller lengths then only enlarge the constant <cite data-source="paper">many smaller lengths are included by enlarging the implicit constant.</cite> One machine therefore runs in $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.
