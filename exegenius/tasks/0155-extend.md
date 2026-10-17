# exegenius task 0155-extend

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Extend a prerequisite graph of concepts built from source documents. Audits of the wiki reported terms that they judged a specific reader cannot follow and that match no existing concept. For each term, point it at an existing concept that covers it, add a new concept, or list it under `inline` to be explained in a sentence where it is used.

- Auditors can misjudge what the reader profile covers. A term the profile covers, whether or not it names it, is known to the reader: point it at a known concept, or add one with `known: true`. Known concepts get no page.
- Add a new concept only when no existing concept covers the term and the term needs a page of its own; a term one sentence can explain goes under `inline`. The task gives the most new concepts the reader does not know that this answer may add, and submit rejects more. Give each new concept an id that is not already used.
- New concepts may require existing concepts or each other; the graph must stay acyclic.
- Mark `known: true` if the reader profile already covers the concept, with `requires: []`.
- `evidence` quotes must be copied from the sources character for character, with their source id. A concept that does not appear in the sources may have no quotes.
- A name with mathematics in it needs a `title` with the mathematics in LaTeX and a binding in `symbols` for every symbol in it, as in the extract task.
- Give every term a resolution, or list it under `inline`.

## Target

The main result of the paper: a deterministic multitape Turing machine algorithm that multiplies n-bit integers in O(n (lg n)^(1-kappa)) time, disproving the n log n optimality conjecture in that model, and how it works

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is a computer science undergraduate: they have taken discrete mathematics, an algorithms course (asymptotics, divide and conquer, schoolbook and Karatsuba multiplication, sorting), a first linear algebra course (vector spaces, subspaces, dimension, rank, matrices as linear maps, inverses, triangular matrices, orthogonality, bilinear forms at a basic level), calculus, elementary number theory (primes, gcd, modular arithmetic) and basic machine-level binary representation (XOR, two's complement). They have seen Turing machines with tapes only at an introductory level. They have not been taught the discrete Fourier transform or FFT as such, abstract algebra beyond basic definitions (quotient rings, finite fields as a theory), tensor products, numerical error analysis, or the specific literature on fast integer multiplication.

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Existing concepts

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bounds on running time such as O(n log n).
- `polynomials`: Polynomials (known to the reader): Sums of powers of a variable with coefficients, added and multiplied term by term.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, with modulus and unit-modulus phases e^{iθ}.
- `turing-machines`: Turing machines and tapes (known to the reader): Machines with a finite control reading and writing cells on tapes, one step at a time.
- `machine-model`: Fixed finite-tape machine model: The computation model of the main theorem: one fixed finite alphabet and a fixed number of one-dimensional tapes, each head moving at most one cell per step.
- `stream-ops`: Elementary stream operations: Linear-time scans on arrays stored in lexicographic order: swapping two digits, moving a digit, splitting into streams, applying a pointwise map and merging back.
- `controlled-shifts`: Controlled shifts and rational scalings: Updating a target address field by an offset computed from earlier control fields, or multiplying it by a unit, in time linear in the array volume.
- `conjecture`: Schönhage–Strassen optimality conjecture: The 1971 proposal that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
- `hvdh-multiplier`: Established O(n log n) multiplier: The earlier Harvey–van der Hoeven multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine.
- `convolution`: Cyclic convolution: The product of two sequences (or elements of a polynomial quotient ring) where indices wrap around: (f∗g)_k = Σ f_j g_{k−j}.
- `radix-digit-reduction`: Multiplication as radix-digit convolution: Splitting each integer into radix-2^b digits turns the product into a convolution of short integer coefficients, which carry propagation turns back into a binary number.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ u_j e^{−2πi jk/q}, which turns convolution into pointwise multiplication.
- `butterfly`: Butterflies and the fast transform: A two-point averaging/differencing step H₀(u,v) = ((u+v)/2, (u−v)/2) whose repeated use over address bits, with twiddle multiplications, computes a transform in log t layers.
- `multidim-transform`: Multidimensional transforms: A transform over several axes at once, the tensor product of one-dimensional transforms, applied to an array one axis at a time.
- `crt-map`: Chinese-remainder address map: An isomorphism that places a cyclic convolution of length S = s₁⋯s_d on pairwise coprime prime axes, implemented as triangular controlled shifts.
- `gaussian-resampling`: Gaussian resampling: Re-expressing a Fourier transform of prime length s through a transform of nearby power-of-two length t using Gaussian weights, so that only power-of-two transforms are needed.
- `chirp`: Bluestein chirp identity: An identity that rewrites a (permuted) Fourier transform as a pointwise chirp phase, a cyclic convolution, and another chirp phase.
- `retained-permutations`: Retained permutation cancellation: Leaving the coordinate permutations of resampling inside the transform identity, so the source permutation cancels across the two forward transforms and the opposite one and none is executed as a sort.
- `ring-y`: Polynomial ring modulo y^r + 1: Polynomials of degree below r over the complex numbers with y^r = −1, so multiplying by a power of y is a signed shift of the coefficient list.
- `phase-twist`: Phase twist: Multiplying coefficient k by e^{πik/r}, which converts the cyclic coordinate modulo x^r − 1 into the negacyclic ring modulo y^r + 1 and is removed afterwards.
- `synthetic-transform`: Synthetic polynomial transform: A transform over the ring modulo y^r + 1 whose roots of unity are powers of y, so every twiddle multiplication is a signed shift of a coefficient list.
- `frequency-order`: Retained frequency order: The forward synthetic transform writes its outputs in bit-reversed order, the pointwise product keeps that order, and the opposite transform consumes it, so no reordering is executed.
- `signed-packing`: Signed packing: A signed Kronecker substitution that evaluates polynomials with signed coefficients at 2^{4p} to form large integers, multiplies them with the O(n log n) multiplier, and recovers the product coefficients.
- `fixed-point`: Fixed-point Gaussian dyadic records: Complex values stored as signed two's-complement integers over a power-of-two denominator 2^{-p}; intermediate values are exact and one truncation Q_p rounds back to the p-bit grid.
- `precision-recovery`: Error tracking and exact recovery: Each normalized transform and product is a contraction with a bounded rounding error, and the total error on the recovered convolution coefficients is below 1/2, so rounding gives exact integers.
- `exchange-network`: Linear exchange network with restored scratch wires: A fixed network of linear gates on wires holding values that swaps two banks with a prescribed sign while undoing the effect of arbitrary initial scratch values, built from three-element subsets.
- `array-frames`: Frames on wire arrays: Replacing each wire scalar by an array and assigning an invertible operator D_v (a frame) at each gate so the pointwise gate commutes with the frame and only the endpoint frames matter.
- `subspace-labels`: Nested subspace labels and rank deficit: Assigning nondegenerate subspaces of an m-dimensional space to gates so adjacent labels are nested; the total dimension change over edges, the number s of smaller calls, is strictly less than W·m.
- `rank-recurrence`: Recursive power saving: Each call at parameter m·f makes s calls at parameter f on streams of 1/W the volume, so cost per unit volume grows by s/W < m per factor m, giving a power saving.
- `matrix-shear`: Matrix shear by triangular factorization: Factoring a rational matrix as A = E₁ΠE₂ with lower triangular E₁, E₂ and partial permutation Π lets the shear (H,D)→(H+AD,D) be done with exactly rank(A) field interchanges.
- `address-interchange`: Fast address-chunk interchange: The first tape procedure: exchanging two disjoint equal-width address fields of u digits in time O(V·u^τ) for a fixed τ < 1, using XOR combinations of intermediate data.
- `phase-kernel`: Two-point kernel C: The matrix C = aI + bX with a = (1+i)/2, b = (1−i)/2, a square root of the bit flip, linked to the butterfly by H₀ = b·S·C·S with S = diag(1, i).
- `phase-frames`: Binary phase frames: Frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} whose edge differences are products of translation kernels aI + bX_v, one per vector of an orthonormal residual basis.
- `packed-bit-addition`: Packed selected-bit addition: XORing selected bits between two address chunks (with a third chunk as restored scratch) using cyclic shifts of whole chunk ranges plus a repair of explicitly bounded exceptional addresses.
- `simultaneous-layer`: Simultaneous butterfly layer: The second tape procedure: applying H₀ coefficientwise on the same bit of up to d address chunks in time O(V·d^λ′) for a fixed λ′ < 1, instead of d passes.
- `transform-layout`: Tape layout for synthetic transforms: Placing the selected bits of the participating axes at a common offset in K-bit chunks so each round of the synthetic transform is one simultaneous layer, costing less than log t passes.
- `ring-convolution`: Convolution from the retained transform layout: Convolution over the ring modulo y^r + 1 on the remaining axes by two forward synthetic transforms, pointwise polynomial products and the opposite transform, normalized by 1/(rM).
- `parameter-choice`: Parameter and prime-length choice: Fixed rational exponents and sizes (precision p = 6b, d axes, K = d^c, T and r powers of two, prime lengths s_i just below t_i) making every hypothesis of the lemmas hold.
- `multiplication-algorithm`: The multiplication algorithm: Digits, then the CRT map, two forward transforms with resampling and chirps, a pointwise product, the opposite transform, rescaling, rounding and carry propagation yield the exact 2n-bit product.
- `cost-accounting`: Cost accounting and the exponent κ: Dividing each cost by V = Tp, the dominant terms are powers of p below one with minimum margin 2^{-181} = 2κ, giving total time O(n(lg n)^{1−κ}).
- `main-result`: Power-saving integer multiplication: A deterministic fixed-tape Turing machine multiplying two n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model.
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication (known to the reader): The quadratic digit-by-digit multiplication algorithm and Karatsuba's divide-and-conquer improvement to O(n^{log_2 3}) by three half-size products.
- `divide-and-conquer-recurrences`: Divide-and-conquer recurrences (known to the reader): Bounding the cost of a recursive algorithm by solving a recurrence such as T(n) = a T(n/b) + f(n).
- `binary-and-radix-representation`: Binary and radix representation (known to the reader): Writing a nonnegative integer as a sequence of digits in base 2 or base 2^b, with carries when digit values overflow.
- `two-s-complement-integers`: Two's complement integers (known to the reader): The standard fixed-width encoding of signed integers in binary, with addition performed bitwise with carries.
- `bitwise-xor-and-arithmetic-mod-2`: Bitwise XOR and arithmetic mod 2 (known to the reader): Addition of bits modulo 2, which is exclusive-or, with x + x = 0, so XORing a value twice restores it.
- `logarithms-and-floors-ceilings`: Logarithms and floors/ceilings (known to the reader): Base-2 logarithms and the floor and ceiling functions, including the rules for manipulating logarithms in growth rates.
- `modular-arithmetic-and-primes`: Modular arithmetic and primes (known to the reader): Arithmetic on remainders modulo n, greatest common divisors, coprimality, prime numbers and inverses of residues coprime to the modulus.
- `roots-of-unity`: Roots of unity (known to the reader): The n complex solutions of z^n = 1, namely e^{2 pi i k/n}, which lie on the unit circle and form a cyclic group under multiplication.
- `vector-spaces-subspaces-dimension-and-rank`: Vector spaces, subspaces, dimension and rank (known to the reader): The core linear algebra notions of vector space, subspace, basis, dimension and the rank of a matrix or linear map.
- `matrices-and-linear-operators`: Matrices and linear operators (known to the reader): Matrices as linear maps on finite-dimensional spaces, with products, inverses, diagonal, triangular and permutation matrices and the notion of two operators commuting.
- `gaussian-elimination-and-triangular-factorization`: Gaussian elimination and triangular factorization (known to the reader): Reducing a matrix by row operations to triangular form, which yields factorizations into triangular factors and solves linear systems.
- `orthogonality-and-inner-products`: Orthogonality and inner products (known to the reader): The dot product on real or complex coordinate spaces, orthogonal and orthonormal bases, and the orthogonal complement of a subspace.
- `norms-and-the-triangle-inequality`: Norms and the triangle inequality (known to the reader): A size function on vectors, such as the maximum absolute coordinate, satisfying the triangle inequality and scaling, used to bound errors.
- `permutations-and-bijections`: Permutations and bijections (known to the reader): Bijective rearrangements of a finite set of indices, with composition and inverses.
- `cartesian-products-and-multi-index-arrays`: Cartesian products and multi-index arrays (known to the reader): Arrays indexed by tuples from a product of finite sets, stored linearly in lexicographic (row-major) order.
- `directed-acyclic-graphs-and-networks-of-gates`: Directed acyclic graphs and networks of gates (known to the reader): Directed graphs without cycles, and circuits made of gates connected by wires that compute a function of their inputs.
- `summation-geometric-series-and-induction`: Summation, geometric series and induction (known to the reader): Sigma notation, closed forms for geometric series, and proofs by induction on integers.
- `rounding-to-the-nearest-integer-and-exactness`: Rounding to the nearest integer and exactness (known to the reader): Replacing a real number by the nearest integer or grid point, and the fact that an approximation within 1/2 of an integer identifies that integer.
- `multitape-turing-machine-running-time`: Multitape Turing machine running time (known to the reader): Counting steps of a multitape machine whose heads move one cell per step, so that one sequential pass over n cells costs O(n).
- `integer-exponentials-and-tuple-notation`: Integer exponentials and tuple notation (known to the reader): Powers of two and fixed rational exponents of a size parameter, as used in expressions like n^{c} and 2^{-p}.
- `contraction-maps`: Contractions and bilinear contractions: A linear map that never increases the norm of a vector, and a bilinear map whose output norm is at most the product of the input norms, so errors in the inputs do not grow beyond a controlled bound.
- `tensor-product-of-spaces`: Tensor products of subspaces: The space built from two spaces whose dimension is the product of their dimensions, in which operators and bilinear forms act factorwise.

