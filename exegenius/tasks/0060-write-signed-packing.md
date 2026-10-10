# exegenius task 0060-write-signed-packing

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
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Record
- Row of an array (also: row)

## This page

Concept: Signed coefficient packing
Gloss: Encoding polynomial coefficients as signed integers at a fixed bit spacing so that one integer multiplication computes a polynomial product in the ring modulo y^r + 1.
Also called: Kronecker substitution

## Prerequisite pages (link each on first use, exactly as written)

- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The ring of polynomials in y with coefficients in C, reduced modulo y^r + 1 for a power of two r, in which y^r = -1.
- [Established O(n log n) multiplier](established-multiplier.md): The known deterministic O(n log n) multitape multiplication, used as an ordinary subroutine on short records.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Record](record.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Row of an array](row-of-array.md)
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

- "Signed coefficient packing is a form of Kronecker substitution" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "gives its time as $O(rp \log(rp))$" (The reader cannot see where this bound comes from from the page, and the lemma is not available to them.)
- Explain "centred extraction" inline: its concept depends on this page, so it cannot be a prerequisite.

## Previous version (revise it)

Signed coefficient packing, a form of Kronecker substitution, computes a product of polynomials by multiplying two integers. It is the tool that lets an integer multiplier compute polynomial products inside the [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md).

Let $w$ be a bit spacing. Pack a polynomial $f(y) = \sum_i f_i y^i$ with small signed coefficients into the integer $F = f(2^w)$. Packing two polynomials and multiplying the integers gives $FG = (fg)(2^w)$. If the coefficients of $fg$ are small enough, the coefficients can be read back out of $FG$ as $w$-bit signed digits.

Here is a worked example with $w = 5$, so the spacing is $32$. Take $f = 3 - 2y$ and $g = 1 + 5y$. Then $F = 3 - 64 = -61$ and $G = 1 + 160 = 161$. Their product is $FG = -9821$. The product polynomial is $fg = 3 + 13y - 10y^2$, and indeed $3 + 13 \cdot 32 - 10 \cdot 32^2 = -9821$.

To decode, take the residue of $-9821$ modulo $32$ in the window $[-16, 16)$. This gives $3$. Subtract it, divide by $32$, and repeat: the digits are $3$, $13$, and $-10$, which are the coefficients of $fg$. Decoding works because every coefficient lies in the window of width $2^w$ centred at zero.

For the negacyclic ring, the same packing is followed by reduction modulo $y^r + 1$ using the sign rule from the ring page. The paper's Lemma 17 combines exact packing, centred extraction, and negacyclic reduction, and gives its time as $O(rp \log(rp))$, using the [established multiplier](established-multiplier.md) on the packed integers.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0060-write-signed-packing.answer.md`, then run `exegenius submit 0060-write-signed-packing` in the project directory. If submit rejects the answer, fix the answer file and submit again.
