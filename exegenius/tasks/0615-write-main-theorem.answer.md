This page states the main theorem, the target of the wiki: one fixed deterministic machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ steps, with $\kappa = 2^{-182}$.

## The statement

Let $x$ and $y$ be the two binary input strings, each of length $n$, written $x\#y$ with $\#$ a separator. For a binary string $w$, $\mathrm{val}(w)$ is its value, with the leftmost bit most significant. The output is the $2n$-bit binary form of $\mathrm{val}(x)\cdot\mathrm{val}(y)$. For example, $x=1011$ and $y=0110$ give $01000010$, since $11\cdot 6=66$.

<cite data-source="paper">There is one deterministic Turing machine A</cite>, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, computes this exact product for every $n\ge 1$. The theorem is stated in the [Fixed-tape machine model](fixed-tape-model.md), so neither the alphabet nor the number of tapes depends on $n$. Its time is measured by the [Running time cost](running-time-cost.md) of $A$, written $T_A(n)$, the largest number of steps $A$ takes on an input of length $n$. The bound is stated with the [Logarithm](logarithm.md) to base two. Here $\lg n=\max\{\lceil\log_2 n\rceil,1\}$, and the claim is $T_A(n)=O(n(\lg n)^{1-\kappa})$.

## Why it improves on $n\lg n$

Schönhage and Strassen <cite data-source="paper">proposed n log n as the optimal order of growth</cite>. The theorem refutes [The n log n optimality conjecture](n-log-n-conjecture.md) in this model. Its bound is $n\lg n$ times $(\lg n)^{-\kappa}$, which is below half of $n\lg n$ only once $\lg n>2^{2^{182}}$.

## Where the saving comes from

The theorem gets its power saving from the [Rank-saving recursion](rank-saving-recursion.md). A call works on a stored volume $V$, the number of stored bits it holds. A call has a parameter $e$ that counts field digits or selected axes. Here $m$ is the growth factor of the parameter. Here $W$ is the number of pieces a call divides its volume into. <cite data-source="paper">Fix integers m, W ≥ 2</cite>. <cite data-source="paper">A recursive call at parameter mf therefore uses s calls at parameter f</cite>. Here $s$ is the number of smaller calls that one call makes, each on a stream of $V/W$ bits. <cite data-source="paper">the total number s of smaller calls satisfies s < W m</cite>. The source proves it in its network construction, and this page takes it as given.

Let $F_k$ be the time per unit volume of a call at parameter $m^k$, which has $k$ levels of recursion beneath it. Its $s$ children cost $(s/W)F_{k-1}$ per unit volume in total. The node's own work is the omitted term: <cite data-source="paper">Pushing, popping, copying, resetting and clearing at this node cost its own volume times</cite> a fixed constant, an $O(1)$ term at each level. So $F_k\le (s/W)F_{k-1}+O(1)$, with $F_0=O(1)$.

Let $\log_m x$ denote the number $t$ with $m^t=x$. Set $\rho=s/W$, the ratio of child calls to pieces. Since $s<Wm$, we have $\rho<m$, so $\log_m \rho<1$, because $\log_m$ increases and $\log_m m=1$. <cite data-source="paper">Choose a rational number τ ∈ (0, 1) with s/W < mτ</cite>. Here $\tau$ is the saving exponent, with $\rho<m^{\tau}$. Unrolling the recurrence bounds $F_k$ by a fixed multiple of $\sum_{j<k}\rho^j$ plus $\rho^kF_0$. That sum is $O(k)$ if $\rho\le 1$ and $O(\rho^k)$ if $\rho>1$, so $F_k=O(m^{k\tau})$. Thus a call at parameter $e=m^k$ costs $O(e^{\tau})$ per unit volume, with $\tau<1$.

## Tying the parameter to $n$

