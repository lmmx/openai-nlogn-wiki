# exegenius task 0063-write-simultaneous-butterfly-layer

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
- Established O(n log n) multiplier (also: base multiplier)
- Signed coefficient packing (also: Kronecker substitution)
- Frankl–Wilson construction (also: Alon's presentation of the Frankl–Wilson construction)
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Record
- Row of an array (also: row)

## This page

Concept: Simultaneous butterfly layer
Gloss: A tape procedure that applies the two-point map H0(u, v) = ((u + v)/2, (u − v)/2) to selected coordinate bits of all records at once, in O(V d^lambda') time.
Also called: H0 layer

## Prerequisite pages (link each on first use, exactly as written)

- [Multitape Turing machine](turing-machine-model.md): A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, where each step moves each head by at most one cell.
- [Gaussian dyadic numbers](gaussian-dyadic.md): Complex numbers whose real and imaginary parts are dyadic rationals, that is, have denominators that are powers of two.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Record](record.md)
- [Row of an array](row-of-array.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Frankl–Wilson construction](frankl-wilson-construction.md)
- [Linear networks with frames](linear-network-frames.md)
- [Gather and scatter operations](gather-scatter.md)
- [Array with a complete Cartesian address set](cartesian-address-array.md)
- [Address-field interchange](address-interchange.md)
- [Linear contraction](linear-contraction.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp-identity.md)
- [Chinese-remainder address map](chinese-remainder-map.md)
- [Sup norm](sup-norm.md)
- [Coefficient phase twist](phase-twist.md)
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

- "The second procedure applies" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Define the symbol p where it is first used: "by about $2\sqrt{2}\cdot 2^{-p}$"
- "Gaussian dyadic numbers" is the concept [Gaussian dyadic numbers](gaussian-dyadic.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

A two-point butterfly acts on a pair of values $u, v$ by the map

$$H_0(u, v) = \left(\frac{u + v}{2},\ \frac{u - v}{2}\right).$$

For example, $H_0(3, 1) = (2, 1)$. The map is linear, and its inverse is $(s, t) \mapsto (s + t, s - t)$, so applying it twice gives back the original pair up to a factor of $2$.

A butterfly layer applies $H_0$ to many pairs at once. In the paper, a pair is selected by fixing one address bit: the two entries whose addresses differ only in that bit are combined. A *simultaneous* layer selects the same bit position in each of at most $d$ equal-width address chunks, and applies the butterfly to all selected pairs in one pass over the data.

The cost of a single simultaneous layer on an array of logical bit volume $V$ is $O(V d^{\lambda'})$, for a fixed exponent $\lambda' < 1$. Separate butterfly factors, applied one at a time, would need a whole-array pass for each factor. The simultaneous layer avoids that, and this is what makes the layered transform fast.

The values are not stored as bits. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts on each coefficient. Intermediate values are exact Gaussian dyadic numbers, whose real and imaginary parts have power-of-two denominators, and a single rounding (truncation) happens after the complete layer. The paper bounds the resulting coefficient error by about $2\sqrt{2}\cdot 2^{-p}$.

The layer is the arithmetic primitive used in the [synthetic transform](synthetic-transform.md). It is implemented by the same [linear network](linear-network-frames.md) technique as the [address-field interchange](address-interchange.md).

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0063-write-simultaneous-butterfly-layer.answer.md`, then run `exegenius submit 0063-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer file and submit again.
