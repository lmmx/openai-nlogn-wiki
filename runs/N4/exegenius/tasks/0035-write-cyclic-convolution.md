# exegenius task 0035-write-cyclic-convolution

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
- Convolution over the polynomial ring
- Parameter choice and cost balance (also: cost table)
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

Concept: Cyclic convolution
Gloss: The product of polynomials modulo x^S − 1 (or its multidimensional analogue), where exponents wrap around cyclically.

## Where the argument relies on this page

- Splitting each $n$-bit input into radix-$2^b$ digits reduces the product to a convolution of short integer coefficient sequences followed by carry propagation. (on [Multiplication as digit convolution](radix-digit-convolution.md))
- The source Fourier transform on pairwise coprime axes factors through Gaussian contractions and a power-of-two transform whose target permutation is absorbed by a chirp, and whose source permutation cancels in convolution. (on [Retained transform permutations](retained-permutations.md))
- The permuted middle transform $QF_{\boldsymbol t}$ equals a chirp multiplication, a cyclic convolution with the chirp, and another chirp multiplication. (on [Bluestein's chirp identity](bluestein-chirp.md))
- The retained source permutation $R$ cancels across the two forward transforms, their pointwise product and the opposite transform, giving $(u*v)/S^2$.
- The map $x\mapsto\prod_ix_i^{\mu_i}$ is an algebra isomorphism turning cyclic convolution of length $S=\prod_is_i$ into convolution on pairwise coprime axes, implemented by triangular controlled shifts. (on [Chinese-remainder address map](crt-address-map.md))
- Multiplying coefficient $k$ by $\zeta^k$ with $\zeta=e^{\pi i/r}$ maps cyclic convolution modulo $x^r-1$ onto negacyclic multiplication in $\mathbb C[y]/(y^r+1)$. (on [Coefficient phase twist](coefficient-twist.md))

## Pages that build on this one

- Multiplication as digit convolution: Splitting each integer into radix-2^b digits turns their product into the convolution of short digit sequences, followed by carry propagation.
- Chinese-remainder address map: An algebra isomorphism x ↦ ∏ x_i^{μ_i} that turns a cyclic convolution of length S = ∏ s_i into a multidimensional cyclic convolution on pairwise coprime axes, implemented by triangular controlled shifts.
- Bluestein's chirp identity: A Fourier transform equals pointwise multiplication by a quadratic-phase chirp, a cyclic convolution with the chirp, and another chirp multiplication.
- Coefficient phase twist: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} maps cyclic convolution modulo x^r − 1 isomorphically onto negacyclic multiplication modulo y^r + 1.
- Retained transform permutations: Instead of sorting, the source and target coordinate permutations of resampling stay inside the transform identity; the target one is absorbed by the chirp and the source one cancels across forward transforms, pointwise product and inverse transform.

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
- [Fast address-chunk interchange](chunk-interchange.md)
- [Packed selected-bit addition](packed-selected-bit-addition.md)
- [Fixed-point approximation and error accounting](fixed-point-approximation.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Signed Kronecker packing](signed-packing.md)
- [Normalized discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Convolution over the polynomial ring](synthetic-convolution.md)
- [Parameter choice and cost balance](parameter-choice.md)
- [Multiplication as digit convolution](radix-digit-convolution.md)
- [Chinese-remainder address map](crt-address-map.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Coefficient phase twist](coefficient-twist.md)
- [Retained transform permutations](retained-permutations.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Integer multiplication in O(n(lg n)^(1−κ)) time](main-theorem.md)

## Evidence from the sources, with the paragraph around each quote

- "Here $*$ denotes cyclic convolution on the product of the coordinate groups and a dot denotes coordinatewise multiplication." (paper)

  > The factor $QF_{\boldsymbol t}$ in \eqref{eq:no-sort-tensor} can be computed from a cyclic convolution and two pointwise phase multiplications. The chirp identity below performs the frequency change in $Q$ without applying $Q$ as a separate permutation of the array. The second identity shows how the retained source permutation $R$ cancels when computing a convolution. Here $*$ denotes cyclic convolution on the product of the coordinate groups and a dot denotes coordinatewise multiplication.


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

Write the body to `exegenius/tasks/0035-write-cyclic-convolution.answer.md` and the JSON to `exegenius/tasks/0035-write-cyclic-convolution.answer.json`, then run `exegenius submit 0035-write-cyclic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0035-write-cyclic-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
