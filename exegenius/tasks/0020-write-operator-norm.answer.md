The operator norm of a linear map is the largest factor by which the map can stretch a vector. It is what lets a bound on each map in a chain be multiplied into a bound on the whole chain.

Here $w$ denotes a complex vector of length $q$. Its vector norm $\|w\|$ is the largest modulus among its coordinates. <cite data-source="paper">The vector norm is the maximum modulus of its coordinates.</cite> For example, if $w=(1+i,\,-2,\,0.5i)$, the moduli of the coordinates are $\sqrt{2}$, $2$ and $0.5$, so $\|w\|=2$.

Here $L$ denotes a linear map from complex vectors to complex vectors. Its operator norm is

$$\|L\| = \sup_{\|w\|\le 1} \|Lw\|,$$

the supremum (least upper bound) of the values $\|Lw\|$ over all vectors $w$ with $\|w\|\le 1$. The operator norm is defined from the vector norm in this way. <cite data-source="paper">All operator norms are induced by this norm</cite>.

Scaling a nonzero vector $w$ to $w/\|w\|$, which has norm one, gives $\|Lw\|\le\|L\|\,\|w\|$ for every $w$. Applying this twice gives $\|LM\|\le\|L\|\,\|M\|$ for linear maps $L$ and $M$, so the norm of a composition is at most the product of the norms.

A linear map $L$ is a linear contraction when $\|L\|\le 1$, that is, when $\|Lw\|\le\|w\|$ for every $w$. Two examples follow from the definition. A coordinate permutation has norm one <cite data-source="paper">Coordinate permutations preserve the norm</cite>, since it only rearranges the moduli. A normalized Fourier transform is a contraction, since each output averages inputs multiplied by complex numbers of modulus one.

The argument uses this for $A=S'$ and $B_0=D'J'C$. Since $\|C\|=1$ and $\|S'\|$, $\|J'\|$, $\|D'\|$ are below their stated bounds, the product bound gives $\|B_0\|\le\|D'\|\,\|J'\|\,\|C\|$, and this is what makes $A$ and $B_0$ linear contractions.
