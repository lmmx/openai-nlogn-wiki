# exegenius task 0052-write-n-log-n-conjecture

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

## This page

Concept: Schönhage–Strassen n log n conjecture
Gloss: The conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
Also called: n log n optimality conjecture

## Prerequisite pages (link each on first use, exactly as written)

- [Exact integer multiplication](exact-integer-multiplication.md): Computing the exact binary representation of the product of two n-bit integers, with no rounding.

## Other pages you may link to

- [Discrete Fourier transform](discrete-fourier-transform.md)
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

- "proposed n log n as the optimal order of growth" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Define the symbol lg where it is first used: "n \lg n$ whenever"
- The reader cannot follow this step: "*optimal at $n \log n$* if, for every fixed machine $A$" (The definition reuses the letter A both for the machine being defined and for the quantified machine, so the reader cannot tell which machine the bound is about.)

## Previous version (revise it)

In 1971 Schönhage and Strassen gave a multiplication algorithm for [exact integer multiplication](exact-integer-multiplication.md) that runs in $O(n \log n \log\log n)$ time on a multitape Turing machine. They proposed $n \log n$ as the optimal order of growth for this problem. This proposal is the Schönhage–Strassen conjecture.

To state it precisely, call a machine $A$ with running time $T_A(n)$ *optimal at $n \log n$* if, for every fixed machine $A$ that multiplies correctly, there are constants $c_A > 0$ and $N_A$ such that $T_A(n) \ge c_A\, n \lg n$ whenever $n \ge N_A$. This is an eventual lower bound: it constrains the running time for all large $n$, not for a single input length.

The conjecture is therefore refuted by one machine $A$ with $\liminf_{n\to\infty} T_A(n)/(n \lg n) = 0$. A machine with running time $O(n(\lg n)^{1-\kappa})$ has this property, since $(\lg n)^{1-\kappa}/\lg n \to 0$. The paper's main theorem supplies such a machine, and it does so with a limit of zero rather than just a smaller constant factor.

Harvey and van der Hoeven later proved an unconditional $O(n \log n)$ upper bound, which matched the conjectured order up to a constant. The conjecture was therefore about whether that $\log n$ factor could be removed, not about whether a faster bound exists at all.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0052-write-n-log-n-conjecture.answer.md`, then run `exegenius submit 0052-write-n-log-n-conjecture` in the project directory. If submit rejects the answer, fix the answer file and submit again.
