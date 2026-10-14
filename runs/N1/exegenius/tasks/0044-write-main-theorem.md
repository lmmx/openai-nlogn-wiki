# exegenius task 0044-write-main-theorem

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N1` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science background: asymptotic analysis of algorithms and solving simple cost recurrences, basic Turing machines and multitape simulation, binary representation of integers and machine arithmetic (carries, two's complement, XOR, fixed-point rounding), and the discrete mathematics taught to everyone (induction, modular arithmetic, gcd, primes, the Chinese remainder theorem, permutations, binomial coefficients, lexicographic order). From the required mathematics they have a first course in linear algebra (vectors, matrices, rank, invertibility, triangular and diagonal matrices, linear maps over Q and C) and basic complex numbers and polynomials. They have not studied tensor products of operators, bilinear forms, Hadamard or Bruhat-type factorizations, FFT variants beyond a textbook mention, or research-level integer multiplication algorithms.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
  - $n$ (input bit length): The number of bits in each of the two integers being multiplied.
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
  - $n$ (input bit length): The number of bits in each input of the subroutine multiplication.
  - $O$ (big-O bound): Asymptotic upper bound up to a constant factor.
- Cyclic convolution
- Radix-digit convolution (also: Kronecker splitting into digits)
- Normalized discrete Fourier transform (also: Fourier transform, DFT)
- Array streams and logical volume (also: logical volume, address field, row)
- Elementary stream operations
- Controlled shifts (also: prefix-controlled cyclic shift)
- Chinese-remainder address map (also: CRT map, prime source lengths)
- Gaussian resampling
- Resampling with retained permutations (also: no-sort resampling, permutation cancellation)
- Tensor resampling interface
- Bluestein's chirp identity (also: chirp transform)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring indeterminate): The polynomial variable whose powers act as synthetic roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Coefficient phase twist (also: coefficient twist)
- Normalized butterfly H₀ (also: H0)
  - $H_0$ (normalized butterfly): The two-point linear map sending (u, v) to ((u+v)/2, (u−v)/2).
- Gaussian dyadics and fixed-point truncation (also: disk grid, Q_p truncation, guard bits)
- Synthetic polynomial transform (also: Nussbaumer transform, synthetic transform)
- Linear bank-exchange network (also: finite network, role, wire)
- Restoration of arbitrary scratch values (also: transparent computation)
- Three-element-subset gather and scatter (also: index-code decoding, Frankl–Wilson construction)
- Frames and the common-frame identity (also: frame)
- Nested subspace labels (also: orthogonal residual, labels)
- Rank deficit of the network (also: s < Wm)
- Address shear (also: shear)
- Rational matrix interface (also: bit network)
- Lower triangular factorization (also: Bruhat factorization)
- Cost of a rational matrix shear
- Row splitting among roles
- Volume-normalized recurrence (also: recursive saving)
- Fast address chunk interchange (also: chunk swap, address interchange)
- Binary phase frames (also: kernel C, phase kernel)
- Binary phase interface (also: complex network)
- Packed selected-bit addition (also: binary change of basis, deterministic repair)
- Simultaneous butterfly layer (also: fast butterfly layer, parallel butterfly)
- Transform layout
- Signed coefficient packing (also: Kronecker substitution)
- Convolution from the retained transform layout
- Exact recovery by rounding and carries
- Parameter choice and cost table
- Binary representation of integers (also: n-bit integer, base-2 expansion, binary digits, bits)
- Carry propagation (also: carries, ripple carry, radix carries, positional addition)
- Two's complement (also: sign-extended two's complement, signed binary integers, sign extension)
- Exclusive or (also: XOR, addition modulo 2, bitwise XOR)
- Schoolbook multiplication (also: long multiplication, grade-school multiplication, quadratic multiplication)
- Floor and ceiling (also: floor function, ceiling function, integer part, ⌊x⌋, ⌈x⌉)
- Rounding to the nearest integer (also: rounding, truncation toward zero, round-off error)
- Fixed-point numbers (also: fixed-point arithmetic, binary fractions, dyadic fractions in a word)
- Binary logarithm (also: lg, log base 2, logarithm, log n)
- Modular arithmetic (also: congruence modulo m, residues, mod, a ≡ b (mod m), centered residue)
- Greatest common divisor (also: gcd, coprime, relatively prime)
- Prime numbers (also: primes, prime factorization)
- Chinese remainder theorem (also: CRT, Chinese remaindering)
- Mathematical induction (also: induction, proof by induction, inductive argument)
- Recurrence relations for running time (also: recurrence, divide-and-conquer recurrence, unrolling a recurrence)
- Geometric series (also: geometric sum, sum of a geometric progression)
- Permutations (also: permutation, bijection of a finite set, reordering, inverse permutation)
- Binomial coefficients (also: n choose k, binom, k-element subsets)
- Lexicographic order (also: lex order, dictionary order, row-major order)
- Vectors and matrices (also: matrix, vector, matrix multiplication, identity matrix, transpose)
- Vector spaces, subspaces and dimension (also: linear subspace, basis, dimension, span, linear map)
- Matrix rank (also: rank, column rank, full rank)
- Invertible matrices (also: nonsingular matrix, inverse matrix, determinant nonzero)
- Triangular and diagonal matrices (also: lower triangular matrix, upper triangular, diagonal matrix, diag, unit triangular)
- Permutation matrices (also: permutation matrix, partial permutation matrix)
- Gaussian elimination (also: row reduction, elimination, LU decomposition)
- Rational numbers (also: Q, fractions, rational matrix)
- Maximum norm (also: infinity norm, sup norm, ‖·‖∞, max absolute entry)
- Triangle inequality (also: |a + b| ≤ |a| + |b|)
- Exponential function and Euler's formula (also: e^{iθ}, Euler's formula, Gaussian function e^{-x^2})

## This page

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: One deterministic fixed-alphabet multitape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{-182}, refuting the n log n lower-bound conjecture in this model.
Also called: Theorem 1
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input bit length): The number of bits in each of the two input integers.
- $\lg$ (ceiling binary logarithm): The function lg n = max{⌈log₂ n⌉, 1}.
- $\kappa$ (saving exponent): The fixed constant 2^{-182} by which the logarithmic exponent drops below one.
- $O$ (big-O bound): Asymptotic upper bound up to a constant factor on worst-case running time.

## This page in the argument

The step: One deterministic fixed-alphabet multitape Turing machine computes the exact $2n$-bit product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.
How: build two tape procedures that beat a scan per level (fast chunk interchange and simultaneous butterfly layers) from finite linear networks with a rank deficit, place them in the Gaussian-resampling and synthetic-transform reduction of multiplication to convolution, recover the product exactly, and total the costs
Why: Scanning $\Theta(n)$ bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$, so both data movement and butterfly arithmetic must be done in less than a scan per level. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))
Striking feature: a fixed power saving $(\lg n)^{-\kappa}$ below $n\log n$, uniformly through all input lengths, refuting the conjectured $n\log n$ lower bound (explain why it holds, from the method)

Its sub-steps, in order:

- Two disjoint equal-width address chunks of $u$ bits in an array of logical volume $V$ can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time with $\tau=1-2^{-50}$. (on [Fast address chunk interchange](chunk-interchange.md))
- On arrays $[P]\times[2^K]^D\times[S]$ of polynomial records with $D\le d$, the tensor product of $H_0$ on one selected bit in each of the $D$ chunks, followed by one truncation $Q_p$, costs $O(Vd^{\lambda'})$ with $\lambda'<1$ and error below $\sqrt2\,2^{-p}$. (on [Simultaneous butterfly layer](simultaneous-layer.md))
- Normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\mathbb C[y]/(y^r+1)$ on $d-1$ power-of-two axes is computed with error below $\sqrt2M(3\ell+1)2^{-p}$ at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$. (on [Convolution from the retained transform layout](synthetic-convolution.md))
- The source transform $RF_{\boldsymbol s}$ on distinct prime axis lengths $s_i$ equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with power-of-two lengths $t_i$, its middle factor is a normalized cyclic convolution between chirps, and the retained permutation $R$ cancels in a convolution.
- The algorithm forms radix-$2^b$ digit arrays, places them on prime axes by $\Phi$, computes $(u*v)/S^2$ through two source transforms, a pointwise product and an opposite transform, and recovers the exact $2n$-bit product by rescaling, rounding and carries.
- With $\tau=1-2^{-50}$, $\epsilon=2^{-75}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $\delta=1/16$, every row of the cost table divided by $Tp$ is at most $p^{1-2\kappa}$, so the total time is $O(n(\lg n)^{1-\kappa})$. (on [Parameter choice and cost table](cost-table.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4, S5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4**: The source transform $RF_{\boldsymbol s}$ on distinct prime axis lengths $s_i$ equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with power-of-two lengths $t_i$, its middle factor is a normalized cyclic convolution between chirps, and the retained permutation $R$ cancels in a convolution.
How: keep the coordinate permutations inside the Gaussian resampling identity, tensor it over the axes, convert the permuted middle transform by Bluestein's chirp identity, and show the source permutation cancels
- S4.4: The retained permutation cancels: $(RF^+_{\boldsymbol s})[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$.
  Source: "proving \eqref{eq:source-permutation-cancel}. Finally, conjugation" (paper)
  > u\mathbin{\cdot}F_{\boldsymbol s}v)$, because a coordinate permutation commutes with pointwise products. Therefore \[ RF_{\boldsymbol s}^+\bigl[R(F_{\boldsymbol s}u\mathbin{\cdot} F_{\boldsymbol s}v)\bigr] =F_{\boldsymbol s}^+(F_{\boldsymbol s}u\mathbin{\cdot} F_{\boldsymbol s}v). \] The normalized convolution rule is $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\mathbin{\cdot} (F_{\boldsymbol s}v)$, while $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$. The two normalizations give \[ F_{\boldsymbol s}^+ (F_{\boldsymbol s}u\mathbin{\cdot}F_{\boldsymbol s}v) =\frac1S F_{\boldsymbol s}^+F_{\boldsymbol s}(u*v) =\frac{u*v}{S^2}, \] proving \eqref{eq:source-permutation-cancel}. Finally, conjugation changes the negative Fourier sign to the positive one and commutes with the real permutation $R$. It preserves both the disk grid and the norm, so conjugating the input and output also preserves an algorithm's error bound. \end{proof} \section{Exact integer multiplication and its cost} \label{sec:assembly}

**S5**: The algorithm forms radix-$2^b$ digit arrays, places them on prime axes by $\Phi$, computes $(u*v)/S^2$ through two source transforms, a pointwise product and an opposite transform, and recovers the exact $2n$-bit product by rescaling, rounding and carries.
How: reduce the integer product to a digit convolution, map it to a multidimensional cyclic convolution on prime axes, evaluate it with the source transforms whose middle convolution uses the phase twist, then round and propagate carries
- S5.4: After the three transforms the exact counterpart is $(u*v)/S^2$, and the two exact scalings by $S$ and $2^{2b+4}S$ return the integer coefficient convolution.
  Source: "The two occurrences of $S$ in this algorithm undo different" (paper)
  > The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1 (on [Fast address chunk interchange](chunk-interchange.md)): Two disjoint equal-width address chunks of $u$ bits in an array of logical volume $V$ can be interchanged on a fixed number of tapes in $O(Vu^\tau)$ time with $\tau=1-2^{-50}$.
- S2 (on [Simultaneous butterfly layer](simultaneous-layer.md)): On arrays $[P]\times[2^K]^D\times[S]$ of polynomial records with $D\le d$, the tensor product of $H_0$ on one selected bit in each of the $D$ chunks, followed by one truncation $Q_p$, costs $O(Vd^{\lambda'})$ with $\lambda'<1$ and error below $\sqrt2\,2^{-p}$.
- S3 (on [Convolution from the retained transform layout](synthetic-convolution.md)): Normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ of arrays over $\mathbb C[y]/(y^r+1)$ on $d-1$ power-of-two axes is computed with error below $\sqrt2M(3\ell+1)2^{-p}$ at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}+\log(rp)])$.
- S6 (on [Parameter choice and cost table](cost-table.md)): With $\tau=1-2^{-50}$, $\epsilon=2^{-75}$, $c=2^{-56}$, $\lambda'=1-2^{-54}$, $\delta=1/16$, every row of the cost table divided by $Tp$ is at most $p^{1-2\kappa}$, so the total time is $O(n(\lg n)^{1-\kappa})$.
- S4.1 (on [Resampling with retained permutations](retained-permutations.md)): For coprime $s<t$ there are contractions $A,B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, approximable with error below $p^2$ in time $O(tp^{3/2+\delta}\alpha)$, without executing $P_s$ or $P_t$.
- S4.2 (on [Tensor resampling interface](tensor-resampling.md)): Tensoring over $d$ axes gives $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with linewise maps of error below $dp^2$, and exposing all lines by chunk interchanges costs $O(Tpd^2(1+\ell^\tau))$.
- S4.3 (on [Bluestein's chirp identity](bluestein-chirp.md)): The permuted transform satisfies $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$ for the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$.
- S5.1 (on [Radix-digit convolution](radix-digit-convolution.md)): Writing the inputs in radix $2^b$ makes the product a convolution of $q=\lceil n/b\rceil$-digit lists with coefficients below $2^{3b}$ and no wraparound modulo $x^S-1$ since $2q-2<S$.
- S5.2 (on [Chinese-remainder address map](crt-address-map.md)): The map $x\mapsto\prod_i x_i^{\mu_i}$ is an isomorphism turning one cyclic convolution of length $S=\prod_i s_i$ into a multidimensional one, implemented by triangular controlled shifts and axis moves in $O(Tpd^2(1+\ell^\tau))$ time.
- S5.3 (on [Coefficient phase twist](phase-twist.md)): The twist $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ converts cyclic convolution along the last axis into multiplication modulo $y^r+1$, so $\mathcal M_{\mathbb C}(f,g)=(f*g)/T$ is computed by the synthetic convolution.
- S5.5 (on [Exact recovery by rounding and carries](exact-recovery.md)): The final coefficient error is below $448b\,2^{-3b/4}<1/2$, so rounding gives the exact integer coefficients, and radix-$2^b$ carry propagation yields the $2n$-bit product.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Gaussian resampling](gaussian-resampling.md)
- [Normalized discrete Fourier transform](dft.md)
- [Resampling with retained permutations](retained-permutations.md)
- [Cyclic convolution](cyclic-convolution.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The n log n optimality conjecture](nlogn-conjecture.md): Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The n log n optimality conjecture
- [Radix-digit convolution](radix-digit-convolution.md): Writing each input as a polynomial in 2^b, so that the product becomes a convolution of small digit coefficients followed by carry propagation.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Radix-digit convolution
- [Chinese-remainder address map](crt-address-map.md): The isomorphism x ↦ ∏ x_i^{μ_i} that turns one cyclic convolution of length S = ∏ s_i into a multidimensional cyclic convolution on distinct prime axes, implemented by triangular controlled shifts and axis moves.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Chinese-remainder address map
- [Tensor resampling interface](tensor-resampling.md): Applying the one-dimensional resampling maps line by line along each of d axes of a padded power-of-two box, with axis exposure done by chunk interchanges.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Tensor resampling interface
- [Bluestein's chirp identity](bluestein-chirp.md): Writing a Fourier transform, including its frequency permutation, as pointwise multiplication by a chirp, a cyclic convolution with the chirp, and another chirp multiplication.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Bluestein's chirp identity
- [Coefficient phase twist](phase-twist.md): The map x_d ↦ ζy with ζ = e^{πi/r} that converts cyclic convolution along the last axis into negacyclic multiplication modulo y^r + 1.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Coefficient phase twist
- [Convolution from the retained transform layout](synthetic-convolution.md): Normalized convolution over the polynomial ring computed by two forward synthetic transforms, pointwise packed products in the stored order, and the opposite transform consuming that order.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Convolution from the retained transform layout
- [Exact recovery by rounding and carries](exact-recovery.md): Undoing known scales, rounding each approximate coefficient whose error is below 1/2 to the exact integer, and propagating radix-2^b carries to obtain the binary product.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Exact recovery by rounding and carries
- [Parameter choice and cost table](cost-table.md): Fixed rational parameters (τ = 1 − 2^{-50}, ε = 2^{-75}, κ = 2^{-182}, …) under which every term of the cost per bit is at most p^{1−2κ}.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Parameter choice and cost table
- [Established O(n log n) multiplier](hvdh-multiplier.md): Harvey and van der Hoeven's fixed-tape O(n log n) integer multiplication algorithm, used here only as an ordinary subroutine on short records.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Established O(n log n) multiplier

## Other pages you may link to

- [Normalized butterfly H₀](butterfly.md)
- [Gaussian dyadics and fixed-point truncation](gaussian-dyadics.md)
- [Linear bank-exchange network](linear-network.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Array streams and logical volume](stream-array-layout.md)
- [Frames and the common-frame identity](frame-invariant.md)
- [Address shear](address-shear.md)
- [Elementary stream operations](elementary-stream-ops.md)
- [Row splitting among roles](row-splitting.md)
- [Controlled shifts](controlled-shifts.md)
- [Restoration of arbitrary scratch values](scratch-restoration.md)
- [Three-element-subset gather and scatter](triple-gadget.md)
- [Nested subspace labels](subspace-labels.md)
- [Rank deficit of the network](rank-deficit.md)
- [Volume-normalized recurrence](volume-recurrence.md)
- [Rational matrix interface](bit-motif-interface.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Fast address chunk interchange](chunk-interchange.md)
- [Binary phase frames](phase-frames.md)
- [Binary phase interface](complex-motif-interface.md)
- [Packed selected-bit addition](packed-selected-bit.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed coefficient packing](signed-packing.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Normalized discrete Fourier transform](dft.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transform](synthetic-fft.md)
- [Resampling with retained permutations](retained-permutations.md)
- [Transform layout](transform-layout.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "$\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes." (paper)

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

Write the body to `exegenius/tasks/0044-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0044-write-main-theorem.answer.json`, then run `exegenius submit 0044-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0044-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
