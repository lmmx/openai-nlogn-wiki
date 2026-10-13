# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/P5` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^{1−κ}) time: A deterministic fixed-tape Turing machine multiplies n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ=2^{-182}, disproving the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate computer scientist: comfortable with asymptotic notation, recurrences and divide-and-conquer, binary and two's-complement arithmetic, integer division with remainder, modular arithmetic, primes and coprimality, sets, bijections and functions, basic vector and matrix algebra, polynomials and complex numbers (including roots of unity), and basic multitape Turing machines with linear scans. The reader has seen schoolbook and Karatsuba multiplication and probably an introductory FFT in an algorithms course, but has not studied abstract algebra (rings, groups, tensor products), finite fields beyond bit arithmetic, numerical analysis of rounding, or the specialist theory of fast integer multiplication, so the wiki must explain those.

## Pages, in reading order

- `fixed-point`: Fixed-point grid arrays with precision p: Complex numbers of modulus at most 1 stored as signed two's-complement integers scaled by 2^{-p}, with truncation toward zero after each completed step and error tracked as multiples of 2^{-p}.
- `dyadic-exact`: Exact Gaussian dyadic evaluation of a layer: Intermediate values of a butterfly layer are Gaussian integers over powers of two, computed exactly with enough guard bits, with a single truncation at the end.
- `fixed-tape-model`: Fixed finite-tape Turing machine model: The cost model: one fixed finite alphabet, a fixed finite number of one-dimensional tapes, each step touching one cell per tape, and cost counted in bit operations on n-bit inputs x#y with output the 2n-bit product.
- `nlogn-conjecture`: The n log n conjecture and the history of multiplication: Schönhage and Strassen's 1971 O(n log n log log n) bound with the conjecture that n log n is optimal, followed by Fürer's and others' improvements up to Harvey–van der Hoeven's unconditional O(n log n).
- `hvdh-multiplier`: Established O(n log n) multiplier as a subroutine: The previously known O(N log N) fixed-tape integer multiplier, used as an ordinary black box on short inputs, never recursively invoking the new algorithm.
- `streams`: Array streams, address fields and elementary scans: Arrays are stored in lexicographic address order on tapes with logical volume V bits; splitting, merging, and fixed permutations of digits cost O(V) by linear scans.
- `controlled-shifts`: Controlled shifts and fixed rational scalings: Updating a later address field by an offset computed from earlier fields, or multiplying it by a fixed unit modulo q^b, in linear time using split and merge of consecutive blocks.
- `linear-algebra`: Subspaces, rank and orthogonal complements: Vector subspaces, matrix rank, bilinear forms, orthogonal complements, projections and tensor products, over the rationals or F₂.
- `three-subset-pairing`: Triple indicator vectors and intersection pairings: Indicator vectors of three-element subsets of a 100-element set, whose bilinear pairings give |S∩T| mod 2 over F₂ or |S∩T|−1 over Q, making neighboring triples orthogonal.
- `scalar-exchange-network`: Scalar exchange network with restored scratch wires: A fixed linear network of gates (copy, gather, scatter, side injection) acting on banks X,Y and scratch wires, which sends (X,Y) to (−Y,X) in three stages and restores arbitrary initial scratch values.
- `frames`: Frames and the common-frame identity: Assigning an invertible operator D_v to each vertex so that stored arrays are D_v applied to logical arrays; pointwise gates commute with the common frame, so the network implements D_out S D_in^{-1} with only edge changes D_v D_u^{-1} to pay for.
- `subspace-labels`: Subspace labels and the rank saving s<Wm: Nested nondegenerate subspaces of an m-dimensional space attached to gates and terminals so the total rank of edge changes satisfies s<Wm.
- `power-saving-recursion`: Power saving from a rank-deficit recursion: Because the network makes s<Wm calls on streams of volume V/W, the per-volume cost recurrence F_k ≤ (s/W)F_{k−1}+O(1) with s/W<m^τ gives cost O(e^τ) at width e=m^k, with depth-first scheduling on fixed tapes.
- `bit-network`: Bit network and its shear interface: The F₂ network with W_b wires and rational labels whose endpoint matrices differ by the identity on every input role, giving the address shear H←H+D with s_b<W_b·m.
- `lower-triangular-factorization`: Lower-triangular factorization of a matrix: Every rational matrix A of rank a equals E₁ΠE₂ with E₁,E₂ lower triangular and Π a partial permutation with a ones.
- `address-shear`: Address shear costing rank-many interchanges: The permutation (H,D)↦(H+AD,D) of address fields mod q^b is done with exactly rank(A) field interchanges plus linear work, using triangular factors and controlled shifts.
- `chunk-interchange`: Address-chunk interchange in O(Vu^τ) time: Exchanging two disjoint contiguous u-bit address fields of an array of volume V by XOR combinations of intermediate data, in time O(V u^τ) for a fixed τ<1; the final effect is an exact permutation.
- `packed-selected-bits`: Packed selected-bit addition: Adding corresponding selected bits of address chunks (a binary row addition) via a constant number of whole-chunk cyclic shifts, then repairing an explicitly bounded exceptional set of addresses.
- `ring-mod-yr-plus-1`: Polynomial ring modulo y^r+1: Polynomials with complex coefficients of degree < r where y^r=−1, so multiplying by a power of y permutes coefficients with sign changes (a signed shift) and y supplies roots of unity.
- `signed-packing`: Signed packing of polynomial products: Evaluating polynomials at 2^{4p} (a signed Kronecker substitution) so one product in the ring is four integer products by the established multiplier, then reading centered coefficients back.
- `convolution`: Cyclic convolution: The product rule f*g on a cyclic group (or product of cyclic groups), equal to polynomial multiplication modulo x^S−1.
- `digit-convolution`: Multiplication as radix-digit convolution: Writing both inputs in radix 2^b with q=⌈n/b⌉ digits, the product coefficients are a convolution with capacity below 2^{3b}, and padding to length S avoids wraparound.
- `crt-cyclic-axes`: Chinese-remainder map to prime cyclic axes: Using pairwise coprime lengths s_i, a length-S cyclic convolution becomes convolution on a product of cyclic axes through the map x↦∏x_i^{μ_i}, realized by triangular controlled shifts.
- `phase-twist`: Coefficient twist from cyclic to negacyclic: Multiplying coefficient k by ζ^k with ζ=e^{πi/r} maps C[x]/(x^r−1) isomorphically onto C[y]/(y^r+1) so negative wrap becomes cyclic wrap.
- `exact-recovery`: Exact recovery by rounding and carry propagation: Undoing known scales S and 2^{2b+4}, showing the coefficient error is below 1/2, rounding to integers, and propagating radix-2^b carries to obtain the exact 2n-bit product.
- `dft`: Normalized discrete Fourier transform F_q: Length-q transform with entries averaged over roots of unity; it turns convolution into pointwise multiplication (F(u*v)=S·Fu·Fv) and has inverse F⁺ up to normalization.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's identity expressing a Fourier transform of prime-related length s through a power-of-two length t≥s transform via Gaussian-weighted contractions A and B₀, with a small error N−I.
- `butterfly`: Two-point butterfly H₀ and the radix-two recursion: The map H₀(u,v)=((u+v)/2,(u−v)/2) and its use in the decimation-in-frequency recursion that splits a length-t transform into two half-length ones after a twiddle multiplication.
- `synthetic-transform`: Synthetic polynomial transforms: Fourier transforms over the ring C[y]/(y^r+1) whose roots of unity ω_t=y^{2r/t} are powers of y, so twiddle multiplications are signed shifts; evaluated by radix-two butterfly rounds.
- `bluestein-chirp`: Bluestein chirp identity: A Fourier transform as a pointwise phase multiplication, a cyclic convolution with a chirp array, and another phase multiplication.
- `stored-order`: Retained bit-reversed frequency order: The forward synthetic transform writes outputs in bit-reversed slots; the pointwise product and the opposite-sign transform consume that same order, so no reordering is executed.
- `retained-permutations`: Retaining resampling permutations in the transform: The coordinate permutations of resampling stay inside the transform formula, so the chirp absorbs the target permutation and the source permutation cancels across two forward transforms, a pointwise product and the opposite transform.
- `phase-frames`: Binary phase frames and the two-point kernel C: The complex network with binary labels, frames given by Hadamard-conjugated phases i^{wt(P_U x)}, so each edge is a product of translation kernels aI+bX_v and the endpoints give C⊗…⊗C on every role, where C=H·diag(1,i)·H and H₀=b·S·C·S.
- `simultaneous-layer`: Simultaneous butterfly layer in O(Vd^λ') time: Applying H₀ to the same bit position of D≤d address chunks of a polynomial array at once, via the phase network and recursion on e=mf axes, in time O(V d^λ') instead of D passes.
- `transform-layout`: Synthetic transform layout and cost: Placing the selected bits of participating axes at a common offset in K-bit chunks so that each synthetic transform round uses the simultaneous layer, with total cost O(Tp[dK+pK^{τ−1}+ℓd^{λ'}]).
- `synthetic-convolution`: Convolution from the retained transform layout: Two forward synthetic transforms, a pointwise ring product by signed packing, and the opposite transform give normalized convolution over C[y]/(y^r+1) with error about 3ℓ·M·2^{-p}.
- `size-parameters`: Size parameters and prime source lengths: Choice b=⌈log₂n⌉, p=6b, d≈b^ε, K≈d^c, T≈n/b a power of two, axis lengths r/2 or r, and distinct odd primes s_i just below t_i, so that Tp=Θ(n) and r outgrows every power of p.
- `multiplication-algorithm`: The assembled multiplication algorithm: Digits are placed on prime axes by the CRT map, two source transforms (Gaussian resampling with chirp convolution over the ring via twist, using synthetic convolution) and one opposite transform give the digit convolution, then rescale, round and carry.
- `cost-accounting`: Cost accounting and the exponent κ: Dividing each term by Tp gives powers of p with margins g_i below one; the smallest margin is 2κ with κ=2^{-182}, absorbing any polylog factor.
- `main-theorem`: Integer multiplication in O(n (lg n)^{1−κ}) time: A deterministic fixed-tape Turing machine multiplies n-bit integers exactly in O(n(lg n)^{1−κ}) time with κ=2^{-182}, disproving the n log n optimality conjecture in this model.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `tape-basics`: Basic Turing machines and tapes
- `logarithms-floors-and-ceilings`: Logarithms, floors and ceilings
- `binary-representation-and-integer-arithmetic`: Binary representation and integer arithmetic
- `division-with-remainder`: Division with remainder
- `modular-arithmetic`: Modular arithmetic
- `primes-divisibility-and-coprimality`: Primes, divisibility and coprimality
- `sets-functions-and-permutations`: Sets, functions and permutations
- `matrices-and-linear-maps`: Matrices and linear maps
- `xor-and-arithmetic-over-f₂`: XOR and arithmetic over F₂
- `asymptotic-notation-beyond-big-o`: Asymptotic notation beyond big-O
- `recurrences-and-divide-and-conquer`: Recurrences and divide and conquer
- `schoolbook-and-karatsuba-multiplication`: Schoolbook and Karatsuba multiplication
- `fast-fourier-transform-as-an-algorithm`: Fast Fourier transform as an algorithm
- `inequalities-for-error-bounds`: Inequalities for error bounds
- `lexicographic-order-and-mixed-radix-indices`: Lexicographic order and mixed-radix indices
- `two-s-complement-and-truncation`: Two's-complement and truncation

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
