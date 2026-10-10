# exegenius task 0062-write-turing-machine-model

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
- Frankl–Wilson construction (also: Alon's presentation of the Frankl–Wilson construction)
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Record
- Row of an array (also: row)

## This page

Concept: Multitape Turing machine
Gloss: A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, where each step moves each head by at most one cell.
Also called: fixed-tape machine

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

- "A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes." (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Explain "bit complexity" inline: its concept depends on this page, so it cannot be a prerequisite.
- Explain "fixed tracks" inline: its concept depends on this page, so it cannot be a prerequisite.

## Previous version (revise it)

A multitape Turing machine in this paper has one fixed finite alphabet and one fixed finite number of one-dimensional tapes. Each tape has its own head. In one step, the machine reads and writes at most one cell on each tape, and moves each head by at most one cell.

The model is the standard one for measuring bit complexity. Its running time is the number of steps. Using fixed tracks or a fixed number of work tapes changes the time by a constant factor, so these choices do not affect the bounds that matter here.

The paper distinguishes two kinds of rearrangement of data on tape. Moving one digit of a fixed radix to another position takes a bounded number of scans of the data. Interchanging two fields whose numbers of digits grow is much more expensive, and it is the subject of the [address-field interchange](address-interchange.md) procedure.

For example, consider an array of volume $V$, the number of stored data bits. Moving one specified radix-$q$ digit to another position, while preserving the order of the other positions, takes $O(V)$ steps. This is a linear-time operation on the whole array, which is the kind of cost the paper's later bounds are built from.

Counting also has a cost in this model. A binary counter over $L$ consecutive counts costs $O(L + w)$ time, where $w$ is its width, because the low-order positions change more often than the high-order ones.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0062-write-turing-machine-model.answer.md`, then run `exegenius submit 0062-write-turing-machine-model` in the project directory. If submit rejects the answer, fix the answer file and submit again.
