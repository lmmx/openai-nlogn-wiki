# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/G4` (paths below are relative to it)

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

`sub-nlogn-multiplication`: Sub-n log n integer multiplication: A deterministic multitape Turing machine multiplies two n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in that model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has done an undergraduate computer science degree: discrete mathematics (modular arithmetic, primes and gcd, sets, induction, recurrences and asymptotics), basic linear algebra over the reals and complex numbers (matrices, inverses, norms), polynomials and complex roots of unity, and algorithms including divide and conquer and Karatsuba multiplication. On the machine side they know basic single- and multi-tape Turing machines and the idea of counting steps. They have not studied the Fourier transform, FFT-based multiplication, Schonhage-Strassen, Harvey-van der Hoeven, numerical error analysis, abstract algebra beyond rings of residues, finite-field linear algebra, or any lower-bound or advanced tape-algorithm technique, so those must be explained.

## Pages, in reading order

- `convolution`: Convolution: The product of two coefficient lists, cyclic when indices wrap around modulo the length, equal to polynomial multiplication modulo x^S − 1.
- `recursive-power-saving`: Recursive power saving from a rank deficit: If a call at parameter mf is made from s calls at parameter f on streams of volume V/W with s < Wm, the normalized cost grows like m^τ per level with τ < 1.
- `fixed-tape-model`: Fixed-tape Turing machine model: The model where one machine has a fixed finite alphabet and a fixed finite number of one-dimensional tapes, each step touching one cell per tape, so time counts head movement as well as arithmetic.
- `nlogn-multiplier`: Established O(n log n) integer multiplier: The Harvey–van der Hoeven fixed-tape multiplier with cost O(N log N) on N-bit inputs, used only as an ordinary subroutine on short records.
- `elementary-stream-ops`: Elementary stream operations on tape arrays: Linear-time scans on an array stored in lexicographic order: swapping or moving one digit, splitting into streams by a digit or cyclically by rows, applying a pointwise map, and merging back.
- `controlled-shift`: Controlled shifts and rational scalings: An O(V) tape operation that adds an offset computed from earlier fields to a later field modulo q^b (a cyclic shift), or multiplies it by a fixed rational unit.
- `linear-subspaces`: Subspaces, rank and orthogonal complements: Linear algebra over Q or F_2: subspaces, matrix rank, bilinear forms, orthogonal complements and projections.
- `frames-on-arrays`: Frames on pointwise linear networks: Replacing scalars on wires by arrays and assigning each gate an invertible frame operator that commutes with the gate, so edges only change representation and the endpoint operators telescope.
- `exchange-network`: Subset-intersection exchange network: A fixed linear network of copy, gather, scatter and side wires indexed by three-element subsets that swaps two banks X and Y with a sign and restores arbitrary scratch values.
- `subspace-labels`: Subspace labels and the rank budget: Nested nondegenerate subspaces attached to gates so each edge's dimension change counts the smaller operations needed, with total dimension lost small enough to give a strict deficit.
- `bit-network-interface`: Bit network shear interface: The bit version of the network with rational matrices M_v at gates such that the endpoint difference is the identity, i.e. the shear H ← H + D, with rank sum s_b < W_b m.
- `triangular-factorization`: Lower triangular (Bruhat-type) factorization: Every rational matrix A of rank a factors as E_1 Π E_2 with lower triangular invertible E_1, E_2 and a partial permutation Π with a ones.
- `matrix-shear`: Cost of a rational matrix shear: The map (H,D) ↦ (H + AD, D) over Z/q^b costs exactly rank(A) interchanges of b-digit fields plus O(V) other work.
- `power-width-interchange`: Power-width address interchange: Swapping two chunks of m^k digits by running the bit network with matrix shears as edges, each edge recursing into smaller interchanges, in time O(V e^τ).
- `chunk-interchange`: Fast chunk interchange: Exchanging two equal-width address fields of u bits in an arbitrary array in O(V u^τ) time for a fixed τ < 1, even though intermediate steps XOR data together.
- `packed-selected-bit-addition`: Packed selected-bit addition: Adding corresponding selected bits of two address chunks (a binary row addition) by a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small exceptional address set.
- `synthetic-ring`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree below r with y^r = −1, where multiplying by a power of y is a signed shift of the coefficient list.
- `fixed-point-precision`: Fixed-point disk arithmetic and truncation error: Storing complex numbers of modulus at most 1 as signed binary numerators over 2^p, truncating toward zero, and tracking how contractions and bilinear maps propagate the errors.
- `signed-packing`: Signed packing of polynomial products: Kronecker substitution: evaluating ring polynomials at 2^{4p} to multiply them with the integer multiplier, then reading coefficients back by centered residues.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ u_j e^{−2πijk/q}, which turns convolution into pointwise multiplication.
- `fft-butterfly`: Radix-2 butterflies and FFT: Computing a power-of-two transform by repeated two-point butterflies (u,v) ↦ ((u+v)/2,(u−v)/2) followed by twiddle multiplications and smaller transforms (decimation in frequency).
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform whose roots of unity are ω_t = y^{2r/t} in the ring modulo y^r + 1, so twiddles are signed shifts, computed by butterfly rounds with outputs left in bit-reversed order.
- `chirp-identity`: Bluestein chirp identity: Writing a Fourier transform (with its target permutation) as a pointwise chirp phase, a cyclic convolution with the chirp, and another chirp phase.
- `phase-kernel-c`: Two-point kernel C and phase frames: The matrix C = H S H = aI + bX with C^2 = X and H_0 = b S C S, so a butterfly layer is a phase-conjugated tensor power of C.
- `complex-phase-network`: Complex phase network: The complex-scalar version of the exchange network with binary labels whose phase frames i^{wt(Px)} reduce to translation kernels aI + bX_v, giving C^{⊗m} on every role with s_c < W_c m.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H_0 to the same bit position in up to d address chunks at once, exactly in dyadic arithmetic and truncating once, in O(V d^λ') time for λ' < 1.
- `synthetic-transform-layout`: Synthetic transform layout and cost: Placing the selected bits of all axes at a common offset in K-bit chunks so each transform round is a simultaneous layer, with the output frequency order retained for reuse.
- `synthetic-convolution`: Convolution from the retained transform layout: Normalized convolution over the polynomial ring by two forward synthetic transforms, pointwise ring products via signed packing, and the opposite transform consuming the same stored order.
- `gaussian-resampling`: Gaussian resampling: Relating a Fourier transform of coprime length s to one of larger power-of-two length t via Gaussian-weighted contractions A and B_0, as P_sF_s = 2^{2α²} B_0 P_t F_t A.
- `permutation-cancellation`: Source permutation cancellation: The coordinate permutation retained from resampling cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S².
- `tensor-resampling`: Multidimensional resampling on a padded box: Applying the one-dimensional resampling maps along each axis of the padded power-of-two box, exposing each axis by chunk interchanges, with permutations left inside the transform.
- `radix-digit-convolution`: Integer multiplication as digit convolution: Writing each n-bit integer as a polynomial in 2^b with digits of b bits, so the integer product is a convolution of digit lists followed by carry propagation.
- `exact-recovery`: Exact recovery of the integer product: Showing the accumulated numerical error on the recovered coefficients is below 1/2, rounding to integers, and propagating radix carries to the exact 2n-bit product.
- `crt-axis-map`: Chinese-remainder axis map: Mapping a cyclic convolution of length S = ∏ s_i with pairwise coprime s_i to a multidimensional cyclic convolution via x ↦ ∏ x_i^{μ_i}, implemented by triangular controlled shifts and axis moves.
- `parameter-choices`: Parameter choices: Choosing b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two axis lengths t_i near r and distinct primes s_i just below them, so Tp = Θ(n) and all hypotheses hold.
- `convolution-twist`: Coefficient twist to the negacyclic ring: The map x_d ↦ ζy with ζ = e^{πi/r} that turns cyclic convolution in the last coordinate into convolution modulo y^r + 1, so complex cyclic convolution reduces to the synthetic one.
- `multiplication-algorithm`: The multiplication algorithm: Digit polynomials are mapped by the CRT map to prime axes, transformed by resampling plus chirp-convolution (via the twist and synthetic convolution), multiplied pointwise, inverse transformed, rescaled, rounded and carried.
- `cost-accounting`: Complete time bound: Summing the normalized costs of layouts, butterfly rounds, resampling, chirps and packed products, each at most p^{1−2κ}, to get O(n (log n)^{1−κ}).
- `sub-nlogn-multiplication`: Sub-n log n integer multiplication: A deterministic multitape Turing machine multiplies two n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in that model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomial`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine`: Turing machines and tapes
- `modular-arithmetic-and-residue-rings`: Modular arithmetic and residue rings
- `primes-coprimality-and-the-euclidean-algorithm`: Primes, coprimality and the Euclidean algorithm
- `positional-radix-number-representation`: Positional (radix) number representation
- `signed-binary-numbers-and-rounding`: Signed binary numbers and rounding
- `dyadic-rationals`: Dyadic rationals
- `bitwise-operations-and-hamming-weight`: Bitwise operations and Hamming weight
- `permutations-and-bijections`: Permutations and bijections
- `lexicographic-order-and-multi-index-addressing`: Lexicographic order and multi-index addressing
- `matrix-algebra`: Matrix algebra
- `vector-norms-and-the-triangle-inequality`: Vector norms and the triangle inequality
- `logarithms-exponentials-and-floor-ceiling-in-analysis`: Logarithms, exponentials and floor/ceiling in analysis
- `theta-omega-and-little-o-notation`: Theta, Omega and little-o notation
- `summations-and-geometric-series`: Summations and geometric series
- `recurrence-relations-and-divide-and-conquer`: Recurrence relations and divide and conquer
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication
- `stacks-and-call-stacks`: Stacks and call stacks
- `pointwise-operations-on-lists-and-vectors`: Pointwise operations on lists and vectors
- `sets-subsets-and-counting`: Sets, subsets and counting
- `mathematical-induction-and-proof-by-contradiction`: Mathematical induction and proof by contradiction
- `euler-s-formula-and-complex-exponentials`: Euler's formula and complex exponentials

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
