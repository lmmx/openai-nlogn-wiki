# exegenius task 0144-write-parameter-choice

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
- Established O(n log n) multiplier (also: base multiplier)
- Signed coefficient packing (also: Kronecker substitution)
- Precision and exact recovery (also: coefficient rounding)
- Bit complexity (also: bit-complexity bound)
- Array with a complete Cartesian address set (also: complete Cartesian product of addresses)
- Linear convolution (also: ordinary polynomial product of coefficient lists, cyclic-free convolution)
- Frankl–Wilson construction (also: Alon's presentation of the Frankl–Wilson construction, pairing formulas)
- Gather and scatter operations
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Disk-grid values (also: p-bit grid values, grid values)
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

Concept: Parameter choice
Gloss: The fixed rational exponents and the sizes b, p, d, T and r chosen so that the cost terms all fit the target bound.
Also called: size parameters

## Prerequisite pages (link each on first use, exactly as written)

- [Precision and exact recovery](precision-and-rounding.md): The bookkeeping showing that fixed-precision approximations of the transforms recover each integer coefficient exactly after rounding, so that carry propagation yields the exact product.
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
- [Multiplication algorithm](multiplication-algorithm.md)
- [Indicator vector](indicator-vector.md)
- [Subset-intersection subspace construction](subspace-intersection-network.md)
- [Recursive rank saving](rank-saving-recursion.md)
- [Cost accounting](cost-accounting.md)
- [Deterministic O(n (lg n)^(1-kappa)) multiplication](main-theorem.md)

## Evidence from the sources

- "Take the power of two T in [4n/b, 8n/b)" (paper)

## Sources (read from disk as needed)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Problems a reader audit found in the previous version (fix all of them)

- Define the symbol sigma where it is first used: "$\tau = \sigma = 1 - 2^{-50}$"

## Previous version (revise it)

The algorithm has several size parameters that depend on the input length $n$. They are chosen so that every term in the cost table fits the target bound. Here $\lg n = \log_2 n$ is the base-2 logarithm. The cost table lists the normalized cost of each operation, as explained on the [normalized cost](normalized-cost.md) page, and the [cost accounting](cost-accounting.md) page checks it. The rules, for sufficiently large $n$, are:

- $b = \lceil \log_2 n \rceil$ and $p = 6b$, so $p = \Theta(\lg n)$ is the working precision.
- $d = \lfloor b^{\epsilon} \rfloor$ and $K = \lfloor d^{c} \rfloor$, where $\epsilon$ and $c$ are fixed rational constants.
- $T$ is the power of two in $[4n/b,\ 8n/b)$, and $r = 2^{\lceil (\log_2 T)/d \rceil}$.
- The $d$ axis lengths $t_i \in \{r/2, r\}$ satisfy $\prod_i t_i = T$, with the last axis $t_d = r$.

The fixed constants are $\epsilon = 2^{-75}$, $c = 2^{-56}$, $\tau = \sigma = 1 - 2^{-50}$, $\lambda = 1 - 2^{-52}$, $\lambda' = 1 - 2^{-54}$, $\delta = 1/16$, and $\kappa = 2^{-182}$. The paper calls these deliberately conservative and claims no optimization.

Because $\epsilon$ is so small, the choice of $d$ has a striking consequence. $d = \lfloor b^{\epsilon} \rfloor$ is at least $2$ only when $b^{\epsilon} \ge 2$, that is, when $b \ge 2^{1/\epsilon} = 2^{2^{75}}$. For all smaller inputs the algorithm uses $d = 1$. This does not contradict the theorem, which is asymptotic, but it shows that the stated constants only take effect for astronomically large $n$.

The paper's key estimates are $T p = \Theta(n)$, $d = \Theta(p^{\epsilon})$, and $r = 2^{\Theta(p^{1-\epsilon})}$. These are what let the cost accounting hold.

The sizes $T$ and $r$ are the transform lengths used by the [multiplication algorithm](multiplication-algorithm.md). The axis lengths $t_i$ are the lengths produced by the [Chinese-remainder address map](chinese-remainder-map.md), and the precision $p$ is the one whose rounding errors are bounded in [precision and exact recovery](precision-and-rounding.md). The number of axes of length $r/2$ is set so that the $t_i$ multiply to exactly $T$.

## Answer

The answer is the page body as markdown (not JSON).

Write the answer to `exegenius/tasks/0144-write-parameter-choice.answer.md`, then run `exegenius submit 0144-write-parameter-choice` in the project directory. If submit rejects the answer, fix the answer file and submit again.
