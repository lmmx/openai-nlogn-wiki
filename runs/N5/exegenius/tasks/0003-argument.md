# exegenius task 0003-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N5` (paths below are relative to it)

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

`main-theorem`: Integer multiplication below n log n: A single deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2⁻¹⁸², disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, permutations, modular arithmetic, gcd and the Chinese remainder theorem, induction, binomial coefficients), the algorithms course (asymptotic notation, recurrences, Karatsuba, the FFT and FFT-based polynomial multiplication, bit-reversal, binary counters, stacks), introductory computability (Turing machines with multiple tapes and constant-factor simulations), and the supporting mathematics of a CS degree: calculus with limits, exponentials and Newton's method, complex numbers, and a first linear algebra course (matrices, rank, invertibility, subspaces, dimension, dot products and orthogonality over the reals, Gaussian elimination). They have not studied bilinear forms over general fields, tensor products of operators, Bruhat factorizations, algebraic complexity of integer multiplication beyond Karatsuba and the basic FFT, or research-level fast multiplication (Schönhage–Strassen, Fürer, Harvey–van der Hoeven, Nussbaumer transforms, Gaussian resampling), nor index coding or the Frankl–Wilson construction.

## Pages, in reading order

- `nlogn-conjecture`: n log n optimality conjecture: Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
- `harvey-hoeven-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The established fixed-tape integer multiplier running in O(n log n) time, used here only as an ordinary subroutine for short polynomial products.
- `polynomial-ring`: Polynomial ring modulo y^r + 1: The ring ℂ[y]/(y^r+1) with r a power of two, where multiplication by a power of y is a signed shift of the coefficient list, so powers of y serve as cheap roots of unity.
- `normalized-butterfly`: Normalized butterfly H₀: The two-point map H₀(u,v) = ((u+v)/2, (u−v)/2), the basic step of radix-two Fourier transforms, applied coefficientwise to polynomial records.
- `gaussian-dyadics`: Gaussian dyadic numbers: Complex numbers in ℤ[i,1/2], whose real and imaginary parts have power-of-two denominators; intermediate values of the numerical procedure are kept exactly in this form.
- `linear-network`: Linear network with wire roles: A fixed finite circuit of wires carrying scalars and gates applying fixed linear maps; a wire's fixed place is its role, and auxiliary scratch wires may start with arbitrary values.
- `frames`: Frames and the common-frame identity: Each source, gate and sink carries an invertible linear operator D_v on wire arrays; because a common frame commutes with a pointwise gate, the network applied to arrays implements D_out·S·D_in⁻¹, so only endpoint frames matter.
- `tape-array-layout`: Arrays on tape and logical volume: Arrays with address set [a₁]×…×[a_t] are stored in lexicographic order with implicit addresses; V, the logical volume, is the number of stored data bits, and rows are contiguous blocks at a fixed prefix and row index.
- `elementary-streams`: Elementary stream operations: Linear-time O(V) tape operations: permuting or moving a single radix digit, splitting and merging streams by a digit, and distributing rows cyclically among a fixed number of streams.
- `controlled-shifts`: Controlled shifts and rational scalings: Updating a target address field y ↦ y + a(controls) mod q^b, or multiplying it by a fixed rational unit, in O(V) time when the target field follows its control fields.
- `scratch-restoration`: Restoration of arbitrary scratch values: An eight-row schedule that subtracts the effect of old scratch values, adds the source's effect, then undoes the copies, so the net change y ← y + x is independent of the scratch contents, which are restored.
- `triple-intersection-construction`: Triple-intersection bank exchange: Two networks indexed by three-element subsets of [100], where gather/scatter through central wires produce coefficients depending on intersection size and side wires cancel the unwanted ones, giving y ← y + x; three stages then exchange banks (X,Y) ↦ (−Y,X).
- `subspace-labels`: Nested subspace labels and orthogonal residuals: Each gate and terminal is labelled by a nondegenerate subspace of a fixed m-dimensional bilinear space, nested along edges; the orthogonal residual of an edge measures how many smaller operations its frame change needs.
- `rank-deficit`: Rank deficit s < Wm: The decisive property of both networks: the total number s of smaller calls needed on all edges is strictly less than the wire count W times the label dimension m.
- `recursive-saving`: Recursive power saving: A call at parameter mf is done by s calls at parameter f on streams of volume V/W, so normalized cost grows by s/W < m^τ per level, giving cost O(V·f^τ) with τ < 1.
- `phase-frames`: Binary phase frames: For the complex network, frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m}; an edge's frame change is a product of one two-point kernel aI + bX_v per orthonormal residual vector, and telescoping gives the kernel C^{⊗m} on every role.
- `triangular-factorization`: Lower triangular factorization: Every rational m×m matrix of rank a factors as E₁ Π E₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with a ones (a reversed-order Bruhat factorization).
- `address-shear`: Address shear: The address permutation (H,D) ↦ (H+MD, D) on two groups of m digit fields over ℤ/q^bℤ; a matrix of rank a is performed with exactly a smaller field interchanges plus O(V) work.
- `bit-network-interface`: Bit network interface: The XOR network with projection frames Φ_{P_U}: each route's endpoint matrices differ by the identity, so every role receives the shear H ← H + D, while the edge ranks sum to s_b < W_b·m.
- `fast-address-interchange`: Fast address-chunk interchange: Interchanging two disjoint contiguous address fields of u bits in an array costs O(V·u^τ) with τ = 1 − 2⁻⁵⁰, realized by recursively applying the bit network and computing XOR combinations of data.
- `fixed-point-precision`: Fixed-point disk grid and truncation: Values are stored as complex numbers in the unit disk with real and imaginary parts on the grid 2^{−p}ℤ, and Q_p truncation toward that grid adds error below √2·2^{−p}.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀ on the same bit position in each of up to d equal-width address chunks costs O(V·d^λ′) with λ′ < 1, by recursing through the complex network's phase frames, with exact dyadic intermediates and one final truncation.
- `signed-kronecker-packing`: Signed Kronecker packing: Multiplying two polynomial records by packing their signed integer coefficients into one large integer, multiplying with the O(n log n) multiplier, and unpacking, in O(rp log(rp)) time.
- `discrete-fourier-transform`: Normalized discrete Fourier transform: The map F_q sending a length-q complex vector u to (1/q)Σ u_j e^{−2πijk/q}, a contraction with a signed inverse F_q⁺.
- `multidimensional-transform`: Multidimensional Fourier transform: The tensor product of one-dimensional normalized Fourier transforms applied along each axis of an array on a product of cyclic groups.
- `synthetic-transform`: Synthetic polynomial transform: Nussbaumer's Fourier transform over ℂ[y]/(y^r+1) using ω_t = y^{2r/t} as root of unity, computed by decimation-in-frequency butterflies and signed shifts, with outputs left in bit-reversed frequency order.
- `gaussian-resampling`: Gaussian resampling with retained permutations: Harvey–van der Hoeven's identity expressing a Fourier transform of prime length s through one of power-of-two length t (P_sF_s = 2^{2α²} B₀ P_t F_t A), here with both coordinate permutations kept in the formula instead of sorted.
- `parameter-choice`: Fixed rational parameters and cost table: The compatible choice τ = σ = 1 − 2⁻⁵⁰, λ′ = 1 − 2⁻⁵⁴, ε = 2⁻⁷⁵, κ = 2⁻¹⁸², etc., under which every term of the normalized cost table is O((lg n)^{1−κ}).
- `transform-layout`: Fast synthetic transform layout: A tape layout placing the selected bits of participating axes at a common offset in consecutive K-bit chunks so simultaneous butterfly layers apply, with chunk interchanges paying for the movement.
- `cyclic-convolution`: Cyclic convolution: The product of coefficient arrays indexed by a cyclic group (polynomial product modulo x^S − 1), which the Fourier transform turns into pointwise multiplication.
- `radix-digit-convolution`: Radix-digit reduction to convolution: Splitting each n-bit input into radix-2^b digits turns integer multiplication into convolution of short integer coefficient lists followed by carry propagation.
- `crt-address-map`: Chinese-remainder address map: A convolution-preserving map placing the radix-digit coefficient list on a product of distinct prime-length cyclic axes, implemented by triangular controlled shifts and axis moves.
- `bluestein-chirp`: Bluestein chirp identity: Rewriting a Fourier transform (with its target permutation) as pointwise multiplication by a chirp, a cyclic convolution with the chirp, and another chirp multiplication.
- `coefficient-twist`: Coefficient twist: The phase twist x ↦ ζy with ζ = e^{πi/r}, mapping ℂ[x]/(x^r−1) isomorphically onto ℂ[y]/(y^r+1), so cyclic convolution in the last coordinate becomes negacyclic polynomial arithmetic.
- `synthetic-convolution`: Normalized convolution over the polynomial ring: Cyclic convolution of arrays with values in ℂ[y]/(y^r+1), computed by two forward synthetic transforms kept in stored frequency order, packed pointwise ring products, and the opposite transform.
- `exact-recovery`: Exact coefficient recovery and carries: Removing known normalizations and digit scales, showing the computed coefficient error is below 1/2 so rounding gives exact integers, then propagating carries to obtain the binary product.
- `main-theorem`: Integer multiplication below n log n: A single deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2⁻¹⁸², disproving the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-turing-machine`: Multitape Turing machine
- `asymptotic-notation-beyond-big-o`: Asymptotic notation beyond big-O
- `logarithms-and-exponents`: Logarithms and exponents
- `floor-and-ceiling`: Floor and ceiling
- `binary-representation-of-integers`: Binary representation of integers
- `schoolbook-integer-arithmetic-with-carries`: Schoolbook integer arithmetic with carries
- `two-s-complement-and-signed-integers`: Two's complement and signed integers
- `xor-and-arithmetic-modulo-2`: XOR and arithmetic modulo 2
- `modular-arithmetic`: Modular arithmetic
- `prime-numbers-and-gcd`: Prime numbers and gcd
- `euclidean-algorithm`: Euclidean algorithm
- `chinese-remainder-theorem`: Chinese remainder theorem
- `binomial-coefficients-and-subsets`: Binomial coefficients and subsets
- `permutations`: Permutations
- `lexicographic-order`: Lexicographic order
- `vectors-and-matrices`: Vectors and matrices
- `linear-maps-and-invertibility`: Linear maps and invertibility
- `vector-spaces-subspaces-and-dimension`: Vector spaces, subspaces and dimension
- `rank-of-a-matrix`: Rank of a matrix
- `dot-product-and-orthogonality`: Dot product and orthogonality
- `gaussian-elimination`: Gaussian elimination
- `fields-and-rings`: Fields and rings
- `fast-fourier-transform`: Fast Fourier transform
- `polynomial-multiplication-via-evaluation-and-interpolation`: Polynomial multiplication via evaluation and interpolation
- `bit-reversal-permutation`: Bit-reversal permutation
- `karatsuba-multiplication`: Karatsuba multiplication
- `divide-and-conquer-recurrences`: Divide-and-conquer recurrences
- `mathematical-induction`: Mathematical induction
- `geometric-series`: Geometric series
- `limits`: Limits
- `exponential-function-and-gaussians`: Exponential function and Gaussians
- `absolute-value-and-the-triangle-inequality`: Absolute value and the triangle inequality
- `rounding-to-the-nearest-integer`: Rounding to the nearest integer
- `newton-s-method`: Newton's method
- `integer-division-and-square-root`: Integer division and square root
- `deterministic-algorithm-and-worst-case-running-time`: Deterministic algorithm and worst-case running time
- `stacks`: Stacks
- `binary-counter`: Binary counter
- `hamming-weight`: Hamming weight
- `matrix-transposition`: Matrix transposition
- `turing-machine-alphabet-and-simulation-constants`: Turing machine alphabet and simulation constants

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
