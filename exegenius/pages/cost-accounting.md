Cost accounting totals the running time of every step of [The multiplication algorithm](multiplication-algorithm.md) and shows that it is $O(n(\lg n)^{1-\kappa})$, where $\kappa=2^{-182}$ is the saved exponent.

Let $T$ be the number of coefficients in the array, $p$ the precision in bits per coefficient, and $V=Tp=\Theta(n)$ the volume. Here $d$ is the number of transform axes, $K$ the width of an exchanged address chunk, $\ell=\log_2 r$ the number of address bits of a record, $\alpha$ the Gaussian window width, and $t_i$ the length of axis $i$. The fixed exponents of [Parameter and prime-length choice](parameter-choice.md) are $\epsilon=2^{-75}$, $c=2^{-56}$, $\delta=1/16$, $\tau=1-2^{-50}$ and $\lambda'=1-2^{-54}$, giving $d=\Theta(p^\epsilon)$, $K=\Theta(p^{\epsilon c})$, $\ell=\Theta(p^{1-\epsilon})$ and $\alpha=\Theta(p^{1/4+\epsilon/2})$.

Dividing by $V$ and substituting these sizes makes each normalized cost a power $p^{1-g_i}$ with margin $g_i$ below one. Seven dominate.

| Operation | Cost$/V$ | Power of $p$ | Margin |
|---|---|---|---|
| Prefix moves | $dK$ | $\epsilon(1+c)$ | $g_1=1-\epsilon(1+c)$ |
| Chunk exchanges | $pK^{\tau-1}$ | $1-\epsilon c(1-\tau)$ | $g_2=\epsilon c(1-\tau)$ |
| Simultaneous rounds | $\ell d^{\lambda'}$ | $1-\epsilon(1-\lambda')$ | $g_3=\epsilon(1-\lambda')$ |
| Axis layouts | $d^2(1+\ell^\tau)$ | $\tau+\epsilon(2-\tau)$ | $g_4=1-\tau-\epsilon(2-\tau)$ |
| Gaussian lines | $dp^{1/2+\delta}\alpha$ | $3/4+\delta+3\epsilon/2$ | $g_5=1/4-\delta-3\epsilon/2$ |
| Chirps | $dp^\delta$ | $\epsilon+\delta$ | $g_6=1-\delta-\epsilon$ |
| Products | $\log(rp)$ | $1-\epsilon$ | $g_7=\epsilon$ |

Substituting the fixed rationals gives $g_1>1/2$, $g_2=2^{-75}2^{-56}2^{-50}=2^{-181}$, $g_3=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$, so the smallest margin is $2^{-181}=2\kappa$ <cite data-source="paper">Thus $\min_i g_i=2^{-181}=2\kappa$.</cite> This slack covers any fixed power of $\log p$.

The layout needs $O(p/K)$ chunk exchanges, since $d\ell=O(p)$, each cost bounded by $O(VK^\tau)$ in [Fast address-chunk interchange](address-interchange.md), so the normalized total is $O(p/K)K^\tau=O(pK^{\tau-1})$. Each of at most $\ell$ rounds is bounded by $O(Vd^{\lambda'})$ in [Simultaneous butterfly layer](simultaneous-layer.md). [Gaussian resampling](gaussian-resampling.md) handles at most $T/t_i$ lines on axis $i$, each costing $O(t_ip^{3/2+\delta}\alpha)$, totalling $O(dTp^{3/2+\delta}\alpha)$. The $T/r$ ring-product records need integer products on $O(rp)$ bits, $O(Tp\log(rp))$ in total.

Fixed exponents $A$ and $C$ bound the recursion visits by $p^A$ and the setup per visit by $p^C$, so the total is small <cite data-source="paper">costs at most $p^{A+C}=o(Tp)$.</cite> Repairing the fraction $O(d2^{-K})$ of exceptional addresses costs $o(V)$ since $K=\Theta(p^{\epsilon c})$, as do global setup and prime search.

Each of the seven powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ <cite data-source="paper">O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}).</cite> Schoolbook multiplication below a fixed cutoff is absorbed into the constant <cite data-source="paper">many smaller lengths are included by enlarging the implicit constant.</cite> So one machine runs in $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.

The exponent is only $2^{-182}$ below one because $g_2$ multiplies three small exponents: $\epsilon$ (few axes), $c$ (narrow chunks) and $1-\tau$ (small interchange saving).
