The subset-intersection finite network is built as a [linear network](linear-network.md) that swaps two banks of scalars indexed by three-element subsets, and [fast interchange of address chunks](tape-interchange.md) uses it for its scalar swap.

Let $[h]=\{1,\dots,h\}$ be the ground set, where $h$ is the number of its elements, and let $\mathcal T$ be the set of its three-element subsets. Write $S,T\in\mathcal T$ for triples. Write $X$ and $Y$ for the two banks, which hold a scalar $x_S$ and a scalar $y_S$ for each triple $S$, and $x_T$ is the same family indexed by $T$.

Bit version: scalars lie in $\mathbb F_2$, and $S,T$ are neighbours when $|S\cap T|=1$. Complex version: scalars lie in $\mathbb Z[i,1/2]$, the set of [Gaussian dyadic numbers](gaussian-dyadic.md), and neighbours are distinct triples with even intersection.

Scratch wires start with arbitrary values: $A_{ST}$ for each ordered neighbouring pair (the side wires), $C_i$ for each $i\in[h]$, and $C_\ast$ in the complex version. Copy adds $x_T$ to $A_{ST}$. Gather adds $\sum_{T\ni i}x_T$ to $C_i$. Scatter adds $\sum_{i\in S}C_i$ to $y_S$. Side injection adds $\sum_T A_{ST}$ over neighbours $T$ to $y_S$.

Gather then scatter gives $\sum_{i\in S}\sum_{T\ni i}x_T=\sum_T|S\cap T|\,x_T$, so $x_T$ reaches $y_S$ with weight $|S\cap T|$. Side injection cancels the unwanted weights. In the bit version, $|S\cap T|\bmod 2$ is $1$ for neighbours and for $T=S$, and the side term cancels the neighbours. In the complex version, gather also adds $\sum_T x_T$ to $C_\ast$, scatter adds $(\sum_{i\in S}C_i-C_\ast)/2$, and side injection adds $-\frac{|S\cap T|-1}{2}A_{ST}$ for each neighbour. Scatter then gives weight $(|S\cap T|-1)/2$, and a neighbour, with $|S\cap T|\in\{0,2\}$, has its two terms cancel. The weight is $0$ when $|S\cap T|=1$, and $1$ for $T=S$, which is not its own neighbour. So $x_T$ reaches $y_S$ with weight $1$ if $T=S$ and $0$ otherwise.

A forward invocation runs eight rows in order: subtract side injection, subtract scatter, copy, gather, scatter, side injection, subtract gather, subtract copy. Rows 0 and 1 remove the starting scratch values from $y_S$. Rows 4 and 5 add them back along with the $x_T$ terms placed by rows 2 and 3, and rows 6 and 7 restore the wires. The starting values cancel whatever they are, so $y_S\gets y_S+x_S$ for each $S$ and nothing else changes.

Each gate adds a sum of wires it does not change, so a gate followed by its negation restores the state. The inverse runs rows 7 to 0 with every gate negated, reading $Y$ and changing $X$. Since the net effect is $y_S\gets y_S+x_S$, it computes $X\gets X-Y$.

For one triple $S$, a forward invocation takes $(x_S,y_S)$ to $(x_S,\,y_S+x_S)$, the inverse takes that to $(-y_S,\,y_S+x_S)$, and a second forward invocation takes that to $(-y_S,\,x_S)$. So the banks go from $(X,Y)$ to $(-Y,X)$, <cite data-source="paper">and restores every auxiliary value</cite>.
