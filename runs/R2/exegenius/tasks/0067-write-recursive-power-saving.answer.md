Recursive power saving is the argument that a recursion can make its cost per stored bit grow as a fixed power of its parameter, with an exponent below 1. The two fixed-tape procedures need this saving on the way to the main theorem.

Let $f$ be the parameter of a call, the number of field digits for address interchange or of selected axes for a numerical layer. Here $m$ is the factor by which the parameter grows; the letter changes meaning from the subspace dimension of the prerequisite. A recursive call at parameter $mf$ makes $s$ subcalls at parameter $f$, each on a stream of volume $V/W$. The recursion is built on the [Three-element subset intersection construction](subset-intersection-construction.md), which gives $s<Wm$ smaller calls.

Let $T(f)$ be the normalized cost of a call at parameter $f$, its running time divided by the volume $V$ it works on. The subcalls contribute $\frac{s}{W}T(f)$ after dividing by $V$. The call also does outside work at its node. The outside work at a node of parameter $mf$ is at most $C(mf)^\lambda$, for a constant $C$ and an exponent $\lambda<1$. So

$$T(mf)\le\frac{s}{W}T(f)+C(mf)^\lambda.$$

Unrolling over $j$ levels, each level multiplies a term by $s/W$ and divides its parameter by $m$, giving a geometric series with ratio $q=\frac{s/W}{m^\lambda}$. The saving exists because $s/W<m$ <cite data-source="paper">This strict inequality is the source of the power saving.</cite>. Take $\lambda$ with $\log_m(s/W)<\lambda<1$. Then $s/W<m^\lambda$, so $q<1$, the series is at most a constant times its first term, and $T(f)$ is at most a constant times $f^\lambda$ <cite data-source="paper">Since \(a\le m^\sigma<m^\lambda\)</cite>.

For example, take $m=2$, $s=3$ and $W=2$. Then $s/W=\tfrac32<2$ and $\log_2(3/2)\approx0.585$. Any $\lambda\in(0.585,1)$ works; for $\lambda=0.8$ the ratio is $q=\tfrac{3/2}{2^{0.8}}\approx0.86$.

The exponent depends only on $m$, $s$ and $W$, so the saving is a fixed power at every level. The outside work only requires $\lambda$ to lie strictly above $\log_m(s/W)$.
