# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/A5` (paths below are relative to it)

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

`target`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic fixed-tape machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time, κ=2^−182, disproving the n log n conjecture in this model; chain: digit convolution, prime axes, resampling and chirps, polynomial ring transforms with fast tape procedures, then rounding and carries.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: An undergraduate computer science reader who has studied algorithms and data structures (divide and conquer, recurrences, sorting, basic complexity), discrete mathematics (modular arithmetic, primes, binary representation, sets, permutations, induction), and linear algebra (vector spaces, subspaces, dimension, rank, invertible matrices, Gaussian elimination, triangular matrices) at an introductory level. They know the basics of Fourier analysis and probability/real analysis only as far as complex numbers and elementary calculus. They have not studied algebraic number theory, advanced finite-field theory, Lie groups or specialist FFT/multiplication literature.

## Pages, in reading order

- `nlogn-conjecture`: Multiplication history and the n log n conjecture: Schönhage–Strassen multiplied n-bit integers in O(n log n log log n) and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).
- `convolution`: Convolution and multiplication: Multiplying integers by splitting into radix digits reduces to convolving short integer coefficient lists, i.e. multiplying polynomials.
- `dft`: Discrete Fourier transform: Evaluating a coefficient list at powers of a primitive root of unity; it turns cyclic convolution into pointwise products.
- `poly-ring-mod`: Polynomial ring modulo y^r + 1: Polynomials in y with complex coefficients reduced using y^r = -1; powers of y are roots of unity and multiplying by one is a signed cyclic shift of the coefficient list.
- `butterfly-fft`: FFT and two-point butterflies: Fast Fourier transform levels built from address rearrangements, root multiplications and two-point butterfly operations; each of Θ(log n) levels scanning Θ(n) bits costs Θ(n log n).
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms over the polynomial ring where roots of unity are powers of y, so root multiplication is a signed shift.
- `fixed-point-precision`: Fixed-point precision and exact recovery: Records hold complex fixed-point coefficients; Gaussian dyadics are exact, one truncation follows a contractive layer, and the final error is below 1/2 so rounding and carries give the exact product.
- `multidim-crt`: Prime cyclic axes and the Chinese remainder map: The coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map preserving convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven technique expressing a Fourier transform through a multidimensional transform whose axis lengths are powers of two.
- `bluestein-chirp`: Bluestein chirp identity: Converts a transform of arbitrary length into a cyclic convolution via multiplication by chirp phases.
- `phase-twist`: Last-coordinate phase twist: A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap yields the original cyclic wrap after untwisting.
- `signed-packing`: Signed packing (Kronecker substitution): Exact polynomial products are computed by packing signed coefficients into one long integer and calling the established O(n log n) multiplier as an ordinary subroutine.
- `tape-streams`: Tape arrays, scans and elementary streams: Arrays stored in address order on tapes with scans, controlled shifts and fixed rational scalings costing linear time.
- `linear-network-frames`: Linear networks, roles and frames: A fixed linear network exchanges banks of values with signs and restores auxiliary values; rows are spread over roles and each vertex stores D_v g in an invertible linear frame so intermediate frames cancel.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H0(u,v)=((u+v)/2,(u−v)/2) coefficientwise on the same selected bit of up to d address chunks, in O(V d^λ') time with λ'<1.
- `matrix-shear`: Address shear and triangular factorization: The endpoint operator (H,D)->(H+D,D) on address fields, with rank reduction via lower-triangular (Bruhat) factorization.
- `address-interchange`: Fast interchange of address fields: Swapping two disjoint contiguous address fields of u bits in a Cartesian-product array in O(V u^τ) time, τ<1, using intermediate XOR combinations that end in an exact permutation.
- `finite-subset-networks`: Finite networks from three-element subsets: Fixed networks with nested subspaces of an m-dimensional space built from three-element subset intersections, giving s<Wm smaller calls.
- `recursive-saving`: Recursive power saving: Calling a parameter-mf operation as s calls at parameter f on volume V/W raises normalized cost by s/W<m per multiplication of the parameter by m, yielding a power saving.
- `retained-permutations`: Resampling with permutations retained in the transform: Source and target coordinate permutations stay in the transform identity and cancel across forward, pointwise, and inverse transforms instead of being executed as sorts.
- `target`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic fixed-tape machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time, κ=2^−182, disproving the n log n conjecture in this model; chain: digit convolution, prime axes, resampling and chirps, polynomial ring transforms with fast tape procedures, then rounding and carries.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-tm`: Multitape Turing machine
- `recurrences-and-divide-and-conquer`: Recurrences and divide and conquer
- `modular-arithmetic`: Modular arithmetic
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `chinese-remainder-theorem`: Chinese remainder theorem
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `radix-base-expansion`: Radix (base) expansion
- `permutations`: Permutations
- `vector-spaces-subspaces-and-dimension`: Vector spaces, subspaces and dimension
- `finite-field-f-2`: Finite field F_2
- `matrices-rank-and-invertibility`: Matrices, rank and invertibility
- `gaussian-elimination`: Gaussian elimination
- `cartesian-product-of-sets`: Cartesian product of sets
- `cyclic-groups-and-roots-of-unity`: Cyclic groups and roots of unity
- `real-and-complex-analysis-basics`: Real and complex analysis basics
- `rounding-floor-and-ceiling`: Rounding, floor and ceiling
- `logarithms-and-exponents`: Logarithms and exponents
- `schoolbook-multiplication-and-karatsuba`: Schoolbook multiplication and Karatsuba
- `sorting-and-merging`: Sorting and merging
- `pigeonhole-principle-and-counting-arguments`: Pigeonhole principle and counting arguments
- `lower-and-upper-bound-asymptotics`: Lower and upper bound asymptotics
- `constants-and-parameters-in-complexity-bounds`: Constants and parameters in complexity bounds

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
