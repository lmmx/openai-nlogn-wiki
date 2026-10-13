The subset-intersection finite network is built as a [linear network](linear-network.md) that exchanges two banks of scalars indexed by three-element subsets of a ground set. [Fast interchange of address chunks](tape-interchange.md) uses it for its scalar swap.

Let $[h]=\{1,\dots,h\}$ be the ground set, where $h$ is the number of its elements. Let $\mathcal T$ be the set of three-element subsets of $[h]$, and write $S,T\in\mathcal T$ for triples. Write $X$ and $Y$ for the two banks, which hold a scalar $x_S$ and a scalar $y_S$ for each triple $S$, and $x_T$ is the same family indexed by $T$.

Bit version: scalars lie in $\mathbb F_2$, and $S,T$ are neighbours when $|S\cap T|=1$. Complex version: the scalars that lie in $\mathbb Z[i,1/2]$ are the [Gaussian dyadic numbers](gaussian-dyadic.md), and neighbours are distinct triples with even intersection.

Scratch wires start with arbitrary values. Each ordered neighbouring pair $(S,T)$ has a side wire $A_{ST}$. Each element $g\in[h]$ has a central wire $C_g$, and the complex version adds one more central wire $C_\ast$. The four operations each add a sum of wires to one wire and leave the wires they read unchanged:

- Copy adds $x_T$ to $A_{ST}$.
- Gather adds $\sum_{T\ni g}x_T$ to $C_g$.
- Scatter adds $\sum_{g\in S}C_g$ to $y_S$.
- Side injection adds $\sum_T A_{ST}$, over the neighbours $T$ of $S$, to $y_S$.

In the complex version, gather also adds $\sum_T x_T$ to $C_\ast$, scatter adds $(\sum_{g\in S}C_g-C_\ast)/2$ to $y_S$, and side injection adds $-\frac{|S\cap T|-1}{2}A_{ST}$ for each neighbour $T$.

Gather then scatter adds $\sum_{g\in S}\sum_{T\ni g}x_T=\sum_T|S\cap T|\,x_T$ to $y_S$, since $T$ contains exactly $|S\cap T|$ elements of $S$. So $x_T$ reaches $y_S$ with weight $|S\cap T|$, and side injection removes the unwanted weight. In the bit version, weights are read mod 2: $|S\cap T|\bmod 2$ is $1$ for neighbours and for $T=S$, and side injection cancels the neighbours over $\mathbb F_2$. In the complex version, scatter gives weight $(|S\cap T|-1)/2$ to $x_T$, and side injection gives $-(|S\cap T|-1)/2$ to each neighbour. A neighbour has $|S\cap T|\in\{0,2\}$, so its two terms cancel. A distinct non-neighbour has $|S\cap T|=1$, so its weight is $0$, while $T=S$ keeps weight $1$. In both versions, $x_T$ reaches $y_S$ with weight $1$ if $T=S$ and $0$ otherwise.

A forward invocation runs eight rows in order: subtract side injection, subtract scatter, copy, gather, scatter, side injection, undo gather, undo copy. Rows 0 and 1 remove the effect of the starting scratch values on $y_S$, rows 2 to 5 add the $x_T$ terms, and rows 6 and 7 restore the scratch wires. The starting values cancel whatever they are, so $y_S\gets y_S+x_S$ for each $S$ and nothing else changes.

Each gate adds a fixed combination of wires that it does not change, so the same rows run in reverse order with every gate negated undo a forward invocation. With $Y$ as source and $X$ as target, the inverse schedule gives $X\gets X-Y$ <cite data-source="paper">The inverse schedule with logical source $Y$ and target $X$ effects</cite>.

Three invocations in turn, forward, inverse and forward, take $(X,Y)$ to $(X,\,Y+X)$, then to $(-Y,\,Y+X)$, then to $(-Y,\,X)$. So the banks go from $(X,Y)$ to $(-Y,X)$ <cite data-source="paper">and restores every auxiliary value</cite>.
