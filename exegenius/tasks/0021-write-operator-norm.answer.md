The operator norm measures how much a linear map can enlarge a vector. It gives each map a single number, which lets a bound on one step of a computation carry over to the next. Here $L$ denotes a [linear map](linear-map.md). The operator norm is defined for any [linear map](linear-map.md), and it is the largest factor by which $L$ stretches a vector.

The variable $u$ denotes a vector whose length matches the input length of $L$. The norm of $u$ is the largest modulus (absolute value) among its coordinates, and operator norms are taken with respect to this norm. <cite data-source="paper">All operator norms are induced by this norm</cite>. Then

$$\|L\| = \sup_{\|u\| \le 1} \|Lu\|,$$

where $\sup$ is the supremum, the least upper bound of the values $\|Lu\|$ over all $u$ with $\|u\| \le 1$.

For example, let $L$ send $(u_0, u_1)$ to $(u_0+u_1,\ u_0-u_1)$. If every coordinate of $u$ has modulus at most one, each output coordinate has modulus at most $2$, and $u=(1,1)$ gives $Lu=(2,0)$. Hence $\|L\|=2$.

A map with $\|L\| \le 1$ never increases the norm of a vector, and is called a contraction. The normalized Fourier transform $F_q$ is one, because <cite data-source="paper">each output averages inputs multiplied by complex numbers of modulus one</cite>.

Operator norms also bound compositions: $\|LM\| \le \|L\|\,\|M\|$, so the norm of a product of maps is at most the product of their norms. On the [Gaussian resampling](gaussian-resampling.md) page, the factors $A$ and $B_0$ are contractions, so they cannot increase the norm of what they are applied to.
