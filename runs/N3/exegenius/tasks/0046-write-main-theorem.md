# exegenius task 0046-write-main-theorem

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N3` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science degree: discrete mathematics (sets, subsets and binomial coefficients, induction, modular arithmetic, gcd and the Chinese remainder theorem, primes), a first course in linear algebra (matrices, Gaussian elimination, rank, dot products, possibly over GF(2)), calculus (exponentials, logarithms, Newton's method, simple inequalities), and algorithms and computation theory (asymptotic notation, recurrences and geometric sums, sorting including radix sort, binary search, schoolbook and Karatsuba multiplication, amortized binary counters, Turing machines and worst-case running time). They know binary and two's-complement representation of integers and XOR, but have not studied abstract algebra beyond what these courses use, the fast Fourier transform in depth, quotient polynomial rings, or the research literature on fast integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine (also: fixed finite-tape model)
- Linear maps, subspaces and rank
- Exact integer multiplication on a multitape machine
- n log n optimality conjecture (also: Schönhage–Strassen conjecture)
  - $n$ (input bit length): The number of bits in each of the two input integers.
- Normalized discrete Fourier transform
- Cyclic convolution
- Harvey–van der Hoeven O(n log n) multiplier (also: established multiplier)
  - $n$ (operand bit length): The number of bits in each integer given to the multiplier.
- Radix-digit reduction to convolution
- Lexicographic array layout and logical volume (also: logical volume, row)
- Elementary stream operations
- Controlled shifts and rational scalings
- Chinese-remainder address map (also: Agarwal–Cooley map, coefficient-address map)
- Gaussian resampling
- Resampling with retained permutations (also: tensor interface)
- Bluestein's chirp identity
- Source permutation cancellation
- Polynomial ring modulo y^r + 1 (also: R_r, negacyclic polynomial ring)
  - $y$ (ring variable): The polynomial indeterminate whose powers act as synthetic roots of unity.
  - $r$ (record length): The number of complex coefficients in each polynomial record, a power of two.
- Coefficient twist (also: phase twist)
- Gaussian dyadic numbers and fixed-point grids (also: disk grid array, Q_p)
- Normalized butterfly H₀ (also: butterfly)
  - $H_0$ (normalized butterfly): The two-point linear map sending (u, v) to ((u+v)/2, (u−v)/2).
- Synthetic polynomial transform (also: Nussbaumer transform, synthetic roots of unity)
- Linear network with roles and scratch wires (also: role, scratch wire)
- Restoring arbitrary scratch values (also: transparent computation)
- Triple-intersection pairings (also: Frankl–Wilson construction)
- Nondegenerate bilinear forms and orthogonal residuals
- Three-stage bank exchange (also: gather and scatter, side injection)
- Frames and the common-frame identity (also: frame)
- Nested subspace labels and rank budget (also: labels)
- Recursive saving from s < Wm (also: power saving)
  - $s$ (smaller-call count): The total number of smaller recursive calls made by one use of the finite network.
  - $W$ (wire count): The number of wires (roles) in the finite network.
  - $m$ (label dimension): The dimension of the label space, equal to the factor by which the parameter shrinks per recursion level.
- Address shear
- Lower triangular factorization (also: Bruhat factorization)
- Cost of a rational matrix shear
- Rational shear interface of the bit network
- Power-width interchange recursion
- Fast address-chunk interchange (also: chunk swap, address interchange)
- Binary phase frames (also: binary phase interface, complex network)
- Packed selected-bit addition
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Transform layout on K-bit chunks
- Signed Kronecker packing (also: Kronecker substitution)
- Normalized convolution over the polynomial ring
- Error below 1/2 and exact recovery
- Parameter choice and cost table
- Binary representation of integers (also: binary expansion, bit string value, most significant bit, least significant bit, bin_k, val, radix-2 representation, base-2 digits)
- Positional number systems with a general radix (also: base q digits, radix-q digits, base 2^b digits, radix, digit expansion)
- Two's complement (also: two's-complement integers, signed binary words, sign extension, signed w-bit integer)
- Binary addition with carry propagation (also: carry propagation, ripple-carry addition, carries, schoolbook addition)
- Schoolbook multiplication (also: long multiplication, grade-school multiplication, quadratic multiplication, O(n^2) multiplication)
- Karatsuba multiplication (also: Karatsuba's algorithm, Karatsuba–Ofman, O(n^{log_2 3}) multiplication)
- Integer division with remainder (also: quotient and remainder, Euclidean division, div and mod, integer square root)
- Floor and ceiling (also: ⌊x⌋, ⌈x⌉, rounding down, rounding up, truncation toward zero, integer part)
- Logarithms and exponentials (also: log_2, lg, natural logarithm, log, exp, e^x, logarithmic factor)
- Asymptotic notation beyond big-O (also: Theta notation, Omega notation, little-o, Θ, Ω, o(1), n^{o(1)}, eventually, for sufficiently large n)
- Worst-case running time (also: time complexity, worst-case time, T(n), step count, bit complexity)
- Deterministic computation (also: deterministic Turing machine, deterministic algorithm, no advice, uniform algorithm)
- Polynomial time and polylogarithmic cost (also: polynomial cost, poly(p), b^{O(1)}, polylog)
- Recurrence relations (also: recurrences, divide-and-conquer recurrence, recursion tree, master theorem)
- Geometric series (also: geometric sum, Σ a^k, geometric progression)
- Mathematical induction (also: induction, proof by induction, inductive argument)
- Sets, subsets and Cartesian products (also: Cartesian product, [a] = {0,...,a−1}, set intersection, cardinality, three-element subsets, indicator vector, characteristic vector)
- Binomial coefficients (also: n choose k, C(n,k), combinations, k-subsets)
- Permutations (also: bijection, permutation, inverse permutation, composition of permutations, reordering)
- Lexicographic order (also: row-major order, dictionary order, lexicographic layout, most significant coordinate first)
- Matrix transposition (also: transpose, row-major to column-major, A^T)
- Modular arithmetic (also: congruence, mod, residues, Z/qZ, ≡ (mod q), residue ring, modular inverse)
- Greatest common divisor and the extended Euclidean algorithm (also: gcd, Euclid's algorithm, extended Euclid, coprime, relatively prime, Bézout)
- Prime numbers and trial division (also: primes, odd primes, primality testing, trial division)
- Chinese remainder theorem (also: CRT, Chinese remaindering)
- Exclusive or and arithmetic modulo 2 (also: XOR, ⊕, GF(2), F_2, binary field, parity, bitwise XOR)
- Hamming weight (also: weight, wt(x), popcount, number of ones)
- Gaussian elimination (also: row reduction, elimination, elementary row operations)
- Dot product and orthogonality (also: inner product, orthogonal vectors, orthonormal basis, z·w)
- Special matrices (also: identity matrix, diagonal matrix, triangular matrix, permutation matrix, Kronecker product of matrices, block matrix)
- Triangle inequality (also: |a+b| ≤ |a|+|b|, absolute error bound)
- Bernoulli's inequality (also: (1+x)^n ≥ 1+nx)
- Newton's method (also: Newton iteration, Newton–Raphson)
- Binary search (also: bisection search)
- Radix sort and stable sorting (also: stable sort, binary radix sort, counting sort, merge, merge sort)
- Amortized cost of a binary counter (also: binary counter, incrementing a counter, ripple counting, amortized analysis)
- Stacks (also: stack, push, pop, last-in first-out, LIFO)
- Fixed-point binary numbers (also: fixed-point, fractional bits, binary point, guard bits, precision p)

## This page

Concept: Integer multiplication below n log n
Gloss: There is one deterministic fixed-alphabet multitape Turing machine computing the exact product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, by chaining radix-digit convolution, a CRT address map, Gaussian resampling with retained permutations, Bluestein chirps, a coefficient twist and synthetic transforms accelerated by fast chunk interchanges and simultaneous butterfly layers; this disproves the n log n optimality conjecture in that model.
Also called: Theorem 1
Heading: Integer multiplication below $n\log n$

The symbols in this page's heading denote (say so on the page):

- $n$ (input bit length): The number of bits in each of the two integers being multiplied.

## This page in the argument

The step: One deterministic fixed-alphabet multitape Turing machine computes the exact product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$, disproving the $n\log n$ optimality conjecture in that model.
How: build two sublinear-per-level tape procedures from finite linear networks with a rank deficit, then chain the known reductions from integer product to synthetic polynomial transforms and bound every cost
Why: The Harvey-van der Hoeven route already reduces multiplication to transform levels made of address rearrangements, signed shifts and butterflies; scanning all data per level costs n log n, so beating it needs savings in both movement and arithmetic. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))
Striking feature: The exponent $1-\kappa$ is strictly below one, so the bound beats $n\log n$ by a power of $\log n$, which the conjectured lower bound forbids. (explain why it holds, from the method)

Its sub-steps, in order:

- Interchanging $u$-bit address chunks costs $O(Vu^\tau)$ and a simultaneous butterfly layer on $d$ chunks costs $O(Vd^{\lambda'})$, with $\tau,\lambda'<1$.
- Exact multiplication of two $n$-bit integers reduces to synthetic transforms and packed ring products whose total cost is $O(n(\lg n)^{1-\kappa})$.

## Steps this page derives

The argument gives this page these sub-steps of its step (S1, S2). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1**: Interchanging $u$-bit address chunks costs $O(Vu^\tau)$ and a simultaneous butterfly layer on $d$ chunks costs $O(Vd^{\lambda'})$, with $\tau,\lambda'<1$.
How: supply linear elementary scans, build two finite networks with a rank deficit, and turn each network into a volume-normalized recursion on tape
- S1.3: Two fixed linear networks with $W$ wires exchange two banks of values, restore every scratch value, and admit nested subspace labels whose total edge rank $s$ satisfies $s<Wm$.
  How: build a three-stage scalar bank exchange, verify that frames commute with pointwise gates, attach nested subspace labels from triple-intersection pairings, and read off the rational and binary interfaces
  - S1.3.6: Both relative deficits exceed $20\cdot2^{-50}$, so $s/W<m^\tau$ with the fixed rational exponent $\tau=1-2^{-50}$ for both networks.
    Source: "For both recurrences we may use the fixed rational exponent" (paper)
    > The relative rank deficits are \[ \eta_{\rm b}=\frac{W_{\rm b}m-s_{\rm b}}{W_{\rm b}m} =\frac{339}{22587335000000},\qquad \eta_{\rm c}=\frac{W_{\rm c}m-s_{\rm c}}{W_{\rm c}m} =\frac{73}{19906842167500}. \] For both recurrences we may use the fixed rational exponent \begin{equation} \tau=\sigma=1-2^{-50}. \label{eq:explicit-motif-exponents} \end{equation} Both exact deficits displayed above are greater than $20\cdot2^{-50}$. Since $m<2^{20}$ and $\log 2<1$, we have $\log m<20$, whence \[ m^{1-2^{-50}} =m\exp(-2^{-50}\log m) >m(1-20\cdot2^{-50})>m(1-\eta) \] for either $\eta=\eta_{\rm b}$ or $\eta=\eta_{\rm c}$. Consequently \[ \frac{s_{\rm b}}{W_{\rm b}}<m^\tau, \qquad \frac{s_{\rm c}}{W_{\rm c}}<m^\sigma, \qquad 0<\tau=\sigma<1. \] Here $\sigma$ is a rational upper bound for the logarithmic exponent of the complex recurrence. \section{Faster interchange of address chunks} \label{sec:tape-interchange}

**S2**: Exact multiplication of two $n$-bit integers reduces to synthetic transforms and packed ring products whose total cost is $O(n(\lg n)^{1-\kappa})$.
How: compute synthetic transforms with the fast layers, build normalized ring convolution, express prime-length transforms by resampling with retained permutations and chirps, then assemble radix digits, the CRT map, the twist, precision and parameters
- S2.1: Normalized synthetic transforms $F_{\boldsymbol t}^\pm$ over $\mathcal R_r$ on $d-1$ power-of-two axes are computed in a retained stored order at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.
  How: decimation-in-frequency with polynomial roots of unity in stored bit-reversed order, grouped into simultaneous rounds on a chunked layout
- S2.6: The assembled algorithm outputs the exact $2n$-bit product in $O(n(\lg n)^{1-\kappa})$ time.
  How: fix rational parameters, convert digits, apply the CRT address map, the source transforms built from resampling, chirps and the twist, then prove error below $1/2$ and tabulate costs
  - S2.6.1: Fixed rationals $\tau=1-2^{-50}$, $\lambda'=1-2^{-54}$, $\epsilon=2^{-75}$, $c=2^{-56}$, $\kappa=2^{-182}$ satisfy all layer and dimension conditions.
    Source: "These constants are deliberately conservative; no optimization is claimed." (paper)
    > The two motif exponents were fixed in \eqref{eq:explicit-motif-exponents}. Take the following fixed rational numbers: \begin{equation}\label{eq:fixed-parameters} \begin{gathered} \tau=\sigma=1-2^{-50},\qquad \beta=\frac12,\qquad \delta=\frac1{16},\\ \lambda=1-2^{-52},\qquad c=2^{-56},\qquad \lambda'=1-2^{-54},\\ C_1=20,\qquad \epsilon=2^{-75},\qquad \kappa=2^{-182}. \end{gathered} \end{equation} These constants are deliberately conservative; no optimization is claimed.
  - S2.6.5: Composing $\widetilde{\mathcal A}$, the chirp transform and $\widetilde{\mathcal B}_0$ computes $RF_{\boldsymbol s}$, and conjugation gives $RF_{\boldsymbol s}^+$.
    Source: "its exact counterpart is $RF_{\boldsymbol s}^{+}$ by" (paper)
    > For a source disk-grid tensor of norm at most $.5$, write $\widetilde{\mathscr F}$ for the following procedure: apply the linewise approximation to $\mathcal A$, apply the computed chirp transform $\widetilde{\mathscr C}$, apply the linewise approximation to $\mathcal B_0$, and multiply the grid numerators exactly by $2^\gamma$. Its exact counterpart is \[ \mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A =RF_{\boldsymbol s}. \] Here an exact counterpart replaces every numerical subroutine by the exact map it approximates and omits truncations. The source arrays are stored in the padded power-of-two box, with zeros outside the valid source coordinates. The compressed scalar output uses $w_{\rm c}$-bit components. Appending $\gamma$ zero bits to each word gives the exact scaled numerator in the known signed width $w_{\rm c}+\gamma$. For the stated input norm, the disk estimate below proves that every scaled coordinate still belongs to $\mathbb D_p$. Its component numerators therefore have magnitude at most $2^p$, so a scan removes only leading sign-extension bits and returns the same integers in $w_{\rm c}$ bits. This scan costs $O(T(w_{\rm c}+\gamma))=O(Tp)$ and leaves the padded zero records zero. Define the opposite-sign procedure by \[ \widetilde{\mathscr F}^{+}(z) =\overline{\widetilde{\mathscr F}(\overline z)}; \] its exact counterpart is $RF_{\boldsymbol s}^{+}$ by Lemma~\ref{lem:chirp-permutation}.
  - S2.6.6: Two forward source transforms, a pointwise product, the opposite transform and two scalings by $S$ recover $2^{2b+4}(u*v)$.
    Source: "The two occurrences of $S$ in this algorithm undo different" (paper)
    > The two occurrences of $S$ in this algorithm undo different normalizations. By \eqref{eq:source-permutation-cancel}, the exact counterpart after the three transforms is $(u*v)/S^2$, so after the first scale it is $w=(u*v)/S$. The second scale gives $2^{2b+4}(u*v)$, whose inverse image under $\Phi$ is the original integer coefficient convolution. The next subsection verifies the disk bounds needed by every call and proves that the final error is less than $1/2$; it also justifies the rounding, carries, and output length.
  - S2.6.9: With schoolbook multiplication below a cutoff, one fixed machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every $n$.
    Source: "$O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely" (paper)
    > Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S1.1 (on [Elementary stream operations](elementary-streams.md)): Moving or permuting single radix digits of addresses, splitting and merging streams on a digit, and distributing rows cyclically among $W$ streams each take $O(V)$ steps.
- S1.2 (on [Controlled shifts and rational scalings](controlled-shifts.md)): An update $y\mapsto y+a(\text{controls})\bmod Q$ of a field following its controls, and multiplication by fixed rational units, cost $O(V)$.
- S1.3.1 (on [Three-stage bank exchange](bank-exchange.md)): Three stages of copy, gather, scatter and side-injection invocations send $(X_a,Y_a)\mapsto(-Y_a,X_a)$ for arbitrary initial scratch values, restoring every auxiliary value.
- S1.3.2 (on [Frames and the common-frame identity](frames.md)): If every vertex $v$ carries an invertible frame $D_v$, common to all incidences of a gate, the network on arrays implements $D_{\rm out}\mathsf S_\Omega D_{\rm in}^{-1}$, so intermediate frames cancel.
- S1.3.3 (on [Nested subspace labels and rank budget](subspace-labels.md)): Every edge joins comparable nondegenerate labels in the $m$-dimensional space $F^{\otimes3}$, the only decreasing edges are central-wire returns of loss $h$, and the total absolute dimension change is $Wm-2N+2L$ with $L<N/2$.
- S1.3.4 (on [Rational shear interface of the bit network](rational-shear-interface.md)): With projection matrices $P_U$ as frames, the bit network routes every role through the endpoint shear $I_m$ while its edge differences have total rational rank $s_{\rm b}<W_{\rm b}m$.
- S1.3.5 (on [Binary phase frames](phase-frames.md)): With binary phase frames $\mathcal C_U$, each edge change is a product of one kernel $aI+bX_v$ per orthonormal residual vector, $s_{\rm c}<W_{\rm c}m$ in total, and the endpoints telescope to $C^{\otimes m}$ on every role.
- S1.4 (on [Fast address-chunk interchange](fast-chunk-interchange.md)): Two disjoint $u$-bit address chunks of an array of volume $V$ can be interchanged in $O(Vu^\tau)$ time for a fixed $\tau<1$.
- S1.5 (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)): A normalized butterfly $H_0$ on the same bit of up to $d$ address chunks can be applied to polynomial records in $O(Vd^{\lambda'})$ time with $\lambda'<1$ and a single final truncation.
- S2.1.1 (on [Synthetic polynomial transform](synthetic-transform.md)): The decimation-in-frequency recursion with $\omega_t=y^{2r/t}$ computes $B_tF_t^-$ and the reverse procedure computes $F_t^+B_t^{-1}$.
- S2.1.2 (on [Transform layout on K-bit chunks](transform-layout.md)): Placing selected bits at a common offset in $K$-bit chunks makes each round one simultaneous layer, with layout and restoration charged in the cost.
- S2.2 (on [Normalized convolution over the polynomial ring](synthetic-convolution.md)): Normalized convolution $\mathcal M_r(f,g)=(f*g)/(rM)$ over $\mathcal R_r$ is approximated with error below $\sqrt2M(3\ell+1)2^{-p}$ at the transform cost plus $O(Tp\log(rp))$.
- S2.3 (on [Resampling with retained permutations](no-sort-resampling.md)): The tensor transform on prime lengths satisfies $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with contractions $\mathcal A,\mathcal B_0$ computable linewise.
- S2.4 (on [Bluestein's chirp identity](bluestein-chirp.md)): With chirp $a$, $QF_{\boldsymbol t}u=\overline a\cdot(a*(\overline a\cdot u))/T$, so the middle transform with its target permutation is a normalized cyclic convolution.
- S2.5 (on [Source permutation cancellation](source-permutation-cancellation.md)): $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$, so the retained source permutation cancels.
- S2.6.2 (on [Radix-digit reduction to convolution](radix-digit-convolution.md)): With $q=\lceil n/b\rceil$ digits in base $2^b$, the product's digits are a convolution modulo $x^S-1$ with no wraparound and coefficients below $2^{3b}$.
- S2.6.3 (on [Chinese-remainder address map](crt-address-map.md)): $x\mapsto\prod_ix_i^{\mu_i}$ is an isomorphism onto the product of prime cyclic axes, preserving convolution, and is implemented by triangular controlled shifts.
- S2.6.4 (on [Coefficient twist](coefficient-twist.md)): The twist $x_d\mapsto\zeta y$ turns complex cyclic convolution on the last axis into negacyclic convolution over $\mathcal R_r$, with the wrap recovered after untwisting.
- S2.6.7 (on [Error below 1/2 and exact recovery](exact-recovery.md)): The recovered coefficient error is below $1/2$, so rounding, $\Phi^{-1}$ and radix-$2^b$ carries give the exact product.
- S2.6.8 (on [Parameter choice and cost table](parameter-choice.md)): Every normalized cost in the table is at most $p^{1-2\kappa}$, since the smallest margin is $2^{-181}=2\kappa$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Lexicographic array layout and logical volume](array-layout.md)
- [Linear network with roles and scratch wires](linear-network.md)
- [Linear maps, subspaces and rank](linear-algebra.md)
- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Recursive saving from s < Wm](rank-deficit-recursion.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Exact integer multiplication on a multitape machine](integer-multiplication-problem.md): The task of reading x#y for two n-bit strings and writing the exact 2n-bit binary product, with cost measured as worst-case steps T_A(n) of one fixed multitape machine A and lg n = max{⌈log₂ n⌉, 1}.
  Shown as: Integer multiplication below n log n *<predicate>* Exact integer multiplication on a multitape machine
- [n log n optimality conjecture](nlogn-conjecture.md): Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers, i.e. that every multiplication machine eventually needs time at least c·n lg n.
  Shown as: Integer multiplication below n log n *<predicate>* n log n optimality conjecture
- [Radix-digit reduction to convolution](radix-digit-convolution.md): Splitting each n-bit input into q = ⌈n/b⌉ digits in base 2^b so that the product's digits are the convolution of the two digit lists, bounded below 2^{3b}, followed by carry propagation.
  Shown as: Integer multiplication below n log n *<predicate>* Radix-digit reduction to convolution
- [Chinese-remainder address map](crt-address-map.md): The algebra isomorphism x ↦ Π x_i^{μ_i} from C[x]/(x^S−1) to the product of cyclic axes of pairwise coprime prime lengths s_i, which preserves convolution and is implemented as triangular controlled shifts.
  Shown as: Integer multiplication below n log n *<predicate>* Chinese-remainder address map
- [Resampling with retained permutations](no-sort-resampling.md): The form P_s F_s = 2^{2α²} B₀ P_t F_t A of Gaussian resampling, and its tensor version R F_s = 2^γ 𝓑₀ Q F_t 𝓐, in which the source and target coordinate permutations stay inside the transform formula instead of being executed as sorts.
  Shown as: Integer multiplication below n log n *<predicate>* Resampling with retained permutations
- [Bluestein's chirp identity](bluestein-chirp.md): The identity Q F_t u = ā · (a * (ā · u))/T with chirp a_j = exp(−πi Σ s_i j_i²/t_i), converting the middle transform together with its target permutation into a normalized cyclic convolution and two pointwise phase multiplications.
  Shown as: Integer multiplication below n log n *<predicate>* Bluestein's chirp identity
- [Source permutation cancellation](source-permutation-cancellation.md): The identity (R F_s^+)[(R F_s u)·(R F_s v)] = (u*v)/S², showing that the source permutation R retained in the forward transforms cancels against the opposite-sign transform, so convolution needs no sort.
  Shown as: Integer multiplication below n log n *<predicate>* Source permutation cancellation
- [Coefficient twist](coefficient-twist.md): The isomorphism x_d ↦ ζy with ζ = e^{πi/r} from C[x_d]/(x_d^r − 1) to C[y]/(y^r + 1), which turns the last cyclic coordinate into a negacyclic polynomial whose wrap recovers the cyclic wrap after untwisting.
  Shown as: Integer multiplication below n log n *<predicate>* Coefficient twist
- [Normalized convolution over the polynomial ring](synthetic-convolution.md): Computing 𝓜_r(f, g) = (f*g)/(rM) for arrays over 𝓡_r by two forward synthetic transforms kept in the same stored frequency order, packed pointwise ring products, and the opposite transform consuming that order.
  Shown as: Integer multiplication below n log n *<predicate>* Normalized convolution over the polynomial ring
- [Error below 1/2 and exact recovery](exact-recovery.md): The precision argument showing the recovered convolution coefficients are within less than 1/2 of the true integers, so rounding, undoing the CRT map and propagating radix-2^b carries gives the exact 2n-bit product.
  Shown as: Integer multiplication below n log n *<predicate>* Error below 1/2 and exact recovery
- [Parameter choice and cost table](parameter-choice.md): The setting b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two box T ≈ 4n/b, prime axis lengths s_i near t_i, and fixed rationals τ, λ', ε, κ = 2^{−182}, under which every normalized cost is at most p^{1−2κ}.
  Shown as: Integer multiplication below n log n *<predicate>* Parameter choice and cost table
- [Fast address-chunk interchange](fast-chunk-interchange.md): The procedure exchanging two disjoint u-bit address fields of an array in O(V u^τ) time for a fixed τ < 1, computing XOR combinations of data along the way though its final effect is an exact permutation.
  Shown as: Integer multiplication below n log n *<predicate>* Fast address-chunk interchange
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): Applying H₀ on the same bit position of up to d address chunks at once in O(V d^{λ'}) time with λ' < 1, by recursing through the complex network's phase frames, packed bit changes and an exact Gaussian-dyadic evaluation with one final truncation.
  Shown as: Integer multiplication below n log n *<predicate>* Simultaneous butterfly layer

## Other pages you may link to

- [Harvey–van der Hoeven O(n log n) multiplier](hvdh-multiplier.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Normalized butterfly H₀](normalized-butterfly.md)
- [Gaussian dyadic numbers and fixed-point grids](gaussian-dyadics.md)
- [Signed Kronecker packing](signed-packing.md)
- [Lexicographic array layout and logical volume](array-layout.md)
- [Elementary stream operations](elementary-streams.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Address shear](address-shear.md)
- [Linear maps, subspaces and rank](linear-algebra.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Linear network with roles and scratch wires](linear-network.md)
- [Frames and the common-frame identity](frames.md)
- [Restoring arbitrary scratch values](scratch-restoration.md)
- [Nondegenerate bilinear forms and orthogonal residuals](bilinear-forms.md)
- [Triple-intersection pairings](triple-intersection.md)
- [Three-stage bank exchange](bank-exchange.md)
- [Nested subspace labels and rank budget](subspace-labels.md)
- [Recursive saving from s < Wm](rank-deficit-recursion.md)
- [Rational shear interface of the bit network](rational-shear-interface.md)
- [Binary phase frames](phase-frames.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Power-width interchange recursion](power-width-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Transform layout on K-bit chunks](transform-layout.md)
- [Cyclic convolution](cyclic-convolution.md)

## Evidence from the sources, with the paragraph around each quote

- "We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time" (paper)

  > \documentclass[11pt]{article} \usepackage[T1]{fontenc} \usepackage{lmodern,microtype} \usepackage{amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,array,longtable} \usepackage[margin=1in]{geometry} \usepackage{tikz} \usetikzlibrary{positioning,arrows.meta} \usepackage[hyphens]{url} \usepackage{hyperref} \hypersetup{colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black,pdftitle={Integer multiplication below n log n},pdfauthor={OpenAI}} \pdfinfoomitdate=1 \pdftrailerid{} \pdfsuppressptexinfo=15 \newtheorem{theorem}{Theorem} \newtheorem{lemma}[theorem]{Lemma} \newtheorem{proposition}[theorem]{Proposition} \newtheorem{corollary}[theorem]{Corollary} \theoremstyle{definition} \newtheorem{definition}[theorem]{Definition} \newtheorem{remark}[theorem]{Remark} \newcommand{\norm}[1]{\lVert#1\rVert_\infty} \title{Integer multiplication below \texorpdfstring{$n\log n$}{n log n}} \author{OpenAI} \date{September 23, 2026} \begin{document} \maketitle \begin{abstract} We give a deterministic algorithm that multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ worst-case time, with $\kappa=2^{-182}$, on one fixed finite-alphabet Turing machine with a fixed finite number of one-dimensional tapes. The algorithm is exact for every input length and disproves the $n\log n$ optimality conjecture of Sch\"onhage and Strassen in this model. \end{abstract} \tableofcontents \clearpage \section{Introduction}

- "The theorem refutes an eventual $\Omega(n\log n)$ lower bound for every fixed multiplication machine in this model." (paper)

  > The bound is asymptotic through all input lengths. The constants and thresholds in the construction are extremely large; the algorithm is intended to establish a bit-complexity bound. The theorem refutes an eventual $\Omega(n\log n)$ lower bound for every fixed multiplication machine in this model.

- "The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers." (paper)

  > Sch\"onhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine, and proposed $n\log n$ as the optimal order of growth \cite[Section~1]{SchonhageStrassen1971}. After a sequence of improvements, Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper bound~\cite{HarveyHoeven2021}. We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model. The algorithm uses linear combinations of intermediate data to reduce the cost of both address rearrangement and Fourier-transform layers.


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
