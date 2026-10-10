# exegenius task 0139-write-bluestein-chirp-identity

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
- Chinese-remainder address map (also: CRT map, Agarwal–Cooley decomposition, CRT)
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
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
- Sup norm (also: coefficient sup norm, maximum norm)
- Linear index-code decoding (also: linear index-coding decoding)
- Middle transform (also: middle factor)
- Rational bilinear form
- Source and target permutations (also: target permutation)
- Transform identity

## This page

Concept: Bluestein chirp identity
Gloss: An identity that rewrites a discrete Fourier transform, including its target permutation, as a normalized cyclic convolution with a quadratic-phase chirp.
Also called: chirp transform

## Prerequisite pages (link each on first use, exactly as written)

- [Gaussian resampling](gaussian-resampling.md): A reduction that replaces a Fourier transform of arbitrary length by a multidimensional transform whose axis lengths are powers of two, using Gaussian-weighted resampling.
- [Cyclic convolution](cyclic-convolution.md): Multiplication of two coefficient sequences as polynomials modulo x^S - 1, so that exponents wrap around modulo S.
- [Middle transform](middle-transform.md): The central factor in the splitting of a source Fourier transform into Gaussian resampling, a chirp, and this middle transform, which the chirp identity then converts into a convolution.
- [Source and target permutations](target-permutation.md): The reorderings of the coordinates of a transform's input and output that the transform identity keeps symbolically instead of executing as separate sorts.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
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
- [Linear contraction](linear-contraction.md)
- [Transform identity](transform-identity.md)
- [Chinese-remainder address map](chinese-remainder-map.md)
- [Sup norm](sup-norm.md)
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

- "converts the middle transform, including its target permutation," (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- "middle transform" is the concept [Middle transform](middle-transform.md), now a prerequisite: link it where the term is used.
- "target permutation" is the concept [Source and target permutations](target-permutation.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

Bluestein's chirp identity rewrites a [discrete Fourier transform](discrete-fourier-transform.md) as a convolution. It is the step that turns the middle transform in the paper's algorithm into a [cyclic convolution](cyclic-convolution.md).

Let $\omega = \zeta^2$ be a root of unity, with $\zeta$ itself a root of unity of twice the order. The DFT entry $\omega^{jk}$ can be split using the identity

$$2jk = j^2 + k^2 - (k - j)^2.$$

So $\zeta^{2jk} = \zeta^{j^2}\,\zeta^{k^2}\,\zeta^{-(k-j)^2}$. The factors $\zeta^{j^2}$ and $\zeta^{-(k-j)^2}$ are the chirp: a quadratic-phase sequence whose phases grow with the square of the index. Substituting into the DFT gives

$$\hat a_k = \zeta^{k^2} \sum_{j} \bigl(a_j \zeta^{j^2}\bigr)\, \zeta^{-(k-j)^2}.$$

The sum is a convolution of the sequence $u_j = a_j \zeta^{j^2}$ with the fixed sequence $v_m = \zeta^{-m^2}$. The output is then multiplied by $\zeta^{k^2}$.

For a small check, take $N = 2$, $\omega = -1$, and $\zeta = i$. The identity gives $\hat a_0 = a_0 + a_1$ and $\hat a_1 = i\,(a_0 \cdot i^{0} \cdot i^{-1} + a_1 \cdot i^{1} \cdot i^{0}) = i(-i\,a_0 + i\,a_1) = a_0 - a_1$, which is the DFT of $(a_0, a_1)$.

The paper applies the identity to a middle transform with its target permutation included. The result is a convolution on power-of-two axes, which the [phase twist](phase-twist.md) converts into a convolution in the [polynomial ring](polynomial-ring-mod-yr-plus-1.md). The identity is applied after the [Gaussian resampling](gaussian-resampling.md) step, which rewrites the source transform so that the identity can be used.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0139-write-bluestein-chirp-identity.answer.md`, then run `exegenius submit 0139-write-bluestein-chirp-identity` in the project directory. If submit rejects the answer, fix the answer file and submit again.
