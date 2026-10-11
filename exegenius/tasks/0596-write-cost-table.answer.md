The cost table is the last accounting step of the proof. It lists the separate running-time terms of the algorithm, each a power of one size parameter, whose sum bounds the total time. It is the step that <cite data-source="paper">makes all terms in its cost table fit Theorem 1.</cite>

## Sizes and parameters

Write $b = \lceil \log_2 n \rceil$ for the rounded-up base-2 logarithm of $n$, the number of bits of $n$ (the letter $b$ changes meaning here). Write $p = 6b$ for the working precision in bits (<cite data-source="paper">p = 6b</cite>), so $p = \Theta(\log n)$. Write $T$ for the number of cells of the padded box (the letter $T$ changes meaning here). The paper takes <cite data-source="paper">Take the power of two T in [4n/b, 8n/b)</cite>, so $4n/b \le T < 8n/b$. Since $2^{b-1} < n \le 2^b$ and $b \ge 8$, we have $4n/b > 2^{b/2}$ and $8n/b \le 2^b$, so $b/2 < \log_2 T < b$.

The fixed exponents $\epsilon = 2^{-75}$, $c = 2^{-56}$, $\tau = 1-2^{-50}$, $\lambda' = 1-2^{-54}$ and $\delta = 1/16$ are constants of the construction (the letters $c$, $\tau$ and $\delta$ change meaning here), and $\epsilon$ is not the tolerance $\varepsilon$ of limit arguments. The factor $\alpha$ scales the cost of the line maps, a line being a slice of the box along one axis (the letter $\alpha$ changes meaning here). <cite data-source="paper">The choice of α gives α = Θ(p1/4+ϵ/2 )</cite>.

The volume of the box is $\Upsilon = Tp = \Theta(n)$ (<cite data-source="paper">T p = Θ(n)</cite>). Write $d = \lfloor b^{\epsilon} \rfloor = \Theta(p^{\epsilon})$ for the number of axes of the box (the letter $d$ changes meaning here), and $K = \lfloor d^{c} \rfloor = \Theta(p^{\epsilon c})$ for the number of bits in each address chunk, a run of consecutive address bits (the letter $K$ changes meaning here).

## Axis lengths

Write $\ell = \lceil \log_2 T/d \rceil$ for the exponent with $r = 2^{\ell}$ (the letter $\ell$ changes meaning here). The paper sets <cite data-source="paper">let r = 2⌈(log2 T )/d⌉ and ℓ = log2 r</cite>. Each axis length is $r/2$ or $r$. With $k = d\ell - \log_2 T$, the ceiling gives $d(\ell-1) < \log_2 T \le d\ell$, so $0 \le k < d$. The construction chooses $k$ axis lengths to be $r/2$ (<cite data-source="paper">of the d axis lengths to be r/2 and the others to be r</cite>). The product is $2^{d\ell-k} = T$, and since $k < d$, one axis has length $r$, so $\ell$ is the largest axis exponent. For example, with $T = 2^{10}$ and $d = 3$, we get $\ell = 4$, $r = 16$, $k = 2$, and axis lengths $8, 8, 16$.

From $b/2 < \log_2 T < b$ we get $b/(2d) < \ell < b/d + 1$, so $\ell = \Theta(p^{1-\epsilon})$.

## Dividing the cost by the volume

The cost table splits the [running time cost](running-time-cost.md) of the algorithm into separate terms, one per kind of work. It divides every term by the [logical bit volume](logical-bit-volume.md) $\Upsilon$ of the box, so each term becomes a power of $p$ once $d$, $K$ and $\ell$ are substituted.

