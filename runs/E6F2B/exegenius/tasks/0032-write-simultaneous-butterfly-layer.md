# exegenius task 0032-write-simultaneous-butterfly-layer

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F2B` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: fluent in asymptotic analysis, discrete mathematics (sets, functions, modular arithmetic, primes and gcd, permutations, induction and recursion), first-course linear algebra (matrices, invertibility, rank, basis, dimension, linear maps over the rationals and the complex numbers), complex arithmetic with Euler's formula, and the basic Turing machine model with tapes and step counting. They have seen binary representation, bit operations such as XOR, and perhaps the idea of multiplying integers by divide and conquer, but have not been taught the discrete Fourier transform, the FFT, polynomial transforms, Schönhage–Strassen, abstract ring theory beyond the basic definition, tensor products, or numerical error analysis, and these are what the wiki must explain.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- The n log n optimality conjecture
- Fixed finite-tape Turing machine model
- Arrays, address fields and elementary scans
- Controlled cyclic shifts and rational scalings
- Integer multiplication as digit convolution
- Normalized DFT and cyclic convolution
- Multidimensional (tensor) Fourier transform
- Chinese-remainder map to prime cyclic axes
- Gaussian resampling
- Fixed-point disk-grid arithmetic and contractions
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): the formal variable of the polynomials, subject to y^r = -1.
  - $r$ (record length): the number of complex coefficients in a polynomial record, a power of two.
- Synthetic Fourier transform modulo y^r + 1
  - $y$ (ring variable): the formal variable of the polynomial ring, subject to y^r = -1.
  - $r$ (record length): the number of complex coefficients in a polynomial record, a power of two.
- Radix-2 butterfly layers and stored frequency order
- Twist from cyclic to negacyclic convolution
- Established n log n multiplier as a subroutine
- Signed Kronecker packing of polynomial products
- Bluestein's chirp identity
- Three-element subset intersection gadget
- Linear network that exchanges two banks and restores scratch values
- Frames and the common-frame identity
- Orthogonal complements and projections in a bilinear space
- Nested subspace labels and the rank saving
- Lower-triangular rank factorization
- Cost of a rational matrix shear
- Power-width chunk interchange in O(Ve^τ) time
  - $V$ (stored bit volume): the number of data bits stored in the array.
  - $e$ (chunk width): the number of radix digits in each of the two interchanged chunks, a power of a fixed integer m.
  - $\tau$ (interchange exponent): a fixed rational constant strictly between 0 and 1.
- Chunk interchange in O(Vu^τ) time
  - $V$ (stored bit volume): the number of data bits stored in the array.
  - $u$ (chunk width): the number of bits in each of the two interchanged address chunks.
  - $\tau$ (interchange exponent): a fixed rational constant strictly below 1, namely 1 - 2^{-50}.
- Two-point kernel C and the complex phase network
- Packed XOR of selected bits across address chunks
- Modular arithmetic and residues (also: congruence, mod q, Z/qZ, integers modulo q, remainder)
- Primes, divisibility, gcd and coprimality (also: prime number, coprime, relatively prime, pairwise coprime, greatest common divisor, odd prime, units mod q, invertible residue)
- Binary representation of integers (also: bit string, radix 2, binary expansion, most significant bit, val(x), bin_k(z), padding with zeros, base-2 digits)
- Bitwise XOR (also: exclusive or, XOR combination, addition mod 2, parity)
- Logarithms, floors, ceilings and powers of two (also: lg, log base 2, floor, ceiling, power of two, exponent rules)
- Matrices, invertibility and rank (also: invertible matrix, matrix inverse, matrix product, rank of a matrix, linear map, linear transformation, Gaussian elimination, row operations)
- Vector spaces, basis and dimension (also: subspace, span, linear independence, linear combination, vector space over the rationals, dimension, standard basis, direct sum)
- Permutations and permutation matrices (also: bijection, reordering of indices, sorting by a permutation, permutation of coordinates, identity matrix)
- Lexicographic order and index tuples (also: dictionary order, Cartesian product of index sets, multi-index, mixed-radix positional notation, row-major order)
- Euler's formula and roots of unity as points on the unit circle (also: e^{i theta}, cos and sin form, unit circle, primitive root of unity, modulus of a complex number, complex conjugate, real and imaginary parts)
- Geometric series and orthogonality of sums of roots of unity (also: geometric sum, sum of powers of a root of unity vanishes, summation manipulation, Kronecker delta, indicator function)
- Norms and the triangle inequality (also: absolute value bound, sup norm, maximum norm, Euclidean norm, error bound, triangle inequality, operator norm)
- Rational numbers, dyadic rationals and exact arithmetic (also: dyadic number, dyadic rational, power-of-two denominator, Gaussian rational, Gaussian integer, rounding to nearest integer, truncation toward zero)
- Algebraic structures: groups, rings and isomorphisms (also: ring, commutative ring, algebra, ring isomorphism, group, cyclic group, zero divisor, unit, field)
- Discrete-math proof techniques (also: induction, recursion, recurrence relation, divide and conquer, proof by cases, pigeonhole principle, counting arguments)
- Schoolbook multiplication and divide-and-conquer multiplication (also: long multiplication, quadratic-time multiplication, Karatsuba, carry propagation, digit-by-digit addition)
- Multitape machine cost model and linear-time scans (also: sequential tape access, tape scan, head movement cost, one-pass copy, linear-time tape operations, sorting by merging, bit-level time complexity)
- Complex polynomial evaluation and interpolation (also: evaluating a polynomial at points, coefficient list, degree, polynomial identity, Horner's rule, coefficient extraction)
- Gaussian function (also: bell curve, exp(-x^2), normal density, Gaussian weight)
- Convolution as polynomial multiplication (also: convolution of sequences, sum over i+j=k, linear convolution, Cauchy product, coefficient of a product)
- Quantifiers, sets and basic asymptotic notation beyond big-O (also: little-o, Theta, Omega, sufficiently large n, for all n, worst-case time, lower bound versus upper bound)

## This page

Concept: Simultaneous butterfly layer in O(Vd^λ') time
Gloss: Applies the normalized butterfly H₀ to one bit position in each of d address chunks of polynomial records in one pass, exactly in Gaussian dyadics followed by a single truncation, in O(V d^λ') for a fixed λ' < 1 instead of d whole-array passes.
Heading: Simultaneous butterfly layer in $O(Vd^{\lambda'})$ time

The symbols in this page's heading denote (say so on the page):

- $V$ (stored bit volume): the number of data bits stored in the array of records.
- $d$ (axis count): the number of equal-width address chunks (transform axes) whose selected bit is butterflied simultaneously.
- $\lambda'$ (layer exponent): a fixed rational constant strictly below 1, namely 1 - 2^{-54}.

## This page in the argument

The step: One normalized butterfly $H_0$ applied to the same bit position in each of $d$ address chunks of polynomial records is computed exactly, then truncated once, in $O(Vd^{\lambda'})$ time for a fixed $\lambda'<1$.
How: Express the tensor of $H_0$ through the two-point kernel $C$, evaluate $C^{\otimes e}$ by the complex bank-exchange network whose child calls act on $e/m$ axes, implement the binary basis changes with packed XORs of selected bits, and bound the intermediate dyadic widths.
Why: Doing the $d$ butterfly factors separately needs $d$ whole-array passes; the network recursion replaces them by a recursion whose per-volume cost grows only like $d^{\lambda'}$. (the sources say so: "factors would require $D$ whole-array passes." (paper))
Striking feature: The layer on $d$ axes costs $O(Vd^{\lambda'})$ with $\lambda'<1$, strictly less than the $d$ passes of separate butterflies, for the same reason as the chunk interchange: $s_{\rm c}/W_{\rm c}<m^\sigma$ with $\sigma<1$. (explain why it holds, from the method)

Its sub-steps, in order:

- Applying the complex network with column frames to $e=mf$ selected axes needs exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and yields $C^{\otimes e}$ on every role.
- The normalized layer is recovered from the $C$ layer by exact diagonal phases: $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$.
- Row addition $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ on the selected bit of each of $f$ chunks costs $O(V(L^\tau+1))$ using a third chunk as restored temporary space. (on [Packed XOR of selected bits across address chunks](packed-selected-bits.md))
- With the row split giving each child $1/W_{\rm c}$ of the parent's volume, the recurrence and packed basis changes give total time $O(Vd^{\lambda'})$ on fixed tapes.
- Intermediate coefficients are exact Gaussian dyadics whose denominator and magnitude growth is bounded by $\lceil C_0d^{C_1}\rceil$, which is $o(p)$, so the width stays $O(p)$.
- Every row of $\mathcal H$ has absolute row sum one, so the layer maps the disk to the disk and the single final truncation $Q_p$ has error below $\sqrt2\,2^{-p}$.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ worst-case time with $\kappa=2^{-182}$.; how: Start from the Gaussian-resampling reduction of integer multiplication to convolution; replace the two costly operations of the synthetic transforms (address rearrangement and butterfly layers) by faster procedures built from one recursive linear-network exchange, assemble the exact algorithm, and account for its cost. (on [Multiplying n-bit integers in O(n (lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.1, S4.2, S4.4, S4.5, S4.6). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.1**: Applying the complex network with column frames to $e=mf$ selected axes needs exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot, and yields $C^{\otimes e}$ on every role.
Source: "$s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot." (paper)
> \paragraph{The exact recursive contract.} Apply the finite network with these column frames to a group of $e=mf$ selected axes. Summing its residual dimensions gives exactly $s_{\rm c}$ child calls, each on the $f=e/m$ axes of one slot. The source and sink $Z_{a,f}$ signs, together with the scalar $i^{27f}$ at each affected sink, turn every endpoint kernel into a forward one. Negating the prescribed physical bank and undoing its exchange returns each result to its original role. Proposition~\ref{prop:complex-motif-interface} therefore gives $C^{\otimes e}$ on every role, including roles whose initial scratch values were arbitrary. Formula~\eqref{eq:phase-inverse-child} supplies each inverse child from one forward call, and none of the corrections adds a child. The remaining operations are a fixed number of binary row additions and coefficientwise scalar operations.

**S4.2**: The normalized layer is recovered from the $C$ layer by exact diagonal phases: $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$.
Source: "H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D." (paper)
> \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

**S4.4**: With the row split giving each child $1/W_{\rm c}$ of the parent's volume, the recurrence and packed basis changes give total time $O(Vd^{\lambda'})$ on fixed tapes.
Source: "give total time $O(Vd^{\lambda'})$ on fixed tapes, including" (paper)
> Uniformly for large $p$, the bands give $f\le d\le p$ and \[ K\ge\tfrac12a_d^c p^{\epsilon c},\qquad r\ge2^{(a_r/b_d)p^{1-\epsilon}}. \] The first inequality follows from $K=\lfloor d^c\rfloor$ once $d^c\ge2$. In particular, $K\ge6$ and $K/\log p\to\infty$, while $r$ dominates every fixed polynomial. Substituting the common bound $A_*\le C_Ap$ into the two additional normalized terms in \eqref{eq:packed-rectangle-time} gives \[ \begin{aligned} \frac{A_*^3}{R_{\rm g}} &\le\frac{C_A^3p^2}{2r},\\ 80(f-1)2^{-K}A_*\left(1+\frac{A_*}{R_{\rm g}}\right) &\le80C_Ap^2 2^{-K}\left(1+\frac{C_A}{2r}\right). \end{aligned} \] Both bounds tend to zero uniformly over all current allowed $d,r$. Thus Lemma~\ref{lem:packed-selected-bit-rectangle} has the required $O(M_{\rm child}R_{\rm g}(L^\tau+1))$ cost for every packed call, with one common time constant. The row construction and the recurrence analysis above give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams. Equation~\eqref{eq:phase-butterfly-layer} converts the resulting exact $C$-layer to $\mathcal H$.

**S4.5**: Intermediate coefficients are exact Gaussian dyadics whose denominator and magnitude growth is bounded by $\lceil C_0d^{C_1}\rceil$, which is $o(p)$, so the width stays $O(p)$.
Source: "The guard-width calculation above bounds both denominator and magnitude" (paper)
> The guard-width calculation above bounds both denominator and magnitude growth by $\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, this is $o(p)$ uniformly over the allowed $d$, so every intermediate coefficient is represented exactly with the stated $O(p)$ width. The initial scan removes or adds only redundant leading sign bits and appends the reserved fractional zeros to put each supplied component in this guarded format. To truncate toward zero at the end, shift its absolute numerator right by the number of added fractional bits, restore its sign, and write the result in $w$ bits. These scans cost $O(V)$. Finally, every row of $\mathcal H$ has absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation preserves that disk and has error less than $\sqrt2\,2^{-p}$: truncation cannot increase the absolute value of either component, and changes each by less than $2^{-p}$. The truncated numerators have magnitude at most $2^p$, so the supplied component width can hold them. \end{proof} \section{Synthetic transforms and their tape layout} \label{sec:synthetic-layouts}

**S4.6**: Every row of $\mathcal H$ has absolute row sum one, so the layer maps the disk to the disk and the single final truncation $Q_p$ has error below $\sqrt2\,2^{-p}$.
Source: "Finally, every row of $\mathcal H$ has" (paper)
> The guard-width calculation above bounds both denominator and magnitude growth by $\lceil C_0d^{C_1}\rceil$. Since $d\le b_dp^\epsilon$ and $\epsilon C_1<1$, this is $o(p)$ uniformly over the allowed $d$, so every intermediate coefficient is represented exactly with the stated $O(p)$ width. The initial scan removes or adds only redundant leading sign bits and appends the reserved fractional zeros to put each supplied component in this guarded format. To truncate toward zero at the end, shift its absolute numerator right by the number of added fractional bits, restore its sign, and write the result in $w$ bits. These scans cost $O(V)$. Finally, every row of $\mathcal H$ has absolute row sum one. Thus $\mathcal H$ maps disk arrays to disk arrays, and componentwise truncation preserves that disk and has error less than $\sqrt2\,2^{-p}$: truncation cannot increase the absolute value of either component, and changes each by less than $2^{-p}$. The truncated numerators have magnitude at most $2^p$, so the supplied component width can hold them. \end{proof} \section{Synthetic transforms and their tape layout} \label{sec:synthetic-layouts}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S4.3 (on [Packed XOR of selected bits across address chunks](packed-selected-bits.md)): Row addition $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ on the selected bit of each of $f$ chunks costs $O(V(L^\tau+1))$ using a third chunk as restored temporary space.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Frames and the common-frame identity](frames.md)
- [Chunk interchange in O(Vu^τ) time](chunk-swap.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Two-point kernel C and the complex phase network](phase-kernel-network.md): The Gaussian-dyadic two-point kernel C = H S H = aI + bX (a = (1+i)/2, b = (1−i)/2) satisfies H₀ = b S C S; the complex bank-exchange network with binary labels makes C^{⊗m} on every role from products of translation kernels, one per residual basis vector.
  Shown as: Simultaneous butterfly layer in O(Vd^λ') time *<predicate>* Two-point kernel C and the complex phase network
- [Packed XOR of selected bits across address chunks](packed-selected-bits.md): A binary row addition y ← y ⊕ x on the selected bit of each of f chunks at once, done by a constant number of cyclic shifts of whole chunk ranges followed by deterministic repair of a small explicit set of bad addresses, using a third chunk as restored temporary space.
  Shown as: Simultaneous butterfly layer in O(Vd^λ') time *<predicate>* Packed XOR of selected bits across address chunks
- [Fixed-point disk-grid arithmetic and contractions](fixed-point-disk-grid.md): Complex numbers stored as signed two's-complement integers scaled by 2^{-p} inside the unit disk; truncation Q_p toward zero costs error below √2·2^{-p}, and contractions never increase the sup norm so errors add up predictably.
  Shown as: Simultaneous butterfly layer in O(Vd^λ') time *<predicate>* Fixed-point disk-grid arithmetic and contractions
- [Radix-2 butterfly layers and stored frequency order](butterfly-layers.md): Decimation in frequency: each level combines entries k and k+t/2 by the two-point butterfly H₀ and a twiddle monomial, leaving frequencies stored in bit-reversed order, which the opposite transform consumes directly.
  Shown as: Simultaneous butterfly layer in O(Vd^λ') time *<predicate>* Radix-2 butterfly layers and stored frequency order
- [Power-width chunk interchange in O(Ve^τ) time](power-width-interchange.md): Recursively interchanges two chunks of e = m^k digits by running the bank-exchange network on W role streams of volume V/W, each edge costing rank-many smaller interchanges; since s/W < m^τ the cost per volume is O(e^τ).
  Shown as: Simultaneous butterfly layer in O(Vd^λ') time *<predicate>* Power-width chunk interchange in O(Ve^τ) time

## Pages that build on this one

- Layout and cost of the synthetic transform: A positional layout permutation puts the selected bits of all axes at a common offset in K-bit chunks so each transform round is one simultaneous layer; the forward transform keeps its output order for the pointwise product and the opposite transform.
- Cost accounting and the saving exponent κ: A table of costs divided by Tp, each at most p^{1−2κ} thanks to the slack in the chosen exponents (seven dominant margins, the smallest 2^{-181} = 2κ), giving O(n (log n)^{1−κ}) overall.

## Other pages you may link to

- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Integer multiplication as digit convolution](radix-digit-convolution.md)
- [Three-element subset intersection gadget](triple-gadget.md)
- [Linear network that exchanges two banks and restores scratch values](bank-exchange-network.md)
- [Fixed finite-tape Turing machine model](fixed-tape-model.md)
- [Established n log n multiplier as a subroutine](nlogn-subroutine.md)
- [Arrays, address fields and elementary scans](stream-arrays.md)
- [Frames and the common-frame identity](frames.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Orthogonal complements and projections in a bilinear space](bilinear-orthogonal.md)
- [Nested subspace labels and the rank saving](subspace-labels.md)
- [Lower-triangular rank factorization](triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear.md)
- [Chunk interchange in O(Vu^τ) time](chunk-swap.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Signed Kronecker packing of polynomial products](signed-kronecker-packing.md)
- [Normalized DFT and cyclic convolution](dft-cyclic-convolution.md)
- [Multidimensional (tensor) Fourier transform](multidim-transform.md)
- [Chinese-remainder map to prime cyclic axes](crt-axis-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Twist from cyclic to negacyclic convolution](coefficient-twist.md)
- [Synthetic Fourier transform modulo y^r + 1](synthetic-transform.md)
- [Layout and cost of the synthetic transform](transform-layout.md)
- [Convolution over the polynomial ring from the retained layout](ring-convolution.md)
- [Resampling with the permutations left in the transform](resampling-no-sort.md)
- [Chirp identity and source-permutation cancellation](chirp-permutation-cancel.md)
- [Choice of sizes, precision and prime axis lengths](parameter-choice.md)
- [Source transform via resampling, chirp and ring convolution](source-transform.md)
- [Exact recovery: scaling, rounding and carries](exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the saving exponent κ](cost-accounting.md)
- [Multiplying n-bit integers in O(n (lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "coefficient order, and component format in $O(Vd^{\lambda'})$ time" (paper)

  > The procedure returns $Q_p(\mathcal H z)$ in the same array, coefficient order, and component format in $O(Vd^{\lambda'})$ time, uniformly over all these choices of $p,d,r,D,P,S,\rho,w$ and $z$. Every returned coefficient belongs to the complex unit disk, and, in the maximum coefficient norm, \[ \|Q_p(\mathcal H z)-\mathcal H z\|_\infty <\sqrt2\,2^{-p}. \] The procedure evaluates the entire layer exactly before this final truncation. Put \[ C_0=128m\bigl(s_{\rm c}+64(W_{\rm c}+m+1)^3\bigr)^2, \] where $m,W_{\rm c},s_{\rm c}$ are the fixed constants of Proposition~\ref{prop:complex-motif-interface}. The procedure uses at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits and $\lceil C_0d^{C_1}\rceil+3$ integer and sign bits per real component internally; these widths are $O(p)$. The time includes address changes, deterministic repair, row padding and its removal, and fixed-tape workspace cleanup. Its tape count is fixed, and its time constant is independent of the allowed array lengths and coefficient values. \end{proposition}

- "whereas separate butterfly factors would require $D$ whole-array passes" (paper)

  > The parameters will satisfy \[ d=\Theta(p^\epsilon),\qquad K=\lfloor d^c\rfloor, \qquad r=2^{\Theta(p/d)},\qquad c>0,\quad 0<\epsilon<1. \] The exponents and comparison constants are fixed, and we impose their further restrictions in Proposition~\ref{prop:simultaneous-layer}. Two consequences explain the layout. The polynomial length $r$ grows faster than every fixed power of $p$, so a scan of a record pays for polynomial work on its address. Also $K/\log p\to\infty$, which will make the exceptional set in a packed change of address bits small enough to repair by sorting. We will obtain cost $O(Vd^{\lambda'})$, with $\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly factors would require $D$ whole-array passes.

- "The procedure evaluates the entire layer exactly before this final truncation." (paper)

  > The procedure returns $Q_p(\mathcal H z)$ in the same array, coefficient order, and component format in $O(Vd^{\lambda'})$ time, uniformly over all these choices of $p,d,r,D,P,S,\rho,w$ and $z$. Every returned coefficient belongs to the complex unit disk, and, in the maximum coefficient norm, \[ \|Q_p(\mathcal H z)-\mathcal H z\|_\infty <\sqrt2\,2^{-p}. \] The procedure evaluates the entire layer exactly before this final truncation. Put \[ C_0=128m\bigl(s_{\rm c}+64(W_{\rm c}+m+1)^3\bigr)^2, \] where $m,W_{\rm c},s_{\rm c}$ are the fixed constants of Proposition~\ref{prop:complex-motif-interface}. The procedure uses at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits and $\lceil C_0d^{C_1}\rceil+3$ integer and sign bits per real component internally; these widths are $O(p)$. The time includes address changes, deterministic repair, row padding and its removal, and fixed-tape workspace cleanup. Its tape count is fixed, and its time constant is independent of the allowed array lengths and coefficient values. \end{proposition}


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

Write the body to `exegenius/tasks/0032-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0032-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0032-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0032-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
