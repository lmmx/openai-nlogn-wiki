# exegenius task 0122-extend

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Extend a prerequisite graph of concepts built from source documents. An audit of the wiki found terms that a specific reader cannot follow and that match no existing concept. For each term, either point it at an existing concept that covers it, or add a new concept.

- Add a new concept only when no existing concept covers the term. Give each new concept an id that is not already used.
- New concepts may require existing concepts or each other; the graph must stay acyclic.
- Mark `known: true` if the reader profile already covers the concept, with `requires: []`.
- `evidence` quotes must be copied from the sources character for character, with their source id. A concept that does not appear in the sources may have no quotes.
- Give a resolution for every term.

## Target

The main result of the paper: a deterministic multitape Turing machine algorithm that multiplies n-bit integers in O(n (lg n)^(1-kappa)) time, disproving the n log n optimality conjecture in that model, and how it works

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers

## Sources (read them from disk)

- `sources/paper.txt`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Existing concepts

- `big-o-notation`: Big-O notation (known to the reader): Asymptotic upper-bound notation for growth rates of running time.
- `polynomials`: Polynomials (known to the reader): Formal sums of powers of an indeterminate with coefficients in a ring or field.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with real a, b and i squared equal to -1.
- `turing-machine-model`: Multitape Turing machine: A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, where each step moves each head by at most one cell.
- `exact-integer-multiplication`: Exact integer multiplication: Computing the exact binary representation of the product of two n-bit integers, with no rounding.
- `n-log-n-conjecture`: Schönhage–Strassen n log n conjecture: The conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
- `discrete-fourier-transform`: Discrete Fourier transform: A linear map that evaluates a sequence at powers of a root of unity, computing convolutions pointwise after transformation.
- `cyclic-convolution`: Cyclic convolution: Multiplication of two coefficient sequences as polynomials modulo x^S - 1, so that exponents wrap around modulo S.
- `radix-digit-convolution`: Radix-digit convolution: Reduction of integer multiplication to a convolution of coefficient lists obtained by splitting each input into radix digits and propagating carries.
- `chinese-remainder-map`: Chinese-remainder address map: A relabelling of a cyclic convolution of length S as a multidimensional cyclic convolution over pairwise coprime lengths, via the Chinese remainder theorem.
- `gaussian-resampling`: Gaussian resampling: A reduction that replaces a Fourier transform of arbitrary length by a multidimensional transform whose axis lengths are powers of two, using Gaussian-weighted resampling.
- `polynomial-ring-mod-yr-plus-1`: Polynomial ring modulo y^r + 1: The ring of polynomials in y with coefficients in C, reduced modulo y^r + 1 for a power of two r, in which y^r = -1.
- `synthetic-transform`: Synthetic polynomial transform: A transform over a polynomial ring modulo y^r + 1 whose roots of unity are powers of y, so that multiplying by a root is a signed cyclic shift of coefficients.
- `bluestein-chirp-identity`: Bluestein chirp identity: An identity that rewrites a discrete Fourier transform, including its target permutation, as a normalized cyclic convolution with a quadratic-phase chirp.
- `phase-twist`: Coefficient phase twist: A multiplication of coefficients by powers of a root zeta = e^(pi i / r) that converts cyclic wraparound in the last coordinate into negacyclic wraparound modulo y^r + 1, and back.
- `address-interchange`: Address-field interchange: A tape procedure that swaps two disjoint contiguous address fields of u bits in O(V u^tau) time for a fixed tau < 1, with intermediate XOR combinations but an exact final permutation.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: A tape procedure that applies the two-point map H0(u, v) = ((u + v)/2, (u − v)/2) to selected coordinate bits of all records at once, in O(V d^lambda') time.
- `linear-network-frames`: Linear networks with frames: A fixed linear network that exchanges banks of values with prescribed signs and restores auxiliary values, where each node carries an invertible frame operator so that intermediate frames cancel along a route.
- `subspace-intersection-network`: Subset-intersection subspace construction: A construction that attaches nested subspaces of a fixed space to the gates of a linear network, using three-element subsets and intersection-size parity, so that the subspace dimensions drop along each edge.
- `rank-saving-recursion`: Recursive rank saving: The recursion in which a call at parameter m uses s smaller calls with s < W m, so the cost per unit of volume is multiplied by a factor below m at each level and gives a power saving.
- `established-multiplier`: Established O(n log n) multiplier: The known deterministic O(n log n) multitape multiplication, used as an ordinary subroutine on short records.
- `signed-packing`: Signed coefficient packing: Encoding polynomial coefficients as signed integers at a fixed bit spacing so that one integer multiplication computes a polynomial product in the ring modulo y^r + 1.
- `precision-and-rounding`: Precision and exact recovery: The bookkeeping showing that fixed-precision approximations of the transforms recover each integer coefficient exactly after rounding, so that carry propagation yields the exact product.
- `parameter-choice`: Parameter choice: The fixed rational exponents and the sizes b, p, d, T and r chosen so that the cost terms all fit the target bound.
- `multiplication-algorithm`: Multiplication algorithm: The six-step algorithm that forms three source transforms, multiplies them pointwise, scales and rounds the result, and propagates carries to output the exact 2n-bit product.
- `cost-accounting`: Cost accounting: The normalized cost table showing each operation costs O(T p) times a power of p, and that every exponent falls below one by a margin of at least 2^(-181) = 2 kappa.
- `main-theorem`: Deterministic O(n (lg n)^(1-kappa)) multiplication: There is one deterministic fixed-tape Turing machine computing the exact product of n-bit integers in O(n (lg n)^(1-kappa)) worst-case time, with kappa = 2^(-182), which refutes the n log n optimality conjecture in this model.
- `bit-complexity`: Bit complexity: The running time of an algorithm measured as the number of elementary bit-level steps on a fixed machine model, as opposed to arithmetic operations on words.
- `centred-extraction`: Centred extraction: Recovering each packed coefficient as the representative in a window centred at zero, so that a signed coefficient is not confused with a large positive one.
- `cartesian-address-array`: Array with a complete Cartesian address set: An array whose addresses are all tuples in a product of ranges, stored in lexicographic order with the first coordinate most significant.
- `linear-convolution`: Linear convolution: The coefficient list of the ordinary product of two polynomials, with no reduction modulo any polynomial, so its length is the sum of the input lengths minus one.
- `fixed-tracks`: Fixed tracks: Additional fixed rows of a tape that store extra data in parallel with the main data, so that a fixed number of tracks changes the running time only by a constant factor.
- `frankl-wilson-construction`: Frankl–Wilson construction: A construction of set systems with restricted intersection sizes, which gives low-degree polynomial representations of intersection graphs over fields.
- `gather-scatter`: Gather and scatter operations: Operations that collect the entries of a network's wires over a three-element subset and redistribute them, producing coefficients that depend only on the size of the intersection of two subsets.
- `gaussian-dyadic`: Gaussian dyadic numbers: Complex numbers whose real and imaginary parts are dyadic rationals, that is, have denominators that are powers of two.
- `disk-grid-values`: Disk-grid values: Complex numbers stored exactly with p fractional bits in each real and imaginary part, with norm bounded by a fixed constant.
- `indicator-vector`: Indicator vector: A vector indexed by a ground set whose entry is 1 at the elements of a given subset and 0 elsewhere.
- `linear-contraction`: Linear contraction: A linear map that does not increase the size of its inputs, so that its output has norm at most that of the input.
- `normalized-cost`: Normalized cost: The running time of an operation divided by the stored volume V, so that costs of different operations on arrays of different sizes can be compared as powers of p.
- `record`: Record: A fixed-width block of stored data, such as one polynomial with complex coefficients, that is handled as a single unit by the procedures.
- `row-of-array`: Row of an array: The block of consecutive entries that share a fixed prefix and row index, containing all address fields after the row field.
- `sup-norm`: Sup norm: The maximum absolute value of the coefficients of a polynomial or array.

## Unresolved terms

- "CRT"
  - on page `cost-accounting`: "CRT and axis layouts"
- "linear index-code decoding"
  - on page `gather-scatter`: "The paper describes their form as that of linear index-code decoding."
- "middle transform"
  - on page `bluestein-chirp-identity`: "It is the step that turns the middle transform in the paper's algorithm into a [cyclic convolution](cyclic-convolution.md)."
- "norm"
  - on page `disk-grid-values`: "The paper's coefficient arrays consist of such values with norm less than $\tfrac14$."
- "pairing formulas"
  - on page `frankl-wilson-construction`: "These are the two pairing formulas the paper uses."
- "rational bilinear form"
  - on page `frankl-wilson-construction`: "expresses the second formula through a rational bilinear form"
- "target permutation"
  - on page `bluestein-chirp-identity`: "The paper applies the identity to a middle transform with its target permutation included."
- "transform identity"
  - on page `multiplication-algorithm`: "The permutations that appear in the transform identity are not executed as separate sorts."

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
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
          "description": "One precise sentence saying what the concept is.",
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
          "description": "Display name, e.g. \"Chirp identity\".",
          "type": "string"
        },
        "requires": {
          "description": "Ids of the concepts a reader must understand before this one.",
          "items": {
            "type": "string"
          },
          "type": "array"
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
    "resolutions": {
      "description": "For every unresolved term, the id of the concept (existing or new) that covers it.",
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

Write the answer to `exegenius/tasks/0122-extend.answer.json`, then run `exegenius submit 0122-extend` in the project directory. If submit rejects the answer, fix the answer file and submit again.
