# exegenius task 0085-write-main-theorem

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
- Multiplication algorithm (also: exact product algorithm)
- Cost accounting (also: Table 1 cost bound, cost table)
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

Concept: Deterministic O(n (lg n)^(1-kappa)) multiplication
Gloss: There is one deterministic fixed-tape Turing machine computing the exact product of n-bit integers in O(n (lg n)^(1-kappa)) worst-case time, with kappa = 2^(-182), which refutes the n log n optimality conjecture in this model.
Also called: m, a, i, n, r, e, s, u, l, t

## Prerequisite pages (link each on first use, exactly as written)

- [Cost accounting](cost-accounting.md): The normalized cost table showing each operation costs O(T p) times a power of p, and that every exponent falls below one by a margin of at least 2^(-181) = 2 kappa.
- [Multiplication algorithm](multiplication-algorithm.md): The six-step algorithm that forms three source transforms, multiplies them pointwise, scales and rounds the result, and propagates carries to output the exact 2n-bit product.
- [Recursive rank saving](rank-saving-recursion.md): The recursion in which a call at parameter m uses s smaller calls with s < W m, so the cost per unit of volume is multiplied by a factor below m at each level and gives a power saving.
- [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md): The conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.

## Other pages you may link to

- [Exact integer multiplication](exact-integer-multiplication.md)
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
- [Indicator vector](indicator-vector.md)
- [Subset-intersection subspace construction](subspace-intersection-network.md)

## Evidence from the sources

- "There is one deterministic Turing machine A, with a fixed finite alphabet" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Define the symbol lg where it is first used: "O\bigl(n(\lg n)^{1-\kappa}\bigr)"
- The reader cannot follow this step: "with the smallest margin $2\kappa$ absorbing the logarithmic factors" (The page does not explain how the margin absorbs the logarithmic factors, so the reader cannot check this step.)

## Previous version (revise it)

The main theorem says that there is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes the exact product of two $n$-bit integers for every $n \ge 1$. Its worst-case running time $T_A(n)$ satisfies

$$T_A(n) = O\bigl(n(\lg n)^{1-\kappa}\bigr), \qquad \kappa = 2^{-182}.$$

The bound is asymptotic: $T_A(n) \le C\, n(\lg n)^{1-\kappa}$ for some constant $C$ and all sufficiently large $n$. The paper notes that the constants and thresholds in the construction are very large, so the result establishes a bit-complexity bound, not a practical algorithm.

The statement uses the [multitape Turing machine](turing-machine-model.md) model and the exact product from [exact integer multiplication](exact-integer-multiplication.md). Compared with the best known bound $O(n \log n)$, the factor $\log n$ is replaced by $(\log n)^{1-\kappa}$, a strict power saving.

The theorem refutes the [Schönhage–Strassen conjecture](n-log-n-conjecture.md) in this model. An eventual $\Omega(n \log n)$ lower bound for every multiplication machine would require $T_A(n)/(n \lg n)$ to stay bounded below for each fixed machine. The machine $A$ has $T_A(n)/(n \lg n) \to 0$, so the lower bound fails for it.

The proof combines the [multiplication algorithm](multiplication-algorithm.md) with the [cost accounting](cost-accounting.md). The algorithm is exact for every input length, and the cost table shows that all its terms fit the bound, with the smallest margin $2\kappa$ absorbing the logarithmic factors. The [rank-saving recursion](rank-saving-recursion.md) supplies the strict inequality that produces the power saving.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0085-write-main-theorem.answer.md`, then run `exegenius submit 0085-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer file and submit again.
