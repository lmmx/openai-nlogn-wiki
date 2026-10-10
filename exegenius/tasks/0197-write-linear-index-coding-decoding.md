# exegenius task 0197-write-linear-index-coding-decoding

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
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Record
- Row of an array (also: row)
- Rational bilinear form
- Complementary intersection graphs
- Side wire (also: side wires)

## This page

Concept: Linear index-code decoding
Gloss: Recovering a wanted coordinate from a low-rank linear summary of several coordinates by subtracting the contributions of neighbouring coordinates that are already known.
Also called: linear index-coding decoding

## Prerequisite pages (link each on first use, exactly as written)

- [Side wire](side-wire.md): A wire of a linear network that joins two neighbouring triples of the construction, carrying values between them in addition to the central wires and the data wires.

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
- [Complementary intersection graphs](complementary-intersection-graph.md)
- [Rational bilinear form](rational-bilinear-form.md)
- [Frankl–Wilson construction](frankl-wilson-construction.md)
- [Multitape Turing machine](turing-machine-model.md)
- [Bit complexity](bit-complexity.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Linear networks with frames](linear-network-frames.md)
- [Array with a complete Cartesian address set](cartesian-address-array.md)
- [Address-field interchange](address-interchange.md)
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

- "a low-rank linear summary gives the wanted coordinate plus contributions from known neighboring coordinates" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- "side wires" is the concept [Side wire](side-wire.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

Index coding is a setting in which a sender broadcasts values that receivers already partly know, and decoding means a receiver recovers the value it wants. Linear index-code decoding uses linear combinations for this recovery.

Suppose a receiver wants a coordinate $x_1$ and holds side information about its neighbours. The sender transmits a low-rank linear summary of several coordinates. This summary contains $x_1$ together with contributions from neighbouring coordinates $x_2, x_3, \dots$. The receiver already knows those neighbouring coordinates, so it can compute their contributions and subtract them. What remains is the wanted coordinate.

As a small example over the rationals, let the summary be $z = x_1 + x_2$, and suppose the receiver knows $x_2 = 3$. Subtracting the known contribution gives $x_1 = z - 3$.

The paper says that the gather and scatter operations, together with the side wires, have this form. A low-rank linear summary of the coordinates is formed, and the contributions of known neighbouring coordinates are subtracted, so the wanted coordinate is recovered from its neighbours. This is the decoding structure behind the [gather and scatter operations](gather-scatter.md).

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0197-write-linear-index-coding-decoding.answer.md`, then run `exegenius submit 0197-write-linear-index-coding-decoding` in the project directory. If submit rejects the answer, fix the answer file and submit again.
