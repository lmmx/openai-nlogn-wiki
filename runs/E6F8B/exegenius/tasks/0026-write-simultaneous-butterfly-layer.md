# exegenius task 0026-write-simultaneous-butterfly-layer

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F8B` (paths below are relative to it)

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

For these sources: The reader has an undergraduate computer science education: algorithm analysis with big-O, divide and conquer and sorting, discrete mathematics (sets, permutations, modular arithmetic, primes, induction), and introductory linear algebra (matrices, linear maps, invertibility, triangular and permutation matrices). They know polynomials and complex numbers including roots of unity and Euler's formula, basic calculus functions, and basic Turing machines with several tapes and head movements. They have probably met schoolbook and Karatsuba multiplication and the idea of the FFT, but have not studied abstract algebra beyond basics, finite-field theory, numerical analysis of error, multidimensional Fourier methods, or the Schönhage–Strassen line of fast multiplication.

The reader already understands these concepts:

- Big-O notation
- Polynomials
- Complex numbers
- Multitape Turing machine
- The n log n barrier
- Convolution
- Discrete Fourier transform
- Fast Fourier transform with butterflies
- Fixed-point complex grid and truncation
- Subspaces, rank and orthogonal complements
- Arrays as address fields on tape
- Controlled cyclic shift
- Scratch-restoring bank exchange
- Frames: changing representation along a network
- Triple-subset labels and the rank budget
- Address shear and triangular factorization
- Recursive rank saving
- Power-width chunk interchange
- Address chunk interchange
- Complex phase network
- Packed selected-bit addition
- Polynomial ring modulo y^r + 1
  - $y$ (ring variable): The formal polynomial variable whose powers act as roots of unity because y^r=−1.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Synthetic polynomial transform
- Signed packing (Kronecker substitution)
- Cyclic-to-negacyclic coefficient twist
- Chinese-remainder address map
- Binary numerals and bit strings (also: binary representation, bit string, binary expansion, most significant bit, bits)
- Positional notation in any radix (also: base-b representation, radix, digits in base b, mixed radix)
- Integer division with remainder, floor and ceiling (also: Euclidean division, quotient and remainder, floor function, ceiling function, rounding to nearest integer)
- Modular arithmetic (also: congruence, residues mod m, integers mod m, Z/mZ, clock arithmetic)
- Arithmetic modulo 2 and XOR (also: XOR, exclusive or, bitwise XOR, parity, F_2, GF(2), addition mod 2)
- Primes, coprimality and gcd (also: prime number, relatively prime, greatest common divisor, pairwise coprime, Euclid's algorithm)
- Roots of unity and Euler's formula (also: e^{i theta}, primitive root of unity, nth roots of unity, unit circle, complex exponential)
- Exponential, logarithm and Gaussian function (also: exp, log base 2, lg, natural logarithm, e^{-x^2}, bell curve)
- Asymptotic notation beyond big-O (also: Omega, Theta, little-o, liminf, limit inferior, omega notation)
- Geometric series and sums (also: geometric sum, geometric progression, summation, telescoping)
- Divide and conquer and recurrences (also: recursion, recurrence relation, master theorem, recursion tree, T(n)=aT(n/b)+f(n))
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, Karatsuba algorithm, O(n^2) multiplication, integer multiplication)
- Sorting and its cost (also: merge sort, comparison sorting, O(n log n) sorting, sorting algorithms)
- Permutations and bijections (also: permutation, bijection, one-to-one correspondence, inverse permutation, reordering)
- Sets, subsets and Cartesian products (also: subset, Cartesian product, indicator vector, characteristic vector, tuples, set intersection, intersection size)
- Multidimensional arrays and row-major order (also: lexicographic order, row-major order, array indexing, nested loops, matrix as array)
- Matrices, vectors and linear maps (also: matrix multiplication, matrix inverse, invertible matrix, linear transformation, linear operator, linear combination, vector space, linear independence, basis, dimension)
- Triangular and permutation matrices (also: lower-triangular matrix, upper-triangular matrix, permutation matrix, LU decomposition, identity matrix, diagonal matrix)
- Dot product, inner product and orthogonality (also: inner product, scalar product, orthogonal vectors, orthonormal, bilinear form)
- Dyadic rationals and fixed-width numerators (also: dyadic fraction, binary fraction, number over a power of two, binary point)
- Matrix transposition (also: transpose, row-major to column-major, transposing an array)
- Triangle inequality and norms (also: maximum norm, sup norm, modulus inequality, |a+b|<=|a|+|b|, error bound)
- Mathematical induction and proof by contradiction (also: induction, inductive proof, proof techniques)
- Cyclic shifts and rotations of lists (also: circular shift, rotation of array, wrap-around shift, cyclic rotation)
- Subroutines and composition of algorithms (also: calling a procedure, black box subroutine, reduction, algorithm composition)

## This page

Concept: Simultaneous butterfly layer
Gloss: Applying H₀ to the same bit position in each of D≤d address chunks at once, on polynomial records of complex fixed-point coefficients, in O(V d^{λ'}) time with one final truncation.

## This page in the argument

The step: Applying $H_0(u,v)=((u+v)/2,(u-v)/2)$ to the same bit position in each of $D\le d$ address chunks of polynomial records at once costs $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$, with a single truncation at the end.
How: Write the tensor power of $H_0$ through the tensor power of the kernel $C=aI+bX$, evaluate that by the complex phase network recursively with packed changes of selected address bits, and convert back to $H_0$.
Why: Doing the $D$ butterflies one after another would need $D$ passes over the whole array, so one network call must serve all the selected bits at once. (the sources say so: "factors would require $D$ whole-array passes." (paper))

Its sub-steps, in order:

- Applying the complex phase network to a group of $e$ selected axes, with column frames built from $C=HSH=aI+bX$, produces $C^{\otimes e}$ on every role, using $s_{\rm c}$ child calls on $e/m$ axes each. (on [Complex phase network](phase-frame-network.md))
- The basis changes between slots are binary row additions $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ on selected bits of whole chunks, done by a constant number of whole-chunk cyclic shifts plus a deterministic sorting repair of the few bad addresses. (on [Packed selected-bit addition](packed-selected-bit-addition.md))
- The phase-frame construction reduces $e$ selected bits to $s_{\rm c}$ children on $e/m$ bits each of $1/W_{\rm c}$ of the volume, so the total time is $O(Vd^{\lambda'})$ on fixed tapes.
- Since $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$ with exact Gaussian dyadic phases, the exact $C$-layer converts to the normalized $H_0$ layer, followed by one truncation $Q_p$.

It serves these steps, from the main result down:

- A deterministic multitape Turing machine multiplies two $n$-bit integers in $O(n(\lg n)^{1-\kappa})$ time with $\kappa=2^{-182}$.; how: Reduce the product to a convolution of radix digits evaluated by approximate Fourier transforms over a polynomial ring, make the transform's address movement and arithmetic cheaper with two new tape procedures, then show the result is exact and add up the cost. (on [Integer multiplication below n log n](main-theorem.md))

## Steps this page derives

The argument gives this page these sub-steps of its step (S2.3, S2.4). Derive each here, so the reader can check how it follows from what comes before: stating its result, or citing the source for it, does not derive it. The passages report each step in the source; they ground the derivation and are not to be copied onto the page. In `derivations`, give each step's id and the passage on the page that derives it, copied exactly: submit checks that the passage is on the page, and the audit judges whether it is enough.

**S2.3**: The phase-frame construction reduces $e$ selected bits to $s_{\rm c}$ children on $e/m$ bits each of $1/W_{\rm c}$ of the volume, so the total time is $O(Vd^{\lambda'})$ on fixed tapes.
Source: "above give total time $O(Vd^{\lambda'})$ on fixed tapes, including" (paper)
> Uniformly for large $p$, the bands give $f\le d\le p$ and \[ K\ge\tfrac12a_d^c p^{\epsilon c},\qquad r\ge2^{(a_r/b_d)p^{1-\epsilon}}. \] The first inequality follows from $K=\lfloor d^c\rfloor$ once $d^c\ge2$. In particular, $K\ge6$ and $K/\log p\to\infty$, while $r$ dominates every fixed polynomial. Substituting the common bound $A_*\le C_Ap$ into the two additional normalized terms in \eqref{eq:packed-rectangle-time} gives \[ \begin{aligned} \frac{A_*^3}{R_{\rm g}} &\le\frac{C_A^3p^2}{2r},\\ 80(f-1)2^{-K}A_*\left(1+\frac{A_*}{R_{\rm g}}\right) &\le80C_Ap^2 2^{-K}\left(1+\frac{C_A}{2r}\right). \end{aligned} \] Both bounds tend to zero uniformly over all current allowed $d,r$. Thus Lemma~\ref{lem:packed-selected-bit-rectangle} has the required $O(M_{\rm child}R_{\rm g}(L^\tau+1))$ cost for every packed call, with one common time constant. The row construction and the recurrence analysis above give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams. Equation~\eqref{eq:phase-butterfly-layer} converts the resulting exact $C$-layer to $\mathcal H$.

**S2.4**: Since $H_0^{\otimes D}=b^D\mathcal S_D C^{\otimes D}\mathcal S_D$ with exact Gaussian dyadic phases, the exact $C$-layer converts to the normalized $H_0$ layer, followed by one truncation $Q_p$.
Source: "converts the resulting exact $C$-layer to $\mathcal H$." (paper)
> Uniformly for large $p$, the bands give $f\le d\le p$ and \[ K\ge\tfrac12a_d^c p^{\epsilon c},\qquad r\ge2^{(a_r/b_d)p^{1-\epsilon}}. \] The first inequality follows from $K=\lfloor d^c\rfloor$ once $d^c\ge2$. In particular, $K\ge6$ and $K/\log p\to\infty$, while $r$ dominates every fixed polynomial. Substituting the common bound $A_*\le C_Ap$ into the two additional normalized terms in \eqref{eq:packed-rectangle-time} gives \[ \begin{aligned} \frac{A_*^3}{R_{\rm g}} &\le\frac{C_A^3p^2}{2r},\\ 80(f-1)2^{-K}A_*\left(1+\frac{A_*}{R_{\rm g}}\right) &\le80C_Ap^2 2^{-K}\left(1+\frac{C_A}{2r}\right). \end{aligned} \] Both bounds tend to zero uniformly over all current allowed $d,r$. Thus Lemma~\ref{lem:packed-selected-bit-rectangle} has the required $O(M_{\rm child}R_{\rm g}(L^\tau+1))$ cost for every packed call, with one common time constant. The row construction and the recurrence analysis above give total time $O(Vd^{\lambda'})$ on fixed tapes, including all padded and auxiliary streams. Equation~\eqref{eq:phase-butterfly-layer} converts the resulting exact $C$-layer to $\mathcal H$.

### Steps derived on other pages

Where this page uses one, state its result and link the page that derives it. Do not derive it here, even where a passage above proves it.

- S2.1 (on [Complex phase network](phase-frame-network.md)): Applying the complex phase network to a group of $e$ selected axes, with column frames built from $C=HSH=aI+bX$, produces $C^{\otimes e}$ on every role, using $s_{\rm c}$ child calls on $e/m$ axes each.
- S2.2 (on [Packed selected-bit addition](packed-selected-bit-addition.md)): The basis changes between slots are binary row additions $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$ on selected bits of whole chunks, done by a constant number of whole-chunk cyclic shifts plus a deterministic sorting repair of the few bad addresses.

## Prerequisite pages (link each on first use, exactly as written, and give a relation for each)

- [Complex phase network](phase-frame-network.md): The second network over Gaussian dyadics with binary labels, whose frames are built from the two-point kernel C=HSH=aI+bX, so each edge is a product of translation kernels and the endpoint operator is C^{⊗m} on every role.
  Shown as: Simultaneous butterfly layer *<predicate>* Complex phase network
- [Packed selected-bit addition](packed-selected-bit-addition.md): XORing corresponding selected bits of many chunks at once by a constant number of whole-chunk cyclic shifts that are correct away from a small set of guard-violating addresses, which are then repaired deterministically by sorting.
  Shown as: Simultaneous butterfly layer *<predicate>* Packed selected-bit addition
- [Recursive rank saving](rank-saving-recurrence.md): Splitting rows among the W network roles makes each recursive call a 1/W-volume stream, so the cost per volume grows by s/W<m when the parameter is multiplied by m, giving a power saving.
  Shown as: Simultaneous butterfly layer *<predicate>* Recursive rank saving
- [Fast Fourier transform with butterflies](fft-butterflies.md): Computing a length-2^a transform in a levels, each pairing entries by a two-point butterfly H₀(u,v)=((u+v)/2,(u−v)/2) followed by a twiddle multiplication.
  Shown as: Simultaneous butterfly layer *<predicate>* Fast Fourier transform with butterflies
- [Fixed-point complex grid and truncation](fixed-point-complex-arithmetic.md): Complex numbers stored as signed two's-complement numerators over 2^p, in the unit disk, with truncation toward zero to the grid after exact dyadic arithmetic.
  Shown as: Simultaneous butterfly layer *<predicate>* Fixed-point complex grid and truncation

## Pages that build on this one

- Transform layout on tape: Placing the selected bit of each participating axis at a common offset in consecutive K-bit chunks, using bit moves and chunk interchanges, so that each transform round is one simultaneous butterfly layer.
- Parameter regime for the multiplier: The choice of precision p=6b, dimension d≈p^ε, record length r=2^Θ(p^(1−ε)), power-of-two axis lengths t_i and distinct prime source lengths s_i just below them, so that Tp=Θ(n) and all hypotheses hold.
- Cost accounting and the exponent κ: Dividing every cost by V=Tp gives normalized costs that are at most p^(1−2κ), the smallest margin 2^−181 coming from the chunk-exchange term, giving total time O(n(log n)^(1−κ)).

## Other pages you may link to

- [The n log n barrier](n-log-n-barrier.md)
- [Convolution](convolution.md)
- [Polynomial ring modulo y^r + 1](negacyclic-ring.md)
- [Cyclic-to-negacyclic coefficient twist](coefficient-twist.md)
- [Signed packing (Kronecker substitution)](signed-packing.md)
- [Arrays as address fields on tape](tape-address-model.md)
- [Controlled cyclic shift](controlled-cyclic-shift.md)
- [Scratch-restoring bank exchange](scratch-restoring-exchange.md)
- [Frames: changing representation along a network](array-frames.md)
- [Subspaces, rank and orthogonal complements](rank-and-orthogonal-subspaces.md)
- [Triple-subset labels and the rank budget](subset-intersection-labels.md)
- [Address shear and triangular factorization](address-shear-factorization.md)
- [Power-width chunk interchange](power-width-interchange.md)
- [Address chunk interchange](address-chunk-interchange.md)
- [Chinese-remainder address map](crt-axis-map.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Synthetic polynomial transform](synthetic-polynomial-transform.md)
- [Bluestein chirp identity](bluestein-chirp.md)
- [Retained frequency order](stored-frequency-order.md)
- [Transform layout on tape](transform-tape-layout.md)
- [Contractions and error accounting](contraction-error-propagation.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](permutation-cancellation.md)
- [Normalized convolution over the polynomial ring](normalized-ring-convolution.md)
- [Parameter regime for the multiplier](parameter-regime.md)
- [Radix-digit convolution](radix-digit-reduction.md)
- [Source transform on the padded box](tensor-source-transform.md)
- [Precision and exact recovery](precision-exact-recovery.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Integer multiplication below n log n](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$" (paper)

  > The second procedure applies \[ H_0(u,v)=\bigl((u+v)/2,(u-v)/2\bigr) \] simultaneously on selected coordinate bits of the numerical arrays. Each record is a polynomial with complex fixed-point coefficients, and $H_0$ acts coefficientwise. On the layouts used in the multiplication algorithm, one selects the same bit position in each of at most $d$ equal-width address chunks, and the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$. Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators. A single truncation follows the completed contractive layer. Section~\ref{sec:tape-interchange} proves the address bound, and Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound.

- "whereas separate butterfly factors would require $D$ whole-array passes." (paper)

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

Write the body to `exegenius/tasks/0026-write-simultaneous-butterfly-layer.answer.md` and the JSON to `exegenius/tasks/0026-write-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0026-write-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0026-write-simultaneous-butterfly-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
