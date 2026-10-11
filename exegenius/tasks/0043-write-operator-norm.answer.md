The operator norm is defined for any [linear map](linear-map.md) $L$, and it is the largest factor by which $L$ stretches a vector. Giving each map one number lets a bound on one step of a computation carry over to the next.

Let $u$ be a vector whose length matches the input length of $L$. The norm of $u$, written $\|u\|$, is the largest modulus (absolute value) among its coordinates. <cite data-source="paper">All operator norms are induced by this norm</cite>. Here $\sup$ denotes the supremum, the least upper bound, so the operator norm $\|L\|$ is the least upper bound of $\|Lu\|$ over all vectors $u$ with $\|u\|\le 1$:

$$\|L\| = \sup_{\|u\| \le 1} \|Lu\|.$$

For example, take $m=2$, so $u=(u_0,u_1)$, and let $L$ send $u$ to $(u_0+u_1,\ u_0-u_1)$. If $\|u\|\le 1$, each output coordinate has modulus at most $2$, so $\|L\|\le 2$. The vector $u=(1,1)$ gives $Lu=(2,0)$, so $\|L\|=2$.

Every vector $w$ satisfies $\|Lw\|\le\|L\|\,\|w\|$, because $\|L(w/\|w\|)\|\le\|L\|$ and $L$ is linear. A map with $\|L\|\le 1$ never increases the norm of a vector, and is called a *contraction*. The normalized Fourier transform $F_q$ is a contraction, because <cite data-source="paper">each output averages inputs multiplied by complex numbers of modulus one</cite>.

Operator norms also bound compositions. Let $M$ be a second linear map whose output length matches the input length of $L$, so that $LM$ is defined. For $\|u\|\le 1$, the bound above with $w=Mu$ gives $\|LMu\|\le\|L\|\,\|Mu\|\le\|L\|\,\|M\|$, since $\|Mu\|\le\|M\|$ by the definition of $\|M\|$. Taking the supremum over such $u$ gives $\|LM\|\le\|L\|\,\|M\|$.

On the [Gaussian resampling](gaussian-resampling.md) page, the factors $A$ and $B_0$ are linear maps that are contractions, so they cannot increase the norm of what they are applied to.
