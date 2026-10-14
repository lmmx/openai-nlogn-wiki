# exegenius task 0045-argument

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e4/V3` (paths below are relative to it)

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

`main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A single deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ=2^{-182}, refuting the n log n optimality conjecture in this model; it works by fast address interchanges and fast simultaneous butterfly layers inside a Gaussian-resampling/Bluestein/synthetic-transform reduction.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate computer scientist: fluent with big-O and basic algorithm analysis (recurrences, divide and conquer, sorting and merging, schoolbook multiplication), discrete mathematics (sets, binomial coefficients, permutations, modular arithmetic, primes, gcd), and introductory linear algebra and complex numbers including roots of unity and polynomial arithmetic. They have seen single-tape and multitape Turing machines and tapes as a cost model, but not the discrete Fourier transform, FFT, fast integer multiplication, abstract algebra beyond residues, number-theoretic estimates such as the prime number theorem, or any research-level multiplication technique.

## Pages, in reading order

- `history`: Integer multiplication complexity and the n log n conjecture: Schönhage–Strassen gave O(n log n log log n) on multitape Turing machines and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n), which this paper's algorithm beats.
- `stream-ops`: Arrays on tape and elementary stream operations: An array with a product address set is stored in lexicographic order on tape; splitting on a digit, merging, moving a digit and splitting whole rows cyclically into streams each cost O(V) for stored volume V.
- `controlled-shift`: Controlled cyclic shifts and fixed rational scalings: Updating a later address field y by y+a(controls) mod q^b, or multiplying it by a fixed rational unit, costs O(V) on tape by splitting each fibre in two pieces and merging them in swapped order.
- `linear-algebra`: Subspaces, rank, orthogonal complements and bilinear forms: Basic linear algebra over Q or F₂: subspaces, rank of a matrix, a nondegenerate symmetric bilinear form, orthogonal complements and orthogonal direct sums.
- `linear-network`: Linear exchange network with restored scratch wires: A fixed network of linear gates on W scalar wires that exchanges two banks of values with signs while returning every auxiliary (scratch) wire to its arbitrary initial value; each wire's fixed place is its role.
- `frames`: Frames: changing the representation along network edges: Each array on a wire is stored as D_v g for a vertex-dependent invertible operator D_v; since all wires at a gate share the frame and gates are pointwise linear, the whole network implements D_out S D_in^{-1}, with edge cost D_v D_u^{-1}.
- `subset-gadget`: Three-element-subset gather/scatter gadget: Using triples of a ground set, gather and scatter create coefficients depending on intersection size, and side wires cancel the unwanted ones so that three stages realize (X,Y)↦(−Y,X) with arbitrary scratch values restored.
- `rank-saving`: Subspace labels and the rank saving s < Wm: Attaching nested nondegenerate subspaces of an m-dimensional space to gates so that the sum s of edge-difference ranks stays strictly below W·m; this strict deficit is the source of the power saving.
- `bit-network-shear`: Bit network and the address shear: The XOR-only bit network with rational matrices M_v whose endpoint difference is the identity, so frames Φ_M (moving entry (H,D) to (H+MD,D)) make every role undergo the shear (H,D)↦(H+D,D).
- `complex-phase-network`: Complex phase network and the C kernel: The complex version of the network with binary labels and phase frames C_U=H^{⊗m}diag(i^{wt(P_U x) mod 4})H^{⊗m}; each edge difference is a product of two-point kernels aI+bX_v, and telescoping gives C^{⊗m} on every role.
- `triangular-factorization`: Lower-triangular (Bruhat) factorization: Every rational m×m matrix of rank a factors as E₁ΠE₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with exactly a ones, matching the tape order of controlled shifts.
- `matrix-shear`: Cost of a rational matrix shear: The shear (H,D)↦(H+AD,D) for a rank-a rational matrix A is done with exactly a interchanges of b-digit fields plus O(V) work, using triangular factors and three controlled updates per pivot.
- `power-width-interchange`: Power-width chunk interchange and the recursive saving: For chunks of e=m^k digits, running the bit network on W row-split role streams, with each edge done by smaller interchanges, gives F_k ≤ (s/W)F_{k−1}+O(1); because s/W<m^τ this yields cost O(V e^τ).
- `chunk-interchange`: Chunk interchange in O(V uᵗ) time: Interchanging two disjoint u-bit address fields of an array in which all address combinations occur costs O(V u^τ) for a fixed τ<1, via XOR-style intermediate steps whose final effect is an exact permutation.
- `packed-bit-addition`: Packed addition of selected address bits: A binary row addition on corresponding selected bits of two address chunks, using a third chunk as restored scratch, is done by eight packed cyclic shifts plus deterministic repair of an exponentially small set of exceptional addresses.
- `ring-mod-yr`: Polynomial ring modulo yʳ + 1: The ring C[y]/(y^r+1) of polynomials of degree below a power of two r; multiplying by y^a permutes the coefficient list with sign changes, and the coefficient maximum norm is preserved.
- `fixed-point`: Fixed-point complex grid and truncation: Complex numbers are stored as pairs of signed two's-complement integers scaled by 2^{-p}; the truncation Q_p rounds each part toward zero to this grid with error below √2·2^{-p}.
- `signed-packing`: Signed packing (Kronecker substitution) of ring products: Polynomials with small signed coefficients are evaluated at a large power of two to give integers, multiplied by the established O(N log N) integer multiplier as a subroutine, and the product coefficients are recovered by centered residues, giving normalized ring products in O(rp log(rp)).
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{-2πi jk/q} of a length-q vector, with the opposite-sign inverse F⁺ satisfying F⁺F = I/q.
- `butterfly-fft`: Butterfly (decimation-in-frequency) transform: A length-t transform is computed in log₂t levels, each pairing z_k with z_{k+t/2}, applying the two-point butterfly H₀(u,v)=((u+v)/2,(u−v)/2), a twiddle multiplication, and recursing on both halves.
- `phase-frame-reduction`: Phase frames reduce a butterfly layer to C kernels: Since H₀=b·S·C·S with a diagonal phase S, a simultaneous layer H₀^{⊗D} equals b^D S_D C^{⊗D} S_D; the network turns C^{⊗e} on e axes into s calls on e/m axes plus binary basis changes of selected bits.
- `simultaneous-layer`: Simultaneous butterfly layer in O(V d^λ′) time: Applying H₀ to the same bit position in d address chunks of polynomial records at once, exactly in Gaussian dyadics with guard bits and one final truncation, costs O(V d^{λ′}) with λ′<1 instead of d passes.
- `contraction-error`: Contractions and error accumulation: A linear map that does not increase the maximum coefficient norm is a contraction; errors of composed approximations add, and for a bilinear contraction the error is bounded by ‖Δf‖‖g′‖+‖f‖‖Δg‖.
- `convolution`: Cyclic convolution and the convolution theorem: Cyclic convolution u*v multiplies polynomials modulo x^q − 1 and equals, up to normalization, the inverse transform of the pointwise product of the transforms.
- `multidim-transform`: Multidimensional transforms (tensor products): A transform on an array indexed by several axes is the tensor product of one-dimensional transforms, computed one axis at a time; convolution on the product group corresponds to pointwise product.
- `synthetic-transform`: Synthetic polynomial transform: A butterfly transform over the ring C[y]/(y^r+1) whose roots of unity ω_t=y^{2r/t} act as exact signed shifts of the coefficient list, so twiddle multiplications are cheap (Nussbaumer–Quandalle).
- `crt-map`: Chinese-remainder map to distinct prime axes: With pairwise coprime axis lengths s_i and product S, the map x ↦ ∏ x_i^{μ_i} is an isomorphism from C[x]/(x^S−1) to the multi-axis cyclic ring, converting one long cyclic convolution into a multidimensional one; on tape it is a sequence of triangular controlled shifts.
- `bluestein`: Bluestein chirp identity: A transform with quadratic-phase (chirp) factors equals pointwise chirp multiplication, a cyclic convolution with the chirp array, and a second chirp multiplication.
- `phase-twist`: Phase twist from cyclic to negacyclic wrap: Multiplying coefficient k by ζ^k with ζ=e^{πi/r} maps C[x]/(x^r−1) isomorphically onto C[y]/(y^r+1), so the negative wrap of the ring gives exactly the cyclic wrap after the twist is removed.
- `transform-layout`: Synthetic transform layout and retained frequency order: Selected bits of the participating axes are brought to a common offset in K-bit chunks by chunk interchanges; the forward transform leaves frequencies in bit-reversed order B_t and layout L, which the opposite transform consumes, at cost O(Tp[dK+pK^{τ−1}+ℓd^{λ′}]).
- `ring-convolution`: Normalized convolution over the ring from the retained layout: Forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform in the same stored order compute f*g/(rM) on the remaining axes over C[y]/(y^r+1) with error below √2·M(3ℓ+1)2^{-p}.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's identity expressing a Fourier transform of coprime length s as a transform of larger power-of-two length t, sandwiched between two Gaussian-weighted contractions A and B₀ and two coordinate permutations.
- `retained-permutations`: Resampling with the permutations left in the transform: Instead of sorting twice per coordinate, the coordinate permutations of resampling are kept in the transform formula; the chirp absorbs the target permutation and the source permutation cancels across the two forward transforms, the pointwise product and the opposite transform.
- `integer-as-convolution`: Integer product as convolution of radix digits: Writing both inputs as polynomials in 2^b with b-bit digits, the product is a convolution of digit lists; padding so the degree is below the cyclic length S avoids wraparound, and coefficients stay below 2^{3b}.
- `exact-recovery`: Exact recovery by rounding and carry propagation: After removing the known scales, each recovered digit-convolution coefficient has error below 1/2, so rounding gives the exact integer coefficients and radix-2^b carries give the 2n-bit product.
- `parameters`: Parameter choices, padded box and prime source lengths: From n pick b=⌈log₂n⌉, p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, a power of two T≈n/b split into d axes of length r/2 or r, and distinct primes s_i just below each t_i (found by deterministic search), with fixed rational exponents leaving positive margins.
- `complex-convolution-twist`: Complex cyclic convolution via the coefficient twist: Normalized cyclic convolution on all d power-of-two axes is obtained by twisting the last coordinate into the ring, applying the ring convolution on the other axes, and untwisting.
- `source-transform`: Computed source transform: The procedure evaluating R F_s: Gaussian map A on each line, the chirp-based transform via complex convolution, Gaussian map B₀, then scaling by 2^γ, with the opposite sign obtained by complex conjugation.
- `multiplication-algorithm`: The multiplication algorithm: Form radix-2^b digits, apply the CRT map Φ, compute two forward source transforms, multiply pointwise, apply the opposite transform, rescale by S and 2^{2b+4}S, round, invert Φ, and propagate carries to output the 2n-bit product.
- `cost-accounting`: Cost table and the κ margin: Dividing costs by Tp=Θ(n), seven dominant terms have powers of p at most 1−2κ (smallest margin 2^{-181}), so every polylogarithmic loss is absorbed and the total is O(n (log n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A single deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ=2^{-182}, refuting the n log n optimality conjecture in this model; it works by fast address interchanges and fast simultaneous butterfly layers inside a Gaussian-resampling/Bluestein/synthetic-transform reduction.

## Concepts the reader knows

- `big-o`: Big-O notation
- `polynomials`: Polynomials
- `complex-numbers`: Complex numbers
- `multitape-tm`: Multitape Turing machine
- `binary-representation-of-integers`: Binary representation of integers
- `modular-arithmetic`: Modular arithmetic
- `primes-divisibility-coprimality-and-gcd`: Primes, divisibility, coprimality and gcd
- `logarithms-floors-and-ceilings`: Logarithms, floors and ceilings
- `divide-and-conquer-and-recurrences`: Divide and conquer and recurrences
- `sorting-merging-and-radix-sort`: Sorting, merging and radix sort
- `schoolbook-multiplication-and-carries`: Schoolbook multiplication and carries
- `permutations`: Permutations
- `sets-subsets-and-binomial-coefficients`: Sets, subsets and binomial coefficients
- `xor-and-mod-2-arithmetic`: XOR and mod 2 arithmetic
- `hamming-weight`: Hamming weight
- `matrices-and-matrix-vector-products`: Matrices and matrix-vector products
- `vector-norms-and-the-triangle-inequality`: Vector norms and the triangle inequality
- `lexicographic-order-and-mixed-radix-indexing`: Lexicographic order and mixed-radix indexing
- `two-s-complement-and-signed-integers`: Two's complement and signed integers
- `dyadic-and-rational-numbers`: Dyadic and rational numbers
- `euler-s-formula-and-complex-conjugation`: Euler's formula and complex conjugation
- `tape-based-subroutines-and-stacks`: Tape-based subroutines and stacks
- `constant-factors-versus-asymptotic-dominance`: Constant factors versus asymptotic dominance

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

Write the answer to `exegenius/tasks/0045-argument.answer.json`, then run `exegenius submit 0045-argument` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0045-argument`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
