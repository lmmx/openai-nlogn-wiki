# exegenius task 0046-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/V2` (paths below are relative to it)

Reconstruct the plan of the argument the sources make for the target result, as a tree of steps. Writers of the wiki's pages are given their page's step, and readers are shown where each page fits, so the plan says what each page is for.

- The root is the intention to show the target result. Each `show` step names a `method` that splits its claim into sub-steps, and a `motivation`: why that method suits the claim. Its `children` are the sub-steps, in the order the method takes them. An `infer` step is a single step the sources report: give its `quote`, copied exactly, and no children.
- Read the plan top down, as a reader of the sources would: "we show that", "it suffices to", "the key step is" and section structure mark the steps. Go down to the level the pages need: every page below is either the module that presents one step (`page`) or a concept some step relies on (`from`). Deeper steps of a page's own proof can stop at an `infer` step quoting where the sources carry them out.
- The sources report the plan in order: the infer steps' quotes must appear in the sources in the order of a depth-first walk of the tree (submit checks it). Mark an infer step `deferred` if the sources report it out of order.
- `motivation.source`: `explicit` if the sources state why the method is used (quote them), `recoverable` if a reader could work it out from what they say, `reconstructed` if you supply it. Do not mark a motivation explicit unless you can quote it. Writers are told to give readers every reconstructed motivation, since the sources will not.
- `from`: the concepts a step relies on, as ids: known concepts, or pages that come before the step's page in the reading order below. A step's page is its own `page` or the nearest ancestor's.
- The key step: the step the target result turns on, the construction or estimate that gives the result its strength (where a saving, a bound or a surprise comes from). A reader who follows only one derivation should follow this one. Develop it with `show` steps down to the reasoning the sources give for it, each sub-step quoting where the sources carry it out, rather than stopping at an `infer` step that quotes its result.
- `salient`: for a step whose claim has a feature a reader would find striking (a symmetry, a uniformity across cases, a surprising value or bound), that feature. A proof explains a result only relative to such a feature (Lange), so its page is asked to explain why the feature holds. Most steps have none.
- `adds`: symbols a step introduces for its sub-steps, each occurring in the mathematics ($...$) of the claims below it, with a display name, meaning and relation as for concept names.
- The target page presents the root. Give each other page at most one step; a page that presents no step must be in some step's `from`.

## Target

`main-theorem`: Power-saving integer multiplication theorem: One deterministic multitape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model; it combines fast address interchange, fast simultaneous butterfly layers, and the resampling–chirp–synthetic-convolution reduction.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate computer science student: they have taken programming, data structures, an algorithms course (asymptotic analysis, divide and conquer, sorting), discrete mathematics (sets, functions, induction, modular arithmetic, basic number theory) and an introductory linear algebra and complex numbers course, plus an introductory theory-of-computation course covering Turing machines. They have not met the Fourier transform beyond what the wiki explains, nor rings of polynomials modulo a polynomial, analytic number theory (prime density estimates), finite fields beyond bits, or any research-level complexity results on integer multiplication. Everything specific to the paper's fixed-tape constructions, networks, frames and numerical precision must be explained.

## Pages, in reading order

