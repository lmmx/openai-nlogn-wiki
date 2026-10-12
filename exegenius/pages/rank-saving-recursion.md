Rank-saving recursion is the recursion in which one call on a stored volume $V$ splits into $s$ smaller calls, each on a stream holding $1/W$ of that volume, so that the cost grows by a strictly smaller factor per level. It is what turns the per-level cost into a power saving.

Here the letter $f$ changes meaning: it is the recursion parameter, the number of field digits for address interchange or of selected axes for a numerical layer, a stage of the arithmetic that works along chosen axes of the data.

Rank-saving recursion is realized by a [subset-intersection network](subset-intersection-network.md) on three-element subsets. Rank-saving recursion is instantiated by [address-field interchange](address-interchange.md), where the parameter $f$ counts field digits.

A call at parameter $mf$ on volume $V$ makes $s$ calls at parameter $f$, each on a stream of volume $V/W$. <cite data-source="paper">A recursive call at parameter mf therefore uses s calls at parameter f</cite> A call at $f$ costs a fixed amount per unit of volume, because its cost scales with the volume it acts on. The $s$ calls at $f$ therefore cost $s \cdot (V/W)$ times that unit cost. Dividing by $V$, the recursive contribution at $mf$ is $s/W$ times that at $f$.

The construction guarantees $s<Wm$ <cite data-source="paper">the total number s of smaller calls satisfies s < W m</cite>, so $s/W<m$. Each level multiplies the parameter by $m$ and the per-volume cost by $s/W$, a smaller factor. The strict inequality is what gives the saving: if $s=Wm$, each level would multiply the cost by $m$ too, and there would be no gain.

For example, take $m=2$, $W=3$ and $s=5$, so $s<Wm=6$. Each level doubles the parameter and multiplies the per-volume cost by $5/3$. Over ten levels the parameter grows by $2^{10}=1024$, while the per-volume cost grows by only $(5/3)^{10}\approx 165$. In general the per-volume cost grows like $f^{\log_m(s/W)}$ as the parameter grows to $f$, and the exponent is below $1$ because $s/W<m$.
