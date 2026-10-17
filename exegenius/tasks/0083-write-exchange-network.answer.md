A linear exchange network is a fixed circuit of linear gates on wires carrying scalars that swaps two banks with a sign and restores every scratch wire, whatever value it started with.

Fix the ground-set size $h=100$ and let $v=\binom h3=161700$ be the number of three-element subsets of $[h]$, and let $\mathcal T$ be the set of these subsets. Banks $X_a,Y_a$ are indexed by $a\in\mathcal T^3$, a triple of triples. Set $N=v^3=4227952113000000$ for the size of each data bank, and $m=h^3=1000000$ for the label-space dimension used later.

## One invocation

Fixing two coordinates of $a$ leaves values $x_S,y_S$ indexed by triples $S\in\mathcal T$; $x$ and $y$ denote the vectors of all $x_S$ and all $y_S$. A forward invocation performs $y_S\gets y_S+x_S$. Through central wires $C_i$, $i\in[h]$, gather adds $\sum_{S'\ni i}x_{S'}$ to $C_i$, with $S'$ another triple, and scatter adds $\sum_{i\in S}C_i$ to $y_S$. But $x_{S'}$ reaches $y_S$ with a coefficient depending on $|S\cap S'|$ <cite data-source="paper">on intersection size, and auxiliary wires cancel the unwanted</cite>. Side wires $A_{SS'}$ copy $x_{S'}$ and inject it into $y_S$ to cancel it.

In the bit construction, scalars lie in $\mathbb F_2$ and two triples $S,S'$ are neighbours when $|S\cap S'|=1$. The central coefficient $|S\cap S'|\bmod 2$ is 1 for $S'=S$ and for intersection one, and 0 otherwise, so side wires cancel the intersection-one cases.

In the complex construction, the network has scalars in $\mathbb Z[i,1/2]$, the Gaussian integers over powers of two of [Fixed-point Gaussian dyadic records](fixed-point.md), and the neighbours of a triple are the distinct triples with even intersection (zero or two). Extra wire $C_\ast$ gathers $\sum_{S'}x_{S'}$ and scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$, so the central coefficient is $(|S\cap S'|-1)/2$. Side injection cancels it for intersection zero and two; intersection one contributes zero.

Let $\sigma,\gamma$ be the initial side and central scratch vectors; $\mathcal V,\mathcal G,\mathcal J,\mathcal R$ are the copy, gather, injection and scatter maps. The schedule subtracts $\mathcal J\sigma+\mathcal R\gamma$ from $y$, copies and gathers (scratch values become $\sigma+\mathcal Vx$, $\gamma+\mathcal Gx$), scatters and injects, adding $\mathcal R(\gamma+\mathcal Gx)+\mathcal J(\sigma+\mathcal Vx)$ to $y$, then undoes gather and copy, restoring $\gamma,\sigma$. The net change of $y$ is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x$ and is independent of $\sigma,\gamma$; by the cancellations above it is $y\gets y+x$. So for arbitrary initial scratch values, one forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged <cite data-source="paper">invocation changes $y_S$ to $y_S+x_S$ and leaves every other value</cite>.

## Three stages

Three stages each run $v^2$ invocations with their own scratch wires, so there are $I=3v^2=78440670000$ invocations. The inverse schedule, the forward one with target updates negated and logical source $Y$, target $X$, has net change $X\gets X-Y$. A forward invocation $X\to Y$ at stage 1, the inverse schedule $Y\to X$ at stage 2 and a forward invocation $X\to Y$ at stage 3 give
$$(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x),$$
that is $(X_a,Y_a)\mapsto(-Y_a,X_a)$ <cite data-source="paper">Performing a forward invocation from $X$ to $Y$ at stage 1,</cite>.

## Counting wires

A fixed triple has $z_{\rm b}=3\binom{97}{2}=13968$ neighbours in the bit construction <cite data-source="paper">z_{\rm b}=3\binom{97}{2}=13968</cite>. It has $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ neighbours in the complex construction (intersection zero plus intersection two). There are $c_{\rm b}=100$ central wires per invocation in the bit network and $c_{\rm c}=101$ in the complex one.

Each ordered neighbour pair has a side wire. The bit network has $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ wires <cite data-source="paper">W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b})</cite>. The complex network has $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$ wires; all these numbers are fixed, independent of the input length.
