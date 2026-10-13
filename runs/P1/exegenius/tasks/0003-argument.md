# exegenius task 0003-argument

Project directory: `/home/user/openai-nlogn-wiki/runs/P1` (paths below are relative to it)

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

`integer-multiplication-below-nlogn`: Integer multiplication in O(n (lg n)^(1−κ)) time: The main theorem: one deterministic fixed-alphabet, fixed-tape Turing machine multiplies n-bit integers in O(n(lg n)^{1−κ}) worst-case time, refuting the n log n conjecture, via synthetic transforms accelerated by the interchange and butterfly procedures.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has an undergraduate computer science education: discrete mathematics (sets, functions, induction, summations, recurrences, basic number theory and elementary group/ring/field vocabulary), an algorithms course (recursion, divide and conquer, schoolbook and Karatsuba multiplication, the FFT at the level of the divide-and-conquer recursion, solving recurrences), single-variable calculus (limits, exponentials, logarithms) and one course in linear algebra and complex numbers. They know Turing machines and big-O at an introductory level, but have not studied fast integer multiplication beyond Karatsuba, Schönhage-Strassen or Harvey-van der Hoeven, numerical error analysis, bilinear forms over finite fields, matrix factorizations such as Bruhat decompositions, or tape-level algorithm engineering.

## Pages, in reading order

- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of multiplication cost on multitape Turing machines; the paper refutes any eventual Ω(n log n) lower bound for a fixed machine.
- `convolution`: Convolution and cyclic convolution: The product of two coefficient lists as polynomials; cyclic convolution wraps indices mod a length, so that it is multiplication in C[x]/(x^S−1).
- `polynomial-ring-mod-y-r-plus-1`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree < r with y^r = −1; multiplication by a power of y is a signed shift of the coefficient list.
- `nlogn-multiplier-subroutine`: The established O(n log n) multiplier as a subroutine: Harvey and van der Hoeven's existing O(N log N) integer multiplication, called as an ordinary black box on shorter records (not the improved algorithm).
- `signed-packing`: Signed packing (Kronecker substitution): Evaluating integer-coefficient polynomials at 2^{4p} to turn polynomial products into integer products, with signed carries and centered extraction of coefficients.
- `tape-address-arrays`: Arrays, addresses, rows and volume on tape: Arrays with multi-field addresses stored in lexicographic order on a tape, with address fields, row fields, prefix and suffix, spectator fields and logical volume V in bits.
- `elementary-stream-operations`: Elementary stream operations: Linear-time tape scans: permuting two digit positions, moving a digit, splitting into streams and merging, and splitting whole rows cyclically into W streams.
- `row-splitting`: Row splitting among roles with padding: Distributing whole rows cyclically among the W wire roles, after padding the row count to a multiple of a power of W, so each role stream has volume V/W.
- `modular-arithmetic`: Modular arithmetic and the Chinese remainder theorem: Arithmetic on residues mod q, units, inverses mod q, gcd, and the fact that coprime moduli split a residue ring into a product.
- `controlled-shifts`: Controlled shifts: Updating a later address field by an offset computed from earlier fields (y ↦ y+a mod q^b), or multiplying it by a rational unit, in linear time.
- `linear-algebra-basics`: Matrices, rank, subspaces and orthogonality: Matrices over a field, their rank, subspaces, orthogonal complements under a bilinear form, and tensor products of spaces.
- `linear-network-roles`: Linear network with roles and restored scratch: A fixed network of linear gates on wires (roles) that exchanges two banks of values with signs while restoring every auxiliary (scratch) wire whatever its initial contents.
- `frames`: Frames and edge operators: Invertible operators D_v on a wire's address-indexed array attached to each network vertex; a common frame commutes with pointwise linear gates, so only edges D_v D_u⁻¹ need implementing and the endpoints determine the net operator.
- `triple-subset-gadget`: Three-subset gather, scatter and side-wire gadget: The scalar gadget on three-element subsets of [100]: copy, gather, scatter and side injection with intersection-size coefficients, scheduled in 8 rows so that y_S gains x_S independently of scratch values.
- `subspace-labels-rank-deficit`: Nested subspace labels and rank deficit: Nondegenerate subspaces of a fixed m-dimensional space attached to gates and terminals, nested along edges, so that the total dimension change s over all edges is strictly less than W·m, where W is the wire count.
- `address-shear`: Address shear interface: The endpoint operator of the bit network: fields H, D over a residue ring updated by (H,D) ↦ (H+MD,D), with matrices M at vertices whose differences give rank-many smaller interchanges per edge.
- `triangular-factorization`: Lower triangular factorization and matrix shear cost: Every rational matrix factors as E₁ΠE₂ with E₁, E₂ lower triangular and Π a partial permutation with rank-many ones, so a shear by A costs rank(A) interchanges plus linear work.
- `fixed-tape-recursion`: Depth-first recursion on fixed tapes: Running recursive calls with finitely many tapes by parking inactive role streams on a stack tape, copying the active one to the child, and restoring afterwards, at cost linear in the parent's volume.
- `recursive-power-saving`: Recursive power saving: When a size-mf call uses s calls of size f on streams of volume V/W with s<Wm, the normalized cost satisfies F_k ≤ (s/W)F_{k−1}+O(1), giving cost O(V e^τ) with τ<1 instead of a factor e.
- `address-chunk-interchange`: Fast address-chunk interchange: The first tape procedure: swapping two disjoint u-bit address chunks of an array by recursion on the bit network in O(V u^τ) time for a fixed τ<1, intermediate steps computing XORs but the final effect an exact permutation.
- `packed-selected-bit-addition`: Packed selected-bit addition: XORing corresponding selected bits of two address chunks across many chunks at once, using a temporary third chunk, a few cyclic shifts, and a deterministic repair of a small exceptional set of addresses.
- `fixed-point-disk-grid`: Fixed-point disk grid and truncation: Complex numbers of modulus at most 1 whose real and imaginary parts are multiples of 2^{−p}, stored as signed two's-complement numerators, with Q_p truncating toward zero.
- `guard-bits-dyadic`: Exact Gaussian dyadic arithmetic and guard bits: Intermediate values with power-of-two denominators are kept exact by allocating extra integer and fractional guard bits, and rounded only once after a whole layer.
- `phase-twist`: Phase twist from cyclic to negacyclic: Multiplying coefficient k of the last cyclic axis by ζ^k with ζ=e^{πi/r} turns x^r−1 into y^r+1, so complex cyclic convolution is computed by ring convolution and the untwist.
- `dft`: Discrete Fourier transform and the convolution theorem: The length-q transform (F_q u)_k = (1/q) Σ u_j e^{−2πi jk/q} built from roots of unity; it turns convolution into pointwise product and is inverted by the opposite-sign transform.
- `multidimensional-transform`: Multidimensional transform (tensor product): A transform on an array indexed by several axes, equal to applying the one-dimensional transform along each axis in turn; convolution on a product of cyclic groups is diagonalised by it.
- `fft-butterfly`: Butterfly and FFT recursion: The fast evaluation of a length-t transform by pairing entries z_k and z_{k+t/2}, applying a two-point butterfly, multiplying by twiddle roots and recursing on both halves.
- `synthetic-polynomial-transform`: Synthetic polynomial transform: A multidimensional transform over the ring mod y^r+1 whose roots of unity are powers of y, so twiddle multiplications are signed shifts and only butterflies cost arithmetic.
- `butterfly-and-phase-kernels`: Butterfly kernel H₀ and phase kernel C: The two-point butterfly H₀(u,v)=((u+v)/2,(u−v)/2) and the kernel C=aI+bX with a=(1+i)/2, b=(1−i)/2, related by H₀=b·S·C·S with S=diag(1,i), so a layer of H₀ equals phases times a layer of C.
- `frequency-order-retention`: Retained frequency order: Leaving transform outputs in the bit-reversed order the recursion writes them, so the pointwise product and the opposite transform consume that order without a separate permutation.
- `binary-phase-interface`: Binary phase interface: The complex network with binary labels, in which each edge's frame change is a product of translation kernels aI+bX_v, one per residual basis vector, so that telescoping gives C⊗m on every role.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The second tape procedure: applying H₀ at the same bit position in d address chunks of every record in O(V d^λ') time, evaluated exactly with guard bits and truncated once.
- `synthetic-transform-layout`: Transform layout for parallel layers: The tape layout that places the selected bits of the participating axes at a common offset in consecutive K-bit chunks, using bit moves and chunk interchanges, so each transform round is one simultaneous butterfly layer.
- `contractions-and-error`: Contractions and error accumulation: A linear map is a contraction if it does not increase the maximum-modulus norm; approximate algorithms for contractions compose with errors that add.
- `synthetic-convolution`: Ring convolution from the retained transform layout: Normalized convolution over the ring: two forward synthetic transforms, pointwise ring products by signed packing, then the opposite transform, with error below √2 M(3ℓ+1)2^{−p}.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's identity converting a Fourier transform of prime-ish length s into one of larger length t via Gaussian-weighted maps S and T, with a near-identity correction N.
- `resampling-permutations-retained`: Resampling with the permutations left in the transform: The paper's variant P_s F_s = 2^{2α²} B₀ P_t F_t A that keeps the coordinate permutations in the identity instead of executing two sorts per axis.
- `bluestein-chirp`: Bluestein chirp identity: Rewriting a transform as pointwise chirp phases around a cyclic convolution with a chirp kernel, which here also absorbs the target permutation.
- `permutation-cancellation`: Source permutation cancellation: The retained source permutation R cancels across two forward source transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S².
- `parameter-choice`: Parameter choices and padded box: The sizes p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T in [4n/b,8n/b), r=2^⌈(log₂T)/d⌉ and axis lengths t_i∈{r/2,r}, with α, γ, η and fixed rational exponents.
- `prime-source-lengths`: Prime source lengths: Distinct odd primes s_i in (1−2η)t_i < s_i ≤ (1−η)t_i near each power of two t_i, found by deterministic trial division, so that T/2<S<T and each ratio t_i/s_i leaves enough separation for resampling.
- `integer-as-digit-convolution`: Integer product as radix-digit convolution: Writing both inputs in base 2^b with q digits, the integer product is the convolution of the digit lists; padding to length S exceeds the degree so no wraparound occurs and coefficients stay below 2^{3b}.
- `exact-recovery`: Exact recovery by scaling, rounding and carries: Removing the known normalizations S and 2^{2b+4}, proving the coefficient error is below 1/2, rounding to integers and propagating radix-2^b carries to the exact 2n-bit product.
- `crt-address-map`: Chinese-remainder address map: An algebra isomorphism from cyclic convolution of length S=∏s_i (s_i pairwise coprime) to convolution on the product of cyclic axes, implemented by triangular controlled shifts.
- `source-transform`: Source transform pipeline: The approximate source transform: resample with A along each axis, apply the chirp transform via ring convolution, compress with B₀, and rescale by 2^γ, equal to R F_s.
- `multiplication-algorithm`: The multiplication algorithm: The six steps: form radix digits, apply the address map Φ, compute two source transforms, multiply pointwise, apply the opposite transform, rescale, round and carry.
- `cost-analysis`: Cost analysis and the exponent κ: The table of normalized costs per Tp, each at most p^{1−2κ}, with the smallest margin 2^{−181}=2κ, giving total O(n (lg n)^{1−κ}) for κ=2^{−182}.
- `integer-multiplication-below-nlogn`: Integer multiplication in O(n (lg n)^(1−κ)) time: The main theorem: one deterministic fixed-alphabet, fixed-tape Turing machine multiplies n-bit integers in O(n(lg n)^{1−κ}) worst-case time, refuting the n log n conjecture, via synthetic transforms accelerated by the interchange and butterfly procedures.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `turing-machine-tapes`: Multitape Turing machine
- `binary-representation-and-schoolbook-arithmetic`: Binary representation and schoolbook arithmetic
- `floor-ceiling-and-logarithms`: Floor, ceiling and logarithms
- `exponentials-and-elementary-inequalities`: Exponentials and elementary inequalities
- `summation-telescoping-sums-and-geometric-series`: Summation, telescoping sums and geometric series
- `recurrences-and-the-recursion-tree`: Recurrences and the recursion tree
- `karatsuba-and-classical-multiplication-algorithms`: Karatsuba and classical multiplication algorithms
- `recursion-call-stack-and-subroutines`: Recursion, call stack and subroutines
- `sets-functions-bijections-and-permutations`: Sets, functions, bijections and permutations
- `mathematical-induction-and-proof-techniques`: Mathematical induction and proof techniques
- `prime-numbers-and-trial-division`: Prime numbers and trial division
- `groups-rings-and-fields`: Groups, rings and fields
- `xor-and-arithmetic-over-f-2`: XOR and arithmetic over F_2
- `special-matrices-and-matrix-algebra`: Special matrices and matrix algebra
- `triangle-inequality-and-norm-bounds`: Triangle inequality and norm bounds
- `rational-numbers-and-dyadic-fractions`: Rational numbers and dyadic fractions
- `deterministic-algorithms-and-worst-case-time`: Deterministic algorithms and worst-case time
- `entrywise-operations-on-arrays-and-vectors`: Entrywise operations on arrays and vectors

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
