A linear exchange network is a fixed circuit of linear gates that swaps two banks of values with a sign and restores every scratch wire.

Fix the ground-set size $h=100$ and let $v=\binom h3=161700$ be the number of three-element subsets of $[h]$, and let $\mathcal T$ be the set of these subsets. Banks $X_a,Y_a$ are indexed by $a\in\mathcal T^3$. Set $N=v^3=4227952113000000$ for the size of each data bank, and $m=h^3=1000000$ for the dimension of the label space used later.

## One invocation

Fixing two coordinates of $a$ leaves values $x_S,y_S$; a forward invocation performs $y_S\gets y_S+x_S$. Through central wires $C_i$, $i\in[h]$, gather adds $\sum_{S'\ni i}x_{S'}$ to $C_i$, and scatter adds $\sum_{i\in S}C_i$ to $y_S$. But $x_{S'}$ then reaches $y_S$ with a coefficient depending on $|S\cap S'|$ <cite data-source="paper">on intersection size, and auxiliary wires cancel the unwanted</cite>. Side wires $A_{SS'}$ copy $x_{S'}$ and inject it into $y_S$ to cancel it.

In the bit construction, scalars lie in $\mathbb F_2$ and two triples $S,S'$ are neighbours when $|S\cap S'|=1$. The central coefficient $|S\cap S'|\bmod 2$ is 1 for intersection one and $S'=S$, and 0 otherwise, so the side wires cancel the intersection-one cases.

In the complex construction, scalars lie in $\mathbb Z[i,1/2]$ and the neighbours of a triple are the distinct triples with even intersection (zero or two). Extra central wire $C_\ast$ gathers $\sum_{S'}x_{S'}$, and scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$, so the central coefficient is $(|S\cap S'|-1)/2$. Side injection adds $-\frac{|S\cap S'|-1}{2}A_{SS'}$ to $y_S$, cancelling the rest.

Let $a,c$ be the initial side and central values; $\mathcal V,\mathcal G,\mathcal J,\mathcal R$ are the copy, gather, injection and scatter maps. The schedule subtracts $\mathcal Ja+\mathcal Rc$ from $y$, adds $\mathcal J(a+\mathcal Vx)+\mathcal R(c+\mathcal Gx)$, then restores the scratch values. The net change is $(\mathcal J\mathcal V+\mathcal R\mathcal G)x=x$, independent of $a,c$. So for arbitrary initial scratch values, one forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged <cite data-source="paper">invocation changes $y_S$ to $y_S+x_S$ and leaves every other value</cite>.

## Three stages

Three stages each run $v^2$ invocations with their own scratch wires, so $I=3v^2=78440670000$ is the number of invocations. A forward invocation $X\to Y$ at stage 1, the inverse schedule $Y\to X$ at stage 2, and a forward invocation $X\to Y$ at stage 3 give
$$(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x),$$
that is $(X_a,Y_a)\mapsto(-Y_a,X_a)$ <cite data-source="paper">Performing a forward invocation from $X$ to $Y$ at stage 1,</cite>.

## Counting wires

A fixed triple has $z_{\rm b}=3\binom{97}{2}=13968$ neighbours in the bit construction <cite data-source="paper">z_{\rm b}=3\binom{97}{2}=13968</cite>. It has $z_{\rm c}=\binom{97}{3}+3\cdot97=147731$ neighbours in the complex construction (intersection zero plus intersection two). There are $c_{\rm b}=100$ central wires per invocation in the bit network and $c_{\rm c}=101$ in the complex one.

The bit network has $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=177176569091445000000$ wires <cite data-source="paper">W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b})</cite>. The complex network has $W_{\rm c}=2N+I(vz_{\rm c}+c_{\rm c})=1873807244643542670000$ wires; all these numbers are fixed, independent of the input length.
