The complex construction is a variant of the [subset-intersection network](subset-intersection-network.md). It takes its scalars from [Gaussian dyadics](gaussian-dyadics.md), so every value it computes is exact. The total number of wires in the complex construction is $W_c$, and the rank-saving argument compares this count with $m$.

## The network

The network keeps the triples $S,T\in\mathcal{K}$, the banks $X$ and $Y$, the vectors $\xi$ and $\eta$, the side wires $W_{ST}$, the central wires $C_\ell$ and the eight-row forward schedule of the subset-intersection network. Two things change: the scalars are Gaussian dyadics, and two distinct triples $S$ and $T$ are *neighbours* when $|S\cap T|$ is even, so $|S\cap T|\in\{0,2\}$.

The extra central wire $C_*$ gathers the sum of all source values. For an ordered pair $(S,T)$ of triples, $\kappa_{ST}=\tfrac12(|S\cap T|-1)$ is the central coefficient. The gates are:

- copy adds $\xi_T$ to $W_{ST}$ for each neighbouring pair $(S,T)$;
- gather adds $\sum_{T\ni\ell}\xi_T$ to $C_\ell$ for each $\ell\in[h]$, and adds $\sum_T\xi_T$ to the extra central wire $C_*$;
- scatter adds $\tfrac12\bigl(\sum_{\ell\in S}C_\ell-C_*\bigr)$ to $\eta_S$;
- side injection adds $-\sum_{T \text{ neighbour of } S}\kappa_{ST}\,W_{ST}$ to $\eta_S$.

Copy is unchanged from the bit case, and the forward schedule runs the same eight rows in the same order.

## Why the neighbour rule changes

The complex construction reads its overlaps from [indicator vectors](indicator-vector.md), since $t_S^{\mathsf T}t_T=|S\cap T|$ for triples $S$ and $T$.

A source value $\xi_T$ reaches $\eta_S$ by the gather-then-scatter route. It enters $C_\ell$ for each of the $|S\cap T|$ elements $\ell\in S\cap T$, and it enters $C_*$ once. Scatter then gives it the coefficient $\tfrac12\bigl(|S\cap T|-1\bigr)=\kappa_{ST}$. The source states this coefficient in the same form: <cite data-source="paper">In the complex case, the central coefficient is</cite> $\kappa_{ST}$.

The side route must cancel this term. Copy puts $\xi_T$ into $W_{ST}$ for each neighbour $T$, and side injection subtracts $\kappa_{ST}$ times that wire. So the side route contributes $-\kappa_{ST}\,\xi_T$ for each neighbour $T$ of $S$, and the two routes cancel exactly for neighbours.

Which triples need a side wire? The coefficient $\kappa_{ST}$ is zero when $|S\cap T|=1$, so those triples need none. It is $-\tfrac12$ when $|S\cap T|=0$, $\tfrac12$ when $|S\cap T|=2$, and $1$ when $T=S$. Only intersections zero and two need cancelling, so the neighbours are the distinct triples with even intersection. In the bit case the coefficient is $|S\cap T| \bmod 2$, which is nonzero exactly at intersection one, so the neighbour rule was the other way round. The source gives the same cancellation: <cite data-source="paper">The side cancels it for distinct triples with intersection zero or two; intersection one</cite> contributes zero.

The factor $\tfrac12$ in scatter and in $\kappa_{ST}$ is why the scalars must be Gaussian dyadics rather than Gaussian integers.

## Worked check

Take $h\ge 6$ and $S=\{1,2,3\}$. The coefficient of $\xi_T$ in the net change of $\eta_S$ is computed from the two routes:

- $T=S$: $\kappa_{SS}=1$, and $S$ is not its own neighbour, so the coefficient is $1$.
- $T=\{1,2,4\}$: $|S\cap T|=2$, so $\kappa_{ST}=\tfrac12$. This $T$ is a neighbour, the side route gives $-\tfrac12$, and the total is $0$.
- $T=\{1,4,5\}$: $|S\cap T|=1$, so $\kappa_{ST}=0$. This $T$ is not a neighbour, and the total is $0$.
- $T=\{4,5,6\}$: $|S\cap T|=0$, so $\kappa_{ST}=-\tfrac12$. This $T$ is a neighbour, the side route gives $+\tfrac12$, and the total is $0$.

So the net change is $\eta_S\leftarrow\eta_S+\xi_S$, and every other entry of $\eta$ is unchanged. The source states the same net map: <cite data-source="paper">Thus both net maps are y ← y + x.</cite>

## Exchange and wire count

Three stages then exchange the banks as in the bit case. On one line the stages act as $(x,y)\mapsto(x,\,y+x)\mapsto(-y,\,y+x)\mapsto(-y,\,x)$, which matches the source's signed exchange <cite data-source="paper">(Xa , Ya ) 7−→ (−Ya , Xa )</cite>. The wire count $W_c$ is fixed: <cite data-source="paper">All these numbers are fixed, independently of any eventual input length.</cite>
