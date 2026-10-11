The cost table is the last accounting step of the paper, the one that <cite data-source="paper">makes all terms in its cost table fit Theorem 1.</cite> It lists the separate running-time terms of the algorithm, each a power of one size parameter, so that their sum bounds the total time. It shows that the algorithm meets the bound $O(n(\lg n)^{1-\kappa})$ of the [main theorem](main-theorem.md).

## Dividing the cost by a volume

Write $b = \lceil \log_2 n \rceil$ for the rounded-up base-2 logarithm of $n$, the number of bits of $n$. Write $p = 6b$ for the working precision in bits, so $p = \Theta(\log n)$ (<cite data-source="paper">p = 6b</cite>). Write $T$ for the number of cells of the padded box, the array the algorithm works on, a power of two chosen with <cite data-source="paper">Take the power of two T in [4n/b, 8n/b)</cite>, so $4n/b \le T < 8n/b$.

The cost table splits the [running time cost](running-time-cost.md) of the algorithm into separate terms, one for each kind of work. The cost table divides every term by the [logical bit volume](logical-bit-volume.md) $V = Tp$ of the padded box, so each term becomes a power of one size parameter. Here $V = Tp = \Theta(n)$ (<cite data-source="paper">T p = Θ(n)</cite>).

The exponents are fixed rationals: <cite data-source="paper">The exponents can all be chosen rational</cite>. The exponent $\epsilon$ is a fixed positive rational number, not the tolerance $\varepsilon$ of the limit inferior. The exponent $c$ is a fixed positive rational number. The exponent $\delta$ is a fixed rational number. The paper's choice is <cite data-source="paper">Take the following fixed rational numbers:</cite> $\epsilon = 2^{-75}$, $c = 2^{-56}$, $\tau = 1-2^{-50}$, $\lambda' = 1-2^{-54}$ and $\delta = 1/16$. The factor $\alpha$ scales the cost of the line maps, and <cite data-source="paper">The choice of α gives α = Θ(p1/4+ϵ/2 )</cite>.

Write $d = \lfloor b^{\epsilon}\rfloor = \Theta(p^{\epsilon})$ for the number of axes of the padded box. Write $K = \lfloor d^{c}\rfloor = \Theta(p^{\epsilon c})$ for the width of the address chunks, which are runs of consecutive address bits, in bits (the letter $K$ changes meaning here). Write $r$ for the largest axis length of the padded box, a power of two (the letter $r$ changes meaning here: it is an axis length, not the record length of the polynomial ring), and $\ell = \log_2 r$.

The construction sets <cite data-source="paper">let r = 2⌈(log2 T )/d⌉ and ℓ = log2 r</cite>. The construction picks $d\ell - \log_2 T$ of the axis lengths to be $r/2$ and the rest to be $r$ (<cite data-source="paper">of the d axis lengths to be r/2 and the others to be r</cite>), so the $d$ axis lengths multiply to $T$ and $d(\ell-1) \le \log_2 T \le d\ell$. Hence $\ell = \lceil \log_2 T / d \rceil$. Since <cite data-source="paper">bounds on n, T give b/2 ≤ log2 T ≤ b.</cite>, we get $b/(2d) \le \ell \le b/d + 1$. As $p = 6b$ and $d = \Theta(p^{\epsilon})$, this gives $\ell = \Theta(p^{1-\epsilon})$.

## The table

| Operation | Cost divided by $V$ | Power of $p$ |
| --- | --- | --- |
| [Prefix-slot moves](destination-rank.md) and individual [butterfly rounds](transform-round.md) | $dK$ | $\epsilon(1+c)$ |
| Chunk exchanges for [transform layout](transform-layout.md) | $pK^{\tau-1}$ | $1-\epsilon c(1-\tau)$ |
| Simultaneous [butterfly rounds](transform-round.md) | $\ell d^{\lambda'}$ | $1-\epsilon(1-\lambda')$ |
| [CRT](chinese-remainder-theorem.md) and axis layouts | $d^2(1+\ell^{\tau})$ | $\tau+\epsilon(2-\tau)$ |
| [Gaussian line maps](gaussian-resampling.md) | $d\,p^{1/2+\delta}\alpha$ | $3/4+\delta+3\epsilon/2$ |
| Chirps, twists and scalar products | $d\,p^{\delta}$ | $\epsilon+\delta$ |
| Packed polynomial products | $\log(rp)$ | $1-\epsilon$ |
| Final scaling and rounding | $p^{\delta}$ | absorbed below |
| Input, padding, carries and output | $1$ | absorbed below |

A packed polynomial product multiplies two records (polynomials with $r$ coefficients of $p$ bits each) by packing each record into one long integer and multiplying the integers, so its cost is the entry $\log(rp)$. Here $\log(rp) = \ell + \log p$, and <cite data-source="paper">log(rp) = O(p1−ϵ + log p) = O(p1−ϵ )</cite>.

The first row bounds the cost of moves to their [destination rank](destination-rank.md). The second row bounds the cost of the chunk exchanges that produce the [transform layout](transform-layout.md). The third row bounds the cost of each simultaneous [transform round](transform-round.md). The fourth row prices the cost of the [Chinese remainder theorem](chinese-remainder-theorem.md) step. The fifth row prices the line maps of [Gaussian resampling](gaussian-resampling.md).

## Why every term fits

The margin of a power is one minus that power. The margins $g_i$ of the seven dominant powers, in table order, are

$$g_1 = 1-\epsilon(1+c) > \tfrac12, \quad g_2 = \epsilon c(1-\tau) = 2^{-75}\cdot 2^{-56}\cdot 2^{-50} = 2^{-181}, \quad g_3 = \epsilon(1-\lambda') = 2^{-129},$$

$$g_4 = 1-\tau-\epsilon(2-\tau) > 2^{-51}, \quad g_5 = \tfrac14-\delta-\tfrac32\epsilon > \tfrac18, \quad g_6 = 1-\delta-\epsilon > \tfrac12, \quad g_7 = \epsilon = 2^{-75}.$$

For $g_4$, $\epsilon(2-\tau) < 2^{-74}$, so $g_4 > 2^{-50}-2^{-74} > 2^{-51}$. The smallest margin is $g_2 = 2^{-181} = 2\kappa$ with <cite data-source="paper">κ = 2−182</cite>, and <cite data-source="paper">Thus mini gi = 2−181 = 2κ.</cite> <cite data-source="paper">Each of the seven displayed powers is at most 1 − 2κ by (45).</cite> Since <cite data-source="paper">Any fixed power of log p is at most pκ eventually.</cite>, each of the seven terms is at most a constant times $p^{1-\kappa}$.

The final scaling row $p^{\delta}$ is at most $d\,p^{\delta}$, the chirp row, since $d \ge 1$, and the input row $1$ is at most $p^{1-\kappa}$. So the table is $O(Vp^{1-\kappa})$, which with $V = \Theta(n)$ and $p = \Theta(\log n)$ is $O(n(\lg n)^{1-\kappa})$, the bound of the [main theorem](main-theorem.md).
