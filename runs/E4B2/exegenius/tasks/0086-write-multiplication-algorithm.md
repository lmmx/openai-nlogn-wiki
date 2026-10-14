# exegenius task 0086-write-multiplication-algorithm

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/B2` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer science student: they have taken programming, data structures, an algorithms course (asymptotic analysis, divide and conquer, sorting), discrete mathematics (sets, functions, induction, modular arithmetic, basic number theory) and an introductory linear algebra and complex numbers course, plus an introductory theory-of-computation course covering Turing machines. They have not met the Fourier transform beyond what the wiki explains, nor rings of polynomials modulo a polynomial, analytic number theory (prime density estimates), finite fields beyond bits, or any research-level complexity results on integer multiplication. Everything specific to the paper's fixed-tape constructions, networks, frames and numerical precision must be explained.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Bitwise XOR and arithmetic mod 2
- Exact integer multiplication on a multitape Turing machine
- Schönhage–Strassen n log n optimality conjecture (also: n log n conjecture)
- Established O(n log n) multiplier (Harvey–van der Hoeven)
- Normalized discrete Fourier transform (also: Fourier transform)
- Cyclic convolution and the convolution theorem (also: convolution)
- Integer multiplication as convolution of radix digits
- Two-point butterfly and radix-2 fast Fourier transform (also: butterfly, FFT)
- Matrix rank, subspaces and orthogonal complements
- Tensor products of operators and arrays
- Multidimensional transform on a tensor of axes
- Disk-grid fixed-point arithmetic, contractions and error (also: disk grid, truncation Q_p)
- Array order and elementary stream scans
- Controlled cyclic shifts and fixed rational scalings
- Chinese-remainder address map to distinct prime axes (also: Agarwal–Cooley map, Φ)
- Gaussian resampling with permutations left in the transform (also: Gaussian resampling)
- Bluestein chirp identity (also: chirp identity)
- Source permutation cancellation
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring)
  - $y$ (ring indeterminate): The formal variable of the polynomials, a root of −1 raised to the r-th power, whose powers serve as roots of unity.
  - $r$ (polynomial length): The number of complex coefficients in a stored polynomial, a power of two.
- Coefficient twist from cyclic to negacyclic wrap
- Synthetic polynomial transform (also: Nussbaumer polynomial transform)
- Signed packing of polynomial products (Kronecker substitution)
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames: changing array representation along network edges (also: common-frame identity)
- Nested subspace labels and the total-rank saving (also: rank deficit, orthogonal residual)
- Bit-network rational matrix interface
- Lower triangular factorization of a matrix (also: Bruhat factorization)
- Cost of a rational matrix shear
- Depth-first schedule of recursive calls on fixed tapes
- Recursive power-width chunk interchange
- Fast interchange of address chunks (also: address interchange, chunk swap)
- Two-point phase kernel C
- Binary phase interface of the complex network (also: phase frames)
- Packed selected-bit addition on one rectangle (also: packed change of address bits)
- Exact Gaussian dyadic evaluation with guard bits
- Simultaneous normalized butterfly layer (also: parallel butterfly layer)
- Transform layout on which parallel layers apply
- Convolution over the polynomial ring from the retained transform layout
- Parameter choice: precision, dimension, axis lengths and prime source lengths
- Precision, rounding and carry propagation
- Asymptotic notation Omega, Theta and little-o (also: Ω, Θ, Big-Omega, Big-Theta, tight bound, lower bound notation)
- Logarithms, floors and ceilings (also: log base 2, lg, natural logarithm, floor function, ceiling function, ⌈x⌉, ⌊x⌋)
- Binary representation of integers (also: binary numbers, bit strings, radix representation, most significant bit, least significant bit, base-2 numerals, n-bit integer)
- Schoolbook binary addition with carries (also: carry propagation, ripple carry, grade-school multiplication, long addition, long multiplication)
- Divide and conquer multiplication (Karatsuba, Toom-Cook) (also: Karatsuba algorithm, Toom-Cook, Karatsuba-Ofman, divide-and-conquer, O(n^{log_2 3}))
- Recurrences, induction and geometric sums (also: recurrence relation, proof by induction, geometric series, unrolling a recurrence, master theorem)
- Sets, functions, bijections and permutations (also: Cartesian product, bijection, permutation, involution, function composition, injective, surjective, index set, indicator function)
- Binomial coefficients (also: n choose k, combinations, C(n,k), counting subsets)
- Modular arithmetic and congruences (also: integers mod n, Z/nZ, residues, congruence, a mod q, cyclic group of integers mod n, modular inverse)
- Greatest common divisor and the Euclidean algorithm (also: gcd, coprime, relatively prime, extended Euclidean algorithm, Bezout identity, modular inverse computation)
- Prime numbers (also: primes, prime factorization, primality testing, sieve of Eratosthenes, distinct primes)
- Chinese remainder theorem (also: CRT, Chinese remainder, residues modulo coprime moduli)
- Roots of unity (also: primitive root of unity, nth roots of unity, e^{2πi/n}, unit-modulus roots, twiddle factor)
- Matrices, matrix products and inverses (also: matrix multiplication, identity matrix, invertible matrix, diagonal matrix, permutation matrix, triangular matrix, transpose, linear map, dot product, inner product)
- Gaussian elimination and row operations (also: row reduction, elementary row operations, row addition, row swap, pivot)
- Vectors and matrices over the two-element field (also: F_2, GF(2), binary vectors, linear algebra mod 2, Hamming weight, binary matrices, GL(m, F_2))
- Vector norms and the triangle inequality (also: max norm, sup norm, infinity norm, absolute value bound, error bound, triangle inequality, modulus bound)
- Two's complement and fixed-width signed integers (also: signed binary, twos complement, signed words, dyadic rationals, binary fixed-point)
- Stacks and queues (also: push and pop, LIFO, stack discipline, last-in first-out, queue)
- Sorting and radix sort (also: stable sort, radix sorting, merge sort, sorting by keys, binary radix sort, merging sorted lists)
- Binary counters and finite-state bookkeeping (also: finite residue counter, counting with a counter, finite control counting, ripple counting)

## This page

Concept: The multiplication algorithm: digits to transform, pointwise product and back
Gloss: Convert operands to digit lists on a padded prime-axis box via Φ, apply the source transform (resample, chirp convolution through the twist, resample) to each, multiply pointwise, apply the opposite transform, scale by S and 2^{2b+4}, undo Φ, round and propagate carries.

## This page in the argument

The step: Radix-$2^b$ digit convolution on $S$ distinct prime axes, computed by transform, pointwise product and opposite transform at precision $p$ in a padded box of $T$ entries, gives the exact $2n$-bit product after scaling, rounding and carries.
How: reduce the integer product to a cyclic convolution of radix digits, move it to prime axes by a CRT map, replace each prime-length transform by power-of-two transforms through Gaussian resampling and a chirp, and solve the remaining ring convolution by synthetic transforms
Why: Each reduction turns the problem into one the next tool handles: only the final ring convolution has roots of unity that are cheap shifts, so the intermediate stages exist to bring the digit convolution into that form. (the sources leave this for the reader to work out: spell it out)

Its sub-steps, in order:

- The normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ over $\mathcal R_r$ on $d-1$ power-of-two axes is computed from the retained transform layout with error below $\sqrt2\,M(3\ell+1)2^{-p}$. (on [Convolution over the polynomial ring from the retained transform layout](synthetic-convolution.md))
- One Fourier transform of length $s$ (coprime to $t>s$) equals $2^{2\alpha^2}B_0P_tF_tA$ up to a coordinate permutation $P_s$, with Gaussian contractions $A,B_0$ and both permutations left inside the formula, and the same holds axis by axis. (on [Gaussian resampling with permutations left in the transform](gaussian-resampling.md))
- The permuted transform $QF_{\boldsymbol t}$ equals pointwise multiplication by $\overline a$, a cyclic convolution with the chirp $a$, and another multiplication by $\overline a$. (on [Bluestein chirp identity](bluestein-chirp.md))
- The retained permutation $R$ cancels across two forward transforms, a pointwise product and the opposite transform, giving $(u*v)/S^2$. (on [Source permutation cancellation](permutation-cancellation.md))
- Taking $b=\lceil\log_2 n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, power-of-two axis lengths $t_i\in\{r/2,r\}$ with product $T\approx n/b$ and distinct odd primes $s_i$ just below $t_i$ with $S=\prod s_i$ satisfies every hypothesis of the preceding steps. (on [Parameter choice: precision, dimension, axis lengths and prime source lengths](parameter-choice.md))
- Writing both operands as polynomials in $2^b$, the product coefficients are a convolution of digit lists, each below $2^{3b}$, with no wraparound modulo $x^S-1$. (on [Integer multiplication as convolution of radix digits](multiplication-by-convolution.md))
- The map $\Phi:x\mapsto\prod_i x_i^{\mu_i}$ turns cyclic convolution of length $S$ into $d$-dimensional cyclic convolution on pairwise coprime axes, implemented by triangular controlled shifts. (on [Chinese-remainder address map to distinct prime axes](crt-address-map.md))
- The twist $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ identifies cyclic convolution on the last axis with negacyclic convolution in $\mathcal R_r$. (on [Coefficient twist from cyclic to negacyclic wrap](coefficient-twist.md))
- The source transform is a resampling map, the middle chirp transform computed through the twisted complex convolution, and a resampling map.
- The algorithm applies $\Phi$, transforms both operands, multiplies pointwise, applies the opposite transform, scales by $S$ and $2^{2b+4}$, undoes $\Phi$, rounds and propagates carries.
- The recovered coefficients have error below $1/2$, so rounding gives the exact integer convolution coefficients and carries give the exact $2n$-bit product. (on [Precision, rounding and carry propagation](precision-exact-recovery.md))

It serves these steps, from the main result down:

- One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, using fast address interchange, fast simultaneous butterfly layers, and the resampling, chirp and synthetic-convolution reduction.; how: supply the two fast tape procedures, then insert them into a reduction from the integer product to polynomial-ring convolution, and add up every cost (on [Power-saving integer multiplication theorem](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.9, S3.10). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.9**: The source transform is a resampling map, the middle chirp transform computed through the twisted complex convolution, and a resampling map.
Source: "We next use the complex convolution to evaluate the middle factor" (paper)
> We next use the complex convolution to evaluate the middle factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor}, and then compose it with the Gaussian maps. For the chirp array $a$ in \eqref{eq:permuted-chirp}, the phase numerator at tensor address $j$ is computed modulo $2r$ as \[ -\sum_i s_i j_i^2(r/t_i)\pmod{2r}. \] All integers have $O(p)$ bits and $r/t_i\in\{1,2\}$. Scan the stored axis descriptors and compute the $d$ squares and products with the previously established integer multiplier. Additions, reductions modulo a power of two, and restarting local counters cost $O(p)$ per term; multiplication costs $O(p\log p)=O(p^{1+\delta})$. Exponential evaluation then has the same $O(p^{1+\delta})$ bound. Thus chirp construction costs $O(Td p^{1+\delta})$ in total. In particular, this cost includes the scan of the axis descriptors at every coefficient.

**S3.10**: The algorithm applies $\Phi$, transforms both operands, multiplies pointwise, applies the opposite transform, scales by $S$ and $2^{2b+4}$, undoes $\Phi$, rounds and propagates carries.
Source: "With these streams prepared, perform the following operations." (paper)
> With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the repres

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S3.1 (on [Convolution over the polynomial ring from the retained transform layout](synthetic-convolution.md)): The normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ over $\mathcal R_r$ on $d-1$ power-of-two axes is computed from the retained transform layout with error below $\sqrt2\,M(3\ell+1)2^{-p}$.
- S3.2 (on [Gaussian resampling with permutations left in the transform](gaussian-resampling.md)): One Fourier transform of length $s$ (coprime to $t>s$) equals $2^{2\alpha^2}B_0P_tF_tA$ up to a coordinate permutation $P_s$, with Gaussian contractions $A,B_0$ and both permutations left inside the formula, and the same holds axis by axis.
- S3.3 (on [Bluestein chirp identity](bluestein-chirp.md)): The permuted transform $QF_{\boldsymbol t}$ equals pointwise multiplication by $\overline a$, a cyclic convolution with the chirp $a$, and another multiplication by $\overline a$.
- S3.4 (on [Source permutation cancellation](permutation-cancellation.md)): The retained permutation $R$ cancels across two forward transforms, a pointwise product and the opposite transform, giving $(u*v)/S^2$.
- S3.5 (on [Parameter choice: precision, dimension, axis lengths and prime source lengths](parameter-choice.md)): Taking $b=\lceil\log_2 n\rceil$, $p=6b$, $d=\lfloor b^\epsilon\rfloor$, power-of-two axis lengths $t_i\in\{r/2,r\}$ with product $T\approx n/b$ and distinct odd primes $s_i$ just below $t_i$ with $S=\prod s_i$ satisfies every hypothesis of the preceding steps.
- S3.6 (on [Integer multiplication as convolution of radix digits](multiplication-by-convolution.md)): Writing both operands as polynomials in $2^b$, the product coefficients are a convolution of digit lists, each below $2^{3b}$, with no wraparound modulo $x^S-1$.
- S3.7 (on [Chinese-remainder address map to distinct prime axes](crt-address-map.md)): The map $\Phi:x\mapsto\prod_i x_i^{\mu_i}$ turns cyclic convolution of length $S$ into $d$-dimensional cyclic convolution on pairwise coprime axes, implemented by triangular controlled shifts.
- S3.8 (on [Coefficient twist from cyclic to negacyclic wrap](coefficient-twist.md)): The twist $x_d\mapsto\zeta y$ with $\zeta=e^{\pi i/r}$ identifies cyclic convolution on the last axis with negacyclic convolution in $\mathcal R_r$.
- S3.11 (on [Precision, rounding and carry propagation](precision-exact-recovery.md)): The recovered coefficients have error below $1/2$, so rounding gives the exact integer convolution coefficients and carries give the exact $2n$-bit product.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Integer multiplication as convolution of radix digits](multiplication-by-convolution.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Chinese-remainder address map to distinct prime axes](crt-address-map.md): An algebra isomorphism x ↦ Π x_i^{μ_i} turning one cyclic convolution of length S = Π s_i (pairwise coprime) into a d-dimensional cyclic convolution on prime axes, implemented as triangular controlled shifts plus axis reordering and zero padding.
  Shown as: The multiplication algorithm: digits to transform, pointwise product and back *<predicate>* Chinese-remainder address map to distinct prime axes
- [Gaussian resampling with permutations left in the transform](gaussian-resampling.md): Replaces a Fourier transform of length s (coprime to t, s<t) by one of length t via Gaussian-weighted contractions A and B₀, with P_s F_s = 2^{2α²} B₀ P_t F_t A, where the two coordinate permutations P_s, P_t stay inside the formula instead of being sorted separately; applied axis by axis for a tensor.
  Shown as: The multiplication algorithm: digits to transform, pointwise product and back *<predicate>* Gaussian resampling with permutations left in the transform
- [Bluestein chirp identity](bluestein-chirp.md): Writes the (permuted) transform Q·F_t as pointwise multiplication by a chirp ā, a cyclic convolution with the chirp a, and another pointwise multiplication by ā, so a transform becomes a normalized cyclic convolution.
  Shown as: The multiplication algorithm: digits to transform, pointwise product and back *<predicate>* Bluestein chirp identity
- [Source permutation cancellation](permutation-cancellation.md): Because the coordinate permutation R commutes with pointwise products and R F⁺ R = F⁺, the retained permutation in R F_s cancels across two forward transforms, a pointwise product and the opposite transform, giving (u*v)/S².
  Shown as: The multiplication algorithm: digits to transform, pointwise product and back *<predicate>* Source permutation cancellation
- [Coefficient twist from cyclic to negacyclic wrap](coefficient-twist.md): The isomorphism C[x]/(x^r−1) → C[y]/(y^r+1), x ↦ ζy with ζ = e^{πi/r}, which multiplies coefficient k by ζ^k so the negative wrap of the ring becomes the cyclic wrap after untwisting.
  Shown as: The multiplication algorithm: digits to transform, pointwise product and back *<predicate>* Coefficient twist from cyclic to negacyclic wrap
- [Convolution over the polynomial ring from the retained transform layout](synthetic-convolution.md): Normalized convolution M_r(f,g) = (f*g)/(rM): two forward synthetic transforms, pointwise ring products by signed packing in the retained stored order, and the opposite transform, with error below √2·M(3ℓ+1)·2^{−p}.
  Shown as: The multiplication algorithm: digits to transform, pointwise product and back *<predicate>* Convolution over the polynomial ring from the retained transform layout
- [Parameter choice: precision, dimension, axis lengths and prime source lengths](parameter-choice.md): For input length n, take b = ⌈log₂ n⌉, precision p = 6b, dimension d = ⌊b^ε⌋, chunk K = ⌊d^c⌋, power-of-two axis lengths t_i ∈ {r/2, r} with product T ≈ n/b, and distinct odd primes s_i just below t_i with T/2 < S < T so all resampling hypotheses hold.
  Shown as: The multiplication algorithm: digits to transform, pointwise product and back *<predicate>* Parameter choice: precision, dimension, axis lengths and prime source lengths
- [Precision, rounding and carry propagation](precision-exact-recovery.md): Tracks scales (the two factors S and 2^{2b+4}) and disk margins to show the recovered convolution coefficients have error below 1/2, rounds to nearest integers, and propagates radix-2^b carries to output the exact 2n-bit product.
  Shown as: The multiplication algorithm: digits to transform, pointwise product and back *<predicate>* Precision, rounding and carry propagation

## Pages that build on this one

- Time-bound accounting and the exponent κ: Dividing the costs of all stages by Tp = Θ(n) gives a table of normalized costs, each a power of p of at most 1 − 2κ (the minimum margin is 2^{−181} = 2κ with κ = 2^{−182}), so the total is O(n (lg n)^{1−κ}).
- Power-saving integer multiplication theorem: One deterministic multitape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model; it combines fast address interchange, fast simultaneous butterfly layers, and the resampling–chirp–synthetic-convolution reduction.

## Other pages you may link to

- [Exact integer multiplication on a multitape Turing machine](integer-multiplication-problem.md)
- [Schönhage–Strassen n log n optimality conjecture](optimality-conjecture.md)
- [Established O(n log n) multiplier (Harvey–van der Hoeven)](harvey-hoeven-multiplier.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring-mod.md)
- [Linear exchange network with restored scratch wires](scalar-exchange-network.md)
- [Array order and elementary stream scans](elementary-streams.md)
- [Controlled cyclic shifts and fixed rational scalings](controlled-cyclic-shifts.md)
- [Matrix rank, subspaces and orthogonal complements](linear-algebra-basics.md)
- [Frames: changing array representation along network edges](frames.md)
- [Tensor products of operators and arrays](tensor-product.md)
- [Nested subspace labels and the total-rank saving](subspace-labels-rank-saving.md)
- [Bit-network rational matrix interface](rational-matrix-interface.md)
- [Lower triangular factorization of a matrix](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](address-shear-cost.md)
- [Depth-first schedule of recursive calls on fixed tapes](fixed-tape-recursion-schedule.md)
- [Recursive power-width chunk interchange](power-width-interchange.md)
- [Fast interchange of address chunks](chunk-interchange.md)
- [Packed selected-bit addition on one rectangle](packed-selected-bit-addition.md)
- [Signed packing of polynomial products (Kronecker substitution)](signed-packing.md)
- [Normalized discrete Fourier transform](dft.md)
- [Two-point butterfly and radix-2 fast Fourier transform](fft-butterfly.md)
- [Two-point phase kernel C](phase-kernel.md)
- [Binary phase interface of the complex network](phase-frame-interface.md)
- [Disk-grid fixed-point arithmetic, contractions and error](fixed-point-disk-arithmetic.md)
- [Exact Gaussian dyadic evaluation with guard bits](guard-width-exactness.md)
- [Simultaneous normalized butterfly layer](simultaneous-butterfly-layer.md)
- [Cyclic convolution and the convolution theorem](cyclic-convolution.md)
- [Integer multiplication as convolution of radix digits](multiplication-by-convolution.md)
- [Multidimensional transform on a tensor of axes](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Transform layout on which parallel layers apply](synthetic-transform-layout.md)
- [Time-bound accounting and the exponent κ](time-bound-accounting.md)
- [Power-saving integer multiplication theorem](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "With these streams prepared, perform the following operations." (paper)

  > With these streams prepared, perform the following operations. \begin{enumerate} \item Apply the coefficient-address map $\Phi$, with its padded layout, to obtain source arrays $u,v$. Their coefficients are exact $p$-bit grid values of norm less than $1/4$. \item Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$. \item Multiply corresponding complex coefficients exactly and truncate each real and imaginary part toward zero to $p$ fractional bits, writing the result in the common $w_{\rm c}$-bit component format. Denote the resulting source array by $z$. \item Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators exactly by $S$, retaining the denominator $2^p$ and writing each component in signed width $w_{\rm c}+b$. Denote the repres

- "The two occurrences of $S$ in this algorithm undo different" (paper)

  > The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.


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

Write the body to `exegenius/tasks/0086-write-multiplication-algorithm.answer.md` and the JSON to `exegenius/tasks/0086-write-multiplication-algorithm.answer.json`, then run `exegenius submit 0086-write-multiplication-algorithm` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0086-write-multiplication-algorithm`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
