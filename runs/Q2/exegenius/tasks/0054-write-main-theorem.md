# exegenius task 0054-write-main-theorem

Project directory: `/home/user/openai-nlogn-wiki/runs/Q2` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education. In discrete mathematics they have sets, counting and binomial coefficients, induction, graphs, modular arithmetic, gcd and the extended Euclidean algorithm, primes and the Chinese remainder theorem. In algorithms and theory they have worst-case analysis, recurrences, sorting, stacks, binary counters, schoolbook and Karatsuba multiplication, Boolean circuits and the multitape Turing machine with its constant-factor simulations, and in computer arithmetic they have binary, two's-complement and fixed-point numbers with carries. They have also taken a first course in linear algebra over the reals (vector spaces, matrices, Gaussian elimination, triangular matrices, eigenvalues, dot products, projections) and calculus (limits, series, exponentials, Newton's method), plus complex numbers with Euler's formula. They have not studied bilinear forms over finite fields, tensor products, ring theory beyond the integers mod n, Fourier analysis or FFT internals, numerical error analysis, or the integer-multiplication literature after Karatsuba.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine (also: fixed finite-tape model)
- Exact binary multiplication problem
- Schönhage–Strassen optimality conjecture (also: n log n optimality conjecture)
- Harvey–van der Hoeven multiplier (also: established O(n log n) multiplier)
- Cyclic convolution
- Radix-digit reduction to convolution
- Matrix rank (also: rational rank)
- Tensor product of linear maps
- The binary field F₂ and XOR (also: F2, XOR combinations)
- Nondegenerate bilinear spaces and orthogonal complements
- Normalized discrete Fourier transform (also: DFT, Fourier transform)
- Normalized butterfly H₀ (also: butterfly, two-point butterfly)
  - $H_0$ (normalized butterfly): The two-point linear map sending (u, v) to ((u+v)/2, (u−v)/2), i.e. half the 2×2 Hadamard matrix.
- Decimation-in-frequency FFT and bit-reversed order (also: bit reversal, B_t)
- Polynomial ring modulo yʳ + 1 (also: R_r, negacyclic ring)
  - $y$ (polynomial variable): The indeterminate of the ring, whose powers act as roots of unity because y to the r equals −1.
  - $r$ (record length): The number of complex coefficients in each polynomial record, a power of two.
- Synthetic roots of unity
- Synthetic polynomial transform (also: Nussbaumer transform, synthetic transform)
- Gaussian dyadic numbers
- Disk grid and truncation (also: D_p, Q_p, p-bit grid)
- Contractions and error accounting
- Signed Kronecker substitution (also: signed packing)
- Lexicographic array layout and logical volume (also: logical volume, address field, row)
- Elementary stream operations
- Controlled cyclic shifts
- Linear network with wire roles (also: role, scratch wires, gate)
- Scratch restoration schedule
- Three-element subset intersection gadget (also: gather, scatter, side injection, Frankl–Wilson construction)
- Three-stage bank exchange
- Frames and the common-frame identity (also: frame, endpoint operator)
- Subspace labels and orthogonal residuals (also: labels, orthogonal residual)
- Rank saving s < Wm (also: rank deficit)
  - $s$ (number of smaller calls): The number of smaller recursive calls one network invocation makes, equal to the summed ranks or residual dimensions over all edges.
  - $W$ (number of wires): The number of wires (roles) in the fixed linear network, which is also the number of streams the rows are split into.
  - $m$ (label dimension): The dimension of the fixed label space, which is the factor by which each recursive call shrinks its parameter.
- Row splitting among wire roles
- Fixed-tape depth-first recursion schedule
- Address shear (also: rational matrix interface)
- Lower-triangular Bruhat factorization
- Matrix shear by interchanges
- Recursive power-width interchange
- Fast address-chunk interchange (also: chunk swap, address interchange)
- Phase kernel C
  - $C$ (phase kernel): The two-point matrix aI + bX with a = (1+i)/2 and b = (1−i)/2, where X swaps the two coordinates.