| Operation | Cost divided by $\Upsilon$ | Power of $p$ |
| --- | --- | --- |
| Prefix-slot moves and individual [butterfly rounds](transform-round.md) | $dK$ | $\epsilon(1+c)$ |
| Chunk exchanges for [transform layout](transform-layout.md) | $pK^{\tau-1}$ | $1-\epsilon c(1-\tau)$ |
| Simultaneous [butterfly rounds](transform-round.md) | $\ell d^{\lambda'}$ | $1-\epsilon(1-\lambda')$ |
| [CRT](chinese-remainder-theorem.md) and axis layouts | $d^2(1+\ell^{\tau})$ | $\tau+\epsilon(2-\tau)$ |
| [Gaussian line maps](gaussian-resampling.md) | $d\,p^{1/2+\delta}\alpha$ | $3/4+\delta+3\epsilon/2$ |
| Chirps, twists and scalar products | $d\,p^{\delta}$ | $\epsilon+\delta$ |
| Packed polynomial products | $\log(rp)$ | $1-\epsilon$ |
| Final scaling and rounding | $p^{\delta}$ | absorbed below |
| Input, padding, carries and output | $1$ | absorbed below |

The first row prices moves to their [destination rank](destination-rank.md), which use $O(dK)$ linear scans.

The second row bounds the cost of the chunk exchanges that produce the [transform layout](transform-layout.md). The layout uses <cite data-source="paper">O(p/K) exchanges of width-K chunks</cite>, each costing $O(\Upsilon K^{\tau})$, giving $pK^{\tau-1}$.

The third row prices each simultaneous [butterfly round](transform-round.md), which acts on all axes at once. There are at most $\ell$ rounds of cost $O(\Upsilon d^{\lambda'})$.

The fourth row bounds the cost of the axis exposure and restoration around the [Chinese remainder theorem](chinese-remainder-theorem.md) step: $O(d^2)$ axis moves of cost $O(\Upsilon(1+\ell^{\tau}))$ each.

The fifth row bounds the cost of the line maps of [Gaussian resampling](gaussian-resampling.md). An axis of length $t$ has at most $T/t$ lines, each costing $O(tp^{3/2+\delta}\alpha)$, so the $d$ axes cost $O(dTp^{3/2+\delta}\alpha)$. With $\alpha = \Theta(p^{1/4+\epsilon/2})$ and $d = \Theta(p^{\epsilon})$ the power is $\frac34+\delta+\frac{3\epsilon}{2}$, larger than the $\frac12+\delta+\epsilon$ that $d$ alone gives because of $\alpha$.

The chirp row covers chirp factors (phase factors quadratic in the position) and twists. The paper's bound for this work is <cite data-source="paper">its O(T dp1+δ ) cost</cite>, and dividing by $\Upsilon$ gives $dp^{\delta}$.

The packed row multiplies the $T/r$ records, each a polynomial with $r$ coefficients of $p$ bits. A record product is four integer products on $O(rp)$-bit integers, each costing $O(rp\log(rp))$ with the [established multiplier](established-multiplier.md), so the normalized cost is $\log(rp) = \ell + \log p$, and <cite data-source="paper">log(rp) = O(p1−ϵ + log p) = O(p1−ϵ )</cite>.

## Why every term fits

The margin of a power is one minus that power. Substitution gives the seven dominant margins:

$$1-\epsilon(1+c)>\tfrac12,\;\epsilon c(1-\tau)=2^{-181},\;\epsilon(1-\lambda')=2^{-129},$$

$$1-\tau-\epsilon(2-\tau)>2^{-51},\;\tfrac14-\delta-\tfrac32\epsilon>\tfrac18,\;1-\delta-\epsilon>\tfrac12,\;\epsilon=2^{-75}.$$

Since $\epsilon(2-\tau) < 2^{-74}$, the fourth exceeds $2^{-51}$. The smallest margin is $2^{-181} = 2\kappa$ with $\kappa = 2^{-182}$, so <cite data-source="paper">Each of the seven displayed powers is at most 1 − 2κ by (45).</cite>

A fixed power of $\log p$ is at most $p^{\kappa}$ for large $p$, so each dominant term is at most $Cp^{1-\kappa}$. The remaining rows are smaller still. So the table is $O(\Upsilon p^{1-\kappa}) = O(n(\lg n)^{1-\kappa})$, the bound of the [main theorem](main-theorem.md).
