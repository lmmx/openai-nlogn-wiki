# exegenius task 0053-write-discrete-fourier-transform

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

## This page

Concept: Discrete Fourier transform
Gloss: A linear map that evaluates a sequence at powers of a root of unity, computing convolutions pointwise after transformation.
Also called: Fourier transform, DFT

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Record](record.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Row of an array](row-of-array.md)
- [Established O(n log n) multiplier](established-multiplier.md)
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

- "Fourier transforms needed for this convolution" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "the roots of unity are chosen so that multiplying by them is cheap on a tape" (The page asserts a property of the paper's transforms but does not say which roots or why multiplying by them is cheap, so the reader cannot check it.)

## Previous version (revise it)

Let $N \ge 1$ and let $\omega$ be a primitive $N$-th root of unity, so $\omega^N = 1$ and $\omega^k \ne 1$ for $0 < k < N$. The discrete Fourier transform (DFT) of a sequence $(a_0, \dots, a_{N-1})$ is the sequence $(\hat a_0, \dots, \hat a_{N-1})$ with

$$\hat a_k = \sum_{j=0}^{N-1} a_j\, \omega^{jk}.$$

Each output is a linear combination of the inputs, so the DFT is a linear map. Computed directly it costs about $N^2$ operations. Fast algorithms reduce this to about $N\log N$.

The reason the DFT matters here is the convolution theorem. The cyclic convolution of two sequences, defined in [cyclic convolution](cyclic-convolution.md), becomes a pointwise product after the DFT. So one can convolve by transforming both inputs, multiplying coefficient by coefficient, and applying the inverse transform.

A small example has $N = 2$ and $\omega = -1$. The DFT is $(a_0, a_1) \mapsto (a_0 + a_1, \ a_0 - a_1)$. Applying it twice gives $(2a_0, 2a_1)$, so the inverse is the same map followed by division by $N = 2$.

Multiplication by $\omega$ is an ordinary complex multiplication. In the paper, the DFTs needed for multiplication are replaced by transforms whose axis lengths are powers of two, and the roots of unity are chosen so that multiplying by them is cheap on a tape.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0053-write-discrete-fourier-transform.answer.md`, then run `exegenius submit 0053-write-discrete-fourier-transform` in the project directory. If submit rejects the answer, fix the answer file and submit again.
