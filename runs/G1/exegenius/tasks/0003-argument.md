# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/G1` (paths below are relative to it)

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

`sub-nlogn-multiplication`: Integer multiplication below n log n: A deterministic fixed-tape Turing machine that multiplies n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture by replacing address rearrangement and Fourier layers with faster recursive tape procedures.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: asymptotic analysis and recurrences, discrete mathematics (sets, functions, permutations, modular arithmetic, primes, gcd), a first course in linear algebra (vectors, matrices, rank, bases, subspaces, orthogonality, dot products), complex numbers and polynomial algebra, and basic multitape Turing machine computation including binary arithmetic. They have seen schoolbook multiplication and basic divide-and-conquer, but not the FFT's number-theoretic refinements, abstract algebra beyond rings of polynomials, tensor products, bilinear forms over finite fields, or the analytic number theory used for prime estimates.

## Pages, in reading order

- `nlogn-conjecture`: The n log n conjecture and multiplication history: Schönhage and Strassen conjectured that n log n is the optimal multiplication cost on multitape Turing machines; Schönhage–Strassen, Fürer and Harvey–van der Hoeven gave successively better upper bounds down to O(n log n).
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree below r in which y^r = −1, so multiplying by a power of y shifts the coefficient list with sign changes.
- `fixed-point-arithmetic`: Fixed-point and Gaussian dyadic arithmetic: Complex values stored as signed two's-complement integers times 2^{−p}; additions, halvings and multiplications by i are exact with enough guard bits, and truncation Q_p to the grid has error below √2·2^{−p}.
- `subset-intersection-gates`: Three-element subset gates (copy, gather, scatter, side wires): Fixed linear maps indexed by three-element subsets of {1..100} whose coefficients depend on intersection size; auxiliary side and center wires cancel the unwanted coefficients and are restored afterwards.
- `bank-exchange-network`: Scratch-restoring bank-exchange network: A fixed linear network of wires and gates that, in three stages, exchanges two banks of values with prescribed signs and restores every auxiliary scratch value whatever its initial content.
- `frames-network`: Frames: changing representation along a network: Arrays replace scalars on wires; each vertex has an invertible frame operator D_v, edges apply D_v D_u^{-1}, and pointwise linear gates commute with the common frame, so the whole network acts as D_out S D_in^{-1}.
- `subspace-rank-saving`: Subspace labels and the rank deficit: Nested subspaces of a fixed bilinear space attached to gates and terminals make each edge cost its rank in smaller operations; the total s of these ranks is strictly less than W·m, where W is the wire count and m the label-space dimension.
- `recursive-power-saving`: Recursive power saving: A call at parameter m·f uses s calls at parameter f on streams of volume V/W, so cost per volume obeys F_k ≤ (s/W)F_{k−1} + O(1) with s/W < m, giving cost O(V e^τ) for some fixed τ < 1.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The established O(N log N) multitape algorithm for multiplying N-bit integers, used here only as an ordinary subroutine for short integers.
- `kronecker-packing`: Signed Kronecker packing of polynomial products: Evaluating integer-coefficient polynomials at a large base B_0 packs them into integers so that one large integer multiplication yields all coefficients of the product, with signs handled by centered residues.
- `stream-operations`: Array layout and elementary tape streams: Arrays stored in lexicographic address order on tape, with linear-time scans that permute digit positions, split into aligned streams, apply pointwise maps and merge them back.
- `controlled-shifts`: Controlled cyclic shifts of an address field: A target address field is shifted cyclically by an offset computed from earlier control fields in linear time, which also gives multiplication by fixed units modulo q^b.
- `binary-phase-interface`: Phase frames and the C kernel: Over Gaussian dyadic values, the phase frame changes between binary subspace labels are products of two-point kernels aI + bX_v (a=(1+i)/2, b=(1−i)/2), one per orthonormal residual vector, and telescope to C^{⊗m} on every role.
- `lower-triangular-factorization`: Lower triangular (Bruhat-type) factorization: Every rational matrix A of rank a factors as E_1 Π E_2 with E_1, E_2 invertible lower triangular and Π a partial permutation matrix with a ones.
- `matrix-shear-cost`: Cost of a rational matrix shear: The address map (H,D) ↦ (H + AD, D) of rank a is performed with exactly a interchanges of pairs of b-digit fields plus linear work, by factoring A and using three controlled updates around each swap.
- `address-interchange`: Address-chunk interchange: The first tape procedure: it swaps two disjoint address chunks of u bits in a complete array of volume V in time O(V u^τ) for a fixed τ < 1, internally using XOR combinations of intermediate data yet ending as an exact permutation.
- `packed-selected-bit-addition`: Packed selected-bit addition: Adds (XORs) the same bit position of f address chunks of one field into another, using a few cyclic shifts of whole chunks and a correction of an explicitly bounded set of exceptional addresses.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q} sending q complex values to their q frequency components.
- `synthetic-roots`: Synthetic roots of unity: In the negacyclic ring, powers of y serve as roots of unity ω_t = y^{2r/t}, and multiplying by one is an exact signed shift of the coefficient list with no arithmetic.
- `fft-butterfly`: FFT butterflies (decimation in frequency): The recursive FFT step that pairs entries z_k and z_{k+t/2}, replaces them by their half-sum and half-difference, multiplies one output by a root of unity and recurses on both halves.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The second tape procedure: applies H_0(u,v) = ((u+v)/2,(u−v)/2) to one selected bit in each of up to d address chunks at once on polynomial records, in time O(V d^λ') for fixed λ' < 1, evaluated exactly and truncated once.
- `cyclic-convolution`: Cyclic convolution: The product of two length-q sequences viewed as polynomials modulo x^q − 1, so that indices wrap around cyclically.
- `integer-mult-as-convolution`: Integer multiplication as radix-digit convolution: Splitting each integer into digits in a fixed radix turns the product into a convolution of the digit sequences, whose coefficients are then carried into binary.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a Fourier transform as two pointwise multiplications by a chirp phase around a cyclic convolution with the chirp, so the middle transform (with its target permutation) becomes a convolution.
- `phase-twist`: Coefficient phase twist: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} turns cyclic convolution of length r into convolution modulo y^r + 1 (negative wrap), and untwisting restores the cyclic wrap.
- `convolution-theorem`: Convolution theorem: The Fourier transform turns cyclic convolution into pointwise multiplication (up to normalization), so a convolution costs two forward transforms, a pointwise product and one inverse transform.
- `multidimensional-transform`: Multidimensional (tensor) transform: The Fourier transform on a product of axes, applied as the tensor product of one-dimensional transforms along each axis.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the negacyclic ring (Nussbaumer–Quandalle) that uses powers of y as roots and is computed by butterflies, signed shifts and address rearrangements.
- `crt-axis-map`: Chinese-remainder address map: An isomorphism sending a cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to a convolution on d prime-length cyclic axes, implemented here by triangular controlled shifts.
- `synthetic-transform-layout`: Tape layout of synthetic transforms: A layout placing the selected bits of the participating axes at a common offset in consecutive K-bit chunks so that simultaneous layers and chunk interchanges evaluate the synthetic transform while keeping a fixed frequency order.
- `synthetic-convolution`: Convolution over the polynomial ring: Two forward synthetic transforms, polynomial products of each record by signed packing, and the opposite transform consuming the same stored frequency order give the normalized ring convolution.
- `contraction-error`: Linear contractions and error accumulation: A map that does not increase the maximum-modulus norm; applying contractions to approximate inputs never enlarges the input error, so errors of composed approximations add.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's identity expressing a prime-length Fourier transform through a power-of-two-length one via Gaussian-weighted contractions A and B_0; the two coordinate permutations are left inside the identity rather than sorted.
- `permutation-cancellation`: Cancellation of the retained source permutation: The coordinate permutation retained in the resampling identity cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S².
- `exact-recovery`: Exact recovery by rounding and carries: Scaling out the known normalizations, showing the total coefficient error is below 1/2, rounding to integers and propagating radix carries yields the exact 2n-bit product.
- `prime-axis-lengths`: Prime source lengths near powers of two: Choice of distinct primes s_i slightly below the power-of-two axis lengths t_i (using a prime-interval estimate) so that their product fills a fixed fraction of the padded box while each ratio t_i/s_i leaves room for resampling.
- `parameter-choice`: Parameter choice and time bound: Fixed rational exponents and sizes (p = 6⌈log n⌉, d ≈ p^ε, T ≈ n/log n, κ = 2^{−182}) make every cost row of the table a power of p below 1, so the total is O(n (lg n)^{1−κ}).
- `multiplication-algorithm`: The multiplication algorithm: Digits are placed on prime axes by the CRT map, transformed by Gaussian-resampled, chirped, synthetic transforms, multiplied pointwise, transformed back, rescaled, rounded and carried to give the exact product.
- `sub-nlogn-multiplication`: Integer multiplication below n log n: A deterministic fixed-tape Turing machine that multiplies n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture by replacing address rearrangement and Fourier layers with faster recursive tape procedures.

