# exegenius task 0028-write-simultaneous-butterfly-layer

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N4` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science degree: discrete mathematics (sets, permutations, binomial coefficients, induction, modular arithmetic, gcd and the extended Euclidean algorithm, primes), an introductory linear algebra course (vectors, matrices, subspaces, dimension, eigenvalues, the standard dot product and orthogonality over the reals), single-variable calculus (limits, logarithms, exponentials, geometric series, Newton's method), and the standard algorithms and theory courses (asymptotic notation, recurrences, divide-and-conquer such as Karatsuba, amortized binary counters, basic Turing machines). They know binary representation, fixed-width binary arithmetic with carries, and complex numbers including roots of unity, but have not studied the FFT literature in depth, abstract algebra beyond modular arithmetic, tensor products, general bilinear forms, numerical error analysis, or the integer-multiplication research line beyond Karatsuba.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine (also: fixed finite-tape model)
- Linear maps and matrix rank (also: rational rank)
- Tensor products
- Nondegenerate bilinear forms (also: orthogonal complement)
- n log n optimality conjecture (also: Schönhage–Strassen conjecture)
  - $n$ (input bit length): The number of bits in each of the two integers being multiplied.
  - $\log$ (logarithm): The logarithm function, so n log n is the conjectured optimal growth rate.
- Harvey–van der Hoeven multiplier
- Arrays on tape and elementary stream operations (also: logical volume)
- Controlled shifts
- Fixed-point approximation and error accounting (also: disk grid, precision p)
- Polynomial ring ℂ[y]/(yʳ+1)
  - $\mathbb C$ (complex numbers): The field of complex numbers from which the coefficients are taken.
  - $y$ (ring variable): The polynomial indeterminate, whose r-th power equals −1 in the ring.
  - $r$ (record length): The number of complex coefficients in each polynomial record, a power of two.
- Normalized butterfly H₀
  - $H_0$ (normalized butterfly): The two-point linear map sending (u,v) to ((u+v)/2,(u−v)/2).
- Gaussian dyadic numbers
- Linear network with wire roles (also: role, bank exchange)
- Restoration of scratch values (also: transparent computation)
- Three-element subset construction (also: gather and scatter, side wires)
- Frames and the common-frame identity
- Subspace labels and orthogonal residuals
- Rank saving s < Wm
  - $s$ (smaller call count): The total number of smaller recursive calls, the sum of edge ranks or residual dimensions over all network edges.
  - $W$ (wire count): The number of wires (roles) in the finite network, including scratch wires.
  - $m$ (label dimension): The dimension of the ambient label space, equal to the number of sub-fields a parameter is split into per recursion level.
- Recursive power saving
- Address shear
- Lower triangular factorization (also: Bruhat factorization)
- Rational matrix interface
- Fast address-chunk interchange (also: chunk swap)
- Binary phase interface (also: phase frames)
- Packed selected-bit addition
- Big-Omega and Big-Theta notation (also: Ω, Θ, Omega notation, Theta notation, asymptotic lower bound, tight bound)
- Worst-case running time (also: worst-case time, time complexity, T_A(n), bit complexity)
- Deterministic algorithm (also: deterministic machine, deterministic Turing machine)
- Logarithms (also: log, lg, log_2, binary logarithm, natural logarithm, ln)
- Iterated logarithm (also: log*, log-star, log^* n)
- Floor and ceiling (also: ⌊x⌋, ⌈x⌉, integer part, rounding down, rounding up)
- Limits and lim inf (also: limit, liminf, limit inferior, tends to zero, asymptotic)
- Geometric series (also: geometric sum, geometrically increasing, geometric progression)
- Recurrence relations (also: recurrence, divide-and-conquer recurrence, master theorem, recursive cost bound)
- Mathematical induction (also: induction, proof by induction, inductive argument)
- Binary representation (also: binary, bit string, bits, most significant bit, least significant bit, binary expansion, radix-2)
- Positional radix representation (also: base-q digits, radix, radix-q digit, digits in base b, mixed radix)
- Binary addition with carries (also: carry propagation, carries, schoolbook addition, ripple-carry addition)
- Signed binary numbers and fixed-point numbers (also: two's complement, signed integers, fixed-point binary, fractional bits, guard bits, truncation)
- Schoolbook multiplication (also: long multiplication, grade-school multiplication, quadratic multiplication)
- Karatsuba multiplication (also: Karatsuba's algorithm, Karatsuba–Ofman, n^{log₂ 3} multiplication)
- Integer division with remainder (also: quotient and remainder, Euclidean division, floor division, a mod b)
- Modular arithmetic (also: congruence, mod, residues modulo Q, pmod, residue ring, integers modulo n, ℤ/nℤ, cyclic shift modulo)
- Greatest common divisor and coprimality (also: gcd, coprime, relatively prime, prime to q, pairwise coprime)
- Extended Euclidean algorithm (also: Euclid's algorithm, modular inverse, Bézout coefficients, inverse modulo Q)
- Chinese remainder theorem (also: CRT, Chinese remaindering)
- Prime numbers (also: prime, primes, distinct primes, prime length)
- Binomial coefficients (also: n choose k, C(n,k), binom, k-element subsets)
- Sets, Cartesian products and indicator vectors (also: Cartesian product, product set, indicator vector, characteristic vector, intersection size, |S ∩ T|)
- Permutations and bijections (also: permutation, bijection, one-to-one correspondence, inverse permutation, reordering)
- Lexicographic order (also: lexicographical order, dictionary order, row-major order)
- Exclusive or (also: XOR, addition modulo 2, ⊕, bitwise XOR)
- The two-element field (also: F_2, 𝔽₂, GF(2), binary field, arithmetic modulo 2)
- Rational numbers and integers (also: ℚ, ℤ, rationals, dyadic rational, power-of-two denominator)
- Vector spaces and subspaces (also: vector space, subspace, linear subspace, span, ⟨v⟩, line spanned by)
- Linear independence, basis and dimension (also: basis, dimension, dim, linearly independent)
- Linear combinations and linear maps (also: linear combination, linear map, linear operator, linearity, linear transformation)
- Matrices and matrix multiplication (also: matrix, matrix product, identity matrix, I, all-ones matrix, J, row, column)
- Invertible matrices (also: invertible, inverse matrix, nonsingular, singular matrix)
- Triangular and diagonal matrices (also: lower triangular, upper triangular, diagonal matrix, unit triangular)
- Permutation matrices (also: permutation matrix, partial permutation matrix)
- Matrix transpose (also: transpose, A^T, transposition, row-major to column-major)
- Eigenvalues and eigenvectors (also: eigenvalue, eigenvector, spectrum)
- Dot product and orthogonality (also: inner product, scalar product, orthogonal, perpendicular, x^T y)
- Kernel and image (also: null space, range, column space, rank–nullity)
- Roots of unity (also: root of unity, primitive root of unity, e^{2πi/q}, ω, ζ, q-th root of unity)
- Gaussian function (also: Gaussian, e^{-x^2}, bell curve, normal density)
- Absolute value and triangle inequality (also: modulus bound, |a+b| ≤ |a|+|b|, error bound, unit disk)
- Rounding to the nearest integer (also: round, rounding, nearest integer)
- Newton's method (also: Newton iteration, Newton–Raphson, Newton reduction)
- Integer square root (also: ⌊√a⌋, isqrt, floor of square root)
- Binary counter and amortized increment cost (also: binary counter, ripple counter, amortized analysis, counter increment)
- Stack (also: push, pop, LIFO)
- Tape alphabet, tracks and constant-factor simulation (also: tape alphabet, tracks, work tape, head, scan, finite control, alphabet enlargement)
- Pointwise operations (also: pointwise product, componentwise, entrywise, coordinatewise, Hadamard product)
- Polynomial multiplication as convolution (also: convolution, coefficient convolution, acyclic convolution, product of coefficient lists)
- Polynomial evaluation and interpolation (also: interpolation, evaluation at points, Lagrange interpolation, Toom–Cook)

## This page

Concept: Simultaneous butterfly layer
Gloss: The second tape procedure: applying H₀ at the same bit position of up to d address chunks at once in O(V d^{λ'}) time with λ' < 1, computed exactly in Gaussian dyadics and truncated once.

## This page in the argument

The step: Applying $H_0$ at the same bit position of $D\le d$ address chunks of polynomial records costs $O(Vd^{\lambda'})$ with $\lambda'<1$, with error below $\sqrt2\,2^{-p}$.
How: write $H_0^{\otimes D}$ as phase wrappers around $C^{\otimes D}$, run the complex network recursively with binary basis changes done by packed selected-bit additions, bound the dyadic growth, and truncate once
Why: The complex network's endpoint is $C^{\otimes m}$ and its edges are products of two-point kernels on fewer selected bits, so the rank saving applies once $C$ is converted to $H_0$ by exact phases. (the sources leave this for the reader to work out: spell it out)
Striking feature: All $D$ butterfly factors together cost less than $D$ separate passes, by a power $d^{\lambda'}$ with $\lambda'<1$. (explain why it holds, from the method)

Its sub-steps, in order:

- Exact Gaussian dyadic phases convert the $C$ layer into the normalized butterfly layer: $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$.
- Binary row additions of selected bits across chunks are done by a constant number of whole-chunk cyclic shifts and moves followed by deterministic repair of a bounded exceptional set. (on [Packed selected-bit addition](packed-selected-bit-addition.md))
- The $s$ child calls on volume $V/W$ give $F(e)\le(s/W)F(e/m)+O((eK)^{\tau}+1)$, which unrolls to $O(d^{\lambda'})$.
- Explicit guard widths bound denominator and magnitude growth of the exact intermediate values within one layer.
- The procedure returns the truncated layer $Q_p(\mathcal Hz)$ in $O(Vd^{\lambda'})$ time.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine computes the exact product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: reduce multiplication through radix digits, a CRT address map, Gaussian resampling and a coefficient twist to convolution over $\mathbb C[y]/(y^r+1)$, accelerate its address moves and butterfly layers with two tape procedures derived from finite linear networks with a rank saving, recover the product exactly, and balance the parameters (on [Integer multiplication in O(n(lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S3.1, S3.3, S3.4, S3.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S3.1**: Exact Gaussian dyadic phases convert the $C$ layer into the normalized butterfly layer: $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$.
Source: "H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D." (paper)
> \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

**S3.3**: The $s$ child calls on volume $V/W$ give $F(e)\le(s/W)F(e/m)+O((eK)^{\tau}+1)$, which unrolls to $O(d^{\lambda'})$.
Source: "Dividing by
the current volume \(V\) gives the factor \(s/W\)." (paper)
> \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).

**S3.4**: Explicit guard widths bound denominator and magnitude growth of the exact intermediate values within one layer.
Source: "We now give explicit constants that bound
denominator and magnitude growth within one layer." (paper)
> The accelerated network is evaluated exactly until an entire normalized butterfly layer is complete. Its intermediate operators need not be contractions. We now give explicit constants that bound denominator and magnitude growth within one layer.

**S3.5**: The procedure returns the truncated layer $Q_p(\mathcal Hz)$ in $O(Vd^{\lambda'})$ time.
Source: "coefficient order, and component format in $O(Vd^{\lambda'})$ time," (paper)
> The procedure returns $Q_p(\mathcal H z)$ in the same array, coefficient order, and component format in $O(Vd^{\lambda'})$ time, uniformly over all these choices of $p,d,r,D,P,S,\rho,w$ and $z$. Every returned coefficient belongs to the complex unit disk, and, in the maximum coefficient norm, \[ \|Q_p(\mathcal H z)-\mathcal H z\|_\infty <\sqrt2\,2^{-p}. \] The procedure evaluates the entire layer exactly before this final truncation. Put \[ C_0=128m\bigl(s_{\rm c}+64(W_{\rm c}+m+1)^3\bigr)^2, \] where $m,W_{\rm c},s_{\rm c}$ are the fixed constants of Proposition~\ref{prop:complex-motif-interface}. The procedure uses at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits and $\lceil C_0d^{C_1}\rceil+3$ integer and sign bits per real component internally; these widths are $O(p)$. The time includes address changes, deterministic repair, row padding and its removal, and fixed-tape workspace cleanup. Its tape count is fixed, and its time constant is independent of the allowed array lengths and coefficient values. \end{proposition}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S3.2 (on [Packed selected-bit addition](packed-selected-bit-addition.md)): Binary row additions of selected bits across chunks are done by a constant number of whole-chunk cyclic shifts and moves followed by deterministic repair of a bounded exceptional set.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Normalized butterfly H₀](butterfly-h0.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Binary phase interface](binary-phase-interface.md): The complex network over Gaussian dyadics with binary labels, whose edge frames are products of two-point kernels C = HSH and whose endpoints telescope to a tensor power of C, convertible to the H₀ layer.
  Shown as: Simultaneous butterfly layer *<predicate>* Binary phase interface
- [Packed selected-bit addition](packed-selected-bit-addition.md): Changing selected address bits in several chunks at once by whole-chunk cyclic shifts and moves, followed by a deterministic repair of an explicitly bounded set of exceptional addresses.
  Shown as: Simultaneous butterfly layer *<predicate>* Packed selected-bit addition
- [Recursive power saving](recursive-power-saving.md): Splitting the work into s calls each on volume V/W gives the normalized recurrence F_k ≤ (s/W)F_{k−1} + O(1), and s/W < m^τ with τ < 1 yields cost O(V e^τ) instead of O(V e).
  Shown as: Simultaneous butterfly layer *<predicate>* Recursive power saving
- [Fast address-chunk interchange](chunk-interchange.md): The first tape procedure: exchanging two disjoint u-bit address fields of an array in O(V u^τ) time with τ < 1, by recursively running the bit network with shears as edge frames.
  Shown as: Simultaneous butterfly layer *<predicate>* Fast address-chunk interchange
- [Fixed-point approximation and error accounting](fixed-point-approximation.md): Complex values are stored on the grid 2^{-p}(ℤ+iℤ) in the unit disk, truncated toward zero, and errors of approximate contractions add when composed.
  Shown as: Simultaneous butterfly layer *<predicate>* Fixed-point approximation and error accounting

## Pages that build on this one

- Convolution over the polynomial ring: Normalized cyclic convolution of arrays over ℂ[y]/(y^r+1) computed by two forward synthetic transforms on a tape layout using chunk interchanges and simultaneous layers, packed pointwise products, and the opposite transform.
- Parameter choice and cost balance: Fixed rational exponents (τ, λ′, c, ε, δ, …) and sizes d ≈ p^ε, K ≈ d^c make every normalized cost-table term at most p^{1−2κ}, with smallest margin 2^{−181} = 2κ.
- Integer multiplication in O(n(lg n)^(1−κ)) time: A single deterministic fixed-tape Turing machine computes the exact product of two n-bit integers in O(n(lg n)^{1−κ}) worst-case time with κ = 2^{−182}, refuting the n log n lower-bound conjecture in this model.

## Other pages you may link to

- [n log n optimality conjecture](n-log-n-conjecture.md)
- [Harvey–van der Hoeven multiplier](harvey-van-der-hoeven-multiplier.md)
- [Polynomial ring ℂ[y]/(yʳ+1)](negacyclic-ring.md)
- [Normalized butterfly H₀](butterfly-h0.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)
- [Arrays on tape and elementary stream operations](elementary-streams.md)
- [Address shear](address-shear.md)
- [Controlled shifts](controlled-shifts.md)
- [Linear maps and matrix rank](matrix-rank.md)
- [Linear network with wire roles](linear-network.md)
- [Frames and the common-frame identity](frames.md)
- [Restoration of scratch values](scratch-restoration.md)
- [Three-element subset construction](triple-intersection-construction.md)
- [Nondegenerate bilinear forms](bilinear-form.md)
- [Tensor products](tensor-product.md)
- [Subspace labels and orthogonal residuals](subspace-labels.md)
- [Rank saving s < Wm](rank-saving.md)
- [Rational matrix interface](rational-matrix-interface.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Signed Kronecker packing](signed-packing.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Convolution over the polynomial ring](synthetic-convolution.md)
- [Parameter choice and cost balance](parameter-choice.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multiplication as digit convolution](radix-digit-convolution.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Coefficient phase twist](coefficient-twist.md)
- [Retained transform permutations](retained-permutations.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Integer multiplication in O(n(lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$." (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.

- "A single truncation follows the completed contractive layer." (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.


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

Write the body to `exegenius/tasks/0028-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0028-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0028-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0028-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
