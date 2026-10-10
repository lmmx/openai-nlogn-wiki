# exegenius task 0067-write-address-interchange

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
- Array with a complete Cartesian address set (also: complete Cartesian product of addresses)
- Frankl–Wilson construction (also: Alon's presentation of the Frankl–Wilson construction)
- Gather and scatter operations
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Record
- Row of an array (also: row)

## This page

Concept: Address-field interchange
Gloss: A tape procedure that swaps two disjoint contiguous address fields of u bits in O(V u^tau) time for a fixed tau < 1, with intermediate XOR combinations but an exact final permutation.
Also called: tape address swap

## Prerequisite pages (link each on first use, exactly as written)

- [Multitape Turing machine](turing-machine-model.md): A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, where each step moves each head by at most one cell.
- [Array with a complete Cartesian address set](cartesian-address-array.md): An array whose addresses are all tuples in a product of ranges, stored in lexicographic order with the first coordinate most significant.

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
- [Frankl–Wilson construction](frankl-wilson-construction.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Linear networks with frames](linear-network-frames.md)
- [Gather and scatter operations](gather-scatter.md)
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

- "interchanges two disjoint contiguous address fields of u bits in an array" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "so during the computation the tapes hold sums of entries rather than copies of them" (The page does not say why XOR of entries is needed for the interchange, so the reader cannot check the claim that it works.)
- "complete Cartesian product of addresses" is the concept [Array with a complete Cartesian address set](cartesian-address-array.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

An address permutation moves each entry of an array from one address to another. Here the arrays are stored as streams of bits, and an address is implicit in an entry's position in the stream. Swapping two fields of an address means exchanging the positions of two groups of address digits, while keeping every other field fixed.

The procedure in this paper handles the case where the two fields are disjoint, contiguous, and each has $u$ bits, inside an array with a complete Cartesian product of addresses. For a fixed array of logical volume $V$ (the number of stored data bits), the procedure runs in $O(V u^{\tau})$ steps for a fixed exponent $\tau < 1$, and it works for arbitrary $u$.

The name "interchange" describes the effect. Take an address written as $(p, h, g, d, z)$ with $h$ and $d$ fields of width $u$. The procedure produces the address $(p, d, g, h, z)$, which swaps the two $u$-bit fields.

The procedure is not a simple sequence of digit moves. Its intermediate steps form pointwise XOR combinations of data, so during the computation the tapes hold sums of entries rather than copies of them. The final effect is still an exact permutation, and the result is exact for any initial contents of the auxiliary wires used as scratch space. The paper's [linear network](linear-network-frames.md) construction is what makes this possible.

The cost exponent $\tau$ matters because the transform layout needs many such swaps. A procedure that costs $O(V u^{\tau})$ with $\tau < 1$ is sublinear in the field width, and the saving compounds over the levels of the recursion, as explained in the [rank saving](rank-saving-recursion.md) page.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0067-write-address-interchange.answer.md`, then run `exegenius submit 0067-write-address-interchange` in the project directory. If submit rejects the answer, fix the answer file and submit again.
