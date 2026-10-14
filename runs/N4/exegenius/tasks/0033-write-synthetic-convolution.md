# exegenius task 0033-write-synthetic-convolution

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
- Normalized discrete Fourier transform (also: DFT)
- Fixed-point approximation and error accounting (also: disk grid, precision p)
- Gaussian resampling
- Polynomial ring ℂ[y]/(yʳ+1)
  - $\mathbb C$ (complex numbers): The field of complex numbers from which the coefficients are taken.
  - $y$ (ring variable): The polynomial indeterminate, whose r-th power equals −1 in the ring.
  - $r$ (record length): The number of complex coefficients in each polynomial record, a power of two.
- Normalized butterfly H₀
  - $H_0$ (normalized butterfly): The two-point linear map sending (u,v) to ((u+v)/2,(u−v)/2).
- Gaussian dyadic numbers
- Synthetic polynomial transform (also: Nussbaumer transform)
- Signed Kronecker packing (also: Kronecker substitution)
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
- Simultaneous butterfly layer
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

Concept: Convolution over the polynomial ring
Gloss: Normalized cyclic convolution of arrays over ℂ[y]/(y^r+1) computed by two forward synthetic transforms on a tape layout using chunk interchanges and simultaneous layers, packed pointwise products, and the opposite transform.

## This page in the argument

