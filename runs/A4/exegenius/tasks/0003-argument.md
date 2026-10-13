# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/A4` (paths below are relative to it)

Reconstruct the plan of the argument the sources make for the target result, as a tree of steps. Writers of the wiki's pages are given their page's step, and readers are shown where each page fits, so the plan says what each page is for.

- The root is the intention to show the target result. Each `show` step names a `method` that splits its claim into sub-steps, and a `motivation`: why that method suits the claim. Its `children` are the sub-steps, in the order the method takes them. An `infer` step is a single step the sources report: give its `quote`, copied exactly, and no children.
- Read the plan top down, as a reader of the sources would: "we show that", "it suffices to", "the key step is" and section structure mark the steps. Go down to the level the pages need: every page below is either the module that presents one step (`page`) or a concept some step relies on (`from`). Deeper steps of a page's own proof can stop at an `infer` step quoting where the sources carry them out.
- The sources report the plan in order: the infer steps' quotes must appear in the sources in the order of a depth-first walk of the tree (submit checks it). Mark an infer step `deferred` if the sources report it out of order.
- `motivation.source`: `explicit` if the sources state why the method is used (quote them), `recoverable` if a reader could work it out from what they say, `reconstructed` if you supply it. Do not mark a motivation explicit unless you can quote it. Writers are told to give readers every reconstructed motivation, since the sources will not.
- `from`: the concepts a step relies on, as ids: known concepts, or pages that come before the step's page in the reading order below. A step's page is its own `page` or the nearest ancestor's.
- `salient`: for a step whose claim has a feature a reader would find striking (a symmetry, a uniformity across cases, a surprising value or bound), that feature. A proof explains a result only relative to such a feature (Lange), so its page is asked to explain why the feature holds. Most steps have none.
- `adds`: symbols a step introduces for its sub-steps, each occurring in the mathematics ($...$) of the claims below it, with a display name, meaning and relation as for concept names.
- The target page presents the root. Give each other page at most one step; a page that presents no step must be in some step's `from`.

## Target

`fast-multiplication`: Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape algorithm: digit convolution, CRT prime axes, Gaussian resampling, Bluestein chirps, phase twist, synthetic transforms with fast interchanges and butterfly layers, then rounding and carries; time O(n (lg n)^(1−κ)), κ=2^−182, disproving the n log n conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: An undergraduate computer science reader who knows asymptotic notation, basic discrete mathematics, linear algebra over the reals and complex numbers, elementary algebra (groups, rings, modular arithmetic, polynomials), elementary number theory (primes, CRT) and basic probability/combinatorics. They know basic Turing machines and tapes and the schoolbook and Karatsuba multiplication, and probably the FFT as an algorithm. They have not studied multitape-machine algorithm engineering, Schönhage–Strassen or later multiplication algorithms, or specialist linear-algebra constructions such as Bruhat factorizations.

## Pages, in reading order

