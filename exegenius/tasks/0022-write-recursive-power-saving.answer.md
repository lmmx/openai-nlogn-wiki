Recursive power saving is the argument that a recursion can make the cost per stored bit grow as a fixed power of its parameter, with exponent below 1. The two fixed-tape procedures need this saving on the way to the main theorem.

Let $f$ be the parameter of a call; it counts field digits for address interchange and selected axes for a numerical layer. Let $V$ be the stored bit volume. A recursive call at parameter $mf$ makes $s$ subcalls at parameter $f$, each on a stream of volume $V/W$, where $m$ is the factor by which the parameter is multiplied, $s$ is the number of subcalls, and $W$ is the divisor of the volume. The recursion is built on the [Three-element subset intersection construction](subset-intersection-construction.md), which gives $s<Wm$ smaller calls.

Let $T(f)$ be the cost of a call at parameter $f$ divided by the volume $V$ it works on. Each subcall costs $T(f)$ times its volume $V/W$, so after dividing by $V$ the $s$ subcalls contribute $\frac{s}{W}\,T(f)$. Thus $T(mf)$ equals $\frac{s}{W}\,T(f)$ plus the work done at that level outside the subcalls. Ignoring that outside work, $T(f)$ grows like $f^{\log_m(s/W)}$. The exponent $\log_m(s/W)$ is below 1 because $s/W<m$. <cite data-source="paper">This strict inequality is the source of the power saving.</cite>

For example, take $m=2$, $s=3$ and $W=2$. Each doubling of the parameter multiplies $T$ by $\tfrac{3}{2}$, so $T$ grows like $f^{\log_2(3/2)}\approx f^{0.585}$.

Since the exponent depends only on $m$, $s$ and $W$, the saving is a fixed power that the recursion gives at every level.
