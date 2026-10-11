The Chinese-remainder map relabels cyclic positions so that one cyclic convolution becomes a convolution over a box of several cyclic axes, which lets later steps treat each axis on its own.

Let $d$ be the number of cyclic axes, not the digit count of the earlier page. Each $t_i$ is the number of positions along axis $i$, and the lengths $t_1,\dots,t_d$ are pairwise coprime. Put $T = t_1 t_2 \cdots t_d$, the total number of positions.

The map $\phi$ sends a position $n$ (not the input length), for $0 \le n < T$, to the tuple of its residues:

$$\phi(n) = (n \bmod t_1,\dots,n \bmod t_d).$$

For positions $u$ and $v$, the Chinese remainder theorem says $\phi$ is a bijection, and it respects sums: $\phi(u+v \bmod T)=\phi(u)+\phi(v)$, where the sum on the right is coordinatewise and reduced modulo each $t_i$.

Hence $u+v \equiv m \pmod T$ holds exactly when $\phi(u)+\phi(v)=\phi(m)$ coordinatewise, for an output position $m$, because $\phi$ is injective. So the product terms that add into output $m$ are exactly the pairs of box points whose coordinatewise sum is $\phi(m)$. Each coordinate wraps modulo its own $t_i$, so this is the $d$-dimensional cyclic convolution on the box $t_1\times\cdots\times t_d$, in which each axis wraps around independently.

Example. Take $T=6=2\cdot 3$, so $t_1=2$ and $t_2=3$. The map sends $0,1,2,3,4,5$ to $(0,0)$, $(1,1)$, $(0,2)$, $(1,0)$, $(0,1)$, $(1,2)$. Check $u=2$ and $v=5$: $(u+v) \bmod 6 = 1$, and $(0,2)+(1,2)=(1,1)$ coordinatewise, which is $\phi(1)$.

The map is applied to the coefficient list of [Radix-digit convolution](radix-digit-convolution.md). The paper uses it this way. <cite data-source="paper">the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution</cite>.
