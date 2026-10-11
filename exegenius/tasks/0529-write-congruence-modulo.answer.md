Congruence is defined on pairs of [Integer](integer.md) values: two of them are congruent when they differ by a multiple of a fixed positive integer. It is the arithmetic behind the [Chinese-remainder map](chinese-remainder-map.md), which places coefficients on distinct prime cyclic axes, and behind the [centered residue](centered-residue.md), which recovers a signed coefficient from its remainder.

## Definition

Let $B$ be a positive integer, the modulus, and let $d$ and $e$ be integers. Then $d$ and $e$ are congruent modulo $B$, written $d \equiv e \pmod B$, when $B$ divides $d-e$, that is, $d-e=\xi B$ for some integer $\xi$. The set of all integers is written $\mathbb{Z}$.

Congruence is an equivalence relation: $B$ divides $0$; $B$ divides $d-e$ exactly when it divides $e-d$; and if $d \equiv e$ and $e \equiv \zeta$, then $d-\zeta=(d-e)+(e-\zeta)$ is a sum of two multiples of $B$. So each integer lies in exactly one residue class, the set of integers $\sigma$ with $\sigma \equiv d \pmod B$.

Each class contains exactly one integer $\delta$ in $\{0,\dots,B-1\}$, its remainder. To find it, take the largest multiple $kB$ of $B$ with $kB \le d$. Then $\delta = d-kB$ satisfies $0 \le \delta < B$ and $\delta \equiv d$. It is unique because two integers in $\{0,\dots,B-1\}$ differ by less than $B$, so their difference cannot be a nonzero multiple of $B$.

Congruence respects sums and products. Let $d' \equiv d$ and $e' \equiv e$ modulo $B$, with $d'-d = \xi B$ and $e'-e = \eta B$. Then $(d'+e')-(d+e) = (\xi+\eta)B$, and since $d'e'-de = d'(e'-e)+e(d'-d)$,

$$d'e'-de = (d'\eta+e\xi)B.$$

## Use in the paper

Congruence is applied in [Carry propagation](carry-propagation.md): each output digit is the residue of the input coefficient plus the incoming carry. Here $u_j$ is the input coefficient at position $j$, $\gamma_j$ is the carry into position $j$, $d_j$ is the output digit at position $j$, $\gamma_{j+1}$ is the carry into position $j+1$, and $B$ stands for the paper's $B_0$. The paper says to <cite data-source="paper">start with carry γ0 = 0</cite>, and to write <cite data-source="paper">dj ≡ uj + γj</cite> with $0 \le d_j < B$:

$$d_j \equiv u_j + \gamma_j \pmod B, \qquad \gamma_{j+1} = \frac{u_j + \gamma_j - d_j}{B}.$$

The congruence says $B$ divides $u_j+\gamma_j-d_j$, so $\gamma_{j+1}$ is an integer. For $B = 10$, $u_j = 27$ and $\gamma_j = 0$, the digit is $d_j = 7$ and the carry is $\gamma_{j+1} = (27-7)/10 = 2$.

The paper recovers each signed coefficient as the <cite data-source="paper">unique integer in [−B0 /2, B0 /2) congruent to qj + ρj modulo B0</cite>. The interval $[-B/2, B/2)$ holds $B$ consecutive integers: $-h,\dots,h-1$ when $B=2h$, and $-h,\dots,h$ when $B=2h+1$. Two of them differ by less than $B$, so they lie in different classes and cover all $B$ classes. For $B = 10$ the interval is $\{-5,\dots,4\}$, so the residue $7$ is recovered as $-3$.
