The subset-intersection finite network is built as a [linear network](linear-network.md) that exchanges two banks of scalars indexed by three-element subsets of a fixed ground set.

Let $[h]=\{1,\dots,h\}$ be the ground set, where $h$ is the number of its elements, and let $\mathcal T$ be the set of its three-element subsets. Each $S\in\mathcal T$ has a bank-$X$ scalar $x_S$ and a bank-$Y$ scalar $y_S$. A wire carries one scalar. A gate applies a fixed linear map to the values on its wires, and a wire it does not touch keeps its value.

The network has two versions with the same gates. In the bit version, scalars lie in $\mathbb F_2$, and $S$ and $T$ are neighbours when $|S\cap T|=1$. In the complex version, scalars lie in $\mathbb Z[i,1/2]$, and neighbours are distinct triples with even intersection.

The point of intersection sizes is this. Gather adds $\sum_{T\ni i}x_T$ to a central wire $C_i$ for each $i\in[h]$, and scatter adds $\sum_{i\in S}C_i$ to $y_S$. Together they send $x_T$ to $y_S$ with coefficient $|S\cap T|$, because $\sum_{i\in S}\sum_{T\ni i}x_T=\sum_T|S\cap T|\,x_T$. Side wires then cancel the unwanted coefficients <cite data-source="paper">auxiliary wires cancel the unwanted coefficients</cite>. In the bit version the coefficient $|S\cap T|\bmod 2$ is $1$ for $T=S$ and for intersection one, and $0$ otherwise; the side injection of the copied values removes the intersection-one terms, which leaves the identity.

The gates are as follows. Copy adds $x_T$ to a scratch wire $A_{ST}$ for each neighbouring pair. Side injection adds the sum of the $A_{ST}$ over the neighbours $T$ of $S$ to $y_S$. The complex version uses the side coefficient $-(|S\cap T|-1)/2$, adds $\sum_T x_T$ to a second central wire $C_\ast$, and makes scatter add $(\sum_{i\in S}C_i-C_\ast)/2$ to $y_S$.

A forward invocation runs an eight-row schedule that clears the old scratch values, adds the source values into the target, and then restores the scratch wires. Its net effect is that $y_S$ becomes $y_S+x_S$ and every other value is unchanged, whatever the scratch wires held at the start.

Three invocations make the swap. A forward invocation from $X$ to $Y$, then the inverse schedule from $Y$ to $X$ (which computes $X\gets X-Y$), then a forward invocation from $X$ to $Y$ again. For one pair of scalars, starting from $(x,y)$ this gives $(x,\,y+x)$, then $(-y,\,y+x)$, then $(-y,\,x)$. So the banks go from $(X,Y)$ to $(-Y,X)$ <cite data-source="paper">and restores every auxiliary value</cite>.
