The union bound says that the probability that at least one of several events occurs is at most the sum of their probabilities. The paper uses its counting form to show that a packed addition is correct at all but a small set of addresses. The [Packed selected-bit addition](packed-bit-addition.md) page builds on that count.

## Statement

Let $\Omega$ be a finite set, the set of all outcomes considered, and let $\omega$ denote an outcome in $\Omega$. For a finite set $\mathcal{X}$, $|\mathcal{X}|$ is the number of its elements. For $i=1,\dots,m$, let $E_i$ be an event, a subset of $\Omega$, where $m$ counts the events and $i$ is an index (both letters change meaning here). The union bound in counting form says

$$|E_1\cup E_2\cup\cdots\cup E_m|\le|E_1|+|E_2|+\cdots+|E_m|.$$

**Why it holds.** For each outcome $\omega$, let $c(\omega)$ be the number of indices $i$ with $\omega\in E_i$. An outcome lies in the union exactly when $c(\omega)\ge 1$, so it contributes 1 to the left side and at least 1 to $\sum_{\omega}c(\omega)$; every other outcome contributes 0 to both. Each pair $(\omega,i)$ with $\omega\in E_i$ is counted once in $\sum_{\omega}c(\omega)$, which equals $|E_1|+\cdots+|E_m|$.

The argument compares each outcome with the events that contain it and never compares events with one another, so the union bound does not require [Independence of events](independence.md) between the events.

**Probability form.** Choosing $\omega$ uniformly gives each outcome probability $1/|\Omega|$, so $\Pr[X]=|X|/|\Omega|$ for an event $X$. Dividing the counting form by $|\Omega|$ gives $\Pr[E_1\cup\cdots\cup E_m]\le\Pr[E_1]+\cdots+\Pr[E_m]$.

## How the paper uses it

Each address has two chunks, $y$ and $z$ (these letters change meaning here), and spectator coordinates, which are its other coordinates. Here the union bound is applied to events on the set of [addresses](address.md) in the rectangle, so $\Omega$ is that set.

Here $f$ is the number of selected bit positions, and $K$ is the width of each segment, a run of $K$ consecutive bits (the letters $f$ and $K$ change meaning here). Dropping the highest selected position leaves $f-1$ segment pairs, one segment of $y$ and one of $z$ each. The guard value $g_i$ of the $y$-segment is the number formed by its upper $K-1$ bits; $h_i$ is the analogous value in $z$ (the letters $g$ and $h$ change meaning here). <cite data-source="paper">The values gi , hi ∈ {0, . . . , 2K−1 − 1} are the guard values.</cite> There are $m=2(f-1)$ guards.

A guard is *bad* when its value falls outside $10\le g\le 2^{K-1}-11$. An address is *exceptional* when some guard of it is bad. <cite data-source="paper">There are exactly twenty excluded values for each guard in (23).</cite> Here the union bound bounds the exceptions to the [Guard-width bound](guard-width-bound.md), the addresses where a guard value leaves its good range.

**Why a guard value is uniform.** <cite data-source="paper">the complete y, z ranges give the same guard distribution at each choice of spectator coordinates</cite>. Fix the spectator coordinates. The rectangle is a product of ranges, so every pair of $y$ and $z$ values occurs. The guard $g_i$ depends only on $K-1$ bits of $y$, and every other bit is free, so each of the $2^{K-1}$ values of $g_i$ is reached by $|\Omega|/2^{K-1}$ addresses. Hence a uniform address has each guard value with probability $1/2^{K-1}$, and a guard is bad with probability $20/2^{K-1}$.

Let $E_i$ be the set of addresses whose $i$-th guard is bad, so $\Pr[E_i]=20/2^{K-1}$. The exceptional addresses form $E_1\cup\cdots\cup E_m$. The paper applies the union bound to these events: <cite data-source="paper">the union bound over the 2(f − 1) guards gives</cite>

$$m\cdot\frac{20}{2^{K-1}}=\frac{80(f-1)}{2^{K}}.$$

A probability above one says nothing, so the bound is capped. Write $\delta_{\mathrm{bad}}$ for the capped bound $\min\{1,80(f-1)/2^K\}$: <cite data-source="paper">Put δbad = min{1, 80(f − 1)2−K }.</cite>

**Example.** Take $K=8$, so each guard has $2^7=128$ values, 20 bad, and is bad with probability $20/128=5/32$. With $f=3$ there are $m=4$ guards, and the union bound gives $4\cdot 5/32=5/8=80\cdot 2/2^8$.