- `integer-multiplication-problem`: Exact integer multiplication on a multitape Turing machine: Given x#y with x,y n-bit binary strings, output the 2n-bit binary product; cost is the number of steps of one fixed machine with a fixed alphabet and a fixed number of one-dimensional tapes, and lg n = max(⌈log₂ n⌉, 1).
- `optimality-conjecture`: Schönhage–Strassen n log n optimality conjecture: The 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers, which is stated here as an eventual lower bound T_A(n) ≥ c·n lg n for every fixed machine A; the paper refutes it.
- `harvey-hoeven-multiplier`: Established O(n log n) multiplier (Harvey–van der Hoeven): The previously known fixed-tape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short records and never recursively on the improved theorem.
- `polynomial-ring-mod`: Polynomial ring modulo yʳ + 1: The ring of complex polynomials of degree less than r with y^r = −1, where multiplying by a power of y permutes the coefficients with sign changes (a signed shift) and so acts as an isometry in the max coefficient norm.
- `scalar-exchange-network`: Linear exchange network with restored scratch wires: A fixed network of linear gates (copy, gather, scatter, side injection) built on triples of an h-element set that exchanges two banks of values (X,Y) ↦ (−Y,X) in three stages while restoring all scratch wires whatever their initial values.
- `elementary-streams`: Array order and elementary stream scans: Arrays stored in lexicographic order on a tape, with address fields and rows; fixed digit permutations, digit moves, splitting into aligned streams, pointwise maps and merging are done in time linear in the volume with counters and rewinds charged.
- `controlled-cyclic-shifts`: Controlled cyclic shifts and fixed rational scalings: Updating a target address field y ↦ y + a(controls) mod q^b, where the controls precede the target on tape, by splitting each fiber into two pieces and merging in swapped order in linear time; also multiplication by fixed rational units mod q^b.
- `linear-algebra-basics`: Matrix rank, subspaces and orthogonal complements: Vector subspaces, rank and dimension of a matrix, projections onto a subspace along its orthogonal complement, and bilinear forms (nondegenerate when no nonzero vector is orthogonal to the whole space).
- `frames`: Frames: changing array representation along network edges: Replacing each scalar by an array and attaching an invertible linear operator D_v (frame) to each vertex lets pointwise gates commute with the frame, so the net effect on a route is the endpoint operator D_sink D_source^{-1}.
- `tensor-product`: Tensor products of operators and arrays: The Kronecker product of linear maps or index sets, so an operator on several coordinates (columns, axes) acting identically on each is written as a tensor power.
- `subspace-labels-rank-saving`: Nested subspace labels and the total-rank saving: Subspaces of a bilinear space built from triple indicator vectors are attached to gates so adjacent labels are nested; edge cost is the dimension of the orthogonal residual, and the total s over all edges is less than (number of wires) × (space dimension).
- `rational-matrix-interface`: Bit-network rational matrix interface: Assigns rational matrices M_v to gates and terminals of the bit network so that endpoint differences equal the identity and the edge ranks sum to s_b < W_b·m, giving the exponent τ = 1 − 2^{-50} with s/W < m^τ.
- `lower-triangular-factorization`: Lower triangular factorization of a matrix: Every rational m×m matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
- `address-shear-cost`: Cost of a rational matrix shear: The address map (H,D) ↦ (H + AD, D) over Z/q^b for a matrix A of rank a is done with exactly a interchanges of b-digit fields plus linear work, by triangular controlled shifts around each pivot and the three-step swap trick.
- `fixed-tape-recursion-schedule`: Depth-first schedule of recursive calls on fixed tapes: Recursive calls on W role streams are run on a fixed set of tapes by parking inactive streams on a stack, copying the active stream to the child, and restoring on return, at O(V) extra cost per node.
- `power-width-interchange`: Recursive power-width chunk interchange: Splits rows cyclically into W role streams, applies the network with shear frames on each edge (s recursive interchanges of chunks of width e/m, each on volume V/W), giving F_k ≤ (s/W)F_{k−1} + O(1) and cost O(V e^τ), because s/W < m^τ.
- `chunk-interchange`: Fast interchange of address chunks: Exchanging two disjoint equal-width address chunks (p,h,g,d,z) ↦ (p,d,g,h,z) of u bits in O(V u^τ) time, τ < 1, for arbitrary shapes; internally the permutation is a sequence of XOR combinations.
- `packed-selected-bit-addition`: Packed selected-bit addition on one rectangle: XORs the selected bits of several chunks into another chunk with a few whole-chunk cyclic shifts that act as packed single-bit additions away from carry-prone guard values, then repairs the small explicitly identified bad set of addresses by sorting, restoring a third scratch chunk.
- `signed-packing`: Signed packing of polynomial products (Kronecker substitution): Evaluating integer polynomials at B₀ = 2^{4p} to get integers, multiplying them with the established multiplier, and extracting signed coefficients by centered residues, then reducing modulo y^r + 1, to multiply ring elements in O(rp log(rp)).
- `dft`: Normalized discrete Fourier transform: The map sending a length-q vector u to (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q}; the opposite-sign transform F⁺ uses e^{+2πi jk/q}, and each is a contraction in the max-modulus norm.
- `fft-butterfly`: Two-point butterfly and radix-2 fast Fourier transform: The butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) pairs entries half a block apart; a decimation-in-frequency transform of length 2^a applies butterflies and twiddle-factor multiplications over a levels and leaves the output in bit-reversed order.
- `phase-kernel`: Two-point phase kernel C: The 2×2 matrix C = H S H = aI + bX with a = (1+i)/2, b = (1−i)/2, satisfying C² = X, C⁴ = I and H₀ = b·S·C·S, so a butterfly equals a diagonal phase, a C kernel, and another phase.
- `phase-frame-interface`: Binary phase interface of the complex network: Using frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} for binary labels, every edge change is a product of translation kernels aI + bX_v, one per orthonormal residual basis vector, so s_c smaller calls of C^{⊗} suffice and the whole network realizes C^{⊗m} on every role.
- `fixed-point-disk-arithmetic`: Disk-grid fixed-point arithmetic, contractions and error: Complex numbers with real and imaginary parts that are multiples of 2^{−p} in the unit disk, stored as two signed two's-complement words; Q_p truncates toward zero, linear contractions do not increase the max norm, and errors of composed approximations add.
- `guard-width-exactness`: Exact Gaussian dyadic evaluation with guard bits: All intermediate values in one butterfly layer are exact Gaussian dyadics (real and imaginary parts with power-of-two denominators), so extra guard bits of width O(d^{C₁}) bound growth and a single truncation follows the completed contractive layer.
- `simultaneous-butterfly-layer`: Simultaneous normalized butterfly layer: Applies H₀ at once to the same bit position of D ≤ d address chunks of a polynomial-record array via the C-kernel network with phase frames, packed binary basis changes and row splitting among roles, in O(V d^{λ'}) time for a fixed λ' < 1 instead of D whole-array passes, with one final truncation.
- `cyclic-convolution`: Cyclic convolution and the convolution theorem: The convolution f*g on a cyclic group, which the Fourier transform turns into a pointwise product (F(u*v) = S·(Fu)·(Fv) with size normalizations), so convolution can be computed by transform, pointwise multiply, inverse transform.
- `multiplication-by-convolution`: Integer multiplication as convolution of radix digits: Write each operand as a polynomial in 2^b with radix-2^b digit coefficients; the product coefficients are a convolution of digit lists (each below 2³ᵇ), padded so cyclic convolution has no wraparound, and carries recover the integer product.
- `multidimensional-transform`: Multidimensional transform on a tensor of axes: The tensor product F_{q₁}⊗…⊗F_{q_d} of one-dimensional Fourier transforms over d axes, computed one axis (line) at a time, with multidimensional cyclic convolution handled the same way.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the polynomial ring with roots of unity ω_t = y^{2r/t}, so twiddle multiplications are signed shifts; computed by butterflies H₀ and twiddles, leaving outputs in bit-reversed frequency order that is retained through the pointwise product and consumed by the opposite transform.
- `coefficient-twist`: Coefficient twist from cyclic to negacyclic wrap: The isomorphism C[x]/(x^r−1) → C[y]/(y^r+1), x ↦ ζy with ζ = e^{πi/r}, which multiplies coefficient k by ζ^k so the negative wrap of the ring becomes the cyclic wrap after untwisting.
- `crt-address-map`: Chinese-remainder address map to distinct prime axes: An algebra isomorphism x ↦ Π x_i^{μ_i} turning one cyclic convolution of length S = Π s_i (pairwise coprime) into a d-dimensional cyclic convolution on prime axes, implemented as triangular controlled shifts plus axis reordering and zero padding.
- `synthetic-transform-layout`: Transform layout on which parallel layers apply: Places the selected bits of all axes at a common offset of consecutive K-bit chunks using prefix-slot moves and chunk exchanges, so each transform round is one simultaneous butterfly layer; total cost O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]).
- `synthetic-convolution`: Convolution over the polynomial ring from the retained transform layout: Normalized convolution M_r(f,g) = (f*g)/(rM): two forward synthetic transforms, pointwise ring products by signed packing in the retained stored order, and the opposite transform, with error below √2·M(3ℓ+1)·2^{−p}.
- `gaussian-resampling`: Gaussian resampling with permutations left in the transform: Replaces a Fourier transform of length s (coprime to t, s<t) by one of length t via Gaussian-weighted contractions A and B₀, with P_s F_s = 2^{2α²} B₀ P_t F_t A, where the two coordinate permutations P_s, P_t stay inside the formula instead of being sorted separately; applied axis by axis for a tensor.
- `bluestein-chirp`: Bluestein chirp identity: Writes the (permuted) transform Q·F_t as pointwise multiplication by a chirp ā, a cyclic convolution with the chirp a, and another pointwise multiplication by ā, so a transform becomes a normalized cyclic convolution.
- `permutation-cancellation`: Source permutation cancellation: Because the coordinate permutation R commutes with pointwise products and R F⁺ R = F⁺, the retained permutation in R F_s cancels across two forward transforms, a pointwise product and the opposite transform, giving (u*v)/S².
- `parameter-choice`: Parameter choice: precision, dimension, axis lengths and prime source lengths: For input length n, take b = ⌈log₂ n⌉, precision p = 6b, dimension d = ⌊b^ε⌋, chunk K = ⌊d^c⌋, power-of-two axis lengths t_i ∈ {r/2, r} with product T ≈ n/b, and distinct odd primes s_i just below t_i with T/2 < S < T so all resampling hypotheses hold.
- `precision-exact-recovery`: Precision, rounding and carry propagation: Tracks scales (the two factors S and 2^{2b+4}) and disk margins to show the recovered convolution coefficients have error below 1/2, rounds to nearest integers, and propagates radix-2^b carries to output the exact 2n-bit product.
- `multiplication-algorithm`: The multiplication algorithm: digits to transform, pointwise product and back: Convert operands to digit lists on a padded prime-axis box via Φ, apply the source transform (resample, chirp convolution through the twist, resample) to each, multiply pointwise, apply the opposite transform, scale by S and 2^{2b+4}, undo Φ, round and propagate carries.
- `time-bound-accounting`: Time-bound accounting and the exponent κ: Dividing the costs of all stages by Tp = Θ(n) gives a table of normalized costs, each a power of p of at most 1 − 2κ (the minimum margin is 2^{−181} = 2κ with κ = 2^{−182}), so the total is O(n (lg n)^{1−κ}).
- `main-theorem`: Power-saving integer multiplication theorem: One deterministic multitape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model; it combines fast address interchange, fast simultaneous butterfly layers, and the resampling–chirp–synthetic-convolution reduction.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine`: Multitape Turing machine
- `bitwise-xor`: Bitwise XOR and arithmetic mod 2
- `asymptotic-notation-omega-theta-and-little-o`: Asymptotic notation Omega, Theta and little-o
- `logarithms-floors-and-ceilings`: Logarithms, floors and ceilings
- `binary-representation-of-integers`: Binary representation of integers
- `schoolbook-binary-addition-with-carries`: Schoolbook binary addition with carries
- `divide-and-conquer-multiplication-karatsuba-toom-cook`: Divide and conquer multiplication (Karatsuba, Toom-Cook)
- `recurrences-induction-and-geometric-sums`: Recurrences, induction and geometric sums
- `sets-functions-bijections-and-permutations`: Sets, functions, bijections and permutations
- `binomial-coefficients`: Binomial coefficients
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `greatest-common-divisor-and-the-euclidean-algorithm`: Greatest common divisor and the Euclidean algorithm
- `prime-numbers`: Prime numbers
- `chinese-remainder-theorem`: Chinese remainder theorem
- `roots-of-unity`: Roots of unity
- `matrices-matrix-products-and-inverses`: Matrices, matrix products and inverses
- `gaussian-elimination-and-row-operations`: Gaussian elimination and row operations
- `vectors-and-matrices-over-the-two-element-field`: Vectors and matrices over the two-element field
- `vector-norms-and-the-triangle-inequality`: Vector norms and the triangle inequality
- `two-s-complement-and-fixed-width-signed-integers`: Two's complement and fixed-width signed integers
- `stacks-and-queues`: Stacks and queues
- `sorting-and-radix-sort`: Sorting and radix sort
- `binary-counters-and-finite-state-bookkeeping`: Binary counters and finite-state bookkeeping

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

Write the answer to `exegenius/tasks/0046-argument.answer.json`, then run `exegenius submit 0046-argument` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0046-argument`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
