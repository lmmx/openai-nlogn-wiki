# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/D3` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape multiplication of n-bit integers in O(n(lg n)^{1−κ}), κ=2^{-182}, disproving the n log n conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate in computer science who has taken discrete mathematics, algorithms and a theory-of-computation course, with linear algebra and basic probability or number theory. They know asymptotic analysis, divide-and-conquer recurrences, binary and positional number representations, modular arithmetic, and sets and functions, and have met the idea of a fast Fourier transform and the n log n multiplication story at most informally. They have not studied finite fields, abstract algebra beyond basics, numerical error analysis, or the specialist literature on multiplication algorithms.

## Pages, in reading order

- `convolution`: Convolution and radix-digit reduction: Multiplying integers reduces, by splitting them into radix digits, to convolving short integer coefficient lists.
- `polynomial-ring-y-r-1`: Polynomial ring modulo y^r + 1: Complex polynomials in y with y^r = −1, r a power of two; powers of y act as roots of unity and multiplying by one is a signed shift of coefficients.
- `fourier-transform`: Discrete Fourier transform: Evaluating a coefficient list at roots of unity, turning convolution into pointwise product; computed in levels of two-point butterflies.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier transforms over the ring where roots of unity are powers of y, so multiplications by roots are signed shifts (Nussbaumer).
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven reduction replacing needed Fourier transforms by multidimensional transforms with power-of-two axis lengths.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Places the radix-digit coefficient list on a product of distinct prime cyclic axes by a convolution-preserving CRT address map.
- `bluestein-chirp`: Bluestein chirp identity: Converts a Fourier transform into a cyclic convolution via chirp factors.
- `phase-twist`: Coefficient twist to the polynomial ring: A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1 whose negative wrap yields the cyclic wrap after untwisting.
- `multitape-model`: Fixed multitape Turing machine model: The cost model: one fixed finite alphabet and a fixed finite number of one-dimensional tapes, each step reading/writing one cell per tape and moving heads by at most one cell.
- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen's O(n log n log log n) bound and conjecture that n log n is optimal, later met by Harvey–van der Hoeven's O(n log n).
- `tape-address-rearrangement`: Address rearrangement cost on tapes: Moving data between address fields on tapes costs a scan per level; naive scanning gives Θ(n log n) over Θ(log n) levels.
- `linear-network-frames`: Linear networks, roles and frames: A fixed linear network exchanging two banks of values with signs, restoring auxiliary values; frames are invertible operators changing array representation along edges and cancelling at the ends.
- `finite-network-subspaces`: Finite network via three-element subsets and nested subspaces: Subspaces of an m-dimensional space attached to gates, using three-element subsets, give a network with fewer than Wm smaller calls.
- `recursive-power-saving`: Recursive saving from s < Wm: Calls at parameter mf use s calls at parameter f on volume V/W; s/W<m strictly gives a power-saving cost.
- `signed-packing`: Signed packing (Kronecker substitution): Packs polynomial coefficients into one long integer so a polynomial product becomes an integer product by the established O(n log n) multiplier.
- `elementary-streams`: Elementary stream operations and controlled shifts: Linear-time scans on tapes: digit permutations, moves, and controlled shifts/fixed rational scalings of a field using earlier control fields; arrays stored in lexicographic order with a self-delimiting integer header code.
- `scalar-motifs`: Scalar gates with restored scratch wires: In the network, a forward invocation adds x_S to y_S for arbitrary scratch contents; three stages exchange the banks (X,Y) to (−Y,X) and restore all auxiliary values.
- `motif-residuals`: Rank budget of the network labels: Edges join comparable subspace labels; total dimension change over edges equals Wm−2N+2L, giving the strict rank deficit s<Wm.
- `motif-interfaces`: Bit and complex network interfaces: The bit network (XOR gates, rational matrices) realises an address permutation with rank sum small; the complex network realises phase frames made of translation kernels and yields the H0 layer.
- `matrix-shear`: Lower triangular factorization and matrix shear: Any rational matrix of rank a factors as E1·Π·E2 with lower triangular E1,E2, so the shear (H,D)↦(H+AD,D) needs exactly a field interchanges plus linear work.
- `chunk-swap`: Power-width and arbitrary-width chunk interchange: Recurrence on parameter e=m^k gives chunk interchange in O(V e^τ); then arbitrary width u by decomposition.
- `address-interchange`: Fast address-field interchange: Interchanges two address fields of u bits at cost O(V u^τ), τ<1, through XOR combinations of data, with the final result an exact permutation.
- `packed-selected-bit-addition`: Packed selected-bit addition on grouped rectangles: XORs selected bits at positions ρ+iK of several chunks simultaneously by packing, repairing a small exceptional set of addresses.
- `fast-butterfly-layer`: Simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u−v)/2) simultaneously on selected coordinate bits of complex fixed-point arrays at cost O(V d^λ′), λ′<1.
- `precision-exact-recovery`: Precision and exact recovery: Fixed-point errors are kept strictly below 1/2 so rounding, rescaling and carry propagation give the exact integer product.
- `transform-layout-cost`: Synthetic transform layout and cost: Layout of the synthetic transform over R_r with truncation Q_p, contractions, and stored frequency order retained through pointwise product; cost via simultaneous layers.
- `tensor-resampling`: Tensor resampling with retained permutations: Gaussian resampling lines combined over d axes, keeping source and target permutations inside the transform identity.
- `parameter-choice`: Fixed rational parameter choice and cost table: Choice τ=σ=1−2^{−50}, c, λ′ etc. and a cost table whose rows each fit O(p^{1−ε′}) after dividing by volume.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape multiplication of n-bit integers in O(n(lg n)^{1−κ}), κ=2^{-182}, disproving the n log n conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-tapes`: Turing machines and tapes
- `linear-algebra-over-the-reals-and-rationals`: Linear algebra over the reals and rationals
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `primes-coprimality-and-gcd`: Primes, coprimality and gcd
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `radix-base-b-positional-representation`: Radix (base-b) positional representation
- `floor-ceiling-and-logarithms`: Floor, ceiling and logarithms
- `schoolbook-multiplication`: Schoolbook multiplication
- `divide-and-conquer-recurrences`: Divide-and-conquer recurrences
- `fixed-point-arithmetic-and-rounding-error`: Fixed-point arithmetic and rounding error
- `complex-exponential-and-unit-roots`: Complex exponential and unit roots
- `cyclic-groups-and-cyclic-indexing`: Cyclic groups and cyclic indexing
- `cartesian-products-and-multidimensional-arrays`: Cartesian products and multidimensional arrays
- `permutations`: Permutations
- `gaussian-elimination-and-triangular-matrices`: Gaussian elimination and triangular matrices
- `gaussian-function`: Gaussian function
- `time-complexity-and-reductions`: Time complexity and reductions
- `basic-induction-and-proof-by-contradiction`: Basic induction and proof by contradiction
- `basic-set-notation-and-counting`: Basic set notation and counting
- `fast-fourier-transform-idea`: Fast Fourier transform idea

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