The step: Normalized cyclic convolution $\mathcal M_r$ of arrays over $\mathbb C[y]/(y^r+1)$ on power-of-two axes is approximated with error below $\sqrt2M(3\ell+1)2^{-p}$ at cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ plus packed products.
How: compute two forward synthetic transforms on a layout built by chunk interchanges with simultaneous layers, multiply pointwise by signed packing, and apply the opposite transform in the stored frequency order
Why: In the ring, the needed roots of unity are powers of $y$, so the transforms reduce to signed shifts, butterflies and address moves, exactly what the two tape procedures accelerate. (the sources say so: "Powers of $y$ then
serve as roots of unity in the remaining axes, and multiplication by
such a root is a signed shift of the coefficient list." (paper))

Its sub-steps, in order:

- Synthetic transforms over $\mathcal R_r$ use powers of $y$ as roots of unity, which act by exact signed permutations of coefficient lists. (on [Synthetic polynomial transform](synthetic-transform.md))
- On the layout placing selected bits at a common offset, each transform costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ and the opposite transform consumes the stored frequency order.
- Signed Kronecker packing computes each normalized ring product $Q_p(fg/r)$ in $O(rp\log(rp))$ time with one call to the $O(N\log N)$ multiplier. (on [Signed Kronecker packing](signed-packing.md))
- Composing the transforms and pointwise products approximates $\mathcal M_r$ with error below $\sqrt2M(3\ell+1)2^{-p}$.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine computes the exact product of two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: reduce multiplication through radix digits, a CRT address map, Gaussian resampling and a coefficient twist to convolution over $\mathbb C[y]/(y^r+1)$, accelerate its address moves and butterfly layers with two tape procedures derived from finite linear networks with a rank saving, recover the product exactly, and balance the parameters (on [Integer multiplication in O(n(lg n)^(1−κ)) time](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S4.2, S4.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S4.2**: On the layout placing selected bits at a common offset, each transform costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$ and the opposite transform consumes the stored frequency order.
Source: "The forward procedure may retain its output layout for a
pointwise product and the following opposite procedure." (paper)
> ucts an explicit positional layout permutation $L$ of record addresses, preserving their polynomial suffixes, and transforms disk grid arrays of $M$ contiguous degree-less-than-$r$ polynomial records. Its exact counterpart is $LB F_{\boldsymbol t}^-$. Its opposite procedure consumes that order and has exact counterpart $F_{\boldsymbol t}^+B^{-1}L^{-1}$. Each procedure has error less than $\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same component format, and costs \begin{equation} O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'}\right]\right). \label{eq:synthetic-transform-cost} \end{equation} Both layout construction and final restoration are charged in this bound. The forward procedure may retain its output layout for a pointwise product and the following opposite procedure. \end{lemma} \begin{proof} Put $D=d-1$ and write $a_i=\log_2t_i$. The supplied encoding has $2w=\Theta(p)$ bits per coefficient, so the logical bit volume is $\Theta(Tp)$. Call an axis long if $a_i=\ell$ and short if $a_i=\ell-1$. Name the original bit slots of axis $i$ by $(i,h)$, $a_i-1\geq h\geq0$. Initially these slots are in axis order and, within each axis, in decreasing $h$. The coefficients of each polynomial form a contiguous suffix. Put \[ b=(\ell-1)\bmod K, \qquad q=\lfloor(\ell-1)/K\rfloor. \] Form a list of the slots to move to a prefix. First list $(i,\ell-1)$ for the length-$2^\ell$ axes in increasing $i$. Then list $(i,h)$ for $h=b-1,\ldots,0$, and w

**S4.4**: Composing the transforms and pointwise products approximates $\mathcal M_r$ with error below $\sqrt2M(3\ell+1)2^{-p}$.
Source: "$\mathcal M_r$ on disk grid operands has an approximation with error" (paper)
> \begin{proposition}[Convolution from the retained transform layout] \label{prop:synthetic-convolution} Under the hypotheses of Lemma~\ref{lem:synthetic-transform-cost}, $\mathcal M_r$ on disk grid operands has an approximation with error less than \begin{equation} \sqrt2\,M(3\ell+1)2^{-p} \label{eq:synthetic-convolution-error} \end{equation} and cost \[ O\left(Tp\left[dK+pK^{\tau-1}+\ell d^{\lambda'} +\log(rp)\right]\right). \] Put $m_M=\log_2M$ and $w_M=w+m_M$. The returned grid array is in the original array and coefficient order, with the same two's-complement component format at width $w_M$. The procedure supplies $\Gamma(w_M)$ on the output descriptor tape, so the caller knows every component boundary from this width and the retained shape parameters. If one operand has norm at most $\rho<1$ and the bound in \eqref{eq:synthetic-convolution-error} is at most $1-\rho$, the returned grid array is a disk array. \end{proposition} \begin{proof} Perform both forward transforms and retain their common $LB$ order. Pass the supplied $p,r,w$ to Lemma~\ref{lem:signed-ring-product} for corresponding polynomial records. Its output keeps that record order and uses the component format required by the opposite procedure. Apply the opposite procedure to that order, and multiply its result exactly by $M=T/r$.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S4.1 (on [Synthetic polynomial transform](synthetic-transform.md)): Synthetic transforms over $\mathcal R_r$ use powers of $y$ as roots of unity, which act by exact signed permutations of coefficient lists.
- S4.3 (on [Signed Kronecker packing](signed-packing.md)): Signed Kronecker packing computes each normalized ring product $Q_p(fg/r)$ in $O(rp\log(rp))$ time with one call to the $O(N\log N)$ multiplier.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Fixed-point approximation and error accounting](fixed-point-approximation.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Synthetic polynomial transform](synthetic-transform.md): Nussbaumer's Fourier transform over ℂ[y]/(y^r+1) using powers of y as roots of unity, so it needs only signed shifts, butterflies and address rearrangements, with a stored frequency order consumed by the inverse transform.
  Shown as: Convolution over the polynomial ring *<predicate>* Synthetic polynomial transform
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): The second tape procedure: applying H₀ at the same bit position of up to d address chunks at once in O(V d^{λ'}) time with λ' < 1, computed exactly in Gaussian dyadics and truncated once.
  Shown as: Convolution over the polynomial ring *<predicate>* Simultaneous butterfly layer
- [Fast address-chunk interchange](chunk-interchange.md): The first tape procedure: exchanging two disjoint u-bit address fields of an array in O(V u^τ) time with τ < 1, by recursively running the bit network with shears as edge frames.
  Shown as: Convolution over the polynomial ring *<predicate>* Fast address-chunk interchange
- [Signed Kronecker packing](signed-packing.md): Packing the signed fixed-point coefficients of two ring elements into large integers so one call to the O(N log N) multiplier yields their exact polynomial product.
  Shown as: Convolution over the polynomial ring *<predicate>* Signed Kronecker packing

## Pages that build on this one

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
- [Recursive power saving](recursive-power-saving.md)
- [Rational matrix interface](rational-matrix-interface.md)
- [Binary phase interface](binary-phase-interface.md)
- [Lower triangular factorization](lower-triangular-factorization.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Fixed-point approximation and error accounting](fixed-point-approximation.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
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

- "The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order." (paper)

  > Next, Bluestein's chirp identity converts the middle transform, including its target permutation, into normalized cyclic convolution. A phase twist changes the last cyclic coordinate into a polynomial modulo $y^r+1$; its negative wrap gives precisely the original cyclic wrap after the twist is removed. Sections~\ref{sec:synthetic-layouts} and~\ref{sec:exact-ring-products} compute convolution on the remaining axes over this polynomial ring. The two forward synthetic transforms retain the same frequency order through their pointwise product, and the opposite transform consumes that order. Their polynomial products use signed packing and the established $O(n\log n)$ multiplier as an ordinary subroutine.


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

Write the body to `exegenius/tasks/0033-write-synthetic-convolution.answer.md` and the JSON to `exegenius/tasks/0033-write-synthetic-convolution.answer.json`, then run `exegenius submit 0033-write-synthetic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0033-write-synthetic-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
