# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/O2` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-tape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^−182, via radix digits, a CRT map, Gaussian resampling with retained permutations, Bluestein chirps, a phase twist and synthetic transforms accelerated by fast interchanges and simultaneous butterfly layers, disproving the n log n conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, induction, modular arithmetic, gcd, primes, the Chinese remainder theorem, binary representation and XOR), a first linear algebra course (vector spaces, matrices, rank, Gaussian elimination, eigenvalues, mostly over the reals but with arithmetic mod 2 seen in discrete math), single-variable calculus (limits, exponentials and logarithms, geometric series, simple inequalities, Newton's method), and an algorithms and theory sequence (asymptotic notation, recurrences, sorting, binary search, Turing machines and time complexity, schoolbook multiplication with carries). They have not studied fast Fourier transform based multiplication, the Schönhage–Strassen/Harvey–van der Hoeven line of work, polynomial transforms over quotient rings, tensor products, bilinear forms over finite fields, or the extremal set-theory constructions the paper borrows; those are what the wiki explains.

## Pages, in reading order

- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's 1971 proposal that Θ(n log n) is the optimal order of n-bit integer multiplication on multitape Turing machines; disproving it requires one machine with T(n)/(n lg n) → 0.
- `ring-y-r-plus-1`: Polynomial ring ℂ[y]/(y^r + 1): The ring R_r of complex polynomials of degree below r with y^r = −1, where powers of y are 2r-th roots of unity and multiplying by them is a signed cyclic shift of the coefficient list.
- `fixed-tape-model`: Fixed finite-tape machine model and stream operations: The model of one machine with a fixed alphabet and fixed number of tapes, where arrays are stored in lexicographic address order and elementary scans (digit moves, row splits, pointwise maps) cost time linear in the logical volume V of stored bits.
- `gaussian-dyadics`: Gaussian dyadic fixed-point arithmetic: Exact arithmetic on complex numbers whose real and imaginary parts have power-of-two denominators, stored as signed fixed-point words on the p-bit disk grid and truncated toward zero by Q_p.
- `controlled-shifts`: Controlled shifts and rational scalings: A linear-time stream operation that adds to a later address field an offset computed from earlier fields, or multiplies it by a fixed rational unit, modulo q^b, by splitting and re-merging blocks.
- `linear-algebra-bilinear`: Nondegenerate bilinear spaces: A vector space with a symmetric bilinear form having no nonzero vector orthogonal to everything, so each nondegenerate subspace U splits the space as U ⊥ U^⊥ with an orthogonal projection P_U.
- `bank-exchange-network`: Bank-exchange linear network: A fixed linear network of wires (roles) and pointwise gates—copy, gather, scatter, side injection on a schedule of eight rows over three stages—that maps two data banks (X, Y) to (−Y, X) while restoring arbitrary initial scratch values.
- `triple-intersection-construction`: Three-element subset intersection construction: Indexing data by 3-element subsets of a 100-element set so that gather/scatter through central wires yields coefficients depending on |S ∩ T| (mod 2 or minus one), with side wires cancelling unwanted neighbor terms, as in Frankl–Wilson/Alon and index-code decoding.
- `tensor-products`: Tensor products: The tensor product of vector spaces or linear maps, used to build multidimensional transforms, label spaces F^{⊗3}, and operators acting independently on several coordinates.
- `frames`: Frames and the common-frame identity: Assigning each network vertex an invertible operator D_v on wire arrays so that stored data is D_v g; pointwise gates commute with a common frame, so a route from role w to ρ(w) applies only D_sink D_source^{−1} and intermediate frames cancel.
- `subspace-labels`: Subspace labels and orthogonal residuals: Nested nondegenerate subspaces of the m-dimensional space F^{⊗3} attached to gates and terminals; on each edge the orthogonal residual's dimension counts the smaller operations needed for that edge's frame change.
- `address-shears`: Address shears (H, D) ↦ (H + MD, D): Array permutations Φ_M that add a rational matrix M times one address-field vector D to another H modulo q^b; the bit network's rational matrix interface makes the endpoint operator the shear H ← H + D on every role.
- `rank-saving`: Rank saving s < Wm: The decisive inequality that the total number s of smaller calls over all edges (sum of residual dimensions or ranks) is strictly less than the wire count W times the label dimension m.
- `power-saving-recursion`: Volume-normalized recursion: Splitting rows cyclically among W roles makes each of s child calls act on volume V/W, so cost per bit obeys F_k ≤ (s/W)F_{k−1} + O(1), and s/W < m^τ yields a power saving e^τ in the parameter.
- `lower-triangular-factorization`: Lower triangular (Bruhat) factorization: Writing a rank-a rational matrix as E₁ Π E₂ with invertible lower triangular E₁, E₂ and a partial permutation Π with a ones, so a matrix shear costs a field interchanges plus linear-time triangular updates.
- `fast-interchange`: Fast address-chunk interchange in O(V u^τ): The first tape procedure: exchanging two disjoint u-bit address fields of a stored array in O(V u^τ) time, τ = 1 − 2^−50, by recursively applying the bit network with XOR gates and row splits, rather than by data movement alone.
- `packed-selected-bit-addition`: Packed selected-bit addition: A tape operation XORing the selected bits of one address chunk into the corresponding bits of another, using a temporary chunk, whole-chunk cyclic shifts and a sorted correction of a small explicit exceptional set.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πijk/q} and its opposite-sign inverse F_q^+, contractions for the max norm, applied axis by axis on multidimensional arrays.
- `butterfly-h0`: Normalized butterfly H₀: The two-point map H₀(u, v) = ((u+v)/2, (u−v)/2), the radix-two step of a Fourier transform, applied coefficientwise to polynomial records.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer–Quandalle Fourier transforms over arrays of R_r elements using ω_t = y^{2r/t} as roots of unity, computed by radix-two decimation-in-frequency rounds of butterflies and monomial twiddles, with outputs left in bit-reversed stored frequency order.
- `phase-frames`: Binary phase frames: The complex network's frames 𝒞_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} for binary labels U, whose edge changes factor into one two-point kernel C = aI + bX per orthonormal residual vector and telescope to C^{⊗m} on every role.
- `cyclic-convolution`: Cyclic convolution: The product in ℂ[x]/(x^S − 1): coefficient lists are combined with indices added modulo S, and transforms turn it into pointwise multiplication.
- `radix-digit-convolution`: Multiplication by radix-digit convolution: Splitting each n-bit input into radix-2^b digits turns integer multiplication into convolution of short integer coefficient lists followed by carry propagation.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The 2021 deterministic multitape algorithm multiplying N-bit integers in O(N log N) time via Gaussian resampling and Nussbaumer polynomial transforms; here it is both the base of the reduction and an ordinary subroutine.
- `crt-address-map`: Chinese-remainder address map: The Agarwal–Cooley isomorphism x ↦ Π x_i^{μ_i} turning one cyclic convolution of length S = Π s_i (distinct primes s_i near powers of two) into a multidimensional cyclic convolution, implemented on tape by triangular controlled shifts.
- `coefficient-twist`: Coefficient phase twist: The isomorphism x_d ↦ ζy (ζ = e^{πi/r}) turning cyclic convolution along the last axis into negacyclic multiplication in ℂ[y]/(y^r+1), whose negative wrap reproduces the cyclic wrap after untwisting.
- `signed-packing`: Signed packing (Kronecker substitution): Multiplying two polynomial records of R_r by packing their signed fixed-point coefficients into large integers, calling the O(N log N) integer multiplier, and unpacking the exact product.
- `error-accounting`: Disk-grid approximation and error accounting: Each routine approximates a linear contraction on the p-bit disk grid with an error bound in units of 2^−p, and composed errors add because contractions do not amplify input errors.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer in O(V d^λ′): The second tape procedure: applying H₀ on the same bit of up to d address chunks at once in O(V d^λ′) time, λ′ < 1, by recursing through the complex phase network, then converting C^{⊗D} to H₀^{⊗D} with diagonal phases and a dyadic scale before one final truncation.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven identity expressing a Fourier transform of prime length s through one of nearby power-of-two length t, sandwiched between Gaussian-kernel contractions A and B₀ and a power-of-two scale.
- `retained-permutations`: Resampling with retained permutations: Keeping the source and target coordinate permutations R, Q inside the resampling identity R F_s = 2^γ B₀ Q F_t A rather than sorting, so the target permutation is absorbed by the chirp and the source permutation cancels across forward and inverse transforms in a convolution.
- `bluestein-chirp`: Bluestein chirp identity: Writing a (permuted) Fourier transform as pointwise multiplication by a chirp ā, cyclic convolution with the chirp a, and multiplication by ā again, so the middle power-of-two transform becomes a convolution.
- `exact-recovery`: Exact recovery by rounding and carries: Removing known normalizations and digit scales, bounding the total coefficient error strictly below 1/2 so rounding recovers the exact integer convolution, then propagating radix-2^b carries to output the 2n-bit product.
- `synthetic-transform-layout`: Synthetic transform tape layout and cost: Arranging the axes of a multidimensional synthetic transform so that each round's selected bits sit at a common offset in K-bit chunks, letting simultaneous butterfly layers and chunk interchanges compute every round.
- `synthetic-convolution`: Normalized convolution over the polynomial ring: Computing the normalized cyclic convolution of R_r-valued arrays by two forward synthetic transforms kept in their stored frequency order, pointwise signed-packed polynomial products, and the opposite transform consuming that order.
- `parameter-choice`: Parameter choice and cost table: The fixed rational exponents (τ = σ = 1 − 2^−50, λ′ = 1 − 2^−54, c = 2^−56, ε = 2^−75, …) and sizes (b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋) under which every per-bit cost term is at most p^{1−2κ}, giving κ = 2^−182.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-tape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^−182, via radix digits, a CRT map, Gaussian resampling with retained permutations, Bluestein chirps, a phase twist and synthetic transforms accelerated by fast interchanges and simultaneous butterfly layers, disproving the n log n conjecture in this model.

