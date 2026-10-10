# exegenius task 0142-write-normalized-cost

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
- Bluestein chirp identity (also: chirp transform)
- Coefficient phase twist (also: twisted negacyclic convolution)
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
- Disk-grid values (also: p-bit grid values, grid values)
- Linear contraction (also: contraction)
- Record
- Row of an array (also: row)
- Sup norm (also: coefficient sup norm, maximum norm)
- Linear index-code decoding (also: linear index-coding decoding)
- Middle transform (also: middle factor)
- Complex modulus (norm of a coefficient) (also: norm of a complex number, absolute value, norm)
- Rational bilinear form
- Source and target permutations (also: target permutation)
- Transform identity

## This page

Concept: Normalized cost
Gloss: The running time of an operation divided by the stored volume V, so that costs of different operations on arrays of different sizes can be compared as powers of p.
Also called: costs after division by V, normalized recursive cost

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

- "Table 1 lists costs after division by V" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "The paper uses this form when it writes each operation's cost as a power of $p$." (The example just gave expresses the cost as a power of d, so the reader cannot tell how the cost is converted to a power of p.)

## Previous version (revise it)

The normalized cost of an operation is its running time divided by the stored volume $V$ of the data it acts on. The paper writes every cost this way, because $V$ is the natural measure of the work that must be done on every stored bit.

The paper's total volume is $V = Tp = \Theta(n)$, so a normalized cost is a cost per stored bit. Table 1 of the paper lists these normalized costs for each operation. Each entry is a fixed constant times a power of $p$, so the entries can be compared directly even though the operations act on arrays of different sizes.

For example, if an operation costs $O(V d^{\lambda'})$ on an array of volume $V$, its normalized cost is $O(d^{\lambda'})$, which is a power of $d$ with exponent less than one. The paper uses this form when it writes each operation's cost as a power of $p$.

The normalized cost is the quantity that the [cost accounting](cost-accounting.md) page sums over the operations of the algorithm.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0142-write-normalized-cost.answer.md`, then run `exegenius submit 0142-write-normalized-cost` in the project directory. If submit rejects the answer, fix the answer file and submit again.
