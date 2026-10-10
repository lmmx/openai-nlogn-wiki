# exegenius task 0194-write-frankl-wilson-construction

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
- Exact integer multiplication (also: n-bit product)
- Schönhage–Strassen n log n conjecture (also: n log n optimality conjecture)
- Discrete Fourier transform (also: Fourier transform, DFT)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
- Synthetic polynomial transform (also: Nussbaumer transform)
- Established O(n log n) multiplier (also: base multiplier)
- Signed coefficient packing (also: Kronecker substitution)
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Record
- Row of an array (also: row)
- Rational bilinear form
- Complementary intersection graphs

## This page

Concept: Frankl–Wilson construction
Gloss: A construction of set systems with restricted intersection sizes, which gives low-degree polynomial representations of intersection graphs over fields.
Also called: Alon's presentation of the Frankl–Wilson construction, pairing formulas

## Prerequisite pages (link each on first use, exactly as written)

- [Rational bilinear form](rational-bilinear-form.md): A function of two vectors that is linear in each argument separately and whose coefficients are rational numbers.
- [Complementary intersection graphs](complementary-intersection-graph.md): A pair of graphs on the same family of sets, one joining two sets when their intersection size lies in a prescribed set of values and the other joining the remaining pairs, so that each is the complement of the other.

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
- [Multitape Turing machine](turing-machine-model.md)
- [Bit complexity](bit-complexity.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Linear networks with frames](linear-network-frames.md)
- [Array with a complete Cartesian address set](cartesian-address-array.md)
- [Address-field interchange](address-interchange.md)
- [Side wire](side-wire.md)
- [Linear index-code decoding](linear-index-coding-decoding.md)
- [Gather and scatter operations](gather-scatter.md)
- [Linear contraction](linear-contraction.md)
- [Cyclic convolution](cyclic-convolution.md)
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

- "presentation of the Frankl–Wilson construction [9] gives low-degree representations of complementary intersection graphs over different fields" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- "complementary intersection graphs" is the concept [Complementary intersection graphs](complementary-intersection-graph.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

The Frankl–Wilson construction is a result on set systems whose intersection sizes are restricted modulo a prime. Its algebraic content is a low-degree polynomial representation of an intersection graph. Low degree means the polynomial has few monomials, which is what makes the representation useful over a field.

The paper cites Alon's presentation of this construction. That presentation gives low-degree representations of complementary intersection graphs over different fields, so the same subsets can be used for two different algebraic tests, one over each field.

The case the paper uses has prime $p = 2$. Its subsets have size three, and the two polynomial evaluations are the intersection count modulo two and the intersection count minus one. These two evaluations are the pairing formulas that the paper uses. The [subset-intersection construction](subspace-intersection-network.md) page shows how they are used.

The paper does not use the construction unchanged. It changes the size of the ground set, and it expresses the second formula through a [rational bilinear form](rational-bilinear-form.md). These changes are what let the subspace labels of its network be built from the same intersection data.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0194-write-frankl-wilson-construction.answer.md`, then run `exegenius submit 0194-write-frankl-wilson-construction` in the project directory. If submit rejects the answer, fix the answer file and submit again.
