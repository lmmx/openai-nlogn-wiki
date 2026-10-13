# exegenius task 0039-write-main-theorem

Project directory: `/home/user/openai-nlogn-wiki/runs/G2` (paths below are relative to it)

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

For these sources: Undergraduate computer science: algorithms and complexity through big-O analysis, recurrences and divide-and-conquer (Karatsuba, FFT-based polynomial multiplication, usually met at the level of the standard recursive FFT), discrete mathematics (modular arithmetic, primes and gcd, sets, functions and permutations, induction), and introductory linear algebra (matrices, rank, bases, inner products, Gaussian elimination, over the reals and probably F_2). Also the basics of complex numbers and Turing machines with multiple tapes. The reader has not studied abstract algebra such as quotient rings or tensor products, finite-field theory beyond F_2, numerical analysis of rounding errors, or the research literature on integer multiplication (Schönhage–Strassen, Fürer, Harvey–van der Hoeven), and has not seen Bluestein, Nussbaumer polynomial transforms or Gaussian resampling.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- Bit XOR
- The n log n conjecture and prior bounds (also: Schönhage–Strassen conjecture)
- Arrays as tape streams and elementary scans
- Controlled shifts and rational scalings
- Fixed-point and Gaussian dyadic arithmetic
- Discrete Fourier transform
- Cyclic convolution
- Multiplication as convolution of radix digits
- Multidimensional transform
- Chinese-remainder address map (also: Φ)
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Two-point butterfly layer (also: butterfly, H₀)
- Synthetic polynomial transform (also: Nussbaumer polynomial transform)
- Signed packing for ring products
- The established O(N log N) multiplier
- Subspaces, bilinear forms and orthogonal complements
- Linear network with restored scratch wires (also: motif network, restoration schedule)
- Triple-subset intersection gadgets
- Frames on wire arrays
- Nested subspace labels and the rank deficit (also: s<Wm)
- Recursive power saving from the rank deficit
- Lower triangular factorization
- Matrix shear on address fields
- Fast interchange of address chunks
- Binary phase frames and the two-point kernel C
- Packed selected-bit addition
- Simultaneous butterfly layer
- Synthetic transform tape layout
- Normalized convolution over the ring
- Last-coordinate phase twist
- Gaussian resampling
- Resampling with permutations left in the transform
- Bluestein chirp identity
- Error bounds and exact recovery
- Parameter choice and cost table
- The multiplication algorithm
- Asymptotic notation beyond big-O (also: Omega notation, Theta notation, little-o, Ω, Θ, o(n log n))
- Logarithms and binary logarithm (also: lg, log base 2, log_2, ceiling of log)
- Floor and ceiling functions (also: floor, ceiling, ⌊x⌋, ⌈x⌉, integer part)
- Binary representation of integers (also: n-bit integer, bit string, binary expansion, two's complement, signed binary)
- Radix representation and digits (also: base-b expansion, positional notation, radix digits, leading zeroes)
- Schoolbook multiplication and carries (also: grade-school multiplication, long multiplication, quadratic multiplication, carry propagation, addition with carry)
- Divide-and-conquer and recurrences (also: recurrence relation, master theorem, Karatsuba multiplication, recursion, geometric series, geometric sum)
- Fast Fourier transform and FFT multiplication (also: FFT, Cooley-Tukey, radix-2 FFT, O(n log n) polynomial multiplication, evaluation and interpolation)
- Mathematical induction and proof by cases (also: induction, inductive proof, proof by contradiction)
- Sets, subsets and Cartesian products (also: set intersection, cardinality, subset of size three, product set, tuples, indicator vector)
- Functions, bijections and permutations (also: permutation, bijection, inverse function, composition, involution, partial permutation)
- Modular arithmetic and congruences (also: mod, residues, congruence, ℤ/nℤ, integers modulo n, remainder, units modulo n)
- Primes, divisibility and coprimality (also: gcd, greatest common divisor, relatively prime, prime power, coprime, trial division, prime factorization)
- Rational numbers and exact fractions (also: rationals, ℚ, denominator, numerator, dyadic rational)
- Finite fields and the field F_2 (also: GF(2), 𝔽_2, binary field, arithmetic modulo 2, parity)
- Vectors, matrices and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, identity matrix, linear transformation, diagonal matrix, linear combination)
- Rank, basis and dimension (also: linear independence, span, vector space, subspace dimension, rank of a matrix, rank-nullity)
- Gaussian elimination (also: row reduction, row operations, elementary matrices, triangular matrix, lower triangular, upper triangular)
- Inner product, norm and orthonormal basis (also: dot product, orthogonal vectors, orthonormal, unit vector, vector norm, max norm, sup norm, l-infinity norm, unit disk, absolute value of complex number, modulus)
- Roots of unity and Euler's formula (also: e^{iθ}, primitive root of unity, n-th roots of unity, unit circle, geometric series of roots)
- Summation and product notation (also: sigma notation, Σ, Π, indices, Kronecker delta)
- Newton's method (also: Newton iteration, Newton-Raphson, reciprocal by Newton, square root by Newton, quadratic convergence)
- Integer division with remainder (also: quotient and remainder, floor division, integer square root, division algorithm)
- Lexicographic order (also: dictionary order, row-major order, most significant first, mixed radix address)
- Arrays, records and matrix transposition (also: row-major, column-major, transpose, matrix layout, indexing)
- Turing machine running time and model conventions (also: worst-case time, time complexity, unit-cost RAM, random access machine, input and output tapes, finite alphabet, tape heads, scanning and sorting on tapes, linear-time scan, simulation)