## Concepts the reader knows

- `big-o-notation`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine-tapes`: Multitape Turing machines
- `logarithms-and-exponents`: Logarithms and exponents
- `floor-and-ceiling-functions`: Floor and ceiling functions
- `binary-and-radix-integer-representation`: Binary and radix integer representation
- `schoolbook-multiplication`: Schoolbook multiplication
- `modular-arithmetic-and-congruences`: Modular arithmetic and congruences
- `primes-gcd-and-coprimality`: Primes, gcd and coprimality
- `sets-functions-bijections-and-permutations`: Sets, functions, bijections and permutations
- `counting-and-binomial-coefficients`: Counting and binomial coefficients
- `xor-and-mod-2-arithmetic`: XOR and mod 2 arithmetic
- `vectors-matrices-and-linear-maps`: Vectors, matrices and linear maps
- `rank-bases-and-subspaces`: Rank, bases and subspaces
- `dot-product-and-orthogonality`: Dot product and orthogonality
- `special-matrices-triangular-diagonal-and-permutation-matrices`: Special matrices: triangular, diagonal and permutation matrices
- `rational-numbers-and-the-number-systems-q-r-c`: Rational numbers and the number systems Q, R, C
- `roots-of-unity`: Roots of unity
- `triangle-inequality-and-absolute-value`: Triangle inequality and absolute value
- `geometric-series-and-recurrences`: Geometric series and recurrences
- `induction-and-proof-by-contradiction`: Induction and proof by contradiction
- `tape-scans-and-constant-factor-simulation-on-turing-machines`: Tape scans and constant-factor simulation on Turing machines
- `schoolbook-and-karatsuba-style-divide-and-conquer-multiplication`: Schoolbook and Karatsuba-style divide-and-conquer multiplication
- `polynomial-evaluation-and-interpolation`: Polynomial evaluation and interpolation
- `newton-iteration-for-reciprocals`: Newton iteration for reciprocals

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
