Rank-saving recursion is the recursion in which one call on a stored volume splits into several smaller calls, each on a stream holding a fixed fraction of that volume, so that the cost grows by a strictly smaller factor per level. It is what turns the per-level cost into a power saving.

Here $V$ is the volume of stored data that a call acts on. Here $f$ is the recursion parameter, the number of field digits for address interchange or of selected axes for a numerical layer. Here $m$ is the dimension of a fixed space, the number of its basis vectors. Here $W$ is the factor by which each stream's volume is divided. Here $s$ is the number of smaller calls that one call makes.

Rank-saving recursion is realized by a [subset-intersection network](subset-intersection-network.md) on three-element subsets. Rank-saving recursion is instantiated by [address-field interchange](address-interchange.md), where the parameter $f$ counts field digits.

A call at parameter $mf$ on volume $V$ makes $s$ calls at parameter $f$, each on a stream of volume $V/W$ <cite data-source="paper">A recursive call at parameter mf therefore uses s calls at parameter f</cite>. Dividing cost by volume, the recursive contribution at $mf$ is $s/W$ times that at $f$.

The construction guarantees $s<Wm$ <cite data-source="paper">the total number s of smaller calls satisfies s < W m</cite>, so $s/W<m$. This strict inequality is what gives the saving: if $s=Wm$, the factor per level would equal $m$, the factor by which the parameter itself grows, and there would be no gain.

For example, take $m=2$, $W=3$ and $s=5$, so $s<Wm=6$. Each level multiplies the parameter by $2$ and the per-volume cost by $5/3$. Over ten levels the parameter grows by $2^{10}=1024$, while the per-volume cost grows by only $(5/3)^{10}\approx 165$. In general the per-volume cost grows like $f^{\log_m(s/W)}$, with exponent below $1$.
