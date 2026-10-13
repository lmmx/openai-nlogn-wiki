# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/C2` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) time: Deterministic multitape TM multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, disproving the n log n conjecture in that model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, basic algorithm design (divide and conquer, recurrences), discrete mathematics (sets, subsets, binary representation, modular arithmetic, primes, gcd), and linear algebra (vector spaces, subspaces, matrices, rank, orthogonal projection, invertible matrices). They have met complex numbers, polynomials and basic Turing machines, but not the fast-multiplication literature, Fourier analysis beyond basics, or advanced algebra and coding theory.

## Pages, in reading order

- `multiplication-history`: Integer multiplication complexity and the n log n conjecture: Schönhage–Strassen gave O(n log n log log n) and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).
- `convolution`: Convolution: Combining two coefficient sequences so each output sums products of entries whose indices add; this is polynomial multiplication.
- `poly-ring-negacyclic`: Polynomial ring modulo y^r + 1: Complex polynomials in y of degree below r with y^r = -1; powers of y act as roots of unity and multiplying by them is a signed shift of coefficients.
- `dft-fft`: Discrete Fourier transform and butterflies: Evaluating a sequence at roots of unity, turning convolution into pointwise products, computed by log-depth layers of two-point butterfly operations.
- `digit-convolution-reduction`: Multiplication by radix-digit convolution: Split each integer into radix digits, convolve digit lists, then recover exact integer by rounding, rescaling and carry propagation.
- `multidim-transform`: Multidimensional transform: A Fourier transform on an array with several axes, applied along each axis in turn.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms using powers of y as roots of unity so each twiddle multiplication is a shift.
- `fixed-point-dyadics`: Fixed-point complex dyadics: Complex numbers with power-of-two denominators used exactly in intermediate values and truncated once after a contractive layer.
- `cyclic-crt-axes`: Chinese-remainder map to prime cyclic axes: A Chinese-remainder address map placing the digit list on a product of cyclic axes of distinct prime lengths, preserving convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven identity expressing a Fourier transform of prime-length axes through a power-of-two tensor transform, with source and target permutations.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a Fourier transform of arbitrary length as a convolution multiplied by chirp phases.
- `phase-twist`: Last-coordinate phase twist: Multiplying by diagonal phases so a cyclic coordinate becomes a negative-wrap (mod y^r+1) coordinate; removing the twist restores cyclic wrap.
- `normalized-ring-products`: Packed polynomial products: Pointwise polynomial products in the ring computed via signed packing (Kronecker substitution) and the standard O(n log n) multiplier as a subroutine.
- `precision-exact-recovery`: Precision analysis and exact recovery: Bounds the rounding error of the whole fixed-point pipeline strictly below 1/2, removes normalizations and propagates carries.
- `tape-streams`: Tape scans and address layout: Arrays stored in address order on tapes; scans move data in linear time but rearranging address fields with growing digit counts is costly.
- `address-interchange-bottleneck`: Address rearrangement cost: Scanning Θ(n) bits at each of Θ(log n) levels costs n log n, so both movement and arithmetic must be cheapened.
- `linear-network-roles`: Linear networks, roles and frames: A fixed linear network exchanging two banks of values with signs and restoring auxiliary values; wires have roles and invertible frames D_v change the stored representation, cancelling across the network.
- `finite-subset-network`: Finite network from three-element subsets: Fixed network with nested subspaces attached to gates, built using three-element subsets and gather/scatter with cancelling auxiliary wires, giving s<Wm smaller calls.
- `recursive-saving`: Recursive saving giving a power of log: Calling parameter mf uses s<Wm calls at parameter f on volume V/W each, so cost per volume grows by factor s/W<m per multiplication of the parameter, giving a power saving.
- `controlled-shifts`: Controlled shifts and rational scalings: Linear-time stream operations adding control-field-dependent offsets to a target field.
- `address-shear-factorization`: Rational matrix shear and lower-triangular factorization: Every rational matrix factors as lower-triangular times partial permutation times lower-triangular, so an address shear (H,D)->(H+D,D) costs by rank.
- `fast-address-interchange`: Fast address-field interchange: Interchanges two contiguous address fields via XOR combinations of data and address shears, with an exact final permutation.
- `packed-selected-bit-addition`: Packed selected-bit addition: Adds selected bit positions across grouped rectangles of packed records on tapes, used inside fast butterfly layers.
- `fast-butterfly-layers`: Simultaneous butterfly layers: Applies H_0(u,v)=((u+v)/2,(u-v)/2) to selected coordinate bits of numerical arrays, via the linear network, at cost O(V d^λ').
- `main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) time: Deterministic multitape TM multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, disproving the n log n conjecture in that model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-tm`: Multitape Turing machine
- `recurrence-relations-and-the-master-theorem`: Recurrence relations and the master theorem
- `binary-representation-of-integers`: Binary representation of integers
- `modular-arithmetic`: Modular arithmetic
- `chinese-remainder-theorem`: Chinese remainder theorem
- `prime-numbers-gcd-and-euclidean-algorithm`: Prime numbers, gcd and Euclidean algorithm
- `vector-spaces-subspaces-and-linear-maps`: Vector spaces, subspaces and linear maps
- `matrices-rank-and-invertibility`: Matrices, rank and invertibility
- `gaussian-elimination`: Gaussian elimination
- `sets-subsets-functions-and-permutations`: Sets, subsets, functions and permutations
- `floor-ceiling-logarithms-and-rounding`: Floor, ceiling, logarithms and rounding
- `roots-of-unity`: Roots of unity
- `cyclic-groups-and-products-of-groups`: Cyclic groups and products of groups
- `multidimensional-arrays-and-mixed-radix-indexing`: Multidimensional arrays and mixed-radix indexing
- `basic-probability-and-counting-bounds`: Basic probability and counting bounds
- `norms-error-bounds-and-triangle-inequality`: Norms, error bounds and triangle inequality
- `fixed-point-and-finite-precision-arithmetic`: Fixed-point and finite precision arithmetic
- `integer-addition-multiplication-and-carry-propagation`: Integer addition, multiplication and carry propagation
- `sorting-and-linear-tape-scans`: Sorting and linear tape scans
- `constants-asymptotic-functions-and-polylog-factors`: Constants, asymptotic functions and polylog factors
- `xor-and-bitwise-operations`: XOR and bitwise operations

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
