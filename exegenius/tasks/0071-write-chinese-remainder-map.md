# exegenius task 0071-write-chinese-remainder-map

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

## This page

Concept: Chinese-remainder address map
Gloss: A relabelling of a cyclic convolution of length S as a multidimensional cyclic convolution over pairwise coprime lengths, via the Chinese remainder theorem.
Also called: CRT map, Agarwal–Cooley decomposition

## Prerequisite pages (link each on first use, exactly as written)

- [Cyclic convolution](cyclic-convolution.md): Multiplication of two coefficient sequences as polynomials modulo x^S - 1, so that exponents wrap around modulo S.

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
- [Multitape Turing machine](turing-machine-model.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Linear networks with frames](linear-network-frames.md)
- [Gather and scatter operations](gather-scatter.md)
- [Array with a complete Cartesian address set](cartesian-address-array.md)
- [Address-field interchange](address-interchange.md)
- [Linear contraction](linear-contraction.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp-identity.md)
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

- "Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- The reader cannot follow this step: "whose lengths are the distinct prime-power factors used by the transform" (The page does not explain why the axis lengths should be prime-power factors, and the reader cannot check this claim from the page.)

## Previous version (revise it)

The Chinese remainder theorem says that if $s_1, \dots, s_d$ are pairwise coprime and $S = s_1 \cdots s_d$, then the map $k \mapsto (k \bmod s_1, \dots, k \bmod s_d)$ is a bijection from $\mathbb{Z}/S\mathbb{Z}$ to $\prod_i \mathbb{Z}/s_i\mathbb{Z}$. Its consequence here is that a [cyclic convolution](cyclic-convolution.md) of length $S$ can be relabelled as a multidimensional cyclic convolution with one axis of length $s_i$ for each factor.

Take $S = 6 = 2 \cdot 3$. The map sends each index to a pair of residues:

$$0 \mapsto (0,0),\quad 1 \mapsto (1,1),\quad 2 \mapsto (0,2),\quad 3 \mapsto (1,0),\quad 4 \mapsto (0,1),\quad 5 \mapsto (1,2).$$

For example, $5 \bmod 2 = 1$ and $5 \bmod 3 = 2$. Under this relabelling, a sum over $k + l \equiv j \pmod 6$ becomes a sum over pairs of residues that add componentwise modulo $2$ and modulo $3$. So the product of two sequences of length $6$ is the same as a two-dimensional cyclic convolution of size $2 \times 3$.

The paper's map $\Phi$ from $\mathbb{C}[x]/(x^S - 1)$ to $\mathbb{C}[x_1, \dots, x_d]/(x_1^{s_1} - 1, \dots, x_d^{s_d} - 1)$ uses this split. Its constants are $P_i = \prod_{j < i} s_j$ and $\mu_i = P_i^{-1} \bmod s_i$. The paper implements the change of order as controlled cyclic shifts of the coefficient stream.

Its purpose in the algorithm is to put the radix-digit coefficients on axes whose lengths are the distinct prime-power factors used by the transform. The [parameter choice](parameter-choice.md) then fixes those lengths.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0071-write-chinese-remainder-map.answer.md`, then run `exegenius submit 0071-write-chinese-remainder-map` in the project directory. If submit rejects the answer, fix the answer file and submit again.
