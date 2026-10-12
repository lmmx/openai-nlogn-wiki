The Chinese-remainder map relabels the positions of a sequence by their residues modulo several lengths, and it preserves the [cyclic convolution](cyclic-convolution.md) of that sequence. It acts on the coefficients of a [radix-digit convolution](radix-digit-convolution.md) before any transform is computed, turning one cyclic convolution into a convolution over several cyclic axes at once.

Let $d$ be the number of axes, and let $m_i$ be the length of the $i$-th axis for $i = 1,\dots,d$, with the lengths pairwise coprime, so no two share a prime factor. Let $N = m_1 m_2 \cdots m_d$ be the number of coefficient positions.

Positions are $x = 0,\dots,N-1$, and $x'$ denotes a second position. The map sends $x$ to the tuple $(x \bmod m_1, \dots, x \bmod m_d)$, a point of the box with sides $m_1,\dots,m_d$. The Chinese remainder theorem says these residues determine $x$ and every tuple arises from exactly one position, so the map is a bijection between the $N$ positions and the $N$ box points.

A convolution over the box sums products of entries over pairs of box points whose coordinates add, each coordinate modulo its own length. The original convolution sums $a_x b_{x'}$ over pairs with $x+x' \equiv z \pmod N$, for a target position $z$. Addition is respected: $(x+x') \bmod m_i = (x \bmod m_i + x' \bmod m_i) \bmod m_i$ for each $i$, and since $m_i$ divides $N$, the residue of $(x+x') \bmod N$ modulo $m_i$ is the same. So the image of $z$ is the coordinatewise sum of the images of $x$ and $x'$. As the map is a bijection, each pair with $x+x' \equiv z$ corresponds to exactly one pair of box points with coordinate sums equal to the image of $z$, so the two sums agree term by term.

Example: $N = 15 = 3 \cdot 5$. Position $7$ maps to $(1,2)$ and position $11$ maps to $(2,1)$. Their sum is $18 \equiv 3 \pmod{15}$, and position $3$ maps to $(0,3)$, which equals $(1+2 \bmod 3,\ 2+1 \bmod 5)$.

The paper's first step is a relabeling of this kind, with distinct primes as axis lengths. <cite data-source="paper">First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.</cite>
