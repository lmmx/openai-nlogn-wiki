# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/O1` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^(−182), refuting the n log n optimality conjecture in that model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: algorithms and data structures (asymptotic analysis, recurrences and divide-and-conquer, sorting including stable radix sort, amortized counting, schoolbook and Karatsuba multiplication, and the textbook FFT for polynomial multiplication), theory of computation (Turing machines, tapes, deterministic machines, Boolean circuits, worst-case time and lower bounds), and discrete mathematics (sets, permutations, subsets and counting, induction, graphs, modular arithmetic, gcd, primes and the Chinese remainder theorem). From the supporting mathematics they have first-year calculus (limits, logarithms and exponentials, geometric series, Newton's method), introductory linear algebra (matrices, inverses, transposes, triangular and permutation matrices, eigenvalues, dot products and orthonormal bases) and complex numbers, plus the machine-level number representations of computer organization (binary and radix digits, two's complement, bitwise XOR, carries). They have not studied the research literature on fast integer multiplication, Gaussian resampling, synthetic polynomial transforms, multilinear algebra beyond the basics, bilinear-form theory, analytic number theory, or index coding.

## Pages, in reading order

- `nlogn-conjecture`: n log n optimality conjecture: Schönhage and Strassen's conjecture that n log n is the optimal order of growth for multiplying n-bit integers, here in the multitape Turing machine model.
- `hvdh-multiplier`: Harvey–van der Hoeven multiplier: The established deterministic O(n log n) multitape integer multiplier, used here only as an ordinary subroutine on short records.
- `polynomial-ring`: Polynomial ring modulo y^r + 1: Complex polynomials reduced modulo y^r + 1 with r a power of two, where multiplication by a power of y is a signed cyclic shift of coefficients.
- `disk-grid`: Disk-grid fixed-point arithmetic: Complex values in the unit disk with real and imaginary parts on the grid 2^{-p}ℤ, computed exactly as Gaussian dyadics and truncated toward zero by Q_p.
- `signed-packing`: Signed Kronecker packing: Multiplying polynomials with signed coefficients by evaluating them at a large power of two, multiplying the resulting integers, and extracting centered coefficients.
- `array-layout`: Lexicographic array layout and logical volume: Arrays on a product of address fields are stored on tape in lexicographic order with addresses implicit, and their cost is measured against the logical volume V, the number of stored data bits.
- `elementary-stream-ops`: Elementary stream operations: Linear-time tape primitives: permuting or moving single digits, splitting on a digit and merging, and splitting rows cyclically into a fixed number of streams.
- `controlled-shifts`: Controlled shifts: Linear-time updates that add to a target address field an offset computed from earlier control fields (or multiply it by a fixed unit), implemented by splitting and remerging each fiber.
- `linear-algebra`: Linear maps, matrices and rank: Vector spaces over a field (including the two-element field F₂ where addition is XOR), linear maps, matrices, subspaces, dimension and rank.
- `scratch-restoration`: Scratch restoration: The transparent-computation trick of subtracting a scratch register's effect, computing, adding, and uncomputing, so that the net result is independent of arbitrary initial scratch values.
- `bilinear-form`: Nondegenerate bilinear forms and orthogonal complements: A symmetric bilinear form pairs vectors; a subspace is nondegenerate when the form restricted to it has no kernel, and then the space splits as the subspace plus its orthogonal complement.
- `triple-intersection`: Three-element-subset intersection construction: The Frankl–Wilson-style use of 3-subsets of a 100-element set, where gather and scatter produce coefficients depending on intersection size and side wires cancel the unwanted ones, giving y ← y + x.
- `bank-exchange-network`: Bank-exchange linear network: A fixed linear network of pointwise gates on wires (roles) that, in three stages, exchanges two banks of values with prescribed signs while restoring every auxiliary scratch wire.
- `role-streams`: Row splitting into role streams: Rows of an array are distributed cyclically among the network's W roles so each role stream has volume V/W, and recursive calls are scheduled depth-first on a fixed set of tapes by parking inactive streams on a stack.
- `frames`: Frames and the common-frame identity: Each network vertex gets an invertible linear operator (frame) giving the stored array's representation; since a common frame commutes with pointwise gates, the network implements the endpoint frame ratio on every role.
- `tensor-product`: Tensor product: The tensor product of vector spaces or linear maps, whose dimension is the product of the factors' dimensions; tensor powers act factorwise on multi-index arrays.
- `subspace-labels`: Subspace labels and orthogonal residuals: Nested nondegenerate subspaces of a fixed m-dimensional tensor space are attached to the network's vertices, and the dimension of each edge's orthogonal residual counts the smaller operations that edge needs.
- `rank-deficit`: Rank deficit and recursive power saving: The total number s of smaller calls satisfies s < Wm, so a recursion with parameter growth m and volume split W gives a cost factor e^τ with τ < 1 instead of e.
- `lower-triangular-factorization`: Lower triangular factorization: Every rational matrix of rank a factors as E₁ΠE₂ with invertible lower triangular E₁, E₂ and a partial permutation Π with a ones (a reversed Bruhat factorization).
- `address-shear`: Rational address shear: The address permutation (H,D) ↦ (H+AD, D) on two groups of fields, performed with exactly rank(A) smaller field interchanges plus linear work.
- `chunk-interchange`: Fast address-chunk interchange: A tape procedure that interchanges two disjoint u-bit address fields of an array in O(V u^τ) time for a fixed τ < 1, by running the bit network with shear frames and recursing on smaller interchanges.
- `packed-selected-bit`: Packed selected-bit addition: XORing corresponding selected bits of two address chunks using eight cyclic shifts of whole chunks with guard values, then deterministically repairing the small set of exceptional addresses by sorting.
- `dft`: Normalized discrete Fourier transform: The length-q transform averaging inputs times powers of e^{∓2πi/q}, normalized by 1/q so it is a contraction.
- `multidim-dft`: Multidimensional Fourier transform: The tensor product of one-dimensional transforms over several axes, applied to arrays indexed by a product of cyclic groups.
- `butterfly`: Normalized butterfly: The two-point map H₀(u,v) = ((u+v)/2, (u−v)/2), the basic step of radix-two decimation-in-frequency transforms.
- `synthetic-transform`: Synthetic polynomial transform: Nussbaumer's Fourier transform over the polynomial ring, where powers of y serve as roots of unity so twiddles are signed shifts and the transform is butterflies plus monomial multiplications.
- `phase-frames`: Binary phase frames: Frames for the complex network built from the kernel C = H·diag(1,i)·H and quadratic-form phases over F₂, so each edge change is one two-point kernel per orthonormal residual basis vector.
- `simultaneous-layer`: Simultaneous butterfly layer: Applying the butterfly H₀ on one selected bit in each of up to d address chunks at once in O(V d^λ′) time, λ′ < 1, by running the complex network with phase frames recursively and truncating once at the end.
- `contraction-error`: Error accounting through contractions: Since every exact map used is a contraction, errors of approximate subroutines add when composed, which bounds the final numerical error.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of prime length s through one of nearby power-of-two length t, via Gaussian-weighted contractions.
- `synthetic-layout`: Synthetic transform layout and cost: The tape layout that places the selected bits of all axes at common offsets in consecutive chunks, so each synthetic transform round is one simultaneous layer, with frequencies left in a retained bit-reversed order.
- `resampling-retained-permutations`: Resampling with retained permutations: A variant of Gaussian resampling that keeps the source and target coordinate permutations inside the transform identity instead of executing them as sorts.
- `parameter-choice`: Parameter choice and cost table: Fixed rational exponents (τ, λ′, ε, c, δ, …) and size parameters chosen so every row of the normalized cost table is at most p^{1−2κ}.
- `cyclic-convolution`: Cyclic convolution: Multiplication modulo x^S − 1 on coefficient arrays, which the Fourier transform turns into pointwise multiplication.
- `radix-digit-reduction`: Radix-digit reduction to convolution: Splitting each n-bit input into b-bit digits turns integer multiplication into convolution of short nonnegative integer coefficient lists, followed by carry propagation.
- `chirp-identity`: Bluestein chirp identity: Multiplying by quadratic phases (chirps) before and after a cyclic convolution computes a Fourier transform, here including its target permutation.
- `coefficient-twist`: Coefficient phase twist: Multiplying coefficient k by e^{πik/r} turns cyclic convolution in the last axis into negacyclic multiplication modulo y^r + 1.
- `permutation-cancellation`: Source-permutation cancellation: The source permutation retained in both forward transforms cancels against the opposite-sign transform when computing a convolution.
- `exact-recovery`: Exact recovery by rounding and carries: Once the approximate coefficient error is below 1/2, rounding gives the exact integer coefficients, and radix carry propagation gives the binary product.
- `ring-convolution`: Normalized convolution over the polynomial ring: Computing normalized cyclic convolution of arrays of ring elements by two forward synthetic transforms, pointwise packed products in the retained order, and the opposite transform.
- `prime-lengths`: Prime source lengths: Distinct odd primes s_i chosen just below the power-of-two axis lengths t_i, so their product fills a fixed fraction of the padded box while leaving the separation resampling needs.
- `crt-address-map`: Chinese-remainder address map: An algebra isomorphism from one cyclic convolution of length S = ∏ s_i to a multidimensional cyclic convolution on pairwise coprime axes, implemented by triangular controlled shifts and axis moves.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^(−182), refuting the n log n optimality conjecture in that model.

