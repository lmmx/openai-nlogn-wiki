# exegenius task 0067-extend

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Extend a prerequisite graph of concepts built from source documents. An audit of the wiki found terms that a specific reader cannot follow and that match no existing concept. For each term, either point it at an existing concept that covers it, or add a new concept.

- Add a new concept only when no existing concept covers the term. Give each new concept an id that is not already used.
- New concepts may require existing concepts or each other; the graph must stay acyclic.
- Mark `known: true` if the reader profile already covers the concept, with `requires: []`.
- `evidence` quotes must be copied from the sources character for character, with their source id. A concept that does not appear in the sources may have no quotes.
- A name with mathematics in it needs a `title` with the mathematics in LaTeX and a binding in `symbols` for every symbol in it, as in the extract task.
- Give a resolution for every term.

## Target

The main result of the paper: a deterministic multitape Turing machine algorithm that multiplies n-bit integers in O(n (lg n)^(1-kappa)) time, disproving the n log n optimality conjecture in that model, and how it works

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

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

## Unresolved terms

- "address field"
  - on page `linear-network-frames`: "a shear of two address fields"
- "Agarwal and Cooley's split"
  - on page `cyclic-convolution`: "Agarwal and Cooley's split is the model:"
- "axis"
  - on page `simultaneous-butterfly-layer`: "one axis per chunk"
- "bilinear form and orthogonality"
  - on page `subset-intersection-network`: "a nondegenerate subspace of a fixed bilinear space, meaning one on which the form restricts to a nonsingular form"
- "bilinear product"
  - on page `recovery-and-error`: "For a bilinear product of two approximate operands"
- "bilinear space and bilinear form"
  - on page `subspace-labels`: "a nondegenerate subspace of a fixed bilinear space"
- "binary change of basis"
  - on page `simultaneous-butterfly-layer`: "to implement its binary changes of basis"
- "bit procedure"
  - on page `linear-network-frames`: "For the bit procedure, the endpoint operator is a shear of two address fields"
  - on page `address-shear`: "of the bit procedure"
- "butterfly"
  - on page `simultaneous-butterfly-layer`: "separate butterfly factors"
- "carry scan"
  - on page `polynomial-ring-convolution`: "can be recovered by a carry scan"
- "centered residue"
  - on page `polynomial-ring-convolution`: "so each coefficient is the centered residue of its block modulo $B_0$"
- "coefficient layout"
  - on page `cyclic-convolution`: "its coefficient layout and its middle transform both become cyclic convolutions"
- "complex variant"
  - on page `subset-intersection-network`: "The complex variant uses the same schedule with the scalars and neighbour rule changed: even intersection."
- "congruence modulo B"
  - on page `signed-packing`: "$f(B)\,g(B) \equiv c \pmod B$"
- "contraction"
  - on page `guard-width-bound`: "the intermediate operators need not be contractions"
- "controlled cyclic shift"
  - on page `packed-bit-addition`: "A controlled cyclic shift of the target chunk"
- "convolution"
  - on page `discrete-fourier-transform`: "The argument needs these transforms for convolution."
- "coprime"
  - on page `prime-source-lengths`: "Distinct primes are pairwise coprime"
- "coprime (gcd)"
  - on page `transform-identity`: "coprimality makes each map a bijection"
- "cost"
  - on page `exact-integer-multiplication`: "Costs are measured on a machine whose alphabet and number of tapes are fixed in advance."
- "cost table"
  - on page `established-multiplier`: "so its running time enters the new algorithm's cost table"
  - on page `packed-bit-addition`: "keeps each layer inside the cost table of the theorem"
- "destination rank"
  - on page `packed-bit-addition`: "reinserts it at its destination rank"
- "endpoint operator"
  - on page `address-shear`: "on every role, the endpoint operator is this shear"
- "finite field F_2"
  - on page `complex-phase-network`: "Here $x \in \mathbb{F}_2^m$ is a binary address"
- "gate and terminal of a network"
  - on page `subspace-labels`: "attached to each gate and terminal of a network"
- "Gaussian integer"
  - on page `subspace-labels`: "a Gaussian integer divided by $2^m$"
- "Gaussian weights"
  - on page `gaussian-resampling`: "using Gaussian weights to move between the two sets of frequencies"
- "generator"
  - on page `chinese-remainder-map`: "Define $\Phi$ on the generator by"
- "grid numerators"
  - on page `recovery-and-error`: "Each acts exactly on grid numerators"
- "ground set"
  - on page `subspace-labels`: "Let $h$ be the size of a ground set"
- "indicator vector"
  - on page `subspace-labels`: "with indicator vector $t_T\in\mathbb{Q}^h$"
- "invertible modulo q"
  - on page `address-shear`: "chosen so that the denominators of the rational matrices used below are invertible modulo $q$."
- "kernel"
  - on page `gaussian-dyadics`: "The paper's kernels stay in this set."
- "last cyclic coordinate"
  - on page `phase-twist`: "the last cyclic coordinate of a convolution becomes a coordinate of the"
- "limit inferior"
  - on page `fixed-tape-model`: "has limit inferior zero"
  - on page `n-log-n-conjecture`: "$\liminf_{n\to\infty} T_A(n)/(n\lg n) = 0$"
- "line spanned by a vector"
  - on page `subspace-labels`: "so the line spanned by $t_T$ is nondegenerate"
