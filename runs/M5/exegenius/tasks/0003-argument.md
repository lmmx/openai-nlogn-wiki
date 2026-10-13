# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/M5` (paths below are relative to it)

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

`target`: Multiplying n-bit integers in O(n (lg n)^(1-κ)) time: Deterministic multitape algorithm combining digit convolution, Chinese-remainder map, Gaussian resampling, chirps, synthetic transforms with fast tape procedures, and carries.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science degree: discrete mathematics (induction, sets, modular arithmetic, primes, permutations, binary representation), algorithm analysis with recurrences, and a first course in linear algebra (vector spaces, subspaces, dimension, invertible and triangular matrices). They know big-O, polynomials, complex numbers including roots of unity, and basic Turing machines with tapes. They have not studied the FFT-based multiplication literature, Schönhage–Strassen, Nussbaumer transforms, multitape complexity theory in depth, or numerical error analysis beyond basics.

## Pages, in reading order

- `multitape-model`: Multitape Turing machine multiplication model: Fixed finite alphabet, fixed finite number of one-dimensional tapes; cost is the number of steps for bit-level multiplication.
- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen proposed n log n as the optimal order for multiplying n-bit integers; Harvey–van der Hoeven reached O(n log n).
- `convolution`: Radix digits and convolution: Splitting integers into radix digits turns multiplication into convolution of short integer coefficient lists.
- `fourier-transform`: Discrete Fourier transform: Evaluates a coefficient list at roots of unity; it turns convolution into pointwise product.
- `multidimensional-transform`: Multidimensional transforms with power-of-two axes: A transform on an array with several axes, each of power-of-two length, applied axis by axis.
- `polynomial-ring`: Polynomial ring modulo y^r + 1: Complex-coefficient polynomials in y reduced by y^r = -1, with r a power of two; negacyclic wrap.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms using powers of y as roots of unity, so root multiplications are signed shifts of coefficient lists.
- `butterfly`: Two-point butterfly: The operation H0(u,v) = ((u+v)/2, (u−v)/2) applied coefficientwise.
- `fixed-point-precision`: Fixed-point Gaussian dyadics and exact recovery: Complex coefficients stored in fixed point with exact Gaussian dyadic intermediates; error is shown below 1/2 so rounding recovers integer coefficients.
- `tape-streams`: Tape array order and elementary stream operations: Arrays stored in address order on tapes with scans, address fields, controlled shifts and whole-chunk moves.
- `linear-network`: Linear network with roles and frames: A fixed linear network exchanging two banks of values; wires are roles, each gate has an invertible frame, and intermediate frames cancel, leaving an endpoint operator.
- `restored-auxiliaries`: Restoring auxiliary values: Scratch values with arbitrary initial contents are subtracted, used, and added back so the result is exact for any initial auxiliary values.
- `address-shear`: Address shear and triangular factorization: The map (H,D) to (H+D,D) on two address fields, with matrix factorization into lower-triangular factors, which with two linear-cost updates completes an interchange.
- `subset-network`: Finite networks from three-element subsets: Subspaces of a fixed m-dimensional space attached to gates, built from three-element subsets with gather, scatter and auxiliary wires, giving fewer than Wm smaller calls.
- `recursive-saving`: Recursive power saving: Because s/W < m, multiplying the parameter by m raises the per-volume cost by less than m, giving a cost of volume times a power of the parameter below 1.
- `address-interchange`: Fast address-field interchange: Interchanges two disjoint contiguous address fields of u bits in an array of stored bit volume V in time O(V u^τ) with τ<1, using XOR combinations of data.
- `fast-butterfly-layer`: Simultaneous butterfly layer: Applies H0 simultaneously on the same bit position in d address chunks of numerical arrays, cost O(V d^λ') with λ'<1, with a single truncation after the layer.
- `crt-address-map`: Chinese-remainder map to prime cyclic axes: A Chinese-remainder address map that places a coefficient list on a product of distinct prime cyclic axes while preserving convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven identity expressing a source Fourier transform through a power-of-two tensor transform, with source and target permutations.
- `bluestein-chirp`: Bluestein chirp identity: Converts a transform into a normalized cyclic convolution via multiplication by chirp phases.
- `phase-twist`: Phase twist to the polynomial ring: A phase multiplication that turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap gives the original cyclic wrap after untwisting.
- `signed-packing`: Signed packing (Kronecker substitution): Packs polynomial coefficients into one integer so a polynomial product is computed by an ordinary integer multiplier.
- `transform-layout`: Transform layout with retained frequency order: Layout on tape in which forward synthetic transforms keep the same frequency order through pointwise product and the opposite transform consumes it.
- `carry-propagation`: Rescaling and carry propagation: Removing known normalizations and digit scales and propagating carries turns recovered coefficients into the binary product.
- `target`: Multiplying n-bit integers in O(n (lg n)^(1-κ)) time: Deterministic multitape algorithm combining digit convolution, Chinese-remainder map, Gaussian resampling, chirps, synthetic transforms with fast tape procedures, and carries.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine`: Turing machines and tapes
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `floors-ceilings-and-logarithms`: Floors, ceilings and logarithms
- `asymptotic-notation-beyond-big-o`: Asymptotic notation beyond big-O
- `vector-spaces-subspaces-and-dimension`: Vector spaces, subspaces and dimension
- `matrices-invertibility-and-linear-maps`: Matrices, invertibility and linear maps
- `permutations-and-bijections`: Permutations and bijections
- `cartesian-products-and-index-tuples`: Cartesian products and index tuples
- `mathematical-induction-and-recurrences`: Mathematical induction and recurrences
- `schoolbook-multiplication-and-linear-time-addition`: Schoolbook multiplication and linear-time addition
- `cyclic-and-negacyclic-indexing`: Cyclic and negacyclic indexing
- `dyadic-rationals-and-fixed-point-numbers`: Dyadic rationals and fixed-point numbers
- `sup-norm-and-rounding-error-bounds`: Sup norm and rounding error bounds
- `real-and-imaginary-parts-complex-conjugate-and-modulus`: Real and imaginary parts, complex conjugate and modulus
- `summation-geometric-series-and-inequalities`: Summation, geometric series and inequalities

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
