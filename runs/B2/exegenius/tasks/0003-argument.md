# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/B2` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1-κ)), κ=2^-182, refuting the n log n conjecture; it chains digit convolution, CRT axes, resampling, chirps, phase twist and synthetic transforms, accelerated by fast address interchange and butterfly layers.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished undergraduate computer science: asymptotic analysis, discrete mathematics, linear algebra over the reals and complex numbers, basic algebra (modular arithmetic, primes, finite fields of two elements at an introductory level), recurrences and divide-and-conquer algorithms such as Karatsuba and the FFT in outline. They have seen Turing machines and tapes but not tape-level complexity theory, and have not studied Fourier analysis on groups, coding theory, or the research literature on fast multiplication.

## Pages, in reading order

- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture: The conjecture that n log n is the optimal order of cost for multiplying n-bit integers on a multitape Turing machine; refuting it needs one machine with liminf T(n)/(n lg n)=0.
- `convolution-dft`: Convolution and discrete Fourier transform: Integer multiplication reduces to convolution of digit lists, which Fourier transforms compute through pointwise products; normalized transforms are contractions.
- `nlogn-multiplier`: Harvey–van der Hoeven O(n log n) multiplication: The established unconditional O(n log n) multiplier, used only as an ordinary subroutine for polynomial products.
- `ring-mod-yr1`: Polynomial ring modulo y^r + 1: Polynomials in y reduced by y^r = -1, so powers of y are roots of unity and multiplying by one is a signed shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring using powers of y as roots, built from address rearrangements, signed shifts and two-point butterflies.
- `tape-scans`: Array order and tape scans: Arrays stored in address order on tapes; scanning Θ(n) bits at each of Θ(log n) levels already costs Θ(n log n), so movement must be saved.
- `linear-network-frames`: Linear networks with roles and frames: A fixed linear network exchanging two banks of values with signs, restoring all auxiliary values; roles are wire places and frames are invertible operators changing stored representation so only an endpoint operator remains.
- `crt-address-map`: Chinese-remainder address map: Places the digit list on a product of distinct prime cyclic axes, preserving convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven reduction expressing a Fourier transform through a multidimensional transform with power-of-two axis lengths.
- `bluestein-chirp`: Bluestein chirp conversion: Converts the middle transform, with its target permutation, into a normalized cyclic convolution.
- `phase-twist`: Last-coordinate phase twist: A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap gives the original cyclic wrap once the twist is removed.
- `stream-operations`: Elementary stream operations and controlled shifts: Linear-time tape scans: digit swaps, moving digits, splitting rows into W role streams, and controlled shifts of a field.
- `finite-subspace-network`: Finite networks with a rank saving: Network construction using three-element subsets and nested subspaces, so that the sum s of edge ranks satisfies s<Wm.
- `recursive-power-saving`: Recursive power saving: A call at parameter mf uses s calls at parameter f on volume V/W; since s/W<m, the normalized cost grows by less than m per scaling, giving a power saving.
- `address-shear`: Address shear and triangular factorization: Endpoint operator (H,D)→(H+D,D) on address fields, implemented via lower-triangular factorization and linear-cost controlled shifts.
- `address-interchange`: Fast address-field interchange: Interchanges two disjoint address fields of u bits in V stored bits at cost O(V u^τ), τ<1, via XOR combinations ending in an exact permutation.
- `signed-packing`: Signed coefficient packing: A form of Kronecker substitution that packs polynomial coefficients into integers so polynomial products use the integer multiplier.
- `fixed-point-dyadics`: Exact Gaussian dyadics and precision: Values are exact Gaussian dyadics with power-of-two denominators; truncation after contractive layers adds bounded error, tracked so the final error is below 1/2.
- `butterfly-layer`: Fast simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u-v)/2) simultaneously on selected bits of several address chunks at cost O(V d^λ'), λ'<1, using phase frames and dyadic scaling.
- `tensor-resampling-chirps`: Tensor resampling with retained permutations: Multidimensional resampling identity RF_s = 2^γ B0 Q F_t A keeping the coordinate permutations, which cancel through chirp convolution and pointwise products.
- `exact-recovery`: Rounding and carry propagation: After removing normalizations, the recovered coefficient error is below 1/2, so rounding and carries give the exact binary product.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1-κ)), κ=2^-182, refuting the n log n conjecture; it chains digit convolution, CRT axes, resampling, chirps, phase twist and synthetic transforms, accelerated by fast address interchange and butterfly layers.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine-tapes`: Multitape Turing machine
- `integer-multiplication-algorithms`: Integer multiplication algorithms
- `binary-representation-and-bit-strings`: Binary representation and bit strings
- `modular-arithmetic`: Modular arithmetic
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `chinese-remainder-theorem`: Chinese remainder theorem
- `fast-fourier-transform`: Fast Fourier transform
- `roots-of-unity`: Roots of unity
- `linear-algebra-over-a-field`: Linear algebra over a field
- `the-field-f-2-and-binary-vector-spaces`: The field F_2 and binary vector spaces
- `triangular-matrices-and-factorization`: Triangular matrices and factorization
- `permutations`: Permutations
- `divide-and-conquer-recurrences`: Divide-and-conquer recurrences
- `logarithms-and-iterated-logarithms`: Logarithms and iterated logarithms
- `little-o-omega-and-liminf-asymptotics`: Little-o, Omega and liminf asymptotics
- `convolution-of-sequences`: Convolution of sequences
- `norms-and-error-bounds`: Norms and error bounds
- `dyadic-rationals-and-fixed-point-numbers`: Dyadic rationals and fixed-point numbers
- `gaussian-function`: Gaussian function
- `direct-sum-and-tensor-product-of-vector-spaces`: Direct sum and tensor product of vector spaces
- `polynomial-evaluation-and-interpolation`: Polynomial evaluation and interpolation
- `asymptotic-definition-of-algorithm-cost-and-time-complexity`: Asymptotic definition of algorithm cost and time complexity

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
