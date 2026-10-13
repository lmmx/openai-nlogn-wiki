# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/D1` (paths below are relative to it)

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

`main-result`: Integer multiplication in O(n (lg n)^(1-κ)): A deterministic multitape Turing machine multiplies n-bit integers in O(n (lg n)^(1-κ)) time with κ=2^-182, disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate computer scientist: comfortable with asymptotic analysis, basic algorithm design (divide and conquer, recurrences, the idea of FFT-style multiplication at the level of knowing it exists), discrete math (modular arithmetic, primes, gcd, binary representation), and linear algebra (vectors, matrices, subspaces, rank, dimension, invertibility). They know complex numbers and polynomials, and basic multitape Turing machines. They have not studied the specialist material of the paper: Harvey-van der Hoeven machinery, Gaussian resampling, Bluestein, Chinese-remainder multidimensional reindexing, Bruhat factorization, or precise fixed-point error analysis.

## Pages, in reading order

- `nlogn-multiplier`: Known O(n log n) multiplier and the n log n conjecture: Harvey and van der Hoeven's O(n log n) multitape multiplication, used as an ordinary subroutine, and the Schönhage-Strassen conjecture that n log n is optimal.
- `convolution`: Convolution and cyclic convolution: The product of two coefficient lists as polynomials, with indices optionally wrapped around cyclically.
- `radix-digit-reduction`: Integer product as radix-digit convolution: Splitting each operand into radix-2^b digits turns the integer product into a convolution of digit lists, followed by carry propagation.
- `tape-layout-streams`: Address fields, streams and scans on tape: Arrays stored in lexicographic address order on tape, with fields of address digits, processed by linear scans, controlled shifts and cyclic splitting into role streams.
- `fixed-point-dyadic`: Fixed-point Gaussian dyadic records: Complex numbers stored with p fractional bits (real and imaginary parts multiples of 2^-p), with exact intermediate dyadics and a single truncation.
- `linear-network-frames`: Linear exchange networks with roles and frames: A fixed linear network exchanging two banks of values and restoring auxiliary values; applied to arrays via rows distributed over wire roles, with an invertible frame per gate so intermediate frames cancel.
- `address-shear`: Address shear and triangular factorization: The endpoint operator (H,D) -> (H+D,D) on address fields, with matrix shears implemented through lower-triangular (Bruhat-type) factorization in tape order.
- `subset-intersection-network`: Three-element-subset subspace construction: Finite network over subsets of size three whose gates and terminals carry nested subspaces of a fixed m-dimensional space, using intersection counts so that the number s of smaller calls satisfies s<Wm.
- `recursive-power-saving`: Recursive rank saving gives a power saving: A call at parameter mf uses s<Wm calls at parameter f on streams of volume V/W, so cost per volume grows as a power below the first, giving exponent <1.
- `address-interchange`: Fast address-field interchange costing O(V u^τ): Exchanging two disjoint address fields of u digits in an array of volume V in time O(V u^τ) with τ<1, via XOR-like combinations that end in an exact permutation.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: A reindexing of the coefficient list onto a product of cyclic axes of distinct prime lengths that preserves convolution, giving a multidimensional convolution.
- `dft`: Discrete Fourier transform and roots of unity: The transform evaluating a coefficient list at powers of a primitive root of unity; it turns convolution into pointwise product.
- `negacyclic-ring`: Polynomial ring modulo y^r+1: Complex polynomials of degree below r with y^r = -1, so powers of y act as roots of unity and multiplication by y^a is a signed shift of coefficients.
- `butterfly`: Two-point butterfly and fast transform levels: The radix-2 step mapping (u,v) to ((u+v)/2,(u-v)/2); a fast transform applies lg n levels of these, each costing a scan of the data.
- `synthetic-transform`: Synthetic polynomial transforms: Fourier transforms over the ring modulo y^r+1 using powers of y as roots, computed by signed shifts and butterflies and retaining one stored frequency order for the inverse.
- `gaussian-resampling`: Gaussian resampling: Harvey-van der Hoeven technique expressing a Fourier transform of prime length through a power-of-two tensor transform, with source and target permutations.
- `bluestein-chirp`: Bluestein chirp identity and phase twist: Rewriting a transform as a cyclic convolution via chirps; a phase twist turns the last cyclic axis into a negacyclic polynomial modulo y^r+1.
- `signed-packing`: Signed packing (Kronecker substitution): Evaluating polynomial products over the ring as a single integer product by packing signed coefficients into one integer, then unpacking.
- `permutation-cancellation`: Retaining permutations in the transform: The source permutation from resampling cancels across the two forward transforms, the pointwise product and the inverse transform, avoiding separate full sorts.
- `precision-exact-recovery`: Precision, rounding and carry recovery: Tracking contractive error bounds through all transforms so the recovered convolution coefficients err by less than 1/2, then rounding and propagating carries.
- `packed-selected-bit-addition`: Packed selected-bit addition: Adding (XOR) selected bit positions at positions rho+iK of grouped address chunks in one packed pass, the primitive behind changing address bits in the butterfly layer.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer on selected bits: Applying H_0 on the same bit position of up to d address chunks at once on polynomial records, with a complex phase network, in time O(V d^λ') with λ'<1, exact until one final truncation.
- `parameter-cost-accounting`: Parameter choice and total cost accounting: A fixed rational choice of exponents (including κ=2^-182) makes each cost term, divided by volume, a power of p below one so the total is O(n (lg n)^(1-κ)).
- `main-result`: Integer multiplication in O(n (lg n)^(1-κ)): A deterministic multitape Turing machine multiplies n-bit integers in O(n (lg n)^(1-κ)) time with κ=2^-182, disproving the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-tm`: Multitape Turing machine
- `linear-algebra-over-a-field`: Linear algebra over a field
- `modular-arithmetic`: Modular arithmetic
- `primes-gcd-and-coprimality`: Primes, gcd and coprimality
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `logarithms-floor-and-ceiling`: Logarithms, floor and ceiling
- `permutations`: Permutations
- `mixed-radix-and-positional-digit-expansion`: Mixed-radix and positional digit expansion
- `multidimensional-arrays-and-tensors`: Multidimensional arrays and tensors
- `elementary-gaussian-integers-and-dyadic-rationals`: Elementary Gaussian integers and dyadic rationals
- `norms-error-bounds-and-rounding`: Norms, error bounds and rounding
- `schoolbook-carry-addition`: Schoolbook carry addition
- `geometric-series-and-recurrences`: Geometric series and recurrences
- `roots-of-unity-and-euler-s-formula`: Roots of unity and Euler's formula
- `basic-finite-set-combinatorics`: Basic finite-set combinatorics
- `deterministic-algorithms-and-tape-scans`: Deterministic algorithms and tape scans

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
