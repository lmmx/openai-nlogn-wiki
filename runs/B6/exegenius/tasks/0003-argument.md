# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/B6` (paths below are relative to it)

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

`main-theorem`: Sub-n log n integer multiplication algorithm: Deterministic multitape Turing machine multiplying n-bit integers in O(n (lg n)^{1-κ}), κ=2^{-182}, by reducing to convolution, resampling, chirps and synthetic transforms accelerated by fast address interchange and butterfly layers.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, basic algorithms, discrete mathematics (modular arithmetic, primes, counting, induction), linear algebra over the reals and complex numbers including matrices, rank, invertibility, subspaces and inner products, and elementary Turing machines. They have seen the idea of the FFT and polynomial multiplication, but not Schönhage–Strassen-style multiplication, Nussbaumer transforms, Harvey–van der Hoeven techniques, or specialist tensor and finite-field matrix factorization material.

## Pages, in reading order

- `multiplication-history`: Schönhage–Strassen conjecture and prior bounds: Multiplication of n-bit integers was known in O(n log n log log n), then n log n 2^O(log* n), then O(n log n) (Harvey–van der Hoeven); Schönhage and Strassen conjectured n log n is optimal.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree < r with y^r = -1; powers of y act as roots of unity and multiplying by one is a signed cyclic shift of the coefficient list.
- `fixed-point-gaussian-dyadics`: Fixed-point Gaussian dyadic numerics: Numbers 2^{-p}(a+ib) in a disk, stored as two's-complement records; intermediate values are exact and a single truncation follows a contractive layer.
- `coefficient-twist`: Coefficient twist to negacyclic convolution: Mapping x to ζy with ζ=e^{πi/r} turns cyclic convolution of length r into negacyclic ring convolution, multiplying coefficient k by ζ^k.
- `tape-streams`: Array order and elementary tape scans: Arrays stored in address order on tape; linear-time scans, pointwise operations and field updates.
- `bank-exchange-network`: Fixed linear network exchanging two banks with restored auxiliaries: A fixed network of linear gates on role wires that swaps two data banks with signs and restores every auxiliary value.
- `frames`: Frames and pointwise gates on arrays: Invertible linear operators D_v giving the stored representation of each wire array; pointwise gates commute with a common frame so intermediate frames cancel.
- `subset-intersection-labels`: Three-element subset construction with nested subspaces: Gather/scatter on three-element subsets with intersection-count pairings, plus side wires, give nested subspace labels with total rank deficit s < Wm.
- `recursive-power-saving`: Recursive rank saving: Edge operators of rank a need a smaller calls; since the total s of calls satisfies s<Wm, parameter growth by m raises cost per volume by s/W<m, giving a power saving.
- `address-shear`: Address shear and Bruhat factorization: Updating fields (H,D) to (H+D,D) over a residue ring and factoring matrices into triangular pieces that can be applied in tape order.
- `fast-address-interchange`: Fast interchange of address chunks: Interchanges two disjoint contiguous u-bit address fields of an array of volume V in O(V u^τ), τ<1, using XOR combinations that cancel to an exact permutation.
- `convolution-dft`: Convolution and the discrete Fourier transform: Convolution of coefficient lists is computed by transforming, multiplying pointwise, and inverse transforming with the normalized DFT.
- `integer-to-convolution`: Radix-digit reduction of integer multiplication to convolution: Splitting integers into radix digits turns the product into a convolution of short integer coefficient lists, followed by carry propagation.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style Fourier transforms over the negacyclic ring where roots of unity are powers of y, so the work is address rearrangement, signed shifts and two-point butterflies.
- `simultaneous-butterfly-layers`: Simultaneous butterfly layers: Apply H_0(u,v)=((u+v)/2,(u-v)/2) coefficientwise on the same selected bit in each of d address chunks in O(V d^λ'), λ'<1, with phase frames and a single truncation.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Places the digit coefficient list on a product of distinct prime-length cyclic axes in a way preserving convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven technique expressing a Fourier transform of coprime-length axes through a multidimensional power-of-two tensor transform, with source and target permutations.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a Fourier transform of arbitrary length as a convolution multiplied by chirp phases.
- `synthetic-layout`: Synthetic transform tape layout: Layout of roots, butterflies and stored frequency order on tape so the parallel layers apply and the same frequency order persists through the pointwise product.
- `exact-recovery`: Precision and exact recovery: Removing normalizations, showing coefficient error is below 1/2, rounding and propagating carries to get the exact binary product.
- `kronecker-signed-packing`: Signed Kronecker packing: Packing polynomial coefficients, including negative ones, into one integer so that a single integer product yields the polynomial product.
- `hh-subroutine`: Harvey–van der Hoeven O(n log n) multiplier as subroutine: The established O(N log N) fixed-tape integer multiplier, used as an ordinary subroutine on small inputs, not recursively.
- `normalized-polynomial-products`: Exact normalized ring products: Pointwise product of ring elements by signed packing and the O(n log n) multiplier, returning rounded results.
- `resampling-permutations-in-transform`: Resampling with permutations left in the transform: Keeps source and target coordinate permutations inside the transform identity so they cancel and avoid full sorts.
- `main-theorem`: Sub-n log n integer multiplication algorithm: Deterministic multitape Turing machine multiplying n-bit integers in O(n (lg n)^{1-κ}), κ=2^{-182}, by reducing to convolution, resampling, chirps and synthetic transforms accelerated by fast address interchange and butterfly layers.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-turing-machine`: Multitape Turing machine
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `floor-and-ceiling-functions`: Floor and ceiling functions
- `binary-representation-of-integers`: Binary representation of integers
- `hamming-weight`: Hamming weight
- `logarithms-and-exponentials`: Logarithms and exponentials
- `matrices-and-linear-maps`: Matrices and linear maps
- `rank-subspaces-and-orthogonal-complements`: Rank, subspaces and orthogonal complements
- `linear-algebra-over-the-field-f-2`: Linear algebra over the field F_2
- `gaussian-elimination`: Gaussian elimination
- `triangular-and-permutation-matrices`: Triangular and permutation matrices
- `tensor-kronecker-product-of-vectors-and-matrices`: Tensor (Kronecker) product of vectors and matrices
- `gaussian-integers`: Gaussian integers
- `dyadic-rationals`: Dyadic rationals
- `complex-modulus-and-norms`: Complex modulus and norms
- `euler-s-formula-and-complex-exponentials`: Euler's formula and complex exponentials
- `abstract-algebra-basics-rings-and-fields`: Abstract algebra basics: rings and fields
- `fast-fourier-transform-divide-and-conquer-idea`: Fast Fourier transform divide-and-conquer idea
- `binomial-coefficients-and-counting`: Binomial coefficients and counting
- `recurrences-and-recursion-analysis`: Recurrences and recursion analysis
- `little-o-theta-and-omega-asymptotics`: Little-o, Theta and Omega asymptotics
- `sorting-and-permutation-routing-on-tapes`: Sorting and permutation routing on tapes
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication
- `finite-state-machine-and-constant-size-alphabet`: Finite-state machine and constant-size alphabet

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
