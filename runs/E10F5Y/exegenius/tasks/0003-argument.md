# exegenius task 0003-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/E10F5Y` (paths below are relative to it)

Reconstruct the plan of the argument the sources make for the target result, as a tree of steps. Writers of the wiki's pages are given their page's step, and readers are shown where each page fits, so the plan says what each page is for.

- The root is the intention to show the target result. Each `show` step names a `method` that splits its claim into sub-steps, and a `motivation`: why that method suits the claim. Its `children` are the sub-steps, in the order the method takes them. An `infer` step is a single step the sources report: give its `quote`, copied exactly, and no children.
- Read the plan top down, as a reader of the sources would: "we show that", "it suffices to", "the key step is" and section structure mark the steps. Go down to the level the pages need: every page below is either the module that presents one step (`page`) or a concept some step relies on (`from`). Deeper steps of a page's own proof can stop at an `infer` step quoting where the sources carry them out.
- The sources report the plan in order: the infer steps' quotes must appear in the sources in the order of a depth-first walk of the tree (submit checks it). Mark an infer step `deferred` if the sources report it out of order.
- `motivation.source`: `explicit` if the sources state why the method is used (quote them), `recoverable` if a reader could work it out from what they say, `reconstructed` if you supply it. Do not mark a motivation explicit unless you can quote it. Writers are told to give readers every reconstructed motivation, since the sources will not.
- `from`: the concepts a step relies on, as ids: known concepts, or pages that come before the step's page in the reading order below. A step's page is its own `page` or the nearest ancestor's.
- The key step: the step the target result turns on, the construction or estimate that gives the result its strength (where a saving, a bound or a surprise comes from). A reader who follows only one derivation should follow this one. Develop it with `show` steps down to the reasoning the sources give for it, each sub-step quoting where the sources carry it out, rather than stopping at an `infer` step that quotes its result. Where a sub-step concludes from a count, a bound or an equality, state the identity, lemma or definition that makes it hold, and every case the sources treat as an exception to it. Where the sources carry out a construction or estimate in more than one variant, develop each variant the target result uses; where a sub-step concludes a bound on an error, a size or a depth, state the recurrence or chain of estimates that produces the bound. Define each parameter and constant the target result's statement or derivation fixes (a size, a count, a threshold) with the value the sources give it, at the step that first uses it; where the sources establish a sub-step case by case or by a table, give every case and what it contributes.
- `salient`: for a step whose claim has a feature a reader would find striking (a symmetry, a uniformity across cases, a surprising value or bound), that feature. A proof explains a result only relative to such a feature (Lange), so its page is asked to explain why the feature holds. Most steps have none.
- `adds`: symbols a step introduces for its sub-steps, each occurring in the mathematics ($...$) of the claims below it, with a display name, meaning and relation as for concept names.
- The target page presents the root. Give each other page at most one step; a page that presents no step must be in some step's `from`.

## Target

`main-theorem`: Integer multiplication below n log n: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{-182}, using fast address interchange and fast simultaneous butterfly layers inside a Gaussian-resampling, chirp and synthetic-transform reduction.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, counting, induction, primes, gcd), a first algorithms course (divide and conquer, recurrences, sorting, Karatsuba multiplication, schoolbook arithmetic) and complexity (big-O family, single- and multitape Turing machines), together with calculus (exponentials, logarithms, series), linear algebra over the reals and complex numbers, and polynomials. They have not met Fourier transforms or the FFT in depth, finite fields beyond arithmetic mod 2, bilinear forms over arbitrary fields, number-theoretic estimates such as prime density, or any research-level multiplication algorithm; those are what the wiki must explain.

## Pages, in reading order

