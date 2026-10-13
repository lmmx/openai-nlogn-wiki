# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/B3` (paths below are relative to it)

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

`main-result`: Integer multiplication below n log n: A fixed deterministic multitape Turing machine multiplies two n-bit integers in O(n (lg n)^(1−κ)) worst-case time with κ = 2^−182, refuting the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: An undergraduate computer scientist who has taken discrete mathematics, linear algebra, algorithms and introductory theory of computation. They know asymptotic notation, divide-and-conquer recurrences, basic number theory (divisibility, gcd, modular arithmetic, primes, Chinese remainder theorem statement), matrices and linear maps, complex numbers and roots of unity, and simple multitape Turing machines. They have not studied the FFT-based multiplication literature in depth, Nussbaumer or Bluestein transforms, fine tape-machine permutation tricks, or finite-ring and numerical-error analysis beyond basics.

## Pages, in reading order

- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen multiplied n-bit integers in O(n log n log log n) on a multitape machine and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).
- `convolution-dft`: Convolution and the discrete Fourier transform: Convolution of coefficient lists is computed by transforming with roots of unity, multiplying pointwise, and transforming back.
- `poly-ring-mod-yr1`: Polynomial ring modulo y^r + 1: Polynomials in y with complex coefficients reduced by y^r = −1; powers of y act as roots of unity and multiplying by one is a signed shift of the coefficient list.
- `hh-nlogn-multiplier`: Established O(n log n) multiplier as subroutine: The Harvey–van der Hoeven O(n log n) algorithm, called as an ordinary subroutine for short products without recursively invoking the new theorem.
- `stream-operations`: Elementary stream operations on tapes: Array order, scans, controlled shifts and rational scalings that a fixed-tape machine performs in linear time.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring where powers of y serve as roots of unity, built from address rearrangements, signed shifts and two-point butterflies (Nussbaumer).
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Placing the coefficient list on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.
- `linear-networks-frames`: Linear networks, roles and frames: A fixed linear network exchanging two banks of values with signs and restoring auxiliary values; roles are wire positions and invertible frames D_v change the stored representation so intermediate frames cancel and only an endpoint operator remains.
- `subset-network-construction`: Finite networks from three-element subsets: Gather, scatter, copy and side-injection maps on wires indexed by triples of three-element subsets, with subspace labels whose edge ranks sum to less than W·m.
- `restoring-auxiliary`: Restoring auxiliary values: Scratch registers with arbitrary initial contents are used and restored so the final effect is exact for any initial auxiliary values.
- `recursive-saving`: Recursive power saving s < Wm: Recursing at parameter m·f uses s calls at parameter f on volume V/W each; since s/W < m the volume-normalized cost grows by a factor below m per level, giving a power of the parameter below the first power.
- `address-shear`: Address shear and triangular factorization: Fields updated by (H,D) -> (H+D,D) over a residue ring; rational matrices factor as lower-triangular times partial permutation times lower-triangular, so shears run in tape order.
- `address-interchange`: Fast interchange of address fields: Exchanging two disjoint contiguous u-bit address fields of an array of volume V in O(V u^τ) time for fixed τ<1, using XOR combinations of intermediate data though the final effect is an exact permutation.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven identity expressing a Fourier transform on coprime-length axes through a transform with power-of-two lengths; the coordinate permutations are retained in the identity rather than sorted.
- `bluestein-chirp`: Bluestein chirp identity: Converts a Fourier transform (with its target permutation) into a cyclic convolution via multiplication by chirp phases; the retained source permutation cancels across forward and opposite transforms.
- `phase-twist`: Coefficient twist to the polynomial ring: A twist x_d -> ζy turning cyclic convolution of length r into convolution modulo y^r+1, whose negative wrap gives exactly the cyclic wrap once untwisted.
- `radix-digit-reduction`: Multiplication as digit convolution: Splitting the inputs into radix digits turns integer multiplication into convolution of short integer coefficients, followed by rounding and carry propagation.
- `signed-packing`: Signed coefficient packing (Kronecker substitution): Packing polynomial coefficients, including negative ones, into one long integer so a polynomial product becomes an integer product.
- `exact-ring-products`: Exact normalized polynomial products: Convolution over the ring using forward synthetic transforms, pointwise polynomial products via signed packing and the O(n log n) multiplier, and the opposite transform consuming the retained frequency order.
- `fixed-point-precision`: Fixed-point precision and exact recovery: Gaussian dyadic intermediates with one truncation after a contractive layer; accumulated error is kept below 1/2 so rounding and carries give the exact integer product.
- `butterfly-layer`: Simultaneous butterfly layer H₀: Applying H_0(u,v)=((u+v)/2,(u−v)/2) coefficientwise on selected address bits of arrays of complex fixed-point polynomial records via the recursive network, in O(V d^λ') time.
- `transform-layout`: Transform layout with retained frequency order: Tape layout on which the parallel layers apply; permutations from resampling and chirps stay inside the transform and cancel across forward, pointwise-product and opposite transforms.
- `main-algorithm`: Multiplication algorithm and its cost: Chain the reductions: digits, prime axes, resampling and chirps, phase twist, ring convolution with fast interchanges and butterfly layers, then rescaling, rounding and carries; the cost table fits n(lg n)^(1−κ).
- `main-result`: Integer multiplication below n log n: A fixed deterministic multitape Turing machine multiplies two n-bit integers in O(n (lg n)^(1−κ)) worst-case time with κ = 2^−182, refuting the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-tm`: Multitape Turing machine
- `modular-arithmetic`: Modular arithmetic
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality
- `prime-numbers`: Prime numbers
- `floor-and-ceiling-functions`: Floor and ceiling functions
- `binary-logarithm`: Binary logarithm
- `binary-representation-and-bit-strings`: Binary representation and bit strings
- `exclusive-or`: Exclusive or
- `matrices-and-linear-maps`: Matrices and linear maps
- `permutations`: Permutations
- `subspaces-dimension-and-rank`: Subspaces, dimension and rank
- `cyclic-groups-and-rings`: Cyclic groups and rings
- `cartesian-products-and-tuples`: Cartesian products and tuples
- `subsets-and-combinatorial-counting`: Subsets and combinatorial counting
- `recurrences-and-geometric-series`: Recurrences and geometric series
- `inequalities-and-error-bounds`: Inequalities and error bounds
- `gaussian-integers`: Gaussian integers
- `exponents-and-powers`: Exponents and powers
- `sorting-and-scanning-arrays`: Sorting and scanning arrays
- `schoolbook-multiplication`: Schoolbook multiplication
- `fast-fourier-transform`: Fast Fourier transform

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
