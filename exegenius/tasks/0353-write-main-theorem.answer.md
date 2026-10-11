This page states the main theorem, the target of the whole argument: one fixed deterministic machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ steps, where $\lg n = \max\{\lceil\log_2 n\rceil, 1\}$ is the base-two logarithm of $n$, rounded up and at least 1. It disproves [The n log n optimality conjecture](n-log-n-conjecture.md) in this model, and each later page establishes one step of the argument for this bound.

## The statement

For a binary string $x$, $\mathrm{val}(x)$ denotes its nonnegative integer value, with the leftmost bit most significant. The input is $x\#y$, with $x$ and $y$ binary strings of length $n$, and the output is the $2n$-bit binary form of $\mathrm{val}(x)\cdot\mathrm{val}(y)$. For example, take $n=4$, $x=1011$ and $y=0110$. Here $\mathrm{val}(x)=11$ and $\mathrm{val}(y)=6$, and the output is $01000010$, the eight-bit form of $66$.

<cite data-source="paper">There is one deterministic Turing machine A, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product</cite>. The theorem is stated in the [Fixed-tape machine model](fixed-tape-model.md): the alphabet and the number of tapes do not depend on the input. The machine's time is measured by the [Running time cost](running-time-cost.md) $T_A(n)$, the worst-case number of steps of $A$ on inputs of length $n$. The claim is $T_A(n) = O(n(\lg n)^{1-\kappa})$ for every $n \ge 1$, with $\kappa = 2^{-182}$.

The bound is stated with the [Logarithm](logarithm.md) to base two. <cite data-source="paper">The constants and thresholds in the construction are extremely large</cite>, so it bounds machine steps, not the speed of a practical multiplier.

## Why the bound is an improvement

Schönhage and Strassen <cite data-source="paper">conjectured n log n as the optimal order of multiplication cost</cite>. For large $n$ the theorem is faster than [Schoolbook multiplication](schoolbook-multiplication.md), which takes quadratic time in the number of digits. The bound is $n\lg n$ times $(\lg n)^{-\kappa}$. This factor is below one half exactly when $(\lg n)^{\kappa}>2$, that is, when $\lg n > 2^{1/\kappa} = 2^{2^{182}}$.

## Where the saving comes from

The theorem gets its power saving from the [Rank-saving recursion](rank-saving-recursion.md): a call splits into smaller calls, each working on a stream holding a fraction of the stored bits. Let $V$ be the number of stored bits a call works on. A call at parameter $m\ell$ makes $s$ child calls at parameter $\ell$, each on a stream of volume $V/W$. Here $m$ is the parameter's growth factor and $W$ the number of pieces. <cite data-source="paper">the total number s of smaller calls satisfies s < W m</cite>.

Let $\gamma(\ell)$ be the cost of a call at parameter $\ell$ divided by its volume. The child calls run one after another, so their costs add to $s\cdot(V/W)\cdot\gamma(\ell)$. Dividing by $V$ gives $\gamma(m\ell)\approx (s/W)\,\gamma(\ell)$. The approximation omits the node's own work: <cite data-source="paper">Pushing, popping, copying, resetting and clearing at this node cost its own volume times a fixed constant</cite>, and these costs enter the same sum over levels.

After $k$ levels the cost per volume is multiplied by $(s/W)^k = (m^k)^{\log_m(s/W)}$, where $\log_m x$ is the number $e$ with $m^e = x$. Since $s<Wm$, $\log_m(s/W)<1$. The cost thus grows as a power of the parameter with exponent below one.

The parameter is tied to $n$. The working precision is $p = 6b$ with <cite data-source="paper">b = ⌈log2 n⌉</cite>, so $p=\Theta(\lg n)$, where $\Theta(f(n))$ denotes a quantity lying between two positive constant multiples of $f(n)$ for all large $n$. The layer uses <cite data-source="paper">d = Θ(pϵ ),</cite> so $d=\Theta(p^{\epsilon})$ for a fixed $\epsilon$ with $0<\epsilon<1$. <cite data-source="paper">There are at most k ≤ ⌈logm d⌉ internal levels</cite>, so $m^k\le md$. The cost is therefore at most a constant times $d^{\log_m(s/W)}=\Theta(p^{\epsilon\log_m(s/W)})$, a power of $\lg n$ with exponent below one.

