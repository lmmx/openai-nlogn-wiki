# Rank-saving recursion

Rank-saving recursion is the recursive scheme that gives the power saving in the logarithmic factor of [Integer multiplication below n log n](main-theorem.md). Each call makes $s$ smaller calls, each on a stream of $1/W$ of its volume, and the step it presents is $s<Wm$, so each level multiplies the cost per unit of data by less than $m$.

## The network and its streams

Rank-saving recursion counts smaller calls on the wires of the [subset-intersection network](subset-intersection-network.md), whose wires carry scalars. Each wire has a fixed place in the network, its role, and carries a label at each vertex: a subspace of a fixed nondegenerate space of dimension $m$. Labels at adjacent vertices are nested. A wire's vertices are its source, the gates that touch it in time order, and its sink. Each touching of a gate and a wire is an [incidence](incidence.md). Let $W$ be the number of wires, which is also the number of roles.

To split an array, <cite data-source="paper">Distribute rows cyclically among the W roles</cite>, padding the row count to a multiple of $W$. If $V$ is the stored volume of the array, as in [address-field interchange](address-interchange.md), each [role stream](stream.md) holds the same volume $V/W$. Rank-saving recursion gives each smaller call one such [role stream](stream.md).

## Counting the smaller calls

Each call splits into smaller calls to the [address-field interchange](address-interchange.md), each on one role stream of $V/W$ bits. An edge runs from a tail label $U$ to a head label $U'$. Its signed change is $\Delta=\dim U'-\dim U$, the dimension of the head label minus that of the tail label. Its rank is the dimension of the orthogonal complement of the smaller label inside the larger one. <cite data-source="paper">Every edge joins comparable nondegenerate labels.</cite> So the smaller label splits off the larger, and the rank is the absolute change $|\Delta|$.

Each unit of rank is one recursive call. The total is the sum over all edges: $s=\sum|\Delta|$. The paper's version reads <cite data-source="paper">The number of recursive calls is the sum of the edge ranks, exactly s.</cite>

The signed sum of dimension changes telescopes over the incidences of each gate: every [incidence](incidence.md) of one gate carries the same label, so the edge entering a gate and the edge leaving it share that label. The signed sum over all edges is therefore the sum of sink dimensions minus the sum of source dimensions. Let $\mu$ be the sum of the source dimensions (this letter changes meaning here; the paper calls it $N$). The sink dimensions sum to $Wm-\mu$, so $\sum\Delta=Wm-2\mu$.

Let $\mathcal{L}$ be the total dimension lost along decreasing edges, those whose head label is smaller than their tail label. A decreasing edge has $|\Delta|=\Delta+2\cdot\mathrm{loss}$, and an increasing edge has $|\Delta|=\Delta$. Summing gives the count. The recursion is counted for the [complex construction](complex-construction.md) as $s=Wm-2\mu+2\mathcal{L}$.

The recursion is also counted for the [bit construction](bit-construction.md) as $s=Wm-\mu+2\mathcal{L}$, because each of the $\mu$ first-stage source edges has rational rank one although its dimension change is zero. Both counts are at most $Wm-\mu+2\mathcal{L}$, which is below $Wm$ exactly when $2\mathcal{L}<\mu$. The paper states this as <cite data-source="paper">We will obtain L < N/2.</cite> For ground-set size $h=100$ it computes $\mathcal{L}/\mu=100/539$ for the bit construction and $101/539$ for the complex one, both below $1/2$. Hence $s<Wm$.

## Why this gives a power saving

The sources leave this step to the reader. The parameter $e$ counts the selected axes of a [numerical layer](numerical-layer.md), or the digits of an address field. Let $\delta(e)$ be the cost of a call at parameter $e$ divided by its volume. A call at parameter $me$ on volume $V$ makes $s$ calls at parameter $e$, each on volume $V/W$, plus linear work. Dividing by $V$, the recursive part is $(s/W)\,\delta(e)$: each level multiplies the cost per unit of data by $s/W$ while the parameter grows by $m$.

Take $e=m^k$ and iterate: $\delta(m^k)\approx(s/W)^k\,\delta(1)$, with the linear work absorbed into the approximation. Set $\tau=\log_m(s/W)$, the power-saving exponent. Since $(s/W)^k=m^{k\tau}=e^\tau$, we get $\delta(e)\approx e^\tau$, so a call on volume $V$ costs about $Ve^\tau$.

The logarithm needs $m>1$. Then $\log_m$ is increasing with $\log_m m=1$, so $s/W<m$ gives $\tau<1$. If $s/W=m$, then $\tau=1$ and no saving remains. <cite data-source="paper">This strict inequality is the source of the power saving.</cite>

As a toy example, not the paper's values, take $W=4$, $s=6$, $m=2$. Then $s<Wm$ since $6<8$, and $\tau=\log_2 1.5\approx0.585$. With $s=8$, $\tau=1$ and the saving disappears.