## Unresolved terms

- "costly recursive primitive"
  - on page `matrix-shear`: "Only an interchange calls the costly recursive primitive."
- "support of a vector"
  - on page `phase-frames`: "|\operatorname{supp}(z)\cap\operatorname{supp}(w)|"

## New pages

New concepts the reader does not know: at most 19, and submit rejects more. Resolve the other terms to existing or known concepts, or list them under `inline`.

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Binding": {
      "additionalProperties": false,
      "description": "What a symbol in a concept's name denotes.",
      "properties": {
        "meaning": {
          "description": "One sentence saying what the symbol denotes; for a count, what it counts.",
          "type": "string"
        },
        "name": {
          "description": "Display name of one to four words, e.g. \"record length\".",
          "type": "string"
        },
        "relation": {
          "$ref": "#/$defs/Relation"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the title's mathematics, without dollar signs,\ne.g. `r` or `\\kappa`.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "name",
        "meaning",
        "relation"
      ],
      "type": "object"
    },
    "Concept": {
      "additionalProperties": false,
      "description": "One concept. This is also the shape of a concept in an extract answer, so the field\ndocs double as instructions in the task file.",
      "properties": {
        "aliases": {
          "description": "Other names and abbreviations the sources use for this concept.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "evidence": {
          "description": "Short quotes copied exactly from the sources that state or use this concept.",
          "items": {
            "$ref": "#/$defs/Evidence"
          },
          "type": "array"
        },
        "gloss": {
          "description": "One precise sentence saying what the concept is, in plain text with Unicode symbols\n(it is shown as a tooltip on links to the concept).",
          "type": "string"
        },
        "id": {
          "description": "Lowercase slug, unique across the graph, e.g. \"chirp-identity\".",
          "type": "string"
        },
        "known": {
          "description": "True if the reader profile already covers this concept.",
          "type": "boolean"
        },
        "name": {
          "description": "Display name in plain text, e.g. \"Chirp identity\". Write symbols in Unicode (κ, ω,\n≤, n log n), not LaTeX or spelled-out Greek: names appear in the navigation, which\ndoes not render mathematics.",
          "type": "string"
        },
        "requires": {
          "description": "Ids of the concepts a reader must understand before this one.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "symbols": {
          "description": "What each symbol in the title's mathematics denotes, one binding per symbol. A reader\nwho knows the concept is shown these, so give every symbol, however minor.",
          "items": {
            "$ref": "#/$defs/Binding"
          },
          "type": "array"
        },
        "title": {
          "description": "Only for a name with mathematics in it: the name with the mathematics in LaTeX, e.g.\n\"Polynomial ring modulo $y^r + 1$\". It is the heading of the concept's page.",
          "type": [
            "string",
            "null"
          ]
        }
      },
      "required": [
        "id",
        "name",
        "aliases",
        "gloss",
        "requires",
        "known",
        "evidence"
      ],
      "type": "object"
    },
    "Evidence": {
      "additionalProperties": false,
      "properties": {
        "quote": {
          "description": "Text copied character for character from that source.",
          "type": "string"
        },
        "source": {
          "description": "Id of the source the quote comes from.",
          "type": "string"
        }
      },
      "required": [
        "source",
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
    },
    "Resolution": {
      "additionalProperties": false,
      "properties": {
        "concept": {
          "description": "Id of the concept that covers it.",
          "type": "string"
        },
        "term": {
          "description": "The unresolved term, exactly as given.",
          "type": "string"
        }
      },
      "required": [
        "term",
        "concept"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "concepts": {
      "description": "New concepts only; existing concepts must not be repeated.",
      "items": {
        "$ref": "#/$defs/Concept"
      },
      "type": "array"
    },
    "inline": {
      "default": [],
      "description": "Unresolved terms to explain in a sentence where they are used, instead of on a page.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "resolutions": {
      "description": "For every unresolved term not under `inline`, the id of the concept (existing or\nnew) that covers it.",
      "items": {
        "$ref": "#/$defs/Resolution"
      },
      "type": "array"
    }
  },
  "required": [
    "concepts",
    "resolutions"
  ],
  "title": "ExtendAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0155-extend.answer.json`, then run `exegenius submit 0155-extend` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0155-extend`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
