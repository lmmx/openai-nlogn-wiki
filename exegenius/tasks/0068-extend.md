# exegenius task 0068-extend

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

For these sources: The reader has completed an undergraduate computer science degree: big-O analysis, polynomials and complex numbers, and Turing machines with tapes, plus the discrete mathematics and first linear algebra course that such a degree requires. For the paper this means modular arithmetic, gcd and primes, roots of unity, binary arithmetic over F2 with Hamming weight, and basic vector-space and matrix facts (subspaces, rank, projections, dot product, eigenvalues) at first-course depth. Bilinear forms, tensor products, finite-field and ring theory, the Chinese remainder theorem, Newton iteration and the Fourier and convolution machinery beyond the basics are treated as not known.

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
- `discrete-fourier-transform`: Discrete Fourier transform: The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q.
- `cyclic-convolution`: Cyclic convolution: The product of two sequences in which indices wrap around modulo the sequence length.
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
- `carry-propagation`: Carry propagation: Converting the recovered integer radix-digit coefficients into a binary string by adding each coefficient to a carry from the previous position.
- `recovery-and-error`: Exact coefficient recovery: The error analysis showing that the computed convolution coefficients are within a half of their true integer values, so rounding recovers them exactly.
- `main-theorem`: Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.
- `mathematical-induction`: Mathematical induction (known to the reader): A proof method that establishes a statement for all natural numbers by proving a base case and that each case implies the next.
- `logarithms-and-floor-and-ceiling-functions`: Logarithms and floor and ceiling functions (known to the reader): The logarithm inverts exponentiation, and the floor and ceiling functions round a real number down or up to an integer.
- `binary-representation-of-integers`: Binary representation of integers (known to the reader): Every nonnegative integer has a unique representation as a finite sum of powers of two with coefficients 0 or 1, written as a string of bits.
- `dyadic-rationals`: Dyadic rationals (known to the reader): Rational numbers whose denominator is a power of two, equivalently those with a finite binary expansion.
- `modular-arithmetic`: Modular arithmetic (known to the reader): Integers a and b are congruent modulo m when m divides their difference, and arithmetic is carried out on remainders after division by m.
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality (known to the reader): The greatest common divisor of two integers is the largest integer dividing both, computed by the Euclidean algorithm, and two integers are coprime when their gcd is 1.
- `prime-numbers`: Prime numbers (known to the reader): A prime is an integer greater than 1 whose only positive divisors are 1 and itself, and every integer greater than 1 factors uniquely into primes.
- `roots-of-unity`: Roots of unity (known to the reader): A complex number z is an n-th root of unity when z^n = 1, and a primitive n-th root of unity is one whose successive powers give all n of the n-th roots.
- `binary-field-f2-and-xor-arithmetic`: Binary field F2 and XOR arithmetic (known to the reader): The integers modulo 2, with addition given by exclusive or and multiplication by logical AND, in which each element is its own additive inverse.
- `hamming-weight`: Hamming weight (known to the reader): The Hamming weight of a binary string is the number of positions that hold a 1.
- `vector-spaces-and-subspaces`: Vector spaces and subspaces (known to the reader): A vector space is a set closed under addition and scalar multiplication, and a subspace is a subset that is itself a vector space; a basis is a linearly independent spanning set and the dimension is the size of any basis.
- `matrices-and-linear-maps`: Matrices and linear maps (known to the reader): A matrix represents a linear map between finite-dimensional vector spaces, and matrices multiply, invert and transpose in the standard way.
- `matrix-rank`: Matrix rank (known to the reader): The rank of a matrix is the dimension of its column space, which equals the maximum number of linearly independent columns.
- `projection-onto-a-subspace`: Projection onto a subspace (known to the reader): A projection is a linear map P with P squared equal to P, which fixes its image pointwise and maps onto a chosen subspace.
- `dot-product-and-orthogonality`: Dot product and orthogonality (known to the reader): The dot product of two vectors is the sum of the products of their corresponding coordinates, and two vectors are orthogonal when their dot product is zero.
- `eigenvalues-and-eigenvectors`: Eigenvalues and eigenvectors (known to the reader): A scalar lambda is an eigenvalue of a square matrix A when some nonzero vector v satisfies Av = lambda v, and such a v is an eigenvector.

## Unresolved terms

- "address"
  - on page `linear-network-frames`: "a scalar gate is applied pointwise to matching addresses on the roles it touches"
- "bilinear form"
  - on page `subspace-labels`: "Let $F$ be the fixed bilinear space"
- "bit procedure"
  - on page `address-shear`: "For the bit procedure, the endpoint operator"
- "butterfly layers"
  - on page `gaussian-dyadics`: "The butterfly layers keep every value in this form"
- "completed complex layer"
  - on page `complex-phase-network`: "It carries the completed complex layer"
- "convolution"
  - on page `transform-identity`: "a convolution can compose them"
  - on page `synthetic-transforms`: "Both forward transforms in a convolution use the same"
- "coordinate ranges"
  - on page `packed-bit-addition`: "Let $N_0,\dots,N_3$ be the sizes of the four other coordinate ranges"
- "cyclic product (cyclic convolution)"
  - on page `polynomial-ring-convolution`: "is the cyclic product of two arrays of records"
- "fixed-tape machine"
  - on page `exact-integer-multiplication`: "gives a deterministic fixed-tape machine"
- "Gather and scatter"
  - on page `subset-intersection-network`: "Gather and scatter create coefficients that depend on intersection size"
- "layouts of the multiplication algorithm"
  - on page `simultaneous-butterfly-layer`: "On the layouts of the multiplication algorithm"
- "nondegenerate form"
  - on page `subspace-labels`: "assume $F$ is nondegenerate"
- "normalized cyclic convolution"
  - on page `bluestein-chirp-identity`: "normalized cyclic convolution"
- "numerical layer"
  - on page `rank-saving-recursion`: "of selected axes for a numerical layer"
- "opposite transform G"
  - on page `polynomial-ring-convolution`: "and $G$ the opposite transform"
- "order of an element"
  - on page `synthetic-transforms`: "so $y$ has order $2r$"
- "Restricted machine model"
  - on page `n-log-n-conjecture`: "a faster bound in a restricted machine model does not by itself settle it in general."
- "scalar gate"
  - on page `linear-network-frames`: "a scalar gate is applied pointwise"
- "selected bits"
  - on page `transform-layout`: "A round acts on the selected bits of the participating axes"
- "streaming operations"
  - on page `packed-bit-addition`: "The construction is built from three streaming operations"
- "streams"
  - on page `address-interchange`: "applied recursively to streams holding a fraction of the volume"
- "tensor product"
  - on page `simultaneous-butterfly-layer`: "computing the tensor product exactly in one pass"
- "transform layers"
  - on page `address-interchange`: "The main result uses it to make the transform layers cheap"
- "transforms"
  - on page `radix-digit-convolution`: "The convolution is the object that transforms can compute quickly on a fixed layout"

## New pages

New concepts the reader does not know: at most 16, and submit rejects more. Resolve the other terms to existing or known concepts, or list them under `inline`.

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

Write the answer to `exegenius/tasks/0068-extend.answer.json`, then run `exegenius submit 0068-extend` in the project directory. If submit rejects the answer, fix the answer and submit again.
