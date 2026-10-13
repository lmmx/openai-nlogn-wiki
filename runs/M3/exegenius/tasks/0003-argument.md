# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/M3` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) time: Deterministic fixed-tape machine multiplying n-bit integers in O(n(lg n)^(1-κ)) with κ=2^-182, disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis and recurrences, algorithm design (divide and conquer, the classical FFT idea), basic Turing machine complexity, discrete mathematics (binary and positional number systems, modular arithmetic, prime numbers, subsets), and the linear algebra and calculus that such a degree includes (vector spaces, subspaces, rank, matrices, inverse, real exponentials and logarithms). The reader has not studied algebraic structures beyond the basics, number theory beyond elementary modular arithmetic, numerical error analysis, or the research literature on fast integer multiplication.

## Pages, in reading order

- `convolution`: Convolution and cyclic convolution: Combining two coefficient lists so that entry k sums products of entries whose indices add to k (cyclically or with wrap); integer multiplication reduces to it.
- `radix-reduction`: Reduction of integer product to digit convolution: Split the inputs into radix digits so the product is a convolution of short integer coefficients, followed by carry propagation.
- `poly-ring-yr1`: Polynomial ring modulo y^r + 1: Polynomials in y with complex coefficients reduced using y^r = -1, so multiplying by a power of y is a signed shift of the coefficient list.
- `complex-fixed-point`: Gaussian dyadics and fixed-point precision: Complex fixed-point numbers with power-of-two denominators; intermediate values exact, with one truncation after a contractive layer.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Placing the digit list on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.
- `phase-twist`: Last-coordinate phase twist: A phase twist turning the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap equals the original cyclic wrap after untwisting.
- `dft-roots-of-unity`: Fourier transform and roots of unity: Evaluating a coefficient list at roots of unity turns convolution into pointwise products; the fast version uses butterfly layers.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms over the ring modulo y^r+1 where roots of unity are powers of y, so root multiplication is a signed shift; computed by address rearrangements, shifts and butterflies.
- `butterfly`: Two-point butterfly H₀: The map (u,v) -> ((u+v)/2,(u-v)/2) applied coefficientwise, the basic step of a transform layer.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven technique expressing each prime-length Fourier transform through a power-of-two multidimensional tensor transform, keeping source and target permutations in the identity.
- `bluestein-chirp`: Bluestein chirp identity: Converts the middle transform, with its target permutation, into a normalized cyclic convolution.
- `multitape-model`: Fixed multitape Turing machine model: Deterministic machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes; the cost is the number of steps.
- `nlogn-conjecture`: The n log n conjecture and history of multiplication: Schönhage and Strassen's 1971 O(n log n log log n) bound and conjecture that n log n is optimal; Harvey and van der Hoeven reached O(n log n).
- `stream-operations`: Elementary stream operations and controlled shifts: Scans, array order, and shifts on tapes in linear time, forming the cost base for rearrangements.
- `linear-network`: Linear networks with roles and restored auxiliaries: A fixed linear network exchanging two banks of values with signs and restoring every auxiliary value; rows of an array are distributed cyclically among W roles and gates apply pointwise.
- `frames`: Frames and endpoint operators: Invertible linear operators D_v attached to gates; intermediate frames cancel so a route applies D_sink D_source^-1, leaving an endpoint operator such as an address shear or the H₀ layer.
- `finite-network-subspaces`: Finite networks with nested subspaces and rank saving: Network whose gates carry nested subspaces of an m-dimensional space built from three-element subset intersections, with total smaller calls s < W m.
- `recursive-saving`: Recursive power saving: A call at parameter m f uses s calls at f on volume V/W, raising the cost factor by s/W < m, giving a power of the logarithm.
- `signed-packing`: Signed packing (Kronecker substitution): Packing polynomial coefficients into one integer so a polynomial product is computed with the ordinary O(n log n) multiplier as a subroutine.
- `lower-triangular-factorization`: Lower triangular (Bruhat) factorization: Every rational matrix of rank a factors as E1 Π E2 with E1, E2 lower triangular and Π a partial permutation with a ones, so a shear of rank a needs only a smaller interchanges, in tape order.
- `address-interchange`: Fast interchange of address chunks: Procedure swapping two disjoint contiguous address fields of u bits in a Cartesian-product array via XOR combinations and address shears, in cost O(V u^τ), τ<1.
- `fast-butterfly-layer`: Simultaneous fast butterfly layers: Applying H₀ at the same bit position in each of d address chunks simultaneously on fixed-point complex polynomial records in cost O(V d^λ'), λ'<1.
- `transform-layout`: Synthetic transforms on the retained layout: Layout on which parallel butterfly layers and address interchanges apply, giving transform cost and retaining frequency order through the pointwise product.
- `normalized-convolution`: Normalized convolution over the polynomial ring: Convolution on the remaining axes over the ring, via two forward transforms, pointwise polynomial products and the opposite transform.
- `exact-recovery`: Precision, rounding and carry propagation: Remove known normalizations and digit scales, show coefficient error is below 1/2, round and propagate carries to the exact binary product.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) time: Deterministic fixed-tape machine multiplying n-bit integers in O(n(lg n)^(1-κ)) with κ=2^-182, disproving the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine`: Turing machines and tapes
- `binary-representation-of-integers`: Binary representation of integers
- `positional-radix-and-digit-expansion`: Positional radix and digit expansion
- `logarithms-and-floor-ceiling`: Logarithms and floor/ceiling
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `matrices-and-linear-maps`: Matrices and linear maps
- `vector-spaces-subspaces-dimension-and-rank`: Vector spaces, subspaces, dimension and rank
- `permutations-and-permutation-matrices`: Permutations and permutation matrices
- `cartesian-products-and-multidimensional-arrays`: Cartesian products and multidimensional arrays
- `divide-and-conquer-recurrences`: Divide and conquer recurrences
- `fast-fourier-transform-idea`: Fast Fourier transform idea
- `absolute-value-norms-and-error-bounds`: Absolute value, norms and error bounds
- `dyadic-rationals-and-fixed-point-numbers`: Dyadic rationals and fixed-point numbers
- `xor-and-bitwise-operations`: XOR and bitwise operations
- `finite-sets-and-subset-operations`: Finite sets and subset operations
- `euler-s-formula-and-unit-circle`: Euler's formula and unit circle
- `worst-case-running-time-and-turing-machine-step-counting`: Worst-case running time and Turing machine step counting
- `gaussian-elimination-and-triangular-matrices`: Gaussian elimination and triangular matrices

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

Keep any other files you make, such as scripts, in `exegenius/tasks/0003-argument`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
