The Chinese-remainder map is a relabeling of cyclic positions that turns one cyclic convolution into a convolution over a box of several cyclic axes, so that later steps can treat each axis on its own. It is also called the Agarwal–Cooley map. The map is applied to the coefficients of [Radix-digit convolution](radix-digit-convolution.md).

Write $r$ for the number of cyclic axes, not the digit count of the earlier page. Write $a$ for an axis index, $1 \le a \le r$, and $t_a$ for the number of positions along axis $a$; the lengths $t_1,\dots,t_r$ are pairwise coprime. Put $T = t_1 t_2 \cdots t_r$, the total number of positions.

On this page $p$ and $q$ are cyclic positions, not the coefficient index of the radix-digit page, with $0 \le p, q < T$; and $w$ is an output position, not the digit width there. The map $\phi$ sends a position $p$ to the tuple of its residues:

$$\phi(p) = (p \bmod t_1,\dots,p \bmod t_r).$$

The box is the set of tuples whose $a$th entry lies in $\{0,\dots,t_a-1\}$. By the Chinese remainder theorem, $\phi$ is a bijection that respects sums: $\phi((p+q) \bmod T)=\phi(p)+\phi(q)$, with the sum taken coordinatewise and each entry reduced modulo its $t_a$. Since $\phi$ is injective, $p+q \equiv w \pmod T$ holds exactly when $\phi(p)+\phi(q)=\phi(w)$. So the terms adding into output $w$ are the pairs of box points whose coordinatewise sum is $\phi(w)$, each axis wrapping on its own. This is the $r$-dimensional cyclic convolution on the box.

Example. Take $T=6$, so $t_1=2$ and $t_2=3$. The map sends $0,\dots,5$ to $(0,0),(1,1),(0,2),(1,0),(0,1),(1,2)$. For $p=2$ and $q=5$, $(p+q) \bmod 6 = 1$, and $(0,2)+(1,2)=(1,1)$ coordinatewise, which is $\phi(1)$.

The paper uses the map in this way; there <cite data-source="paper">the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution</cite>.