- Binary phase frames (also: complex phase network, complex motif interface)
- Packed selected-bit addition (also: binary change of basis, deterministic repair)
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Synthetic transform tape layout
- Convolution over the polynomial ring
- Coefficient phase twist
- Gaussian resampling
- Retained source and target permutations
- Bluestein chirp identity
- Distinct prime axis lengths
- Chinese-remainder address map (also: CRT map, Agarwal–Cooley map)
- Exact coefficient recovery
- Parameter choice and cost table
- Binary representation of integers (also: base-2 representation, binary numeral, most significant bit, least significant bit, leading zeroes, bit string)
- Logarithms (also: log base 2, log_2, lg, logarithm laws)
- Floor and ceiling functions (also: floor, ceiling, rounding down, rounding up, nearest integer, integer part)
- Two's complement (also: signed binary integers, two's-complement word, sign bit)
- Fixed-point binary numbers (also: fixed-point arithmetic, dyadic fraction, fractional bits, guard bits, binary point)
- Schoolbook binary arithmetic and carry propagation (also: carry, carry propagation, ripple-carry addition, long multiplication, schoolbook multiplication, grade-school multiplication)
- Integer division with remainder (also: quotient and remainder, Euclidean division, integer square root, floor of a/b)
- Modular arithmetic (also: congruence, residues, mod, integers modulo Q, Z/QZ, residue counter, modular inverse)
- Greatest common divisor and the extended Euclidean algorithm (also: gcd, coprime, relatively prime, pairwise coprime, Euclid's algorithm, extended Euclidean algorithm, Bezout coefficients)
- Prime numbers (also: primes, odd prime, trial division)
- Chinese remainder theorem (also: CRT, Chinese remaindering)
- Sets, Cartesian products and indicator vectors (also: subset, intersection, cardinality, Cartesian product, characteristic vector, indicator vector, support)
- Binomial coefficients (also: n choose k, combinations, three-element subsets, counting subsets)
- Permutations and bijections (also: permutation, bijection, inverse permutation, composition of permutations, isomorphism, one-to-one correspondence)
- Mathematical induction (also: proof by induction, inductive argument)
- Directed graphs (also: vertices, edges, nodes, path, head and tail of an edge)
- Worst-case running time (also: time complexity, worst-case cost, deterministic algorithm, bit complexity)
- RAM model of computation (also: random-access machine, unit-cost RAM, word RAM, random access)
- Recurrence relations and divide and conquer (also: recurrence, divide-and-conquer, recursive algorithm, master theorem, solving recurrences)
- Geometric series (also: geometric sum, geometrically increasing)
- Karatsuba multiplication (also: Karatsuba's algorithm, Karatsuba–Ofman, O(n^{log₂3}) multiplication)
- Polynomial evaluation and interpolation (also: evaluation and interpolation, Lagrange interpolation, Toom-Cook idea, coefficient representation)
- Sorting (also: sort, merge sort, radix sort, O(n log n) sorting, label-and-sort)
- Stacks (also: stack, push and pop, LIFO, stack tape)
- Binary counters (also: binary counter, counter increment, amortized increment cost, ripple counting)
- Matrix transposition and row-major order (also: transpose, row-major, matrix transpose)
- Vector spaces, subspaces and dimension (also: linear subspace, span, basis, linear independence, dimension, linear combination, Q^h, ground field)
- Matrices and linear maps (also: matrix multiplication, identity matrix, invertible matrix, inverse, diagonal matrix, linear operator, all-ones matrix, change of basis, transpose of a matrix)
- Gaussian elimination and triangular matrices (also: row reduction, elementary matrices, pivot, lower triangular matrix, LU decomposition, elimination)
- Eigenvalues (also: eigenvalue, eigenvector, diagonalization)
- Dot product and orthonormal bases (also: inner product, dot product, orthogonal vectors, orthonormal basis, unit vector, norm one)
- Projections onto subspaces (also: projection matrix, orthogonal projection, projection along a complement, idempotent matrix)
- Direct sums (also: direct sum, ⊕, block-diagonal operator, complementary subspaces)
- Hamming weight (also: weight, wt(x), number of ones, population count, parity)
- Euler's formula and the complex exponential (also: e^{iθ}, Euler's formula, complex exponential, phase, e^{2πi jk/q})
- Exponential function and Gaussian function (also: exponential, e^x, Gaussian, e^{-x^2}, bell curve)
- Limits and convergent series (also: limit, limit of a sequence, infinite series, absolute convergence, convergence)
- Triangle inequality (also: |a + b| ≤ |a| + |b|, absolute value bound)
- Newton's method (also: Newton iteration, Newton–Raphson, quadratic convergence, Newton reductions)

## This page

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: The main theorem: one deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in that model.
Also called: Theorem 1, main result
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input bit length): The number of bits in each of the two input integers.
- $\lg$ (rounded binary logarithm): The function lg n = max{⌈log₂ n⌉, 1}.
- $\kappa$ (saving exponent): The fixed constant 2^−182 by which the exponent of the logarithmic factor is reduced below one.