- `two-point-butterfly`: Two-point butterfly H₀ and the kernel C: The butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) and its Gaussian dyadic relative C = H S H = aI + bX with a=(1+i)/2, b=(1−i)/2, C² = X and H₀ = b S C S, which lets H₀ layers be computed from C layers.
- `multitape-model`: Fixed-tape Turing machine model: The cost model: one fixed finite alphabet and one fixed finite number of one-dimensional tapes, where a step touches one cell per tape and time counts steps.
- `nlogn-multiplier`: Established O(n log n) integer multiplier: The Harvey–van der Hoeven multitape algorithm multiplying N-bit integers in O(N log N), used here only as a black-box subroutine on short records.
- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's 1971 proposal that n log n is the optimal order of growth for multitape multiplication, which a power saving in the log factor refutes.
- `array-layout`: Arrays, address fields and logical volume: Data is stored as a stream in lexicographic address order over a product of fields; the logical volume V counts stored bits and rows are consecutive blocks over a suffix field.
- `gate-network-frames`: Role networks and frames: A fixed linear network of wires (roles) and pointwise gates is run on arrays; assigning each vertex an invertible frame D_v makes the implemented operator D_out S D_in⁻¹, so only changes of frame along edges cost work.
- `elementary-streams`: Elementary stream operations: Linear-time scans on fixed tapes that permute digit values, move one digit, split a stream on a digit, apply a pointwise map to aligned streams and merge, or split whole rows cyclically among W streams.
- `controlled-shifts`: Controlled cyclic shifts and rational scalings: A later target field can be shifted cyclically by an offset computed from earlier control fields, or multiplied by a unit modulo q^b, in linear time by splitting and merging blocks.
- `scratch-restoration`: Restoring arbitrary scratch values: A linear computation that first subtracts the effect of unknown scratch contents, adds in the real contribution, and undoes it, so the target changes correctly and every scratch value is restored whatever it started as.
- `subset-intersection-network`: Three-subset gather and scatter network: A fixed network on banks indexed by triples of 3-subsets whose gather, scatter, copy and side-injection gates have net coefficient depending on intersection size, cancelled by scratch wires, so three stages realize the signed exchange (X, Y) ↦ (−Y, X).
- `nondegenerate-subspaces`: Nondegenerate subspaces and orthogonal residuals: Subspaces of a bilinear space on which the form is nondegenerate, so the space splits as a subspace plus its orthogonal complement; the orthogonal residual of nested subspaces is the complement of the smaller inside the larger.
- `subspace-labels`: Subspace labels and the rank budget: Each gate and terminal of the network gets a nested nondegenerate subspace of an m-dimensional space, so an edge costs its dimension change, and the only decreasing edges are central wires, keeping the total below the wire count times m.
- `rank-saving-recurrence`: Rank saving and the power-saving recurrence: If a network of W wires has total edge rank s < W m, a call at parameter m·f makes s calls on streams of volume V/W at parameter f, so per-volume cost obeys F_k ≤ (s/W) F_{k−1} + O(1) and grows only like e^τ with τ < 1.
- `bit-network-interface`: Bit network as an address shear: Using projection matrices of the labels as frames, the XOR network turns the role exchange into the shear H ← H + D on every role, with total rational edge rank s_b < W_b m.
- `phase-interface`: Binary phase frames: For the complex network with binary labels, the frame C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} makes each edge change a product of one two-point kernel aI + bX_v per residual basis vector, and the whole network equals C^{⊗m} on every role.
- `lower-triangular-factorization`: Lower-triangular factorization of a matrix: Every rational matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones (a Bruhat-type factorization in reversed coordinate order).
- `matrix-shear-cost`: Cost of a rational matrix shear: The address map (H,D) ↦ (H + A D, D) over Z/q^b is performed with exactly rank(A) interchanges of b-digit fields plus linear work, using triangular steps and the trick that three updates turn H+D into a swap.
- `power-width-interchange`: Power-width address interchange: Two chunks of m^k radix-q digits are interchanged by splitting rows into W role streams, running the bit network with each edge shear done by recursive interchanges of chunks of 1/m the width, in O(V e^τ) time on fixed tapes.
- `chunk-interchange`: Fast interchange of address chunks: Two disjoint address chunks of u bits in an array with complete Cartesian address set can be exchanged in O(V u^τ) time for a fixed τ < 1, although the intermediate steps form XOR combinations of the data.
- `packed-selected-bit-addition`: Packed selected-bit addition: An XOR of the same bit position in f chunks of one address range into another is done together by a constant number of cyclic shifts of whole chunk ranges, followed by a deterministic repair of the small explicitly identified set of exceptional addresses.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree below r with y^r = −1, where multiplying by y^a only permutes coefficients and flips some signs, so powers of y act as exact roots of unity.
- `cyclic-convolution`: Cyclic convolution: The convolution of two length-S sequences with indices added modulo S, which is polynomial multiplication in C[x]/(x^S − 1).
- `radix-digit-convolution`: Integer multiplication as digit convolution: Writing each operand in radix 2^b turns the product into a convolution of short digit polynomials whose coefficients are small integers; carries then recover the binary product.
- `discrete-fourier-transform`: Normalized discrete Fourier transform: The map u ↦ (1/q) Σ_j u_j e^{−2πi jk/q} on length-q vectors; it turns cyclic convolution into pointwise product, is inverted by the opposite-sign transform up to scaling, and is a contraction in the maximum norm.
- `multidimensional-transform`: Multidimensional transforms and convolution on several axes: Tensor-product transforms and cyclic convolution on arrays indexed by a product of axes, applied one axis at a time, with the maximum-norm contraction property preserved.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the negacyclic ring in which the roots of unity are powers of y, ω_t = y^{2r/t}, so every twiddle multiplication is a signed shift of a coefficient list (Nussbaumer–Quandalle).
- `bluestein-chirp`: Bluestein chirp identity: A Fourier transform (including its target frequency permutation) equals a pointwise chirp phase, a cyclic convolution with the chirp, and another pointwise chirp phase, so it reduces to cyclic convolution.
- `butterfly-recursion`: Decimation-in-frequency butterflies and bit-reversed frequency order: The transform is computed by log t rounds each pairing entries z_k and z_{k+t/2}, applying the two-point butterfly and a twiddle shift, which leaves frequency j stored at its bit-reversed position; the opposite transform consumes that order.
- `fixed-point-numerics`: Fixed-point complex arithmetic and truncation error: Complex values are stored as pairs of signed integers over a 2^p grid inside the unit disk, truncated toward zero by Q_p; contractions pass errors through unchanged and errors of composed steps add.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: One H₀ butterfly applied at the same bit offset in D ≤ d address chunks at once, computed exactly via the phase network with recursive calls on 1/m of the axes and a single final truncation, in O(V d^{λ'}) time with λ' < 1.
- `transform-layout`: Transform layout and cost: A positional permutation moves selected bits of the d−1 axes to a common offset in K-bit chunks so each transform round is one simultaneous layer, giving a forward and opposite synthetic transform costing O(T p [dK + p K^{τ−1} + ℓ d^{λ'}]).
- `signed-packing`: Signed packing (Kronecker substitution): A product of two disk-grid polynomials is computed exactly by evaluating their integer parts at a large base 2^{4p}, multiplying the resulting integers with the O(N log N) multiplier, and reading centered coefficients back out, then wrapping modulo y^r + 1.
- `ring-convolution`: Convolution from the retained transform layout: Normalized convolution over the negacyclic ring is computed by two forward synthetic transforms, pointwise polynomial products in the retained frequency order, and the opposite transform, with explicit error bound.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's method expressing a Fourier transform of coprime length s through one of a nearby power-of-two length t via Gaussian-weighted contractions A and B₀, with the two coordinate permutations left inside the identity.
- `permutation-cancellation`: Cancellation of the retained source permutation: The coordinate permutation R left inside the resampled transform cancels across two forward transforms, their pointwise product and the opposite transform, giving R F⁺[(R F u)·(R F v)] = u*v/S².
- `tensor-resampling-box`: Tensor resampling on a padded box: The one-dimensional resampling maps are applied line by line along each axis of a zero-padded power-of-two box, with axes exposed by chunk interchanges, giving error below d p² and cost O(d T p^{3/2+δ} α).
- `prime-lengths`: Choosing prime source lengths: Distinct odd primes s_i in (1−2η)t_i < s_i ≤ (1−η)t_i are found by trial division, so their product S fills at least half the padded box while each ratio t_i/s_i leaves the separation resampling needs.
- `size-parameters`: Size parameters of the multiplication: From n set b = ⌈log₂ n⌉, precision p = 6b, number of axes d = ⌊b^ε⌋, chunk width K = ⌊d^c⌋, box size T ≈ n/b, axis lengths t_i ∈ {r/2, r} with r = 2^ℓ, so that Tp = Θ(n) and r exceeds every fixed power of p.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: A cyclic convolution of length S = s_1⋯s_d with pairwise coprime s_i becomes a convolution on the product of cyclic axes of lengths s_i via x ↦ ∏ x_i^{μ_i}, implemented by triangular controlled shifts and axis moves.
- `coefficient-twist`: Phase twist from cyclic to negacyclic: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} maps the cyclic coordinate C[x]/(x^r − 1) isomorphically onto the polynomial ring modulo y^r + 1, so cyclic convolution is computed over the ring and untwisted.
- `source-transform`: Source Fourier transform procedure: The computed transform for a coprime-length source: linewise Gaussian map A, the chirp transform done by complex convolution through the phase twist, linewise map B₀, and an exact 2^γ rescale, approximating R F_s.
- `multiplication-algorithm`: The multiplication algorithm: Split the operands into radix digits, map them by Φ to prime axes, apply the source transform to each, multiply pointwise, apply the opposite transform, rescale by S and 2^{2b+4}, round to integers, undo Φ and propagate carries.
- `exact-recovery`: Precision and exact recovery: Disk-margin and error bookkeeping shows the recovered coefficient error stays below 1/2, so rounding gives the exact integer convolution coefficients and carries give the exact binary product.
- `time-accounting`: Cost table and the saving exponent κ: Dividing each cost by V = Tp, seven dominant terms have powers of p at most 1 − 2κ below one; the smallest margin 2^{-181} fixes κ = 2^{-182}, and any polylog factor is absorbed.
- `main-theorem`: Integer multiplication below n log n: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{-182}, using fast address interchange and fast simultaneous butterfly layers inside a Gaussian-resampling, chirp and synthetic-transform reduction.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine-basics`: Turing machines and tapes
- `binary-integers`: Binary integers
- `modular-arithmetic`: Modular arithmetic
- `linear-algebra-basics`: Matrices, rank and linear maps
- `big-theta-big-omega-and-little-o-notation`: Big-Theta, big-Omega and little-o notation
- `divide-and-conquer-recurrences`: Divide-and-conquer recurrences
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication
- `positional-notation-in-any-radix-and-mixed-radix`: Positional notation in any radix and mixed radix
- `bitwise-operations-xor-and-hamming-weight`: Bitwise operations, XOR and Hamming weight
- `floor-ceiling-and-rounding`: Floor, ceiling and rounding
- `exponential-and-logarithm-functions`: Exponential and logarithm functions
- `convergent-series-and-the-geometric-series`: Convergent series and the geometric series
- `prime-numbers-coprimality-and-trial-division`: Prime numbers, coprimality and trial division
- `extended-euclidean-algorithm`: Extended Euclidean algorithm
- `counting-subsets-and-binomial-coefficients`: Counting subsets and binomial coefficients
- `permutations-and-permutation-matrices`: Permutations and permutation matrices
- `lexicographic-order-and-cartesian-products-of-index-sets`: Lexicographic order and Cartesian products of index sets
- `vector-norms-inner-products-and-orthogonality`: Vector norms, inner products and orthogonality
- `gaussian-elimination`: Gaussian elimination
- `dyadic-rationals-and-binary-fractions`: Dyadic rationals and binary fractions
- `stable-radix-sort-and-counting-sort`: Stable radix sort and counting sort
- `mathematical-induction`: Mathematical induction

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
