# exegenius task 0077-write-radix-digit-convolution

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
- Coefficient phase twist (also: twisted negacyclic convolution)
- Address-field interchange (also: tape address swap)
- Simultaneous butterfly layer (also: H0 layer)
- Linear networks with frames (also: frames, role exchange network)
- Established O(n log n) multiplier (also: base multiplier)
- Signed coefficient packing (also: Kronecker substitution)
- Array with a complete Cartesian address set (also: complete Cartesian product of addresses)
- Linear convolution (also: ordinary polynomial product of coefficient lists, cyclic-free convolution)
- Frankl–Wilson construction (also: Alon's presentation of the Frankl–Wilson construction)
- Gather and scatter operations
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Disk-grid values (also: p-bit grid values, grid values)
- Linear contraction (also: contraction)
- Normalized cost (also: costs after division by V, normalized recursive cost)
- Record
- Row of an array (also: row)
- Sup norm (also: coefficient sup norm, maximum norm)

## This page

Concept: Radix-digit convolution
Gloss: Reduction of integer multiplication to a convolution of coefficient lists obtained by splitting each input into radix digits and propagating carries.
Also called: digit convolution

## Prerequisite pages (link each on first use, exactly as written)

- [Exact integer multiplication](exact-integer-multiplication.md): Computing the exact binary representation of the product of two n-bit integers, with no rounding.
- [Cyclic convolution](cyclic-convolution.md): Multiplication of two coefficient sequences as polynomials modulo x^S - 1, so that exponents wrap around modulo S.
- [Linear convolution](linear-convolution.md): The coefficient list of the ordinary product of two polynomials, with no reduction modulo any polynomial, so its length is the sum of the input lengths minus one.

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
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp-identity.md)
- [Chinese-remainder address map](chinese-remainder-map.md)
- [Sup norm](sup-norm.md)
- [Coefficient phase twist](phase-twist.md)
- [Disk-grid values](disk-grid-values.md)
- [Normalized cost](normalized-cost.md)
- [Precision and exact recovery](precision-and-rounding.md)
- [Parameter choice](parameter-choice.md)
- [Multiplication algorithm](multiplication-algorithm.md)
- [Indicator vector](indicator-vector.md)
- [Subset-intersection subspace construction](subspace-intersection-network.md)
- [Recursive rank saving](rank-saving-recursion.md)
- [Cost accounting](cost-accounting.md)
- [Deterministic O(n (lg n)^(1-kappa)) multiplication](main-theorem.md)

## Evidence from the sources

- "Splitting the inputs into radix digits reduces multiplication to convolution of short integer coefficients." (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- "cyclic-free convolution" is the concept [Linear convolution](linear-convolution.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

Let $b \ge 1$ be a digit width and write the two inputs $x, y$ in radix $2^b$. Each input has $q = \lceil n/b \rceil$ digits, so $x = \sum_{k} a_k 2^{bk}$ and $y = \sum_{l} b_l 2^{bl}$, with each digit in $[0, 2^b)$. The digits are stored as the coefficient lists of two polynomials in a variable $z$ with $z = 2^b$.

The product of the inputs is then the product of two polynomials evaluated at $z = 2^b$. The coefficients of the product polynomial are the cyclic-free convolution

$$c_j = \sum_{k + l = j} a_k b_l,$$

and $xy = \sum_j c_j 2^{bj}$. Each $c_j$ is an integer with $0 \le c_j \le q(2^b - 1)^2$. In the paper's setting $q \le n \le 2^b$, which gives $c_j < 2^{3b}$, so every coefficient fits in $3b$ bits.

A small example uses $b = 2$, so the radix is $4$. Take $x = 13 = 3 \cdot 4 + 1$ and $y = 11 = 2 \cdot 4 + 3$. Written least-significant digit first, the digits are $(1, 3)$ and $(3, 2)$. The convolution gives $c_0 = 1 \cdot 3 = 3$, $c_1 = 1 \cdot 2 + 3 \cdot 3 = 11$, and $c_2 = 3 \cdot 2 = 6$. Then $3 + 11 \cdot 4 + 6 \cdot 16 = 143 = 13 \cdot 11$.

The coefficients $c_j$ can exceed $2^b$, so the final integer is obtained by propagating carries from low to high coefficients. The convolution has length at most $2q - 1$, so it can be computed as a [cyclic convolution](cyclic-convolution.md) of any length $S \ge 2q - 1$ without wraparound. This is the reduction that the rest of the algorithm accelerates.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0077-write-radix-digit-convolution.answer.md`, then run `exegenius submit 0077-write-radix-digit-convolution` in the project directory. If submit rejects the answer, fix the answer file and submit again.
