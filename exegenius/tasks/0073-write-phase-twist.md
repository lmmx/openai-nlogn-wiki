# exegenius task 0073-write-phase-twist

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
- Chinese-remainder address map (also: CRT map, Agarwal–Cooley decomposition)
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
- Synthetic polynomial transform (also: Nussbaumer transform)
- Bluestein chirp identity (also: chirp transform)
- Address-field interchange (also: tape address swap)
- Simultaneous butterfly layer (also: H0 layer)
- Linear networks with frames (also: frames, role exchange network)
- Established O(n log n) multiplier (also: base multiplier)
- Signed coefficient packing (also: Kronecker substitution)
- Array with a complete Cartesian address set (also: complete Cartesian product of addresses)
- Frankl–Wilson construction (also: Alon's presentation of the Frankl–Wilson construction)
- Gather and scatter operations
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Linear contraction (also: contraction)
- Record
- Row of an array (also: row)
- Sup norm (also: coefficient sup norm, maximum norm)

## This page

Concept: Coefficient phase twist
Gloss: A multiplication of coefficients by powers of a root zeta = e^(pi i / r) that converts cyclic wraparound in the last coordinate into negacyclic wraparound modulo y^r + 1, and back.
Also called: twisted negacyclic convolution

## Prerequisite pages (link each on first use, exactly as written)

- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): The ring of polynomials in y with coefficients in C, reduced modulo y^r + 1 for a power of two r, in which y^r = -1.
- [Bluestein chirp identity](bluestein-chirp-identity.md): An identity that rewrites a discrete Fourier transform, including its target permutation, as a normalized cyclic convolution with a quadratic-phase chirp.
- [Sup norm](sup-norm.md): The maximum absolute value of the coefficients of a polynomial or array.

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
- [Chinese-remainder address map](chinese-remainder-map.md)
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

- "A phase twist changes the last cyclic coordinate into a polynomial" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- "sup norm" is the concept [Sup norm](sup-norm.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

The phase twist converts a cyclic convolution in one coordinate into a convolution in the [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md). It is used after the [Bluestein chirp identity](bluestein-chirp-identity.md), which leaves a cyclic convolution in its last coordinate.

Let $r$ be a power of two and put $\zeta = e^{\pi i / r}$. Define the map $\Theta$ that sends the cyclic variable $x_d$, with $x_d^r = 1$, to $\zeta y$:

$$x_d \mapsto \zeta y.$$

This is well defined, because $(\zeta y)^r = \zeta^r y^r = (-1)(-1) = 1$. On the bases $(x_d^k)$ and $(y^k)$ for $0 \le k < r$, it multiplies the $k$-th coefficient by $\zeta^k$. It is therefore an isomorphism, and its inverse multiplies coefficient $k$ by $\zeta^{-k}$.

The reason this helps is the wraparound check. Suppose a product term has exponents $k + l$, and write $k + l = j + hr$ with $h \in \{0, 1\}$. In the cyclic ring $x_d^r = 1$, so this term lands at position $j$ with no sign. In the twisted ring, the term has factor $\zeta^{k+l}(-1)^h$ after the negacyclic reduction $y^r = -1$. Using $\zeta^r = -1$, this equals $\zeta^{j}(\zeta^r)^h(-1)^h = \zeta^{j}$.

So multiplying by $\zeta^{-k}$ after the product untwists the coefficients, and recovers the cyclic result with the correct sign. The paper states this as: untwisting recovers the cyclic coefficient with the correct sign. The map preserves the sup norm of coefficients.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0073-write-phase-twist.answer.md`, then run `exegenius submit 0073-write-phase-twist` in the project directory. If submit rejects the answer, fix the answer file and submit again.
