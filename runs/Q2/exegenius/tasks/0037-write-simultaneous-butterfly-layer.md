# exegenius task 0037-write-simultaneous-butterfly-layer

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
- Matrix rank (also: rational rank)
- Tensor product of linear maps
- The binary field F₂ and XOR (also: F2, XOR combinations)
- Nondegenerate bilinear spaces and orthogonal complements
- Normalized butterfly H₀ (also: butterfly, two-point butterfly)
  - $H_0$ (normalized butterfly): The two-point linear map sending (u, v) to ((u+v)/2, (u−v)/2), i.e. half the 2×2 Hadamard matrix.
- Polynomial ring modulo yʳ + 1 (also: R_r, negacyclic ring)
  - $y$ (polynomial variable): The indeterminate of the ring, whose powers act as roots of unity because y to the r equals −1.
  - $r$ (record length): The number of complex coefficients in each polynomial record, a power of two.
- Synthetic roots of unity
- Gaussian dyadic numbers
- Disk grid and truncation (also: D_p, Q_p, p-bit grid)
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

Concept: Simultaneous butterfly layer
Gloss: A procedure applying H₀ on the same bit position of up to d address chunks of an array of polynomial records at once, in O(V d^{λ′}) time for a fixed λ′ < 1, evaluated exactly and truncated once.
Also called: parallel butterfly layer

## This page in the argument

