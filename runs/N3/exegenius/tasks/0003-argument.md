# exegenius task 0003-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N3` (paths below are relative to it)

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

`main-theorem`: Integer multiplication below n log n: There is one deterministic fixed-alphabet multitape Turing machine computing the exact product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, by chaining radix-digit convolution, a CRT address map, Gaussian resampling with retained permutations, Bluestein chirps, a coefficient twist and synthetic transforms accelerated by fast chunk interchanges and simultaneous butterfly layers; this disproves the n log n optimality conjecture in that model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science degree: discrete mathematics (sets, subsets and binomial coefficients, induction, modular arithmetic, gcd and the Chinese remainder theorem, primes), a first course in linear algebra (matrices, Gaussian elimination, rank, dot products, possibly over GF(2)), calculus (exponentials, logarithms, Newton's method, simple inequalities), and algorithms and computation theory (asymptotic notation, recurrences and geometric sums, sorting including radix sort, binary search, schoolbook and Karatsuba multiplication, amortized binary counters, Turing machines and worst-case running time). They know binary and two's-complement representation of integers and XOR, but have not studied abstract algebra beyond what these courses use, the fast Fourier transform in depth, quotient polynomial rings, or the research literature on fast integer multiplication.

## Pages, in reading order

- `integer-multiplication-problem`: Exact integer multiplication on a multitape machine: The task of reading x#y for two n-bit strings and writing the exact 2n-bit binary product, with cost measured as worst-case steps T_A(n) of one fixed multitape machine A and lg n = max{⌈log₂ n⌉, 1}.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The previously established fixed-tape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short records, never recursively on the new theorem.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: The ring 𝓡_r = C[y]/(y^r + 1) with r a power of two, where multiplying by a power of y is a signed cyclic shift of the coefficient list and the wrap is negacyclic.
- `normalized-butterfly`: Normalized butterfly H₀: The two-point map H₀(u, v) = ((u+v)/2, (u−v)/2), a contraction applied coefficientwise on polynomial records along one address bit; it is the arithmetic step of each radix-two transform level.
- `gaussian-dyadics`: Gaussian dyadic numbers and fixed-point grids: Complex numbers in Z[i, 1/2], whose real and imaginary parts have power-of-two denominators, stored as fixed-point two's-complement words on the grid 2^{−p}Z[i] and truncated toward zero by Q_p.
- `signed-packing`: Signed Kronecker packing: Multiplying two polynomials of 𝓡_r with fixed-point Gaussian coefficients by packing their signed integer numerators into large integers, multiplying with the O(N log N) multiplier, and unpacking and negacyclically reducing.
- `nlogn-conjecture`: n log n optimality conjecture: Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers, i.e. that every multiplication machine eventually needs time at least c·n lg n.
- `array-layout`: Lexicographic array layout and logical volume: Arrays on address sets [a₁]×…×[a_t] stored in lexicographic order with implicit addresses, address permutations acting on entry positions, rows as contiguous suffix blocks, and V the number of stored data bits.
- `elementary-streams`: Elementary stream operations: Linear-time O(V) tape scans that permute or move single radix digits of addresses, split and merge streams on a digit, and distribute whole rows cyclically among W role streams.
- `controlled-shifts`: Controlled shifts and rational scalings: Linear-time updates y ↦ y + a(controls) mod q^b of an address field by an offset computed from earlier fields, and multiplication of the field by fixed rational units, implemented by splitting and re-merging blocks.
- `address-shear`: Address shear: The array permutation Φ_M moving the entry at address (H, D) to (H + MD, D), where H and D are two chunks viewed as vectors of m fields over Z/q^b; the shear H ← H + D plus two linear-cost updates gives an interchange.
- `linear-algebra`: Linear maps, subspaces and rank: Matrices over a field, their rank, invertibility, subspaces, dimension and tensor products of vector spaces.
- `lower-triangular-factorization`: Lower triangular factorization: The factorization A = E₁ Π E₂ of any rational matrix of rank a into invertible lower triangular factors and a partial permutation Π with a ones (a reversed Bruhat factorization, after Grigor'ev).
- `linear-network`: Linear network with roles and scratch wires: A fixed circuit of wires carrying scalars and gates applying fixed linear maps to some wires, where each wire's fixed place is its role and auxiliary scratch wires may start with arbitrary values.
- `frames`: Frames and the common-frame identity: Invertible operators D_v chosen at each source, gate and sink so that the stored array is D_v applied to the logical array; because a common frame commutes with a pointwise gate, the network applies D_out S D_in^{−1} and intermediate frames cancel.
- `scratch-restoration`: Restoring arbitrary scratch values: The schedule that first subtracts the effect of the current scratch values, then adds data to scratch, applies its effect, and finally undoes the scratch updates, so the net effect is independent of the scratch's initial contents and every scratch value is restored.
- `bilinear-forms`: Nondegenerate bilinear forms and orthogonal residuals: Symmetric bilinear forms with no nonzero vector orthogonal to everything; for nested nondegenerate subspaces U ⊂ V the orthogonal residual is the complement of U inside V, of dimension dim V − dim U.
- `triple-intersection`: Triple-intersection pairings: Indicator vectors of the 3-element subsets of a 100-element set, whose pairings give |S∩T| − 1 under a rational form or |S∩T| mod 2 over F₂, so that neighboring triples have orthogonal lines (after Frankl–Wilson and Alon).
- `bank-exchange`: Three-stage bank exchange: The scalar network built from copy, gather, scatter and side-injection gates on triples which, in three stages, maps the two banks (X_a, Y_a) to (−Y_a, X_a) while restoring every auxiliary value.
- `subspace-labels`: Nested subspace labels and rank budget: An assignment of nondegenerate subspaces of the m-dimensional space F^{⊗3} to the gates and terminals of the network, nested along every edge, whose total dimension change s is strictly less than the number of wires times m.
- `rank-deficit-recursion`: Recursive saving from s < Wm: The volume-normalized recurrence F_k ≤ (s/W)F_{k−1} + O(1): a call at parameter mf makes s calls at parameter f on streams of volume V/W, so s/W < m^τ yields cost O(V e^τ) with τ = 1 − 2^{−50} < 1.
- `rational-shear-interface`: Rational shear interface of the bit network: Assigning projection matrices P_U to the bit network's labels so that every routed role sees the endpoint shear I_m, while the edge differences have total rational rank s_b < W_b m.
- `phase-frames`: Binary phase frames: Frames 𝓒_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} for binary labels U, whose change along an edge is a product of one two-point kernel C_v = aI + bX_v per orthonormal residual vector, telescoping to C^{⊗m} on every role.
- `matrix-shear-cost`: Cost of a rational matrix shear: A shear (H, D) ↦ (H + AD, D) by a rational matrix of rank a is performed with exactly a interchanges of field pairs plus O(V) triangular work.
- `power-width-interchange`: Power-width interchange recursion: The recursive procedure interchanging two chunks of e = m^k radix-q digits by splitting rows among the W roles, applying each edge shear via smaller interchanges, and running the XOR gates pointwise, in O(V e^τ) time with a depth-first fixed-tape schedule.
- `fast-chunk-interchange`: Fast address-chunk interchange: The procedure exchanging two disjoint u-bit address fields of an array in O(V u^τ) time for a fixed τ < 1, computing XOR combinations of data along the way though its final effect is an exact permutation.
- `packed-selected-bit-addition`: Packed selected-bit addition: A procedure that XORs selected bits of one address chunk into corresponding bits of another, using a third chunk as restored scratch, by eight cyclic rotations of whole chunk ranges followed by deterministic sorting repair of a small exceptional set of addresses.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀ on the same bit position of up to d address chunks at once in O(V d^{λ'}) time with λ' < 1, by recursing through the complex network's phase frames, packed bit changes and an exact Gaussian-dyadic evaluation with one final truncation.
- `discrete-fourier-transform`: Normalized discrete Fourier transform: The map (F_q u)_k = (1/q) Σ_j u_j e^{−2πijk/q} (and its opposite-sign version F_q^+), a contraction in the max-modulus norm; tensor products F_q over several axes give multidimensional transforms.
- `synthetic-transform`: Synthetic polynomial transform: Nussbaumer's transform F_t^± over C[y]/(y^r+1) using ω_t = y^{2r/t} as root of unity, computed by decimation-in-frequency levels of butterflies and signed shifts, with outputs stored in bit-reversed frequency order.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of coprime length s through one of power-of-two length t, using Gaussian-weighted resampling maps A and B₀ that are contractions computable to precision p.
- `no-sort-resampling`: Resampling with retained permutations: The form P_s F_s = 2^{2α²} B₀ P_t F_t A of Gaussian resampling, and its tensor version R F_s = 2^γ 𝓑₀ Q F_t 𝓐, in which the source and target coordinate permutations stay inside the transform formula instead of being executed as sorts.
- `transform-layout`: Transform layout on K-bit chunks: The tape layout placing the selected address bits of all participating axes at a common offset in consecutive K-bit chunks, with polynomial coefficients in a contiguous suffix, so that each transform round is one simultaneous layer.
- `cyclic-convolution`: Cyclic convolution: The product in C[x]/(x^S − 1), or its multidimensional analogue on a product of cyclic axes, which Fourier transforms turn into pointwise multiplication.
- `radix-digit-convolution`: Radix-digit reduction to convolution: Splitting each n-bit input into q = ⌈n/b⌉ digits in base 2^b so that the product's digits are the convolution of the two digit lists, bounded below 2^{3b}, followed by carry propagation.
- `crt-address-map`: Chinese-remainder address map: The algebra isomorphism x ↦ Π x_i^{μ_i} from C[x]/(x^S−1) to the product of cyclic axes of pairwise coprime prime lengths s_i, which preserves convolution and is implemented as triangular controlled shifts.
- `bluestein-chirp`: Bluestein's chirp identity: The identity Q F_t u = ā · (a * (ā · u))/T with chirp a_j = exp(−πi Σ s_i j_i²/t_i), converting the middle transform together with its target permutation into a normalized cyclic convolution and two pointwise phase multiplications.
- `coefficient-twist`: Coefficient twist: The isomorphism x_d ↦ ζy with ζ = e^{πi/r} from C[x_d]/(x_d^r − 1) to C[y]/(y^r + 1), which turns the last cyclic coordinate into a negacyclic polynomial whose wrap recovers the cyclic wrap after untwisting.
- `synthetic-convolution`: Normalized convolution over the polynomial ring: Computing 𝓜_r(f, g) = (f*g)/(rM) for arrays over 𝓡_r by two forward synthetic transforms kept in the same stored frequency order, packed pointwise ring products, and the opposite transform consuming that order.
- `source-permutation-cancellation`: Source permutation cancellation: The identity (R F_s^+)[(R F_s u)·(R F_s v)] = (u*v)/S², showing that the source permutation R retained in the forward transforms cancels against the opposite-sign transform, so convolution needs no sort.
- `exact-recovery`: Error below 1/2 and exact recovery: The precision argument showing the recovered convolution coefficients are within less than 1/2 of the true integers, so rounding, undoing the CRT map and propagating radix-2^b carries gives the exact 2n-bit product.
- `parameter-choice`: Parameter choice and cost table: The setting b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two box T ≈ 4n/b, prime axis lengths s_i near t_i, and fixed rationals τ, λ', ε, κ = 2^{−182}, under which every normalized cost is at most p^{1−2κ}.
- `main-theorem`: Integer multiplication below n log n: There is one deterministic fixed-alphabet multitape Turing machine computing the exact product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, by chaining radix-digit convolution, a CRT address map, Gaussian resampling with retained permutations, Bluestein chirps, a coefficient twist and synthetic transforms accelerated by fast chunk interchanges and simultaneous butterfly layers; this disproves the n log n optimality conjecture in that model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-turing-machine`: Multitape Turing machine
- `binary-representation-of-integers`: Binary representation of integers
- `positional-number-systems-with-a-general-radix`: Positional number systems with a general radix
- `two-s-complement`: Two's complement
- `binary-addition-with-carry-propagation`: Binary addition with carry propagation
- `schoolbook-multiplication`: Schoolbook multiplication
- `karatsuba-multiplication`: Karatsuba multiplication
- `integer-division-with-remainder`: Integer division with remainder
- `floor-and-ceiling`: Floor and ceiling
- `logarithms-and-exponentials`: Logarithms and exponentials
- `asymptotic-notation-beyond-big-o`: Asymptotic notation beyond big-O
- `worst-case-running-time`: Worst-case running time
- `deterministic-computation`: Deterministic computation
- `polynomial-time-and-polylogarithmic-cost`: Polynomial time and polylogarithmic cost
- `recurrence-relations`: Recurrence relations
- `geometric-series`: Geometric series
- `mathematical-induction`: Mathematical induction
- `sets-subsets-and-cartesian-products`: Sets, subsets and Cartesian products
- `binomial-coefficients`: Binomial coefficients
- `permutations`: Permutations
- `lexicographic-order`: Lexicographic order
- `matrix-transposition`: Matrix transposition
- `modular-arithmetic`: Modular arithmetic
- `greatest-common-divisor-and-the-extended-euclidean-algorithm`: Greatest common divisor and the extended Euclidean algorithm
- `prime-numbers-and-trial-division`: Prime numbers and trial division
- `chinese-remainder-theorem`: Chinese remainder theorem
- `exclusive-or-and-arithmetic-modulo-2`: Exclusive or and arithmetic modulo 2
- `hamming-weight`: Hamming weight
- `gaussian-elimination`: Gaussian elimination
- `dot-product-and-orthogonality`: Dot product and orthogonality
- `special-matrices`: Special matrices
- `triangle-inequality`: Triangle inequality
- `bernoulli-s-inequality`: Bernoulli's inequality
- `newton-s-method`: Newton's method
- `binary-search`: Binary search
- `radix-sort-and-stable-sorting`: Radix sort and stable sorting
- `amortized-cost-of-a-binary-counter`: Amortized cost of a binary counter
- `stacks`: Stacks
- `fixed-point-binary-numbers`: Fixed-point binary numbers

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
