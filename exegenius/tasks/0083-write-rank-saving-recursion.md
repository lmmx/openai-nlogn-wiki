# exegenius task 0083-write-rank-saving-recursion

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
- Radix-digit convolution (also: digit convolution)
- Chinese-remainder address map (also: CRT map, Agarwal–Cooley decomposition)
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
- Synthetic polynomial transform (also: Nussbaumer transform)
- Bluestein chirp identity (also: chirp transform)
- Coefficient phase twist (also: twisted negacyclic convolution)
- Address-field interchange (also: tape address swap)
- Simultaneous butterfly layer (also: H0 layer)
- Linear networks with frames (also: frames, role exchange network)
- Subset-intersection subspace construction (also: nested subspaces)
- Established O(n log n) multiplier (also: base multiplier)
- Signed coefficient packing (also: Kronecker substitution)
- Precision and exact recovery (also: coefficient rounding)
- Parameter choice (also: size parameters)
- Multiplication algorithm (also: exact product algorithm)
- Array with a complete Cartesian address set (also: complete Cartesian product of addresses)
- Linear convolution (also: ordinary polynomial product of coefficient lists, cyclic-free convolution)
- Frankl–Wilson construction (also: Alon's presentation of the Frankl–Wilson construction)
- Gather and scatter operations
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Disk-grid values (also: p-bit grid values, grid values)
- Indicator vector
- Linear contraction (also: contraction)
- Normalized cost (also: costs after division by V, normalized recursive cost)
- Record
- Row of an array (also: row)
- Sup norm (also: coefficient sup norm, maximum norm)

## This page

Concept: Recursive rank saving
Gloss: The recursion in which a call at parameter m uses s smaller calls with s < W m, so the cost per unit of volume is multiplied by a factor below m at each level and gives a power saving.
Also called: power saving

## Prerequisite pages (link each on first use, exactly as written)

- [Address-field interchange](address-interchange.md): A tape procedure that swaps two disjoint contiguous address fields of u bits in O(V u^tau) time for a fixed tau < 1, with intermediate XOR combinations but an exact final permutation.
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): A tape procedure that applies the two-point map H0(u, v) = ((u + v)/2, (u − v)/2) to selected coordinate bits of all records at once, in O(V d^lambda') time.
- [Subset-intersection subspace construction](subspace-intersection-network.md): A construction that attaches nested subspaces of a fixed space to the gates of a linear network, using three-element subsets and intersection-size parity, so that the subspace dimensions drop along each edge.
- [Normalized cost](normalized-cost.md): The running time of an operation divided by the stored volume V, so that costs of different operations on arrays of different sizes can be compared as powers of p.

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
- [Linear networks with frames](linear-network-frames.md)
- [Gather and scatter operations](gather-scatter.md)
- [Array with a complete Cartesian address set](cartesian-address-array.md)
- [Linear contraction](linear-contraction.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp-identity.md)
- [Chinese-remainder address map](chinese-remainder-map.md)
- [Sup norm](sup-norm.md)
- [Coefficient phase twist](phase-twist.md)
- [Disk-grid values](disk-grid-values.md)
- [Linear convolution](linear-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Precision and exact recovery](precision-and-rounding.md)
- [Parameter choice](parameter-choice.md)
- [Multiplication algorithm](multiplication-algorithm.md)
- [Indicator vector](indicator-vector.md)
- [Cost accounting](cost-accounting.md)
- [Deterministic O(n (lg n)^(1-kappa)) multiplication](main-theorem.md)

## Evidence from the sources

- "that the total number s of smaller calls satisfies s < W m" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Define the symbol lg where it is first used: "$(\lg n)^{-\kappa}$ saved relative to $n \lg n$"
- "normalized recursive cost" is the concept [Normalized cost](normalized-cost.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

The power saving comes from a counting argument on the recursion. Consider a procedure that handles a call at parameter $mf$ by making $s$ smaller calls at parameter $f$. Each smaller call acts on a stream of volume $V/W$, where $W$ is the number of roles in the [linear network](linear-network-frames.md) and $V$ is the volume of the full array.

After dividing the cost by the volume, the cost of the recursive part at parameter $mf$ is $s/W$ times the cost at parameter $f$. The key condition is that the total number of smaller calls satisfies $s < W m$, which the [subspace construction](subspace-intersection-network.md) provides. So the factor per level is

$$\frac{s}{W} < m.$$

Multiplying the parameter by $m$ therefore increases the normalized recursive cost by less than the factor $m$. Iterating this over the levels of the recursion compounds the saving.

As a numerical illustration, let $W = 2$ and $m = 3$. The condition $s < Wm = 6$ holds for $s = 5$. Each level then multiplies the normalized cost by $s/W = 2.5$, which is less than $m = 3$. After $k$ levels the factor is $2.5^k$ rather than $3^k$, so the saving compounds.

The paper calls this strict inequality the source of the power saving. In the final bound, it appears as the factor $(\lg n)^{-\kappa}$ saved relative to $n \lg n$, with $\kappa = 2^{-182}$. The same recursion appears in the [address-field interchange](address-interchange.md) and the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), where the parameter counts field digits or selected axes.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0083-write-rank-saving-recursion.answer.md`, then run `exegenius submit 0083-write-rank-saving-recursion` in the project directory. If submit rejects the answer, fix the answer file and submit again.
