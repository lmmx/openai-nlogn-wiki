# exegenius task 0040-write-main-theorem

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N5` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, permutations, modular arithmetic, gcd and the Chinese remainder theorem, induction, binomial coefficients), the algorithms course (asymptotic notation, recurrences, Karatsuba, the FFT and FFT-based polynomial multiplication, bit-reversal, binary counters, stacks), introductory computability (Turing machines with multiple tapes and constant-factor simulations), and the supporting mathematics of a CS degree: calculus with limits, exponentials and Newton's method, complex numbers, and a first linear algebra course (matrices, rank, invertibility, subspaces, dimension, dot products and orthogonality over the reals, Gaussian elimination). They have not studied bilinear forms over general fields, tensor products of operators, Bruhat factorizations, algebraic complexity of integer multiplication beyond Karatsuba and the basic FFT, or research-level fast multiplication (Schönhage–Strassen, Fürer, Harvey–van der Hoeven, Nussbaumer transforms, Gaussian resampling), nor index coding or the Frankl–Wilson construction.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Harvey–van der Hoeven O(n log n) multiplier
- Normalized discrete Fourier transform (also: DFT, Fourier transform)
- Cyclic convolution
- Multidimensional Fourier transform
- Radix-digit reduction to convolution
- Arrays on tape and logical volume (also: logical volume, row field)
- Elementary stream operations
- Controlled shifts and rational scalings (also: ordered affine updates)
- Linear network with wire roles (also: role, scratch wires)
- Restoration of arbitrary scratch values (also: transparent computation)
- Triple-intersection bank exchange (also: bit construction, complex construction, three-stage bank exchange)
- Frames and the common-frame identity (also: frame)
- Nested subspace labels and orthogonal residuals
- Rank deficit s < Wm
  - $s$ (smaller-call count): The total number of smaller recursive calls needed on all network edges (sum of edge ranks or residual dimensions).
  - $W$ (wire count): The number of wires (roles) in the fixed network, including scratch wires.
  - $m$ (label dimension): The dimension of the ambient label space, the number of address fields per chunk handled by one recursion level (here 10⁶).
- Recursive power saving
- Lower triangular factorization (also: Bruhat factorization)
- Address shear (also: matrix shear)
- Bit network interface
- Fast address-chunk interchange (also: chunk swap, address interchange)
- Normalized butterfly H₀ (also: butterfly)
  - $H_0$ (normalized butterfly): The 2×2 map sending a pair (u,v) to ((u+v)/2,(u−v)/2).
- Gaussian dyadic numbers
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial records, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in each polynomial record, a power of two.
- Fixed-point disk grid and truncation (also: disk grid, precision p)
- Binary phase frames (also: complex phase network)
- Simultaneous butterfly layer
- Synthetic polynomial transform (also: Nussbaumer transform)
- Fast synthetic transform layout
- Signed Kronecker packing (also: Kronecker substitution)
- Normalized convolution over the polynomial ring
- Coefficient twist (also: phase twist)
- Gaussian resampling with retained permutations
- Bluestein chirp identity (also: chirp)
- Chinese-remainder address map (also: CRT map, Agarwal–Cooley)
- Exact coefficient recovery and carries
- Fixed rational parameters and cost table
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, o(n log n), Ω, Θ)
- Logarithms and exponents (also: log, lg, log base 2, binary logarithm, ceiling of log)
- Floor and ceiling (also: floor function, ceiling function, ⌊x⌋, ⌈x⌉, integer part)
- Binary representation of integers (also: base-2 representation, binary numeral, most significant bit, least significant bit, bin_k, bit string value, radix-q digits, positional notation)
- Schoolbook integer arithmetic with carries (also: grade-school multiplication, long multiplication, carry propagation, ripple-carry addition, binary addition)
- Two's complement and signed integers (also: signed binary integers, sign bit, negative numbers in binary)
- XOR and arithmetic modulo 2 (also: exclusive or, bitwise XOR, addition mod 2, parity, F_2 arithmetic, GF(2))
- Modular arithmetic (also: congruence modulo n, residues, mod, Z/nZ, integers modulo q^b, modular inverse, residue ring)
- Prime numbers and gcd (also: primes, greatest common divisor, coprime, relatively prime, prime to q)
- Euclidean algorithm (also: extended Euclidean algorithm, Bezout coefficients, computing modular inverses)
- Chinese remainder theorem (also: CRT, Chinese remaindering)
- Binomial coefficients and subsets (also: n choose k, binom, k-element subsets, combinations, set intersection, Cartesian product)
- Permutations (also: bijection, reordering, permutation of indices, inverse permutation, address permutation)
- Lexicographic order (also: dictionary order, row-major order, mixed-radix ordering)
- Vectors and matrices (also: matrix multiplication, matrix-vector product, identity matrix, diagonal matrix, transpose, row-major matrix, permutation matrix, triangular matrix)
- Linear maps and invertibility (also: linear transformation, linear operator, inverse matrix, invertible matrix, composition of linear maps, linear combination)
- Vector spaces, subspaces and dimension (also: subspace, span, basis, dimension, linear independence, nested subspaces)
- Rank of a matrix (also: matrix rank, column rank, row rank, full rank)
- Dot product and orthogonality (also: inner product, orthogonal vectors, orthonormal vectors, orthogonal complement, perpendicular)
- Gaussian elimination (also: row reduction, LU decomposition, elimination)
- Fields and rings (also: field, ring, rational numbers Q, integers Z, finite field, F_2)
- Fast Fourier transform (also: FFT, Cooley–Tukey FFT, radix-two FFT, inverse FFT)
- Polynomial multiplication via evaluation and interpolation (also: FFT-based polynomial multiplication, convolution theorem, coefficient vs point-value representation, multiplying polynomials with the FFT)
- Bit-reversal permutation (also: bit-reversed order, bit reversal)
- Karatsuba multiplication (also: Karatsuba algorithm, Karatsuba–Ofman)
- Divide-and-conquer recurrences (also: recurrence relation, master theorem, recursion tree, T(n)=aT(n/b)+f(n))
- Mathematical induction (also: proof by induction, induction on n, strong induction)
- Geometric series (also: geometric sum, sum of a geometric progression)
- Limits (also: limit, limit inferior, liminf, tends to infinity, asymptotically)
- Exponential function and Gaussians (also: exp, e^x, Gaussian function, e^{-x²}, Euler's formula, complex exponential)
- Absolute value and the triangle inequality (also: modulus of a complex number, |z|, triangle inequality, error bound)
- Rounding to the nearest integer (also: rounding, round-off, truncation error)
- Newton's method (also: Newton iteration, Newton–Raphson)
- Integer division and square root (also: quotient and remainder, division with remainder, floor of square root)
- Deterministic algorithm and worst-case running time (also: worst-case time, time complexity, deterministic, bit complexity, running time T(n))
- Stacks (also: push and pop, LIFO)
- Binary counter (also: counter increment, amortized counter, ripple counter)
- Hamming weight (also: popcount, number of ones, wt, bit count)
- Matrix transposition (also: transpose a matrix, transposition)
- Turing machine alphabet and simulation constants (also: tape alphabet, tracks, constant-factor simulation, finite control)

## This page

Concept: Integer multiplication below n log n
Gloss: A single deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2⁻¹⁸², disproving the n log n optimality conjecture in this model.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input bit length): The number of bits in each of the two input integers.
- $\lg$ (binary logarithm): The function lg n = max{⌈log₂ n⌉, 1}.
- $\kappa$ (saving exponent): The fixed constant 2⁻¹⁸² by which the exponent of the logarithmic factor drops below one.
- $O$ (big-O): Asymptotic upper bound up to a constant factor.

## This page in the argument

The step: A single deterministic fixed-alphabet multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: speed up address movement and butterfly arithmetic by recursive linear-network procedures, plug them into Harvey and van der Hoeven's reduction of multiplication to synthetic polynomial transforms, and bound the total cost
Why: Scanning Θ(n) bits at each of Θ(log n) transform levels already costs Θ(n log n), so beating n log n requires power savings in both data movement and arithmetic. (the sources say so: "Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$. We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The bound beats $n\log n$ by a power $(\lg n)^{\kappa}$ of the logarithm, refuting the conjectured optimality, though $\kappa=2^{-182}$ is minute. (explain why it holds, from the method)

Its sub-steps, in order:

- Address-field interchange costs $O(Vu^\tau)$ and a simultaneous butterfly layer costs $O(Vd^{\lambda'})$, with fixed $\tau,\lambda'<1$, where $V$ is the stored bit volume.
- Cyclic convolution on distinct prime axes is computed from synthetic transforms over $\mathbb C[y]/(y^r+1)$, Gaussian resampling with retained permutations, and Bluestein chirps.
- The machine computes the exact $2n$-bit product of $n$-bit inputs in $O(n(\lg n)^{1-\kappa})$ time.

## Steps this page derives

The argument gives this page these sub-steps of its step (A, B, C). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**A**: Address-field interchange costs $O(Vu^\tau)$ and a simultaneous butterfly layer costs $O(Vd^{\lambda'})$, with fixed $\tau,\lambda'<1$, where $V$ is the stored bit volume.
How: turn a strict rank deficit of two finite linear networks into recursive power savings for both tape procedures

**B**: Cyclic convolution on distinct prime axes is computed from synthetic transforms over $\mathbb C[y]/(y^r+1)$, Gaussian resampling with retained permutations, and Bluestein chirps.
How: evaluate the needed transforms as synthetic polynomial transforms on a layout where the fast layers apply, and connect them to the prime-length transforms by resampling and chirps
- S10: The retained source permutation $R$ cancels: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$.
  Source: "The second identity shows how the retained source permutation $R$ cancels when computing a convolution." (paper)
  > The factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor} can be computed from a cyclic convolution and two pointwise phase multiplications. The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array. The second identity shows how the retained source permutation $R$ cancels when computing a convolution. Here $*$ denotes cyclic convolution on the product of the coordinate groups and a dot denotes coordinatewise multiplication.

**C**: The machine computes the exact $2n$-bit product of $n$-bit inputs in $O(n(\lg n)^{1-\kappa})$ time.
How: place the radix-digit coefficients on prime axes, reduce to ring convolution by a twist, run the transforms, recover exact coefficients, and sum the normalized cost table under fixed parameters

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Arrays on tape and logical volume](tape-array-layout.md)): Arrays of logical volume $V$ stored in lexicographic order admit a toolkit of $O(V)$-time tape operations: digit permutations and moves, splits and merges, cyclic row distribution among $W$ streams, and controlled shifts of a later field.
- S2 (on [Rank deficit s < Wm](rank-deficit.md)): There are two fixed linear networks, one over $\mathbb F_2$ and one over $\mathbb Z[i,1/2]$, each with $W$ wires, that exchange two banks of values, restore all scratch values, and admit nested subspace labels whose edge changes need only $s<Wm$ smaller calls in total.
- S3 (on [Recursive power saving](recursive-saving.md)): Since $s/W<m^\tau$ with $\tau=1-2^{-50}$, a call at parameter $mf$ done by $s$ calls at parameter $f$ on volume $V/W$ gives normalized cost $O(f^\tau)$.
- S4 (on [Fast address-chunk interchange](fast-address-interchange.md)): Two disjoint contiguous $u$-bit address fields of an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time.
- S5 (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)): Applying $H_0$ at one common bit position in each of $D\le d$ equal-width address chunks of polynomial records costs $O(Vd^{\lambda'})$ with $\lambda'<1$, with exact dyadic intermediates and one final truncation.
- S6 (on [Fast synthetic transform layout](transform-layout.md)): Synthetic transforms over $\mathbb C[y]/(y^r+1)$ on $d-1$ power-of-two axes, with outputs kept in a stored frequency order, cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ with error below $\sqrt2\ell\,2^{-p}$.
- S7 (on [Normalized convolution over the polynomial ring](synthetic-convolution.md)): The normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\mathbb C[y]/(y^r+1)$ is computed with error below $\sqrt2M(3\ell+1)2^{-p}$, adding only $O(Tp\log(rp))$ to the transform cost.
- S8 (on [Gaussian resampling with retained permutations](gaussian-resampling.md)): The tensor of prime-length source transforms satisfies $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with power-of-two lengths $t_i$, contractions $\mathcal A,\mathcal B_0$, and the permutations $R,Q$ kept in the formula.
- S9 (on [Bluestein chirp identity](bluestein-chirp.md)): The middle factor $QF_{\boldsymbol t}u$ equals $\overline a\cdot(a*(\overline a\cdot u))/T$ for a chirp $a$, so it is a normalized cyclic convolution between two phase multiplications.
- S11 (on [Chinese-remainder address map](crt-address-map.md)): A Chinese-remainder map $x\mapsto\prod_ix_i^{\mu_i}$ preserves cyclic convolution and is implemented by triangular controlled shifts and axis moves.
- S12 (on [Coefficient twist](coefficient-twist.md)): The twist $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ turns cyclic convolution in the last coordinate into negacyclic arithmetic in $\mathbb C[y]/(y^r+1)$.
- S13 (on [Radix-digit reduction to convolution](radix-digit-convolution.md)): Splitting each input into radix-$2^b$ digits turns the product into a convolution of short coefficient lists, scaled into the disk and padded to $S$ records.
- S14 (on [Exact coefficient recovery and carries](exact-recovery.md)): After removing the scales $S$ and $2^{2b+4}S$, the coefficient error is below $1/2$, so rounding gives the exact integers, and carry propagation yields the $2n$-bit product.
- S15 (on [Fixed rational parameters and cost table](parameter-choice.md)): With $\tau=\sigma=1-2^{-50}$, $\lambda'=1-2^{-54}$, $\epsilon=2^{-75}$, every normalized cost in the table is at most $p^{1-2\kappa}$, so the total time is $O(n(\lg n)^{1-\kappa})$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Cyclic convolution](cyclic-convolution.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [n log n optimality conjecture](nlogn-conjecture.md): Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
  Shown as: Integer multiplication below n log n *<predicate>* n log n optimality conjecture
- [Radix-digit reduction to convolution](radix-digit-convolution.md): Splitting each n-bit input into radix-2^b digits turns integer multiplication into convolution of short integer coefficient lists followed by carry propagation.
  Shown as: Integer multiplication below n log n *<predicate>* Radix-digit reduction to convolution
- [Chinese-remainder address map](crt-address-map.md): A convolution-preserving map placing the radix-digit coefficient list on a product of distinct prime-length cyclic axes, implemented by triangular controlled shifts and axis moves.
  Shown as: Integer multiplication below n log n *<predicate>* Chinese-remainder address map
- [Gaussian resampling with retained permutations](gaussian-resampling.md): Harvey–van der Hoeven's identity expressing a Fourier transform of prime length s through one of power-of-two length t (P_sF_s = 2^{2α²} B₀ P_t F_t A), here with both coordinate permutations kept in the formula instead of sorted.
  Shown as: Integer multiplication below n log n *<predicate>* Gaussian resampling with retained permutations
- [Bluestein chirp identity](bluestein-chirp.md): Rewriting a Fourier transform (with its target permutation) as pointwise multiplication by a chirp, a cyclic convolution with the chirp, and another chirp multiplication.
  Shown as: Integer multiplication below n log n *<predicate>* Bluestein chirp identity
- [Coefficient twist](coefficient-twist.md): The phase twist x ↦ ζy with ζ = e^{πi/r}, mapping ℂ[x]/(x^r−1) isomorphically onto ℂ[y]/(y^r+1), so cyclic convolution in the last coordinate becomes negacyclic polynomial arithmetic.
  Shown as: Integer multiplication below n log n *<predicate>* Coefficient twist
- [Normalized convolution over the polynomial ring](synthetic-convolution.md): Cyclic convolution of arrays with values in ℂ[y]/(y^r+1), computed by two forward synthetic transforms kept in stored frequency order, packed pointwise ring products, and the opposite transform.
  Shown as: Integer multiplication below n log n *<predicate>* Normalized convolution over the polynomial ring
- [Exact coefficient recovery and carries](exact-recovery.md): Removing known normalizations and digit scales, showing the computed coefficient error is below 1/2 so rounding gives exact integers, then propagating carries to obtain the binary product.
  Shown as: Integer multiplication below n log n *<predicate>* Exact coefficient recovery and carries
- [Fixed rational parameters and cost table](parameter-choice.md): The compatible choice τ = σ = 1 − 2⁻⁵⁰, λ′ = 1 − 2⁻⁵⁴, ε = 2⁻⁷⁵, κ = 2⁻¹⁸², etc., under which every term of the normalized cost table is O((lg n)^{1−κ}).
  Shown as: Integer multiplication below n log n *<predicate>* Fixed rational parameters and cost table

## Other pages you may link to

- [Harvey–van der Hoeven O(n log n) multiplier](harvey-hoeven-multiplier.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring.md)
- [Normalized butterfly H₀](normalized-butterfly.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)
- [Linear network with wire roles](linear-network.md)
- [Frames and the common-frame identity](frames.md)
- [Arrays on tape and logical volume](tape-array-layout.md)
- [Elementary stream operations](elementary-streams.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Restoration of arbitrary scratch values](scratch-restoration.md)
- [Triple-intersection bank exchange](triple-intersection-construction.md)
- [Nested subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank deficit s < Wm](rank-deficit.md)
- [Recursive power saving](recursive-saving.md)
- [Binary phase frames](phase-frames.md)
- [Lower triangular factorization](triangular-factorization.md)
- [Address shear](address-shear.md)
- [Bit network interface](bit-network-interface.md)
- [Fast address-chunk interchange](fast-address-interchange.md)
- [Fixed-point disk grid and truncation](fixed-point-precision.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Signed Kronecker packing](signed-kronecker-packing.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Multidimensional Fourier transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Fast synthetic transform layout](transform-layout.md)
- [Cyclic convolution](cyclic-convolution.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model." (paper)

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

Write the body to `exegenius/tasks/0040-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0040-write-main-theorem.answer.json`, then run `exegenius submit 0040-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0040-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
