# exegenius task 0050-extend

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

## Unresolved terms

- "bit complexity"
  - on page `turing-machine-model`: "The model is the standard one for measuring bit complexity."
- "centred extraction"
  - on page `signed-packing`: "The paper's Lemma 17 combines exact packing, centred extraction, and negacyclic reduction"
- "complete Cartesian product of addresses"
  - on page `address-interchange`: "inside an array with a complete Cartesian product of addresses"
- "cost table"
  - on page `parameter-choice`: "They are chosen so that every term in the cost table fits the target bound."
- "cyclic-free convolution"
  - on page `radix-digit-convolution`: "The coefficients of the product polynomial are the cyclic-free convolution"
- "fixed tracks"
  - on page `turing-machine-model`: "Using fixed tracks or a fixed number of work tapes changes the time by a constant factor"
- "Frankl–Wilson construction"
  - on page `subspace-intersection-network`: "Alon presented the Frankl–Wilson construction, which represents complementary intersection graphs over different fields."
- "gather and scatter operations"
  - on page `subspace-intersection-network`: "Gather and scatter operations create coefficients that depend only on the intersection size"
- "Gaussian dyadic numbers"
  - on page `simultaneous-butterfly-layer`: "Intermediate values are exact Gaussian dyadic numbers"
- "grid values"
  - on page `multiplication-algorithm`: "Their coefficients are exact $p$-bit grid values."
- "indicator vectors"
  - on page `subspace-intersection-network`: "Indicator vectors of the subsets are used to define the coefficients of the network."
- "linear contractions"
  - on page `gaussian-resampling`: "The resampling itself uses linear contractions"
- "normalized recursive cost"
  - on page `rank-saving-recursion`: "Multiplying the parameter by $m$ therefore increases the normalized recursive cost by less than the factor $m$."
- "record"
  - on page `established-multiplier`: "It calls the established multiplier on records whose length is $O(rp)$"
- "row"
  - on page `linear-network-frames`: "the array's rows are distributed cyclically among $W$ roles"
- "sup norm"
  - on page `phase-twist`: "The map preserves the sup norm of coefficients."

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

Write the answer to `exegenius/tasks/0050-extend.answer.json`, then run `exegenius submit 0050-extend` in the project directory. If submit rejects the answer, fix the answer file and submit again.
