# exegenius task 0003-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N4` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n(lg n)^(1−κ)) time: A single deterministic fixed-tape Turing machine computes the exact product of two n-bit integers in O(n(lg n)^{1−κ}) worst-case time with κ = 2^{−182}, refuting the n log n lower-bound conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science degree: discrete mathematics (sets, permutations, binomial coefficients, induction, modular arithmetic, gcd and the extended Euclidean algorithm, primes), an introductory linear algebra course (vectors, matrices, subspaces, dimension, eigenvalues, the standard dot product and orthogonality over the reals), single-variable calculus (limits, logarithms, exponentials, geometric series, Newton's method), and the standard algorithms and theory courses (asymptotic notation, recurrences, divide-and-conquer such as Karatsuba, amortized binary counters, basic Turing machines). They know binary representation, fixed-width binary arithmetic with carries, and complex numbers including roots of unity, but have not studied the FFT literature in depth, abstract algebra beyond modular arithmetic, tensor products, general bilinear forms, numerical error analysis, or the integer-multiplication research line beyond Karatsuba.

## Pages, in reading order

- `n-log-n-conjecture`: n log n optimality conjecture: Schönhage and Strassen's conjecture that n-bit integer multiplication needs order n log n time, here read as an eventual Ω(n lg n) lower bound for every fixed multitape machine.
- `harvey-van-der-hoeven-multiplier`: Harvey–van der Hoeven multiplier: The previously established deterministic multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short records.
- `negacyclic-ring`: Polynomial ring ℂ[y]/(yʳ+1): The ring of complex polynomials of degree below r with y^r = −1, in which multiplying by a power of y is a signed shift of the coefficient list and powers of y act as roots of unity.
- `butterfly-h0`: Normalized butterfly H₀: The two-point map H₀(u,v) = ((u+v)/2, (u−v)/2), the radix-two step of fast Fourier-type transforms, applied coefficientwise to polynomial records.
- `gaussian-dyadics`: Gaussian dyadic numbers: Complex numbers whose real and imaginary parts are rationals with power-of-two denominators, the ring ℤ[i,1/2], in which the butterfly layers are computed exactly.
- `elementary-streams`: Arrays on tape and elementary stream operations: Multi-index arrays are stored in lexicographic address order with implicit addresses, and fixed digit permutations, digit moves, splits into streams and merges each cost O(V) for logical bit volume V.
- `address-shear`: Address shear: The address permutation (H,D) ↦ (H+D,D) on two field groups, which together with two linear-cost updates gives the interchange (H,D) ↦ (D,H).
- `controlled-shifts`: Controlled shifts: Linear-time updates that add to, or cyclically shift, a later address field by an amount computed from earlier fields, possible because the target field follows its control fields in tape order.
- `matrix-rank`: Linear maps and matrix rank: Matrices represent linear maps between vector spaces, and the rank of a matrix is the dimension of its image.
- `linear-network`: Linear network with wire roles: A fixed finite circuit of linear gates on wires, each wire's fixed place called its role, which in three stages exchanges two data banks (X,Y) ↦ (−Y,X) with prescribed signs.
- `frames`: Frames and the common-frame identity: Each network vertex gets an invertible operator D_v on the wire's array; edges apply D_v D_u^{-1}, pointwise gates commute with a common frame, so the whole network implements D_out S D_in^{-1} on rows split cyclically among the roles.
- `scratch-restoration`: Restoration of scratch values: A gate schedule that subtracts the effect of arbitrary initial auxiliary values, performs the update, and undoes its copies so every scratch wire ends with its initial value.
- `triple-intersection-construction`: Three-element subset construction: Data indexed by 3-element subsets of a 100-set are combined by gather/scatter through central wires, giving coefficients depending on intersection size, and side wires cancel the unwanted ones so the net effect is y ← y + x.
- `bilinear-form`: Nondegenerate bilinear forms: A bilinear form pairs vectors into scalars; it is nondegenerate when no nonzero vector is orthogonal to everything, which lets a subspace split off its orthogonal complement.
- `tensor-product`: Tensor products: The tensor product of vector spaces or operators builds a multi-index space or acts independently on each index; the paper's label space and simultaneous butterfly layers are tensor products.
- `subspace-labels`: Subspace labels and orthogonal residuals: Nested nondegenerate subspaces of a fixed m-dimensional bilinear space are attached to the network's vertices, and the dimension of the orthogonal residual on each edge counts the smaller operations needed there.
- `rank-saving`: Rank saving s < Wm: The key finite fact: the total number s of smaller calls over all edges of a network with W wires and label dimension m is strictly less than Wm.
- `recursive-power-saving`: Recursive power saving: Splitting the work into s calls each on volume V/W gives the normalized recurrence F_k ≤ (s/W)F_{k−1} + O(1), and s/W < m^τ with τ < 1 yields cost O(V e^τ) instead of O(V e).
- `rational-matrix-interface`: Rational matrix interface: The XOR bit network with projection matrices as frames, whose endpoint differences are the identity on every role, so it implements the address shear with total edge rank s_b < W_b m.
- `binary-phase-interface`: Binary phase interface: The complex network over Gaussian dyadics with binary labels, whose edge frames are products of two-point kernels C = HSH and whose endpoints telescope to a tensor power of C, convertible to the H₀ layer.
- `lower-triangular-factorization`: Lower triangular factorization: Every rational matrix of rank a factors as E₁ΠE₂ with invertible lower triangular E₁, E₂ and a partial permutation Π with a ones, a reordered Bruhat factorization.
- `chunk-interchange`: Fast address-chunk interchange: The first tape procedure: exchanging two disjoint u-bit address fields of an array in O(V u^τ) time with τ < 1, by recursively running the bit network with shears as edge frames.
- `packed-selected-bit-addition`: Packed selected-bit addition: Changing selected address bits in several chunks at once by whole-chunk cyclic shifts and moves, followed by a deterministic repair of an explicitly bounded set of exceptional addresses.
- `fixed-point-approximation`: Fixed-point approximation and error accounting: Complex values are stored on the grid 2^{-p}(ℤ+iℤ) in the unit disk, truncated toward zero, and errors of approximate contractions add when composed.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The second tape procedure: applying H₀ at the same bit position of up to d address chunks at once in O(V d^{λ'}) time with λ' < 1, computed exactly in Gaussian dyadics and truncated once.
- `signed-packing`: Signed Kronecker packing: Packing the signed fixed-point coefficients of two ring elements into large integers so one call to the O(N log N) multiplier yields their exact polynomial product.
- `discrete-fourier-transform`: Normalized discrete Fourier transform: The map sending a length-q vector to the averages of its entries multiplied by powers of a q-th root of unity; it is a contraction and diagonalizes cyclic convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of coprime length s through one of a nearby length t, using Gaussian-weighted contractions, so prime-length axes become power-of-two axes.
- `synthetic-transform`: Synthetic polynomial transform: Nussbaumer's Fourier transform over ℂ[y]/(y^r+1) using powers of y as roots of unity, so it needs only signed shifts, butterflies and address rearrangements, with a stored frequency order consumed by the inverse transform.
- `synthetic-convolution`: Convolution over the polynomial ring: Normalized cyclic convolution of arrays over ℂ[y]/(y^r+1) computed by two forward synthetic transforms on a tape layout using chunk interchanges and simultaneous layers, packed pointwise products, and the opposite transform.
- `parameter-choice`: Parameter choice and cost balance: Fixed rational exponents (τ, λ′, c, ε, δ, …) and sizes d ≈ p^ε, K ≈ d^c make every normalized cost-table term at most p^{1−2κ}, with smallest margin 2^{−181} = 2κ.
- `cyclic-convolution`: Cyclic convolution: The product of polynomials modulo x^S − 1 (or its multidimensional analogue), where exponents wrap around cyclically.
- `radix-digit-convolution`: Multiplication as digit convolution: Splitting each integer into radix-2^b digits turns their product into the convolution of short digit sequences, followed by carry propagation.
- `crt-address-map`: Chinese-remainder address map: An algebra isomorphism x ↦ ∏ x_i^{μ_i} that turns a cyclic convolution of length S = ∏ s_i into a multidimensional cyclic convolution on pairwise coprime axes, implemented by triangular controlled shifts.
- `bluestein-chirp`: Bluestein's chirp identity: A Fourier transform equals pointwise multiplication by a quadratic-phase chirp, a cyclic convolution with the chirp, and another chirp multiplication.
- `coefficient-twist`: Coefficient phase twist: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} maps cyclic convolution modulo x^r − 1 isomorphically onto negacyclic multiplication modulo y^r + 1.
- `retained-permutations`: Retained transform permutations: Instead of sorting, the source and target coordinate permutations of resampling stay inside the transform identity; the target one is absorbed by the chirp and the source one cancels across forward transforms, pointwise product and inverse transform.
- `exact-recovery`: Exact recovery by rounding and carries: Removing known scales, bounding the coefficient error strictly below 1/2, rounding to integers and propagating carries gives the exact binary product.
- `main-theorem`: Integer multiplication in O(n(lg n)^(1−κ)) time: A single deterministic fixed-tape Turing machine computes the exact product of two n-bit integers in O(n(lg n)^{1−κ}) worst-case time with κ = 2^{−182}, refuting the n log n lower-bound conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-turing-machine`: Multitape Turing machine
- `big-omega-and-big-theta-notation`: Big-Omega and Big-Theta notation
- `worst-case-running-time`: Worst-case running time
- `deterministic-algorithm`: Deterministic algorithm
- `logarithms`: Logarithms
- `iterated-logarithm`: Iterated logarithm
- `floor-and-ceiling`: Floor and ceiling
- `limits-and-lim-inf`: Limits and lim inf
- `geometric-series`: Geometric series
- `recurrence-relations`: Recurrence relations
- `mathematical-induction`: Mathematical induction
- `binary-representation`: Binary representation
- `positional-radix-representation`: Positional radix representation
- `binary-addition-with-carries`: Binary addition with carries
- `signed-binary-numbers-and-fixed-point-numbers`: Signed binary numbers and fixed-point numbers
- `schoolbook-multiplication`: Schoolbook multiplication
- `karatsuba-multiplication`: Karatsuba multiplication
- `integer-division-with-remainder`: Integer division with remainder
- `modular-arithmetic`: Modular arithmetic
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality
- `extended-euclidean-algorithm`: Extended Euclidean algorithm
- `chinese-remainder-theorem`: Chinese remainder theorem
- `prime-numbers`: Prime numbers
- `binomial-coefficients`: Binomial coefficients
- `sets-cartesian-products-and-indicator-vectors`: Sets, Cartesian products and indicator vectors
- `permutations-and-bijections`: Permutations and bijections
- `lexicographic-order`: Lexicographic order
- `exclusive-or`: Exclusive or
- `the-two-element-field`: The two-element field
- `rational-numbers-and-integers`: Rational numbers and integers
- `vector-spaces-and-subspaces`: Vector spaces and subspaces
- `linear-independence-basis-and-dimension`: Linear independence, basis and dimension
- `linear-combinations-and-linear-maps`: Linear combinations and linear maps
- `matrices-and-matrix-multiplication`: Matrices and matrix multiplication
- `invertible-matrices`: Invertible matrices
- `triangular-and-diagonal-matrices`: Triangular and diagonal matrices
- `permutation-matrices`: Permutation matrices
- `matrix-transpose`: Matrix transpose
- `eigenvalues-and-eigenvectors`: Eigenvalues and eigenvectors
- `dot-product-and-orthogonality`: Dot product and orthogonality
- `kernel-and-image`: Kernel and image
- `roots-of-unity`: Roots of unity
- `gaussian-function`: Gaussian function
- `absolute-value-and-triangle-inequality`: Absolute value and triangle inequality
- `rounding-to-the-nearest-integer`: Rounding to the nearest integer
- `newton-s-method`: Newton's method
- `integer-square-root`: Integer square root
- `binary-counter-and-amortized-increment-cost`: Binary counter and amortized increment cost
- `stack`: Stack
- `tape-alphabet-tracks-and-constant-factor-simulation`: Tape alphabet, tracks and constant-factor simulation
- `pointwise-operations`: Pointwise operations
- `polynomial-multiplication-as-convolution`: Polynomial multiplication as convolution
- `polynomial-evaluation-and-interpolation`: Polynomial evaluation and interpolation

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
