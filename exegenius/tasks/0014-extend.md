# exegenius task 0014-extend

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

For these sources: This reader has an undergraduate computer science degree: discrete mathematics (modular arithmetic, gcd and primes, binomial counting, induction), linear algebra over the reals and small fields (subspaces, rank, elimination, eigenvalues, dot-product orthogonal complements and projections), and algorithms (divide-and-conquer recurrences, Karatsuba multiplication, and the DFT and cyclic convolution as used for FFT-based polynomial multiplication). Complex numbers are known as far as roots of unity and Gaussian integers, Turing machines are known with multiple tapes, and basic probability reaches the union bound. Tensor products, bilinear forms beyond the dot product, quotient rings and the sources' network and address constructions are not part of this background.

## Sources (read them from disk)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Existing concepts

- `big-o-notation`: Big-O notation (known to the reader): A way of comparing growth rates of functions, ignoring constant factors.
- `polynomials`: Polynomials (known to the reader): Finite sums of powers of a variable with coefficients, multiplied and reduced in the usual way.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with real a and b and imaginary unit i, with i² = −1.
- `turing-machine-tapes`: Turing machines and tapes (known to the reader): A finite-state machine that reads and writes symbols on one or more tapes, each with a movable head.
- `fixed-tape-model`: Fixed-tape machine model: A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, whose size does not grow with the input.
- `exact-integer-multiplication`: Exact integer multiplication: Given binary strings x and y of length n, output the 2n-bit binary representation of their product.
- `n-log-n-conjecture`: The n log n optimality conjecture: The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers.
- `established-multiplier`: Established O(n log n) multiplier: The known fixed-tape integer multiplier running in O(n log n) time, used here only as a black-box subroutine.
- `radix-digit-convolution`: Radix-digit convolution: Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients.
- `discrete-fourier-transform`: Discrete Fourier transform (known to the reader): The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
- `cyclic-convolution`: Cyclic convolution (known to the reader): The product of two sequences in which indices wrap around modulo the sequence length.
- `gaussian-resampling`: Gaussian resampling: A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies.
- `chinese-remainder-map`: Chinese-remainder map: A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution.
- `bluestein-chirp-identity`: Bluestein's chirp identity: An identity that rewrites a Fourier transform as a cyclic convolution multiplied by chirp factors, so that it can be computed with convolution.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms whose roots of unity are powers of y in a polynomial ring, so that multiplying by a root is a signed shift of coefficients.
- `polynomial-ring-mod-yr-plus-1`: Polynomial ring modulo y^r + 1: The ring of polynomials with complex coefficients in which y^r is identified with −1, so that y has order 2r and wrap-around flips a sign.
- `phase-twist`: Phase twist: A coefficientwise multiplication by roots of unity that converts the last cyclic coordinate into a polynomial ring, so its wrap-around becomes the negative wrap of that ring.
- `signed-packing`: Signed coefficient packing: Encoding polynomial coefficients, including negative ones, as one large integer by fixed-width blocks, so that polynomial multiplication becomes integer multiplication.
- `polynomial-ring-convolution`: Convolution over the polynomial ring: The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform.
- `subspace-labels`: Subspace labels: Nondegenerate subspaces of a fixed bilinear space attached to each wire of a network, whose inclusions control how much work a change of representation costs.
- `linear-network-frames`: Linear networks and frames: A fixed linear network that exchanges two banks of values while restoring scratch values, in which each vertex carries an invertible operator called its frame.
- `subset-intersection-network`: Subset-intersection network: A linear network on the three-element subsets of a ground set, whose wires carry scalars and whose gates combine them by intersection size, so that it swaps two banks while cancelling arbitrary scratch values.
- `address-interchange`: Address-field interchange: A tape procedure that swaps two disjoint contiguous address fields of an array in time that grows like a power of the field width, rather than linearly.
- `address-shear`: Address shear: The map that updates two address fields H, D to H + D, D, which is implemented by a small number of field interchanges.
- `rank-saving-recursion`: Rank-saving recursion: The recursion in which each call splits into s smaller calls on streams of 1/W of the volume, where s < W m, so that the cost grows by the strictly smaller factor s/W per level.
- `gaussian-dyadics`: Gaussian dyadics: Complex numbers whose real and imaginary parts are integers divided by a power of two, with the Gaussian integer part also an integer.
- `complex-phase-network`: Complex phase network: A subset-intersection network whose frame change on each edge is a product of two-point kernels aI + bX on Gaussian dyadic values.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The tensor product of the two-point map H0 applied to several selected address bits at once, computed exactly in one pass rather than one axis at a time.
- `packed-bit-addition`: Packed selected-bit addition: An operation that adds one selected bit position across several address chunks at once, using cyclic shifts and a small deterministic correction for exceptional addresses.
- `guard-width-bound`: Guard-width bound: An explicit number of extra fractional and integer bits that makes every intermediate coefficient of a butterfly layer exact, so that a single final truncation suffices.
- `transform-layout`: Transform layout: A permutation of address bits that places the selected bits of all participating axes at a common offset in consecutive chunks, so that a simultaneous butterfly layer applies to each transform round.
- `prime-source-lengths`: Prime source lengths: Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box.
- `transform-identity`: Transform identity with retained permutations: The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts.
- `carry-propagation`: Carry propagation (known to the reader): Converting the recovered integer radix-digit coefficients into a binary string by adding each coefficient to a carry from the previous position.
- `recovery-and-error`: Exact coefficient recovery: The error analysis showing that the computed convolution coefficients are within a half of their true integer values, so rounding recovers them exactly.
- `main-theorem`: Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.
- `vector-spaces-subspaces-bases-and-dimension`: Vector spaces, subspaces, bases and dimension (known to the reader): A set closed under addition and scalar multiplication over a field, whose subspaces, bases and dimension are the usual notions of linear algebra.
- `rank-of-a-matrix`: Rank of a matrix (known to the reader): The number of linearly independent rows or columns of a matrix, equal to the dimension of its column space.
- `invertible-matrices-and-inverses`: Invertible matrices and inverses (known to the reader): A square matrix M is invertible when some matrix M^-1 satisfies M M^-1 = I, and then M represents a bijective linear map.
- `gaussian-elimination-and-triangular-matrices`: Gaussian elimination and triangular matrices (known to the reader): Row reduction by elementary row operations, which puts a matrix in echelon form, and matrices whose entries vanish on one side of the diagonal.
- `eigenvalues-and-diagonalization`: Eigenvalues and diagonalization (known to the reader): A scalar lambda is an eigenvalue of a matrix A when Av = lambda v for some nonzero vector v, and a matrix is diagonalizable when it is similar to a diagonal matrix.
- `dot-product-orthogonal-complement-and-projection`: Dot product, orthogonal complement and projection (known to the reader): The dot product of two vectors, the set of vectors orthogonal to every vector of a subspace, and the linear map that projects onto a subspace along a complementary subspace.
- `permutations-and-permutation-matrices`: Permutations and permutation matrices (known to the reader): A permutation is a bijection of a finite index set to itself, and its permutation matrix is the 0-1 matrix that moves coordinates accordingly.
- `modular-arithmetic`: Modular arithmetic (known to the reader): Integers a and b are congruent modulo q when q divides a minus b, and arithmetic on the residue classes Z/qZ is well defined.
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality (known to the reader): The greatest common divisor of two integers is the largest integer dividing both, computable by Euclid's algorithm, and two integers are coprime when their gcd is 1.
- `prime-numbers`: Prime numbers (known to the reader): A prime is an integer greater than 1 whose only positive divisors are 1 and itself, and every integer greater than 1 factors uniquely into primes.
- `chinese-remainder-theorem`: Chinese remainder theorem (known to the reader): For pairwise coprime moduli q_1, ..., q_k, the system of congruences x = a_i modulo q_i has a unique solution modulo their product.
- `binary-field-gf-2`: Binary field GF(2) (known to the reader): The field with two elements 0 and 1, in which addition is exclusive or (XOR) and multiplication is AND.
- `hamming-weight`: Hamming weight (known to the reader): The Hamming weight of a binary vector is its number of entries equal to 1.
- `indicator-vector-of-a-set`: Indicator vector of a set (known to the reader): The 0-1 vector of a finite set with entry 1 exactly at the elements of the set, given a fixed ordering of the ground set.
- `binomial-coefficients`: Binomial coefficients (known to the reader): The binomial coefficient C(n, k) is the number of k-element subsets of an n-element set.
- `positional-and-mixed-radix-notation`: Positional and mixed-radix notation (known to the reader): A representation of an integer as digits whose place values are powers of a fixed radix, or of a sequence of radices in the mixed-radix case.
- `dyadic-rationals`: Dyadic rationals (known to the reader): Rational numbers whose denominator is a power of two, equivalently the numbers with finitely many binary digits after the point.
- `gaussian-integers`: Gaussian integers (known to the reader): The complex numbers a + bi with integers a and b, which form a ring under complex addition and multiplication.
- `roots-of-unity`: Roots of unity (known to the reader): A complex number z is an nth root of unity when z^n = 1, and a primitive nth root has order exactly n, so its powers give all nth roots of unity.
- `mathematical-induction`: Mathematical induction (known to the reader): A proof method that establishes a statement for every integer from a base case and a proof that each case implies the next.
- `recurrence-relations-and-geometric-sums`: Recurrence relations and geometric sums (known to the reader): An equation that defines a sequence in terms of its earlier terms, solved by unrolling it, together with the geometric sum of powers of a fixed ratio.
- `iterated-logarithm`: Iterated logarithm (known to the reader): The function log* n is the number of times the base-2 logarithm must be applied to n before the result is at most 1.
- `logarithms-floor-and-ceiling`: Logarithms, floor and ceiling (known to the reader): The base-2 logarithm, written lg n or log2 n, with the floor and ceiling functions that round it to integers.
- `union-bound`: Union bound (known to the reader): The probability that at least one of finitely many events occurs is at most the sum of the probabilities of the events.
- `karatsuba-multiplication`: Karatsuba multiplication (known to the reader): The divide-and-conquer multiplication of two n-bit integers that splits each into halves and uses three half-size products, running in O(n^1.585) time.

## Unresolved terms

- "butterfly network"
  - on page `gaussian-resampling`: "which have simple butterfly networks"
- "Gaussian weights"
  - on page `gaussian-resampling`: "Gaussian weights, multiplied onto the values before and after the power-of-two transforms"
- "Strict Bernoulli inequality"
  - on page `prime-source-lengths`: "The strict Bernoulli inequality gives"

## New pages

New concepts the reader does not know: at most 2, and submit rejects more. Resolve the other terms to existing or known concepts, or list them under `inline`.

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

Write the answer to `exegenius/tasks/0014-extend.answer.json`, then run `exegenius submit 0014-extend` in the project directory. If submit rejects the answer, fix the answer and submit again.
