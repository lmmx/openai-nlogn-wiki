# exegenius task 0003-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3B` (paths below are relative to it)

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

`main-theorem`: Sub-n-log-n integer multiplication: A single deterministic multitape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate in computer science who has taken discrete mathematics, data structures and algorithms, introductory theory of computation, and the linear algebra and calculus that accompany such a degree. They are fluent with asymptotic analysis, recurrences, binary representation and bitwise operations, modular arithmetic, matrices and rank, vector spaces over the reals, and complex numbers including roots of unity; they know the schoolbook and Karatsuba multiplication algorithms and what a Turing machine with tapes is. They have not studied abstract algebra beyond basics, the FFT's algebraic variants, number-theoretic transforms, finite fields beyond arithmetic mod 2, analytic number theory, numerical analysis of rounding error, or any bit-complexity multiplication algorithm.

## Pages, in reading order

- `schonhage-strassen-conjecture`: Schönhage–Strassen optimality conjecture: The 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine; the best earlier bound was the unconditional O(n log n) of Harvey and van der Hoeven.
- `hh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The established fixed-tape algorithm multiplying N-bit integers in O(N log N) time, used here as an ordinary subroutine for short integer products.
- `tape-stream-operations`: Arrays and elementary stream operations on tape: Arrays stored in lexicographic address order, with linear-time scans that split on a digit, apply a pointwise map and merge, or distribute whole rows among streams.
- `controlled-shift`: Controlled shifts and rational scalings: Adding to a later address field an offset computed from earlier control fields, or multiplying it by a rational unit, in linear time by splitting and re-merging blocks.
- `exchange-network`: Bank-exchange network with restored scratch wires: A fixed network of linear gates on wires, built from three-element subsets, that swaps two banks X and Y with a sign and returns every auxiliary scratch wire to its arbitrary initial value.
- `frames`: Frames on network wires: Choosing an invertible operator D_v on the array carried by a wire at each gate, so a pointwise linear gate commutes with it and the intermediate frames cancel, leaving only the endpoint operator on every role.
- `subspace-labels`: Nested subspace labels and orthogonal residuals: Subspaces of a fixed m-dimensional bilinear space attached to gates and terminals, nested along edges; an edge's orthogonal residual has dimension equal to the number of smaller operations the edge needs.
- `rank-saving`: Strict rank saving: The total rank s of all edge changes in the fixed network is strictly less than W·m (wires times label dimension), which makes each recursive level cost a factor s/W < m.
- `matrix-factorization`: Lower-triangular factorization of a matrix: Every rational m×m matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
- `matrix-shear`: Cost of a matrix shear on address fields: The map (H,D) ↦ (H+AD,D) over Z/q^b for a rational matrix A of rank a is done with exactly a interchanges of b-digit fields plus linear extra work.
- `power-width-interchange`: Power-width chunk interchange: Interchanging two address chunks of m^k digits by running the bit network on W cyclic role streams, with one smaller interchange per unit of edge rank, giving the recurrence F_k ≤ (s/W)F_{k−1} + O(1) and cost O(V e^τ).
- `chunk-interchange`: Address chunk interchange: Swapping two disjoint equal-width bit chunks of an address array in O(V u^τ) steps for a fixed τ < 1, by XOR combinations whose final effect is an exact permutation.
- `packed-selected-bit-addition`: Packed selected-bit addition: XORing corresponding selected bits of two address chunks by constantly many cyclic shifts of whole chunk ranges plus a deterministic repair of an explicitly small set of exceptional addresses, using a third chunk as restored scratch.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: The complex polynomials of degree below r with y^r = −1; multiplying by a power of y just shifts the coefficient list and flips some signs.
- `kronecker-packing`: Signed Kronecker packing: Packing the coefficients of two polynomials into big signed integers (evaluation at 2^{4p}), multiplying with the fast integer multiplier and unpacking the coefficients.
- `contraction-error`: Contractions and error accumulation: A linear map that does not increase the sup norm is a contraction; approximating contractions on a fixed-point grid of 2^{−p} spacing adds errors without amplifying them.
- `guard-bits`: Exact dyadic intermediates with one truncation: Intermediate values in a butterfly layer are exact Gaussian dyadics held with enough guard bits, and a single truncation to the 2^{−p} grid follows the whole contractive layer.
- `cyclic-convolution`: Cyclic convolution: For arrays indexed by a product of cyclic groups, the product whose entry at address j is the sum of u_k v_{j−k} with all indices taken modulo the axis lengths.
- `radix-digit-convolution`: Integer product as digit convolution: Splitting two integers into radix-2^b digits turns their product into a convolution of the digit sequences followed by carry propagation.
- `phase-twist`: Coefficient phase twist: Substituting x_d ↦ ζy with ζ = e^{πi/r} multiplies coefficient k by ζ^k and turns cyclic convolution of length r into negacyclic polynomial multiplication, exactly undone by untwisting.
- `exact-recovery`: Exact recovery by rounding and carries: Removing the known normalizations S and 2^{2b+4}, showing the recovered coefficient error is below 1/2, rounding to integers, and propagating radix carries to output the exact 2n-bit product.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q} (and its opposite-sign version) that turns cyclic convolution into pointwise multiplication.
- `fft-butterfly`: Two-point butterfly and radix-two recursion: The operation H₀(u,v) = ((u+v)/2, (u−v)/2) on a pair of entries, and the decimation-in-frequency recursion that builds a length-2^a transform from a, such layers interleaved with twiddle multiplications.
- `chirp-identity`: Bluestein chirp identity: A Fourier transform of even length t can be written as pointwise multiplication by a chirp phase a, a cyclic convolution with a, and another chirp multiplication.
- `phase-frames`: Phase frames and the two-point kernel C: The complex network uses frames diagonalized by Hadamard matrices with phases i^{wt}; an edge change becomes a product of kernels C = H S H = aI + bX, which are translations of the array, and H₀ = b S C S.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀ to one selected bit in each of D address chunks at once, on arrays of ring records, in O(V d^{λ′}) with λ′ < 1 instead of D whole-array passes, via the recursive complex network on packed bit changes.
- `multidimensional-transform`: Multidimensional transform: The tensor product of one-dimensional transforms applied along each axis of an array whose axis lengths are t_1,…,t_D; convolution on the product of cyclic groups becomes pointwise multiplication.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the negacyclic ring using ω_t = y^{2r/t} as root of unity, so each twiddle multiplication is a signed shift and only butterflies cost arithmetic.
- `bit-reversed-order`: Stored bit-reversed frequency order: The recursion writes outputs in bit-reversed order (record permutation B_t), and the opposite transform consumes that same order, so no reordering is needed between the forward transforms and the inverse.
- `transform-layout`: Transform layout and cost: Placing the selected bits of all participating axes at a common offset in K-bit chunks, so each round of the synthetic transform uses the simultaneous layer, at total normalized cost dK + pK^{τ−1} + ℓd^{λ′}.
- `ring-convolution`: Convolution over the polynomial ring: Normalized convolution of arrays with entries in the negacyclic ring: forward synthetic transforms, pointwise polynomial products by Kronecker packing, and the opposite transform in the retained order.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's identity expressing a Fourier transform of prime-product length s as a transform of power-of-two length t, between two cheap Gaussian-weighted linear contractions A and B₀.
- `permutation-cancellation`: Retained permutations cancel in a convolution: The coordinate permutations left inside the resampled transform cancel across two forward transforms, a pointwise product and an opposite-sign transform, so no full sort is executed.
- `crt-axis-map`: Chinese-remainder map to prime axes: An algebra isomorphism from cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to convolution on the product of cyclic axes of lengths s_i, implemented by triangular controlled shifts.
- `prime-axis-lengths`: Prime axis lengths near powers of two: Choosing distinct odd primes s_i slightly below the powers of two t_i so their product fills a fixed fraction of the padded box and each ratio t_i/s_i leaves room for resampling.
- `parameter-choice`: Parameter choice for the multiplier: Fixed rational exponents (τ, σ, λ′, c, ε, δ, κ) and sizes b = ⌈log₂n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, T ≈ n/b, r = 2^ℓ, with prime axis lengths s_i < t_i.
- `multiplication-algorithm`: The multiplication algorithm: Digits are placed on prime axes by the CRT map, transformed by resampling plus chirp convolution over the polynomial ring for both operands, multiplied pointwise, transformed with opposite sign, rescaled, rounded and carried.
- `time-bound`: Complete time bound: Dividing costs by the volume Tp, seven dominant terms with powers of p below one (margins g₁,…,g₇) show total time O(n (lg n)^{1−κ}); the smallest margin is 2κ.
- `main-theorem`: Sub-n-log-n integer multiplication: A single deterministic multitape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o-notation`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-turing-machine`: Multitape Turing machine
- `asymptotic-notation-beyond-big-o`: Asymptotic notation beyond big-O
- `limits-and-limit-inferior`: Limits and limit inferior
- `logarithms-exponentials-floors-and-ceilings`: Logarithms, exponentials, floors and ceilings
- `recurrences-and-geometric-sums`: Recurrences and geometric sums
- `positional-number-systems-and-carries`: Positional number systems and carries
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication
- `bitwise-operations-and-xor`: Bitwise operations and XOR
- `modular-arithmetic`: Modular arithmetic
- `primes-coprimality-and-the-extended-euclidean-algorithm`: Primes, coprimality and the extended Euclidean algorithm
- `roots-of-unity`: Roots of unity
- `matrices-and-linear-maps`: Matrices and linear maps
- `vector-spaces-subspaces-dimension-and-rank`: Vector spaces, subspaces, dimension and rank
- `inner-products-bilinear-forms-and-orthogonal-complements`: Inner products, bilinear forms and orthogonal complements
- `gaussian-elimination-and-triangular-matrices`: Gaussian elimination and triangular matrices
- `permutations-bijections-and-permutation-matrices`: Permutations, bijections and permutation matrices
- `arithmetic-modulo-2-and-linear-algebra-over-f-2`: Arithmetic modulo 2 and linear algebra over F_2
- `finite-sets-subsets-and-counting`: Finite sets, subsets and counting
- `circuits-and-directed-acyclic-graphs`: Circuits and directed acyclic graphs
- `vector-norms-and-the-triangle-inequality`: Vector norms and the triangle inequality
- `fixed-point-numbers-dyadic-rationals-and-rounding`: Fixed-point numbers, dyadic rationals and rounding
- `row-major-order-and-matrix-transposition`: Row-major order and matrix transposition
- `subroutines-and-reductions-between-problems`: Subroutines and reductions between problems
- `convolution-of-sequences`: Convolution of sequences

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
