# exegenius task 0057-write-coefficient-twist

Project directory: `/home/user/openai-nlogn-wiki/runs/P4` (paths below are relative to it)

Write one page of an explanatory wiki. The wiki explains a target result from source documents to a specific reader, one concept per page, in reading order.

- Write for this reader's next uncertainty: at each point, give what they need to follow, and no more. The task lists the step of the argument this page presents, its motivations, and the pages around it. They are material for deciding what to say, not a list to cover: explain the transitions this reader would find hard, and leave familiar ones to ordinary sentences.
- Open with a sentence that says what the concept is and what it is for on the way to the target.
- If the page presents a step of the argument, say how its method shows its claim, and give its main motivation in a sentence. Add another motivation only if the reader would be stuck without it.
- Explain the page's concept so that this reader can follow it using only what they already understand (listed below), what this page itself explains, and the linked prerequisite pages.
- Define any other technical term on this page, where it is first used.
- Say what each symbol denotes where you introduce it: what it stands for, and for a size or count, what it counts ("$r$, the number of complex coefficients in a record", not "a power of two $r$"). A use in an example ("take $r = 4$") does not say what $r$ denotes. Symbols listed as already bound can be used without restating them: the page shows the reader their meanings. Using one of those letters with another meaning confuses readers: pick another letter, or say on the page that the letter changes meaning here.
- Link each prerequisite page the first time you rely on it, using the exact markdown link given. You may also link the other pages listed. Submit rejects links to anything else in the wiki; external URLs are allowed.
- For each prerequisite page, give a relation: the prerequisite's id, a predicate, and the sentence that links or names it, copied exactly. Use the sentence where the page relies on it; do not add a sentence for the purpose. The page shows the relation as "<this page's concept> *<predicate>* <prerequisite>", so pick a predicate that makes that a true sentence, with this page's concept as subject: "is reduced to", "computes its transforms by", "is based on", "follows from", "bounds the cost of". Build the predicate from the sentence's own words (other forms of a word count: "reduces" for "reduced"), and pick one that says what the prerequisite does for this page: "uses" says little.
- Stay accurate to the sources. The paragraphs around the evidence are given below; read further in the sources only if they are not enough. State only what the sources support or what is standard background; do not invent results, constants or attributions.
- Cite the results and constants a reader may want to check, right after the claim: `<cite data-source="id">text copied word for word from that source</cite>`. Readers see these as "(see p. 5)"-style references, hidden until they ask for them, so the sentence must read complete without the quoted words: write "the cost is $O(n \log n)$ <cite …>…</cite>", not "the paper states the cost as <cite …>…</cite>". Submit rejects a citation right after "that", "as", "states", "says", "is", "gives", "reads" or a colon, and text not found in the named source. Do not cite common background.
- A citation says where a claim comes from; it does not explain it. If the page's concept is an identity, a construction or a definition, state it. Explain how the concept works and how it shows its claim. For a result the page uses from prior work, say what the result states and why it applies here, and cite the source for its proof: the page need not reproduce it.
- Keep the page short. The task gives its word limit, counted without mathematics and citations, and submit rejects a longer page. Give a small worked example where it makes the idea clearer. No filler, no rhetorical flourishes, no announcing what the page will do.
- Write mathematics in LaTeX: $...$ inline, $$...$$ on its own lines for display.
- Do not write a title heading, a prerequisites list or a sources section: those are added automatically. Use ## subheadings only if the page is long.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished a standard undergraduate computer science degree: discrete mathematics (induction, counting, modular arithmetic, primes, gcd, permutations, basic graphs), algorithms (asymptotic notation, divide and conquer, recurrences, sorting including radix sort, the idea of the FFT and Karatsuba multiplication at survey level), calculus and basic real analysis (limits, logarithms, exponentials, floors and ceilings, inequalities), introductory linear algebra and probability, and the basics of Turing machines and complexity. They have not studied abstract algebra beyond arithmetic mod n, coding theory, or number-theoretic transforms in depth, and have not met the multitape fast-multiplication literature (Schönhage–Strassen, Fürer, Harvey–van der Hoeven), Gaussian resampling, or Nussbaumer polynomial transforms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape Turing machine model
- The n log n optimality conjecture
- Established near-linear integer multiplier
- Matrices, rank, subspaces and projections
- Tensor products of vectors, spaces and operators
- Binary vectors, XOR and Hamming weight
- Nondegenerate bilinear forms and orthogonal complements
- Discrete Fourier transform
- Multidimensional transform and cyclic convolution on a product of axes
- Cyclic convolution and the convolution theorem
- Butterfly step and decimation-in-frequency recursion
- Integer multiplication as convolution of radix digits
- Max-modulus norm, contractions and error propagation
- Disk grid and truncation
  - $p$ (precision bits): the number of fractional bits kept in each real or imaginary part
  - $\mathbb D_p$ (p-bit disk grid): the set of complex numbers 2^{-p}(a+ib) with integers a,b lying in the closed unit disk
  - $Q_p$ (truncation operator): the map that truncates the real and imaginary parts of each coefficient toward zero to multiples of 2^{-p}
