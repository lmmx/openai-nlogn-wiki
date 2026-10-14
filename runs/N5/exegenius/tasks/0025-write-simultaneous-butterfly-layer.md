# exegenius task 0025-write-simultaneous-butterfly-layer

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

Concept: Simultaneous butterfly layer
Gloss: Applying H₀ on the same bit position in each of up to d equal-width address chunks costs O(V·d^λ′) with λ′ < 1, by recursing through the complex network's phase frames, with exact dyadic intermediates and one final truncation.

## This page in the argument

The step: Applying $H_0$ at one common bit position in each of $D\le d$ equal-width address chunks of polynomial records costs $O(Vd^{\lambda'})$ with $\lambda'<1$, with exact dyadic intermediates and one final truncation.
How: recurse through the complex network's phase frames, realizing binary basis changes by packed address moves and converting the C-layer to the H_0 layer by phases
Why: Separate butterfly factors would need one full pass per selected axis; the phase-frame recursion shares the work across axes and saves a power of d. (the sources say so: "We will obtain cost $O(Vd^{\lambda'})$, with $\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly factors would require $D$ whole-array passes." (paper))

Its sub-steps, in order:

- With phase frames $\mathcal C_U$, each edge's frame change is a product of one two-point kernel $aI+bX_v$ per orthonormal residual vector, and telescoping gives $C^{\otimes e}$ on every role by $s_{\rm c}$ child calls on $e/m$ axes. (on [Binary phase frames](phase-frames.md))
- Diagonal phases and the scalar $b^D$ convert the exact $C^{\otimes D}$ layer into $H_0^{\otimes D}$ using only Gaussian dyadic operations.
- Packed changes of selected address bits and the recursion give total time $O(Vd^{\lambda'})$ on fixed tapes.
- Since $H_0^{\otimes D}$ maps disk arrays to disk arrays, the final truncation $Q_p$ keeps values in the disk with error below $\sqrt2\,2^{-p}$. (on [Fixed-point disk grid and truncation](fixed-point-precision.md))

It serves these steps, from the main result down:

- A single deterministic fixed-alphabet multitape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: speed up address movement and butterfly arithmetic by recursive linear-network procedures, plug them into Harvey and van der Hoeven's reduction of multiplication to synthetic polynomial transforms, and bound the total cost (on [Integer multiplication below n log n](main-theorem.md))
- Address-field interchange costs $O(Vu^\tau)$ and a simultaneous butterfly layer costs $O(Vd^{\lambda'})$, with fixed $\tau,\lambda'<1$, where $V$ is the stored bit volume.; how: turn a strict rank deficit of two finite linear networks into recursive power savings for both tape procedures

## Steps this page derives

The argument gives this page these sub-steps of its step (S5.2, S5.3). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S5.2**: Diagonal phases and the scalar $b^D$ convert the exact $C^{\otimes D}$ layer into $H_0^{\otimes D}$ using only Gaussian dyadic operations.
Source: "Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation." (paper)
> \paragraph{Returning to normalized butterflies.} For an address $x$ in a full layer, write $x_1,\ldots,x_D$ for its selected bits. The diagonal operator $\mathcal S_D$ multiplies the value stored at an address by the phase determined by those bits: \[ (\mathcal S_D z)(x)=i^{x_1+\cdots+x_D}z(x). \] Here the unselected address bits are unchanged, and the same phase is applied to every coefficient stored at that address. Applying \eqref{eq:phase-basic-identities} on all selected coordinates gives \begin{equation}\label{eq:phase-butterfly-layer} H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D. \end{equation} The scalar is \[ b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}, \] so it is a binary shift and fourth-root phase, with at most one further factor $b$. All phases, inverse wrappers, and scalar corrections above are exact Gaussian dyadic operations. Thus, once the physical binary basis changes and recursive stream layout are supplied, the complete parallel butterfly layer is exact up to its prescribed final truncation.

**S5.3**: Packed changes of selected address bits and the recursion give total time $O(Vd^{\lambda'})$ on fixed tapes.
Source: "The row construction and the recurrence analysis above give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams." (paper)
> Uniformly for large $p$, the bands give $f\le d\le p$ and \[ K\ge\tfrac12a_d^c p^{\epsilon c},\qquad r\ge2^{(a_r/b_d)p^{1-\epsilon}}. \] The first inequality follows from $K=\lfloor d^c\rfloor$ once $d^c\ge2$. In particular, $K\ge6$ and $K/\log p\to\infty$, while $r$ dominates every fixed polynomial. Substituting the common bound $A_*\le C_Ap$ into the two additional normalized terms in \eqref{eq:packed-rectangle-time} gives \[ \begin{aligned} \frac{A_*^3}{R_{\rm g}} &\le\frac{C_A^3p^2}{2r},\\ 80(f-1)2^{-K}A_*\left(1+\frac{A_*}{R_{\rm g}}\right) &\le80C_Ap^2 2^{-K}\left(1+\frac{C_A}{2r}\right). \end{aligned} \] Both bounds tend to zero uniformly over all current allowed $d,r$. Thus Lemma~\ref{lem:packed-selected-bit-rectangle} has the required $O(M_{\rm child}R_{\rm g}(L^\tau+1))$ cost for every packed call, with one common time constant. The row construction and the recurrence analysis above give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams. Equation~\eqref{eq:phase-butterfly-layer} converts the resulting exact $C$-layer to $\mathcal H$.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S5.1 (on [Binary phase frames](phase-frames.md)): With phase frames $\mathcal C_U$, each edge's frame change is a product of one two-point kernel $aI+bX_v$ per orthonormal residual vector, and telescoping gives $C^{\otimes e}$ on every role by $s_{\rm c}$ child calls on $e/m$ axes.
- S5.4 (on [Fixed-point disk grid and truncation](fixed-point-precision.md)): Since $H_0^{\otimes D}$ maps disk arrays to disk arrays, the final truncation $Q_p$ keeps values in the disk with error below $\sqrt2\,2^{-p}$.

### Other pages these steps use

Link each where the derivation uses it, stating what it gives; do not derive its results again.

- [Normalized butterfly H₀](normalized-butterfly.md)
- [Gaussian dyadic numbers](gaussian-dyadics.md)

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Binary phase frames](phase-frames.md): For the complex network, frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m}; an edge's frame change is a product of one two-point kernel aI + bX_v per orthonormal residual vector, and telescoping gives the kernel C^{⊗m} on every role.
  Shown as: Simultaneous butterfly layer *<predicate>* Binary phase frames
- [Recursive power saving](recursive-saving.md): A call at parameter mf is done by s calls at parameter f on streams of volume V/W, so normalized cost grows by s/W < m^τ per level, giving cost O(V·f^τ) with τ < 1.
  Shown as: Simultaneous butterfly layer *<predicate>* Recursive power saving
- [Fast address-chunk interchange](fast-address-interchange.md): Interchanging two disjoint contiguous address fields of u bits in an array costs O(V·u^τ) with τ = 1 − 2⁻⁵⁰, realized by recursively applying the bit network and computing XOR combinations of data.
  Shown as: Simultaneous butterfly layer *<predicate>* Fast address-chunk interchange
- [Fixed-point disk grid and truncation](fixed-point-precision.md): Values are stored as complex numbers in the unit disk with real and imaginary parts on the grid 2^{−p}ℤ, and Q_p truncation toward that grid adds error below √2·2^{−p}.
  Shown as: Simultaneous butterfly layer *<predicate>* Fixed-point disk grid and truncation
- [Polynomial ring modulo y^r + 1](polynomial-ring.md): The ring ℂ[y]/(y^r+1) with r a power of two, where multiplication by a power of y is a signed shift of the coefficient list, so powers of y serve as cheap roots of unity.
  Shown as: Simultaneous butterfly layer *<predicate>* Polynomial ring modulo y^r + 1

## Pages that build on this one

- Fixed rational parameters and cost table: The compatible choice τ = σ = 1 − 2⁻⁵⁰, λ′ = 1 − 2⁻⁵⁴, ε = 2⁻⁷⁵, κ = 2⁻¹⁸², etc., under which every term of the normalized cost table is O((lg n)^{1−κ}).
- Fast synthetic transform layout: A tape layout placing the selected bits of participating axes at a common offset in consecutive K-bit chunks so simultaneous butterfly layers apply, with chunk interchanges paying for the movement.

## Other pages you may link to

- [n log n optimality conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplier](harvey-hoeven-multiplier.md)
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
- [Lower triangular factorization](triangular-factorization.md)
- [Address shear](address-shear.md)
- [Bit network interface](bit-network-interface.md)
- [Signed Kronecker packing](signed-kronecker-packing.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Multidimensional Fourier transform](multidimensional-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling with retained permutations](gaussian-resampling.md)
- [Fixed rational parameters and cost table](parameter-choice.md)
- [Fast synthetic transform layout](transform-layout.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit reduction to convolution](radix-digit-convolution.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Coefficient twist](coefficient-twist.md)
- [Normalized convolution over the polynomial ring](synthetic-convolution.md)
- [Exact coefficient recovery and carries](exact-recovery.md)
- [Integer multiplication below n log n](main-theorem.md)

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

Write the body to `exegenius/tasks/0025-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0025-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0025-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0025-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
