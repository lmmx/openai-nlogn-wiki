The Chinese-remainder map relabels the positions of a sequence by their residues modulo several lengths, and it preserves the [cyclic convolution](cyclic-convolution.md) of that sequence. The map relabels the coefficients of a [radix-digit convolution](radix-digit-convolution.md) before any transform is computed. Its job is to turn one cyclic convolution into a convolution over several cyclic axes at once.

Let $k$ be the number of axes. Let $m_i$ be the length of the $i$-th axis, for $i = 1,\dots,k$, with the lengths pairwise coprime, so no two share a prime factor. Let $N = m_1 m_2 \cdots m_k$ be the number of coefficient positions.

Positions are $x = 0,\dots,N-1$. The Chinese remainder theorem says that the residues $x \bmod m_1, \dots, x \bmod m_k$ determine $x$, and that every tuple of residues arises from exactly one position. The map sends $x$ to the tuple $(x \bmod m_1, \dots, x \bmod m_k)$, a point of the box with sides $m_1, \dots, m_k$. Since there are $N$ positions and $N$ box points, this is a relabeling.

A second position is written $x'$. For each $i$, $(x+x') \bmod m_i = (x \bmod m_i + x' \bmod m_i) \bmod m_i$, and because $m_i$ divides $N$, $(x+x') \bmod N$ has the same residues. So adding two positions modulo $N$ means adding their coordinates separately, each modulo its own $m_i$. A wrap-around in the original sequence becomes a wrap-around along every axis, which is why the convolution is preserved.

Take $N = 15 = 3 \cdot 5$. Position $7$ maps to $(1,2)$ and position $11$ maps to $(2,1)$. Their sum is $18 \equiv 3 \pmod{15}$, and position $3$ maps to $(0,3)$, which equals $(1+2 \bmod 3,\ 2+1 \bmod 5)$.

The paper's first step is a relabeling of this kind, with distinct primes as axis lengths. <cite data-source="paper">First, the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.</cite>
