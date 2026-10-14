# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/Q1` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^{1−κ}) time: One deterministic fixed-alphabet, fixed-tape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n·(lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n conjecture in that model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, binomial counting, permutations, induction, graphs, the union bound, and elementary number theory with gcd, primes, modular inverses and the Chinese remainder theorem), an algorithms course (asymptotic notation, recurrences and geometric sums, divide and conquer including Karatsuba, sorting including radix sort, stacks, amortized counters, the RAM model and worst-case running time), and an introductory theory course with Turing machines and multitape tapes. From computer organization they know binary and two's-complement encodings, bit order, XOR and binary arithmetic; from calculus and a first linear-algebra course they know logarithms, exponentials, Newton's method, simple inequalities, complex numbers with conjugates, polynomials, matrices, Gaussian elimination, rank, dot products, projections and eigenvalues over the real or rational numbers. They have not studied abstract algebra (rings, quotient rings, finite fields, tensor products, bilinear forms over 𝔽₂), Fourier analysis, numerical error analysis, or the research literature on fast integer multiplication, so the FFT machinery, resampling and all of the paper's constructions are new to them.

## Pages, in reading order

- `nlogn-conjecture`: The n log n conjecture: Schönhage and Strassen's 1971 proposal that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The established deterministic multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short records.
- `negacyclic-ring`: Polynomial ring modulo yʳ + 1: The ring ℂ[y]/(yʳ + 1) with r a power of two, in which y is a primitive 2r-th root of unity and multiplication by a power of y is a signed cyclic shift of the coefficient list.
- `normalized-butterfly`: Normalized butterfly H₀: The two-point map H₀(u, v) = ((u + v)/2, (u − v)/2), the radix-two butterfly of the transforms, which is a contraction with H₀² = I/2.
- `fixed-point`: Gaussian dyadic fixed-point arithmetic: Complex numbers whose real and imaginary parts have power-of-two denominators, stored as fixed-width two's-complement numerators on the p-bit disk grid, with truncation Q_p toward zero to 2^{−p}ℤ.
- `signed-packing`: Signed Kronecker packing: Multiplying two polynomials with signed Gaussian-integer coefficients by evaluating them at B₀ = 2^{4p} into single integers, multiplying with the established multiplier, and extracting centered coefficients before reducing modulo yʳ + 1.
- `array-layout`: Lexicographic array layout and logical volume: Arrays on address sets [a₁]×…×[a_t] stored on tape in lexicographic order with implicit addresses, with cost measured relative to the logical volume V (number of stored data bits).
- `elementary-streams`: Elementary stream operations: Linear-time O(V) tape scans that permute or move single radix-q digits of addresses, apply fixed pointwise maps to split streams, and split or merge whole rows cyclically into a fixed number of streams.
- `modular-arithmetic`: Modular arithmetic and finite fields: Arithmetic in residue rings ℤ/qᵇℤ and in the two-element field 𝔽₂, where addition is XOR, used both for address fields and for scalar values.
- `address-shear`: Address shear: The address permutation (H, D) ↦ (H + D, D) on two groups of address fields over ℤ/qᵇℤ; together with two linear-cost updates it yields the interchange (H, D) ↦ (D, H).
- `controlled-shifts`: Controlled shifts and rational scalings: O(V) tape procedures that add to an address field y an offset computed from earlier control fields modulo Q = qᵇ, or multiply y by a fixed rational unit, by splitting each fiber into pieces and merging them in a new order.
- `linear-algebra`: Linear maps, matrices and rank: Vector spaces over a field, linear maps represented by matrices, invertibility, and the rank of a matrix as the dimension of its image.
- `linear-network`: Linear network with wire roles: A fixed finite circuit of wires each carrying one scalar, with gates that apply fixed linear maps to the wires they touch; a wire's fixed place in the network is its role.
- `row-splitting`: Row splitting among wire roles: Distributing the rows of an array cyclically among the W roles of a network (padding to a multiple of W) so that every role stream has the same address shape and volume V/W and gates act pointwise.
- `frames`: Frames and the common-frame identity: Assigning an invertible linear operator D_v (a frame) to each gate and terminal so that stored arrays are D_v applied to logical arrays; since a common frame commutes with pointwise gates, the network implements D_out·S·D_in⁻¹ and each route gets its endpoint operator.
- `scratch-restoration`: Restoring scratch values: A gate schedule that first subtracts the effect of the arbitrary initial scratch values, then injects the data, then undoes its own auxiliary updates, so every scratch wire ends with its arbitrary initial value.
- `bruhat`: Lower triangular (Bruhat) factorization: Every rational matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
- `bilinear-forms`: Nondegenerate bilinear forms and orthogonal complements: A symmetric bilinear form ⟨x, y⟩ on a vector space, nondegenerate when only 0 is orthogonal to everything, together with orthogonal complements U^⊥ and orthogonal direct sums U ⊥ E.
- `triple-construction`: Three-element subset construction: Indicator vectors of 3-element subsets of a 100-element set, whose pairings |S ∩ T| mod 2 and |S ∩ T| − 1 make intersecting (or neighbouring) triples orthogonal, following Alon's account of Frankl–Wilson.
- `bank-exchange`: Three-stage bank exchange: The scalar network that, using copy, gather, scatter and side-injection gates per coordinate stage, maps two banks (X, Y) to (−Y, X) (a pure swap over 𝔽₂) while restoring all scratch wires.
- `tensor-product`: Tensor products: The tensor product of vector spaces or linear maps, so that an operator on a multi-index array acting as A₁ ⊗ … ⊗ A_d applies Aᵢ independently along each coordinate.
- `subspace-labels`: Nested subspace labels and orthogonal residuals: Attaching to every gate and terminal of the network a nondegenerate subspace of the m-dimensional space F^{⊗3}, nested along each edge, whose orthogonal residual dimension counts the smaller operations that edge needs.
- `rank-deficit`: Rank deficit s < Wm: The key property of both finite networks: the total number s of smaller calls needed over all edges is strictly less than W·m, so s/W < m.
- `power-saving-recursion`: Volume-normalized recursion and the power saving: The recurrence F(mf) ≤ (s/W)·F(f) + overhead for cost divided by volume, which, because s/W < m, gives cost O(V·e^τ) with τ < 1 instead of O(V·e) for a parameter e.
- `bit-interface`: Rational matrix interface of the bit network: Using projections P_U onto the labels as rational matrices on the XOR network so that each edge's matrix difference has rank equal to its residual and every route's endpoint difference is the identity Iₘ, giving the address shear on every role.
- `matrix-shear`: Matrix shear by rank-many interchanges: A shear (H, D) ↦ (H + AD, D) by a fixed rational matrix A of rank a is performed with exactly a smaller field interchanges plus O(V) triangular controlled shifts.
- `fixed-tape-schedule`: Fixed-tape depth-first schedule: Running the recursion on a fixed set of tapes by parking the inactive role streams on a stack tape before each child call and restoring them afterward, at O(V) cost per node.
- `power-width-interchange`: Power-width interchange: Interchanging two address chunks of e = mᵏ radix-q digits in O(V·e^τ) time by running the bit network on row-split role streams with shear frames and recursive smaller interchanges.
- `chunk-swap`: Fast address-chunk interchange: The tape procedure that interchanges two disjoint u-bit address fields of any array in O(V·u^τ) time with fixed τ = 1 − 2^{−50}, computing XOR combinations of data along the way.
- `kernel-c`: Two-point kernel C: The Gaussian-dyadic 2×2 kernel C = H·diag(1, i)·H = aI + bX with a = (1 + i)/2, b = (1 − i)/2, satisfying C⁴ = I and H₀ = b·S·C·S, so a layer of H₀ equals a layer of C up to diagonal phases and a scale.
- `phase-interface`: Binary phase interface of the complex network: Using phase frames 𝒞_U = H^{⊗m}·diag(i^{q_U(x)})·H^{⊗m} on the complex network so that each edge's frame change is a product of one translation kernel aI + bX_v per orthonormal residual vector and the whole network yields C^{⊗m} on every role.
- `packed-addition`: Packed selected-bit addition: XORing the selected bits of one address chunk into the corresponding bits of another using eight packed cyclic shifts guarded by a third chunk, then deterministically repairing the small set of addresses where guards overflow.
- `recursive-c-layer`: Recursive C-layer via phase frames: Computing C^{⊗e} on e selected address bits by running the complex network on row-split streams, implementing each edge's frame change by a binary change of basis and one recursive C^{⊗e/m} call per residual vector.
- `simultaneous-layer`: Simultaneous butterfly layer: The procedure applying H₀ on the same bit position in up to d address chunks of an array of polynomial records at once in O(V·d^{λ′}) time, λ′ < 1, evaluating exactly with guard bits and truncating once.
- `cyclic-convolution`: Cyclic convolution: The product of polynomials modulo xˢ − 1 (or of arrays on a product of cyclic groups ℤ/tᵢℤ), where indices add with wraparound.
- `radix-reduction`: Radix-digit reduction: Writing each n-bit input as a polynomial in 2ᵇ with b-bit digits, so the product is recovered from the integer convolution of the digit lists followed by carry propagation.
- `crt-map`: Chinese-remainder convolution map: The Agarwal–Cooley isomorphism ℂ[x]/(x^S − 1) → ⊗ᵢ ℂ[xᵢ]/(xᵢ^{sᵢ} − 1) for pairwise coprime sᵢ, placing the digit list on a product of prime cyclic axes and implemented on tape by triangular controlled shifts and axis moves.
- `dft`: Normalized discrete Fourier transform: The map (F_q u)_k = (1/q) Σⱼ uⱼ e^{−2πijk/q} and its opposite-sign version F_q⁺, extended to several axes by tensor products, which turns cyclic convolution into pointwise products.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of prime length s through one of nearby power-of-two length t by convolving with Gaussian kernels, with well-conditioned resampling maps.
- `synthetic-transform`: Synthetic polynomial transform: The Nussbaumer–Quandalle Fourier transform over ℂ[y]/(yʳ + 1) using powers of y as roots of unity, computed by decimation-in-frequency butterflies and monomial twiddles and leaving outputs in bit-reversed order.
- `bluestein`: Bluestein's chirp identity: The identity QF_t u = ā · (a ∗ (ā · u))/T with chirp a_j = exp(−πi Σ sᵢjᵢ²/tᵢ), which converts the permuted middle Fourier transform into a cyclic convolution.
- `contraction-errors`: Contractions and error accounting: Linear maps of operator norm at most one do not amplify errors, so errors of approximate algorithms for contractions (and bilinear contractions) simply add when composed.
- `resampling-retained`: Resampling with retained permutations: The identity P_s F_s = 2^{2α²} B₀ P_t F_t A, in which the two coordinate permutations of Gaussian resampling are kept inside the transform identity instead of being executed as sorts.
- `source-perm-cancel`: Source permutation cancellation: The identity RF⁺[(RFu)·(RFv)] = (u ∗ v)/S², showing that the source permutation R kept from resampling cancels between the two forward transforms and the opposite transform.
- `transform-layout`: Transform layout and cost: Rearranging the address bits of a multidimensional synthetic transform so that each round's selected bits sit at a common offset in consecutive K-bit chunks, letting every round use the simultaneous butterfly layer.
- `synthetic-convolution`: Ring convolution from the retained layout: Computing normalized cyclic convolution of arrays over ℂ[y]/(yʳ + 1) by two forward synthetic transforms, pointwise products in their retained stored order, and one opposite transform.
- `coefficient-twist`: Coefficient twist: The map x ↦ ζy with ζ = e^{πi/r}, which turns cyclic convolution in the last coordinate into negacyclic multiplication modulo yʳ + 1 and back.
- `tensor-resampling`: Tensor resampling interface: Applying the one-dimensional resampling maps line by line on every axis of a padded power-of-two box, moving axes into position with the fast chunk interchange.
- `parameters`: Size parameters and prime source lengths: The choices b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two box T ≈ 4n/b split into d axes of length r or r/2, distinct odd primes sᵢ just below each tᵢ, and the fixed rational exponents ending in κ = 2^{−182}.
- `source-transform`: Computed source transform: The procedure approximating RF_s on the prime-axis array by composing the Gaussian expansion A, the chirp transform (via twisted ring convolution), the compression B₀, and an exact scale 2^γ.
- `precision-recovery`: Precision analysis and exact recovery: The error bookkeeping showing that after undoing the normalizations S and the digit scales, every recovered convolution coefficient is within 1/2 of the true integer, so rounding and carry propagation give the exact product.
- `cost-accounting`: Cost table and the exponent κ: The accounting that bounds every stage's cost divided by Tp = Θ(n) by a power of p at most 1 − 2κ, so the whole algorithm runs in O(n·(log n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^{1−κ}) time: One deterministic fixed-alphabet, fixed-tape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n·(lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n conjecture in that model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-tm`: Multitape Turing machine
- `binary-representation-of-integers`: Binary representation of integers
- `two-s-complement-representation`: Two's-complement representation
- `bit-order-and-endianness`: Bit order and endianness
- `bitwise-exclusive-or`: Bitwise exclusive or
- `hamming-weight`: Hamming weight
- `logarithms-and-exponent-rules`: Logarithms and exponent rules
- `floor-ceiling-and-rounding`: Floor, ceiling and rounding
- `worst-case-running-time`: Worst-case running time
- `ram-model-of-computation`: RAM model of computation
- `recurrences-and-recursion-trees`: Recurrences and recursion trees
- `geometric-series`: Geometric series
- `telescoping-sums`: Telescoping sums
- `karatsuba-multiplication`: Karatsuba multiplication
- `stacks`: Stacks
- `binary-counter-and-amortized-increment-cost`: Binary counter and amortized increment cost
- `radix-sort-and-stable-sorting`: Radix sort and stable sorting
- `row-major-order-and-matrix-transposition`: Row-major order and matrix transposition
- `directed-graphs`: Directed graphs
- `sets-cartesian-products-and-indicator-vectors`: Sets, Cartesian products and indicator vectors
- `binomial-coefficients`: Binomial coefficients
- `permutations-and-cycle-notation`: Permutations and cycle notation
- `union-bound`: Union bound
- `greatest-common-divisor-and-euclid-s-algorithm`: Greatest common divisor and Euclid's algorithm
- `prime-numbers-and-trial-division`: Prime numbers and trial division
- `chinese-remainder-theorem`: Chinese remainder theorem
- `matrix-operations`: Matrix operations
- `gaussian-elimination`: Gaussian elimination
- `dot-product-and-orthogonality`: Dot product and orthogonality
- `projection-onto-a-subspace`: Projection onto a subspace
- `eigenvalues-of-a-matrix`: Eigenvalues of a matrix
- `complex-conjugate`: Complex conjugate
- `triangle-inequality`: Triangle inequality
- `bernoulli-s-inequality`: Bernoulli's inequality
- `newton-s-method`: Newton's method
- `proof-by-induction`: Proof by induction

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
