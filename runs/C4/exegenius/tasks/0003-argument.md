# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/C4` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape machine multiplying n-bit integers exactly in O(n(lg n)^{1−κ}) with κ=2^{-182}, refuting the n log n optimality conjecture; built from radix convolution, CRT axes, Gaussian resampling, chirps, the polynomial ring and fast chunk and butterfly operations.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science core: asymptotic analysis and recurrences, algorithms and data structures (divide and conquer, FFT-style ideas at the level of an algorithms course), discrete mathematics (modular arithmetic, binary representation, induction, basic combinatorics), and linear algebra (vectors, matrices, bases, invertible maps, subspaces over the reals and complex numbers). They know basic Turing machines with tapes, but not multitape time-complexity subtleties, the Schönhage–Strassen or Harvey–van der Hoeven methods, number-theoretic transforms in depth, or any research-level algebra or numerical analysis.

## Pages, in reading order

- `multitape-model`: Fixed multitape machine model and scans: A Turing machine with one fixed finite alphabet and a fixed number of one-dimensional tapes; moving data is paid for by scanning tapes, so a pass over n bits costs Θ(n).
- `conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen's 1971 O(n log n log log n) multiplication and their conjecture that n log n is optimal, with Harvey–van der Hoeven's O(n log n) the previous best.
- `linear-network-frames`: Linear exchange networks with frames and roles: A fixed linear network of gates on wires (roles) exchanging two banks of values and restoring auxiliary values; with invertible frames D_v per vertex, gates act pointwise and intermediate frames cancel, leaving an endpoint operator on each role array.
- `lower-triangular-shear`: Address shear and lower triangular factorization: Bruhat-style factorization into lower triangular factors with reversed coordinate order; a shear (H,D)→(H+D,D) updates later fields from earlier ones in linear time on tape.
- `subset-intersection-network`: Three-element subset construction with rank saving: Subspaces of an m-dimensional space labelled by three-element subsets, using gather/scatter and auxiliary wires, make adjacent edge operators nested so the total number s of smaller calls is less than W·m.
- `recursive-power-saving`: Recursive power saving from s < Wm: A recursive call at parameter mf uses s calls at parameter f on volume V/W each, so the per-volume cost multiplies by s/W < m, giving cost V·(parameter)^θ with θ<1.
- `chunk-interchange`: Interchange of address chunks in time O(Vu^τ): Interchanging two disjoint contiguous u-bit address fields of an array by XOR combinations of intermediate data and the bit network, with exact final permutation for arbitrary auxiliary values.
- `ring-y-r`: Polynomial ring modulo y^r + 1: The ring of polynomials over ℂ modulo y^r+1, where powers of y are roots of unity and multiplication by y^a is a signed cyclic shift of coefficients; norm is the max coefficient modulus.
- `kronecker-packing`: Signed Kronecker packing: Packing polynomial coefficients (including negative ones) into one large integer so that a polynomial product becomes an integer product.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier as subroutine: The established O(N log N) fixed-tape integer multiplier, used as an ordinary subroutine for short polynomial records.
- `dft-convolution`: Discrete Fourier transform and cyclic convolution: The length-q DFT (normalized by 1/q) turns cyclic convolution into pointwise multiplication; inverse transform has opposite sign in the exponent.
- `radix-digit-convolution`: Multiplication as convolution of radix digits: Writing both integers in a radix turns their product into a convolution of short integer coefficient lists, followed by carry propagation.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: A Chinese-remainder address map placing the coefficient list on a product of distinct prime cyclic axes, preserving convolution.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a DFT of arbitrary length as a cyclic convolution sandwiched between pointwise phase (chirp) multiplications.
- `phase-twist`: Phase twist to the polynomial ring: A phase multiplication converting the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap yields the original cyclic wrap after untwisting.
- `fixed-point-precision`: Fixed-point precision and exact recovery: Complex values are stored on a 2^{-p} grid with truncation errors; composing contractive approximations adds errors, and final coefficient error below 1/2 lets rounding and carries recover the exact integer product.
- `gaussian-dyadics`: Exact Gaussian dyadic arithmetic with single truncation: Intermediate values are kept exactly as complex numbers with power-of-two denominators, with one truncation after a completed contractive layer.
- `synthetic-transform`: Synthetic polynomial transforms: Nussbaumer–Quandalle transforms over the ring with roots of unity ω_t = y^{2r/t} acting as signed shifts, computed by radix-two butterflies; frequency order is retained through the pointwise product.
- `butterfly-h0`: Simultaneous butterfly layer H₀: The two-point butterfly H₀(u,v)=((u+v)/2,(u−v)/2) applied coefficientwise to selected coordinate bits of many address chunks at once.
- `phase-frames`: Phase frames for simultaneous butterflies: Diagonal phase frames express a tensor product of the auxiliary kernel C on many selected bits via smaller groups of bits separated by binary changes of basis implemented as whole-chunk moves.
- `fast-butterfly-layer`: Fast simultaneous butterfly layer in time O(Vd^λ′): Applying H₀ to the same bit in d address chunks of the polynomial array in cost O(V d^λ′) instead of d full passes.
- `transform-layout`: Synthetic transform layout and convolution: Layout on tape on which the parallel layers apply and the pointwise-multiplied transforms are inverted, with polynomial products by signed packing and the Harvey–van der Hoeven multiplier.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's method expressing a Fourier transform of coprime length through a power-of-two tensor transform, via Gaussian-weighted interpolation.
- `retained-permutations`: Retained permutations cancelling in transforms: Keeping the source and target coordinate permutations of resampling inside the transform formula so that they cancel across the forward transforms, product and inverse instead of being sorted.
- `tensor-resampling`: Tensor resampling over growing dimension: Applying one-dimensional resampling maps line by line over many coordinates, with axis movement done by chunk interchange.
- `parameter-choice`: Compatible parameter choice and cost accounting: A fixed rational choice (τ, λ′, ε, κ=2^{-182}, ...) making all cost terms fit the final bound.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape machine multiplying n-bit integers exactly in O(n(lg n)^{1−κ}) with κ=2^{-182}, refuting the n log n optimality conjecture; built from radix convolution, CRT axes, Gaussian resampling, chirps, the polynomial ring and fast chunk and butterfly operations.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-tapes`: Basic Turing machines and tapes
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `modular-arithmetic`: Modular arithmetic
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality
- `matrices-and-linear-maps`: Matrices and linear maps
- `vector-spaces-over-finite-fields`: Vector spaces over finite fields
- `norms-and-triangle-inequality`: Norms and triangle inequality
- `floor-ceiling-rounding-and-logarithms`: Floor, ceiling, rounding and logarithms
- `recurrences-and-divide-and-conquer`: Recurrences and divide and conquer
- `schoolbook-multiplication-and-carries`: Schoolbook multiplication and carries
- `fast-fourier-transform`: Fast Fourier transform
- `euler-s-formula-and-exponentials-of-complex-numbers`: Euler's formula and exponentials of complex numbers
- `gaussian-function-and-gaussian-sums`: Gaussian function and Gaussian sums
- `geometric-series-and-exponential-decay-bounds`: Geometric series and exponential decay bounds
- `tuples-products-of-sets-and-mixed-radix-indexing`: Tuples, products of sets and mixed-radix indexing
- `permutations`: Permutations
- `cyclic-groups-and-direct-products`: Cyclic groups and direct products
- `real-and-complex-number-approximation`: Real and complex number approximation
- `big-o-variants-and-constants`: Big-O variants and constants
- `induction-and-proof-by-recursion`: Induction and proof by recursion
- `diagonal-matrices`: Diagonal matrices

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
