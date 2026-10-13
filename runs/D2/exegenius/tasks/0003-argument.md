# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/D2` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^{1−κ}): A deterministic multitape Turing machine multiplies n-bit integers in O(n (lg n)^{1−κ}) with κ=2^{-182}, disproving the n log n optimality conjecture in that model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has finished an undergraduate computer science degree: asymptotic analysis, basic algorithms (divide and conquer, sorting, recurrences, schoolbook integer arithmetic), discrete mathematics, and introductory linear algebra, abstract algebra (groups, rings, fields, modular arithmetic) and probability. They know Turing machines and tapes at a basic level, but not the multitape fixed-alphabet cost model in detail, nor Fourier-analytic multiplication, FFT variants, or specialist algebra such as bilinear forms over F_2 and matrix factorizations like Bruhat.

## Pages, in reading order

- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen's 1971 multiplication bound O(n log n log log n) and their conjecture that n log n is optimal; later work (Fürer, Harvey–van der Hoeven) reached O(n log n) unconditionally.
- `harvey-hoeven-multiplier`: Established O(n log n) multiplier as a subroutine: The Harvey–van der Hoeven multitape integer multiplier with cost O(N log N), called as an ordinary subroutine on short inputs.
- `fixed-tape-model`: Fixed-tape machine model and cost of scans: One fixed finite alphabet and a fixed finite number of one-dimensional tapes; one step touches one cell per tape, so rearranging growing fields costs real time.
- `elementary-streams`: Elementary stream operations and controlled shifts: Linear-time tape scans: swapping or moving a digit, splitting into streams and merging, and updating a field by an offset computed from earlier fields.
- `linear-network`: Linear network with roles, frames and restored scratch: A fixed network of linear gates on wires (roles) exchanging two banks with signs, restoring every scratch value for arbitrary initial contents; applied to arrays, each wire gets an invertible frame whose change on an edge is what must be implemented.
- `transparent-restoration`: Restoring scratch values (transparent computation): The schedule subtracts old scratch contributions, performs the operation, and undoes it so arbitrary initial auxiliary values cancel.
- `triple-subspace-labels`: Three-element subsets and nested subspace labels: Indicator vectors of 3-subsets of [h] have intersection-count inner products; orthogonality gives nested nondegenerate subspaces whose dimension drops (orthogonal residuals) count the smaller operations on an edge.
- `rank-saving`: Total smaller calls below W m: In the finite network the edges need s<Wm smaller calls in total, so a recursive call at parameter m·f uses s calls at parameter f on volume V/W, whose per-volume cost grows by s/W<m, giving a power saving.
- `bruhat-shear`: Lower-triangular factorization and address shear: Every rational matrix factors as E1 Π E2 with lower triangular E1,E2 and a partial permutation of rank-many ones; so an edge matrix of rank a costs a smaller interchanges, and the shear (H,D)→(H+D,D) is done in tape order.
- `chunk-interchange`: Fast interchange of address chunks: Interchanging two equal-width address fields of u digits in an array of volume V in O(V u^τ), τ<1, via XOR-style combinations whose final effect is an exact permutation.
- `packed-bit-addition`: Packed selected-bit addition: Adding the selected bit across address chunks of many axes at once on packed records, with a small exceptional set of addresses repaired by sorting.
- `ring-y-r-plus-1`: Polynomial ring modulo y^r + 1: Polynomials with complex coefficients of degree < r where y^r = −1 (negacyclic); multiplying by a power of y is a signed shift of the coefficient list.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{-2πi jk/q}; a contraction in the max norm.
- `butterfly`: Two-point butterfly H₀: The map H0(u,v)=((u+v)/2,(u−v)/2), the basic step of radix-2 fast transforms; a transform has about log n levels of butterfly layers.
- `phase-frames`: Phase kernel C and complex network: The kernel C=H S H=aI+bX with C²=X and H₀=b S C S lets the complex network's frame changes be products of translation kernels on binary subspaces, over Gaussian dyadic numbers.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the ring R_r using ω_t = y^{2r/t} as root of unity, so twiddle multiplications are signed shifts; its inverse pairs are exact up to a factor.
- `convolution`: Cyclic convolution: Convolution of arrays on a product of cyclic groups; the transform turns it into a pointwise product, so convolutions are computed by transform, multiply, inverse transform.
- `radix-digit-convolution`: Multiplication as convolution of radix digits: Splitting each integer into radix-2^b digits turns the product into a convolution of short digit sequences, recovered into an integer by rounding and carry propagation.
- `crt-prime-axes`: Chinese-remainder address map to prime cyclic axes: A convolution-preserving map Φ places the radix-digit list on a product of distinct prime cyclic axes, implemented by triangular controlled shifts and axis moves.
- `bluestein-chirp`: Chirp identity and permutation cancellation: Bluestein's identity rewrites the permuted transform Q F_t as a chirp multiplication, a cyclic convolution, and another chirp; the retained source permutation R cancels across two forward and one inverse transform.
- `coefficient-twist`: Coefficient twist to the negacyclic ring: Scaling coefficient k by ζ^k with ζ=e^{πi/r} maps cyclic convolution in the last coordinate to polynomial multiplication modulo y^r+1, with the negative wrap undoing to the cyclic wrap.
- `fixed-point-contraction`: Fixed-point grids, contractions and error: Values are complex numbers in the unit disk on a grid 2^-p Z[i]; maps that never grow the max norm (contractions) let truncation errors add rather than blow up.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applies H₀ to the same bit position in d address chunks of complex fixed-point polynomial records in one pass, costing O(V d^λ') instead of d whole-array passes, with exact Gaussian dyadic intermediates and a single final truncation.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven identity expressing a Fourier transform of coprime (prime) length s through one of power-of-two length t via contractions A and B0, at cost O(t p^{3/2+δ} α) per line.
- `exact-recovery`: Precision, rounding and carries: Rescaling by the known normalizations, showing the coefficient error is below 1/2, rounding to integers, and propagating radix carries yield the exact 2n-bit product.
- `signed-packing`: Signed packing of polynomial records: A signed Kronecker substitution packs a polynomial's coefficients into one big integer, multiplied by the O(N log N) multiplier and unpacked, giving ring multiplication in O(rp log(rp)).
- `synthetic-convolution`: Convolution from the retained transform layout: Convolution over R_r on a multi-axis array: two forward synthetic transforms keep the same frequency order, multiply pointwise by signed packing, and the opposite transform consumes that order, using layers on a layout built from chunk swaps.
- `retained-permutations`: Resampling with the permutations left in the transform: Instead of sorting twice per coordinate, the source and target coordinate permutations stay inside the transform identity and cancel, so no separate full sorts are executed.
- `parameter-choice`: Parameter choice and cost table: With b=⌈log₂n⌉, p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log₂T/d⌉}, every term of the normalized cost table is p^{1−margin}, so the total is O(Tp·p^{1−g}) = O(n (lg n)^{1−κ}).
- `multiplication-algorithm`: The multiplication algorithm pipeline: Digits, Φ to prime axes, two source transforms via Gaussian resampling and chirp convolution, pointwise product, opposite transform, scale, round, Φ⁻¹, carry.
- `main-theorem`: Integer multiplication in O(n (lg n)^{1−κ}): A deterministic multitape Turing machine multiplies n-bit integers in O(n (lg n)^{1−κ}) with κ=2^{-182}, disproving the n log n optimality conjecture in that model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-tm`: Turing machines and tapes
- `roots-of-unity`: Roots of unity
- `matrices-and-linear-maps`: Matrices and linear maps
- `modular-arithmetic`: Modular arithmetic
- `chinese-remainder-theorem`: Chinese remainder theorem
- `prime-numbers-and-coprimality`: Prime numbers and coprimality
- `groups-rings-and-fields`: Groups, rings and fields
- `binary-representation-and-bit-operations`: Binary representation and bit operations
- `schoolbook-and-divide-and-conquer-multiplication`: Schoolbook and divide-and-conquer multiplication
- `fast-fourier-transform`: Fast Fourier transform
- `floor-ceiling-logarithms-and-exponents`: Floor, ceiling, logarithms and exponents
- `recurrences-and-amortized-cost-accounting`: Recurrences and amortized cost accounting
- `sorting-and-permutations`: Sorting and permutations
- `norms-and-inequalities`: Norms and inequalities
- `rounding-and-floating-or-fixed-point-error`: Rounding and floating or fixed point error
- `gaussian-integers-and-dyadic-rationals`: Gaussian integers and dyadic rationals
- `multidimensional-arrays-and-product-index-sets`: Multidimensional arrays and product index sets
- `sums-and-product-notation-euler-s-formula`: Sums and product notation, Euler's formula
- `graphs-and-networks`: Graphs and networks
- `subsets-and-counting`: Subsets and counting
- `basic-probability-and-combinatorial-bounds`: Basic probability and combinatorial bounds

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