- `multitape-model`: Fixed multitape Turing machine model: Deterministic Turing machine with a fixed finite alphabet and fixed finite number of one-dimensional tapes; the model in which time is measured.
- `known-nlogn`: Established O(n log n) multiplication and history: Schönhage–Strassen O(n log n log log n), Fürer, and Harvey–van der Hoeven O(n log n) multiplication on multitape machines, with n log n conjectured optimal; the O(n log n) multiplier is used as a subroutine.
- `convolution-dft`: Convolution and Fourier transforms: Cyclic convolution of sequences, computed by transforming, multiplying pointwise and inverse-transforming using roots of unity.
- `radix-digit-reduction`: Multiplication as convolution of radix digits: Split each integer into digits in a radix, so the product becomes a convolution of short integer coefficient lists followed by carry propagation.
- `ring-mod-yr`: Polynomial ring modulo y^r + 1: Complex polynomials in y reduced modulo y^r+1, so y^r = −1; multiplying by a power of y is a signed cyclic shift of the coefficient list and powers of y act as roots of unity.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring where roots of unity are powers of y, so root multiplication is a signed shift (Nussbaumer, Quandalle).
- `elementary-scans`: Array order and elementary tape scans: Storing arrays in address order on tapes and performing basic scans, copies and streams in linear time.
- `butterfly-h0`: Two-point butterfly H₀: The map H0(u,v) = ((u+v)/2,(u−v)/2) applied coefficientwise; the basic arithmetic step of a transform layer.
- `multidim-transform`: Multidimensional transform with power-of-two axes: Fourier transform on an array indexed by several axes, computed one axis at a time by butterflies; axis lengths are powers of two.
- `linear-network-frames`: Linear networks, roles and frames: A fixed linear gate network exchanges banks of values with signs and restores auxiliary values; roles are wire positions applied pointwise to role streams, and frames D_v are invertible operators changing stored representation along edges so intermediate frames cancel.
- `address-shear`: Address shear and restoration of scratch values: The endpoint operator (H,D)↦(H+D,D) on address fields over a residue ring, obtained via a Bruhat-type factorization; scratch registers are restored for arbitrary initial contents.
- `subset-finite-network`: Finite networks from three-element subsets: Fixed networks with nested subspaces attached to gates built from 3-element subsets (Frankl–Wilson style intersection counts, index-code gather/scatter, cancelling auxiliary wires), using s < W m smaller calls.
- `recursive-saving`: Recursive power saving from s < Wm: A call at parameter mf makes s calls at parameter f on streams of volume V/W; since s/W < m the per-volume cost grows slower than the parameter, giving a power saving.
- `address-interchange`: Fast interchange of address chunks: Tape procedure swapping two disjoint address fields of u bits in an array of stored volume V at cost O(V u^τ), τ<1, via XOR combinations that net to an exact permutation.
- `crt-prime-axes`: Chinese-remainder map to distinct prime cyclic axes: Re-index the digit list over a product of cyclic axes of distinct prime lengths by the Chinese remainder theorem, preserving convolution; implemented by triangular controlled shifts and axis moves.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven technique expressing a Fourier transform over prime axes via a power-of-two tensor transform, with source and target permutations kept inside the identity.
- `bluestein-chirp`: Bluestein's chirp identity: Rewrites a DFT of arbitrary length as a cyclic convolution with a chirp sequence, here converting the middle transform and its permutation into normalized cyclic convolution.
- `phase-twist`: Last-coordinate phase twist: Multiply by roots-of-unity phases so a cyclic coordinate becomes a polynomial modulo y^r+1, whose negative wrap equals the original cyclic wrap after untwisting.
- `fixed-point-precision`: Fixed-point complex coefficients and exact recovery: Numerical records use complex fixed-point numbers (Gaussian dyadics); with total error below 1/2, rounding recovers exact integer coefficients and carries give the binary product.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Tape procedure applying H0 simultaneously on one selected bit in each of d address chunks of numerical arrays at cost O(V d^λ'), using phase frames and one truncation after the contractive layer.
- `synthetic-layout`: Synthetic transforms on tape layouts: Layout storing roots, butterflies and frequency order so that the two forward transforms keep the same frequency order through the pointwise product and the opposite transform consumes it.
- `kronecker-packing`: Signed coefficient packing (Kronecker substitution): Encode a polynomial with bounded integer coefficients as one integer by evaluating at a power of two with signed digits, so a polynomial product becomes an integer product.
- `ring-products`: Exact polynomial-ring products: Products in the ring modulo y^r+1 computed by signed packing and the established O(n log n) multiplier as subroutine, giving normalized convolution.
- `fast-multiplication`: Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape algorithm: digit convolution, CRT prime axes, Gaussian resampling, Bluestein chirps, phase twist, synthetic transforms with fast interchanges and butterfly layers, then rounding and carries; time O(n (lg n)^(1−κ)), κ=2^−182, disproving the n log n conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-tapes`: Turing machines and tapes
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `primes-and-divisibility`: Primes and divisibility
- `linear-algebra-over-fields`: Linear algebra over fields
- `permutations-and-bijections`: Permutations and bijections
- `groups-and-rings-basic-algebra`: Groups and rings (basic algebra)
- `finite-sets-and-elementary-combinatorics`: Finite sets and elementary combinatorics
- `floating-and-fixed-point-approximation-and-rounding`: Floating and fixed-point approximation and rounding
- `recurrences-and-divide-and-conquer-analysis`: Recurrences and divide-and-conquer analysis
- `logarithms-and-exponentials`: Logarithms and exponentials
- `fast-fourier-transform-algorithm`: Fast Fourier transform algorithm
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication
- `floor-ceiling-and-big-omega-notation`: Floor, ceiling and big-omega notation

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

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
    "Intention": {
      "oneOf": [
        {
          "const": "show",
          "description": "Show a claim by a method that splits it into sub-steps.",
          "type": "string"
        },
        {
          "const": "infer",
          "description": "Infer one claim in a single step the sources report.",
          "type": "string"
        }
      ]
    },
    "Motivation": {
      "additionalProperties": false,
      "description": "Why a method suits the claim it shows.",
      "properties": {
        "quote": {
          "anyOf": [
            {
              "$ref": "#/$defs/Evidence"
            },
            {
              "type": "null"
            }
          ],
          "description": "For an explicit motivation, the sources' words, copied exactly."
        },
        "source": {
          "$ref": "#/$defs/Provenance",
          "description": "Whether the sources state the reason, leave it to be worked out, or neither."
        },
        "text": {
          "description": "The reason, in one or two sentences.",
          "type": "string"
        }
      },
      "required": [
        "text",
        "source"
      ],
      "type": "object"
    },
    "Node": {
      "additionalProperties": false,
      "description": "One step of the argument.",
      "properties": {
        "adds": {
          "description": "Symbols the step introduces, in force in its sub-steps.",
          "items": {
            "$ref": "#/$defs/Binding"
          },
          "type": "array"
        },
        "children": {
          "description": "For a show step: its sub-steps, in the order the method takes them.",
          "items": {
            "$ref": "#/$defs/Node"
          },
          "type": "array"
        },
        "claim": {
          "description": "What the step shows or infers, in one sentence, with mathematics in LaTeX ($...$).",
          "type": "string"
        },
        "deferred": {
          "description": "For an infer step the sources report out of order, before or after the steps around\nit.",
          "type": "boolean"
        },
        "from": {
          "default": [],
          "description": "Ids of the concepts the step relies on: known concepts, or pages before the step's\npage.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "id": {
          "description": "A short label, unique in the tree, such as \"S0\" or \"S2.1\".",
          "type": "string"
        },
        "intention": {
          "$ref": "#/$defs/Intention"
        },
        "method": {
          "description": "For a show step: how the claim is shown, in a phrase (\"reduce to a cyclic\nconvolution and bound its cost\").",
          "type": [
            "string",
            "null"
          ]
        },
        "motivation": {
          "anyOf": [
            {
              "$ref": "#/$defs/Motivation"
            },
            {
              "type": "null"
            }
          ],
          "description": "For a show step: why that method suits the claim."
        },
        "page": {
          "description": "Id of the page that presents this step and its sub-steps, if one does.",
          "type": [
            "string",
            "null"
          ]
        },
        "quote": {
          "anyOf": [
            {
              "$ref": "#/$defs/Evidence"
            },
            {
              "type": "null"
            }
          ],
          "description": "For an infer step: the step as the sources report it, copied exactly."
        },
        "salient": {
          "description": "For a step whose claim has a feature a reader would find striking (a symmetry, a\nuniformity across cases, a surprising value or bound): that feature. The page should\nexplain why it holds, from a matching feature of the method.",
          "type": [
            "string",
            "null"
          ]
        }
      },
      "required": [
        "id",
        "intention",
        "claim"
      ],
      "type": "object"
    },
    "Provenance": {
      "oneOf": [
        {
          "const": "explicit",
          "description": "The sources state the reason; quote them.",
          "type": "string"
        },
        {
          "const": "recoverable",
          "description": "The sources do not state it, but a reader can work it out from what they say.",
          "type": "string"
        },
        {
          "const": "reconstructed",
          "description": "The sources neither state it nor make it recoverable: you supply it.",
          "type": "string"
        }
      ]
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
  "properties": {
    "root": {
      "$ref": "#/$defs/Node",
      "description": "The main step: to show the target result."
    }
  },
  "required": [
    "root"
  ],
  "title": "ArgumentAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0003-argument.answer.json`, then run `exegenius submit 0003-argument` in the project directory. If submit rejects the answer, fix the answer and submit again.
