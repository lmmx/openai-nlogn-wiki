# exegenius task 0134-write-gaussian-resampling

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Write one page of an explanatory wiki. The wiki explains a target result from source documents to a specific reader, one concept per page, in reading order.

- Explain the page's concept so that this reader can follow it using only what they already understand (listed below), what this page itself explains, and the linked prerequisite pages.
- Define any other technical term or symbol on this page, where it is first used.
- Link each prerequisite page the first time you rely on it, using the exact markdown link given. You may also link the other pages listed. Submit rejects links to anything else in the wiki; external URLs are allowed.
- Stay accurate to the sources: read the parts you need (search for the evidence quotes). State only what the sources support or what is standard background; do not invent results, constants or attributions.
- Be concrete and specific. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine (also: fixed-tape machine)
- Exact integer multiplication (also: n-bit product)
- Schönhage–Strassen n log n conjecture (also: n log n optimality conjecture)
- Discrete Fourier transform (also: Fourier transform, DFT)
- Cyclic convolution (also: convolution modulo x^S - 1)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
- Synthetic polynomial transform (also: Nussbaumer transform)
- Address-field interchange (also: tape address swap)
- Simultaneous butterfly layer (also: H0 layer)
- Linear networks with frames (also: frames, role exchange network)
- Established O(n log n) multiplier (also: base multiplier)
- Signed coefficient packing (also: Kronecker substitution)
- Bit complexity (also: bit-complexity bound)
- Array with a complete Cartesian address set (also: complete Cartesian product of addresses)
- Frankl–Wilson construction (also: Alon's presentation of the Frankl–Wilson construction, pairing formulas)
- Gather and scatter operations
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Linear contraction (also: contraction)
- Record
- Row of an array (also: row)
- Linear index-code decoding (also: linear index-coding decoding)
- Rational bilinear form

## This page

Concept: Gaussian resampling
Gloss: A reduction that replaces a Fourier transform of arbitrary length by a multidimensional transform whose axis lengths are powers of two, using Gaussian-weighted resampling.
Also called: Harvey–van der Hoeven resampling

## Prerequisite pages (link each on first use, exactly as written)

- [Discrete Fourier transform](discrete-fourier-transform.md): A linear map that evaluates a sequence at powers of a root of unity, computing convolutions pointwise after transformation.
- [Cyclic convolution](cyclic-convolution.md): Multiplication of two coefficient sequences as polynomials modulo x^S - 1, so that exponents wrap around modulo S.
- [Linear contraction](linear-contraction.md): A linear map that does not increase the size of its inputs, so that its output has norm at most that of the input.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Record](record.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Row of an array](row-of-array.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Rational bilinear form](rational-bilinear-form.md)
- [Frankl–Wilson construction](frankl-wilson-construction.md)
- [Linear index-code decoding](linear-index-coding-decoding.md)
- [Multitape Turing machine](turing-machine-model.md)
- [Bit complexity](bit-complexity.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Linear networks with frames](linear-network-frames.md)
- [Gather and scatter operations](gather-scatter.md)
- [Array with a complete Cartesian address set](cartesian-address-array.md)
- [Address-field interchange](address-interchange.md)
- [Transform identity](transform-identity.md)
- [Source and target permutations](target-permutation.md)
- [Chinese-remainder address map](chinese-remainder-map.md)
- [Sup norm](sup-norm.md)
- [Middle transform](middle-transform.md)
- [Bluestein chirp identity](bluestein-chirp-identity.md)
- [Coefficient phase twist](phase-twist.md)
- [Complex modulus (norm of a coefficient)](complex-modulus.md)
- [Disk-grid values](disk-grid-values.md)
- [Normalized cost](normalized-cost.md)
- [Linear convolution](linear-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Precision and exact recovery](precision-and-rounding.md)
- [Parameter choice](parameter-choice.md)
- [Multiplication algorithm](multiplication-algorithm.md)
- [Indicator vector](indicator-vector.md)
- [Subset-intersection subspace construction](subspace-intersection-network.md)
- [Recursive rank saving](rank-saving-recursion.md)
- [Cost accounting](cost-accounting.md)
- [Deterministic O(n (lg n)^(1-kappa)) multiplication](main-theorem.md)

## Evidence from the sources

- "it replaces the Fourier transforms needed for this convolution by multidimensional transforms whose" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "which approximate a Gaussian-weighted interpolation between the two grids" (The page does not say what the maps approximate or why, so the reader cannot check that the resampling is an approximate interpolation.)

## Previous version (revise it)

Gaussian resampling is the step that replaces a [discrete Fourier transform](discrete-fourier-transform.md) of a length that is not a power of two by a transform whose axes all have power-of-two lengths. The idea is to move values between two grids of different sizes, so that the transform matches the wraparound structure of a [cyclic convolution](cyclic-convolution.md). The paper adapts the identity of Harvey and van der Hoeven.

Let $s < t$ be coprime integers. A length-$s$ grid and a length-$t$ grid are related by two coordinate permutations. The paper defines them as $(P_s u)_j = u_{tj}$ and $(P_t v)_k = v_{-sk}$, where indices are taken modulo the length. When $\gcd(s,t) = 1$, the map $j \mapsto tj \bmod s$ is a bijection.

For a small case, take $s = 3$ and $t = 4$. The map $j \mapsto 4j \bmod 3$ sends $0, 1, 2$ to $0, 1, 2$, so it is a permutation. The gcd condition is what makes this hold in general.

The resampling itself uses two [linear contractions](linear-contraction.md), $A : \mathbb{C}^s \to \mathbb{C}^t$ and $B_0 : \mathbb{C}^t \to \mathbb{C}^s$, which approximate a Gaussian-weighted interpolation between the two grids. The paper's analysis requires the ratio $t/s$ to be far enough from $1$ that the approximation error is small: the condition is $\theta = t/s - 1 > p/\alpha^4$, where $p$ is the precision and $\alpha$ is an auxiliary integer parameter. This is what allows the approximate resampling to use a fixed number of bits.

The payoff is that each source Fourier transform can be expressed through a transform whose axes have power-of-two lengths, together with these resampling maps. The remaining middle transform is then turned into a convolution by the [Bluestein chirp identity](bluestein-chirp-identity.md).

The paper proves that the two permutations need not be executed as separate full sorts. They can be left in the transform identity and cancelled later.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0134-write-gaussian-resampling.answer.md`, then run `exegenius submit 0134-write-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer file and submit again.
