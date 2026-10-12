The operator norm of a linear map is the largest factor by which the map can stretch a vector. It is what lets a bound on each map in a chain be multiplied into a bound on the whole chain.

Here $w$ denotes a complex vector of length $q$. Its vector norm $\|w\|$ is the largest modulus among its coordinates. <cite data-source="paper">The vector norm is the maximum modulus of its coordinates.</cite> For example, if $w=(1+i,\,-2,\,0.5i)$, the moduli of the coordinates are $\sqrt{2}$, $2$ and $0.5$, so $\|w\|=2$.

Here $L$ denotes a linear map from complex vectors to complex vectors. Its operator norm is

$$\|L\| = \sup_{\|w\|\le 1} \|Lw\|,$$

the supremum (least upper bound) of $\|Lw\|$ over all $w$ with $\|w\|\le 1$. <cite data-source="paper">All operator norms are induced by this norm</cite>.

For $w\neq 0$, the vector $w/\|w\|$ has norm one, so $\|Lw\|\le\|L\|\,\|w\|$ for every $w$. For another linear map $M$, the composition $LM$ applies $M$ first and then $L$. Applying the bound to $Mw$ and then to $w$ gives $\|LM\|\le\|L\|\,\|M\|$.

A linear map $L$ is a linear contraction when $\|L\|\le 1$. A normalized Fourier transform $F_q$ is one: each output $\frac1q\sum_j w_j e^{-2\pi i jk/q}$ averages inputs multiplied by complex numbers of modulus one, so its modulus is at most $\|w\|$.

Here $S'$ denotes half of a [Gaussian resampling](gaussian-resampling.md) map. Here $J'$ denotes half the inverse of an invertible map close to the identity. Here $D'$ denotes a diagonal map scaled by a fixed factor at most one. Here $C$ denotes a map that selects some coordinates, so each output entry copies one input entry and $\|C\|\le 1$.

The argument uses these for $A=S'$ and $B_0=D'J'C$. The Gaussian resampling estimates give $\|S'\|<\frac34$, $\|J'\|<\frac78$ and $\|D'\|<1$. Hence $\|A\|<1$, and $\|B_0\|\le\|D'\|\,\|J'\|\,\|C\|<1$. So $A$ and $B_0$ are linear contractions.
