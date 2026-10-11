The main theorem of the argument is a single deterministic machine that multiplies two binary integers exactly, in a number of steps that is the input length times a power of its logarithm, with an exponent just below one. Every step of the argument exists to establish this bound, and the steps below show how each one contributes to it.

## The statement

Let $n$ be the number of bits in each of the two input integers. Let $\kappa = 2^{-182}$, a fixed positive constant. Write $\lg n = \max\{\lceil \log_2 n\rceil, 1\}$ for the base-two logarithm of $n$, rounded up and at least 1. The inputs are $x$ and $y$, two binary strings of length $n$, written as $x\#y$. For a binary string $x$, $\mathrm{val}(x)$ denotes its nonnegative integer value, with the leftmost bit most significant.

<cite data-source="paper">There is one deterministic Turing machine A, with a fixed finite alphabet and a fixed</cite> finite number of one-dimensional tapes that computes the exact product. The theorem is stated for the [fixed-tape machine model](fixed-tape-model.md): one machine with a fixed finite alphabet and a fixed finite number of tapes. Call this machine $A$, and let $T_A(n)$ be its worst-case number of steps on inputs of length $n$.

The output must be the $2n$-bit binary representation of $\mathrm{val}(x)\,\mathrm{val}(y)$. For example, take $n = 4$, $x = 1011$ and $y = 0110$. Then $\mathrm{val}(x) = 11$ and $\mathrm{val}(y) = 6$, so the product is $66$, and the output is the eight-bit string $01000010$. The theorem says that $T_A(n) = O(n(\lg n)^{1-\kappa})$ for every $n \ge 1$.

<cite data-source="paper">The constants and thresholds in the construction are extremely large</cite>; the algorithm is intended to establish a bit-complexity bound.

## Why the bound is a real improvement

Schönhage and Strassen <cite data-source="paper">conjectured n log n as the optimal order of multiplication cost</cite>. It refutes the [n log n optimality conjecture](n-log-n-conjecture.md) in this model.

The new bound is smaller than $n\lg n$ by the factor $(\lg n)^{-\kappa}$, which tends to zero as $n$ grows. Since $\kappa$ is so small, this factor is below one half only when $\lg n > 2^{2^{182}}$. The saving is therefore real but appears only at input lengths far beyond any practical size.

The theorem is stated for every input length, not only for large ones. <cite data-source="paper">The finitely many smaller lengths are included by enlarging the implicit constant.</cite> Inputs below a fixed cutoff are multiplied by schoolbook multiplication, and the cutoff is absorbed into the constant.

The saving is strict because of the recursion. The machine splits each recursive call into smaller calls on streams of a fraction of the volume, and each level of recursion increases the cost by a factor smaller than the factor by which the parameter grows. The power saving comes from the [rank-saving recursion](rank-saving-recursion.md), in which each call splits into smaller calls on streams of a fraction of the volume. <cite data-source="paper">This strict inequality is the source of the power saving.</cite>

## Why the method is needed

<cite data-source="paper">Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n).</cite> Address rearrangements and transform layers must therefore be cheaper than a scan. <cite data-source="paper">The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers.</cite>

## How the argument proceeds

Each step is developed on the linked page.

1. The first step reduces multiplication to a [radix-digit convolution](radix-digit-convolution.md) of short integer coefficients, obtained by splitting each input into radix digits. <cite data-source="paper">Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients.</cite>
2. [Gaussian resampling](gaussian-resampling.md) <cite data-source="paper">replaces the Fourier transforms needed for this convolution by multidimensional transforms whose axis lengths are powers of two</cite>.
3. One coordinate is stored as the coefficient list of a [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md). <cite data-source="paper">Powers of y then serve as roots of unity in the remaining axes</cite>, and <cite data-source="paper">multiplication by such a root is a signed shift of the coefficient list</cite>.
4. The transforms are [synthetic transforms](synthetic-transforms.md). <cite data-source="paper">These are the synthetic polynomial transforms of Nussbaumer and Quandalle and Nussbaumer</cite>.
5. An [address-field interchange](address-interchange.md) exchanges two address fields. <cite data-source="paper">The first procedure interchanges two disjoint contiguous address fields of u bits in an array whose addresses form a complete Cartesian product.</cite>
6. A [simultaneous butterfly layer](simultaneous-butterfly-layer.md) acts at once. <cite data-source="paper">simultaneously on selected coordinate bits of the numerical arrays</cite>.
7. Each procedure is a [linear network](linear-network-frames.md). <cite data-source="paper">Each procedure arises from its own fixed linear network that exchanges two banks of values</cite>.
8. The transforms are laid out by a [transform layout](transform-layout.md) that places the selected bits of all axes at a common offset, so that the butterfly layer applies to each transform round.
9. The machine adds the selected bits of the address chunks by [packed selected-bit addition](packed-bit-addition.md), which uses cyclic shifts of whole chunks and a deterministic correction. <cite data-source="paper">We implement a binary row addition on corresponding selected bits in two address chunks.</cite>
10. The radix-digit coefficients are placed on distinct prime cyclic axes by a [Chinese-remainder map](chinese-remainder-map.md) that preserves convolution. It uses [prime source lengths](prime-source-lengths.md): distinct odd primes chosen close to the powers of two. <cite data-source="paper">The distinct prime lengths si must be close to the powers of two ti</cite>.
11. The method keeps the source and target coordinate permutations inside the [transform identity with retained permutations](transform-identity.md), so they need not be executed as sorts. <cite data-source="paper">Section 8 retains the source and target coordinate permutations in the transform identity, so they need not be executed as separate full sorts.</cite>
12. [Bluestein's chirp identity](bluestein-chirp-identity.md) <cite data-source="paper">converts the middle transform, including its target permutation</cite> into normalized cyclic convolution.
13. The last cyclic coordinate is converted by a [phase twist](phase-twist.md) into a coordinate of a polynomial ring. <cite data-source="paper">A phase twist changes the last cyclic coordinate into a polynomial</cite> ring.
14. The remaining axes are handled by [convolution over the polynomial ring](polynomial-ring-convolution.md), which computes the convolution with two forward synthetic transforms, a pointwise product and an opposite transform. <cite data-source="paper">Sections 6 and 7 compute convolution on the remaining axes over this polynomial ring.</cite>
15. The algorithm recovers the coefficients by rounding, which is justified by [exact coefficient recovery](recovery-and-error.md): the error is below one half. <cite data-source="paper">proves that the recovered coefficient error is strictly below 1/2</cite>.
16. [Carry propagation](carry-propagation.md) turns the recovered coefficients into the exact binary product. <cite data-source="paper">Propagate radix-2b carries in increasing coefficient order.</cite>

The parameters are chosen so that each term of the cost table fits the bound. <cite data-source="paper">The complete large-input bound is consequently</cite> $O(n(\log n)^{1-\kappa})$.
