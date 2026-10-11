This page states the main theorem, the target of the whole argument: one fixed deterministic machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ steps. The theorem disproves [The n log n optimality conjecture](n-log-n-conjecture.md) in this model, and each later step exists to establish its bound.

## The statement

For a binary string $x$, $\mathrm{val}(x)$ denotes its nonnegative integer value, with the leftmost bit most significant. The input is $x\#y$, where $x$ and $y$ are binary strings of length $n$, and the output is the $2n$-bit binary form of $\mathrm{val}(x)\cdot\mathrm{val}(y)$. For example, take $n=4$, $x=1011$ and $y=0110$. Then $\mathrm{val}(x)=11$ and $\mathrm{val}(y)=6$, so the output is $66$ written in eight bits, $01000010$.

<cite data-source="paper">There is one deterministic Turing machine A, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product</cite>. The theorem is stated in the [Fixed-tape machine model](fixed-tape-model.md): the alphabet and the number of tapes do not depend on the input. $T_A(n)$ is the worst-case number of steps of $A$ on inputs of length $n$, and the claim is $T_A(n) = O(n(\lg n)^{1-\kappa})$ for every $n \ge 1$. <cite data-source="paper">The constants and thresholds in the construction are extremely large</cite>, so it is a bit-complexity bound, not a practical algorithm.

## Why the bound is a real improvement

Schönhage and Strassen <cite data-source="paper">conjectured n log n as the optimal order of multiplication cost</cite>. For large $n$ the theorem is faster than [Schoolbook multiplication](schoolbook-multiplication.md), which takes quadratic time in the number of digits. The new bound is smaller than $n\lg n$ by the factor $(\lg n)^{-\kappa}$. This factor tends to zero, but it falls below one half only when $\lg n > 2^{2^{182}}$.

## Where the saving comes from

The theorem gets its power saving from the [Rank-saving recursion](rank-saving-recursion.md): a call splits into smaller calls, each working on a stream holding a fraction of the stored bits. Let $g(f)$ be the cost of a call at parameter $f$ divided by its volume. A call at parameter $mf$ makes $s$ smaller calls at parameter $f$, each on a stream of volume $V/W$, so $g(mf) \approx (s/W)\,g(f)$, ignoring overhead. Since $s < Wm$, the factor $s/W$ is below $m$, the factor by which the parameter grew. <cite data-source="paper">This strict inequality is the source of the power saving.</cite>

After $\nu$ levels of recursion, where $\nu$ counts the levels, the normalized cost is about $(s/W)^\nu = (m^\nu)^{\log_m(s/W)}$ times the base cost. With the parameter of order $\lg n$, this is a power of $\lg n$ with exponent $\log_m(s/W)$, which is below one. The saving holds at every input length because its ingredients are fixed: <cite data-source="paper">All these numbers are fixed, independently of any eventual input length.</cite>

## Why the method is needed

<cite data-source="paper">Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n).</cite> A scan reads every stored bit once in order, so it costs $\Theta(n)$. A level that costs a full scan contributes $\Theta(n)$, and the total falls below $n\lg n$ only if each level costs less than a scan. Address rearrangements and transform layers must therefore be cheaper than a scan. <cite data-source="paper">The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers.</cite>

## How the argument proceeds

1. The first step reduces multiplication to a [Radix-digit convolution](radix-digit-convolution.md) of short integer coefficients, obtained by splitting each input into radix digits, that is, blocks of consecutive bits. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite>
2. One coordinate is stored as a polynomial modulo $y^r+1$. <cite data-source="paper">Powers of y then serve as roots of unity in the remaining axes</cite>, and <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>.
3. The method lays out the transforms by a [Transform layout](transform-layout.md), so that a butterfly layer can act on every transform round. <cite data-source="paper">place the selected bits of the participating axes at a common offset in consecutive K-bit chunks</cite>.
4. The machine adds selected bits by [Packed selected-bit addition](packed-bit-addition.md). <cite data-source="paper">We implement a binary row addition on corresponding selected bits in two address chunks.</cite>
5. The method places coefficients on distinct axes by a [Chinese-remainder map](chinese-remainder-map.md) that preserves convolution. The theorem chooses its axis lengths by [Prime source lengths](prime-source-lengths.md): distinct odd primes lying just below powers of two. <cite data-source="paper">The distinct prime lengths si must be close to the powers of two ti</cite>.
6. The method keeps permutations inside the [Transform identity with retained permutations](transform-identity.md), so the source and target coordinate permutations need not be executed as sorts. [Bluestein's chirp identity](bluestein-chirp-identity.md) <cite data-source="paper">converts the middle transform, including its target permutation</cite> into normalized cyclic convolution.
7. The method turns the last cyclic coordinate into a polynomial by [Phase twist](phase-twist.md). <cite data-source="paper">A phase twist changes the last cyclic coordinate into a polynomial</cite>.
8. The method handles the remaining axes by [Convolution over the polynomial ring](polynomial-ring-convolution.md). <cite data-source="paper">Sections 6 and 7 compute convolution on the remaining axes over this polynomial ring</cite>.
9. The method recovers the coefficients by rounding through [Exact coefficient recovery](recovery-and-error.md), which shows that the error is below one half. <cite data-source="paper">proves that the recovered coefficient error is strictly below 1/2</cite>.
10. The algorithm ends with [Carry propagation](carry-propagation.md), which turns the recovered coefficients into the exact binary product. <cite data-source="paper">propagates carries to obtain the exact binary product</cite>.

Each stage is charged to the stored volume $V$; for example, <cite data-source="paper">Its cost is O(V uτ ) for a fixed τ < 1.</cite> <cite data-source="paper">A compatible choice of rational parameters makes all terms in its cost table fit Theorem 1.</cite>
