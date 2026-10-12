Recursive power saving is the mechanism that gives a tape procedure, a procedure that rearranges stored data on the tapes of a Turing machine, a cost that is a fixed power of its parameter, with exponent below one.

Recursive power saving is built from a [Linear network with restored auxiliary values](linear-network-exchange.md), a fixed network that exchanges two banks of values and restores every auxiliary value.

Let $V$ be the number of data values a call moves, $W$ the number of roles in the network, $s$ the number of smaller calls the network makes, and $m$ the factor by which the parameter grows. Here $f$ is the parameter of a smaller call. A call at parameter $mf$ makes $s$ calls at parameter $f$, each on a stream of volume $V/W$, plus linear work on its own volume.

Let $k$ be the number of levels, so the top call has parameter $m^k$ and the bottom calls have parameter $1$; base calls at parameter $1$ cost time linear in their volume. Here $j$ is the level index, counting levels from the top. After $j$ levels there are $s^j$ calls, each on volume $V/W^j$, so level $j$ costs $V(s/W)^j$ up to a constant. Let $\theta = \log_m(s/W)$ be the exponent of the saving, so $s/W = m^\theta$ and level $j$ costs $V m^{\theta j}$. Summing over $j=0,\dots,k$ gives a geometric sum with ratio $m^\theta>1$, dominated by its last term, so the total is $O(V(m^k)^\theta)$. This needs $s>W$, so that $\theta>0$.

The condition $s<Wm$ is exactly $\theta<1$, since $s/W<m$ means $m^\theta<m$. <cite data-source="paper">This strict inequality is the source of the power saving</cite>. If $s=Wm$, the cost is linear in the parameter and nothing is saved.

The exponent is uniform: it depends only on $s$, $W$ and $m$, because each level multiplies the call count by $s$ and divides each call's volume by $W$, so $s/W$ is the same at every level, whatever $V$ is.

For the field-digit parameter $u$ of its bound $O(Vu^\tau)$, the recursion bounds the cost of the [Fast address interchange](address-interchange.md), with $\tau=\theta$.

The same recursion is applied to the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) on $d$ chunks, with parameter $d$, the number of chunks, and exponent $\lambda'=\theta$, which matches $O(Vd^{\lambda'})$.
