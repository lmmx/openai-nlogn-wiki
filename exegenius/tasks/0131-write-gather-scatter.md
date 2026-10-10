# exegenius task 0131-write-gather-scatter

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
- Simultaneous butterfly layer (also: H0 layer)
- Linear networks with frames (also: frames, role exchange network)
- Established O(n log n) multiplier (also: base multiplier)
- Signed coefficient packing (also: Kronecker substitution)
- Bit complexity (also: bit-complexity bound)
- Frankl–Wilson construction (also: Alon's presentation of the Frankl–Wilson construction, pairing formulas)
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Record
- Row of an array (also: row)
- Linear index-code decoding (also: linear index-coding decoding)
- Rational bilinear form

## This page

Concept: Gather and scatter operations
Gloss: Operations that collect the entries of a network's wires over a three-element subset and redistribute them, producing coefficients that depend only on the size of the intersection of two subsets.

## Prerequisite pages (link each on first use, exactly as written)

- [Linear networks with frames](linear-network-frames.md): A fixed linear network that exchanges banks of values with prescribed signs and restores auxiliary values, where each node carries an invertible frame operator so that intermediate frames cancel along a route.
- [Linear index-code decoding](linear-index-coding-decoding.md): Recovering a wanted coordinate from a low-rank linear summary of several coordinates by subtracting the contributions of neighbouring coordinates that are already known.

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
- [Multitape Turing machine](turing-machine-model.md)
- [Bit complexity](bit-complexity.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Array with a complete Cartesian address set](cartesian-address-array.md)
- [Address-field interchange](address-interchange.md)
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

- "gather and scatter create coefficients depending on intersection size" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- "linear index-code decoding" is the concept [Linear index-code decoding](linear-index-coding-decoding.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

Gather and scatter are the operations, on the wires of a [linear network](linear-network-frames.md), that build the coefficients of the subset-intersection construction. They work on three-element subsets of a ground set, and they are the reason the coefficients depend only on intersection sizes.

The paper describes their form as that of linear index-code decoding. A low-rank linear summary of several values gives the wanted coordinate, plus contributions from neighbouring coordinates that are already known. Decoding subtracts those known contributions, leaving the wanted coordinate. Gather forms such a summary, and scatter places the result back on the wires.

The paper's sentence on the construction states the outcome: gather and scatter create coefficients depending on intersection size. So the coefficient that links two subsets is determined by how many elements the subsets share, which can be $0$, $1$, $2$, or $3$ for three-element subsets.

Auxiliary wires then cancel the coefficients that should not appear. Together with the [indicator vectors](indicator-vector.md) of the subsets, this fixes the coefficients of the network. The [subset-intersection construction](subspace-intersection-network.md) uses these operations to assign subspaces to the gates.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0131-write-gather-scatter.answer.md`, then run `exegenius submit 0131-write-gather-scatter` in the project directory. If submit rejects the answer, fix the answer file and submit again.
