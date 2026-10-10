# exegenius task 0051-write-exact-integer-multiplication

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

## This page

Concept: Exact integer multiplication
Gloss: Computing the exact binary representation of the product of two n-bit integers, with no rounding.
Also called: n-bit product

## Other pages you may link to

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

- "We consider exact multiplication" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Define the symbol lg where it is first used: "O(n(\lg n)^{1-\kappa})"
- The reader cannot follow this step: "The best known bound for this problem before the paper was $O(n \log n)$" (This is a claim about the literature with no source or explanation on the page, so the reader cannot check it.)

## Previous version (revise it)

Exact integer multiplication takes two binary strings of length $n$ and returns the full binary representation of their product. For $x \in \{0,1\}^n$, let $\mathrm{val}(x)$ be its nonnegative integer value, with the leftmost bit most significant. On input $x\#y$, the machine must output the $2n$-bit string representing $\mathrm{val}(x)\cdot\mathrm{val}(y)$, padded with leading zeroes.

"Exact" means there is no rounding and no error: the output is the true product for every pair of inputs, not an approximation with a bounded error. Any product of two $n$-bit numbers fits in $2n$ bits, so the output length is fixed in advance.

For example, with $n = 3$, take $x = 101$ (so $\mathrm{val}(x) = 5$) and $y = 011$ (so $\mathrm{val}(y) = 3$). The product is $15$, which is $001111$ in six bits, so the machine must output `001111`.

The problem is a computation on a [multitape Turing machine](turing-machine-model.md), and the cost of an algorithm is measured as a function of $n$. The best known bound for this problem before the paper was $O(n \log n)$, which is the reference point for the [Schönhage–Strassen conjecture](n-log-n-conjecture.md). The paper's main theorem is an exact algorithm in this same model whose worst-case time is $O(n(\lg n)^{1-\kappa})$ for a fixed $\kappa = 2^{-182}$.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0051-write-exact-integer-multiplication.answer.md`, then run `exegenius submit 0051-write-exact-integer-multiplication` in the project directory. If submit rejects the answer, fix the answer file and submit again.
