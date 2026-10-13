# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/A2` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) time: A deterministic fixed-tape machine multiplying n-bit integers in O(n (lg n)^(1-κ)) time, refuting the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate computer scientist: asymptotic notation and recurrences, discrete mathematics (sets, products, permutations, modular arithmetic, the Chinese remainder theorem, logarithms, floor and ceiling), and introductory linear algebra (matrices, bases, subspaces, inner products, norms, Kronecker products). They know polynomials, complex numbers and roots of unity, basic Turing machines with tapes, and sorting and divide-and-conquer. They have not studied FFT-based multiplication in depth, abstract ring theory beyond basics, numerical error analysis, or any research on integer multiplication complexity.

## Pages, in reading order

- `convolution`: Convolution: Combining two coefficient lists so that entry k sums products a_i b_j over i+j=k (linearly, cyclically, or with negative wrap).
- `multiplication-via-convolution`: Multiplication as digit convolution: Split each integer into radix-2^b digits; the product's digit coefficients are the convolution of the digit lists, followed by carry propagation.
- `poly-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree below r with y^r = -1, so multiplying by a power of y is a signed shift of the coefficient list.
- `fixed-point-contraction`: Fixed-point dyadic arithmetic and contractions: Gaussian dyadic values on a 2^-p grid, one truncation per layer, and norm-nonincreasing linear maps whose errors add when composed.
- `crt-prime-axes`: Chinese-remainder map to prime axes: Re-indexing the coefficient list onto a product of distinct prime cyclic axes by the Chinese remainder theorem so cyclic convolution is preserved.
- `precision-recovery`: Precision and exact recovery: Bounding rounding error so recovered coefficients are within 1/2 of integers, then rounding and propagating carries.
- `fixed-tape-model`: Fixed-tape Turing machine model: The model: one fixed finite alphabet and a fixed finite number of one-dimensional tapes, where time counts steps and moving data over growing distances costs scans.
- `linear-network`: Linear network with roles and frames: A fixed linear network exchanging two banks of values while restoring auxiliary values; arrays on wires carry invertible frames that cancel along routes and leave an endpoint operator.
- `subset-network`: Three-subset intersection construction: Nested subspaces attached to gates using three-element subsets, with gather/scatter and auxiliary wires cancelling unwanted intersection coefficients, giving s<Wm smaller calls.
- `recursive-power-saving`: Recursive rank saving: Recursing at parameter mf with s calls on streams of volume V/W where s<Wm, so cost per volume grows by s/W<m per factor m, giving a power saving.
- `matrix-shear`: Triangular factorization of address shears: Bruhat-style factorization into lower triangular maps so a shear (H,D)→(H+D,D) of address fields is done by ordered scans.
- `address-interchange`: Fast interchange of address chunks: Swapping two disjoint address fields of u digits in time O(V u^τ), τ<1, via XOR-combined intermediate data restoring an exact permutation.
- `dft`: Discrete Fourier transform: Linear map F_q sending a length-q vector to its averaged sums with roots of unity e^(-2πi jk/q); it turns convolution into pointwise product and is a contraction.
- `fft-butterfly`: Fast transforms and butterflies: Computing a transform of power-of-two length in about log levels of two-point butterfly operations, each level scanning all data.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the ring modulo y^r+1 using powers of y as roots of unity, so all root multiplications are exact signed shifts.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H0(u,v)=((u+v)/2,(u-v)/2) on one bit in each of up to d address chunks at once on polynomial records in cost O(V d^λ'), λ'<1.
- `gaussian-resampling`: Gaussian resampling: Expressing a Fourier transform of prime-like length through a power-of-two multidimensional transform via Gaussian-weighted resampling, with permutations on source and target.
- `bluestein-chirp`: Bluestein chirp identity: Rewriting a DFT of arbitrary length as a convolution with a chirp e^(πi j^2/q) and pre/post multiplications.
- `phase-twist`: Last-coordinate phase twist: Multiplying by a diagonal phase so that a cyclic coordinate becomes a polynomial modulo y^r+1, whose negative wrap yields the cyclic wrap after the twist is removed.
- `schonhage-strassen-conjecture`: Schönhage–Strassen optimality conjecture: The 1971 O(n log n log log n) multitape multiplication and the conjecture that n log n is the optimal order of multiplication cost.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The unconditional O(n log n) multitape multiplication algorithm, used here as an ordinary subroutine on short inputs.
- `kronecker-packing`: Signed packing (Kronecker substitution): Packing polynomial coefficients, possibly negative, into one integer so a ring product becomes one integer product, recovered exactly afterward.
- `transform-layout`: Retained transform layout: Storing synthetic transform output in a layout where the parallel layers apply and keeping the frequency order so the opposite transform consumes it after pointwise product.
- `ring-convolution`: Exact normalized ring convolution: Convolution over the polynomial ring on the remaining axes: two forward transforms, pointwise ring products via signed packing, and the opposite transform.
- `resampling-no-sort`: Resampling with permutations left in the transform: Keeping the source and target coordinate permutations inside the transform identity so no separate full sorts are run, and the source permutation cancels across transforms.
- `parameter-choice`: Fixed rational parameter choice: Conservative fixed exponents (τ, λ, c, ε, etc.) compatible across procedures, yielding κ=2^-182.
- `multiplication-algorithm`: The multiplication algorithm: Digits to source arrays via address map, two forward transforms, pointwise product, opposite transform, rescale, round, carry.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) time: A deterministic fixed-tape machine multiplying n-bit integers in O(n (lg n)^(1-κ)) time, refuting the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `tm-basics`: Turing machines and tapes
- `binary-integers`: Binary integers
- `linear-maps-and-matrices`: Linear maps and matrices
- `subspaces-bases-and-dimension`: Subspaces, bases and dimension
- `tensor-kronecker-product-of-vectors-and-matrices`: Tensor (Kronecker) product of vectors and matrices
- `vector-norms-and-the-sup-norm`: Vector norms and the sup norm
- `inner-product-and-orthogonality`: Inner product and orthogonality
- `triangular-matrices-and-permutation-matrices`: Triangular matrices and permutation matrices
- `modular-arithmetic`: Modular arithmetic
- `chinese-remainder-theorem`: Chinese remainder theorem
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `cyclic-groups-and-indices-mod-m`: Cyclic groups and indices mod m
- `finite-field-f-2-and-xor`: Finite field F_2 and XOR
- `bit-operations-and-address-fields`: Bit operations and address fields
- `permutations`: Permutations
- `cartesian-products-and-multidimensional-arrays`: Cartesian products and multidimensional arrays
- `floor-ceiling-and-logarithms`: Floor, ceiling and logarithms
- `powers-of-two-and-dyadic-rationals`: Powers of two and dyadic rationals
- `rings-and-the-identity-y-r-1`: Rings and the identity y^r = -1
- `recurrences-and-recursion-cost-analysis`: Recurrences and recursion cost analysis
- `sorting-and-sequential-scans-on-tapes`: Sorting and sequential scans on tapes
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication
- `symbols-for-asymptotics-theta-and-omega`: Symbols for asymptotics: Theta and Omega
- `real-and-imaginary-parts-conjugates-and-modulus-bounds`: Real and imaginary parts, conjugates and modulus bounds
- `gaussian-function-and-gaussian-integers`: Gaussian function and Gaussian integers
- `subsets-binomial-counts-and-combinatorial-counting`: Subsets, binomial counts and combinatorial counting
- `fixed-finite-alphabet-and-worst-case-time`: Fixed finite alphabet and worst-case time
- `linear-independence-and-rank`: Linear independence and rank
- `cyclic-and-negacyclic-indices-as-polynomial-wrap`: Cyclic and negacyclic indices as polynomial wrap

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
