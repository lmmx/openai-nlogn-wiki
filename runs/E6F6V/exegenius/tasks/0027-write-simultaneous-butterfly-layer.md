# exegenius task 0027-write-simultaneous-butterfly-layer

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F6V` (paths below are relative to it)

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

For these sources: The reader is an undergraduate computer scientist: asymptotic analysis and recurrences, discrete mathematics (induction, sets, functions, permutations, logarithms, floor and ceiling, modular arithmetic, primes, gcd and the Euclidean algorithm), introductory linear algebra (matrices, invertibility, rank, Gaussian elimination, vectors and inner products), basic algorithms (grade-school multiplication, divide and conquer, number representations in binary, bitwise XOR) and the basics of Turing machines with several tapes. They have met complex numbers and polynomials, but not the FFT in depth, abstract algebra beyond basic rings or quotient constructions, number-theoretic results such as prime density, numerical error analysis, or any research on fast integer multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed-tape model and elementary stream scans
- Controlled cyclic shifts and rational scalings
- Established O(n log n) integer multiplier
- Integer multiplication as convolution of radix digits
- Normalized discrete Fourier transform and convolution theorem
- Radix-two FFT butterflies
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The indeterminate of the polynomials, whose powers act as roots of unity because y^r = −1.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, a power of two.
- Synthetic polynomial transforms
- Fixed-point disk-grid arrays and truncation
- Signed packing of polynomial products
- Subspaces, orthogonal complements and projections
- Lower-triangular (Bruhat) factorization
- Linear network exchanging two banks with restored scratch wires
- Frames and the common-frame identity
- Nested subspace labels with a rank deficit
- Recursive power saving from s < Wm
- Rational matrix interface and address shear
- Cost of a rational matrix shear
- Power-width chunk interchange with rows
- Fast interchange of address chunks
- Phase frames and the two-point kernel C
- Packed changes of selected address bits
- Exact Gaussian dyadics and guard width
- Modular arithmetic and congruences (also: integers mod n, Z/nZ, residues, congruence, mod q^b)
- Primes, coprimality and gcd (also: prime numbers, relatively prime, coprime, prime to q, greatest common divisor, gcd)
- Euclidean algorithm and modular inverses (also: extended Euclidean algorithm, Euclid's algorithm, Bezout identity, inverse modulo q)
- Trial division and primality search (also: finding a prime by scanning, testing divisibility, trial division)
- Binary representation, bit strings and XOR (also: binary expansion, bit string, bits, exclusive or, XOR, addition mod 2, most significant bit)
- Radix representation and carry propagation (also: base-b digits, radix, carries, grade-school addition, schoolbook multiplication, digit expansion)
- Logarithms, floor and ceiling (also: lg, log base 2, natural logarithm, floor function, ceiling function, power of two)
- Recurrences and induction (also: proof by induction, recurrence relations, unrolling a recurrence, geometric series)
- Divide-and-conquer multiplication (also: Karatsuba, schoolbook algorithm, O(n^2) multiplication, Toom-Cook)
- Permutations and bijections (also: permutation of coordinates, permutation matrix, partial permutation, bit reversal, bijection)
- Matrices, invertibility and rank (also: matrix product, invertible matrix, rank of a matrix, linear map, diagonal matrix, identity matrix, matrix inverse, linear combination)
- Gaussian elimination (also: row reduction, elementary row operations, row echelon form)
- Vector spaces, bases and dimension (also: basis, span, linear independence, dimension, coordinates, standard basis)
- Cartesian products and lexicographic order (also: product of sets, tuples, lexicographic ordering, multi-index, d-dimensional array indexing, row-major order)
- Rational numbers and dyadic fractions (also: dyadic rationals, binary fractions, denominators, numerators, rational coefficients, lowest terms)
- Norms, absolute value and triangle inequality (also: modulus, sup norm, maximum norm, triangle inequality, unit disk, Euclidean norm, contraction, error bound)
- Euler's formula and roots of unity (also: e^(i theta), primitive root of unity, cis, complex exponential, unit circle)
- Rounding and square roots (also: nearest integer, rounding to integer, square root, truncation toward zero)
- Polynomial time and computational cost on tapes (also: polynomial in p, linear time, worst-case running time, single scan of a tape, fixed alphabet, finite control)
- Fast Fourier transform as a known algorithm (also: FFT, Cooley-Tukey, divide-and-conquer FFT, fast polynomial multiplication)

## This page

Concept: Simultaneous butterfly layer
Gloss: Applying H₀(u,v) = ((u+v)/2,(u−v)/2) to the same bit position in d address chunks at once, on polynomial records, in O(V d^λ') time with λ' < 1 instead of d whole-array passes.

## This page in the argument

The step: The two-point butterfly $H_0$ is applied to the same bit position of $d$ address chunks at once, on polynomial records, in $O(Vd^{\lambda'})$ time with $\lambda'<1$ instead of $d$ whole-array passes.
How: build the layer from the kernel $C$ by the same rank-deficit recursion, with packed bit changes and guard bits
Why: Separate butterfly factors would need D whole-array passes; the recursion gets a power saving in d. (the sources say so: "$\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly" (paper))

Its sub-steps, in order:

- On selected bits, $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$ with $C=aI+bX$, and each edge of the complex network is a product of translation kernels, one per residual basis vector. (on [Phase frames and the two-point kernel C](phase-frames.md))
- Adding (XOR) selected bits of one address chunk into another is done by a constant number of cyclic shifts of whole chunk ranges plus deterministic repair of a small exceptional set of addresses. (on [Packed changes of selected address bits](packed-selected-bit-addition.md))
- Unrolling the recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ gives total cost $O(Vd^{\lambda'})$ for $d$ axes, with $\lambda'<1$.
- Intermediate values are exact Gaussian dyadics whose denominators and magnitudes grow by $o(p)$ guard bits, so one truncation follows the completed layer. (on [Exact Gaussian dyadics and guard width](guard-bits.md))
- The simultaneous normalized layer returns $Q_p(\mathcal H z)$ with error below $\sqrt2\,2^{-p}$ in time $O(Vd^{\lambda'})$.

It serves these steps, from the main result down:

- A single deterministic fixed-tape Turing machine multiplies two $n$-bit integers exactly in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: put fast address interchange and simultaneous butterfly layers inside the Gaussian-resampling and synthetic-transform reduction of multiplication to convolution, then verify exactness and cost (on [Integer multiplication below n log n](multiplication-below-nlogn.md))
- Two fast tape procedures exist: exact interchange of address fields and simultaneous butterfly layers, both with a power saving in the logarithmic factor.; how: obtain each procedure from a fixed linear network whose total edge rank is below the number of wires times the dimension

## Steps this page derives

The argument gives this page these sub-steps of its step (A4.3, A4.5). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**A4.3**: Unrolling the recurrence $F(e)\le(s/W)F(e/m)+O((eK)^\tau+1)$ gives total cost $O(Vd^{\lambda'})$ for $d$ axes, with $\lambda'<1$.
How: set up the recurrence for time divided by volume, now with $s=s_{\rm c}$ children, and sum it
- A4.3a: Each node makes $s$ calls on slots of $e/m$ chunks and volume $V/W$.
  Source: " F(e)\le (s/W)F(e/m)+O((eK)^\tau+1)," (paper)
  > \paragraph{Unrolling the recurrence.} Fix \(\beta=1/2\), and choose real exponents satisfying \[ 0<\tau<1,\qquad \max\{0,\log_m(s/W)\}\le\sigma<1, \qquad \max\{\tau,\sigma\}<\lambda<1, \qquad \tau(1+c/\beta)<\lambda. \] The exponents can all be chosen rational, with a strict upper bound in the condition on \(\sigma\). Stop recursion when \(e<d^\beta\) and apply the \(e\) \(C\) kernels individually. If \(F(e)\) denotes time divided by the current logical stream volume, then \[ F(e)\le (s/W)F(e/m)+O((eK)^\tau+1), \qquad F(e)=O(e)\quad(e<d^\beta). \] Indeed, the \(s\) child calls are executed on streams of volume \(V/W\), so their total cost is \(s(V/W)F(e/m)\). Dividing by the current volume \(V\) gives the factor \(s/W\). At an internal node \(e\ge d^\beta\), hence \(K\le d^c\le e^{c/\beta}\). The overhead is therefore \(O(e^{\tau(1+c/\beta)}+1)=O(e^\lambda)\). Put \(a=s/W\). Since \(a\le m^\sigma<m^\lambda\), the internal costs sum to at most \[ C e^\lambda\sum_{j\ge0}(a/m^\lambda)^j=O(e^\lambda). \] If the leaves after \(j\) levels contain \(u=e/m^j<d^\beta\) active chunks each, their combined normalized contribution is at most \[ O(a^ju)\le O(e^\sigma u^{1-\sigma}) \le O(e^\sigma d^{\beta(1-\sigma)}). \] The first inequality uses \(a^j\le m^{j\sigma}=(e/u)^\sigma\). It also covers \(a<1\) by taking \(\sigma\ge0\).
- A4.3b: Summing over levels and base-$m$ pieces gives $O(d^{\lambda'})$ for a fixed $\lambda'<1$.
  Source: "=O(d^{\lambda'})" (paper)
  > Write \(D-q_0=\sum_j a_jm^j\) in base \(m\), with \(0\le a_j<m\). Partition the remaining chunks into \(a_j\) consecutive pieces containing \(m^j\) chunks for each \(j\). There are at most \((m-1)(1+\lfloor\log_m d\rfloor)\) pieces. Adding their costs and the row preprocessing gives \[ O\!\left(\log(2d) \bigl[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1\bigr]\right) =O(d^{\lambda'}) \] for any fixed \[ \max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1. \] The case \(D\le q_0\), in which preprocessing would consume all active chunks, was handled by individual kernels. Thus all constants and all tape counts are independent of \(p,d,r\) and the input data.

**A4.5**: The simultaneous normalized layer returns $Q_p(\mathcal H z)$ with error below $\sqrt2\,2^{-p}$ in time $O(Vd^{\lambda'})$.
Source: "coefficient order, and component format in $O(Vd^{\lambda'})$ time," (paper)
> The procedure returns $Q_p(\mathcal H z)$ in the same array, coefficient order, and component format in $O(Vd^{\lambda'})$ time, uniformly over all these choices of $p,d,r,D,P,S,\rho,w$ and $z$. Every returned coefficient belongs to the complex unit disk, and, in the maximum coefficient norm, \[ \|Q_p(\mathcal H z)-\mathcal H z\|_\infty <\sqrt2\,2^{-p}. \] The procedure evaluates the entire layer exactly before this final truncation. Put \[ C_0=128m\bigl(s_{\rm c}+64(W_{\rm c}+m+1)^3\bigr)^2, \] where $m,W_{\rm c},s_{\rm c}$ are the fixed constants of Proposition~\ref{prop:complex-motif-interface}. The procedure uses at most $p+\lceil C_0d^{C_1}\rceil$ fractional bits and $\lceil C_0d^{C_1}\rceil+3$ integer and sign bits per real component internally; these widths are $O(p)$. The time includes address changes, deterministic repair, row padding and its removal, and fixed-tape workspace cleanup. Its tape count is fixed, and its time constant is independent of the allowed array lengths and coefficient values. \end{proposition}

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- A4.1 (on [Phase frames and the two-point kernel C](phase-frames.md)): On selected bits, $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$ with $C=aI+bX$, and each edge of the complex network is a product of translation kernels, one per residual basis vector.
- A4.2 (on [Packed changes of selected address bits](packed-selected-bit-addition.md)): Adding (XOR) selected bits of one address chunk into another is done by a constant number of cyclic shifts of whole chunk ranges plus deterministic repair of a small exceptional set of addresses.
- A4.4 (on [Exact Gaussian dyadics and guard width](guard-bits.md)): Intermediate values are exact Gaussian dyadics whose denominators and magnitudes grow by $o(p)$ guard bits, so one truncation follows the completed layer.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Phase frames and the two-point kernel C](phase-frames.md): With C = H S H = aI+bX (a=(1+i)/2, b=(1−i)/2) one has H₀^(⊗D) = b^D S_D C^(⊗D) S_D, and phase frames of binary labels make each network edge a product of translation kernels, one per residual basis vector.
  Shown as: Simultaneous butterfly layer *<predicate>* Phase frames and the two-point kernel C
- [Packed changes of selected address bits](packed-selected-bit-addition.md): Adding (XOR) selected bits of one address chunk into another using a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small explicitly identified set of exceptional addresses.
  Shown as: Simultaneous butterfly layer *<predicate>* Packed changes of selected address bits
- [Recursive power saving from s < Wm](recursive-power-saving.md): A call at parameter m·f makes s calls at parameter f on streams of volume V/W, so normalized cost satisfies F_k ≤ (s/W)F_(k−1)+O(1) with s/W < m^τ, giving cost O(V e^τ) with τ < 1.
  Shown as: Simultaneous butterfly layer *<predicate>* Recursive power saving from s < Wm
- [Exact Gaussian dyadics and guard width](guard-bits.md): Intermediate values in a butterfly layer are exact Gaussian dyadics whose denominators and magnitudes grow by at most a bounded number of guard bits, so one truncation follows the completed layer.
  Shown as: Simultaneous butterfly layer *<predicate>* Exact Gaussian dyadics and guard width
- [Radix-two FFT butterflies](radix-two-fft.md): The decimation-in-frequency recursion that pairs entries k and k+t/2, applies the two-point butterfly H₀ = ½[[1,1],[1,−1]] and a twiddle multiplication, then recurses on both halves, leaving outputs in bit-reversed order.
  Shown as: Simultaneous butterfly layer *<predicate>* Radix-two FFT butterflies
- [Fixed-point disk-grid arrays and truncation](fixed-point-precision.md): Complex coefficients of modulus at most 1 stored with p fractional bits per component; truncation Q_p toward zero costs error below √2·2^(−p) and never increases the norm.
  Shown as: Simultaneous butterfly layer *<predicate>* Fixed-point disk-grid arrays and truncation
- [Fast interchange of address chunks](chunk-interchange.md): Interchanging two disjoint address fields of u bits in an array in O(V u^τ) time for a fixed τ < 1, although the intermediate steps XOR data together; arbitrary widths are handled by padding and a base-m decomposition.
  Shown as: Simultaneous butterfly layer *<predicate>* Fast interchange of address chunks

## Pages that build on this one

- Synthetic transform layout on tape: A positional address permutation placing the selected bits of all participating axes at a common offset in consecutive K-bit chunks so that each FFT round is one simultaneous layer; total cost O(Tp[dK + pK^(τ−1) + ℓ d^λ']).
- Cost table and exponent margins: Dividing each phase's cost by Tp = Θ(n) gives seven dominant powers of p, each at most 1−2κ for the fixed rational exponents, so the total is O(n (log n)^(1−κ)).

## Other pages you may link to

- [Integer multiplication as convolution of radix digits](convolution-multiplication.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Established O(n log n) integer multiplier](hvdh-multiplier.md)
- [Fixed-tape model and elementary stream scans](multitape-streams.md)
- [Controlled cyclic shifts and rational scalings](controlled-shifts.md)
- [Linear network exchanging two banks with restored scratch wires](bank-exchange-network.md)
- [Subspaces, orthogonal complements and projections](linear-algebra-spaces.md)
- [Frames and the common-frame identity](frames-on-arrays.md)
- [Nested subspace labels with a rank deficit](subspace-labels.md)
- [Rational matrix interface and address shear](bit-shear-interface.md)
- [Lower-triangular (Bruhat) factorization](lower-triangular-factorization.md)
- [Cost of a rational matrix shear](matrix-shear-cost.md)
- [Power-width chunk interchange with rows](power-width-interchange.md)
- [Signed packing of polynomial products](signed-kronecker-packing.md)
- [Normalized discrete Fourier transform and convolution theorem](discrete-fourier-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Synthetic transform layout on tape](synthetic-transform-layout.md)
- [Convolution over the polynomial ring from retained frequency order](synthetic-convolution.md)
- [Cyclic-to-negacyclic coefficient twist](coefficient-twist.md)
- [Gaussian resampling without sorting](gaussian-resampling.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Cancellation of the retained source permutation](permutation-cancellation.md)
- [Tensor resampling on the padded box](tensor-resampling.md)
- [Chinese-remainder map to distinct prime cyclic axes](crt-cyclic-convolution.md)
- [Size parameters and prime axis lengths](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Precision, rounding and carry recovery](exact-recovery.md)
- [Cost table and exponent margins](time-bound-accounting.md)
- [Integer multiplication below n log n](multiplication-below-nlogn.md)

## Evidence from the sources, with the paragraph around each quote

- "Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise." (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.

- "whereas separate butterfly factors would require $D$ whole-array passes" (paper)

  > The parameters will satisfy \[ d=\Theta(p^\epsilon),\qquad K=\lfloor d^c\rfloor, \qquad r=2^{\Theta(p/d)},\qquad c>0,\quad 0<\epsilon<1. \] The exponents and comparison constants are fixed, and we impose their further restrictions in Proposition~\ref{prop:simultaneous-layer}. Two consequences explain the layout. The polynomial length $r$ grows faster than every fixed power of $p$, so a scan of a record pays for polynomial work on its address. Also $K/\log p\to\infty$, which will make the exceptional set in a packed change of address bits small enough to repair by sorting. We will obtain cost $O(Vd^{\lambda'})$, with $\lambda'<1$ and $V$ the logical bit volume, whereas separate butterfly factors would require $D$ whole-array passes.


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

Write the body to `exegenius/tasks/0027-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0027-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0027-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0027-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
