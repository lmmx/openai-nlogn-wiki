# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/A6` (paths below are relative to it)

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

`main-result`: Integer multiplication in O(n (lg n)^{1-κ}) time: Deterministic multitape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}) time, κ=2^{-182}, by chaining digit convolution, prime axes, Gaussian resampling, chirps, a polynomial-ring twist, synthetic transforms accelerated by fast address interchanges and butterfly layers, then exact recovery.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: An undergraduate computer science reader who has studied discrete mathematics, algorithms (divide and conquer, fast multiplication such as Karatsuba, the FFT at a basic level), linear algebra, and elementary number theory and probability. They know asymptotic notation, binary and positional number representation, polynomials and complex numbers, and basic Turing machines. They have not studied multitape complexity details, advanced harmonic analysis, algebraic number theory, or the research literature on integer multiplication.

## Pages, in reading order

- `multitape-model`: Fixed multitape Turing machine model: Deterministic Turing machine with fixed finite alphabet and fixed finite number of one-dimensional tapes; the cost model where time counts bit-level tape steps and scans of n stored bits cost Θ(n).
- `nlogn-conjecture-history`: Multiplication history and the n log n conjecture: Schönhage–Strassen gave O(n log n log log n) and conjectured n log n optimal; Fürer and others improved the factor; Harvey–van der Hoeven reached O(n log n).
- `convolution-reduction`: Multiplication as convolution of radix digits: Splitting both integers into short radix digits turns the integer product into a convolution of digit lists, followed by carry propagation.
- `poly-ring-mod`: Polynomial ring modulo y^r + 1: Complex polynomials in y reduced by y^r=-1, with r a power of two; multiplying by a power of y is a signed cyclic shift of the coefficient list.
- `fourier-transform-butterflies`: Fourier transforms and butterfly operations: A discrete Fourier transform evaluates a sequence at roots of unity, turning cyclic convolution into pointwise products; fast versions use layers of two-point butterflies.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms using powers of y as roots of unity so twiddle multiplications are signed shifts, computed by address rearrangements, shifts and butterflies.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Placing the digit list on a product of distinct prime cyclic axes by a Chinese-remainder address map that preserves convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven reduction expressing a Fourier transform of arbitrary axis length through a transform with power-of-two axes, with source and target permutations kept in the identity.
- `bluestein-chirp`: Bluestein chirp conversion: Bluestein's identity rewrites a transform (with its target permutation) as a normalized cyclic convolution via chirp factors.
- `phase-twist`: Phase twist to the polynomial ring: A twist on the last cyclic coordinate makes its wraparound negative, turning it into a polynomial modulo y^r+1 whose negative wrap restores the cyclic wrap after untwisting.
- `signed-packing`: Signed packing of polynomial products: Kronecker-style packing of signed coefficients into integers so ring products are computed with the established O(n log n) multiplier as an ordinary subroutine.
- `tape-streams`: Array order, streams and controlled shifts: Elementary tape operations: scanning arrays in address order, stream operations and controlled shifts/rational scalings that cost linear time.
- `linear-network-frames`: Linear networks with roles and frames: A fixed linear network exchanging two banks of values with signs and restoring auxiliaries; wires are roles, rows are distributed among W roles, and invertible frames D_v change array representation so intermediate frames cancel.
- `subset-intersection-network`: Finite networks from three-element subsets: Construction attaching nested subspaces of an m-dimensional space to gates, using three-element subset intersection counts, gather/scatter and auxiliary wires, so total smaller calls s < W m.
- `recursive-power-saving`: Recursive power saving: A call at parameter mf uses s calls at parameter f on volume V/W streams; since s/W<m, cost per volume grows like a power less than 1 of the parameter instead of linearly.
- `address-interchange`: Fast interchange of address chunks: Interchanges two disjoint contiguous address fields of u bits in a Cartesian-product array in O(V u^τ) with τ<1, via XOR combinations and address shears, yielding an exact permutation.
- `simultaneous-butterfly`: Fast simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u-v)/2) on the same bit of at most d address chunks of polynomial records of complex fixed-point numbers in O(V d^λ'), λ'<1, using exact Gaussian dyadics and one final truncation.
- `precision-exact-recovery`: Precision, error bound and exact recovery: Fixed-point precision analysis showing the recovered coefficient error is below 1/2 so rounding, rescaling and carry propagation give the exact integer product.
- `main-result`: Integer multiplication in O(n (lg n)^{1-κ}) time: Deterministic multitape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}) time, κ=2^{-182}, by chaining digit convolution, prime axes, Gaussian resampling, chirps, a polynomial-ring twist, synthetic transforms accelerated by fast address interchanges and butterfly layers, then exact recovery.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-tapes`: Basic Turing machines and tapes
- `binary-representation-and-radix-digits`: Binary representation and radix digits
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `logarithms-and-powers-of-two`: Logarithms and powers of two
- `schoolbook-multiplication-and-convolution-of-sequences`: Schoolbook multiplication and convolution of sequences
- `karatsuba-and-divide-and-conquer-multiplication`: Karatsuba and divide-and-conquer multiplication
- `fast-fourier-transform-basics`: Fast Fourier transform basics
- `linear-algebra-over-the-reals-and-complex-numbers`: Linear algebra over the reals and complex numbers
- `direct-product-of-sets-and-multidimensional-arrays`: Direct product of sets and multidimensional arrays
- `permutations-and-bijections`: Permutations and bijections
- `cyclic-groups-and-z-mz`: Cyclic groups and Z/mZ
- `fixed-point-and-rounding-arithmetic`: Fixed-point and rounding arithmetic
- `error-bounds-and-the-triangle-inequality`: Error bounds and the triangle inequality
- `binary-xor-and-bitwise-operations`: Binary XOR and bitwise operations
- `basic-counting-and-combinatorics`: Basic counting and combinatorics
- `induction-and-recurrences`: Induction and recurrences
- `real-analysis-basics-inequalities-and-exponentials`: Real analysis basics: inequalities and exponentials
- `ring-and-group-axioms`: Ring and group axioms

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
