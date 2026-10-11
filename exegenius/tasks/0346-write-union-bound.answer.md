The union bound says that the probability that at least one of several events occurs is at most the sum of their probabilities. The paper uses its counting form to show that the exceptional addresses of a packed addition form a small set, so the addition is correct at every other address. The [Packed selected-bit addition](packed-bit-addition.md) page builds on that count.

## Statement

Let $\Omega$ be a finite [Ground set](ground-set.md), the set of all outcomes considered. For a set $X$, $|X|$ is the number of elements of $X$. Let $E_i$, for $i=1,\dots,m$, be subsets of $\Omega$, the events, where $m$ is their number; $m$ has this meaning on this page only. The union bound in counting form says

$$|E_1\cup E_2\cup\cdots\cup E_m|\le|E_1|+|E_2|+\cdots+|E_m|.$$

The bound holds without [Independence of events](independence.md) between the events.

Choosing an element of $\Omega$ uniformly at random gives each element probability $1/|\Omega|$. For a subset $X$ of $\Omega$, $\Pr[X]=|X|/|\Omega|$ is the probability that the chosen element lies in $X$. Dividing the counting form by $|\Omega|$ gives

$$\Pr[E_1\cup\cdots\cup E_m]\le\Pr[E_1]+\cdots+\Pr[E_m].$$

**Example.** Let $\Omega=\{0,1,\dots,99\}$, $m=2$, $E_1$ the even numbers in $\Omega$ (50 elements), and $E_2$ the multiples of 5 (20 elements). The union has 60 elements, because the 10 multiples of 10 lie in both sets. The bound gives $60\le 50+20=70$, and in probability form $0.6\le 0.5+0.2$. The slack of 10 is the overlap, which the bound ignores.

## How the paper uses it

Here $f$ is the number of selected bit positions, and $K$ is the width in bits of each segment of the [Guard-width bound](guard-width-bound.md), a run of $K$ consecutive bits. Here $y$ and $z$ are the two address chunks. Each of the $f-1$ segment pairs $i$ carries two guard values: $g_i$, the segment in $y$ with its lowest bit removed, and $h_i$, the analogous value in $z$. Each guard value lies in $\{0,\dots,2^{K-1}-1\}$, and there are $m=2(f-1)$ guards. The union bound bounds the bad fraction of the guard values that the [Guard-width bound](guard-width-bound.md) provides for each segment.

A guard is bad when its value falls outside the good range $10\le g\le 2^{K-1}-11$, which excludes the 10 smallest and 10 largest values. <cite data-source="paper">There are exactly twenty excluded values for each guard in (23)</cite>.

Why may a guard value be treated as uniform on its $2^{K-1}$ values? The spectator coordinates are the address coordinates that the addition leaves unchanged. <cite data-source="paper">the complete y, z ranges give the same guard distribution at each choice of spectator coordinates</cite>. So with the spectators fixed, every guard value occurs equally often, and a uniform guard is bad with probability $20/2^{K-1}$.

An [Address](address.md) is exceptional when at least one of its guards is bad, so the union bound bounds the number of exceptional addresses by the sum of the per-guard bad sets. Each event $E_i$ is the set of addresses whose $i$-th guard is bad. The paper applies the union bound to these $m=2(f-1)$ events: <cite data-source="paper">the union bound over the 2(f − 1) guards gives</cite>

$$m\cdot\frac{20}{2^{K-1}}=\frac{80(f-1)}{2^{K}}.$$

Writing $\delta_{\mathrm{bad}}$ for the capped bound, $\delta_{\mathrm{bad}}=\min\{1,80(f-1)/2^K\}$, since a probability bound above one says nothing. <cite data-source="paper">Put δbad = min{1, 80(f − 1)2−K }.</cite>

**Example.** Take $K=8$, so each guard has $2^7=128$ values, 20 of them bad, and each guard is bad with probability $20/128=5/32$. With $f=3$ there are $m=4$ guards, and the bound gives $4\cdot 5/32=5/8$. This equals $80\cdot 2/2^8=5/8$, the paper's formula.