## Concepts the reader knows

- `big-o-notation`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-turing-machine`: Multitape Turing machine
- `asymptotic-notation-beyond-big-o`: Asymptotic notation beyond big-O
- `logarithms-and-exponentials`: Logarithms and exponentials
- `floor-and-ceiling`: Floor and ceiling
- `limits-and-liminf`: Limits and liminf
- `geometric-series`: Geometric series
- `mathematical-induction`: Mathematical induction
- `recurrences-and-divide-and-conquer-analysis`: Recurrences and divide-and-conquer analysis
- `worst-case-running-time`: Worst-case running time
- `lower-bounds-for-computational-problems`: Lower bounds for computational problems
- `deterministic-algorithm`: Deterministic algorithm
- `binary-and-radix-representation`: Binary and radix representation
- `schoolbook-addition-and-multiplication-with-carries`: Schoolbook addition and multiplication with carries
- `karatsuba-multiplication`: Karatsuba multiplication
- `fast-fourier-transform`: Fast Fourier transform
- `two-s-complement-and-signed-integer-representation`: Two's complement and signed integer representation
- `fixed-point-binary-fractions`: Fixed-point binary fractions
- `bitwise-xor`: Bitwise XOR
- `modular-arithmetic`: Modular arithmetic
- `greatest-common-divisor-and-coprimality`: Greatest common divisor and coprimality
- `prime-numbers`: Prime numbers
- `chinese-remainder-theorem`: Chinese remainder theorem
- `integer-division-and-integer-square-root`: Integer division and integer square root
- `newton-s-method`: Newton's method
- `sets-cartesian-products-and-cardinality`: Sets, Cartesian products and cardinality
- `subsets-and-binomial-coefficients`: Subsets and binomial coefficients
- `indicator-vector`: Indicator vector
- `permutations`: Permutations
- `lexicographic-order`: Lexicographic order
- `sorting-and-stable-radix-sort`: Sorting and stable radix sort
- `binary-counters-and-amortized-analysis`: Binary counters and amortized analysis
- `stack`: Stack
- `directed-graphs-and-acyclic-networks`: Directed graphs and acyclic networks
- `boolean-and-arithmetic-circuits`: Boolean and arithmetic circuits
- `matrix-inverse-transpose-and-identity`: Matrix inverse, transpose and identity
- `special-matrices`: Special matrices
- `eigenvalues`: Eigenvalues
- `sup-norm-and-the-triangle-inequality`: Sup norm and the triangle inequality
- `number-systems-and-their-notation`: Number systems and their notation
- `fields-and-rings`: Fields and rings
- `gaussian-function`: Gaussian function

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
