# exegenius task 0003-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N1` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-alphabet multitape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{-182}, refuting the n log n lower-bound conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science background: asymptotic analysis of algorithms and solving simple cost recurrences, basic Turing machines and multitape simulation, binary representation of integers and machine arithmetic (carries, two's complement, XOR, fixed-point rounding), and the discrete mathematics taught to everyone (induction, modular arithmetic, gcd, primes, the Chinese remainder theorem, permutations, binomial coefficients, lexicographic order). From the required mathematics they have a first course in linear algebra (vectors, matrices, rank, invertibility, triangular and diagonal matrices, linear maps over Q and C) and basic complex numbers and polynomials. They have not studied tensor products of operators, bilinear forms, Hadamard or Bruhat-type factorizations, FFT variants beyond a textbook mention, or research-level integer multiplication algorithms.

## Pages, in reading order

- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
- `butterfly`: Normalized butterfly H₀: The two-point map (u, v) ↦ ((u+v)/2, (u−v)/2), the basic step of radix-two Fourier transforms.
- `gaussian-dyadics`: Gaussian dyadics and fixed-point truncation: Complex numbers whose real and imaginary parts have power-of-two denominators, stored exactly in fixed-point words and truncated toward zero to the p-bit grid only at the end of a layer.
- `linear-network`: Linear bank-exchange network: A fixed finite network of linear gates on wires (roles) that exchanges two banks of values with prescribed signs while restoring every auxiliary scratch value.
- `hvdh-multiplier`: Established O(n log n) multiplier: Harvey and van der Hoeven's fixed-tape O(n log n) integer multiplication algorithm, used here only as an ordinary subroutine on short records.
- `lower-triangular-factorization`: Lower triangular factorization: Writing any rational matrix of rank a as E₁ΠE₂ with invertible lower triangular E₁, E₂ and a partial permutation Π with a ones, a reversed Bruhat factorization.
- `stream-array-layout`: Array streams and logical volume: Arrays are stored on tape in lexicographic order of their address fields with implicit addresses, and the logical volume V is the number of stored data bits.
- `frame-invariant`: Frames and the common-frame identity: Storing each wire's array through an invertible operator (frame) that is common at each gate, so pointwise gates commute with frames and only endpoint frames determine the net operator.
- `address-shear`: Address shear: The array permutation moving the entry at address (H, D) to (H + MD, D) for a matrix M acting on two groups of address fields.
- `elementary-stream-ops`: Elementary stream operations: Linear-time tape operations that permute or move a single fixed-radix digit of the address, split and merge streams on a digit, and split rows cyclically into a fixed number of streams.
- `row-splitting`: Row splitting among roles: Distributing rows of an array cyclically among the W wire roles so that each role stream has the same address shape and volume V/W.
- `controlled-shifts`: Controlled shifts: A linear-time update adding to a later address field an offset computed from earlier control fields (or scaling it by a fixed unit), implemented by splitting and remerging blocks.
- `scratch-restoration`: Restoration of arbitrary scratch values: An eight-row schedule that subtracts the effect of unknown scratch contents, adds the intended computation, and uncomputes, so scratch wires may start with arbitrary values.
- `triple-gadget`: Three-element-subset gather and scatter: Gates indexed by three-element subsets of [100]: gather and scatter produce coefficients depending on intersection size, and side wires cancel the unwanted ones so the net effect is y ← y + x.
- `subspace-labels`: Nested subspace labels: Nondegenerate subspaces of a fixed bilinear space attached to gates and terminals, nested along each edge, whose orthogonal residual dimensions count the smaller operations an edge needs.
- `rank-deficit`: Rank deficit of the network: The property that the total number s of smaller calls over all edges is strictly less than the wire count W times the label dimension m.
- `volume-recurrence`: Volume-normalized recurrence: The recurrence F_k ≤ (s/W)F_{k−1} + O(1) for cost divided by volume, which yields a power saving because s/W < m.
- `bit-motif-interface`: Rational matrix interface: The bit network with XOR gates and rational projection matrices on its vertices, whose endpoint matrices differ by the identity on every role and whose edge ranks sum to s_b < W_b·m.
- `matrix-shear-cost`: Cost of a rational matrix shear: A shear (H, D) ↦ (H + AD, D) by a fixed rational matrix of rank a costs exactly a interchanges of smaller field pairs plus linear work.
- `chunk-interchange`: Fast address chunk interchange: A fixed-tape procedure that exchanges two equal-width contiguous address chunks of u bits in O(Vu^τ) time with τ < 1, via XOR combinations of data driven by the bit network.
- `phase-frames`: Binary phase frames: Frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} attached to binary labels, whose edge changes factor into one two-point kernel aI + bX_v per residual basis vector.
- `complex-motif-interface`: Binary phase interface: The complex network with binary labels: after endpoint corrections it applies the tensor power of the kernel C on every role using s_c < W_c·m smaller kernel calls.
- `packed-selected-bit`: Packed selected-bit addition: XORing selected bits of one address chunk into another by eight packed cyclic shifts with guard bits, followed by deterministic repair of an explicitly bounded set of exceptional addresses.
- `simultaneous-layer`: Simultaneous butterfly layer: Applying H₀ on the same bit position in up to d address chunks at once in O(Vd^{λ'}) time, λ' < 1, by recursing through the complex network and evaluating the layer exactly before one truncation.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree below r with y^r = −1, where multiplication by a power of y is a signed cyclic shift of coefficients.
- `signed-packing`: Signed coefficient packing: A signed Kronecker substitution that evaluates integer polynomials at B₀ = 2^{4p}, multiplies with the established multiplier, and recovers coefficients by centered residues, giving products in the ring modulo y^r + 1.
- `cyclic-convolution`: Cyclic convolution: The product of coefficient arrays in which indices add modulo the array length, i.e. polynomial multiplication modulo x^S − 1.
- `radix-digit-convolution`: Radix-digit convolution: Writing each input as a polynomial in 2^b, so that the product becomes a convolution of small digit coefficients followed by carry propagation.
- `phase-twist`: Coefficient phase twist: The map x_d ↦ ζy with ζ = e^{πi/r} that converts cyclic convolution along the last axis into negacyclic multiplication modulo y^r + 1.
- `exact-recovery`: Exact recovery by rounding and carries: Undoing known scales, rounding each approximate coefficient whose error is below 1/2 to the exact integer, and propagating radix-2^b carries to obtain the binary product.
- `dft`: Normalized discrete Fourier transform: The map sending a length-q vector to its averages against the q-th roots of unity; it is a contraction and turns cyclic convolution into pointwise multiplication.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of prime length s through one of nearby power-of-two length t, using Gaussian-weighted contractions.
- `synthetic-fft`: Synthetic polynomial transform: A radix-two Fourier transform over the ring modulo y^r + 1 whose roots of unity are powers of y, so twiddles are signed shifts; its output is stored in bit-reversed frequency order.
- `retained-permutations`: Resampling with retained permutations: Keeping the coordinate permutations P_s and P_t inside the resampling identity P_sF_s = 2^{2α²}B₀P_tF_tA instead of sorting, and letting the source permutation cancel across forward transforms, pointwise product, and opposite transform.
- `bluestein-chirp`: Bluestein's chirp identity: Writing a Fourier transform, including its frequency permutation, as pointwise multiplication by a chirp, a cyclic convolution with the chirp, and another chirp multiplication.
- `transform-layout`: Transform layout: A positional permutation of address bits placing the bits used in each transform round at a common offset in consecutive K-bit chunks, so simultaneous layers apply and the frequency order is retained.
- `synthetic-convolution`: Convolution from the retained transform layout: Normalized convolution over the polynomial ring computed by two forward synthetic transforms, pointwise packed products in the stored order, and the opposite transform consuming that order.
- `tensor-resampling`: Tensor resampling interface: Applying the one-dimensional resampling maps line by line along each of d axes of a padded power-of-two box, with axis exposure done by chunk interchanges.
- `crt-address-map`: Chinese-remainder address map: The isomorphism x ↦ ∏ x_i^{μ_i} that turns one cyclic convolution of length S = ∏ s_i into a multidimensional cyclic convolution on distinct prime axes, implemented by triangular controlled shifts and axis moves.
- `cost-table`: Parameter choice and cost table: Fixed rational parameters (τ = 1 − 2^{-50}, ε = 2^{-75}, κ = 2^{-182}, …) under which every term of the cost per bit is at most p^{1−2κ}.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-alphabet multitape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{-182}, refuting the n log n lower-bound conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-turing-machine`: Multitape Turing machine
- `binary-representation-of-integers`: Binary representation of integers
- `carry-propagation`: Carry propagation
- `two-s-complement`: Two's complement
- `exclusive-or`: Exclusive or
- `schoolbook-multiplication`: Schoolbook multiplication
- `floor-and-ceiling`: Floor and ceiling
- `rounding-to-the-nearest-integer`: Rounding to the nearest integer
- `fixed-point-numbers`: Fixed-point numbers
- `binary-logarithm`: Binary logarithm
- `modular-arithmetic`: Modular arithmetic
- `greatest-common-divisor`: Greatest common divisor
- `prime-numbers`: Prime numbers
- `chinese-remainder-theorem`: Chinese remainder theorem
- `mathematical-induction`: Mathematical induction
- `recurrence-relations-for-running-time`: Recurrence relations for running time
- `geometric-series`: Geometric series
- `permutations`: Permutations
- `binomial-coefficients`: Binomial coefficients
- `lexicographic-order`: Lexicographic order
- `vectors-and-matrices`: Vectors and matrices
- `vector-spaces-subspaces-and-dimension`: Vector spaces, subspaces and dimension
- `matrix-rank`: Matrix rank
- `invertible-matrices`: Invertible matrices
- `triangular-and-diagonal-matrices`: Triangular and diagonal matrices
- `permutation-matrices`: Permutation matrices
- `gaussian-elimination`: Gaussian elimination
- `rational-numbers`: Rational numbers
- `maximum-norm`: Maximum norm
- `triangle-inequality`: Triangle inequality
- `exponential-function-and-euler-s-formula`: Exponential function and Euler's formula

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
