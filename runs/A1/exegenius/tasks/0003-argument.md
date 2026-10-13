# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/A1` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time with κ=2^−182, by chaining digit convolution, Chinese-remainder map, Gaussian resampling, chirps, twist, and synthetic transforms accelerated by fast interchanges and butterfly layers.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: asymptotic analysis, recursion and divide-and-conquer recurrences, basic discrete mathematics (modular arithmetic, primes, Chinese remainder theorem, permutations, sets), and introductory linear algebra (vectors, matrices, invertible maps, subspaces, triangular matrices, Gaussian elimination). They know binary arithmetic, schoolbook and Karatsuba multiplication, and basic Turing machines with tapes. They have not studied abstract algebra beyond basics, the FFT in depth, Schönhage-Strassen, Nussbaumer transforms, or fast multitape tape-programming techniques; those are explained by the wiki.

## Pages, in reading order

- `convolution`: Convolution and cyclic convolution: Combining two coefficient lists so entry k sums products of entries whose indices add to k (cyclically modulo the length in the cyclic case); this is polynomial multiplication.
- `radix-digit-convolution`: Multiplication as radix-digit convolution: Split each integer into short radix digits so the product becomes a convolution of integer coefficient lists; carries then give the exact product.
- `ring-mod-yr`: Polynomial ring modulo y^r + 1: Complex polynomials in y of degree below r multiplied with y^r replaced by -1; powers of y act as roots of unity, so multiplying by one is a signed cyclic shift of the coefficient list.
- `dft`: Fourier transform and roots of unity: The discrete Fourier transform evaluates a coefficient list at powers of a root of unity, turning convolution into pointwise product; fast algorithms compute it in layers of two-point butterflies.
- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's 1971 O(n log n log log n) multitape multiplication and their proposal that n log n is optimal; Harvey and van der Hoeven later reached O(n log n).
- `tape-arrays-and-streams`: Arrays on tapes, scans and stored bit volume: Data is stored as arrays addressed by fields of bits in a fixed order on tapes; elementary scans and stream operations cost time linear in the stored bit volume.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the ring modulo y^r+1 that use powers of y as roots of unity, so each transform consists of address rearrangements, signed shifts and butterflies (Nussbaumer; Quandalle and Nussbaumer).
- `linear-networks-frames`: Linear networks with roles and frames: A fixed linear network of scalar gates exchanging banks of values and restoring auxiliary values is applied to row streams, one role per wire; a frame is an invertible operator giving the stored representation, and intermediate frames cancel leaving an endpoint operator.
- `controlled-shifts`: Controlled shifts and carries by packing: Elementary tape procedures that shift records by amounts given by control values, used to implement signed shifts and address maps.
- `address-shear`: Address shear and lower triangular factorization: The endpoint operator of the bit network updates two address fields by (H,D)↦(H+D,D); rank reduction via a Bruhat-type factorization into lower-triangular matrices makes such shears cheap on tape.
- `chinese-remainder-address-map`: Chinese-remainder map onto prime cyclic axes: A map placing the radix-digit coefficient list on a product of distinct prime cyclic axes that preserves convolution, implemented by triangular controlled shifts and axis moves.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing each Fourier transform of prime length through a multidimensional transform with power-of-two axis lengths; source and target permutations stay inside the identity instead of being executed as sorts.
- `bluestein-chirp`: Bluestein chirp conversion: Bluestein's chirp identity rewrites a Fourier transform as a convolution with chirp factors, so the middle transform with its target permutation becomes a normalized cyclic convolution.
- `phase-twist`: Last-coordinate phase twist: A phase twist changes the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap gives the original cyclic wrap once the twist is removed.
- `signed-packing`: Signed coefficient packing (Kronecker substitution) and the n log n subroutine: Polynomial products over the ring are computed by packing signed coefficients into long integers and calling the established O(n log n) multiplier as an ordinary subroutine.
- `restoring-auxiliary-values`: Restoring auxiliary values: Scratch registers with arbitrary initial contents are subtracted, used, added back and the computation reversed, so every auxiliary value is restored (transparent computation).
- `finite-subset-network`: Finite network from three-element subsets: A fixed small network built from three-element subsets of an m-dimensional ground set, with gather, scatter and auxiliary wires cancelling unwanted coefficients, assigning nested subspaces to gates so the number s of smaller calls satisfies s<Wm.
- `recursive-power-saving`: Recursive power saving: A recursive call at parameter mf uses s<Wm calls at parameter f on streams of volume V/W, so dividing by volume the cost grows by factor s/W<m per multiplication of the parameter by m, giving a power rather than a logarithmic saving.
- `address-interchange`: Fast address-field interchange: Interchanging two disjoint contiguous address fields of u bits in a Cartesian-product array at cost O(V u^τ) for a fixed τ<1, via intermediate XOR combinations whose final effect is an exact permutation.
- `butterfly-layer`: Simultaneous butterfly layer: The map H₀(u,v)=((u+v)/2,(u−v)/2) applied coefficientwise to polynomial records at one chosen bit position in each of d address chunks at cost O(V d^λ′), using exact Gaussian dyadic intermediates and one truncation afterward.
- `transform-layout-convolution`: Synthetic transform layout and convolution: Forward synthetic transforms keep the same frequency order through the pointwise product and the opposite transform consumes it, so convolution over the ring is computed on the retained layout using fast butterfly layers and address interchanges.
- `precision-exact-recovery`: Precision, rounding and carry propagation: After removing known normalizations and digit scales, the recovered coefficient error is shown strictly below 1/2, so rounding gives exact integer coefficients and carries yield the binary product.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time with κ=2^−182, by chaining digit convolution, Chinese-remainder map, Gaussian resampling, chirps, twist, and synthetic transforms accelerated by fast interchanges and butterfly layers.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-turing-machine`: Multitape Turing machine
- `logarithms-and-iterated-logarithms`: Logarithms and iterated logarithms
- `binary-representation-of-integers`: Binary representation of integers
- `positional-radix-notation`: Positional radix notation
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication
- `recursion-and-divide-and-conquer-recurrences`: Recursion and divide-and-conquer recurrences
- `modular-arithmetic`: Modular arithmetic
- `primes-and-coprimality`: Primes and coprimality
- `chinese-remainder-theorem`: Chinese remainder theorem
- `permutations-and-bijections`: Permutations and bijections
- `vectors-matrices-and-linear-maps`: Vectors, matrices and linear maps
- `subspaces-dimension-and-linear-independence`: Subspaces, dimension and linear independence
- `triangular-matrices-and-gaussian-elimination`: Triangular matrices and Gaussian elimination
- `bitwise-operations-and-xor`: Bitwise operations and XOR
- `cartesian-products-and-multidimensional-arrays`: Cartesian products and multidimensional arrays
- `sets-and-subsets`: Sets and subsets
- `rationals-rounding-and-error-bounds`: Rationals, rounding and error bounds
- `dyadic-rationals-and-fixed-point-numbers`: Dyadic rationals and fixed-point numbers
- `two-s-complement-and-signed-integers`: Two's complement and signed integers
- `basic-ring-and-group-structure`: Basic ring and group structure
- `euler-s-formula-and-primitive-roots-of-unity`: Euler's formula and primitive roots of unity
- `fast-fourier-transform-for-power-of-two-length`: Fast Fourier transform for power-of-two length
- `gaussian-function`: Gaussian function
- `time-and-space-as-functions-of-input-size`: Time and space as functions of input size
- `tape-head-movement-and-sequential-access`: Tape head movement and sequential access

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