## This page in the argument

The step: One deterministic fixed-alphabet multitape Turing machine computes $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$ for all $n$-bit inputs in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in that model.
How: build two sub-logarithmic tape procedures (address-chunk interchange and simultaneous butterfly layers) from finite linear networks with a rank saving, insert them into the Harvey--van der Hoeven reduction of multiplication to convolution over $\mathbb C[y]/(y^r+1)$ via a Chinese-remainder map, Gaussian resampling, chirps and a phase twist, recover the integer coefficients exactly, and sum the normalized cost table
Why: In the $O(n\log n)$ approach every one of $\Theta(\log n)$ transform levels rescans $\Theta(n)$ bits, so going below $n\log n$ requires saving both on address movement and on butterfly arithmetic, which is what the two network-based procedures provide. (the sources say so: "Scanning an array of $\Theta(n)$ stored bits at each of
$\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$.
We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The saving is a fixed power of the logarithm, uniform over all input lengths, with the explicit but tiny exponent $\kappa=2^{-182}$. (explain why it holds, from the method)

Its sub-steps, in order:

- Two disjoint contiguous address fields of $u$ bits in an array of logical volume $V$ can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time for a fixed $\tau<1$. (on [Fast address-chunk interchange](chunk-swap.md))
- A layer of normalized butterflies $H_0$ on the same bit position of $D\le d$ address chunks of an array of polynomial records can be applied, exactly and then truncated once, in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))
- Normalized cyclic convolution of arrays of $\mathbb C[y]/(y^r+1)$ records on power-of-two axes of total size $T$ can be approximated within $\sqrt2\,M(3\ell+1)2^{-p}$ at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$. (on [Convolution over the polynomial ring](synthetic-convolution.md))
- The permuted multidimensional source transform $RF_{\boldsymbol s}$ on distinct prime axes equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with power-of-two axes, its middle factor $QF_{\boldsymbol t}$ is a chirp-wrapped cyclic convolution, and the retained permutation $R$ cancels in a convolution.
- Distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist, give $T/2<S<T$, and satisfy every hypothesis of the resampling lemma for large $n$. (on [Distinct prime axis lengths](prime-axis-lengths.md))
- Splitting the inputs into $q=\lceil n/b\rceil$ radix-$2^b$ digits makes the product a convolution of coefficients $0\le c_j<2^{3b}$, with no wraparound modulo $x^S-1$. (on [Radix-digit reduction to convolution](radix-digit-convolution.md))
- The map $x\mapsto\prod_ix_i^{\mu_i}$ is an isomorphism from cyclic convolution of length $S$ to multidimensional cyclic convolution on the prime axes, implemented by triangular controlled shifts and axis moves in $O(Tp\,d^2(1+\ell^\tau))$ time. (on [Chinese-remainder address map](crt-address-map.md))
- Multiplying coefficient $k$ of the last axis by $\zeta^k$, $\zeta=e^{\pi i/r}$, turns normalized complex cyclic convolution on power-of-two axes into convolution over $\mathbb C[y]/(y^r+1)$, and untwisting recovers the cyclic wrap with the correct sign. (on [Coefficient phase twist](phase-twist.md))
- The composed procedure (CRT map, two source transforms, pointwise product, opposite transform, rescaling) returns every product coefficient within less than $1/2$, so rounding and carry propagation give exactly $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$. (on [Exact coefficient recovery](exact-recovery.md))
- With $\tau=1-2^{-50}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$ and $V=Tp=\Theta(n)$, every normalized cost term is at most $p^{1-2\kappa}$, so the total time is $O(n(\lg n)^{1-\kappa})$ for large $n$. (on [Parameter choice and cost table](parameter-cost-table.md))
- Below one fixed cutoff the machine uses schoolbook multiplication, so the bound holds for every $n\ge1$.
- A single machine with time $O(n(\lg n)^{1-\kappa})$ has $T_A(n)/(n\lg n)\to0$, which refutes an eventual $\Omega(n\lg n)$ lower bound in the fixed multitape model.

