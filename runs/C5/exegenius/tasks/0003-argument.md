# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/C5` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1−κ}) time with κ=2^{-182}, disproving the n log n conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate computer scientist: asymptotic analysis, algorithm design basics (divide and conquer, recurrences, schoolbook and Karatsuba multiplication), discrete mathematics (modular arithmetic, primes, induction, permutations), and linear algebra and calculus at the usual first-course level. They know polynomials, complex numbers with roots of unity, and simple Turing machines with tapes. They have not studied the FFT in depth, Fourier analysis on groups, tensor products, numerical analysis, or fast integer multiplication research.

## Pages, in reading order

- `ring-y-r-plus-1`: Polynomial ring modulo y^r + 1: The ring of polynomials with complex coefficients in y modulo y^r+1, r a power of two; powers of y act as roots of unity and multiplying by one is a signed shift of the coefficient list.
- `dft-roots-of-unity`: Discrete Fourier transform and roots of unity: Evaluating a polynomial at all powers of a root of unity; the fast version is the FFT, built from layers of two-point butterflies.
- `cyclic-convolution`: Convolution and the convolution theorem: Multiplying polynomials (mod x^N−1 for cyclic) by transforming, multiplying pointwise, and inverse transforming; integer multiplication reduces to it by splitting into radix digits.
- `multidimensional-transform`: Multidimensional transforms: A transform on an array with several axes, applied axis by axis; axis lengths such as primes or powers of two determine cost and layout.
- `butterfly-layer`: Two-point butterfly H₀: The operation (u,v)↦((u+v)/2,(u−v)/2) applied coefficientwise.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms whose roots of unity are powers of y in the ring, so multiplications by roots are signed shifts, leaving only shifts, address rearrangements and butterflies.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: A Chinese-remainder address map placing a coefficient list onto a product of distinct prime cyclic axes while preserving convolution.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a transform as a cyclic convolution by multiplying by chirp phases.
- `phase-twist`: Phase twist to the negative-wrap ring: A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap gives the original cyclic wrap after untwisting.
- `fixed-point-precision`: Fixed-point complex coefficients and exact recovery: Numerical arrays hold complex fixed-point dyadic numbers; errors are bounded below 1/2 so rounding recovers exact integer coefficients.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven identity expressing each Fourier transform on prime-length axes through a power-of-two tensor transform, with contraction bounds on the error.
- `multitape-model`: Fixed multitape Turing machine model: One fixed finite alphabet and a fixed finite number of one-dimensional tapes; each step reads/writes one cell per tape and moves each head at most one cell, so moving data costs time.
- `nlogn-conjecture`: The n log n conjecture and history: Schönhage and Strassen proposed n log n as optimal multiplication cost; Schönhage–Strassen, Fürer and Harvey–van der Hoeven reduced upper bounds down to O(n log n).
- `hh-multiplier`: Established O(n log n) multiplier: The Harvey–van der Hoeven O(n log n) multiplication algorithm, used here only as an ordinary subroutine for small products.
- `signed-packing`: Signed packing (Kronecker substitution): Packing polynomial coefficients into a single integer with signs so ring products reduce to integer products done by the established multiplier.
- `address-fields-layout`: Array addresses, fields and tape layout: Arrays are stored on tape in row-major address order; address bit-fields (chunks) are contiguous and permuting them costs more than scanning.
- `linear-network`: Linear networks with restored auxiliary values: A fixed network of gates exchanging two banks of values with signs, with roles for each wire, whose auxiliary values are restored so the effect is exact for arbitrary initial auxiliary contents.
- `frames`: Frames of a linear network: Invertible linear operators attached to sources, gates and sinks changing how a logical array is stored; intermediate frames cancel leaving an endpoint operator.
- `address-shear`: Address shear and triangular factorization: The endpoint operator (H,D)↦(H+D,D) on address fields; a rank-reducing lower-triangular factorization lets two further linear updates complete an interchange.
- `subset-subspace-labels`: Subset-intersection subspace labels: Subspaces of a fixed m-dimensional space attached to gates using three-element subsets, nested along edges so dimension drops count smaller calls and the total s<Wm.
- `recursive-saving`: Recursive power saving from s<Wm: A call at parameter mf makes s<Wm calls at parameter f on volume V/W streams, so per-volume cost grows by a factor below m, giving a power saving.
- `fast-address-interchange`: Fast interchange of address fields: Swaps two disjoint contiguous u-bit address fields of an array of stored volume V in cost O(V u^τ), τ<1, using XOR combinations whose final effect is an exact permutation.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Applies H₀ simultaneously on the same selected bit of at most d address chunks in cost O(V d^λ′), via the linear network with phase frames and a single final truncation.
- `retained-permutations`: Resampling with permutations left in the transform: The source and target coordinate permutations stay inside the transform identity and cancel across forward, product and inverse transforms instead of being sorted separately.
- `fast-synthetic-transform`: Synthetic transforms with retained frequency order: Forward synthetic transforms keep the same frequency order through their pointwise product and the opposite transform consumes it, using fast butterfly layers and interchanges.
- `multiplication-assembly`: Assembling the exact product: Chain: radix digits, CRT prime axes, Gaussian resampling and chirps, phase twist, ring convolution; then rescale, round and propagate carries; cost table summed.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1−κ}) time with κ=2^{-182}, disproving the n log n conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine-basics`: Turing machines and tapes
- `logarithms-and-iterated-logarithm-notation`: Logarithms and iterated logarithm notation
- `floor-ceiling-and-rounding`: Floor, ceiling and rounding
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `radix-base-b-expansion`: Radix (base-b) expansion
- `schoolbook-multiplication-and-carries`: Schoolbook multiplication and carries
- `divide-and-conquer-recurrences`: Divide and conquer recurrences
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `permutations-and-bijections`: Permutations and bijections
- `vectors-matrices-and-linear-maps`: Vectors, matrices and linear maps
- `subspaces-dimension-and-rank`: Subspaces, dimension and rank
- `vector-spaces-over-gf-2`: Vector spaces over GF(2)
- `triangular-matrices-and-elimination`: Triangular matrices and elimination
- `norms-and-triangle-inequality`: Norms and triangle inequality
- `exponential-function-and-euler-s-formula`: Exponential function and Euler's formula
- `fixed-point-and-finite-precision-numbers`: Fixed-point and finite-precision numbers
- `direct-sum-and-product-of-index-sets`: Direct sum and product of index sets
- `deterministic-algorithms-and-upper-lower-bounds`: Deterministic algorithms and upper/lower bounds
- `induction-and-proofs-by-recursion`: Induction and proofs by recursion
- `constants-exponents-and-power-of-two-sizes`: Constants, exponents and power-of-two sizes

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

Keep any other files you make, such as scripts, in `exegenius/tasks/0003-argument`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
