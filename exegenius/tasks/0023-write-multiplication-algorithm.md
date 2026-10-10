# exegenius task 0023-write-multiplication-algorithm

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
- Recursive rank saving (also: power saving)
- Established O(n log n) multiplier (also: base multiplier)
- Signed coefficient packing (also: Kronecker substitution)
- Precision and exact recovery (also: coefficient rounding)
- Parameter choice (also: size parameters)

## This page

Concept: Multiplication algorithm
Gloss: The six-step algorithm that forms three source transforms, multiplies them pointwise, scales and rounds the result, and propagates carries to output the exact 2n-bit product.
Also called: exact product algorithm

## Prerequisite pages (link each on first use, exactly as written)

- [Radix-digit convolution](radix-digit-convolution.md): Reduction of integer multiplication to a convolution of coefficient lists obtained by splitting each input into radix digits and propagating carries.
- [Chinese-remainder address map](chinese-remainder-map.md): A relabelling of a cyclic convolution of length S as a multidimensional cyclic convolution over pairwise coprime lengths, via the Chinese remainder theorem.
- [Gaussian resampling](gaussian-resampling.md): A reduction that replaces a Fourier transform of arbitrary length by a multidimensional transform whose axis lengths are powers of two, using Gaussian-weighted resampling.
- [Bluestein chirp identity](bluestein-chirp-identity.md): An identity that rewrites a discrete Fourier transform, including its target permutation, as a normalized cyclic convolution with a quadratic-phase chirp.
- [Coefficient phase twist](phase-twist.md): A multiplication of coefficients by powers of a root zeta = e^(pi i / r) that converts cyclic wraparound in the last coordinate into negacyclic wraparound modulo y^r + 1, and back.
- [Synthetic polynomial transform](synthetic-transform.md): A transform over a polynomial ring modulo y^r + 1 whose roots of unity are powers of y, so that multiplying by a root is a signed cyclic shift of coefficients.
- [Signed coefficient packing](signed-packing.md): Encoding polynomial coefficients as signed integers at a fixed bit spacing so that one integer multiplication computes a polynomial product in the ring modulo y^r + 1.
- [Precision and exact recovery](precision-and-rounding.md): The bookkeeping showing that fixed-precision approximations of the transforms recover each integer coefficient exactly after rounding, so that carry propagation yields the exact product.
- [Address-field interchange](address-interchange.md): A tape procedure that swaps two disjoint contiguous address fields of u bits in O(V u^tau) time for a fixed tau < 1, with intermediate XOR combinations but an exact final permutation.
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): A tape procedure that applies the two-point map H0(u, v) = ((u + v)/2, (u − v)/2) to selected coordinate bits of all records at once, in O(V d^lambda') time.
- [Parameter choice](parameter-choice.md): The fixed rational exponents and the sizes b, p, d, T and r chosen so that the cost terms all fit the target bound.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Multitape Turing machine](turing-machine-model.md)
- [Linear networks with frames](linear-network-frames.md)
- [Subset-intersection subspace construction](subspace-intersection-network.md)
- [Recursive rank saving](rank-saving-recursion.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cost accounting](cost-accounting.md)
- [Deterministic O(n (lg n)^(1-kappa)) multiplication](main-theorem.md)

## Evidence from the sources

- "The source-transform procedures now supply the three transforms needed for the radix-digit convolution." (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0023-write-multiplication-algorithm.answer.md`, then run `exegenius submit 0023-write-multiplication-algorithm` in the project directory. If submit rejects the answer, fix the answer file and submit again.
