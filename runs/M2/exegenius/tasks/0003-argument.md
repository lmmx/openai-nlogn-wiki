# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/M2` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) on a multitape Turing machine: A deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n(lg n)^{1-κ}) time with κ=2^{-182}, disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: asymptotic analysis, discrete mathematics with modular arithmetic and primes, introductory linear algebra and probability-free algorithm design (divide and conquer, sorting, recursion with recurrences), complex numbers and polynomials, and basic Turing machines with tapes. They have likely seen the idea of the FFT only in passing, if at all, and have not studied abstract algebra, harmonic analysis, numerical error analysis or the Harvey-van der Hoeven line of work.

## Pages, in reading order

- `convolution`: Convolution and multiplication by radix digits: Splitting integers into radix digits turns integer multiplication into convolution of short integer coefficient lists.
- `poly-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree < r with y^r = -1, so multiplying by a power of y is a signed shift of the coefficient list.
- `tape-streams`: Tape streams, array order and controlled shifts: Elementary linear-time scans, array layouts in lexicographic address order, whole-chunk moves and controlled shifts on tapes.
- `linear-network-frames`: Linear exchange networks with frames and roles: Fixed linear networks that exchange two banks of values and restore auxiliary values, applied pointwise to arrays whose representations are changed by invertible frame operators.
- `subset-network`: Three-subset networks with rank saving: Finite networks built from three-element subsets whose gates and terminals carry nested subspaces so that the total number s of smaller calls is less than W times m.
- `recursive-saving`: Recursive power saving: Recursion with s calls at parameter f on volume V/W, with s/W < m, yields a power-of-parameter saving over naive passes.
- `address-interchange`: Address interchange in time O(V u^τ): Interchanging two disjoint address fields of u bits via XOR combinations of intermediate streams, with exact final permutation.
- `crt-map`: Chinese-remainder map to prime cyclic axes: Places the radix-digit coefficient list on a product of distinct prime cyclic axes so that convolution is preserved.
- `fixed-point-precision`: Fixed-point precision and error control: Complex values stored on a 2^{-p} grid, with contractive maps, error accumulation and rounding so integer coefficients are recoverable.
- `simultaneous-butterfly`: Simultaneous butterfly layer in time O(V d^λ′): Applies H0(u,v)=((u+v)/2,(u-v)/2) coefficientwise on the same bit in up to d address chunks, using exact Gaussian dyadics and one final truncation.
- `dft`: Discrete Fourier transform: Normalized transform (F_q u)_k = (1/q) Σ u_j e^{-2πi jk/q} that diagonalizes cyclic convolution and is a contraction in max norm.
- `nlogn-conjecture`: The n log n optimality conjecture and prior bounds: Schönhage and Strassen's O(n log n log log n) multiplier and conjecture that n log n is optimal, followed by the Harvey–van der Hoeven O(n log n) multiplier.
- `tensor-transform`: Multidimensional transform on power-of-two axes: A tensor-product Fourier transform over several axes of power-of-two length, with arbitrary growing dimension.
- `synthetic-transform`: Synthetic polynomial transforms: Fourier transforms over the polynomial ring whose roots of unity are powers of y, computed by signed shifts and two-point butterflies (Nussbaumer).
- `bluestein`: Bluestein chirp identity: Rewrites a Fourier transform of arbitrary length as a cyclic convolution via chirp factors.
- `signed-packing`: Signed packing (Kronecker substitution): Packing polynomial coefficients including negative ones into one integer so ring products reduce to integer multiplication by the O(n log n) multiplier.
- `ring-convolution`: Normalized convolution over the polynomial ring with retained frequency order: Convolution computed by two forward synthetic transforms, a pointwise product via packed products, and the opposite transform, keeping the same frequency order throughout.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven reduction expressing a Fourier transform on prime lengths via a power-of-two multidimensional transform, here keeping source and target permutations inside the transform formula.
- `multiplication-assembly`: Assembly of the multiplication algorithm: Chains digit convolution, CRT, Gaussian resampling, chirps, twist to the polynomial ring, rescaling, rounding and carry propagation, with parameters chosen so the cost table fits the theorem.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) on a multitape Turing machine: A deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n(lg n)^{1-κ}) time with κ=2^{-182}, disproving the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `multitape-tm`: Multitape Turing machine
- `complex-poly`: Complex numbers and polynomials
- `euler-s-formula-and-roots-of-unity`: Euler's formula and roots of unity
- `modular-arithmetic-and-divisibility`: Modular arithmetic and divisibility
- `chinese-remainder-theorem`: Chinese remainder theorem
- `prime-numbers`: Prime numbers
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `radix-b-representation-of-integers`: Radix-b representation of integers
- `schoolbook-carry-addition-and-multiplication`: Schoolbook carry addition and multiplication
- `divide-and-conquer-recurrences`: Divide and conquer recurrences
- `logarithms-and-exponentials`: Logarithms and exponentials
- `sums-products-and-summation-manipulation`: Sums, products and summation manipulation
- `vectors-matrices-and-linear-maps`: Vectors, matrices and linear maps
- `subspaces-dimension-and-rank`: Subspaces, dimension and rank
- `vector-norms-and-the-max-norm`: Vector norms and the max norm
- `permutations-and-bijections`: Permutations and bijections
- `multidimensional-arrays-and-index-tuples`: Multidimensional arrays and index tuples
- `floating-and-fixed-point-approximation-and-rounding`: Floating and fixed-point approximation and rounding
- `floor-ceiling-and-rounding-functions`: Floor, ceiling and rounding functions
- `real-analysis-basics-inequalities-and-exponential-decay`: Real analysis basics: inequalities and exponential decay
- `dyadic-rationals`: Dyadic rationals
- `cyclic-and-negacyclic-indexing`: Cyclic and negacyclic indexing
- `time-complexity-of-sorting-and-merging-on-tapes`: Time complexity of sorting and merging on tapes

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
