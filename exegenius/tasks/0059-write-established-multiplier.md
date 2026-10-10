# exegenius task 0059-write-established-multiplier

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
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Record
- Row of an array (also: row)

## This page

Concept: Established O(n log n) multiplier
Gloss: The known deterministic O(n log n) multitape multiplication, used as an ordinary subroutine on short records.
Also called: base multiplier

## Prerequisite pages (link each on first use, exactly as written)

- [Exact integer multiplication](exact-integer-multiplication.md): Computing the exact binary representation of the product of two n-bit integers, with no rounding.
- [Record](record.md): A fixed-width block of stored data, such as one polynomial with complex coefficients, that is handled as a single unit by the procedures.

## Other pages you may link to

- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Row of an array](row-of-array.md)
- [Signed coefficient packing](signed-packing.md)
- [Frankl–Wilson construction](frankl-wilson-construction.md)
- [Multitape Turing machine](turing-machine-model.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
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

- "Calls to the established O(n log n) multiplier are ordinary subroutine calls" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The cost of that product is charged once per record, and the total cost of all such products is part of the final cost bound." (The page does not say how the cost is charged or how the total enters the final bound, so the reader cannot check the claim.)
- "record" is the concept [Record](record.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

The established multiplier is a known deterministic algorithm that multiplies two $N$-bit integers in $O(N \log N)$ time on a multitape Turing machine. Harvey and van der Hoeven proved this unconditional bound, and the paper uses it as a black box. It is the same kind of object as the [exact integer multiplication](exact-integer-multiplication.md) problem, but for the smaller records that appear inside the main algorithm.

The paper's main construction does not call itself recursively on its own large integers. It calls the established multiplier on records whose length is $O(rp)$, where $r$ is a power of two and $p$ is a precision parameter. The paper shows that this length is $o(n)$, so these calls are on inputs much shorter than the original problem.

The paper states that these calls are ordinary subroutine calls, and that they do not invoke the improved theorem recursively. So the bound it proves does not depend on any assumption about the subroutine beyond its known $O(N \log N)$ cost.

These calls are used in [signed coefficient packing](signed-packing.md), which turns a product of polynomials into one integer product. The cost of that product is charged once per record, and the total cost of all such products is part of the final cost bound.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0059-write-established-multiplier.answer.md`, then run `exegenius submit 0059-write-established-multiplier` in the project directory. If submit rejects the answer, fix the answer file and submit again.
