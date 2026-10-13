# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/M4` (paths below are relative to it)

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

`main-multiplication`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time, κ=2^−182, via radix digits, Chinese-remainder axes, Gaussian resampling, chirps, the twist to the polynomial ring, synthetic transforms accelerated by fast address interchange and butterfly layers, then exact recovery.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: An undergraduate computer science reader who knows asymptotic notation, algorithm analysis and recursion, discrete mathematics (modular arithmetic, primes, the Chinese remainder theorem, sets, permutations, binary representation), and first-year linear algebra (matrices, rank, invertibility, subspaces). They know polynomials and complex numbers including roots of unity, and basic multitape Turing machines. They have not met the fast Fourier transform in depth, convolution theory, Gaussian analysis, fixed-point error control, or the research literature on fast multiplication.

## Pages, in reading order

- `nlogn-conjecture`: The n log n optimality conjecture and prior bounds: Schönhage and Strassen proposed n log n as the optimal multiplication time; Harvey and van der Hoeven reached O(n log n) in the multitape model.
- `convolution`: Convolution: Combining two coefficient lists so that entry k sums products of entries whose indices add to k (cyclically for cyclic convolution); equivalent to polynomial multiplication.
- `fourier-transform`: Discrete Fourier transform: Evaluation of a coefficient list at roots of unity, which turns convolution into pointwise multiplication.
- `radix-digit-reduction`: Reduction of integer multiplication to convolution: Split each integer into short radix digits so the product becomes a convolution of digit lists, followed by carry propagation.
- `polynomial-ring-y-r`: Polynomial ring modulo y^r + 1: Polynomials in y with complex coefficients where y^r is identified with −1, so powers of y act as roots of unity and multiplying by one is a signed cyclic shift.
- `butterfly-h0`: Butterfly map H_0: The two-point map (u,v) ↦ ((u+v)/2, (u−v)/2), the basic arithmetic step of a transform layer.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring using powers of y as roots of unity, built from signed shifts and two-point butterflies.
- `linear-network-frames`: Linear networks with roles and frames: A fixed linear network exchanging two banks of values and restoring auxiliary values, applied pointwise on role arrays under invertible frame operators that cancel along routes to leave an endpoint operator.
- `subset-network`: Finite network from three-element subsets: A network labelled by nested subspaces built from three-element subset intersections, whose number s of smaller calls is less than W·m.
- `recursive-power-saving`: Recursive power saving: A recursive call at parameter m·f using s<W·m calls at parameter f on volume V/W makes the cost per volume grow as a power less than linear in the parameter.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Index re-mapping that turns a long cyclic convolution into a multidimensional one over axes of distinct prime lengths.
- `gaussian-resampling`: Gaussian resampling: Expresses a Fourier transform of prime length through a multidimensional transform with power-of-two axis lengths.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a Fourier transform as a convolution with a chirp (quadratic-phase) sequence.
- `phase-twist`: Phase twist to the negacyclic ring: A diagonal phase multiplication turning the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap yields the original cyclic wrap once the twist is removed.
- `exact-recovery`: Precision and exact recovery of the product: Fixed-point arithmetic with controlled error: removing known normalizations leaves coefficient error below 1/2, so rounding and carry propagation give the exact binary product.
- `signed-packing`: Signed packing of polynomial products: Packing coefficients into long integers with signs so a polynomial product is computed by an ordinary O(n log n) integer multiplier.
- `elementary-streams`: Elementary stream operations and controlled shifts: Linear-time tape scans that permute, move, split and merge digit streams, and add controlled offsets modulo a prime power.
- `matrix-shear`: Rational matrix shear and triangular factorization: The address map (H,D) ↦ (H+AD,D) for a rational matrix A is performed via a factorization A=E1ΠE2 into lower-triangular factors and a partial permutation, at cost depending on the rank of A.
- `address-interchange`: Fast interchange of address chunks: Exchanging two address fields of u bits by XOR-combinations (address shears) at cost O(V u^τ) with τ<1, though the final effect is an exact permutation.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Applying the butterfly map to the same bit of up to d address chunks at once on numerical arrays, at cost O(V d^λ') with λ'<1.
- `main-multiplication`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time, κ=2^−182, via radix digits, Chinese-remainder axes, Gaussian resampling, chirps, the twist to the polynomial ring, synthetic transforms accelerated by fast address interchange and butterfly layers, then exact recovery.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine`: Multitape Turing machine
- `logarithms-and-floor-ceiling`: Logarithms and floor/ceiling
- `modular-arithmetic`: Modular arithmetic
- `prime-numbers-and-prime-powers`: Prime numbers and prime powers
- `chinese-remainder-theorem`: Chinese remainder theorem
- `roots-of-unity`: Roots of unity
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `radix-base-b-representation`: Radix (base-b) representation
- `schoolbook-multiplication-and-carries`: Schoolbook multiplication and carries
- `recursion-and-recurrences`: Recursion and recurrences
- `matrices-and-linear-maps`: Matrices and linear maps
- `rank-of-a-matrix`: Rank of a matrix
- `triangular-matrices`: Triangular matrices
- `vector-spaces-and-subspaces`: Vector spaces and subspaces
- `rational-numbers-and-fields`: Rational numbers and fields
- `permutations`: Permutations
- `multidimensional-arrays`: Multidimensional arrays
- `finite-sets-and-subsets`: Finite sets and subsets
- `cyclic-groups`: Cyclic groups
- `complex-magnitude-and-conjugate`: Complex magnitude and conjugate
- `fixed-point-and-rounding-error`: Fixed-point and rounding error
- `gaussian-function`: Gaussian function
- `time-and-space-on-tapes`: Time and space on tapes
- `inequalities-and-exponent-arithmetic`: Inequalities and exponent arithmetic

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
