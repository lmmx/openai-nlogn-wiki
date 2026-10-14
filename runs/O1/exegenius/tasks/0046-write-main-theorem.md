# exegenius task 0046-write-main-theorem

Project directory: `/home/user/openai-nlogn-wiki/runs/O1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: algorithms and data structures (asymptotic analysis, recurrences and divide-and-conquer, sorting including stable radix sort, amortized counting, schoolbook and Karatsuba multiplication, and the textbook FFT for polynomial multiplication), theory of computation (Turing machines, tapes, deterministic machines, Boolean circuits, worst-case time and lower bounds), and discrete mathematics (sets, permutations, subsets and counting, induction, graphs, modular arithmetic, gcd, primes and the Chinese remainder theorem). From the supporting mathematics they have first-year calculus (limits, logarithms and exponentials, geometric series, Newton's method), introductory linear algebra (matrices, inverses, transposes, triangular and permutation matrices, eigenvalues, dot products and orthonormal bases) and complex numbers, plus the machine-level number representations of computer organization (binary and radix digits, two's complement, bitwise XOR, carries). They have not studied the research literature on fast integer multiplication, Gaussian resampling, synthetic polynomial transforms, multilinear algebra beyond the basics, bilinear-form theory, analytic number theory, or index coding.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine (also: fixed finite-tape model)
- Linear maps, matrices and rank (also: rank, F2-linear algebra)
- Tensor product
- Nondegenerate bilinear forms and orthogonal complements (also: orthogonal complement, orthonormal basis)
- n log n optimality conjecture
  - $n$ (input bit length): The number of bits in each of the two integers being multiplied.
- Harvey–van der Hoeven multiplier (also: established multiplier)
- Lexicographic array layout and logical volume (also: address field, row, logical volume)
- Elementary stream operations
- Controlled shifts (also: prefix-controlled cyclic shift)
- Scratch restoration (also: transparent computation)
- Three-element-subset intersection construction (also: Frankl–Wilson construction, gather and scatter)
- Bank-exchange linear network (also: finite network, role, bit network, complex network)
- Row splitting into role streams
- Frames and the common-frame identity
- Subspace labels and orthogonal residuals (also: labels, rank budget)
- Rank deficit and recursive power saving
- Lower triangular factorization (also: Bruhat factorization)
- Rational address shear (also: matrix shear)
- Fast address-chunk interchange (also: chunk swap, address interchange)
- Normalized discrete Fourier transform (also: DFT)
- Cyclic convolution
- Multidimensional Fourier transform
- Radix-digit reduction to convolution
- Disk-grid fixed-point arithmetic (also: Gaussian dyadic, truncation Q_p)
- Error accounting through contractions
- Gaussian resampling
- Resampling with retained permutations
- Prime source lengths
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Bluestein chirp identity (also: Bluestein's algorithm)
- Source-permutation cancellation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The formal polynomial variable, whose powers act as roots of unity in the ring.
  - $r$ (record length): The number of complex coefficients in one ring element, a power of two.
- Coefficient phase twist
- Normalized butterfly (also: H_0, two-point butterfly)
- Synthetic polynomial transform (also: Nussbaumer transform, synthetic roots of unity)
- Binary phase frames (also: phase kernel C)
- Packed selected-bit addition (also: deterministic repair)
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Synthetic transform layout and cost
- Signed Kronecker packing (also: Kronecker substitution)
- Normalized convolution over the polynomial ring
- Exact recovery by rounding and carries
- Parameter choice and cost table
- Asymptotic notation beyond big-O (also: Big-Theta, Big-Omega, little-o, Θ, Ω, o(·), eventually, for sufficiently large n)
- Logarithms and exponentials (also: log, lg, log_2, natural logarithm, ln, exp, e)
- Floor and ceiling (also: ⌊x⌋, ⌈x⌉, integer part, rounding down, rounding up)
- Limits and liminf (also: limit, lim, liminf, limit inferior, tends to infinity, → ∞)
- Geometric series (also: geometric sum, geometrically increasing precisions)
- Mathematical induction (also: induction, proof by induction, inductive argument)
- Recurrences and divide-and-conquer analysis (also: recurrence relation, recursion, recursion tree, master theorem, divide and conquer, recursive call)
- Worst-case running time (also: time complexity, worst-case time, T_A(n), bit complexity, running time)
- Lower bounds for computational problems (also: lower bound, optimality, Ω(n log n) lower bound)
- Deterministic algorithm (also: deterministic machine, deterministic Turing machine)
- Binary and radix representation (also: binary representation, base-q digits, radix, positional notation, most significant bit, bit string, n-bit integer)
- Schoolbook addition and multiplication with carries (also: long multiplication, carry propagation, carries, grade-school multiplication, quadratic multiplication)
- Karatsuba multiplication (also: Karatsuba algorithm, Karatsuba–Ofman, O(n^{log_2 3}) multiplication)
- Fast Fourier transform (also: FFT, Cooley–Tukey FFT, radix-2 FFT, FFT polynomial multiplication)
- Two's complement and signed integer representation (also: two's complement, sign-extended two's complement, sign and magnitude, signed integers)
- Fixed-point binary fractions (also: fixed-point arithmetic, dyadic rationals, binary fractions, precision p, truncation)
- Bitwise XOR (also: XOR, exclusive or, addition mod 2, ⊕)
- Modular arithmetic (also: congruence, mod, ≡ (mod q), residues, residue ring, Z/qZ, unit modulo q, modular inverse)
- Greatest common divisor and coprimality (also: gcd, coprime, relatively prime, pairwise coprime, prime to q, Euclidean algorithm)
- Prime numbers (also: primes, odd prime, trial division, primality test)
- Chinese remainder theorem (also: CRT, Chinese remainder, Chinese-remainder theorem)
- Integer division and integer square root (also: quotient and remainder, Euclidean division, floor division, ⌊a/b⌋, ⌊√a⌋, integer square root)
- Newton's method (also: Newton iteration, Newton–Raphson)
- Sets, Cartesian products and cardinality (also: Cartesian product, product set, intersection, |S ∩ T|, cardinality, ×)
- Subsets and binomial coefficients (also: k-subsets, three-element subsets, triples, binomial coefficient, n choose k)
- Indicator vector (also: characteristic vector, 0/1 vector of a subset, indicator function)
- Permutations (also: permutation, bijection, inverse permutation, composition of permutations, address permutation, reordering)
- Lexicographic order (also: lexicographic order, dictionary order, row-major order, most significant coordinate first)
- Sorting and stable radix sort (also: sorting, stable sort, radix sort, merge, merging sorted streams)
- Binary counters and amortized analysis (also: binary counter, increment, amortized cost, countdown)
- Stack (also: stack, push and pop, LIFO, depth-first scheduling)
- Directed graphs and acyclic networks (also: directed graph, DAG, directed acyclic graph, vertex, edge, source, sink, path)
- Boolean and arithmetic circuits (also: circuit, logical network, circuit size, gates, wires)
- Matrix inverse, transpose and identity (also: inverse matrix, invertible matrix, transpose, x^T, identity matrix, I, matrix transposition)
- Special matrices (also: diagonal matrix, diag, triangular matrix, lower triangular, upper triangular, permutation matrix, all-ones matrix, J)
- Eigenvalues (also: eigenvalue, eigenvector, spectrum)
- Sup norm and the triangle inequality (also: maximum norm, infinity norm, ‖·‖_∞, coefficient sup norm, absolute error, triangle inequality)
- Number systems and their notation (also: Z, Q, R, C, integers, rationals, reals, ℤ, ℚ, ℂ)
- Fields and rings (also: field, ring, finite field, commutative ring, unit of a ring)
- Gaussian function (also: Gaussian, e^{-x^2}, bell curve)

## This page

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: One deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^(−182), refuting the n log n optimality conjecture in that model.
Also called: Theorem 1
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input bit length): The number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent): The fixed exponent 2^{-182} by which the logarithmic factor is reduced.

## This page in the argument

The step: One deterministic fixed-alphabet multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.
How: reduce the product to a cyclic convolution of radix digits, move it by a Chinese-remainder map and Gaussian resampling to power-of-two axes, compute that convolution with synthetic polynomial transforms accelerated by two network-based tape procedures, recover the exact coefficients by rounding, and bound every cost term
Why: The Harvey and van der Hoeven route already reaches $O(n\log n)$; its remaining cost is a full scan per transform level for both address rearrangement and butterflies, so a power saving in those two tape operations lowers the whole bound. (the sources say so: "The algorithm
uses linear combinations of intermediate data to reduce the cost of
both address rearrangement and Fourier-transform layers." (paper))
Striking feature: The saving is a strict power of the logarithm, $(\lg n)^{-\kappa}$, but with a minute exponent $\kappa=2^{-182}$, enough to refute the $n\log n$ conjecture in this model. (explain why it holds, from the method)

Its sub-steps, in order:

- Two tape procedures save a power of their parameter: chunk interchange in $O(Vu^\tau)$ and a simultaneous butterfly layer in $O(Vd^{\lambda'})$, with $\tau,\lambda'<1$.
- Normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\mathbb C[y]/(y^r+1)$ on $d-1$ power-of-two axes has error below $\sqrt2M(3\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$. (on [Normalized convolution over the polynomial ring](ring-convolution.md))
- With $R=\bigotimes_iP_{s_i}$ and $Q=\bigotimes_iP_{t_i}$, $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ for contractions $\mathcal A,\mathcal B_0$ computable linewise with error below $dp^2$, the permutations never being executed as sorts. (on [Resampling with retained permutations](resampling-retained-permutations.md))
- With chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$, $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}{T}$, so the middle transform with its target permutation is a normalized cyclic convolution. (on [Bluestein chirp identity](chirp-identity.md))
- The retained source permutation cancels: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$. (on [Source-permutation cancellation](permutation-cancellation.md))
- Distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist, give $T/2<S<T$, and satisfy the resampling separation $\alpha^4\theta_i>p$. (on [Prime source lengths](prime-lengths.md))
- Splitting the inputs into $q=\lceil n/b\rceil$ digits base $2^b$ gives a product of degree below $S$, so convolution modulo $x^S-1$ has no wraparound and coefficients are below $2^{3b}$. (on [Radix-digit reduction to convolution](radix-digit-reduction.md))
- The map $x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism onto convolution on axes of lengths $s_i$, implemented by triangular controlled shifts and axis moves in $O(Tp\,d^2(1+\ell^\tau))$ time. (on [Chinese-remainder address map](crt-address-map.md))
- Multiplying coefficient $k$ by $\zeta^k$, $\zeta=e^{\pi i/r}$, turns cyclic convolution in the last axis into multiplication modulo $y^r+1$, so $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$. (on [Coefficient phase twist](coefficient-twist.md))
- Through the source transforms, pointwise product and opposite transform, the final coefficient error is below $448b\,2^{-3b/4}<1/2$, so rounding and radix carry propagation give the exact product. (on [Exact recovery by rounding and carries](exact-recovery.md))
- With $\tau=1-2^{-50}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$, every row of the normalized cost table is at most $p^{1-2\kappa}$, since the smallest margin is $2^{-181}=2\kappa$. (on [Parameter choice and cost table](parameter-choice.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S1). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1**: Two tape procedures save a power of their parameter: chunk interchange in $O(Vu^\tau)$ and a simultaneous butterfly layer in $O(Vd^{\lambda'})$, with $\tau,\lambda'<1$.
How: derive both from fixed linear networks with a rank deficit, transferred to arrays by frames on role streams and applied recursively
- S1.1: Fixed digit permutations and moves, digit splits and merges, cyclic row splits, and controlled shifts $y\mapsto y+a(\text{controls}) \pmod Q$ of a later field each cost $O(V)$ on fixed tapes.
  How: establish each primitive by a constant number of split-and-merge scans with counters

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2 (on [Normalized convolution over the polynomial ring](ring-convolution.md)): Normalized cyclic convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\mathbb C[y]/(y^r+1)$ on $d-1$ power-of-two axes has error below $\sqrt2M(3\ell+1)2^{-p}$ and cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.
- S3 (on [Resampling with retained permutations](resampling-retained-permutations.md)): With $R=\bigotimes_iP_{s_i}$ and $Q=\bigotimes_iP_{t_i}$, $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ for contractions $\mathcal A,\mathcal B_0$ computable linewise with error below $dp^2$, the permutations never being executed as sorts.
- S4 (on [Bluestein chirp identity](chirp-identity.md)): With chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$, $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}{T}$, so the middle transform with its target permutation is a normalized cyclic convolution.
- S5 (on [Source-permutation cancellation](permutation-cancellation.md)): The retained source permutation cancels: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$.
- S6 (on [Prime source lengths](prime-lengths.md)): Distinct odd primes $s_i$ with $(1-2\eta)t_i<s_i\le(1-\eta)t_i$ exist, give $T/2<S<T$, and satisfy the resampling separation $\alpha^4\theta_i>p$.
- S7 (on [Radix-digit reduction to convolution](radix-digit-reduction.md)): Splitting the inputs into $q=\lceil n/b\rceil$ digits base $2^b$ gives a product of degree below $S$, so convolution modulo $x^S-1$ has no wraparound and coefficients are below $2^{3b}$.
- S8 (on [Chinese-remainder address map](crt-address-map.md)): The map $x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism onto convolution on axes of lengths $s_i$, implemented by triangular controlled shifts and axis moves in $O(Tp\,d^2(1+\ell^\tau))$ time.
- S9 (on [Coefficient phase twist](coefficient-twist.md)): Multiplying coefficient $k$ by $\zeta^k$, $\zeta=e^{\pi i/r}$, turns cyclic convolution in the last axis into multiplication modulo $y^r+1$, so $\mathcal M_{\mathbb C}(f,g)=D_-\iota^{-1}\mathcal M_r(\iota D_+f,\iota D_+g)=(f*g)/T$.
- S10 (on [Exact recovery by rounding and carries](exact-recovery.md)): Through the source transforms, pointwise product and opposite transform, the final coefficient error is below $448b\,2^{-3b/4}<1/2$, so rounding and radix carry propagation give the exact product.
- S11 (on [Parameter choice and cost table](parameter-choice.md)): With $\tau=1-2^{-50}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\epsilon=2^{-75}$, every row of the normalized cost table is at most $p^{1-2\kappa}$, since the smallest margin is $2^{-181}=2\kappa$.
- S1.1.1 (on [Elementary stream operations](elementary-stream-ops.md)): Permuting or moving fixed radix digits, splitting on a digit and merging, and splitting rows cyclically into $W$ streams each take $O(V)$ steps.
- S1.1.2 (on [Controlled shifts](controlled-shifts.md)): Adding to a target field an offset computed from earlier control fields, or multiplying it by a fixed rational unit, costs $O(V)$.
- S1.2 (on [Rank deficit and recursive power saving](rank-deficit.md)): There are two fixed linear networks with $W$ wires that exchange two banks while restoring all scratch wires, whose edge changes need in total $s<Wm$ smaller calls, so that $s/W<m^\tau$ with $\tau=1-2^{-50}$.
- S1.3 (on [Fast address-chunk interchange](chunk-interchange.md)): Two disjoint $u$-bit address chunks of an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$.
- S1.4 (on [Simultaneous butterfly layer](simultaneous-layer.md)): Applying $H_0$ on one selected bit in each of $D\le d$ address chunks of a polynomial-record array costs $O(Vd^{\lambda'})$ with $\lambda'<1$, with error below $\sqrt2\,2^{-p}$.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [n log n optimality conjecture](nlogn-conjecture.md): Schönhage and Strassen's conjecture that n log n is the optimal order of growth for multiplying n-bit integers, here in the multitape Turing machine model.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* n log n optimality conjecture
- [Radix-digit reduction to convolution](radix-digit-reduction.md): Splitting each n-bit input into b-bit digits turns integer multiplication into convolution of short nonnegative integer coefficient lists, followed by carry propagation.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Radix-digit reduction to convolution
- [Chinese-remainder address map](crt-address-map.md): An algebra isomorphism from one cyclic convolution of length S = ∏ s_i to a multidimensional cyclic convolution on pairwise coprime axes, implemented by triangular controlled shifts and axis moves.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Chinese-remainder address map
- [Prime source lengths](prime-lengths.md): Distinct odd primes s_i chosen just below the power-of-two axis lengths t_i, so their product fills a fixed fraction of the padded box while leaving the separation resampling needs.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Prime source lengths
- [Resampling with retained permutations](resampling-retained-permutations.md): A variant of Gaussian resampling that keeps the source and target coordinate permutations inside the transform identity instead of executing them as sorts.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Resampling with retained permutations
- [Bluestein chirp identity](chirp-identity.md): Multiplying by quadratic phases (chirps) before and after a cyclic convolution computes a Fourier transform, here including its target permutation.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Bluestein chirp identity
- [Source-permutation cancellation](permutation-cancellation.md): The source permutation retained in both forward transforms cancels against the opposite-sign transform when computing a convolution.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Source-permutation cancellation
- [Coefficient phase twist](coefficient-twist.md): Multiplying coefficient k by e^{πik/r} turns cyclic convolution in the last axis into negacyclic multiplication modulo y^r + 1.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Coefficient phase twist
- [Normalized convolution over the polynomial ring](ring-convolution.md): Computing normalized cyclic convolution of arrays of ring elements by two forward synthetic transforms, pointwise packed products in the retained order, and the opposite transform.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Normalized convolution over the polynomial ring
- [Exact recovery by rounding and carries](exact-recovery.md): Once the approximate coefficient error is below 1/2, rounding gives the exact integer coefficients, and radix carry propagation gives the binary product.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Exact recovery by rounding and carries
- [Parameter choice and cost table](parameter-choice.md): Fixed rational exponents (τ, λ′, ε, c, δ, …) and size parameters chosen so every row of the normalized cost table is at most p^{1−2κ}.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Parameter choice and cost table
- [Fast address-chunk interchange](chunk-interchange.md): A tape procedure that interchanges two disjoint u-bit address fields of an array in O(V u^τ) time for a fixed τ < 1, by running the bit network with shear frames and recursing on smaller interchanges.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Fast address-chunk interchange
- [Simultaneous butterfly layer](simultaneous-layer.md): Applying the butterfly H₀ on one selected bit in each of up to d address chunks at once in O(V d^λ′) time, λ′ < 1, by running the complex network with phase frames recursively and truncating once at the end.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Simultaneous butterfly layer

## Other pages you may link to

- [Harvey–van der Hoeven multiplier](hvdh-multiplier.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring.md)
- [Disk-grid fixed-point arithmetic](disk-grid.md)
- [Signed Kronecker packing](signed-packing.md)
- [Lexicographic array layout and logical volume](array-layout.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Controlled shifts](controlled-shifts.md)
- [Linear maps, matrices and rank](linear-algebra.md)
- [Scratch restoration](scratch-restoration.md)
- [Nondegenerate bilinear forms and orthogonal complements](bilinear-form.md)
- [Three-element-subset intersection construction](triple-intersection.md)
- [Bank-exchange linear network](bank-exchange-network.md)
- [Row splitting into role streams](role-streams.md)
- [Frames and the common-frame identity](frames.md)
- [Tensor product](tensor-product.md)
- [Subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank deficit and recursive power saving](rank-deficit.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Rational address shear](address-shear.md)
- [Packed selected-bit addition](packed-selected-bit.md)
- [Normalized discrete Fourier transform](dft.md)
- [Multidimensional Fourier transform](multidim-dft.md)
- [Normalized butterfly](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Binary phase frames](phase-frames.md)
- [Error accounting through contractions](contraction-error.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic transform layout and cost](synthetic-layout.md)
- [Cyclic convolution](cyclic-convolution.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "for every input length and disproves the $n\log n$ optimality conjecture" (paper)

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

Write the body to `exegenius/tasks/0046-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0046-write-main-theorem.answer.json`, then run `exegenius submit 0046-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0046-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
