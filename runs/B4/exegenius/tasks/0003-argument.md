# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/B4` (paths below are relative to it)

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

`main-theorem`: Multiplication in O(n (lg n)^{1-κ}) time: The deterministic multitape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}) time with κ = 2^{-182}, disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: asymptotic analysis, algorithms (including divide and conquer, sorting, and the basic idea of fast multiplication), basic Turing machines, and the supporting mathematics of linear algebra, discrete math, probability-free basics, and complex numbers. They have not studied the FFT in depth, algebraic complexity, polynomial rings modulo relations, number theory beyond modular arithmetic and CRT basics, or numerical error analysis, and they know nothing of the research literature on fast multiplication.

## Pages, in reading order

- `multitape-model`: Fixed multitape Turing machine model: The bit-complexity model: one deterministic machine with a fixed finite alphabet and a fixed number of one-dimensional tapes, where moving data costs time.
- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen's O(n log n log log n) multiplication and their conjecture that n log n is optimal, followed by Fürer and Harvey–van der Hoeven reaching O(n log n).
- `dft-convolution`: Discrete Fourier transform and convolution: The DFT evaluates a sequence at roots of unity; pointwise multiplication of transforms corresponds to convolution of sequences, which is how products are computed.
- `radix-digit-reduction`: Multiplication as convolution of radix digits: Splitting each n-bit operand into short radix-2^b digits makes the integer product a convolution of digit lists, followed by carry propagation.
- `polynomial-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree below r with y^r = -1; multiplying by a power of y is a signed cyclic shift of the coefficient list.
- `butterfly-h0`: Two-point butterfly H₀: The map (u,v) ↦ ((u+v)/2,(u−v)/2) applied coefficientwise; layers of these make up a radix-two transform.
- `synthetic-transform`: Synthetic polynomial transform: A Nussbaumer-style Fourier transform over the polynomial ring whose roots of unity are powers of y, so multiplications are signed shifts; computed by radix-two butterflies.
- `fixed-point-precision`: Fixed-point dyadic precision and exact recovery: Coefficients stored as p-bit grid values on the unit disk, with truncation errors tracked through contractions so the final integer coefficient error is below 1/2.
- `cyclic-crt`: Chinese-remainder map to prime cyclic axes: Placing the digit list on a product of cyclic axes of distinct prime lengths by a Chinese-remainder address map that preserves convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's reduction of a Fourier transform of coprime length to a transform with power-of-two axis lengths, using Gaussian-weighted resampling maps that are contractions.
- `bluestein`: Bluestein's chirp identity: Rewriting a DFT as a convolution with a chirp (quadratic phase) sequence.
- `coefficient-twist`: Coefficient twist from cyclic to negacyclic: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} turns cyclic convolution of length r into multiplication modulo y^r+1, with the wrap sign cancelling.
- `hvdh-multiplier`: Established O(n log n) multiplier (subroutine): The Harvey–van der Hoeven O(n log n) integer multiplier, used here only as an ordinary subroutine for short products.
- `stream-operations`: Tape streams, array order and elementary scans: Arrays stored in row-major address order on tapes, with linear-time scans, controlled shifts and affine updates of later fields from earlier ones.
- `linear-network-frames`: Linear network with roles and frames: A fixed linear network exchanging two banks of values with signs and restoring auxiliary wires; applied to arrays by giving each wire an invertible frame operator so that intermediate frames cancel and only an endpoint operator remains.
- `subset-intersection-labels`: Subset-intersection subspace labels: Nested subspaces spanned by tensor products of three-element-subset indicator vectors (Frankl–Wilson/Alon style), giving a network whose total edge rank s is less than W·m.
- `recursive-saving`: Recursive power saving from rank deficit: A call at parameter m·f uses s < W·m calls at parameter f on volume V/W, so normalized cost grows by factor s/W < m per level, giving cost V·(parameter)^{τ} with τ < 1.
- `lower-triangular-factorization`: Lower triangular (Bruhat-type) factorization and matrix shear: Every rational matrix of rank a factors as E₁ΠE₂ with E_i lower triangular and Π a partial permutation with a ones, so a shear costs only a smaller interchanges plus linear-time updates.
- `fast-address-interchange`: Fast interchange of address chunks: Interchanging two contiguous address fields of u bits in a Cartesian-product array, by XOR/shear combinations through the bit network, at cost O(V u^τ) for fixed τ < 1.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀ at the same bit position of up to d address chunks at once on records of complex fixed-point polynomials, using the complex phase network, at cost O(V d^λ′).
- `resampling-keep-permutations`: Resampling with permutations left in the transform: Keeping the source and target coordinate permutations inside the transform identity so they cancel across the forward and inverse transforms instead of being executed as sorts.
- `signed-packing`: Signed packing (Kronecker substitution): Multiplying ring polynomials exactly by packing their integer coefficients, including negative ones, into long integers and calling the integer multiplier.
- `ring-convolution`: Exact normalized convolution over the polynomial ring: Convolution on the remaining axes via forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform consuming the same frequency order.
- `parameter-choice`: Fixed rational parameter choice: The conservative constants (τ, λ, λ′, ε, δ, κ = 2^{-182}) chosen compatibly so all terms in the cost table fit the main bound.
- `multiplication-algorithm`: Complete multiplication algorithm and cost: Digits → CRT address map → forward synthetic Gaussian-resampled transforms of both operands → pointwise product → inverse transform → rescale, round and carry to get the exact product.
- `main-theorem`: Multiplication in O(n (lg n)^{1-κ}) time: The deterministic multitape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}) time with κ = 2^{-182}, disproving the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine`: Turing machines and tapes
- `linear-algebra-basics`: Linear algebra basics
- `modular-arithmetic`: Modular arithmetic
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `binary-representation-and-radix-expansion`: Binary representation and radix expansion
- `schoolbook-multiplication-and-carries`: Schoolbook multiplication and carries
- `divide-and-conquer-and-recurrences`: Divide and conquer and recurrences
- `sorting-and-its-cost`: Sorting and its cost
- `logarithms-and-exponentials`: Logarithms and exponentials
- `cartesian-product-and-mixed-radix-indexing`: Cartesian product and mixed-radix indexing
- `cyclic-groups-and-roots-of-unity`: Cyclic groups and roots of unity
- `euclidean-norm-and-unit-disk`: Euclidean norm and unit disk
- `fixed-point-and-rounding-arithmetic`: Fixed-point and rounding arithmetic
- `proof-by-induction-and-summation`: Proof by induction and summation
- `subsets-indicator-vectors-and-set-intersection`: Subsets, indicator vectors and set intersection
- `permutation-matrices`: Permutation matrices
- `euler-s-formula-and-trigonometry`: Euler's formula and trigonometry
- `gaussian-function`: Gaussian function
- `big-endian-bit-strings-and-boolean-operations`: Big-endian bit strings and Boolean operations
- `rational-numbers-and-field-arithmetic`: Rational numbers and field arithmetic

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