- Streaming fixed-point and Gaussian dyadic arithmetic
- Arrays, address fields, rows and logical volume
- Linear-time stream operations
- Controlled cyclic shifts and rational scalings
- Depth-first recursion schedule on fixed tapes
- Triple-intersection pairing formulas
- Linear network exchanging two banks with restored scratch
- Frames and the common-frame identity
- Nested subspace labels and the rank deficit
- Address shear
- Bit network and rational shear interface
- Phase kernel C = aI + bX
  - $C$ (phase kernel): the two-by-two matrix H S H acting on one selected bit
  - $a$ (kernel coefficient a): the complex number (1+i)/2 multiplying the identity
  - $b$ (kernel coefficient b): the complex number (1−i)/2 multiplying the bit flip
  - $I$ (identity matrix): the two-by-two identity matrix
  - $X$ (bit-flip matrix): the two-by-two matrix interchanging the two coordinates
- Complex phase network interface
- Lower-triangular factorization of a matrix
- Cost of a rational matrix shear
- Strict rank deficit gives a power saving
- Rows distributed cyclically among wire roles
- Power-width interchange with rows
- Fast address-chunk interchange
- Carry-free packed controlled rotations
- Deterministic repair of exceptional addresses
- Packed selected-bit addition on one rectangle
- Guard width for exact intermediate values
- Recursive phase-frame layer on slots
- Simultaneous normalized butterfly layer
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): the indeterminate of the polynomial ring, satisfying y^r = −1
  - $r$ (polynomial length): the number of complex coefficients in a record, a power of two
- Synthetic root of unity ω_t = y^{2r/t}
  - $\omega_t$ (synthetic root): the element y^{2r/t} acting as a primitive t-th root of unity in the ring
  - $t$ (transform length): the length of the axis, a power of two dividing 2r
  - $y$ (ring variable): the indeterminate of the polynomial ring, satisfying y^r = −1
  - $r$ (polynomial length): the number of complex coefficients in a record, a power of two
