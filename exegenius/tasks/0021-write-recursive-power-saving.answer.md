Recursive power saving is the mechanism that turns a linear-cost network into a tape procedure whose cost is a fixed power of its parameter, with exponent below one. Each tape procedure is realized as a [Linear network with restored auxiliary values](linear-network-exchange.md) that exchanges two banks of values and restores every auxiliary value.

Let $V$ be the number of data values a call moves, $W$ the number of roles in the network, $s$ the number of smaller calls the network makes, and $m$ the factor by which the parameter grows. Here $f$ is the parameter of a smaller call. A call at parameter $mf$ makes $s$ calls at parameter $f$, each on a stream of volume $V/W$, plus linear work on its own volume.

Iterate this. After $j$ levels there are $s^j$ calls, each on volume $V/W^j$, so the work at level $j$ is $(s/W)^j$ times $V$. Let $\theta = \log_m(s/W)$ be the exponent of the saving, so $s/W = m^\theta$. The levels form a geometric sum dominated by its last term, so the cost at parameter $m^k$ is $O(V(m^k)^\theta)$ when $s \ge W$.

The inequality $s/W<m$ is exactly $\theta<1$. <cite data-source="paper">This strict inequality is the source of the power saving</cite> If $s/W$ equalled $m$, $\theta$ would be $1$ and nothing would be saved.

The exponent $\theta$ depends only on the fixed numbers $s$, $W$ and $m$ of the network, so it is uniform. The volume $V$ cancels: each level multiplies the number of calls by $s$ and divides every call's volume by $W$, so the ratio $s/W$ is the same at every level, whatever $V$ and the parameter are.

The recursion is applied to the [Fast address interchange](address-interchange.md), where $u$ is the number of bits in each field. The recursion is also applied to a [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) on $d$ chunks, where $d$ is the number of chunks. <cite data-source="paper">The parameter counts field digits for address interchange and selected axes for a numerical layer.</cite>
