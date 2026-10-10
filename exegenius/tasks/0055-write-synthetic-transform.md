# exegenius task 0055-write-synthetic-transform

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

## This page

Concept: Synthetic polynomial transform
Gloss: A transform over a polynomial ring modulo y^r + 1 whose roots of unity are powers of y, so that multiplying by a root is a signed cyclic shift of coefficients.
Also called: Nussbaumer transform

## Prerequisite pages (link each on first use, exactly as written)

- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The ring of polynomials in y with coefficients in C, reduced modulo y^r + 1 for a power of two r, in which y^r = -1.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
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

- "These are the synthetic polynomial transforms of Nussbaumer and Quandalle and" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "gives a transform of polynomial length, and the same layers run in reverse to invert it" (The page does not say what the layers compute or why running them in reverse inverts the transform, so the reader cannot check it.)
- The reader cannot follow this step: "on the axes that carry a polynomial coordinate" (The page does not explain which axes carry a polynomial coordinate or how the transform is used, so this role cannot be followed.)

## Previous version (revise it)

A synthetic polynomial transform is a discrete Fourier-type transform whose roots of unity are powers of $y$ in the [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md). Multiplying by $y^k$ only shifts coefficients and changes some signs, so each stage of the transform is made of address rearrangements, signed shifts, and two-point butterfly operations.

The paper credits this construction to Nussbaumer and to Quandalle and Nussbaumer. Its role here is to evaluate the transforms of the convolution on the axes that carry a polynomial coordinate.

Take $r = 4$ and a coefficient list $(a_0, a_1, a_2, a_3)$. Multiplying by $y$ gives $(-a_3, a_0, a_1, a_2)$, as in the ring page. Multiplying by $y^2$ applies this twice, giving $(-a_2, -a_3, a_0, a_1)$. Both are a shift followed by sign changes, which costs no multiplications.

A butterfly on two records $u$ and $v$ has the form $(u + v, u - v)$, possibly with a shift applied to one input first. Combining shifts and butterflies in layers gives a transform of polynomial length, and the same layers run in reverse to invert it.

In the paper, the transform is computed in simultaneous layers on a tape. The cost of each layer is governed by the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) procedure, which is the reason these transforms can be applied on a fixed number of tapes.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0055-write-synthetic-transform.answer.md`, then run `exegenius submit 0055-write-synthetic-transform` in the project directory. If submit rejects the answer, fix the answer file and submit again.
