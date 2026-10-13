# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/D4` (paths below are relative to it)

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

`main-theorem`: Integer multiplication below n log n: A deterministic fixed-tape Turing machine multiplies n-bit integers in O(n (lg n)^(1−κ)) time with κ=2^(−182), disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, algorithms (divide and conquer, recurrences, FFT-style ideas at a basic level), discrete mathematics (sets, binomial coefficients, binary representation, modular arithmetic, primes), and linear algebra (vector spaces, subspaces, rank, matrix products, Gaussian elimination, orthogonal projections, over the rationals and basic finite fields). They know complex numbers and polynomials, and basic Turing machines. They have not studied advanced algebra (Bruhat decomposition, general rings and quotients in depth), number theory beyond basics, numerical error analysis of FFTs, or the research literature on fast multiplication.

## Pages, in reading order

- `convolution-dft`: Convolution and the discrete Fourier transform: Convolution multiplies coefficient lists as polynomials; a Fourier transform at roots of unity turns it into pointwise products.
- `mult-to-convolution`: Integer multiplication as digit convolution: Splitting each n-bit integer into radix digits turns the product into a convolution of short integer coefficients, followed by carry propagation.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven reduction replacing arbitrary-length Fourier transforms by multidimensional transforms with power-of-two axis lengths.
- `ring-mod-y-r-plus-1`: Polynomial ring modulo y^r + 1: Complex polynomials in y reduced with y^r = −1, where powers of y act as roots of unity and multiplying by them is a signed shift.
- `butterfly`: Two-point butterfly: The operation H₀(u,v) = ((u+v)/2, (u−v)/2) on a pair of values, the building block of transform layers.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms using powers of y in the ring as roots of unity, built from address rearrangements, signed shifts and butterflies.
- `fixed-point-dyadics`: Fixed-point complex coefficients and exact dyadics: Records hold complex fixed-point coefficients; layers are exact Gaussian dyadics with power-of-two denominators and a single truncation afterwards.
- `bluestein-chirp`: Bluestein chirp conversion: Bluestein's chirp identity rewrites a transform of arbitrary length as a cyclic convolution.
- `phase-twist`: Coefficient twist to the negative wrap: Multiplying coefficients by phases turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap reproduces the cyclic wrap after untwisting.
- `exact-recovery`: Rounding, rescaling and carry propagation: Known normalizations and digit scales are removed, coefficient error is shown below 1/2, and carries yield the exact binary product.
- `signed-packing`: Signed packing (Kronecker substitution): Packing signed polynomial coefficients into one integer so that a polynomial product is computed by an ordinary integer multiplication.
- `fixed-tape-model`: Fixed-tape machine model and stream scans: The cost model: one fixed alphabet and a fixed number of one-dimensional tapes, where moving data by a bounded number of scans is cheap but permuting growing fields is not.
- `nlogn-conjecture`: History and the n log n conjecture: Schönhage–Strassen gave O(n log n log log n) and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).
- `linear-network-frames`: Linear networks with frames and restored auxiliaries: A fixed linear network exchanges two banks of roles with signs; frames D_v change array representation along edges, intermediate frames cancel, and auxiliary values are restored.
- `address-shear`: Address shear and triangular factorization: The endpoint operator (H,D) ↦ (H+D,D) on address fields over a residue ring, implemented via lower-triangular factorization.
- `subset-network`: Finite network from three-element subsets: A finite network with nested subspaces of an m-dimensional space attached to gates, built from three-element subset intersection counts, with total smaller calls s < Wm.
- `recursive-saving`: Recursive power saving: Applying the network at parameter mf uses s calls at parameter f on streams of volume V/W, and s < Wm makes the per-volume cost grow like a power below 1.
- `fast-address-interchange`: Fast interchange of address chunks: Interchanging two disjoint contiguous address fields of u bits at cost O(V u^τ), τ<1, via XOR combinations that end as an exact permutation.
- `fast-butterfly-layers`: Simultaneous fast butterfly layers: Applying H₀ on the same selected bit of up to d address chunks at once at cost O(V d^λ′), λ′<1, with phase frames and a single truncation.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Placing the radix-digit coefficient list on a product of distinct prime cyclic axes so that convolution is preserved.
- `transform-layout`: Synthetic transform layout with retained frequency order: Layout on which the parallel layers apply; forward transforms keep the same frequency order through the pointwise product and the inverse consumes it.
- `permutation-cancellation`: Retained permutations cancelling: Source and target coordinate permutations are kept inside the transform identity and cancel across the forward transforms, product and inverse, avoiding full sorts.
- `polynomial-products`: Exact normalized polynomial products: Ring products in the transformed domain computed by signed packing and the established O(n log n) multiplier used as an ordinary subroutine.
- `multiplication-algorithm`: The assembled multiplication algorithm: Pipeline: digits to prime axes, resampling and chirps to power-of-two axes, phase twist to the ring, synthetic-transform convolution, then exact recovery.
- `main-theorem`: Integer multiplication below n log n: A deterministic fixed-tape Turing machine multiplies n-bit integers in O(n (lg n)^(1−κ)) time with κ=2^(−182), disproving the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-tapes`: Multitape Turing machines
- `binary-representation-of-integers`: Binary representation of integers
- `hamming-weight`: Hamming weight
- `bitwise-xor`: Bitwise XOR
- `modular-arithmetic`: Modular arithmetic
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `linear-algebra-over-the-rationals`: Linear algebra over the rationals
- `gaussian-elimination-and-the-general-linear-group-over-f2`: Gaussian elimination and the general linear group over F2
- `binomial-coefficients-and-basic-counting`: Binomial coefficients and basic counting
- `recurrences-and-divide-and-conquer`: Recurrences and divide and conquer
- `exponentials-logarithms-and-iterated-logarithm-bounds`: Exponentials, logarithms and iterated logarithm bounds
- `matrix-and-block-notation`: Matrix and block notation
- `roots-of-unity-and-euler-s-formula`: Roots of unity and Euler's formula
- `fast-fourier-transform-idea`: Fast Fourier transform idea
- `sorting-and-permutations`: Sorting and permutations
- `basic-real-error-bounds`: Basic real error bounds
- `schoolbook-integer-multiplication-and-carries`: Schoolbook integer multiplication and carries

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
