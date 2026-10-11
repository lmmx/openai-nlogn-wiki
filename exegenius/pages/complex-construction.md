The complex construction is a variant of the [Subset-intersection network](subset-intersection-network.md) that takes its scalars from [Gaussian dyadics](gaussian-dyadics.md), so that it exchanges two banks of values exactly. It gives the complex-case count of smaller calls that the [Rank-saving recursion](rank-saving-recursion.md) needs.

## The network

An *invocation* fixes two of the three triple coordinates of a bank entry and varies the third, so it reads $x_T$ and updates $y_S$ for triples $S,T$. Its auxiliary wires are side wires $W_{ST}$, one for each ordered neighbouring pair $(S,T)$, central wires $C_\ell$ for $\ell\in[h]$, and an extra central wire $C_*$. The complex construction reads its overlaps from [Indicator vector](indicator-vector.md)s, since $|S\cap T|=t_S^{\mathsf T}t_T$, where $t_S$ is the indicator vector of $S$. Two distinct triples are *neighbours* when $|S\cap T|$ is even. <cite data-source="paper">scalars lie in Z[i, 1/2], and neighbors are distinct triples with</cite> even intersection.

The coefficient $\varpi_{ST}=\tfrac12(|S\cap T|-1)$ is the central coefficient of $x_T$ in $y_S$.

The gates are:

- copy adds $x_T$ to $W_{ST}$ for each neighbouring pair $(S,T)$;
- gather adds $\sum_{T\ni \ell}x_T$ to $C_\ell$ for each $\ell\in[h]$, and $\sum_T x_T$ to $C_*$;
- scatter adds $\tfrac12\bigl(\sum_{\ell\in S}C_\ell-C_*\bigr)$ to $y_S$;
- side injection adds $-\sum_{T \text{ neighbour of } S}\varpi_{ST}\,W_{ST}$ to $y_S$.

<cite data-source="paper">Write V for copy, G for gather, J for side injection and R for scatter.</cite> <cite data-source="paper">The first two rows of the following schedule remove</cite> the old scratch values, the next four add $x$ to $y$, and the last two restore the scratch values. A forward invocation changes $y_S$ to $y_S+x_S$ and <cite data-source="paper">leaves every other value unchanged</cite>.

## Why the neighbour rule changes

The complex construction changes the neighbour rule of the [Bit construction](bit-construction.md) and keeps its copy step. A value $x_T$ enters $C_\ell$ for each of the $|S\cap T|$ elements $\ell\in S\cap T$, and enters $C_*$ once, so scatter gives it the central coefficient $\varpi_{ST}$, which the source writes as <cite data-source="paper">(|S ∩ T | − 1)/2</cite>.

Side injection subtracts $\varpi_{ST}W_{ST}$, so the two routes cancel for each neighbour. A side wire is needed exactly where the central coefficient is nonzero and $T\neq S$. That coefficient is $0$ at intersection one, $-\tfrac12$ at intersection zero and $\tfrac12$ at intersection two, so the neighbours are the distinct triples with intersection zero or two: <cite data-source="paper">The side cancels it for distinct triples with intersection zero or two</cite>. In the bit case, the central coefficient from $x_T$ to $y_S$ is <cite data-source="paper">|S ∩ T | mod 2</cite>, nonzero at intersection one, so the bit neighbours have intersection one.

## Worked check

Take $h\ge 6$ and $S=\{1,2,3\}$. The coefficient of $x_T$ in $y_S$ is the central term plus side term:

- $T=S$: $\varpi_{SS}=1$, with no side term, so the total is $1$.
- $T=\{1,2,4\}$: $\varpi_{ST}=\tfrac12$ and side term $-\tfrac12$, so the total is $0$.
- $T=\{1,4,5\}$: $\varpi_{ST}=0$ and no side wire, so the total is $0$.
- $T=\{4,5,6\}$: $\varpi_{ST}=-\tfrac12$ and side term $+\tfrac12$, so the total is $0$.

So $y_S\leftarrow y_S+x_S$. <cite data-source="paper">Thus both net maps are y ← y + x.</cite>

## Exchange of the banks

Stages 1 and 3 are forward invocations from $X$ to $Y$, and stage 2 is the inverse schedule. Starting from $(x,y)$, <cite data-source="paper">the three stages give (x, y + x), then (−y, y + x), then (−y, x).</cite> The net effect is <cite data-source="paper">(Xa , Ya ) 7−→ (−Ya , Xa )</cite>, <cite data-source="paper">and restores every auxiliary value.</cite>

## Wire count and the saving

Let $v=\binom h3$ be the number of triples; the letter $v$ changes meaning here. Each bank has $N=v^3$ entries, one wire each. <cite data-source="paper">A wire carries one scalar.</cite> There are $I=3v^2$ invocations. Each has $vz_c$ side wires and $c_c$ central wires, where $z_c$ is the number of neighbours of a fixed triple. <cite data-source="paper">With cb = 100 and cc = 101 central wires per invocation</cite> gives $c_c=101$. The total number of wires, $W_c$, is

$$W_c=2N+I\,(vz_c+c_c)=1873807244643542670000.$$

Let $s_c$ be the total number of smaller calls. The source gives <cite data-source="paper">sc = Wc m − 2N + 2Lc = 1873807244636671267308000000 < Wc m.</cite> $L_c$ is the dimension lost on central-wire edges. By Lemma 6, <cite data-source="paper">L = Ich,</cite> so $L_c=792250767000000<N/2=2113976056500000$.

The letter $m$ changes meaning here: it is the dimension of the label space, $m=h^3$. <cite data-source="paper">m = h3 = 1000000.</cite> Dividing by $W_c$ gives $s_c/W_c<m$, the inequality <cite data-source="paper">that the total number s of smaller calls satisfies s < W m</cite> that the rank-saving argument uses.