## This page

Concept: Integer multiplication in O(n (lg n)^(1−κ)) time
Gloss: A deterministic multitape Turing machine multiplying two n-bit integers in O(n(lg n)^{1−κ}) time with κ=2^{−182}, refuting the n log n optimality conjecture in this model.
Heading: Integer multiplication in $O(n(\lg n)^{1-\kappa})$ time

The symbols in this page's heading denote (say so on the page):

- $n$ (input length): The number of bits in each of the two integers being multiplied.
- $\kappa$ (saving exponent): The fixed constant 2^{-182} giving the power saving in the logarithmic factor.

## This page in the argument

The step: A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$, refuting the $n\log n$ optimality conjecture in this model.
How: Reduce the product to a convolution over a polynomial ring computed by Fourier-type transforms; supply the two fast tape procedures that remove the logarithmic factor from address movement and from butterfly arithmetic, both obtained from linear networks that save a power; then assemble the algorithm and tally every cost.
Why: Scanning the data once per transform level already costs $n\log n$, so the logarithmic factor can only be reduced by savings in both data movement and arithmetic. (the sources say so: "We therefore need savings in both movement and arithmetic." (paper))

Its sub-steps, in order:

- There are two fixed linear networks of $W$ wires, one over bits and one over Gaussian dyadic numbers, each exchanging two banks of values with a sign while restoring every scratch wire, whose frames can be chosen so that the edge changes have total rank $s<W m$.
- For a fixed $\tau<1$, two disjoint contiguous address chunks of $u$ bits in an array of volume $V$ can be interchanged in $O(V u^\tau)$ time on a fixed number of tapes, although the intermediate streams are XOR combinations of the data. (on [Fast interchange of address chunks](fast-chunk-interchange.md))
- The map $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied at one common bit offset in each of $D\le d$ equal-width $K$-bit address chunks of an array of records, each a polynomial with $r$ complex coefficients on the grid $2^{-p}\mathbb Z[i]$, of total volume $V$, with a single final truncation, costs $O(V d^{\lambda'})$ for a fixed $\lambda'<1$. (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md))
- On disk-grid arrays over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ indexed by a product of cyclic axes with $T$ coefficients in all and $M=T/r$ records, the normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ is approximated with error below $\sqrt2 M(3\ell+1)2^{-p}$ in time $O(T p[d K+p K^{\tau-1}+\ell d^{\lambda'}+\log(r p)])$, where $\ell=\log_2 r$. (on [Normalized convolution over the ring](synthetic-convolution.md))
- For coprime $s_i<t_i$ with enough separation, the tensor Fourier transform $RF_{\boldsymbol s}$ together with its source permutation $R$ equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ for contractions $\mathcal A,\mathcal B_0$ computed line by line on a padded box of $T$ entries in time $O(d T p^{3/2+\delta}\alpha)$ plus axis movements $O(T p\,d^2(1+\ell^\tau))$, with both coordinate permutations left inside the formula. (on [Resampling with permutations left in the transform](resampling-without-sorting.md))
- For even $t_i$, the permuted transform satisfies $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}{T}$ with the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$, and the source permutation cancels, $(RF^+_{\boldsymbol s})[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$ with $S=\prod_i s_i$. (on [Bluestein chirp identity](bluestein-chirp.md))
- The procedure that extracts radix-$2^b$ digits, applies the Chinese-remainder address map $\Phi$, computes two forward source transforms, a pointwise product and the opposite transform with exact rescalings, rounds, and propagates carries outputs the exact $2n$-bit product. (on [The multiplication algorithm](multiplication-algorithm.md))
- Divided by $V=T p$, every cost term is $p$ to a power at most $1-2\kappa$, setup and exceptional repairs are $o(V)$, and powers of $\log p$ are absorbed, so the single fixed machine runs in time $O(n(\lg n)^{1-\kappa})$.

## Steps this page derives

The argument gives this page these sub-steps of its step (S1, S8). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S1**: There are two fixed linear networks of $W$ wires, one over bits and one over Gaussian dyadic numbers, each exchanging two banks of values with a sign while restoring every scratch wire, whose frames can be chosen so that the edge changes have total rank $s<W m$.
How: Construct the scalar exchange network, lift it to arrays with frames, then attach nested subspace labels to its gates and terminals and count the dimension changes, once for bits and once for phases.

**S8**: Divided by $V=T p$, every cost term is $p$ to a power at most $1-2\kappa$, setup and exceptional repairs are $o(V)$, and powers of $\log p$ are absorbed, so the single fixed machine runs in time $O(n(\lg n)^{1-\kappa})$.
How: Tabulate the normalized cost of every operation, check the seven dominant exponents against explicit margins, and show that setup, prime search and exceptional-address repairs are negligible.
- S8.1: Costs are tabulated after division by $V=T p=\Theta(n)$ with a fixed number of repeated transforms and convolutions absorbed into constants.
  Source: "For the cost calculation put $V=Tp=\Theta(n)$." (paper)
  > For the cost calculation put $V=Tp=\Theta(n)$. The fixed-width coefficient formats use $\Theta(p)$ bits per coefficient, so a full padded array has $\Theta(V)$ stored bits. Table~\ref{tab:costs} lists costs after division by $V$; a fixed number of repeated transforms and convolutions is included in its constants. \begin{table}[ht] \centering \small \begin{tabular}{@{}>{\raggedright\arraybackslash}p{.40\linewidth}ll@{}} \toprule Operation & Normalized cost & Power of $p$\\ \midrule Prefix-slot moves and individual butterfly rounds & $dK$ & $\epsilon(1+c)$\\ Chunk exchanges for transform layout & $pK^{\tau-1}$ & $1-\epsilon c(1-\tau)$\\ Simultaneous butterfly rounds & $\ell d^{\lambda'}$ & $1-\epsilon(1-\lambda')$\\ CRT and axis layouts & $d^2(1+\ell^\tau)$ & $\tau+\epsilon(2-\tau)$\\ Gaussian line maps & $dp^{1/2+\delta}\alpha$ & $3/4+\delta+3\epsilon/2$\\ Chirps, twists and scalar products & $dp^\delta$ & $\epsilon+\delta$\\ Packed polynomial products & $\log(rp)$ & $1-\epsilon$\\ Final scaling and rounding & $p^\delta$ & absorbed above\\ Input, padding, carries and output & $1$ & absorbed above\\ \bottomrule \end{tabular} \caption{Costs divided by $Tp$; each coefficient representation has $O(p)$ bits.}\label{tab:costs} \end{table}
- S8.2: Direct substitution gives the seven margins below one, the smallest being $2^{-181}=2\kappa$.
  Source: "Direct substitution gives" (paper)
  > The seven dominant powers in Table~\ref{tab:costs} have the following margins below one: \begin{equation}\label{eq:margin-list} \begin{split} g_1&=1-\epsilon(1+c),\qquad g_2=\epsilon c(1-\tau),\qquad g_3=\epsilon(1-\lambda'),\\ g_4&=1-\tau-\epsilon(2-\tau),\qquad g_5=1/4-\delta-3\epsilon/2,\\ g_6&=1-\delta-\epsilon,\qquad g_7=\epsilon. \end{split} \end{equation} Direct substitution gives \[ g_1>\frac12,\quad g_2=2^{-181},\quad g_3=2^{-129},\quad g_4>2^{-51},\quad g_5>\frac18,\quad g_6>\frac12,\quad g_7=2^{-75}. \] Thus $\min_i g_i=2^{-181}=2\kappa$. This explicit slack will cover any remaining fixed power of $\log p$.
- S8.3: Setup at recursion nodes, prime search and the compact exceptional streams of the packed changes of basis all cost $o(V)$ deterministically.
  Source: "We next separate setup at recursion nodes from work repeated for every" (paper)
  > \paragraph{Setup and exceptional streams across all calls.} We next separate setup at recursion nodes from work repeated for every polynomial record or every Gaussian line. Here a visit means a node of the layer or address-layout recursions, or one of their round and group invocations. The internal recursion of the established integer multiplier and the iterations of the quoted Gaussian algorithms are already included in their separately charged running times. The layer and address-layout recursions have constant branching and depth $O(\log p)$, and the number of their rounds and base-$m$ groups is polynomial in $p$. Choose a fixed exponent $A$ so that their total number of visits is at most $p^A$, and a fixed $C$ bounding descriptor setup performed once per visit by $p^C$ steps. This setup then costs at most $p^{A+C}=o(Tp)$.
- S8.4: Each of the seven displayed powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually, so the total is $O(T p\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$.
  Source: "Each of the seven displayed powers is at most $1-2\kappa$ by" (paper)
  > Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}
- S8.5: Using schoolbook multiplication below a fixed cutoff, the single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and outputs exactly the $2n$-bit product.
  Source: "With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single" (paper)
  > Each of the seven displayed powers is at most $1-2\kappa$ by \eqref{eq:margin-list}. Any fixed power of $\log p$ is at most $p^\kappa$ eventually. The complete large-input bound is consequently \[ O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa}). \] Fix one cutoff beyond all the size, precision, margin and layout conditions, and use schoolbook multiplication below it. The finitely many smaller lengths are included by enlarging the implicit constant. With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, the resulting single fixed-alphabet, fixed-tape deterministic machine has worst-case time $O(n(\lg n)^{1-\kappa})$ for every input length and produces precisely the required $2n$-bit product. \section{Exact division and integer square root} \label{sec:exact-arithmetic-proof}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2 (on [Fast interchange of address chunks](fast-chunk-interchange.md)): For a fixed $\tau<1$, two disjoint contiguous address chunks of $u$ bits in an array of volume $V$ can be interchanged in $O(V u^\tau)$ time on a fixed number of tapes, although the intermediate streams are XOR combinations of the data.
- S3 (on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)): The map $H_0(u,v)=((u+v)/2,(u-v)/2)$ applied at one common bit offset in each of $D\le d$ equal-width $K$-bit address chunks of an array of records, each a polynomial with $r$ complex coefficients on the grid $2^{-p}\mathbb Z[i]$, of total volume $V$, with a single final truncation, costs $O(V d^{\lambda'})$ for a fixed $\lambda'<1$.
- S4 (on [Normalized convolution over the ring](synthetic-convolution.md)): On disk-grid arrays over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ indexed by a product of cyclic axes with $T$ coefficients in all and $M=T/r$ records, the normalized convolution $\mathcal M_r(f,g)=(f*g)/T$ is approximated with error below $\sqrt2 M(3\ell+1)2^{-p}$ in time $O(T p[d K+p K^{\tau-1}+\ell d^{\lambda'}+\log(r p)])$, where $\ell=\log_2 r$.
- S5 (on [Resampling with permutations left in the transform](resampling-without-sorting.md)): For coprime $s_i<t_i$ with enough separation, the tensor Fourier transform $RF_{\boldsymbol s}$ together with its source permutation $R$ equals $2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ for contractions $\mathcal A,\mathcal B_0$ computed line by line on a padded box of $T$ entries in time $O(d T p^{3/2+\delta}\alpha)$ plus axis movements $O(T p\,d^2(1+\ell^\tau))$, with both coordinate permutations left inside the formula.
- S6 (on [Bluestein chirp identity](bluestein-chirp.md)): For even $t_i$, the permuted transform satisfies $QF_{\boldsymbol t}u=\overline a\cdot\frac{a*(\overline a\cdot u)}{T}$ with the chirp $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$, and the source permutation cancels, $(RF^+_{\boldsymbol s})[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=(u*v)/S^2$ with $S=\prod_i s_i$.
- S7 (on [The multiplication algorithm](multiplication-algorithm.md)): The procedure that extracts radix-$2^b$ digits, applies the Chinese-remainder address map $\Phi$, computes two forward source transforms, a pointwise product and the opposite transform with exact rescalings, rounds, and propagates carries outputs the exact $2n$-bit product.
- S1.1 (on [Linear network with restored scratch wires](linear-network.md)): A fixed circuit of linear gates on the wires, with arbitrary initial values on its scratch wires, sends the data banks $(X_a,Y_a)$ to $(-Y_a,X_a)$ and restores every scratch value.
- S1.2 (on [Frames on wire arrays](frames.md)): If every source, gate and sink $v$ gives each wire's array an invertible linear frame $D_v$, so that the stored array is $D_v$ applied to the logical array, then pointwise gates commute with the common frame and the network implements $D_{\rm out}\mathsf S D_{\rm in}^{-1}$, so that only the edge changes $D_vD_u^{-1}$ cost anything.
- S1.3 (on [Nested subspace labels and the rank deficit](rank-deficit-labels.md)): The bit network can be given nested nondegenerate subspace labels on its gates and terminals such that the endpoint matrices of every route differ by the identity $I_m$ and the total rank of all edge differences is $s<W m$.
- S1.4 (on [Binary phase frames and the two-point kernel C](phase-frames.md)): For the complex network with binary labels, the phase frames $\mathcal C_U=H^{\otimes m}\operatorname{diag}(i^{\operatorname{wt}(P_Ux)\bmod 4})H^{\otimes m}$ change along each edge by a product of translation kernels $aI+bX_v$, one per vector of an orthonormal basis of the edge residual, for $s<W m$ kernels in all, and telescope to $C^{\otimes m}$ on every role.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Normalized convolution over the ring](synthetic-convolution.md)
- [Resampling with permutations left in the transform](resampling-without-sorting.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Fast interchange of address chunks](fast-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [The multiplication algorithm](multiplication-algorithm.md): Digit extraction, the Chinese-remainder map, two forward source transforms, pointwise product, opposite transform, rescaling, rounding and carry propagation yielding the exact 2n-bit product.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The multiplication algorithm
- [Parameter choice and cost table](parameter-choice.md): Fixed rational exponents (τ=σ=1−2^{−50}, ε=2^{−75}, κ=2^{−182}, …) and sizes p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log₂T/d⌉} making every cost term a power of p below one.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* Parameter choice and cost table
- [The n log n conjecture and prior bounds](nlogn-conjecture.md): Schönhage–Strassen's 1971 bound O(n log n log log n), their conjecture that n log n is optimal, and Harvey–van der Hoeven's O(n log n) upper bound for multitape machines.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The n log n conjecture and prior bounds
- [The established O(N log N) multiplier](nlogn-multiplier.md): The Harvey–van der Hoeven fixed-tape multiplier with cost O(N log 2N) on N-bit inputs, used only as an ordinary subroutine on short inputs.
  Shown as: Integer multiplication in O(n (lg n)^(1−κ)) time *<predicate>* The established O(N log N) multiplier

## Other pages you may link to

- [Linear network with restored scratch wires](linear-network.md)
- [Frames on wire arrays](frames.md)
- [Arrays as tape streams and elementary scans](tape-streams.md)
- [Fixed-point and Gaussian dyadic arithmetic](fixed-point-dyadics.md)
- [Controlled shifts and rational scalings](controlled-shift.md)
- [Subspaces, bilinear forms and orthogonal complements](linear-algebra-orthogonality.md)
- [Triple-subset intersection gadgets](triple-subset-gadgets.md)
- [Nested subspace labels and the rank deficit](rank-deficit-labels.md)
- [Recursive power saving from the rank deficit](recursive-power-saving.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Matrix shear on address fields](matrix-shear.md)
- [Fast interchange of address chunks](fast-chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Polynomial ring modulo y^r + 1](ring-mod-y-r-plus-1.md)
- [Discrete Fourier transform](dft.md)
- [Two-point butterfly layer](two-point-butterfly.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multiplication as convolution of radix digits](multiplication-as-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Error bounds and exact recovery](error-and-exact-recovery.md)
- [Last-coordinate phase twist](phase-twist.md)
- [Binary phase frames and the two-point kernel C](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Synthetic transform tape layout](synthetic-transform-layout.md)
- [Signed packing for ring products](kronecker-packing.md)
- [Normalized convolution over the ring](synthetic-convolution.md)
- [Resampling with permutations left in the transform](resampling-without-sorting.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Chinese-remainder address map](crt-address-map.md)

## Evidence from the sources, with the paragraph around each quote

- "T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}

- "There is one deterministic Turing machine $A$, with a fixed finite" (paper)

  > \begin{theorem}\label{thm:main} There is one deterministic Turing machine $A$, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every $n\ge1$ and every pair of $n$-bit inputs. Its worst-case running time satisfies \[ T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right), \qquad \kappa=2^{-182}. \] \end{theorem}


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

Write the body to `exegenius/tasks/0039-write-main-theorem.answer.md` and the JSON to `exegenius/tasks/0039-write-main-theorem.answer.json`, then run `exegenius submit 0039-write-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0039-write-main-theorem`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