The saving holds at every input length because its ingredients are fixed. <cite data-source="paper">All these numbers are fixed, independently of any eventual input length.</cite> Small inputs are covered by <cite data-source="paper">Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook</cite> multiplication below it.

## Why the method is needed

<cite data-source="paper">For the cost calculation put V = T p = Θ(n).</cite> A scan reads each stored bit once, so it costs $\Theta(n)$. <cite data-source="paper">Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n).</cite> A full scan per level gives the conjectured cost and no better. The levels must together cost less than $n\lg n$. The recursion achieves this: the work at depth $j$ is $V(s/W)^j$, and $s/W<m$ keeps this below the parameter's growth. <cite data-source="paper">The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers.</cite>

## How the argument proceeds

1. The first step reduces multiplication to a [Radix-digit convolution](radix-digit-convolution.md) of short integer coefficients, obtained by splitting each input into radix digits (blocks of consecutive bits). <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite>
2. The Fourier transforms are replaced by multidimensional transforms whose axis lengths are powers of two. <cite data-source="paper">it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two</cite>.
3. Then <cite data-source="paper">one coordinate is stored as the coefficient list of a polynomial modulo y r + 1, with r a power of two.</cite> <cite data-source="paper">Powers of y then serve as roots of unity in the remaining axes</cite>, and <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>.
4. The method lays out the transforms by a [Transform layout](transform-layout.md), so that a butterfly layer can act on every transform round. <cite data-source="paper">place the selected bits of the participating axes at a common offset in consecutive K-bit chunks</cite>.
5. The machine adds selected bits by [Packed selected-bit addition](packed-bit-addition.md). <cite data-source="paper">We implement a binary row addition on corresponding selected bits in two address chunks.</cite>
6. The method places coefficients on distinct axes by a [Chinese-remainder map](chinese-remainder-map.md) that preserves convolution. <cite data-source="paper">the radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution</cite>. The theorem chooses its axis lengths by [Prime source lengths](prime-source-lengths.md): distinct odd primes close to powers of two. <cite data-source="paper">The distinct prime lengths si must be close to the powers of two ti</cite>.
7. The method keeps permutations inside the [Transform identity with retained permutations](transform-identity.md), so the source and target coordinate permutations need not be executed as sorts. [Bluestein's chirp identity](bluestein-chirp-identity.md) <cite data-source="paper">converts the middle transform, including its target permutation</cite> into a normalized cyclic convolution.
8. The method turns the last cyclic coordinate into a polynomial by [Phase twist](phase-twist.md). <cite data-source="paper">A phase twist changes the last cyclic coordinate into a polynomial</cite>.
9. The method handles the remaining axes by [Convolution over the polynomial ring](polynomial-ring-convolution.md). <cite data-source="paper">Sections 6 and 7 compute convolution on the remaining axes over this polynomial ring</cite>.
10. The method recovers the coefficients by rounding through [Exact coefficient recovery](recovery-and-error.md), which shows that the error is below one half. <cite data-source="paper">proves that the recovered coefficient error is strictly below 1/2</cite>.
11. The algorithm ends with [Carry propagation](carry-propagation.md), which turns the recovered coefficients into the exact binary product. <cite data-source="paper">propagates carries to obtain the exact binary product</cite>.

Each stage is charged to the stored volume $V$: its cost is $V$ times a power of its parameter. For example, the first tape procedure interchanges two address fields of $u$ bits. <cite data-source="paper">Its cost is O(V uτ ) for a fixed τ < 1.</cite> <cite data-source="paper">A compatible choice of rational parameters makes all terms in its cost table fit Theorem 1.</cite>
