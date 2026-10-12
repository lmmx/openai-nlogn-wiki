The Chinese-remainder map is a relabeling of coefficient positions by their residues modulo several pairwise coprime lengths. It preserves the [cyclic convolution](cyclic-convolution.md) of a sequence. It acts on the coefficients of a [radix-digit convolution](radix-digit-convolution.md) before any transform is computed, turning one cyclic convolution into a convolution over several cyclic axes at once.

Let $K$ be the number of axes, and let $M_\nu$ be the length of axis $\nu$ for $\nu = 1,\dots,K$, with the lengths pairwise coprime, so no two share a prime factor. Let $N = M_1 M_2 \cdots M_K$ be the number of coefficient positions.

Positions are $p = 0,\dots,N-1$, and $p'$ denotes a second position. The map sends $p$ to the tuple $(p \bmod M_1, \dots, p \bmod M_K)$, a point of the box with sides $M_1,\dots,M_K$, meaning the tuples whose $\nu$-th entry lies in $\{0,\dots,M_\nu-1\}$. The Chinese remainder theorem says these residues determine $p$ and that every tuple arises from exactly one position, so the map is a bijection, a one-to-one correspondence, between the $N$ positions and the $N$ box points.

A convolution over the box sums products of entries over pairs of box points whose coordinates add, each coordinate modulo its own length. The original convolution sums $a_p b_{p'}$ over pairs with $p + p' \equiv \ell \pmod N$, for a target position $\ell$.

Addition is respected: $(p + p') \bmod M_\nu = (p \bmod M_\nu + p' \bmod M_\nu) \bmod M_\nu$ for each $\nu$. Since $M_\nu$ divides $N$, reducing $(p + p') \bmod N$ modulo $M_\nu$ gives the same residue. So the image of $\ell$ is the coordinatewise sum of the images of $p$ and $p'$. As the map is a bijection, each pair with $p + p' \equiv \ell$ corresponds to exactly one pair of box points whose coordinate sums equal the image of $\ell$, so the two sums agree term by term.

Example: $N = 15 = 3 \cdot 5$, so $M_1 = 3$ and $M_2 = 5$. Position $7$ maps to $(1,2)$ and position $11$ maps to $(2,1)$. Their sum is $18 \equiv 3 \pmod{15}$, and position $3$ maps to $(0,3)$, which equals $(1+2 \bmod 3,\ 2+1 \bmod 5)$.

The paper's first step is a relabeling of this kind, with distinct primes as axis lengths. <cite data-source="paper">First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.</cite>
