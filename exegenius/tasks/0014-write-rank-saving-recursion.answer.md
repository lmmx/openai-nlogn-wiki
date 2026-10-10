The power saving comes from a counting argument on the recursion. Consider a procedure that handles a call at parameter $mf$ by making $s$ smaller calls at parameter $f$. Each smaller call acts on a stream of volume $V/W$, where $W$ is the number of roles in the [linear network](linear-network-frames.md) and $V$ is the volume of the full array.

After dividing the cost by the volume, the cost of the recursive part at parameter $mf$ is $s/W$ times the cost at parameter $f$. The key condition is that the total number of smaller calls satisfies $s < W m$, which the [subspace construction](subspace-intersection-network.md) provides. So the factor per level is

$$\frac{s}{W} < m.$$

Multiplying the parameter by $m$ therefore increases the normalized recursive cost by less than the factor $m$. Iterating this over the levels of the recursion compounds the saving.

As a numerical illustration, let $W = 2$ and $m = 3$. The condition $s < Wm = 6$ holds for $s = 5$. Each level then multiplies the normalized cost by $s/W = 2.5$, which is less than $m = 3$. After $k$ levels the factor is $2.5^k$ rather than $3^k$, so the saving compounds.

The paper calls this strict inequality the source of the power saving. In the final bound, it appears as the factor $(\lg n)^{-\kappa}$ saved relative to $n \lg n$, with $\kappa = 2^{-182}$. The same recursion appears in the [address-field interchange](address-interchange.md) and the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), where the parameter counts field digits or selected axes.
