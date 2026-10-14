# exegenius task 0003-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1B` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: asymptotic analysis (O, Theta, Omega), recursion and induction, discrete mathematics (sets, functions, permutations, graphs, modular arithmetic, primes and gcd, elementary combinatorics), and single-variable calculus. They have taken linear algebra at the level of vectors, matrices, bases, dimension and dot products, and have met complex numbers, polynomials, binary representation, Boolean gates and basic multitape Turing machines. They have not studied abstract algebra beyond residues and the two-element field, Fourier analysis, the FFT, fast integer multiplication, tensor products, or any research-level algorithms or complexity.

## Pages, in reading order

- `fixed-tape-model`: Fixed finite-tape machine model: The computation model: one fixed finite alphabet and a fixed number of one-dimensional tapes, each step touching one cell per tape, so extra tracks or work tapes change time only by a constant factor.
- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's proposal that n log n is the optimal order of growth for multiplying n-bit integers on multitape Turing machines.
- `nlogn-multiplier`: Established O(n log n) multiplier (Harvey–van der Hoeven): The known fixed-tape integer multiplier running in O(N log N) time on N-bit inputs, used here only as an ordinary subroutine on short records.
- `array-order`: Arrays in lexicographic tape order with address fields: A multidimensional array is stored on a tape in lexicographic order of its address (first coordinate most significant), so address fields are contiguous ranges of positions and an address is implicit in position.
- `stream-ops`: Elementary stream operations: Linear-time tape scans that permute digit values, move a digit, split an array by a digit, apply a pointwise map and merge, or split whole rows cyclically into a fixed number of equal streams.
- `controlled-shifts`: Controlled cyclic shifts and rational scalings: In linear time, update a target address field by adding an offset computed from earlier control fields modulo q^b (a cyclic shift of blocks), or multiply it by a fixed rational unit.
- `matrix-basics`: Matrix rank, subspaces and orthogonal complements: Rank of a matrix, subspaces of a vector space with a bilinear form, and the orthogonal complement of one subspace inside a larger one, whose dimension equals the change in dimension.
- `network`: Linear exchange network with restored scratch wires: A fixed network of linear gates on wires (roles) that swaps two banks of values with prescribed signs and returns every auxiliary scratch wire to its arbitrary initial value, using a copy/gather/scatter/side-injection schedule.
- `frames`: Frames and the common-frame identity: Giving each array on a wire an invertible address-space operator (a frame) at every vertex; because a common frame commutes with a pointwise linear gate, the network's overall effect is the endpoint frames applied to each role, and each edge only changes the frame.
- `subset-labels`: Three-element-subset subspace labels: Subspaces of a tensor-cube bilinear space attached to gates, built from indicator vectors of three-element subsets with intersection-size pairings (Frankl–Wilson, Alon), so labels are nested along edges and neighbors are orthogonal.
- `rank-saving`: Rank deficit s < Wm: Summing the dimension changes (edge ranks) of all labels gives a total s of smaller calls strictly below W·m, where W is the number of wires and m the dimension, which is the source of the power saving.
- `bit-network`: Bit exchange network with shear interface: The F₂ network with rational labels whose frames are address shears: its endpoint operator is (H,D)→(H+D,D) on every role, using only XOR gates, with rank sum s_b < W_b m.
- `lower-triangular`: Lower-triangular factorization of matrices: Every rational matrix A of rank a factors as E₁ΠE₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with a ones (a reversed-order Bruhat factorization).
- `matrix-shear`: Rational matrix shear as field interchanges: The map (H,D)→(H+AD,D) over Z/q^b for a rank-a rational matrix A is performed by triangular controlled shifts and exactly a interchanges of b-digit fields.
- `power-saving-recurrence`: Power-saving recurrence: Calling s smaller operations of parameter f/m on streams of volume V/W gives normalized cost F_k ≤ (s/W)F_{k−1}+O(1); since s/W < m^τ this solves to O(e^τ), a strict power saving.
- `power-interchange`: Power-width address interchange with rows: Interchanges two chunks of m^k digits using the bit network: split rows among the W roles, apply a matrix shear on each edge via recursive smaller interchanges, merge, then compose three shears into a swap.
- `chunk-interchange`: Fast interchange of address chunks: Exchanges two disjoint address chunks of u bits in an array (any prefix, gap and suffix) in O(V u^τ) tape steps for a fixed τ < 1, by padding rows and splitting the width in base m; the final effect is an exact permutation although intermediate steps form XOR combinations.
- `packed-bit-addition`: Packed selected-bit addition with deterministic repair: Performs y←y⊕x on the same bit position of f chunks at once using eight cyclic shifts of whole chunk ranges (a three-chunk rotation trick that restores a scratch chunk), then corrects the small explicitly identified set of addresses where guard values fail.
- `polynomial-ring-mod`: Polynomial ring modulo y^r + 1: Complex polynomials of degree below r with y^r = −1, so multiplication by a power of y is a signed cyclic shift of the coefficient list (negacyclic wraparound).
- `kronecker-packing`: Signed packing (Kronecker substitution): Multiplies two ring polynomials by evaluating them at B₀=2^{4p} as signed integers, multiplying with the O(N log N) integer multiplier, extracting centered coefficients and wrapping negacyclically.
- `cyclic-convolution`: Cyclic convolution: Multiplication of polynomials (or arrays) modulo x^S − 1, where indices wrap around modulo the length on every axis.
- `int-as-convolution`: Integer multiplication as digit convolution: Writing each input in radix 2^b digits makes the product's digit sequence a convolution of the two coefficient lists; with enough zero padding, cyclic convolution equals ordinary polynomial multiplication, and carrying recovers the integer.
- `dft`: Discrete Fourier transform: The normalized map sending a length-q vector u to (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q}; its inverse-direction version uses the opposite sign, and both are contractions.
- `butterfly-fft`: Two-point butterfly and radix-2 FFT order: The butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) applied recursively by decimation in frequency, with twiddle multiplications, computes a transform of power-of-two length and leaves outputs in bit-reversed slot order.
- `phase-network`: Complex phase network: The Z[i,1/2] network with binary labels whose frames are phase operators C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m}; each edge is a product of two-point kernels aI+bX_v and the endpoint operator is C^{⊗m} on every role, with s_c < W_c m.
- `fixed-point-disk-grid`: Fixed-point disk grid and error propagation: Complex values stored as pairs of signed fixed-point integers with p fractional bits in the unit disk; algorithms approximate linear contractions, truncation toward zero adds bounded error, and errors add under composition.
- `negacyclic-twist`: Coefficient twist to negacyclic ring: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} maps cyclic convolution on the last axis to convolution in the ring of polynomials modulo y^r+1, whose negative wrap exactly cancels the twist.
- `simultaneous-layer`: Simultaneous butterfly layer: Applies the two-point butterfly H₀ at one bit position in each of D address chunks at once in O(V d^{λ'}) time, by recursing on the complex phase network with packed basis changes, exact Gaussian-dyadic arithmetic and one final truncation.
- `convolution-theorem`: Convolution theorem for normalized transforms: The transform of a cyclic convolution equals the pointwise product of transforms (with a normalizing factor), so convolution can be computed by transform, pointwise product and inverse transform.
- `multidim-transform`: Multidimensional (tensor) transforms: A transform on a product of axes of lengths t_1,…,t_D, equal to the tensor product of the one-dimensional transforms applied along each axis in turn.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier-type transform of arrays of ring polynomials in which the roots of unity are powers y^{2r/t}, so twiddle multiplications are exact signed shifts of coefficient lists and only butterflies cost arithmetic.
- `gaussian-resampling`: Gaussian resampling with retained permutations: Harvey–van der Hoeven's identity expressing a Fourier transform of coprime length s through one of power-of-two length t via Gaussian-weighted maps A and B₀, here keeping the two coordinate permutations inside the formula instead of sorting.
- `chirp-identity`: Bluestein chirp identity: Rewrites a Fourier transform (with its frequency permutation) as pointwise multiplication by a quadratic phase, a cyclic convolution with the chirp array, and another pointwise phase multiplication.
- `permutation-cancellation`: Source-permutation cancellation: The coordinate permutation retained by resampling cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S² so no sort is executed.
- `transform-layout`: Synthetic transform layout and stored frequency order: Places selected bits of all participating axes at a common offset in consecutive chunks so each radix-two round is one simultaneous layer, and keeps the bit-reversed frequency order through the pointwise product to the opposite transform.
- `ring-convolution`: Convolution over the polynomial ring from the retained layout: Computes normalized convolution of arrays of ring polynomials by two forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform consuming the same stored order.
- `crt-axis-map`: Chinese-remainder address map: A ring isomorphism from cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to d-dimensional cyclic convolution on prime axes, implemented on tape by triangular prefix-controlled cyclic shifts.
- `prime-lengths`: Choice of prime source lengths: Chooses distinct odd primes s_i just below the powers of two t_i (with t_i/s_i separated from 1) via a prime-interval lower bound, found by deterministic search, so S is a constant fraction of the padded box T.
- `complex-convolution`: Complex cyclic convolution by coefficient twist: Normalized cyclic convolution f*g/T of complex arrays on power-of-two axes, obtained by twisting the last axis into the polynomial ring and using the ring convolution.
- `source-transform`: Source transform procedure: Computes the transform of coprime length by applying the Gaussian map A line by line, the chirp transform through complex convolution, the map B₀, and an exact power-of-two scale, with the retained permutation R.
- `exact-recovery`: Rounding and carry propagation to the exact product: Shows the recovered coefficient error is below 1/2, rounds to the integer convolution coefficients, and propagates radix-2^b carries to output exactly 2n product bits.
- `mult-algorithm`: The multiplication algorithm: Splits both inputs into digits, applies the coefficient-address map, computes the source transform of each, multiplies pointwise, applies the opposite-sign transform with scalings, rounds and propagates carries.
- `parameter-balance`: Parameter choice and cost balance: Fixes p = Θ(log n), d = ⌊b^ε⌋ axes, chunk size K, ring dimension r = 2^{Θ(p/d)} and the tiny exponents so that every row of the cost table has normalized power of p at most 1 − 2κ, giving total O(n (log n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `tape-machines`: Turing machines and tapes
- `asymptotic-notation-beyond-big-o`: Asymptotic notation beyond big-O
- `logarithms-and-exponentials`: Logarithms and exponentials
- `floor-ceiling-and-rounding`: Floor, ceiling and rounding
- `proof-by-induction-and-recursion`: Proof by induction and recursion
- `sets-subsets-and-basic-combinatorics`: Sets, subsets and basic combinatorics
- `functions-bijections-and-permutations`: Functions, bijections and permutations
- `graphs`: Graphs
- `modular-arithmetic`: Modular arithmetic
- `primes-coprimality-and-gcd`: Primes, coprimality and gcd
- `binary-field-f2-and-xor`: Binary field F2 and XOR
- `positional-number-representation-and-carries`: Positional number representation and carries
- `dyadic-rationals-and-binary-fractions`: Dyadic rationals and binary fractions
- `exponential-function-and-gaussian-function`: Exponential function and Gaussian function
- `vectors-matrices-and-linear-maps`: Vectors, matrices and linear maps
- `vector-norms-and-error-bounds`: Vector norms and error bounds
- `boolean-gates-and-circuits`: Boolean gates and circuits
- `determinism-and-exact-versus-approximate-computation`: Determinism and exact versus approximate computation

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
