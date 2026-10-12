# exegenius task 0094-extend

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

For these sources: The reader has an undergraduate computer science degree: big-O notation and worst-case time of Turing machines, polynomials and complex numbers, and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). The same degree is taken to include introductory discrete mathematics (modular arithmetic, primes, induction, sets, graphs, recurrences) and a first course in linear algebra over the reals (vectors, subspaces, matrices, elimination, dot products), each at introductory depth. Fields in the abstract sense, tensor products, bilinear forms over general fields, Gaussian integers and the Chinese remainder theorem are not assumed.

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Existing concepts

- `integer-multiplication-target`: Integer multiplication in O(n(lg n)^(1-κ)) time: A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.
- `big-o`: Big-O notation (known to the reader): Notation O(g) for the set of functions bounded above by a constant multiple of g for all sufficiently large inputs.
- `multitape-tm`: Multitape Turing machine (known to the reader): A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, each with its own head that moves at most one cell per step.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with a, b real and i² = −1, used for the roots of unity and the coefficients of the transforms.
- `polynomials`: Polynomials (known to the reader): Expressions a₀ + a₁y + … + a_k y^k over a coefficient ring, with the usual addition and multiplication.
- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture: The conjecture of Schönhage and Strassen that n log n is the optimal order of growth of the time to multiply two n-bit integers on a multitape Turing machine.
- `harvey-hoeven-multiplier`: Harvey–van der Hoeven O(n log n) multiplication: The unconditional O(n log n) multiplication algorithm on a multitape Turing machine, used in this result as an ordinary subroutine.
- `matrix-rank`: Matrix rank: The rank of a matrix is the maximum number of linearly independent rows or columns; the number of nonzero pivots in elimination.
- `fourier-transform`: Discrete Fourier transform: The map sending a length-n sequence to its values at the n-th roots of unity, i.e. the sums of the sequence weighted by powers of a root of unity.
- `roots-of-unity`: Primitive roots of unity: A complex number ω is a primitive n-th root of unity when ω^n = 1 and no smaller positive power equals 1.
- `cyclic-convolution`: Cyclic convolution: The product of two sequences in which indices are taken modulo a fixed length, so each coefficient of the result is a sum of products over residues.
- `convolution-reduction`: Multiplication as convolution of digits: Writing each integer in radix 2^b digits so that the integer product becomes a convolution of the digit sequences, which is then carried back to binary.
- `chinese-remainder-address-map`: Chinese-remainder address map: A rearrangement that places a digit sequence on a product of distinct prime cyclic axes while preserving convolution, implemented with address interchanges.
- `gaussian-resampling`: Gaussian resampling: An identity that expresses a Fourier transform of length given by a prime as a multidimensional transform with power-of-two axis lengths, with the source and target permutations kept in the identity.
- `bluestein-chirp`: Bluestein's chirp identity: The identity that converts a Fourier transform into a cyclic convolution by multiplying by chirp factors before and after it.
- `polynomial-ring-y`: Polynomial ring modulo yʳ + 1: The ring of complex polynomials in y reduced modulo y^r + 1, where multiplying by a power of y is a signed cyclic shift of the coefficient list.
- `synthetic-transform`: Synthetic polynomial transform: A transform over a polynomial ring in which the roots of unity are powers of y, so that each transform stage uses only signed shifts and butterfly additions.
- `kronecker-packing`: Signed Kronecker packing: Encoding a polynomial with bounded signed coefficients as an integer by evaluating it at a large power of two, so that polynomial products become integer products.
- `butterfly-operation`: Butterfly operation: The two-point map (u, v) ↦ ((u + v)/2, (u − v)/2) applied to a pair of values, the basic step of a fast transform.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: A butterfly operation applied at once on one selected address bit of every record, with exact Gaussian dyadic intermediates and a single truncation after the layer.
- `linear-network-exchange`: Linear network with restored auxiliary values: A fixed linear network that exchanges banks of values with prescribed signs and restores every auxiliary value, with each gate acting on the stored array through a frame operator that cancels between edges.
- `lower-triangular-factorization`: Lower-triangular factorization: The factorization A = E₁ΠE₂ of a rational matrix into invertible lower-triangular factors and a partial permutation matrix with one 1 per pivot.
- `address-shear`: Address shear: The permutation (H, D) ↦ (H + AD, D) on two ordered groups of address fields, which is performed with as many pairwise interchanges as the rank of A.
- `address-interchange`: Fast address interchange: A tape procedure that swaps two disjoint contiguous address fields of an array in time O(V u^τ) for width u, computed through XOR combinations of intermediate data.
- `recursive-power-saving`: Recursive power saving: The mechanism in which a network with s smaller calls on W roles and parameter m gives a recursion with cost ratio s/W < m, so that repeated recursion saves a power of the parameter.
- `rounding-recovery`: Exact recovery by rounding: The step in which the approximate convolution coefficients are rounded to integers, provided the error is strictly below 1/2, and carries are then propagated to give the exact binary product.
- `modular-arithmetic`: Modular arithmetic (known to the reader): Arithmetic on integers in which a and b are identified when they differ by a multiple of a fixed modulus c, written a ≡ b (mod c).
- `prime-numbers-and-greatest-common-divisors`: Prime numbers and greatest common divisors (known to the reader): A prime is an integer greater than 1 with no divisors other than 1 and itself, and gcd(a, b) is the largest integer dividing both a and b; a and b are coprime when their gcd is 1.
- `arithmetic-modulo-2-and-xor`: Arithmetic modulo 2 and XOR (known to the reader): The set {0, 1} with addition given by exclusive-or (sum modulo 2) and multiplication given by AND, which is the arithmetic of bits and parity.
- `dyadic-rationals`: Dyadic rationals (known to the reader): Rational numbers of the form a/2^k with a an integer and k a nonnegative integer, i.e. the numbers with finite binary expansions.
- `vector-spaces-subspaces-bases-and-dimension`: Vector spaces, subspaces, bases and dimension (known to the reader): A vector space is a set closed under addition and scalar multiplication; a basis is a linearly independent spanning set, and the dimension is the number of vectors in any basis.
- `linear-maps-matrix-operations-and-invertibility`: Linear maps, matrix operations and invertibility (known to the reader): A linear map sends sums to sums and scalar multiples to scalar multiples and is represented by a matrix; a square matrix is invertible when it has a two-sided inverse, and the kernel is the set of vectors sent to zero.
- `gaussian-elimination`: Gaussian elimination (known to the reader): The procedure that reduces a matrix by elementary row operations to echelon form, whose pivots determine solutions and rank.
- `triangular-matrices`: Triangular matrices (known to the reader): A square matrix whose entries above (lower-triangular) or below (upper-triangular) the diagonal are all zero.
- `dot-product-and-orthogonality-in-r-n`: Dot product and orthogonality in R^n (known to the reader): The dot product of two real vectors is the sum of products of corresponding entries; two vectors are orthogonal when their dot product is zero, and an orthonormal basis consists of mutually orthogonal unit vectors.
- `permutations-of-a-finite-set`: Permutations of a finite set (known to the reader): A bijection from a finite set of indices to itself, which rearranges the entries of a sequence or array.
- `finite-sets-subsets-and-intersections`: Finite sets, subsets and intersections (known to the reader): The intersection of two sets is the set of their common elements, the cardinality counts elements, and the binomial coefficient (n choose k) counts the k-element subsets of an n-element set.
- `graphs`: Graphs (known to the reader): A graph is a set of vertices together with a set of edges, each joining two vertices, and two vertices are adjacent when they are joined by an edge.
- `mathematical-induction`: Mathematical induction (known to the reader): A proof method that establishes a statement for all integers n by proving a base case and that the statement for smaller values implies it for n.
- `recurrence-relations-and-divide-and-conquer-recursion`: Recurrence relations and divide-and-conquer recursion (known to the reader): An equation that defines a quantity, such as the running time of a recursive algorithm, in terms of its values on smaller inputs.
- `floor-and-ceiling-functions`: Floor and ceiling functions (known to the reader): The floor of x is the largest integer not exceeding x and the ceiling is the smallest integer not less than x.
- `logarithms-base-2`: Logarithms base 2 (known to the reader): The base-2 logarithm lg x is the exponent to which 2 must be raised to give x, which is the number of binary digits needed to represent x up to one.
- `big-omega-and-big-theta-notation`: Big-Omega and big-Theta notation (known to the reader): f = Ω(g) means f is bounded below by a positive constant multiple of g for all large inputs, and f = Θ(g) means f is both O(g) and Ω(g).
- `limits-and-convergence-of-sequences-and-series`: Limits and convergence of sequences and series (known to the reader): A sequence converges to L when its terms eventually stay arbitrarily close to L, and a series converges when its partial sums converge.
- `geometric-series`: Geometric series (known to the reader): The series a + ar + ar^2 + ... whose partial sums equal a(1 - r^(k+1))/(1 - r), converging when |r| < 1 to a/(1 - r).
- `newton-s-method`: Newton's method (known to the reader): The iteration x_{k+1} = x_k - f(x_k)/f'(x_k) that approximates a root of f by repeatedly following tangent lines.
- `worst-case-time-complexity-of-a-turing-machine`: Worst-case time complexity of a Turing machine (known to the reader): For a Turing machine, the maximum number of steps it takes on any input of length n, viewed as a function of n.
- `tensor-product`: Tensor product: The tensor product V ⊗ W of two vector spaces, whose basis consists of all pairs of basis vectors of V and W, together with the tensor product A ⊗ B of linear maps, which acts on each coordinate separately.

## Unresolved terms

- "address bit"
  - on page `tensor-product`: "on several address bits"
- "chirp factors"
  - on page `cyclic-convolution`: "with chirp factors before and after it"
- "layer"
  - on page `address-interchange`: "that a layer produces"
- "signed shifts and address rearrangements"
  - on page `butterfly-operation`: "The paper's transform calculation uses address rearrangements, signed shifts, and the butterfly steps (cited)."
- "target permutation"
  - on page `bluestein-chirp`: "The target permutation is the reordering that the next stage needs of the transform output."

## New pages

New concepts the reader does not know: at most 11, and submit rejects more. Resolve the other terms to existing or known concepts, or list them under `inline`.

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

Write the answer to `exegenius/tasks/0094-extend.answer.json`, then run `exegenius submit 0094-extend` in the project directory. If submit rejects the answer, fix the answer and submit again.
