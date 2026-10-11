Congruence is the relation between two integers that they leave the same remainder when divided by a fixed positive integer. It is the arithmetic behind the [Chinese-remainder map](chinese-remainder-map.md), which places coefficients on distinct prime cyclic axes, and behind the [centered residue](centered-residue.md) that recovers a signed coefficient from its remainder.

## Definition

Let $m$ be a positive integer, the modulus, and let $d$ and $e$ be integers. Then $d$ and $e$ are congruent modulo $m$, written $d \equiv e \pmod m$, when $m$ divides their difference, that is, when $(d-e)/m$ is an integer. The residue class of $d$ modulo $m$ is the set of all integers $w$ congruent to $d$ modulo $m$:

$$\{\, w \in \mathbb{Z} : w \equiv d \pmod m \,\}.$$

Each integer lies in exactly one of the $m$ residue classes. Each class has a least nonnegative member, its remainder in $\{0, 1, \dots, m-1\}$.

For example, take $m = 7$. We have $23 \equiv 2 \pmod 7$, since $23 - 2 = 21 = 3 \cdot 7$. Also $-5 \equiv 2 \pmod 7$, since $-5 - 2 = -7$. The class of $2$ contains $\dots, -5, 2, 9, 16, \dots$, and the remainder of $-5$ is $2$, because $-5 + 7 = 2$.

Congruence respects sums and products: if $d \equiv d' \pmod m$ and $e \equiv e' \pmod m$, then $d + e \equiv d' + e' \pmod m$ and $de \equiv d'e' \pmod m$. For instance, $23 \cdot 5 = 115 \equiv 2 \cdot 5 = 10 \equiv 3 \pmod 7$, which agrees with $115 = 16 \cdot 7 + 3$.

## Use in the paper

Carry propagation is a congruence computation. The paper forms a sum by starting with carry zero and writing each output digit as the residue of the input coefficient plus the incoming carry: <cite data-source="paper">dj ≡ uj + γj</cite>. For the modulus $10$, the integer $27$ gives the digit $27 \equiv 7 \pmod{10}$ and the carry $(27-7)/10 = 2$, since $27 = 7 + 2 \cdot 10$.

The paper recovers each signed coefficient as the <cite data-source="paper">unique integer in [−B0 /2, B0 /2) congruent to qj + ρj modulo B0</cite>, so a coefficient of either sign is determined by its residue.
