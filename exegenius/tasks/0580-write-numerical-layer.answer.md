A numerical layer is one stage of the transform calculation. It computes the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) on its selected bits, and its cost bound lets the [Rank-saving recursion](rank-saving-recursion.md) save a power at each level.

The layer acts on the [record](payload.md) at each address, coefficient by coefficient. Each address is written as $D$ consecutive chunks of $\delta$ bits, and each chunk selects the bit at offset $o$. The output at a setting $x\in\{0,1\}^D$ of the selected bits is
$$2^{-D}\sum_{b\in\{0,1\}^D}(-1)^{x\cdot b}\,v_b,$$
where $v_b$ is the input at setting $b$ and $x\cdot b$ counts the positions where both are 1. For example, take $D=2$ and inputs $1,3,5,7$ at settings $(0,0)$, $(0,1)$, $(1,0)$, $(1,1)$. The output is $4,-1,-2,0$; at $(0,1)$ it is $(1-3+5-7)/4=-1$.

Let $V$ be the number of stored bits. One axis at a time needs <cite data-source="paper">separate butterfly factors would require D whole-array passes</cite>, each scanning all $V$ stored bits. A row is the address suffix at one fixed prefix and row index. <cite data-source="paper">Distribute rows cyclically among the W roles</cite>, so <cite data-source="paper">each contains V /W bits</cite> per role.

Here $e$ is the number of selected axes a call acts on (the letter changes meaning here). Here $m$ is the fixed integer by which a call divides $e$ (the letter changes meaning here). Here $s$ is the number of smaller calls a call makes (the letter changes meaning here). <cite data-source="paper">A recursive call at parameter mf therefore uses s calls at parameter f</cite>: a call on $e$ axes makes $s$ calls on $e/m$ axes, each on $V/W$ bits. Here $d$ is an upper bound on $D$ (the letter changes meaning here). Here $\log_m x$ is the exponent to which $m$ must be raised to give $x$. Each call divides its axes by $m$, so there are about $\log_m d$ levels.

<cite data-source="paper">Dividing by the current volume V gives the factor s/W</cite>, so each level multiplies the cost per stored bit by $s/W$. Over $\log_m d$ levels this compounds to
$$(s/W)^{\log_m d}=d^{\log_m(s/W)},$$
since both sides equal $\exp(\ln d\,\ln(s/W)/\ln m)$.

The paper requires <cite data-source="paper">that the total number s of smaller calls satisfies s < W m.</cite> That is $s/W<m$, so $\log_m(s/W)<1$. Otherwise the exponent is at least one and nothing is saved. <cite data-source="paper">This strict inequality is the source of the power saving.</cite> The layer costs $O(V d^{\lambda'})$, where $\lambda'$ is a fixed exponent below one. <cite data-source="paper">the cost is O(V dλ ) for a fixed λ′ < 1</cite>.

The layer is exact. Its operations are <cite data-source="paper">complex additions, subtractions, halvings, sign</cite> changes and multiplication by $i$. Each keeps Gaussian dyadics closed: sums use the larger power of two as denominator, halving doubles it, and the rest leave it alone. The inputs lie on $2^{-p}\mathbb{Z}[i]$, so <cite data-source="paper">Intermediate values are exact Gaussian dyadics</cite>.