- Synthetic polynomial transform
- Retained stored frequency order
- Transform layout and cost
- Signed Kronecker packing for ring products
- Convolution from the retained transform layout
- Gaussian resampling with retained permutations
- Tensor interface for resampling
- Bluestein chirp identity
- Cancellation of the source permutation
- Chinese-remainder map to prime cyclic axes
- Size parameters of the algorithm
- Distinct prime source lengths near powers of two
- Asymptotic notation beyond big-O (also: Theta, Omega, little-o, Θ, Ω, o(1), liminf, eventual lower bound)
- Logarithms, exponentials, floors and ceilings (also: log base 2, lg n, floor, ceiling, change of base, iterated logarithm)
- Binary and radix-b representation of integers (also: positional notation, base-b digits, mixed radix, bit length, val(x))
- Schoolbook multiplication and Karatsuba (also: grade-school multiplication, long multiplication, quadratic multiplication, Karatsuba-Ofman, Toom-Cook)
- Divisibility, primes and gcd (also: coprime, relatively prime, greatest common divisor, Euclidean algorithm, trial division, prime number)
- Modular arithmetic and residue classes (also: integers mod n, Z/nZ, congruence, mod Q, remainder, division with remainder, residue ring)
- Roots of unity (also: primitive root of unity, n-th roots of unity, e^{2πi/n}, twiddle factors)
- Recurrences and geometric series (also: divide-and-conquer recurrence, master theorem, solving recurrences, geometric sum, T(n) = aT(n/b) + f(n))
- Induction and elementary proof technique (also: proof by induction, structural induction, contradiction, pigeonhole principle)
- Elementary counting and the union bound (also: binomial coefficients, counting subsets, inclusion–exclusion, union bound, fraction of a finite set, Boole's inequality)
- Sorting and radix sort (also: stable sort, radix sort, counting sort, sorting by key, bucket sort)
- Permutations and bijections (also: index permutation, bit reversal, inverse permutation, permutation matrix, one-to-one correspondence)
- Sets, products of ranges and lexicographic order (also: Cartesian product, index set [n], multi-index, lexicographic order, row-major order)
- Matrix transposition and row-major storage (also: transpose, k×k binary matrix, row-major matrix)
- Triangle inequality and error bounds (also: absolute error, rounding error, approximation error, supremum, modulus inequality, rounding to nearest integer)
- Boolean and arithmetic circuits as networks (also: logic gates, XOR gate, circuit, wires and gates, directed acyclic graph, fan-in and fan-out)
- Graphs, paths and neighbors (also: directed graph, edges and vertices, adjacent vertices, route in a graph)
- Stacks and recursion (also: call stack, LIFO, push and pop, depth-first traversal, recursive procedure)
- Fast Fourier transform and Karatsuba as survey knowledge (also: FFT multiplication, Schönhage–Strassen, polynomial multiplication via evaluation, evaluation and interpolation)
- Real and imaginary parts, rounding and truncation (also: Re and Im, truncate toward zero, nearest integer, fixed-point numbers)
- Dot product, vectors over the rationals and orthonormal bases (also: inner product, orthogonal vectors, standard basis, Gram–Schmidt, bilinear pairing)

## This page

Concept: Coefficient twist from cyclic to negacyclic
Gloss: The isomorphism x_d ↦ ζy with ζ = e^{πi/r} sends cyclic convolution of length r to the ring modulo y^r+1, multiplying coefficient k by ζ^k; the negative wrap exactly cancels the factor ζ^r, so untwisting recovers the cyclic result.

## This page in the argument

The step: The isomorphism $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ sends cyclic convolution of length $r$ to the ring modulo $y^r+1$ by multiplying coefficient $k$ by $\zeta^k$; the negative wrap cancels the factor $\zeta^r$, so untwisting recovers the cyclic result.
How: Check well-definedness and invertibility of the diagonal twist on bases, and verify directly that terms that wrap around pick up $(-1)\cdot\zeta^r=1$.
Why: A cyclic wrap multiplies by one and a negacyclic wrap by $-1$, and a twist by an $r$th root of $-1$ exchanges the two. (the sources leave this for the reader to work out: spell it out)
Striking feature: The negative sign of the wrap exactly cancels the factor $\zeta^r=-1$ picked up by wrapped terms, so the twist converts a cyclic convolution into a negacyclic one without changing the result. (explain why it holds, from the method)

Its sub-steps, in order:

- The map is well defined since $(\zeta y)^r=(-1)(-1)=1$, and it is diagonal on the monomial bases with nonzero entries $\zeta^k$, hence an isomorphism.
- For $k+l=j+hr$ a product term after twisting and negacyclic reduction has factor $\zeta^{k+l}(-1)^h=\zeta^j$.
- Untwisting therefore recovers the cyclic coefficient with the correct sign.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce multiplication to convolution over $\mathbb C[y]/(y^r+1)$ through radix digits, Chinese-remainder axes, Gaussian resampling and chirps, speed up the data movement and the butterfly arithmetic with two network-based tape procedures with a strict rank saving, recover the exact product by rounding and carries, and add up the costs. (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))
- Convert the inputs to radix-$2^b$ digits, map them to the prime axes by the CRT map, compute the two source transforms, multiply pointwise, compute the opposite transform, rescale by $S$ and $2^{2b+4}$, round, undo the CRT map and propagate carries to output the exact $2n$-bit product.; how: Instantiate the earlier procedures with explicit compatible parameters and chain them in the order digits, CRT map, source transforms, pointwise product, opposite transform, rescaling, rounding, inverse map, carries. (on [The complete multiplication algorithm](multiplication-algorithm.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (A5.1, A5.2, A5.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**A5.1**: The map is well defined since $(\zeta y)^r=(-1)(-1)=1$, and it is diagonal on the monomial bases with nonzero entries $\zeta^k$, hence an isomorphism.
Source: "is well defined, since $(\zeta y)^r=(-1)(-1)=1$." (paper)
> The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist. Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and $\zeta=e^{\pi i/r}$. The map \[ \Theta:\mathbb C[x_d]/(x_d^r-1)\longrightarrow\mathcal R, \qquad x_d\longmapsto\zeta y \] is well defined, since $(\zeta y)^r=(-1)(-1)=1$. On the bases $(x_d^k)_{0\le k<r}$ and $(y^k)_{0\le k<r}$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$. It is therefore an isomorphism, with inverse multiplying that coefficient by $\zeta^{-k}$. Both exact maps preserve the coefficient sup norm. For an explicit check on the wrap, write $k+l=j+hr$, where $h\in\{0,1\}$. A product term after twisting and negacyclic reduction has factor \[ \zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j. \] Untwisting therefore recovers the cyclic coefficient with the correct sign. We next specify how this linewise map meets the ring-convolution interface. Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$ on $\prod_{i=1}^d\mathbb Z/t_i\mathbb Z

**A5.2**: For $k+l=j+hr$ a product term after twisting and negacyclic reduction has factor $\zeta^{k+l}(-1)^h=\zeta^j$.
Source: "For an explicit check on the wrap, write $k+l=j+hr$, where" (paper)
> The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist. Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and $\zeta=e^{\pi i/r}$. The map \[ \Theta:\mathbb C[x_d]/(x_d^r-1)\longrightarrow\mathcal R, \qquad x_d\longmapsto\zeta y \] is well defined, since $(\zeta y)^r=(-1)(-1)=1$. On the bases $(x_d^k)_{0\le k<r}$ and $(y^k)_{0\le k<r}$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$. It is therefore an isomorphism, with inverse multiplying that coefficient by $\zeta^{-k}$. Both exact maps preserve the coefficient sup norm. For an explicit check on the wrap, write $k+l=j+hr$, where $h\in\{0,1\}$. A product term after twisting and negacyclic reduction has factor \[ \zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j. \] Untwisting therefore recovers the cyclic coefficient with the correct sign. We next specify how this linewise map meets the ring-convolution interface. Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$ on $\prod_{i=1}^d\mathbb Z/t_i\mathbb Z$, with $t_d=r$, define \[ (\iota f)_{\boldsymbol j} =\sum_{k=0}^{r-1}f_{\boldsymbol j,k}y^k, \qquad \boldsymbol j\in\prod_{i<d}\mathbb Z/t_i\mathbb Z. \] This identifies the scalar tensor with an array of $M$ records in $\mathcal R$. As maps of values, $\iota$ and $\iota^{-1}$ preserve norms and grids. Write $(D_\pm f)_{\bol

**A5.3**: Untwisting therefore recovers the cyclic coefficient with the correct sign.
Source: "Untwisting therefore recovers the cyclic coefficient with the correct" (paper)
> twist. Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and $\zeta=e^{\pi i/r}$. The map \[ \Theta:\mathbb C[x_d]/(x_d^r-1)\longrightarrow\mathcal R, \qquad x_d\longmapsto\zeta y \] is well defined, since $(\zeta y)^r=(-1)(-1)=1$. On the bases $(x_d^k)_{0\le k<r}$ and $(y^k)_{0\le k<r}$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$. It is therefore an isomorphism, with inverse multiplying that coefficient by $\zeta^{-k}$. Both exact maps preserve the coefficient sup norm. For an explicit check on the wrap, write $k+l=j+hr$, where $h\in\{0,1\}$. A product term after twisting and negacyclic reduction has factor \[ \zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j. \] Untwisting therefore recovers the cyclic coefficient with the correct sign. We next specify how this linewise map meets the ring-convolution interface. Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$ on $\prod_{i=1}^d\mathbb Z/t_i\mathbb Z$, with $t_d=r$, define \[ (\iota f)_{\boldsymbol j} =\sum_{k=0}^{r-1}f_{\boldsymbol j,k}y^k, \qquad \boldsymbol j\in\prod_{i<d}\mathbb Z/t_i\mathbb Z. \] This identifies the scalar tensor with an array of $M$ records in $\mathcal R$. As maps of values, $\iota$ and $\iota^{-1}$ preserve norms and grids. Write $(D_\pm f)_{\boldsymbol j,k}=\zeta^{\pm k}f_{\boldsymbol j,k}$. The linewise extension of $\Theta$ is $\iota D_+$, with inverse $D_-\iota^{-1}$. Consequently, with $\mathcal M_r$ from Section~\ref{sec:exact-ring-products

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Polynomial ring modulo y^r + 1](polynomial-ring-negacyclic.md): Polynomials with complex coefficients of degree below r, with y^r = −1; multiplying by a power y^a is an exact signed cyclic shift of the coefficient list (an isometry), and the wrap-around carries a minus sign (negacyclic).
  Shown as: Coefficient twist from cyclic to negacyclic *<predicate>* Polynomial ring modulo y^r + 1
- [Cyclic convolution and the convolution theorem](cyclic-convolution.md): Convolution of arrays indexed by cyclic groups; the DFT turns it into pointwise multiplication (up to normalization), so convolution can be computed by transform, pointwise product, inverse transform.
  Shown as: Coefficient twist from cyclic to negacyclic *<predicate>* Cyclic convolution and the convolution theorem

## Pages that build on this one

- Middle transform computed by chirp and complex convolution: The padded power-of-two transform Q F_t is computed by chirp phase products, a complex cyclic convolution obtained through the coefficient twist and synthetic convolution, and a final chirp product, with error below 8TL·2^{−p}.

## Other pages you may link to

- [Fixed-tape Turing machine model](multitape-model.md)
- [The n log n optimality conjecture](nlogn-conjecture.md)
- [Streaming fixed-point and Gaussian dyadic arithmetic](fixed-point-arithmetic.md)
- [Established near-linear integer multiplier](established-multiplier.md)
- [Arrays, address fields, rows and logical volume](address-fields-volume.md)
- [Linear-time stream operations](stream-ops.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Matrices, rank, subspaces and projections](linear-algebra-basics.md)
- [Tensor products of vectors, spaces and operators](tensor-products.md)
- [Address shear](address-shear.md)
- [Binary vectors, XOR and Hamming weight](f2-vectors.md)
- [Nondegenerate bilinear forms and orthogonal complements](bilinear-orthogonality.md)
- [Triple-intersection pairing formulas](subset-pairing-formulas.md)
- [Linear network exchanging two banks with restored scratch](scalar-exchange-network.md)
- [Frames and the common-frame identity](network-frames.md)
- [Rows distributed cyclically among wire roles](row-splitting-roles.md)
- [Nested subspace labels and the rank deficit](subspace-labels-rank-saving.md)
- [Strict rank deficit gives a power saving](rank-deficit-recurrence.md)
- [Bit network and rational shear interface](bit-network-interface.md)
- [Lower-triangular factorization of a matrix](lower-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Depth-first recursion schedule on fixed tapes](fixed-tape-dfs-schedule.md)
- [Power-width interchange with rows](power-width-interchange.md)
- [Fast address-chunk interchange](chunk-swap.md)
- [Carry-free packed controlled rotations](packed-rotations.md)
- [Deterministic repair of exceptional addresses](exceptional-address-repair.md)
- [Packed selected-bit addition on one rectangle](packed-selected-bit-addition.md)
- [Discrete Fourier transform](dft.md)
- [Synthetic root of unity ω_t = y^{2r/t}](synthetic-roots.md)
- [Butterfly step and decimation-in-frequency recursion](fft-butterfly.md)
- [Phase kernel C = aI + bX](phase-kernel.md)
- [Complex phase network interface](complex-network-interface.md)
- [Recursive phase-frame layer on slots](phase-frame-layer.md)
- [Multidimensional transform and cyclic convolution on a product of axes](multidim-dft.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Retained stored frequency order](frequency-order.md)
- [Max-modulus norm, contractions and error propagation](contraction-error-budget.md)
- [Disk grid and truncation](disk-grid-truncation.md)
- [Guard width for exact intermediate values](guard-width.md)
- [Simultaneous normalized butterfly layer](simultaneous-layer.md)
- [Transform layout and cost](transform-layout.md)
- [Signed Kronecker packing for ring products](signed-packing.md)
- [Gaussian resampling with retained permutations](gaussian-resampling.md)
- [Tensor interface for resampling](tensor-resampling.md)
- [Integer multiplication as convolution of radix digits](multiplication-as-convolution.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Cancellation of the source permutation](source-permutation-cancel.md)
- [Convolution from the retained transform layout](synthetic-convolution.md)
- [Size parameters of the algorithm](parameter-choice.md)
- [Chinese-remainder map to prime cyclic axes](crt-address-map.md)
- [Distinct prime source lengths near powers of two](prime-lengths.md)
- [Middle transform computed by chirp and complex convolution](chirp-transform.md)
- [Source transform procedure](source-transform.md)
- [Exact recovery by rounding and carry propagation](exact-recovery.md)
- [The complete multiplication algorithm](multiplication-algorithm.md)
- [Cost analysis and the exponent κ](cost-analysis.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "is well defined, since $(\zeta y)^r=(-1)(-1)=1$" (paper)

  > The power-of-two complex convolution used in the chirp identity is obtained from the synthetic convolution by a coefficient twist. Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and $\zeta=e^{\pi i/r}$. The map \[ \Theta:\mathbb C[x_d]/(x_d^r-1)\longrightarrow\mathcal R, \qquad x_d\longmapsto\zeta y \] is well defined, since $(\zeta y)^r=(-1)(-1)=1$. On the bases $(x_d^k)_{0\le k<r}$ and $(y^k)_{0\le k<r}$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$. It is therefore an isomorphism, with inverse multiplying that coefficient by $\zeta^{-k}$. Both exact maps preserve the coefficient sup norm. For an explicit check on the wrap, write $k+l=j+hr$, where $h\in\{0,1\}$. A product term after twisting and negacyclic reduction has factor \[ \zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j. \] Untwisting therefore recovers the cyclic coefficient with the correct sign. We next specify how this linewise map meets the ring-convolution interface. Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$ on $\prod_{i=1}^d\mathbb Z/t_i\mathbb

- "Untwisting therefore recovers the cyclic coefficient with the correct
sign." (paper)

  > st. Put $\mathcal R=\mathcal R_r=\mathbb C[y]/(y^r+1)$ and $\zeta=e^{\pi i/r}$. The map \[ \Theta:\mathbb C[x_d]/(x_d^r-1)\longrightarrow\mathcal R, \qquad x_d\longmapsto\zeta y \] is well defined, since $(\zeta y)^r=(-1)(-1)=1$. On the bases $(x_d^k)_{0\le k<r}$ and $(y^k)_{0\le k<r}$ it is diagonal, multiplying coefficient $k$ by the nonzero number $\zeta^k$. It is therefore an isomorphism, with inverse multiplying that coefficient by $\zeta^{-k}$. Both exact maps preserve the coefficient sup norm. For an explicit check on the wrap, write $k+l=j+hr$, where $h\in\{0,1\}$. A product term after twisting and negacyclic reduction has factor \[ \zeta^{k+l}(-1)^h=\zeta^j(\zeta^r)^h(-1)^h=\zeta^j. \] Untwisting therefore recovers the cyclic coefficient with the correct sign. We next specify how this linewise map meets the ring-convolution interface. Put $M=\prod_{i<d}t_i=T/r$. For a complex array $f$ on $\prod_{i=1}^d\mathbb Z/t_i\mathbb Z$, with $t_d=r$, define \[ (\iota f)_{\boldsymbol j} =\sum_{k=0}^{r-1}f_{\boldsymbol j,k}y^k, \qquad \boldsymbol j\in\prod_{i<d}\mathbb Z/t_i\mathbb Z. \] This identifies the scalar tensor with an array of $M$ records in $\mathcal R$. As maps of values, $\iota$ and $\iota^{-1}$ preserve norms and grids. Write $(D_\pm f)_{\boldsymbol j,k}=\zeta^{\pm k}f_{\boldsymbol j,k}$. The linewise extension of $\Theta$ is $\iota D_+$, with inverse $D_-\iota^{-1}$. Consequently, with $\mathcal M_r$ from Section~\ref{sec:exact-ring-products},


## Sources (read from disk as needed)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Length

At most 350 words, not counting mathematics and citations: submit rejects a longer page.

## Answer

The answer is two files: the page body as markdown (not JSON), and a JSON object with the symbols the page binds and its relations to its prerequisite pages. In JSON strings, write each backslash of LaTeX twice (`"\\kappa"`). The JSON follows this schema:

```json
{
  "$defs": {
    "Derivation": {
      "additionalProperties": false,
      "description": "Where the page derives one of the steps the argument gives it.",
      "properties": {
        "quote": {
          "description": "The passage on this page that derives the step, copied exactly: a sentence or more,\noutside citations.",
          "type": "string"
        },
        "step": {
          "description": "The step's id, as listed under \"Steps this page derives\".",
          "type": "string"
        }
      },
      "required": [
        "step",
        "quote"
      ],
      "type": "object"
    },
    "Edge": {
      "additionalProperties": false,
      "description": "What this page uses one prerequisite page for.",
      "properties": {
        "predicate": {
          "description": "A short predicate built from the sentence's own words, such that \"<this page's\nconcept> <predicate> <prerequisite>\" is a true sentence: \"is reduced to\", \"computes\nits transforms by\", \"is based on\".",
          "type": "string"
        },
        "prerequisite": {
          "description": "Id of the prerequisite page.",
          "type": "string"
        },
        "quote": {
          "description": "The sentence on this page that states it, copied exactly. It must link or name the\nprerequisite and contain the predicate's words.",
          "type": "string"
        }
      },
      "required": [
        "prerequisite",
        "predicate",
        "quote"
      ],
      "type": "object"
    },
    "PageBinding": {
      "additionalProperties": false,
      "description": "What a symbol a page introduces denotes, and where the page says so.",
      "properties": {
        "meaning": {
          "description": "One sentence saying what the symbol denotes; for a count, what it counts.",
          "type": "string"
        },
        "name": {
          "description": "Display name of one to four words, e.g. \"record length\".",
          "type": "string"
        },
        "quote": {
          "description": "The sentence on the page that says what the symbol denotes, copied exactly. A use\nin an example (\"take $r = 4$\") does not say what a symbol denotes.",
          "type": "string"
        },
        "relation": {
          "$ref": "#/$defs/Relation"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs,\ne.g. `r` or `\\kappa`.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "name",
        "meaning",
        "relation",
        "quote"
      ],
      "type": "object"
    },
    "Relation": {
      "oneOf": [
        {
          "const": "direct",
          "description": "The symbol denotes a thing: \"ω, a primitive root of unity\".",
          "type": "string"
        },
        {
          "const": "count",
          "description": "The symbol is the number of instances of something: \"r, the number of complex\ncoefficients in a record\".",
          "type": "string"
        }
      ]
    }
  },
  "additionalProperties": false,
  "description": "The structured part of a write answer; the body is the markdown answer file.",
  "properties": {
    "derivations": {
      "default": [],
      "description": "For each step listed under \"Steps this page derives\", the passage on the page that\nderives it. Empty if the task lists none.",
      "items": {
        "$ref": "#/$defs/Derivation"
      },
      "type": "array"
    },
    "relations": {
      "description": "One relation for each prerequisite page: what this page uses it for. Empty if the\npage has no prerequisite pages.",
      "items": {
        "$ref": "#/$defs/Edge"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol the page binds: each symbol it introduces and says what it denotes.\nLeave out symbols listed as already bound, unless the page gives them a new meaning.\nEmpty if the page introduces no symbols.",
      "items": {
        "$ref": "#/$defs/PageBinding"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "relations"
  ],
  "title": "WriteAnswer",
  "type": "object"
}
```

Write the body to `exegenius/tasks/0057-write-coefficient-twist.answer.md` and the JSON to `exegenius/tasks/0057-write-coefficient-twist.answer.json`, then run `exegenius submit 0057-write-coefficient-twist` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0057-write-coefficient-twist`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
