# exegenius task 0147-write-cost-accounting

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
- Chinese-remainder address map (also: CRT map, Agarwal–Cooley decomposition, CRT)
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
- Bit complexity (also: bit-complexity bound)
- Array with a complete Cartesian address set (also: complete Cartesian product of addresses)
- Linear convolution (also: ordinary polynomial product of coefficient lists, cyclic-free convolution)
- Frankl–Wilson construction (also: Alon's presentation of the Frankl–Wilson construction, pairing formulas)
- Gather and scatter operations
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Disk-grid values (also: p-bit grid values, grid values)
- Indicator vector
- Linear contraction (also: contraction)
- Normalized cost (also: costs after division by V, normalized recursive cost)
- Record
- Row of an array (also: row)
- Sup norm (also: coefficient sup norm, maximum norm)
- Linear index-code decoding (also: linear index-coding decoding)
- Middle transform (also: middle factor)
- Complex modulus (norm of a coefficient) (also: norm of a complex number, absolute value, norm)
- Rational bilinear form
- Source and target permutations (also: target permutation)
- Transform identity

## This page

Concept: Cost accounting
Gloss: The normalized cost table showing each operation costs O(T p) times a power of p, and that every exponent falls below one by a margin of at least 2^(-181) = 2 kappa.
Also called: Table 1 cost bound, cost table

## Prerequisite pages (link each on first use, exactly as written)

- [Multiplication algorithm](multiplication-algorithm.md): The six-step algorithm that forms three source transforms, multiplies them pointwise, scales and rounds the result, and propagates carries to output the exact 2n-bit product.
- [Recursive rank saving](rank-saving-recursion.md): The recursion in which a call at parameter m uses s smaller calls with s < W m, so the cost per unit of volume is multiplied by a factor below m at each level and gives a power saving.
- [Parameter choice](parameter-choice.md): The fixed rational exponents and the sizes b, p, d, T and r chosen so that the cost terms all fit the target bound.
- [Chinese-remainder address map](chinese-remainder-map.md): A relabelling of a cyclic convolution of length S as a multidimensional cyclic convolution over pairwise coprime lengths, via the Chinese remainder theorem.

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
- [Rational bilinear form](rational-bilinear-form.md)
- [Frankl–Wilson construction](frankl-wilson-construction.md)
- [Linear index-code decoding](linear-index-coding-decoding.md)
- [Multitape Turing machine](turing-machine-model.md)
- [Bit complexity](bit-complexity.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Linear networks with frames](linear-network-frames.md)
- [Gather and scatter operations](gather-scatter.md)
- [Array with a complete Cartesian address set](cartesian-address-array.md)
- [Address-field interchange](address-interchange.md)
- [Linear contraction](linear-contraction.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform identity](transform-identity.md)
- [Source and target permutations](target-permutation.md)
- [Sup norm](sup-norm.md)
- [Middle transform](middle-transform.md)
- [Bluestein chirp identity](bluestein-chirp-identity.md)
- [Coefficient phase twist](phase-twist.md)
- [Complex modulus (norm of a coefficient)](complex-modulus.md)
- [Disk-grid values](disk-grid-values.md)
- [Normalized cost](normalized-cost.md)
- [Linear convolution](linear-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Precision and exact recovery](precision-and-rounding.md)
- [Indicator vector](indicator-vector.md)
- [Subset-intersection subspace construction](subspace-intersection-network.md)
- [Deterministic O(n (lg n)^(1-kappa)) multiplication](main-theorem.md)

## Evidence from the sources

- "The seven dominant powers in Table 1 have the following margins below one" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- "CRT" is the concept [Chinese-remainder address map](chinese-remainder-map.md), now a prerequisite: link it where the term is used.

## Previous version (revise it)

Cost accounting checks that the [multiplication algorithm](multiplication-algorithm.md) meets the claimed time bound. The paper writes every cost as a multiple of the stored volume $V = Tp = \Theta(n)$, using the [normalized cost](normalized-cost.md) of each operation. Each normalized cost is a fixed constant times a power of $p$ with an exponent depending on $\epsilon$, $c$, $\tau$, $\lambda'$, $\delta$.

Table 1 of the paper lists these normalized costs for the operations in the algorithm: prefix-slot moves and butterfly rounds, chunk exchanges for the transform layout, simultaneous butterfly rounds, CRT and axis layouts, Gaussian line maps, chirps and twists, packed polynomial products, final scaling, and input and output. Most rows are a power of $p$ with an exponent less than one, and two rows are logarithmic or constant.

The bound holds because every dominant exponent in the table falls below one by a margin. The paper names seven dominant margins $g_1, \dots, g_7$:

$$g_1 = 1 - \epsilon(1+c), \quad g_2 = \epsilon c (1-\tau), \quad g_3 = \epsilon(1 - \lambda'), \quad g_4 = 1 - \tau - \epsilon(2-\tau), \quad g_5 = \tfrac14 - \delta - \tfrac32\epsilon, \quad g_6 = 1 - \delta - \epsilon, \quad g_7 = \epsilon.$$

With the chosen constants, $g_2 = 2^{-75} \cdot 2^{-56} \cdot 2^{-50} = 2^{-181}$ and $g_3 = 2^{-129}$, and the others are larger. So the smallest margin is $2^{-181} = 2\kappa$.

The paper states that this explicit slack covers any remaining fixed power of $\log p$. Since $V = \Theta(n)$ and $p = \Theta(\lg n)$, where $\lg n = \log_2 n$, the total cost is $O(n(\lg n)^{1-\kappa})$, which is the stated bound.

The exponents come from the operations themselves. For example, the chunk exchanges use the [address-field interchange](address-interchange.md) cost $O(V u^{\tau})$, and the simultaneous rounds use the [simultaneous butterfly layer](simultaneous-butterfly-layer.md) cost $O(V d^{\lambda'})$. The [recursive rank saving](rank-saving-recursion.md) is what keeps the recursive rows below the trivial bound. The choice of constants in the [parameter choice](parameter-choice.md) is what makes each margin positive.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0147-write-cost-accounting.answer.md`, then run `exegenius submit 0147-write-cost-accounting` in the project directory. If submit rejects the answer, fix the answer file and submit again.
