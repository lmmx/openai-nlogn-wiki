# exegenius task 0029-write-simultaneous-butterfly-layer

Project directory: `/home/user/openai-nlogn-wiki/runs/P2` (paths below are relative to it)

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
- Two-point butterfly and radix-2 fast Fourier transform (also: butterfly, FFT)
- Matrix rank, subspaces and orthogonal complements
- Tensor products of operators and arrays
- Disk-grid fixed-point arithmetic, contractions and error (also: disk grid, truncation Q_p)
- Array order and elementary stream scans
- Controlled cyclic shifts and fixed rational scalings
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring)
  - $y$ (ring indeterminate): The formal variable of the polynomials, a root of −1 raised to the r-th power, whose powers serve as roots of unity.
  - $r$ (polynomial length): The number of complex coefficients in a stored polynomial, a power of two.
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

Concept: Simultaneous normalized butterfly layer
Gloss: Applies H₀ at once to the same bit position of D ≤ d address chunks of a polynomial-record array via the C-kernel network with phase frames, packed binary basis changes and row splitting among roles, in O(V d^{λ'}) time for a fixed λ' < 1 instead of D whole-array passes, with one final truncation.
Also called: parallel butterfly layer

## This page in the argument

The step: The butterfly $H_0(u,v)=((u+v)/2,(u-v)/2)$ can be applied at once to the same bit position of $D\le d$ address chunks of a polynomial-record array in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$, followed by one truncation $Q_p$.
How: Apply the complex phase network recursively to compute $C^{\otimes D}$ (which differs from $H_0^{\otimes D}$ by diagonal phases), implement the binary basis changes by packed whole-chunk shifts, split rows among the network roles to shrink each call, and keep all values exact until one final truncation
Why: Applying $D$ separate butterfly factors would need $D$ whole-array passes; the same exchange network that speeds up address moves gives a recursion with $s$ children on a $1/W$ share of the volume, so the cost per unit volume grows as a power of $d$ below one. (the sources say so: "factors would require $D$ whole-array passes." (paper))
Striking feature: A layer on $D\le d$ axes costs $O(Vd^{\lambda'})$ with $\lambda'<1$, which is sublinear in the number of axes, not $D$ passes over the array. (explain why it holds, from the method)

Its sub-steps, in order:

- With phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\mathrm{wt}(P_Ux)\bmod4})H^{\otimes m}$, each edge change is a product of translation kernels $aI+bX_v$, one per vector of an orthonormal basis of its residual, so $s_{\rm c}<W_{\rm c}m$ smaller calls of $C^{\otimes}$ suffice and the whole network realises $C^{\otimes m}$ on every role. (on [Binary phase interface of the complex network](phase-frame-interface.md))
- Applying the network with column frames to a group of $e=mf$ selected axes needs exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and returns $C^{\otimes e}$ on every role.
- The normalized layer equals phase-conjugated $C$ layer: $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$, where $\mathcal S_D$ multiplies by $i^{x_1+\cdots+x_D}$ and all phases and scalars are exact Gaussian dyadic operations.
- The XOR $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ of selected bits of chunks, needed for binary basis changes, is done by a few whole-chunk cyclic shifts and a sorting repair of a small bad set, restoring a scratch chunk $z$, in $O(V(L^\tau+1))$ time. (on [Packed selected-bit addition on one rectangle](packed-selected-bit-addition.md))
- Splitting rows among the $W$ roles gives the recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ for time per unit volume, which unrolls to $O(d^{\lambda'})$ with $\lambda'<1$.
- All intermediate values of one layer are exact Gaussian dyadics, and $\lceil C_0d^{C_1}\rceil$ guard bits bound denominator and magnitude growth, so a single truncation after the completed layer suffices. (on [Exact Gaussian dyadic evaluation with guard bits](guard-width-exactness.md))
- The recursion, the packed basis changes and the guard-width bound together give total time $O(Vd^{\lambda'})$, and $\mathcal H$ maps disk arrays to disk arrays with truncation error below $\sqrt2\,2^{-p}$.

It serves these steps, from the main result down:

- One deterministic multitape Turing machine multiplies $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.; how: Build two fast tape procedures (address interchange and simultaneous butterfly layers), run them inside synthetic transforms, reduce integer multiplication to such a convolution by resampling, chirps and a Chinese-remainder layout, then check precision and total up the time (on [Power-saving integer multiplication theorem](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.2, S2.3, S2.5, S2.7). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.2**: Applying the network with column frames to a group of $e=mf$ selected axes needs exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and returns $C^{\otimes e}$ on every role.
Source: "$e=mf$ selected axes.  Summing its residual dimensions gives exactly" (paper)
> \paragraph{The exact recursive contract.} Apply the finite network with these column frames to a group of $e=mf$ selected axes. Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot. The source and sink $Z_{a,f}$ signs, together with the scalar $i^{27f}$ at each affected sink, turn every endpoint kernel into a forward one. Negating the prescribed physical bank and undoing its exchange returns each result to its original role. Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary. Formula~\eqref{eq:phase-inverse-child} supplies each inverse child from one forward call, and none of the corrections adds a child. The remaining operations are a fixed number of binary row additions and coefficientwise scalar operations.

**S2.3**: The normalized layer equals phase-conjugated $C$ layer: $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$, where $\mathcal S_D$ multiplies by $i^{x_1+\cdots+x_D}$ and all phases and scalars are exact Gaussian dyadic operations.
Source: "H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D." (paper)
> \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

**S2.5**: Splitting rows among the $W$ roles gives the recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ for time per unit volume, which unrolls to $O(d^{\lambda'})$ with $\lambda'<1$.
Source: "F(e)\le (s/W)F(e/m)+O((eK)^\tau+1)," (paper)
> \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).

**S2.7**: The recursion, the packed basis changes and the guard-width bound together give total time $O(Vd^{\lambda'})$, and $\mathcal H$ maps disk arrays to disk arrays with truncation error below $\sqrt2\,2^{-p}$.
Source: "The row construction and the recurrence analysis" (paper)
> Uniformly for large $p$, the bands give $f\le d\le p$ and \[ K\ge\tfrac12a_d^c p^{\epsilon c},\qquad r\ge2^{(a_r/b_d)p^{1-\epsilon}}. \] The first inequality follows from $K=\lfloor d^c\rfloor$ once $d^c\ge2$. In particular, $K\ge6$ and $K/\log p\to\infty$, while $r$ dominates every fixed polynomial. Substituting the common bound $A_*\le C_Ap$ into the two additional normalized terms in \eqref{eq:packed-rectangle-time} gives \[ \begin{aligned} \frac{A_*^3}{R_{\rm g}} &\le\frac{C_A^3p^2}{2r},\\ 80(f-1)2^{-K}A_*\left(1+\frac{A_*}{R_{\rm g}}\right) &\le80C_Ap^2 2^{-K}\left(1+\frac{C_A}{2r}\right). \end{aligned} \] Both bounds tend to zero uniformly over all current allowed $d,r$. Thus Lemma~\ref{lem:packed-selected-bit-rectangle} has the required $O(M_{\rm child}R_{\rm g}(L^\tau+1))$ cost for every packed call, with one common time constant. The row construction and the recurrence analysis above give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams. Equation~\eqref{eq:phase-butterfly-layer} converts the resulting exact $C$-layer to $\mathcal H$.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.1 (on [Binary phase interface of the complex network](phase-frame-interface.md)): With phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\mathrm{wt}(P_Ux)\bmod4})H^{\otimes m}$, each edge change is a product of translation kernels $aI+bX_v$, one per vector of an orthonormal basis of its residual, so $s_{\rm c}<W_{\rm c}m$ smaller calls of $C^{\otimes}$ suffice and the whole network realises $C^{\otimes m}$ on every role.
- S2.4 (on [Packed selected-bit addition on one rectangle](packed-selected-bit-addition.md)): The XOR $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ of selected bits of chunks, needed for binary basis changes, is done by a few whole-chunk cyclic shifts and a sorting repair of a small bad set, restoring a scratch chunk $z$, in $O(V(L^\tau+1))$ time.
- S2.6 (on [Exact Gaussian dyadic evaluation with guard bits](guard-width-exactness.md)): All intermediate values of one layer are exact Gaussian dyadics, and $\lceil C_0d^{C_1}\rceil$ guard bits bound denominator and magnitude growth, so a single truncation after the completed layer suffices.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Fast interchange of address chunks](chunk-interchange.md)
- [Two-point phase kernel C](phase-kernel.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Binary phase interface of the complex network](phase-frame-interface.md): Using frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} for binary labels, every edge change is a product of translation kernels aI + bX_v, one per orthonormal residual basis vector, so s_c smaller calls of C^{⊗} suffice and the whole network realizes C^{⊗m} on every role.
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Binary phase interface of the complex network
- [Packed selected-bit addition on one rectangle](packed-selected-bit-addition.md): XORs the selected bits of several chunks into another chunk with a few whole-chunk cyclic shifts that act as packed single-bit additions away from carry-prone guard values, then repairs the small explicitly identified bad set of addresses by sorting, restoring a third scratch chunk.
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Packed selected-bit addition on one rectangle
- [Exact Gaussian dyadic evaluation with guard bits](guard-width-exactness.md): All intermediate values in one butterfly layer are exact Gaussian dyadics (real and imaginary parts with power-of-two denominators), so extra guard bits of width O(d^{C₁}) bound growth and a single truncation follows the completed contractive layer.
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Exact Gaussian dyadic evaluation with guard bits
- [Recursive power-width chunk interchange](power-width-interchange.md): Splits rows cyclically into W role streams, applies the network with shear frames on each edge (s recursive interchanges of chunks of width e/m, each on volume V/W), giving F_k ≤ (s/W)F_{k−1} + O(1) and cost O(V e^τ), because s/W < m^τ.
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Recursive power-width chunk interchange
- [Depth-first schedule of recursive calls on fixed tapes](fixed-tape-recursion-schedule.md): Recursive calls on W role streams are run on a fixed set of tapes by parking inactive streams on a stack, copying the active stream to the child, and restoring on return, at O(V) extra cost per node.
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Depth-first schedule of recursive calls on fixed tapes
- [Two-point butterfly and radix-2 fast Fourier transform](fft-butterfly.md): The butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) pairs entries half a block apart; a decimation-in-frequency transform of length 2^a applies butterflies and twiddle-factor multiplications over a levels and leaves the output in bit-reversed order.
  Shown as: Simultaneous normalized butterfly layer *<predicate>* Two-point butterfly and radix-2 fast Fourier transform

## Pages that build on this one

- Transform layout on which parallel layers apply: Places the selected bits of all axes at a common offset of consecutive K-bit chunks using prefix-slot moves and chunk exchanges, so each transform round is one simultaneous butterfly layer; total cost O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]).
- Time-bound accounting and the exponent κ: Dividing the costs of all stages by Tp = Θ(n) gives a table of normalized costs, each a power of p of at most 1 − 2κ (the minimum margin is 2^{−181} = 2κ with κ = 2^{−182}), so the total is O(n (lg n)^{1−κ}).

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
- [Fast interchange of address chunks](chunk-interchange.md)
- [Signed packing of polynomial products (Kronecker substitution)](signed-packing.md)
- [Normalized discrete Fourier transform](dft.md)
- [Two-point phase kernel C](phase-kernel.md)
- [Disk-grid fixed-point arithmetic, contractions and error](fixed-point-disk-arithmetic.md)
- [Cyclic convolution and the convolution theorem](cyclic-convolution.md)
- [Integer multiplication as convolution of radix digits](multiplication-by-convolution.md)
- [Multidimensional transform on a tensor of axes](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Coefficient twist from cyclic to negacyclic wrap](coefficient-twist.md)
- [Chinese-remainder address map to distinct prime axes](crt-address-map.md)
- [Transform layout on which parallel layers apply](synthetic-transform-layout.md)
- [Convolution over the polynomial ring from the retained transform layout](synthetic-convolution.md)
- [Gaussian resampling with permutations left in the transform](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Source permutation cancellation](permutation-cancellation.md)
- [Parameter choice: precision, dimension, axis lengths and prime source lengths](parameter-choice.md)
- [Precision, rounding and carry propagation](precision-exact-recovery.md)
- [The multiplication algorithm: digits to transform, pointwise product and back](multiplication-algorithm.md)
- [Time-bound accounting and the exponent κ](time-bound-accounting.md)
- [Power-saving integer multiplication theorem](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Simultaneous normalized butterfly layer" (paper)

  > \begin{proposition}[Simultaneous normalized butterfly layer] \label{prop:simultaneous-layer} Fix \[ \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad C_1=20. \] Let $c,\epsilon,\lambda,\lambda'$ be fixed positive rational numbers satisfying \[ \max\{\tau,\sigma\}<\lambda<1,\qquad \tau(1+c/\beta)<\lambda,\qquad \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1, \qquad \epsilon C_1<1. \] Fix positive constants $a_d\le b_d$ and $a_r\le b_r$, and fix positive constants $C_M,C_{\rm desc},C_w$ with $C_w>1$. For these fixed choices there are a cutoff $p_0$, one fixed finite-alphabet multitape procedure, and an implicit time constant with the following guarantee. The cutoff and time constant may depend on the fixed rational parameters and these constants. For every choice of positi

- "equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a" (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.

- "H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D" (paper)

  > \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.


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

Write the body to `exegenius/tasks/0029-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0029-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0029-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0029-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