Let $b=\lceil\log_2 n\rceil$ be the bit length of $n$. Here $p=6b$ is the working precision in bits, so $p=\Theta(\lg n)$. The source sets <cite data-source="paper">p = 6b</cite>. Here $\epsilon$ is a fixed exponent with $0<\epsilon<1$. The numerical layer has a bound $d$ on its number of selected axes, with $d=\Theta(p^{\epsilon})$. The source writes <cite data-source="paper">d = Θ(pϵ )</cite>. The source gives no reason for this choice. Since the cost per unit volume is a power of the parameter, a power of $p$ for $d$ makes it a power of $\lg n$.

The levels are few: <cite data-source="paper">There are at most k ≤ ⌈logm d⌉ internal levels</cite>. Since $m^{\lceil\log_m d\rceil}<m\cdot m^{\log_m d}=md$, the top parameter is $e=m^k\le md$. So the cost per unit volume is $O(d^{\tau})=O(p^{\epsilon\tau})=O((\lg n)^{\epsilon\tau})$. A compatible choice of rational parameters <cite data-source="paper">makes all terms in its cost table fit Theorem 1</cite>.

## Small inputs and fixed constants

The theorem handles small inputs by [Schoolbook multiplication](schoolbook-multiplication.md), which is quadratic in the number of digits. <cite data-source="paper">Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook</cite> multiplication below it. <cite data-source="paper">All these numbers are fixed, independently of any eventual input length.</cite>

## Why the method is needed

Let $C$ be the number of cells of the padded box, the array the transforms act on. It is a power of two with <cite data-source="paper">Take the power of two T in [4n/b, 8n/b)</cite>, so the transforms have $\Theta(\lg n)$ levels. <cite data-source="paper">For the cost calculation put V = T p = Θ(n).</cite> A full scan per level therefore costs $\Theta(n\lg n)$, the conjectured order and no better. Each stage instead costs $V$ times a power of its parameter, as in <cite data-source="paper">Its cost is O(V uτ ) for a fixed τ < 1.</cite>

## How the argument proceeds

1. The theorem reduces exact multiplication to [Radix-digit convolution](radix-digit-convolution.md) of short integer coefficients. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite>
2. The Fourier transforms become multidimensional transforms of power-of-two lengths. <cite data-source="paper">replaces the Fourier transforms needed for this convolution</cite> The theorem keeps its permutations inside a [Transform identity with retained permutations](transform-identity.md).
3. Here $z$ is the polynomial variable, which the source writes as $y$. One coordinate is stored as a polynomial in $z$ modulo $z^r+1$, where $r$, the number of coefficients, is a power of two. <cite data-source="paper">a polynomial modulo y r + 1, with r a power of two.</cite>
4. The theorem lays out its transforms by a [Transform layout](transform-layout.md), which places the selected bits of all transform axes at a common offset. <cite data-source="paper">place the selected bits of the participating</cite>
5. The theorem adds selected bits by [Packed selected-bit addition](packed-bit-addition.md). <cite data-source="paper">We implement a binary row addition on corresponding selected bits in two address chunks.</cite>
6. The theorem places coefficients on axes by a [Chinese-remainder map](chinese-remainder-map.md) that preserves convolution. <cite data-source="paper">by a Chinese-remainder map that preserves convolution</cite>
7. The theorem chooses its axis lengths by [Prime source lengths](prime-source-lengths.md), which are distinct odd primes close to powers of two. <cite data-source="paper">The distinct prime lengths si must be close to the powers of two ti</cite>
8. The theorem turns the last coordinate into a polynomial by a [Phase twist](phase-twist.md). <cite data-source="paper">A phase twist changes the last cyclic coordinate into a polynomial</cite>
9. The theorem computes the remaining axes by [Convolution over the polynomial ring](polynomial-ring-convolution.md). <cite data-source="paper">Sections 6 and 7 compute convolution on the remaining axes over this polynomial ring</cite>
10. The theorem recovers the coefficients by rounding through [Exact coefficient recovery](recovery-and-error.md). <cite data-source="paper">proves that the recovered coefficient error is strictly below 1/2</cite> Rounding then gives exact integers.
11. The theorem ends with [Carry propagation](carry-propagation.md), which turns the recovered coefficients into the exact binary product. <cite data-source="paper">propagates carries to obtain the exact binary product</cite>
