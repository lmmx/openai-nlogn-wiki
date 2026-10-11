The Chinese-remainder map relabels cyclic positions so that one cyclic convolution becomes a convolution over a box of several cyclic axes, which lets later steps treat each axis on its own.

Let $d$ be the number of cyclic axes. Each $t_i$ is the number of positions along axis $i$, and the lengths $t_1,\dots,t_d$ are pairwise coprime. Put $T = t_1 t_2 \cdots t_d$, which is the total number of positions.

The map $\phi$ sends a position $n$, for $0 \le n < T$, to the tuple of its residues:

$$\phi(n) = (n \bmod t_1,\dots,n \bmod t_d).$$

The Chinese remainder theorem says $\phi$ is a bijection, and it respects sums: for each axis $r$, the $r$th coordinate of a sum of two positions is the sum of their $r$th coordinates, reduced modulo $t_r$. So a product term at positions $u$ and $v$ lands, after relabeling, at the box point $\phi(u)+\phi(v)$, with each coordinate reduced modulo its axis length. Relabeling the coefficients by $\phi$ therefore turns the cyclic convolution of length $T$ into the $d$-dimensional cyclic convolution on the box $t_1\times\cdots\times t_d$, in which each axis wraps around independently.

Example. Take $T=6=2\cdot 3$, so $t_1=2$ and $t_2=3$. The map sends $0,1,2,3,4,5$ to $(0,0)$, $(1,1)$, $(0,2)$, $(1,0)$, $(0,1)$, $(1,2)$. Check $u=2$ and $v=5$: $(u+v) \bmod 6 = 1$, and $(0,2)+(1,2)=(1,1)$ coordinatewise, which is $\phi(1)$.

The map is applied to the coefficient list of [Radix-digit convolution](radix-digit-convolution.md). The paper uses it this way. <cite data-source="paper">the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution</cite>.
