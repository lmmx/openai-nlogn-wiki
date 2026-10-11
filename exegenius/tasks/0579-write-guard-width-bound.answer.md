The guard-width bound reserves an explicit count $\Delta$ of extra fractional and integer bits per real component, which makes every intermediate coefficient of one [simultaneous butterfly layer](simultaneous-butterfly-layer.md) exact, so a single final truncation suffices.

The two-point map $H_0$ sends values $u,v$ to $((u+v)/2,(u-v)/2)$. Here $d$ is a bound on the number $D$ of selected bits, so $1\le D\le d$. The bound applies to the output of the [tensor product](tensor-product.md) of $D$ copies of the map.

The bound allows for operators that are not [linear contractions](linear-contraction.md), that is, linear maps that can increase the largest modulus of a vector. <cite data-source="paper">Its intermediate operators need not be contractions.</cite> Rounding after each stage would be unsafe, since errors need not shrink. <cite data-source="paper">The procedure evaluates the entire layer exactly before this final truncation.</cite>

The bound keeps every intermediate value in [Gaussian dyadics](gaussian-dyadics.md), since <cite data-source="paper">Intermediate values are exact Gaussian dyadics</cite>, so both denominators and magnitudes need limits. The paper starts with <cite data-source="paper">disk-valued coefficients in 2−p Z[i]</cite>, where $p$ is the fractional precision.

Let $\ell$ be the depth of a value, the number of operations on a chain that follows an operand from an input into it. The claim is that <cite data-source="paper">value at depth ℓ lies in 2−(p+ℓ) Z[i] and has modulus at most 2ℓ</cite>. Inputs have depth $0$. An operand of depth at most $\ell-1$ lies in $2^{-(p+\ell-1)}\mathbb{Z}[i]$ with modulus at most $2^{\ell-1}$, so a sum or difference of two such operands lies in $2^{-(p+\ell)}\mathbb{Z}[i]$ with modulus at most $2^\ell$, and a halving lies there with modulus at most $2^{\ell-2}$. For example, with $p=10$, $u=1$ and $v=2^{-10}$, the depth-2 value $(u+v)/2=(2^{10}+1)/2^{11}$ needs eleven fractional bits, so twelve reserved bits suffice.

Each call divides the axis count by $m$, the splitting factor. A group of $e$ selected axes splits into $s$ calls on groups of $e/m$ axes. Let $A(e)$ bound the operations on any chain within such a group, and let $E=64(W+m+1)^3$ be the most gate operations charged at a node. Then <cite data-source="paper">A(e) ≤ sA(e/m) + E</cite> at an internal node, and $A(e)\le 8e$ at a leaf. Let $k$ count the internal levels: <cite data-source="paper">There are at most k ≤ ⌈logm d⌉ internal levels.</cite>

Put $B=s+E$, so each level multiplies a bound of at least $1$ by $B$. Indeed, for any real number $x\ge1$, $sx+E\le Bx$. Every group has $e\le d$, so at a leaf $8e\le 8d\le 8dB$, and $k$ levels give $A(e)\le 8dB^{k+1}$. Let $\nu$ be the least $j\ge1$ with $m^j\ge B$, so $\log_m B\le\nu$. Then $B^{k+1}\le B^{\log_m d+2}=B^2d^{\log_m B}\le B^2d^\nu$, hence $A(e)\le 8B^2d^{\nu+1}$.

Preprocessing adds at most $md$ earlier pieces, <cite data-source="paper">For the sufficiently large sizes under consideration, the earlier piece count is at most md.</cite> each of depth at most $8B^2d^{\nu+1}$, so their depths add to at most $8mB^2d^{\nu+2}$. The at most $d$ individual kernels, each of depth $8$, add $8d$. The two outer phases cost two operations each, the scalar phase two and one optional factor three, so phases add at most $9$.

Here $\lfloor x\rfloor$ is the largest integer not exceeding $x$, and the shift is by $t=\lfloor D/2\rfloor$ places. <cite data-source="paper">The shift by t consumes t fractional bits, so we charge it t units of denominator growth</cite>. Here $C_0=128mB^2$ and $C_1=\max\{20,\nu+3\}$; <cite data-source="paper">the choice twenty leaves an explicit additional margin</cite>. Adding the counts,
$$8mB^2d^{\nu+2}+8d+t+9\le 8mB^2d^{\nu+2}+18d\le 26mB^2d^{\nu+2}<128mB^2d^{\nu+3}\le C_0d^{C_1},$$
using $d\ge1$, $mB^2\ge1$ and $C_1\ge\nu+3$. So every depth is at most $C_0d^{C_1}$, and $\Delta=\lceil C_0d^{C_1}\rceil$ bounds it.

Every value lies in $2^{-(p+\Delta)}\mathbb{Z}[i]$ with modulus at most $2^\Delta$, so $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits suffice. <cite data-source="paper">Shifts consume the reserved fractional zeros and discard no bits.</cite>

The exponent $\varepsilon$ is chosen with $0<\varepsilon<1$ and <cite data-source="paper">Choose ϵC1 < 1</cite>. The bound states the growth of $d$ with [Big-Theta notation](big-theta-notation.md): $d$ lies between two constant multiples of $p^{\varepsilon}$. Since $W$, $m$ and $s$ are fixed, $\Delta=O(p^{\varepsilon C_1})$. The bound states growth in the sense of [little-o notation](little-o-notation.md): $\Delta=o(p)$ means $\Delta/p\to0$, which holds because $\varepsilon C_1<1$.

Truncation (rounding toward zero to $2^{-p}\mathbb{Z}$) is safe: <cite data-source="paper">truncation cannot increase the absolute value of either component, and changes each by less than</cite> $2^{-p}$.
