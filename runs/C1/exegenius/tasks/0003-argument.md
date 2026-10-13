# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/C1` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A fixed deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)), κ=2^−182, disproving the n log n optimality conjecture in that model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis including recurrences and logarithms, basic discrete mathematics (modular arithmetic, binary representation, divisibility and primes), linear algebra (vectors, matrices, tensor-like indexing of arrays), and elementary algorithms such as schoolbook multiplication. They know Turing machines and tapes, polynomials and complex numbers, but have not studied fast integer multiplication, the FFT in depth, number-theoretic transforms, finite fields, or abstract algebra beyond basics. Specialist material introduced by the paper is not assumed.

## Pages, in reading order

- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture: The 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers.
- `dft-convolution`: Convolution and discrete Fourier transform: Convolution of coefficient lists is computed by transforming, multiplying pointwise and inverting the transform, using roots of unity.
- `radix-digit-convolution`: Multiplication as digit convolution: Splitting each input into radix digits turns the integer product into a convolution of short integer coefficients, followed by carry propagation.
- `poly-ring-y-r-1`: Polynomial ring modulo y^r + 1: Polynomials in y with complex coefficients modulo y^r+1, where powers of y act as roots of unity and multiplication by them is a signed shift.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring where roots of unity are powers of y, so root multiplications are signed shifts and the work is butterflies, shifts and address rearrangements.
- `crt-address-map`: Chinese-remainder address map: A map placing the coefficient list on a product of distinct prime cyclic axes that preserves convolution.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven identity expressing a transform of arbitrary axis length through a transform with power-of-two axis lengths.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a transform as a normalized cyclic convolution via chirp phase factors.
- `fixed-point-precision`: Fixed-point precision and exact recovery: Complex fixed-point coefficients with dyadic intermediates, one truncation, and an error bound below 1/2 that allows exact rounding and carry propagation.
- `signed-packing`: Signed packing (Kronecker substitution): Packing polynomial coefficients into one long integer with signs so ring products are computed by an ordinary O(n log n) integer multiplier.
- `tape-streams`: Elementary tape streams and scans: Array layouts on tapes with address fields, scans, controlled shifts and fixed rational scalings, each costing linear time in stored bit volume.
- `gate-frames`: Linear networks with frames and roles: A fixed linear network exchanging banks of values; roles are wire positions and an invertible frame operator per gate makes intermediate representations cancel.
- `finite-network-subspaces`: Finite networks with rank saving: Networks built from three-element subsets with nested subspaces so the number s of smaller calls satisfies s<Wm.
- `recursive-power-saving`: Recursive power saving: Recursive calls at parameter mf use s<Wm calls at parameter f on volume V/W each, giving cost per volume growth with an exponent below 1.
- `address-interchange`: Fast interchange of address chunks: Interchanges two address fields of u bits in cost O(V u^τ), τ<1, through XOR combinations whose final effect is an exact permutation.
- `fast-butterfly-layers`: Simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u−v)/2) simultaneously on selected address bits of d chunks at cost O(V d^λ'), λ'<1.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A fixed deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)), κ=2^−182, disproving the n log n optimality conjecture in that model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-tm`: Multitape Turing machine
- `binary-representation-of-integers`: Binary representation of integers
- `logarithms-and-floor-ceiling`: Logarithms and floor/ceiling
- `modular-arithmetic`: Modular arithmetic
- `primes-and-coprimality`: Primes and coprimality
- `vectors-matrices-and-linear-maps`: Vectors, matrices and linear maps
- `tensor-kronecker-product-and-multidimensional-arrays`: Tensor (Kronecker) product and multidimensional arrays
- `roots-of-unity`: Roots of unity
- `schoolbook-multiplication-and-basic-divide-and-conquer`: Schoolbook multiplication and basic divide-and-conquer
- `recurrence-relations-and-geometric-sums`: Recurrence relations and geometric sums
- `floating-and-fixed-point-numbers-and-rounding`: Floating and fixed-point numbers and rounding
- `sorting-and-permutations`: Sorting and permutations
- `asymptotic-notation-variants`: Asymptotic notation variants
- `finite-sets-products-and-maps`: Finite sets, products and maps

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
