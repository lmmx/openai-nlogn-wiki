# exegenius task 0101-extend

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

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

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, discrete mathematics (modular arithmetic, primes, binary representation, induction), introductory linear algebra (vectors, matrices, inverses, dot products), and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). They know basic Turing machines with several tapes and standard algorithm analysis, including recurrences and schoolbook multiplication. They have not studied the FFT-based multiplication literature, abstract algebra beyond basics, or tape-level data-movement algorithms.

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Existing concepts

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on growth.
- `polynomials`: Polynomials (known to the reader): Sums of powers of a variable with coefficients.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi, with roots of unity.
- `turing-machine-tapes`: Multitape Turing machine (known to the reader): Finite-state machine with tapes read and written one cell per step.
- `fixed-tape-model`: Fixed-tape machine model and stream operations: Machine with one fixed finite alphabet and a fixed number of one-dimensional tapes; each step touches one cell per tape, so data movement (scans, shifts, permutations) is the cost to minimize.
- `convolution`: Convolution: Product of polynomials / combination of coefficient lists where entries sum by index (cyclic if indices wrap).
- `dft-fft`: Discrete Fourier transform and butterflies: Evaluation of a coefficient list at roots of unity, computed in log-many levels of two-point butterfly operations; turns convolution into pointwise product.
- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage–Strassen's proposal that n log n is the optimal order of cost for multiplying n-bit integers.
- `ss-hh-background`: Schönhage–Strassen to Harvey–van der Hoeven multiplication: Chain of multitape algorithms from O(n log n log log n) to the unconditional O(n log n) bound, using transforms over rings with cheap roots of unity.
- `radix-digit-reduction`: Reduction of integer product to digit convolution: Splitting the inputs into radix digits turns the integer product into a convolution of short integer coefficients, followed by carry propagation.
- `crt-address-map`: Chinese-remainder map to prime cyclic axes: Places the coefficient list on a product of distinct prime cyclic axes by a map preserving convolution, implemented via triangular controlled shifts and axis moves.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven reduction expressing each Fourier transform of prime-length axes through a multidimensional transform with power-of-two axis lengths.
- `bluestein-chirp`: Bluestein's chirp identity: Rewrites a discrete Fourier transform as a cyclic convolution via chirp phases.
- `poly-ring-y-r`: Polynomial ring modulo $y^r+1$: Complex-coefficient polynomials in y reduced by y^r = -1, so multiplying by a power of y is a signed shift of the coefficient list and powers of y serve as roots of unity.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms over the polynomial ring where root multiplications are signed shifts, leaving address rearrangements, shifts and butterflies.
- `signed-packing`: Signed coefficient packing (Kronecker substitution): Packs polynomial coefficients into one integer so polynomial products are done by an ordinary n log n integer multiplier.
- `phase-twist-convolution`: Last-coordinate phase twist: Twisting the last cyclic coordinate into a polynomial modulo y^r+1 whose negative wrap equals the original cyclic wrap after untwisting.
- `ring-convolution-retained-order`: Convolution with retained transform order and cancelled permutations: Two forward synthetic transforms keep the same frequency order through the pointwise product, and the opposite transform consumes it, so retained permutations cancel without separate sorts.
- `address-fields`: Address fields and array layout on tapes: Arrays stored in tape order with addresses forming a Cartesian product of digit fields; rearranging fields costs time.
- `linear-network-roles`: Finite linear network with roles and frames: Fixed linear network exchanging two banks of values with prescribed signs and restoring auxiliary values; wires have roles, rows are distributed cyclically among roles, and invertible frame operators cancel along routes leaving an endpoint operator.
- `subset-intersection-construction`: Three-element subset intersection construction: Gather/scatter with auxiliary wires cancelling unwanted coefficients, using indicator-vector orthogonality to assign subspaces; gives s<Wm smaller calls.
- `recursive-power-saving`: Recursive power saving from s<Wm: Recursive call at parameter mf uses s calls at parameter f on streams of volume V/W; since s/W<m the volume-normalized cost grows as a power, giving a fixed power saving.
- `address-shear-factorization`: Address shear and lower-triangular factorization: Endpoint operator (H,D)->(H+D,D) over a residue ring, with rank reduction via a singular-matrix Bruhat factorization into lower-triangular factors.
- `scratch-restoration`: Restoring auxiliary scratch values: Subtract initial register value, compute, add result, reverse, so the permutation is exact for arbitrary initial auxiliary values.
- `fast-address-interchange`: Fast interchange of address fields: Interchange two disjoint contiguous u-bit address fields in an array in O(V u^τ) for fixed τ<1, via XOR combinations that end as an exact permutation.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u-v)/2) on selected address bits of polynomial-valued arrays with exact Gaussian dyadics in O(V d^λ') with λ'<1, one truncation at the end.
- `fixed-point-precision`: Fixed-point precision and exact recovery: Complex fixed-point coefficients; bounding error below 1/2 so rounding recovers exact integer coefficients and carry propagation yields the product.
- `main-theorem`: Integer multiplication in O(n(lg n)^{1-κ}) time: Deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, by reducing to ring convolution with fast address interchanges and simultaneous butterfly layers, disproving the n log n conjecture in this model.
- `binary-representation-and-bit-operations`: Binary representation and bit operations (known to the reader): Integers written in base 2, with bitwise operations such as XOR acting on their digits.
- `modular-arithmetic`: Modular arithmetic (known to the reader): Arithmetic on integers where values differing by a multiple of the modulus are identified.
- `prime-numbers-and-coprimality`: Prime numbers and coprimality (known to the reader): Primes are integers greater than 1 with no proper divisors; two integers are coprime when their gcd is 1.
- `logarithms-and-floor-ceiling`: Logarithms and floor/ceiling (known to the reader): The base-2 logarithm and rounding down or up to integers, as used in size and depth bounds.
- `vectors-matrices-and-inverses`: Vectors, matrices and inverses (known to the reader): Finite-dimensional vectors, matrices acting as linear maps, invertibility, and orthogonality via dot products.
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication (known to the reader): Quadratic digit-by-digit multiplication and the divide-and-conquer improvement using three half-size products.
- `divide-and-conquer-recurrences`: Divide-and-conquer recurrences (known to the reader): Solving cost recurrences such as T(n)=aT(n/b)+f(n) to obtain asymptotic bounds.
- `limits-series-and-convergence`: Limits, series and convergence (known to the reader): Limits of sequences, convergence of series such as geometric sums, used to bound errors and total costs.
- `cartesian-product-and-tuples`: Cartesian product and tuples (known to the reader): Ordered tuples of coordinates drawn from several index sets, used to index multidimensional arrays.
- `permutations`: Permutations (known to the reader): A bijective rearrangement of positions in a list, composable and invertible.
- `roots-of-unity`: Roots of unity (known to the reader): Complex numbers w with w^n=1, evenly spaced on the unit circle.
- `rings-and-basic-algebraic-structures`: Rings and basic algebraic structures (known to the reader): Sets with addition and multiplication satisfying the standard laws, including integers modulo m and polynomials modulo a polynomial.
- `fixed-point-and-rounding-arithmetic`: Fixed-point and rounding arithmetic (known to the reader): Representing reals by integers scaled by a power of 2, with bounded error from rounding or truncation.

## Unresolved terms

- "address interchange"
  - on page `recursive-power-saving`: "the number of field digits for address interchange"
- "bit-reversed input"
  - on page `dft-fft`: "With bit-reversed input, the last level leaves"
- "fast transform and transform axes"
  - on page `poly-ring-y-r`: "A fast transform is built from butterflies"
- "forward transform of length S"
  - on page `fixed-point-precision`: "Let $\mathcal F$ be the forward transform of length $S$"
- "Gaussian (weighting function)"
  - on page `gaussian-resampling`: "$G$ and $J$ are sums weighted by Gaussians that move values between the two grids."
- "negative source projections"
  - on page `main-theorem`: "minus a positive deficit from the negative source projections"
- "norm"
  - on page `gaussian-resampling`: "is within less than one half of the identity in norm"
- "numerical layer"
  - on page `recursive-power-saving`: "of selected axes for a numerical layer"
- "rank budget of the network (motif-residual lemma)"
  - on page `address-shear-factorization`: "which the paper bounds by a rank budget of the network (its motif-residual lemma)"
- "scratch (auxiliary) roles"
  - on page `linear-network-roles`: "so scratch roles are unchanged by this undoing"
- "source and sink nodes of a route"
  - on page `linear-network-roles`: "Let $\mathrm{source}(w)$ and $\mathrm{sink}(\rho(w))$ be the source and sink nodes at the ends of that route."
- "source scale 2^gamma"
  - on page `fixed-point-precision`: "the exponent of the source scale $2^{\gamma}$"
- "tensor product of vector spaces"
  - on page `subset-intersection-construction`: "Let $\mathcal F=(\mathbb Q^h)^{\otimes 3}$, of dimension $m=h^3$"
- "transform (the DFT/FFT the layout is for)"
  - on page `address-fields`: "The transform is computed in levels"
- "twiddle factor"
  - on page `synthetic-transforms`: "every twiddle factor is a power of $y$"
- "unitary"
  - on page `fast-butterfly-layers`: "$C$ is unitary"

## New pages

New concepts the reader does not know: at most 12, and submit rejects more. Resolve the other terms to existing or known concepts, or list them under `inline`.

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

Write the answer to `exegenius/tasks/0101-extend.answer.json`, then run `exegenius submit 0101-extend` in the project directory. If submit rejects the answer, fix the answer and submit again.