- "linear algebra: invertible linear operator, matrix, inverse"
  - on page `linear-network-frames`: "choose an invertible linear operator $D_v$ on these arrays"
- "linear map"
  - on page `discrete-fourier-transform`: "A linear map $L$ is a contraction"
  - on page `transform-identity`: "A linear map is a contraction if it does not increase the maximum modulus of a vector."
- "little-o notation"
  - on page `guard-width-bound`: "$\Delta$ is $o(p)$"
  - on page `recovery-and-error`: "$\gamma = o(b)$"
- "matrix"
  - on page `address-shear`: "For a fixed rational $m \times m$ matrix $M$"
- "middle transform"
  - on page `cyclic-convolution`: "its middle transform both become cyclic convolutions"
  - on page `bluestein-chirp-identity`: "converts the middle transform"
- "mixed-radix digit"
  - on page `chinese-remainder-map`: "Let $a_j$ be the mixed-radix digit of $k$ on axis $j$"
- "mixed-radix digits"
  - on page `prime-source-lengths`: "relabels coefficient positions by mixed-radix digits"
- "modulo"
  - on page `transform-identity`: "taken modulo $q$"
- "multidimensional transforms with power-of-two axes"
  - on page `gaussian-resampling`: "multidimensional transforms with power-of-two axes"
- "norm of an array"
  - on page `recovery-and-error`: "so every norm is at most one and the two errors simply add"
- "normalizations and known scales"
  - on page `recovery-and-error`: "Two exact multiplications by known scales undo the normalizations."
- "normalized cyclic convolution"
  - on page `bluestein-chirp-identity`: "into a normalized cyclic convolution"
- "numerical layer"
  - on page `rank-saving-recursion`: "or the number of selected axes in a numerical layer."
- "Nussbaumer and Quandalle"
  - on page `synthetic-transforms`: "of Nussbaumer and Quandalle."
- "opposite-sign transform"
  - on page `transform-identity`: "the opposite-sign transform"
- "Opposite transform"
  - on page `transform-layout`: "and the opposite transform reads them in that order."
  - on page `recovery-and-error`: "an opposite transform, with one truncation in the product"
- "padded transform box"
  - on page `recovery-and-error`: "the number of entries in the padded transform box"
- "pairwise coprime source lengths"
  - on page `recovery-and-error`: "the product of the pairwise coprime source lengths"
- "payloads"
  - on page `packed-bit-addition`: "over all payloads."
- "phase factors and scalar corrections"
  - on page `gaussian-dyadics`: "the phase factors and scalar corrections stay in the same set"
- "polynomial ring"
  - on page `signed-packing`: "Here $y$ is the indeterminate of the polynomial ring."
- "polynomial transforms"
  - on page `gaussian-resampling`: "The polynomial transforms of the later steps keep this layered structure"
- "rational rank"
  - on page `address-shear`: "which is its rank as a matrix over the rational numbers"
- "remaining axes"
  - on page `polynomial-ring-convolution`: "computed along the remaining axes after the earlier reductions"
- "ring homomorphism and ring isomorphism"
  - on page `chinese-remainder-map`: "extend it to polynomials as a ring homomorphism"
- "scalar sign of a route"
  - on page `linear-network-frames`: "together with the scalar sign of that route."
- "schoolbook multiplication"
  - on page `main-theorem`: "Inputs below a fixed cutoff are multiplied by schoolbook multiplication, and the cutoff is absorbed into the constant."
- "scratch chunk"
  - on page `packed-bit-addition`: "which change the target and scratch chunks"
- "scratch values"
  - on page `address-interchange`: "restores its scratch values"
- "stable radix sort"
  - on page `packed-bit-addition`: "after a stable radix sort of the extracted records"
- "subset-intersection network and complex phase network"
  - on page `subspace-labels`: "the subset-intersection network and the complex phase network that follow"
- "tape procedure for interchanging address chunks"
  - on page `address-shear`: "the tape procedure for interchanging two address chunks reduces"
- "target chunk"
  - on page `packed-bit-addition`: "Before any update, the target chunk is moved beside its controls."
- "target permutation"
  - on page `bluestein-chirp-identity`: "including its target permutation"
- "tensor power"
  - on page `complex-phase-network`: "the $m$-fold tensor power of $H$"
- "tensor product"
  - on page `simultaneous-butterfly-layer`: "as one tensor product"
  - on page `guard-width-bound`: "By the definition of the tensor product"
- "the argument"
  - on page `polynomial-ring-mod-yr-plus-1`: "The argument stores one coordinate of its array in this ring"
  - on page `bluestein-chirp-identity`: "In the argument, this is the step"
- "the paper"
  - on page `bluestein-chirp-identity`: "The paper states the step as into normalized cyclic convolution."
- "transform"
  - on page `radix-digit-convolution`: "Its work is set by how the transforms move the $2q-1$ coefficients."
- "transform round"
  - on page `packed-bit-addition`: "Each binary basis change in a transform round is paid for at this cost"
- "truncation"
  - on page `simultaneous-butterfly-layer`: "truncates only once, at the end"
- "union bound"
  - on page `packed-bit-addition`: "A union bound over them shows that"
- "XOR"
  - on page `packed-bit-addition`: "the selected bit of $W$ is XORed with the selected bit of $X$"

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

Write the answer to `exegenius/tasks/0067-extend.answer.json`, then run `exegenius submit 0067-extend` in the project directory. If submit rejects the answer, fix the answer and submit again.
