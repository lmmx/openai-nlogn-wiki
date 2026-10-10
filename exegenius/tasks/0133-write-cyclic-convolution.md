# exegenius task 0133-write-cyclic-convolution

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

Concept: Cyclic convolution
Gloss: Multiplication of two coefficient sequences as polynomials modulo x^S - 1, so that exponents wrap around modulo S.
Also called: convolution modulo x^S - 1

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
- [Gaussian resampling](gaussian-resampling.md)
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

- "convolution modulo xS − 1 has no nonzero wraparound" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Define the symbol q where it is first used: "for radix-digit polynomials of degree at most $2q - 2$"

## Previous version (revise it)

For two sequences $a = (a_0, \dots, a_{S-1})$ and $b = (b_0, \dots, b_{S-1})$, the cyclic convolution $c = a * b$ is defined by

$$c_j = \sum_{\substack{k, l \\ k + l \equiv j \pmod S}} a_k b_l, \qquad 0 \le j < S.$$

Equivalently, $c$ is the product of the polynomials $a(x)$ and $b(x)$ reduced modulo $x^S - 1$. The indices wrap around modulo $S$, so the term $x^{S}$ becomes $1$ and the term $x^{S+k}$ becomes $x^k$.

Take $S = 3$, $a = (1, 2, 0)$, and $b = (0, 1, 1)$. The linear product is $(1 + 2x)(x + x^2) = x + 3x^2 + 2x^3$. Reducing with $x^3 = 1$ turns $2x^3$ into $2$, giving $c = (2, 1, 3)$. The sum formula gives the same: for example $c_2$ collects $a_0 b_2 + a_1 b_1 + a_2 b_0 = 1 + 2 + 0 = 3$.

If the linear product has degree below $S$, no term wraps, and the cyclic convolution equals the ordinary product. The paper uses this to avoid wraparound: for radix-digit polynomials of degree at most $2q - 2$, the condition $2q - 2 < S$ means there is no nonzero wraparound.

Cyclic convolution is the operation that the [radix-digit reduction](radix-digit-convolution.md) produces, and the [discrete Fourier transform](discrete-fourier-transform.md) is the standard way to compute it.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0133-write-cyclic-convolution.answer.md`, then run `exegenius submit 0133-write-cyclic-convolution` in the project directory. If submit rejects the answer, fix the answer file and submit again.