## Steps this page derives

The argument gives this page these sub-steps of its step (S4, S11, S12). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4**: The permuted multidimensional source transform $RF_{\boldsymbol s}$ on distinct prime axes equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with power-of-two axes, its middle factor $QF_{\boldsymbol t}$ is a chirp-wrapped cyclic convolution, and the retained permutation $R$ cancels in a convolution.
How: apply Gaussian resampling linewise while keeping the source and target permutations inside the identity, evaluate the middle factor by Bluestein's chirp identity, and show the source permutation cancels
- S4.2: Applying the one-dimensional maps line by line gives the tensor identity $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$, with axis movements done by chunk interchanges.
  Source: "For the tensor product, apply the one-dimensional maps to one coordinate
line at a time." (paper)
  > For the tensor product, apply the one-dimensional maps to one coordinate line at a time. The chunk-swap algorithm supplies the movement of the physical axis fields, including its cost when the number of axes grows.

**S11**: Below one fixed cutoff the machine uses schoolbook multiplication, so the bound holds for every $n\ge1$.
Source: "Fix one cutoff beyond all the size, precision, margin and layout
conditions, and use schoolbook multiplication below it." (paper)
> Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

**S12**: A single machine with time $O(n(\lg n)^{1-\kappa})$ has $T_A(n)/(n\lg n)\to0$, which refutes an eventual $\Omega(n\lg n)$ lower bound in the fixed multitape model.
Source: "The theorem refutes an
eventual $\Omega(n\log n)$ lower bound for every fixed multiplication
machine in this model." (paper)
> The bound is asymptotic through all input lengths. The constants and thresholds in the construction are extremely large; the algorithm is intended to establish a bit-complexity bound. The theorem refutes an eventual $\Omega(n\log n)$ lower bound for every fixed multiplication machine in this model.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Fast address-chunk interchange](chunk-swap.md)): Two disjoint contiguous address fields of $u$ bits in an array of logical volume $V$ can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time for a fixed $\tau<1$.
- S2 (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)): A layer of normalized butterflies $H_0$ on the same bit position of $D\le d$ address chunks of an array of polynomial records can be applied, exactly and then truncated once, in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$.
- S3 (on [Convolution over the polynomial ring](synthetic-convolution.md)): Normalized cyclic convolution of arrays of $\mathbb C[y]/(y^r+1)$ records on power-of-two axes of total size $T$ can be approximated within $\sqrt2\,M(3\ell+1)2^{-p}$ at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.
- S5 (on [Distinct prime axis lengths](prime-axis-lengths.md)): Distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist, give $T/2<S<T$, and satisfy every hypothesis of the resampling lemma for large $n$.
- S6 (on [Radix-digit reduction to convolution](radix-digit-convolution.md)): Splitting the inputs into $q=\lceil n/b\rceil$ radix-$2^b$ digits makes the product a convolution of coefficients $0\le c_j<2^{3b}$, with no wraparound modulo $x^S-1$.
- S7 (on [Chinese-remainder address map](crt-address-map.md)): The map $x\mapsto\prod_ix_i^{\mu_i}$ is an isomorphism from cyclic convolution of length $S$ to multidimensional cyclic convolution on the prime axes, implemented by triangular controlled shifts and axis moves in $O(Tp\,d^2(1+\ell^\tau))$ time.
- S8 (on [Coefficient phase twist](phase-twist.md)): Multiplying coefficient $k$ of the last axis by $\zeta^k$, $\zeta=e^{\pi i/r}$, turns normalized complex cyclic convolution on power-of-two axes into convolution over $\mathbb C[y]/(y^r+1)$, and untwisting recovers the cyclic wrap with the correct sign.
- S9 (on [Exact coefficient recovery](exact-recovery.md)): The composed procedure (CRT map, two source transforms, pointwise product, opposite transform, rescaling) returns every product coefficient within less than $1/2$, so rounding and carry propagation give exactly $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$.
- S10 (on [Parameter choice and cost table](parameter-cost-table.md)): With $\tau=1-2^{-50}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$ and $V=Tp=\Theta(n)$, every normalized cost term is at most $p^{1-2\kappa}$, so the total time is $O(n(\lg n)^{1-\kappa})$ for large $n$.
- S4.1 (on [Gaussian resampling](gaussian-resampling.md)): For coprime $s<t$ with enough separation, $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$ for contractions $A,B_0$ built from Gaussian kernels, approximable with error below $p^2$ in $O(tp^{3/2+\delta}\alpha)$ time.
- S4.3 (on [Bluestein chirp identity](bluestein-chirp.md)): With the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$, $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$, so the target permutation is absorbed by the chirp.
- S4.4 (on [Retained source and target permutations](retained-permutations.md)): $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$, so the source permutation $R$ never has to be executed.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Normalized discrete Fourier transform](dft.md)
- [Tensor product of linear maps](tensor-product.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Schönhage–Strassen optimality conjecture](optimality-conjecture.md): The 1971 conjecture that n log n is the optimal order of integer multiplication cost, i.e. that every fixed multitape multiplication machine eventually needs time Ω(n lg n).
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Schönhage–Strassen optimality conjecture
- [Exact binary multiplication problem](exact-multiplication-problem.md): The task of reading x#y for two n-bit binary strings and writing the exact 2n-bit binary product val(x)·val(y), with lg n = max{⌈log₂ n⌉, 1}.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Exact binary multiplication problem
- [Harvey–van der Hoeven multiplier](hvdh-multiplier.md): The previously established O(n log n) multitape integer multiplication algorithm, used here only as an ordinary subroutine on short records.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Harvey–van der Hoeven multiplier
- [Radix-digit reduction to convolution](radix-digit-convolution.md): Splitting each input into radix-2^b digits turns the integer product into a convolution of short nonnegative coefficients, from which the binary product is recovered by carry propagation.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Radix-digit reduction to convolution
- [Chinese-remainder address map](crt-address-map.md): The isomorphism x ↦ ∏ xᵢ^{μᵢ} from one cyclic convolution of length S = ∏ sᵢ to a multidimensional cyclic convolution on the prime axes, implemented on tape by triangular controlled shifts and axis moves.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Chinese-remainder address map
- [Gaussian resampling](gaussian-resampling.md): The Harvey–van der Hoeven identity expressing a Fourier transform of prime length s through one of power-of-two length t > s, sandwiched between contractions built from Gaussian kernels, with a scale factor 2^{2α²}.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Gaussian resampling
- [Retained source and target permutations](retained-permutations.md): Keeping the coordinate permutations of Gaussian resampling inside the transform identity instead of sorting, since the target permutation is absorbed by the chirp step and the source permutation cancels in the convolution.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Retained source and target permutations
- [Bluestein chirp identity](bluestein-chirp.md): The identity writing a Fourier transform (here including its frequency permutation) as pointwise multiplication by a chirp, a cyclic convolution with the chirp, and another chirp multiplication.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Bluestein chirp identity
- [Coefficient phase twist](phase-twist.md): Multiplying the k-th coefficient of the last cyclic axis by ζ^k with ζ = e^{πi/r}, which turns cyclic convolution of length r into multiplication modulo yʳ + 1 and is undone afterwards.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Coefficient phase twist
- [Convolution over the polynomial ring](synthetic-convolution.md): Normalized cyclic convolution of arrays of ℂ[y]/(yʳ+1) records computed by two forward synthetic transforms kept in their stored order, packed pointwise polynomial products, and one opposite transform.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Convolution over the polynomial ring
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): A procedure applying H₀ on the same bit position of up to d address chunks of an array of polynomial records at once, in O(V d^{λ′}) time for a fixed λ′ < 1, evaluated exactly and truncated once.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Simultaneous butterfly layer
- [Fast address-chunk interchange](chunk-swap.md): A fixed multitape procedure that exchanges two disjoint contiguous address fields of u bits in O(V u^τ) time for a fixed τ < 1, using XOR combinations of data although its final effect is a permutation.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fast address-chunk interchange
- [Exact coefficient recovery](exact-recovery.md): Undoing the known scalings, showing the computed convolution coefficients are within 1/2 of the true integers, rounding them, and propagating carries to obtain the exact binary product.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Exact coefficient recovery
- [Parameter choice and cost table](parameter-cost-table.md): The fixed rational exponents and size parameters (b, p, d, K, r, ℓ) for which every normalized cost term is at most p^{1−2κ}, so the total time is O(n (lg n)^{1−κ}).
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Parameter choice and cost table

