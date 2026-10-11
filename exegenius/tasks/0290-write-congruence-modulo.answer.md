Congruence is defined on pairs of [Integer](integer.md) values: two of them are congruent when they leave the same remainder on division by a fixed positive integer. It is the arithmetic behind the [Chinese-remainder map](chinese-remainder-map.md), which places coefficients on distinct prime cyclic axes, and behind the [centered residue](centered-residue.md), which recovers a signed coefficient from its remainder.

## Definition

Let $B$ be a positive integer, the modulus, and let $d$ and $e$ be integers. Then $d$ and $e$ are congruent modulo $B$, written $d \equiv e \pmod B$, when $B$ divides $d-e$. The set of all integers is written $\mathbb{Z}$.

Congruence is an equivalence relation: $d \equiv d$; $d \equiv e$ implies $e \equiv d$; and $d \equiv e$ with $e \equiv f$ implies $d \equiv f$, since $d-f = (d-e)+(e-f)$. So each integer lies in exactly one residue class. Here $\nu$ is an integer in the class of $d$, and the residue class of $d$ is

$$\{\, \nu \in \mathbb{Z} : \nu \equiv d \pmod B \,\}.$$

Each class contains exactly one integer $\delta$ in $\{0,\dots,B-1\}$, its remainder. Such a $\delta$ exists because $d$ differs from a multiple of $B$ by $\delta$. It is unique because two integers in $\{0,\dots,B-1\}$ differ by less than $B$. So there are $B$ classes.

For example, with $B = 7$: $23 \equiv 2 \pmod 7$, since $23 - 2 = 3 \cdot 7$, and $-5 \equiv 2 \pmod 7$, since $-5 + 7 = 2$.

Congruence respects sums and products. Let $d'$ be an integer congruent to $d$ modulo $B$, and let $e'$ be an integer congruent to $e$ modulo $B$. Then $d'+e' \equiv d+e$ and $d'e' \equiv de \pmod B$.

## Use in the paper

Congruence is applied in [Carry propagation](carry-propagation.md): each output digit is the residue of the input coefficient plus the incoming carry. The paper says to <cite data-source="paper">start with carry γ0 = 0</cite>, with <cite data-source="paper">dj ≡ uj + γj</cite>. Here $u_j$ is the input coefficient at position $j$, $\gamma_j$ is the carry into it, and $B$ stands for the paper's $B_0$:

$$d_j \equiv u_j + \gamma_j \pmod B, \qquad \gamma_{j+1} = \frac{u_j + \gamma_j - d_j}{B}.$$

For $B = 10$, $u_j = 27$ and $\gamma_j = 0$, the digit is $7$ and the carry is $(27-7)/10 = 2$.

The paper recovers each signed coefficient as the <cite data-source="paper">unique integer in [−B0 /2, B0 /2) congruent to qj + ρj modulo B0</cite>. The interval $[-B/2, B/2)$ holds exactly one integer from each class, so a coefficient of either sign is determined by its residue.