## Concepts the reader knows

- `big-o-notation`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-turing-machine`: Multitape Turing machine
- `binary-representation-of-integers`: Binary representation of integers
- `positional-radix-number-systems`: Positional (radix) number systems
- `schoolbook-multiplication-and-carries`: Schoolbook multiplication and carries
- `two-s-complement-and-signed-integers`: Two's complement and signed integers
- `floor-ceiling-and-rounding`: Floor, ceiling and rounding
- `integer-division-with-remainder`: Integer division with remainder
- `logarithms-and-exponentials`: Logarithms and exponentials
- `theta-omega-and-little-o-notation`: Theta, Omega and little-o notation
- `limits-of-sequences-lim-inf`: Limits of sequences, lim inf
- `geometric-series`: Geometric series
- `bernoulli-s-inequality`: Bernoulli's inequality
- `triangle-inequality-and-absolute-value`: Triangle inequality and absolute value
- `gaussian-function`: Gaussian function
- `newton-s-method`: Newton's method
- `roots-of-unity`: Roots of unity
- `modular-arithmetic`: Modular arithmetic
- `greatest-common-divisor-and-modular-inverses`: Greatest common divisor and modular inverses
- `prime-numbers-and-trial-division`: Prime numbers and trial division
- `chinese-remainder-theorem`: Chinese remainder theorem
- `xor-and-arithmetic-modulo-2`: XOR and arithmetic modulo 2
- `hamming-weight`: Hamming weight
- `sets-subsets-and-cartesian-products`: Sets, subsets and Cartesian products
- `lexicographic-order`: Lexicographic order
- `permutations`: Permutations
- `vector-spaces-subspaces-basis-and-dimension`: Vector spaces, subspaces, basis and dimension
- `linear-maps-and-matrices`: Linear maps and matrices
- `rank-of-a-matrix`: Rank of a matrix
- `invertible-matrices`: Invertible matrices
- `gaussian-elimination`: Gaussian elimination
- `triangular-matrices`: Triangular matrices
- `eigenvalues`: Eigenvalues
- `max-norm`: Max norm
- `mathematical-induction`: Mathematical induction
- `recurrence-relations`: Recurrence relations
- `binary-search`: Binary search
- `stable-sorting-and-radix-sort`: Stable sorting and radix sort
- `binary-counter`: Binary counter
- `deterministic-worst-case-time-complexity`: Deterministic worst-case time complexity
- `cyclic-shift`: Cyclic shift

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