The step: A layer of normalized butterflies $H_0$ on the same bit position of $D\le d$ address chunks of an array of polynomial records can be applied, exactly and then truncated once, in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$.
How: write the $H_0$ layer as $b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, compute $C^{\otimes e}$ by the complex network with binary phase frames (each edge is a few $C$ layers on $e/m$ chunks after packed binary basis changes), recurse on row-split streams, keep exact Gaussian dyadics with guard bits and truncate once
Why: Applying $D$ butterfly factors one after another costs $D$ whole-array passes; the phase frames express a $C$ tensor product through smaller groups of selected bits so that the rank saving $s<Wm$ gives a sublinear dependence on $d$. (the sources say so: "We will obtain cost $O(Vd^{\lambda'})$, with
$\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly
factors would require $D$ whole-array passes." (paper))

Its sub-steps, in order:

- The kernel $C=H\mathsf SH=aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$ satisfies $H_0=b\mathsf SC\mathsf S$, $C^4=I$ and $C^{-1}=-iZCZ$, all with Gaussian dyadic coefficients. (on [Phase kernel C](phase-kernel.md))
- With binary phase frames $\mathcal C_U$ on the complex network, each edge factors into one translation kernel per orthonormal residual vector, so a group of $e=mf$ selected axes needs exactly $s$ child calls on $f$ axes, after binary basis changes, and the endpoints give $C^{\otimes e}$ on every role. (on [Binary phase frames](phase-frames.md))
- On all $D$ selected coordinates, $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, where $\mathcal S_D$ is a diagonal fourth-root phase and $b^D$ a binary shift and phase.
- A binary row addition on selected bits of two address chunks is performed by eight packed cyclic shifts of whole chunk ranges plus a deterministic sort-based repair of a small exceptional set, in $O(V(L^\tau+1))$ time for chunks of $L$ bits. (on [Packed selected-bit addition](packed-selected-bit-addition.md))
- Splitting rows among the $W$ roles gives the time-per-volume recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, which unrolls to $O(d^{\lambda'})$.
- Reserving $p+\Delta$ fractional and $\Delta+3$ integer bits, with $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$, represents every intermediate value of the layer exactly.
- Since $H_0^{\otimes D}$ maps disk arrays to disk arrays, the single final truncation $Q_p$ keeps the output in the disk with error below $\sqrt2\,2^{-p}$.

It serves these steps, from the main result down:

- One deterministic fixed-alphabet multitape Turing machine computes $\operatorname{bin}_{2n}(\operatorname{val}(x)\operatorname{val}(y))$ for all $n$-bit inputs in time $O(n(\lg n)^{1-\kappa})$ with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in that model.; how: build two sub-logarithmic tape procedures (address-chunk interchange and simultaneous butterfly layers) from finite linear networks with a rank saving, insert them into the Harvey--van der Hoeven reduction of multiplication to convolution over $\mathbb C[y]/(y^r+1)$ via a Chinese-remainder map, Gaussian resampling, chirps and a phase twist, recover the integer coefficients exactly, and sum the normalized cost table (on [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.3, S2.5, S2.6, S2.7). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.3**: On all $D$ selected coordinates, $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$, where $\mathcal S_D$ is a diagonal fourth-root phase and $b^D$ a binary shift and phase.
Source: "Applying
\eqref{eq:phase-basic-identities} on all selected coordinates gives" (paper)
> \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

**S2.5**: Splitting rows among the $W$ roles gives the time-per-volume recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$, which unrolls to $O(d^{\lambda'})$.
Source: "Indeed, the \(s\) child calls are executed on streams of volume
\(V/W\), so their total cost is \(s(V/W)F(e/m)\)." (paper)
> \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).

**S2.6**: Reserving $p+\Delta$ fractional and $\Delta+3$ integer bits, with $\Delta=\lceil C_0d^{C_1}\rceil=o(p)$, represents every intermediate value of the layer exactly.
Source: "Thus reserving \(p+\Delta\)
fractional bits and \(\Delta+3\) integer and sign bits per real
component represents every intermediate coefficient exactly and
prevents overflow." (paper)
> To see how this count controls numerical size, start with disk-valued coefficients in \(2^{-p}\mathbb Z[i]\). A value at depth \(\ell\) lies in \(2^{-(p+\ell)}\mathbb Z[i]\) and has modulus at most \(2^\ell\). This follows by induction: addition or subtraction can at most double the maximum modulus of its operands; halving adds at most one denominator bit; and signs and multiplication by \(i\) preserve both bounds. The charge of \(t\) for the final shift is the same as \(t\) successive halvings. Thus reserving \(p+\Delta\) fractional bits and \(\Delta+3\) integer and sign bits per real component represents every intermediate coefficient exactly and prevents overflow. Shifts consume the reserved fractional zeros and discard no bits.

**S2.7**: Since $H_0^{\otimes D}$ maps disk arrays to disk arrays, the single final truncation $Q_p$ keeps the output in the disk with error below $\sqrt2\,2^{-p}$.
Source: "Finally, every row of $\mathcal H$ has
absolute row sum one." (paper)
> The guard-width calculation above bounds both denominator and magnitude growth by $\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, this is $o(p)$ uniformly over the allowed $d$, so every intermediate coefficient is represented exactly with the stated $O(p)$ width. The initial scan removes or adds only redundant leading sign bits and appends the reserved fractional zeros to put each supplied component in this guarded format. To truncate toward zero at the end, shift its absolute numerator right by the number of added fractional bits, restore its sign, and write the result in $w$ bits. These scans cost $O(V)$. Finally, every row of $\mathcal H$ has absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation preserves that disk and has error less than $\sqrt2\,2^{-p}$: truncation cannot increase the absolute value of either component, and changes each by less than $2^{-p}$. The truncated numerators have magnitude at most $2^p$, so the supplied component width can hold them. \end{proof} \section{Synthetic transforms and their tape layout} \label{sec:synthetic-layouts}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.1 (on [Phase kernel C](phase-kernel.md)): The kernel $C=H\mathsf SH=aI+bX$ with $a=(1+i)/2$, $b=(1-i)/2$ satisfies $H_0=b\mathsf SC\mathsf S$, $C^4=I$ and $C^{-1}=-iZCZ$, all with Gaussian dyadic coefficients.
- S2.2 (on [Binary phase frames](phase-frames.md)): With binary phase frames $\mathcal C_U$ on the complex network, each edge factors into one translation kernel per orthonormal residual vector, so a group of $e=mf$ selected axes needs exactly $s$ child calls on $f$ axes, after binary basis changes, and the endpoints give $C^{\otimes e}$ on every role.
- S2.4 (on [Packed selected-bit addition](packed-selected-bit-addition.md)): A binary row addition on selected bits of two address chunks is performed by eight packed cyclic shifts of whole chunk ranges plus a deterministic sort-based repair of a small exceptional set, in $O(V(L^\tau+1))$ time for chunks of $L$ bits.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Phase kernel C](phase-kernel.md)
- [Tensor product of linear maps](tensor-product.md)
- [Rank saving s < Wm](rank-saving.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Binary phase frames](phase-frames.md): Frames 𝒞_U = H^{⊗m}·diag(i^{wt(P_U x) mod 4})·H^{⊗m} attached to binary labels U, whose edge changes factor into one translation kernel per orthonormal residual vector and whose endpoints give C^{⊗m} on every role.
  Shown as: Simultaneous butterfly layer *<predicate>* Binary phase frames
- [Packed selected-bit addition](packed-selected-bit-addition.md): Performing XORs of one selected bit position across many K-bit address chunks at once by eight packed cyclic shifts of whole chunk ranges plus a deterministic sort-based repair of a small set of exceptional addresses.
  Shown as: Simultaneous butterfly layer *<predicate>* Packed selected-bit addition
- [Row splitting among wire roles](row-splitting.md): Distributing whole rows of an array cyclically among the W network roles (padding the row count), so every role stream has the same address set and volume V/W and gates act pointwise on matching addresses.
  Shown as: Simultaneous butterfly layer *<predicate>* Row splitting among wire roles
- [Fixed-tape depth-first recursion schedule](depth-first-schedule.md): Running the recursive calls one at a time while parking the inactive role streams on a stack tape, so a fixed number of tapes serves every depth and each node's overhead is linear in its own volume.
  Shown as: Simultaneous butterfly layer *<predicate>* Fixed-tape depth-first recursion schedule
- [Normalized butterfly H₀](fft-butterfly.md): The two-point map H₀(u, v) = ((u+v)/2, (u−v)/2), the basic arithmetic step of a radix-two fast Fourier transform.
  Shown as: Simultaneous butterfly layer *<predicate>* Normalized butterfly H₀
- [Disk grid and truncation](disk-grid-truncation.md): Fixed-point storage of complex values in the unit disk on the grid 2^{−p}ℤ[i], with Q_p truncating real and imaginary parts toward zero, an error below √2·2^{−p} that never increases the norm.
  Shown as: Simultaneous butterfly layer *<predicate>* Disk grid and truncation
- [Polynomial ring modulo yʳ + 1](poly-ring.md): The ring ℂ[y]/(yʳ+1) of complex polynomials of degree below r, r a power of two, in which yʳ = −1 so that multiplication wraps negacyclically.
  Shown as: Simultaneous butterfly layer *<predicate>* Polynomial ring modulo yʳ + 1

## Pages that build on this one

- Synthetic transform tape layout: A layout permutation that places the bits of all transform axes at common offsets in consecutive K-bit chunks so each round of the synthetic transform is one simultaneous butterfly layer plus a recordwise twiddle shift.
- Parameter choice and cost table: The fixed rational exponents and size parameters (b, p, d, K, r, ℓ) for which every normalized cost term is at most p^{1−2κ}, so the total time is O(n (lg n)^{1−κ}).
- Integer multiplication in O(n (lg n)^(1−κ)) time: The main theorem: one deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in that model.

## Other pages you may link to

- [Exact binary multiplication problem](exact-multiplication-problem.md)
- [Schönhage–Strassen optimality conjecture](optimality-conjecture.md)
- [Synthetic roots of unity](synthetic-roots.md)
- [The binary field F₂ and XOR](binary-field.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)
- [Linear network with wire roles](linear-network.md)
- [Three-element subset intersection gadget](subset-intersection-gadget.md)
- [Harvey–van der Hoeven multiplier](hvdh-multiplier.md)
- [Signed Kronecker substitution](kronecker-packing.md)
- [Scratch restoration schedule](scratch-restoration.md)
- [Three-stage bank exchange](bank-exchange.md)
- [Lexicographic array layout and logical volume](lexicographic-array-layout.md)
- [Frames and the common-frame identity](frames.md)
- [Elementary stream operations](elementary-streams.md)
- [Controlled cyclic shifts](controlled-shifts.md)
- [Matrix rank](matrix-rank.md)
- [Lower-triangular Bruhat factorization](bruhat-factorization.md)
- [Nondegenerate bilinear spaces and orthogonal complements](bilinear-forms.md)
- [Tensor product of linear maps](tensor-product.md)
- [Subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank saving s < Wm](rank-saving.md)
- [Address shear](address-shear.md)
- [Matrix shear by interchanges](matrix-shear-cost.md)
- [Recursive power-width interchange](power-width-interchange.md)
- [Fast address-chunk interchange](chunk-swap.md)
- [Phase kernel C](phase-kernel.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit reduction to convolution](radix-digit-convolution.md)
- [Coefficient phase twist](phase-twist.md)
- [Normalized discrete Fourier transform](dft.md)
- [Decimation-in-frequency FFT and bit-reversed order](decimation-in-frequency.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Synthetic transform tape layout](transform-layout.md)
- [Contractions and error accounting](contraction-error.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Convolution over the polynomial ring](synthetic-convolution.md)
- [Retained source and target permutations](retained-permutations.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Exact coefficient recovery](exact-recovery.md)
- [Distinct prime axis lengths](prime-axis-lengths.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Parameter choice and cost table](parameter-cost-table.md)
- [Integer multiplication in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Simultaneous normalized butterfly layer" (paper)

  > \begin{proposition}[Simultaneous normalized butterfly layer] \label{prop:simultaneous-layer} Fix \[ \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad C_1=20. \] Let $c,\epsilon,\lambda,\lambda'$ be fixed positive rational numbers satisfying \[ \max\{\tau,\sigma\}<\lambda<1,\qquad \tau(1+c/\beta)<\lambda,\qquad \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1, \qquad \epsilon C_1<1. \] Fix positive constants $a_d\le b_d$ and $a_r\le b_r$, and fix positive constants $C_M,C_{\rm desc},C_w$ with $C_w>1$. For these fixed choices there are a cutoff $p_0$, one fixed finite-alphabet multitape procedure, and an implicit time constant with the following guarantee. The cutoff and time constant may depend on the fixed rational parameters and these constants. For every choice of positi

- "the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$" (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.

- "The entire layer is evaluated exactly before one final truncation." (paper)

  > We first construct tensor products of the auxiliary two-point kernel $C$ from Proposition~\ref{prop:complex-motif-interface}. Its phase frames express a $C$ tensor product using smaller groups of selected bits, separated by binary changes of basis. We implement those changes by moving whole address chunks. Splitting complete rows among the network's wire roles then reduces the volume of each recursive call. Finally, we bound the intermediate dyadic values and convert the completed $C$ layer to the normalized $H_0$ layer. The entire layer is evaluated exactly before one final truncation.


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

Write the body to `exegenius/tasks/0037-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0037-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0037-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0037-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
