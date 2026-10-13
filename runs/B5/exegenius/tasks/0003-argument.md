# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/B5` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)): A deterministic fixed-tape machine multiplies n-bit integers by digit convolution, CRT axes, resampling, chirps, twisting, synthetic convolution and rounding, disproving the n log n conjecture.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: An undergraduate computer science reader who has studied algorithm analysis (big-O, recurrences, sorting, divide and conquer including Karatsuba-style multiplication), discrete mathematics (modular arithmetic, gcd and coprimality, the Chinese remainder theorem in its basic form, permutations, binary representation), and calculus and linear algebra through matrices, Gaussian elimination and basic vector spaces. They know complex numbers and polynomials, and have seen simple Turing machines with tapes. They have not met the fast Fourier transform in depth beyond its name, finite-field or group-theoretic structure beyond Z/n, Kronecker products, or any research-level multiplication algorithms.

## Pages, in reading order

- `nlogn-conjecture`: The n log n conjecture and its history: Schönhage and Strassen conjectured n log n is the optimal multiplication cost on multitape Turing machines; Harvey and van der Hoeven reached O(n log n), which also serves here as an ordinary subroutine multiplier.
- `convolution`: Cyclic convolution: The product of two coefficient lists as polynomials modulo x^S−1, so entries sum over index pairs adding to a fixed value modulo S; also done on products of several cyclic axes.
- `radix-digit-mult`: Integer product as digit convolution: Splitting each integer into radix-2^b digits turns multiplication into a convolution of short coefficients; carries are propagated afterwards.
- `array-layout`: Arrays on tape, address fields and volume: An array indexed by a product of ranges is stored in lexicographic order on a tape, so address fields, chunks, rows and the bit volume V are positions in the tape stream.
- `stream-ops`: Elementary stream operations: Splitting an array into streams by a digit or by cyclic rows, applying a pointwise map, and merging, all in O(V) tape steps.
- `controlled-shifts`: Controlled shifts and rational scalings: A target field can be cyclically shifted or multiplied by a unit modulo q^b by an offset computed from earlier fields in linear time.
- `linear-algebra`: Rank, subspaces and orthogonal complements: Matrix rank, subspaces, a bilinear form, orthogonal complement and projection, over the rationals and over the two-element field F2.
- `scalar-network`: Bank-exchanging linear network with restored scratch: A fixed network of linear gates on scalar wires that swaps two banks X,Y (X→−Y, Y→X) using scratch wires with arbitrary initial values that are restored.
- `frames`: Frames and the common-frame invariant: Assigning an invertible operator on a wire's array at each gate lets pointwise gates commute with it, so intermediate frames cancel and only endpoint operators remain.
- `labels`: Subspace labels from triple indicator vectors: Nested nondegenerate subspaces built from three-element subsets of a fixed set, attached to gates so each edge's frame change costs its residual dimension.
- `rank-deficit`: Rank deficit and the recursive power saving: The edge residual dimensions sum to s<Wm, so a recursive call on m times more parameter uses s calls on 1/W of the volume, giving cost exponent below 1.
- `bit-interface`: Bit network and rational shear interface: The XOR network with rational matrices at gates whose endpoint difference is the identity, yielding the same shear H←H+D on every role.
- `bruhat`: Lower triangular factorization: Any rational matrix of rank a equals E1·Π·E2 with E1,E2 invertible lower triangular and Π a partial permutation with a ones.
- `matrix-shear`: Cost of a rational matrix shear: The map (H,D)→(H+AD,D) over Z/q^b needs exactly rank(A) interchanges of b-digit fields plus O(V) work.
- `power-interchange`: Power-width chunk interchange: Recursively interchanging two address chunks of m^k digits by running the bit network on W role streams, with cost recurrence F_k ≤ (s/W)F_{k−1}+O(1).
- `chunk-swap`: Fast interchange of address chunks: Swapping two disjoint address chunks of u bits in O(V u^τ) tape time for a fixed τ<1, by padding to power widths and base-m pieces.
- `packed-addition`: Packed selected-bit addition: XORing corresponding selected bits of two address chunks at once, using a third chunk as restored scratch, with exceptional addresses repaired by sorting.
- `synthetic-ring`: Polynomial ring modulo y^r+1: Complex polynomials of degree below r with y^r=−1, where multiplying by a power of y is a signed shift of coefficients and serves as a root of unity.
- `signed-packing`: Signed packing for ring products: Kronecker substitution evaluating polynomial coefficients at a power of two to multiply ring elements with an ordinary O(N log N) integer multiplier.
- `dft`: Discrete Fourier transform: The normalized transform F_q taking u to averages of u_j times roots of unity, which turns convolution into pointwise product.
- `butterfly`: Two-point butterfly: The basic fast-transform step replacing a pair (u,v) by their sum and difference, here H0(u,v)=((u+v)/2,(u−v)/2).
- `phase-interface`: Phase frames and the kernel C=aI+bX: The Gaussian-dyadic network whose frame changes are products of translation kernels aI+bX_v, ending in C⊗m on every role.
- `butterfly-layer`: Simultaneous butterfly layer: Applying H0 to the same bit of up to d address chunks at once, using the phase network and packed bit additions, at cost O(V d^λ′) with one final truncation.
- `synthetic-transform`: Synthetic polynomial transform: The transform F_t with root ω_t=y^{2r/t} in the ring modulo y^r+1, a contraction whose root multiplications are signed shifts.
- `transform-layout`: Transform layout and cost: Placing selected bits of all axes at a common offset in consecutive chunks so butterfly layers apply round by round, and bounding the whole synthetic transform.
- `synthetic-convolution`: Convolution from retained transform layout: Convolution over the ring: two forward synthetic transforms, pointwise ring products, and the opposite transform, keeping the same frequency order throughout.
- `crt-map`: Chinese-remainder address map: An isomorphism of cyclic convolution on S=∏s_i points onto a product of pairwise coprime cyclic axes, implemented by triangular controlled shifts.
- `coefficient-twist`: Coefficient phase twist: Mapping x_d to ζy, ζ=e^{πi/r}, turns cyclic wrap of the last axis into the negative wrap of the ring modulo y^r+1.
- `fixed-point-errors`: Fixed-point error control: Complex values on a grid of spacing 2^{-p} in the unit disk, linear contractions that do not enlarge error, truncation, and additive error bookkeeping.
- `resampling`: Gaussian resampling: Gaussian-weighted contractions A and B0 that relate a Fourier transform of length s to one of length t slightly larger, with the two coordinate permutations kept inside the identity.
- `tensor-resampling`: Multidimensional resampling: The tensor product of the one-dimensional resampling identities over d axes, applied one line at a time, with axis movement done by chunk interchange.
- `chirp`: Bluestein chirp and permutation cancellation: A chirp identity turns the permuted middle transform into a cyclic convolution with pointwise phases, and the source permutation cancels between forward transforms and the opposite one.
- `parameters-cost`: Parameter choices and cost table: Choice p=6b, d≈b^ε, K≈d^c and the rational exponents, with a cost table whose every normalized term is at most p^{1−2κ}.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)): A deterministic fixed-tape machine multiplies n-bit integers by digit convolution, CRT axes, resampling, chirps, twisting, synthetic convolution and rounding, disproving the n log n conjecture.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-tm`: Multitape Turing machine
- `logarithms-and-exponentials`: Logarithms and exponentials
- `floor-and-ceiling`: Floor and ceiling
- `modular-arithmetic`: Modular arithmetic
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality
- `prime-numbers`: Prime numbers
- `chinese-remainder-theorem`: Chinese remainder theorem
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `positional-radix-representation`: Positional radix representation
- `permutations`: Permutations
- `matrices-and-matrix-products`: Matrices and matrix products
- `vector-spaces-and-linear-maps`: Vector spaces and linear maps
- `finite-field-f2`: Finite field F2
- `euler-s-formula-and-complex-exponentials`: Euler's formula and complex exponentials
- `geometric-series`: Geometric series
- `gaussian-function`: Gaussian function
- `basic-calculus-and-inequalities`: Basic calculus and inequalities
- `fixed-point-and-rounding-arithmetic`: Fixed-point and rounding arithmetic
- `cartesian-product-and-tuples`: Cartesian product and tuples
- `cyclic-groups-and-direct-products`: Cyclic groups and direct products
- `sorting`: Sorting
- `divide-and-conquer-recurrences`: Divide and conquer recurrences
- `karatsuba-and-schoolbook-multiplication`: Karatsuba and schoolbook multiplication
- `fast-fourier-transform-idea`: Fast Fourier transform idea
- `sums-and-indexed-notation`: Sums and indexed notation

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