## Other pages you may link to

- [Polynomial ring modulo yʳ + 1](poly-ring.md)
- [Synthetic roots of unity](synthetic-roots.md)
- [Normalized butterfly H₀](fft-butterfly.md)
- [The binary field F₂ and XOR](binary-field.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)
- [Linear network with wire roles](linear-network.md)
- [Three-element subset intersection gadget](subset-intersection-gadget.md)
- [Signed Kronecker substitution](kronecker-packing.md)
- [Scratch restoration schedule](scratch-restoration.md)
- [Three-stage bank exchange](bank-exchange.md)
- [Lexicographic array layout and logical volume](lexicographic-array-layout.md)
- [Frames and the common-frame identity](frames.md)
- [Elementary stream operations](elementary-streams.md)
- [Row splitting among wire roles](row-splitting.md)
- [Controlled cyclic shifts](controlled-shifts.md)
- [Matrix rank](matrix-rank.md)
- [Lower-triangular Bruhat factorization](bruhat-factorization.md)
- [Nondegenerate bilinear spaces and orthogonal complements](bilinear-forms.md)
- [Tensor product of linear maps](tensor-product.md)
- [Subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank saving s < Wm](rank-saving.md)
- [Address shear](address-shear.md)
- [Matrix shear by interchanges](matrix-shear-cost.md)
- [Fixed-tape depth-first recursion schedule](depth-first-schedule.md)
- [Recursive power-width interchange](power-width-interchange.md)
- [Phase kernel C](phase-kernel.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Disk grid and truncation](disk-grid-truncation.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Normalized discrete Fourier transform](dft.md)
- [Decimation-in-frequency FFT and bit-reversed order](decimation-in-frequency.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Synthetic transform tape layout](transform-layout.md)
- [Contractions and error accounting](contraction-error.md)
- [Distinct prime axis lengths](prime-axis-lengths.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model." (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}


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

Write the body to `exegenius/tasks/0054-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0054-write-main-theorem.answer.json`, then run `exegenius submit 0054-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0054-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
