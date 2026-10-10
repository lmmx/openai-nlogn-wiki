# exegenius task 0054-write-polynomial-ring-mod-yr-plus-1

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

## This page

Concept: Polynomial ring modulo y^r + 1
Gloss: The ring of polynomials in y with coefficients in C, reduced modulo y^r + 1 for a power of two r, in which y^r = -1.
Also called: negacyclic ring

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
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

- "a polynomial modulo y r + 1, with r a power of two" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "so no further reduction step is needed on each product" (This contradicts the reduction rule explained earlier on the page, which says each product is reduced by y^r = -1, and the reader cannot see what is meant.)
- The reader cannot follow this step: "serve as roots of unity for transforms" (The page does not say which transform is meant or why these powers are roots of unity for it, so the reader cannot check the claim.)

## Previous version (revise it)

Fix a power of two $r$. The ring $R_r = \mathbb{C}[y]/(y^r + 1)$ consists of the polynomials in $y$ with complex coefficients, where any power $y^r$ is replaced by $-1$. Every element can be written uniquely as $c_0 + c_1 y + \dots + c_{r-1} y^{r-1}$, so it is stored as a list of $r$ complex coefficients.

Multiplication works as ordinary polynomial multiplication followed by reduction. Since $y^r = -1$, the reduction rule is $y^{r+k} = -y^k$ for $0 \le k < r$. This is called a negacyclic wrap: a term that overflows past degree $r-1$ comes back with a minus sign.

For example, with $r = 4$, the reduction rules are $y^4 = -1$, $y^5 = -y$, and $y^6 = -y^2$. Then $y^3 \cdot y^2 = y^5 = -y$, so the wrapped term changes sign.

Since $y^r = -1$, we have $y^{2r} = 1$. So $y$ is a $2r$-th root of unity in this ring, and its powers $1, y, \dots, y^{2r-1}$ serve as roots of unity for transforms. Multiplying a coefficient list by $y$ is a cyclic shift in which the coefficient that moves past position $r-1$ is negated. With $r = 4$, $y \cdot (a_0, a_1, a_2, a_3) = (-a_3, a_0, a_1, a_2)$.

This is the structure that the [synthetic polynomial transform](synthetic-transform.md) and the [signed packing](signed-packing.md) use. The ring is a polynomial ring with the sign rule built in, so no further reduction step is needed on each product.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0054-write-polynomial-ring-mod-yr-plus-1.answer.md`, then run `exegenius submit 0054-write-polynomial-ring-mod-yr-plus-1` in the project directory. If submit rejects the answer, fix the answer file and submit again.
