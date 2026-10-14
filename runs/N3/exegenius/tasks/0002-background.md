# exegenius task 0002-background

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N3` (paths below are relative to it)

Say what a specific reader already knows, for these sources. The reader profile describes the reader in a few words, and its examples do not list everything it covers: it stands for a level of study. Make it concrete for the sources.

The sources were written for readers of their own, and use without explanation what those readers know. Read the sources and find that background: the notions, notation and standard results they use without defining. For each, decide whether a reader at the profile's level has been taught it, in the profile's subject or in the subjects that subject rests on (an undergraduate degree in physics teaches linear algebra, Fourier series and probability as well as mechanics, whether or not a profile names them).

- The reader knows what their level of study teaches to everyone at that level. Do not withhold it because the profile does not name it.
- The reader does not know what is taught only in some courses, or in later or specialist study, nor what the sources introduce, define or prove: that is what the wiki explains. When unsure, count it as not known.
- The existing concepts were planned by an earlier task and stay as they are: this answer only adds background they lack.
- `summary`: the subjects and how far into each this reader has gone, as they bear on the sources. Everyone who writes or checks the wiki is shown it with the profile.
- `known`: each concept from that background that the reader knows and no existing concept covers, with the aliases a writer might use for it. Include what the sources use and what an explanation of them would naturally use. Known concepts get no page.

## Target

The main result of the paper: a deterministic multitape Turing machine algorithm that multiplies n-bit integers in O(n (lg n)^(1-kappa)) time, disproving the n log n optimality conjecture in that model, and how it works

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Existing concepts

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bounds f = O(g) up to a constant factor for large inputs.
- `polynomials`: Polynomials (known to the reader): Expressions Σ a_k x^k with coefficient lists, added and multiplied in the usual way.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with modulus, conjugation and roots of unity e^{2πik/n}.
- `multitape-turing-machine`: Multitape Turing machine (known to the reader): A finite-control machine with a fixed finite alphabet and a fixed number of one-dimensional tapes, each head reading, writing and moving one cell per step.
- `linear-algebra`: Linear maps, subspaces and rank: Matrices over a field, their rank, invertibility, subspaces, dimension and tensor products of vector spaces.
- `integer-multiplication-problem`: Exact integer multiplication on a multitape machine: The task of reading x#y for two n-bit strings and writing the exact 2n-bit binary product, with cost measured as worst-case steps T_A(n) of one fixed multitape machine A and lg n = max{⌈log₂ n⌉, 1}.
- `nlogn-conjecture`: n log n optimality conjecture: Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers, i.e. that every multiplication machine eventually needs time at least c·n lg n.
- `discrete-fourier-transform`: Normalized discrete Fourier transform: The map (F_q u)_k = (1/q) Σ_j u_j e^{−2πijk/q} (and its opposite-sign version F_q^+), a contraction in the max-modulus norm; tensor products F_q over several axes give multidimensional transforms.
- `cyclic-convolution`: Cyclic convolution: The product in C[x]/(x^S − 1), or its multidimensional analogue on a product of cyclic axes, which Fourier transforms turn into pointwise multiplication.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The previously established fixed-tape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short records, never recursively on the new theorem.
- `radix-digit-convolution`: Radix-digit reduction to convolution: Splitting each n-bit input into q = ⌈n/b⌉ digits in base 2^b so that the product's digits are the convolution of the two digit lists, bounded below 2^{3b}, followed by carry propagation.
- `array-layout`: Lexicographic array layout and logical volume: Arrays on address sets [a₁]×…×[a_t] stored in lexicographic order with implicit addresses, address permutations acting on entry positions, rows as contiguous suffix blocks, and V the number of stored data bits.
- `elementary-streams`: Elementary stream operations: Linear-time O(V) tape scans that permute or move single radix digits of addresses, split and merge streams on a digit, and distribute whole rows cyclically among W role streams.
- `controlled-shifts`: Controlled shifts and rational scalings: Linear-time updates y ↦ y + a(controls) mod q^b of an address field by an offset computed from earlier fields, and multiplication of the field by fixed rational units, implemented by splitting and re-merging blocks.
- `crt-address-map`: Chinese-remainder address map: The algebra isomorphism x ↦ Π x_i^{μ_i} from C[x]/(x^S−1) to the product of cyclic axes of pairwise coprime prime lengths s_i, which preserves convolution and is implemented as triangular controlled shifts.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of coprime length s through one of power-of-two length t, using Gaussian-weighted resampling maps A and B₀ that are contractions computable to precision p.
- `no-sort-resampling`: Resampling with retained permutations: The form P_s F_s = 2^{2α²} B₀ P_t F_t A of Gaussian resampling, and its tensor version R F_s = 2^γ 𝓑₀ Q F_t 𝓐, in which the source and target coordinate permutations stay inside the transform formula instead of being executed as sorts.
- `bluestein-chirp`: Bluestein's chirp identity: The identity Q F_t u = ā · (a * (ā · u))/T with chirp a_j = exp(−πi Σ s_i j_i²/t_i), converting the middle transform together with its target permutation into a normalized cyclic convolution and two pointwise phase multiplications.
- `source-permutation-cancellation`: Source permutation cancellation: The identity (R F_s^+)[(R F_s u)·(R F_s v)] = (u*v)/S², showing that the source permutation R retained in the forward transforms cancels against the opposite-sign transform, so convolution needs no sort.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: The ring 𝓡_r = C[y]/(y^r + 1) with r a power of two, where multiplying by a power of y is a signed cyclic shift of the coefficient list and the wrap is negacyclic.
- `coefficient-twist`: Coefficient twist: The isomorphism x_d ↦ ζy with ζ = e^{πi/r} from C[x_d]/(x_d^r − 1) to C[y]/(y^r + 1), which turns the last cyclic coordinate into a negacyclic polynomial whose wrap recovers the cyclic wrap after untwisting.
- `gaussian-dyadics`: Gaussian dyadic numbers and fixed-point grids: Complex numbers in Z[i, 1/2], whose real and imaginary parts have power-of-two denominators, stored as fixed-point two's-complement words on the grid 2^{−p}Z[i] and truncated toward zero by Q_p.
- `normalized-butterfly`: Normalized butterfly H₀: The two-point map H₀(u, v) = ((u+v)/2, (u−v)/2), a contraction applied coefficientwise on polynomial records along one address bit; it is the arithmetic step of each radix-two transform level.
- `synthetic-transform`: Synthetic polynomial transform: Nussbaumer's transform F_t^± over C[y]/(y^r+1) using ω_t = y^{2r/t} as root of unity, computed by decimation-in-frequency levels of butterflies and signed shifts, with outputs stored in bit-reversed frequency order.
- `linear-network`: Linear network with roles and scratch wires: A fixed circuit of wires carrying scalars and gates applying fixed linear maps to some wires, where each wire's fixed place is its role and auxiliary scratch wires may start with arbitrary values.
- `scratch-restoration`: Restoring arbitrary scratch values: The schedule that first subtracts the effect of the current scratch values, then adds data to scratch, applies its effect, and finally undoes the scratch updates, so the net effect is independent of the scratch's initial contents and every scratch value is restored.
- `triple-intersection`: Triple-intersection pairings: Indicator vectors of the 3-element subsets of a 100-element set, whose pairings give |S∩T| − 1 under a rational form or |S∩T| mod 2 over F₂, so that neighboring triples have orthogonal lines (after Frankl–Wilson and Alon).
- `bilinear-forms`: Nondegenerate bilinear forms and orthogonal residuals: Symmetric bilinear forms with no nonzero vector orthogonal to everything; for nested nondegenerate subspaces U ⊂ V the orthogonal residual is the complement of U inside V, of dimension dim V − dim U.
- `bank-exchange`: Three-stage bank exchange: The scalar network built from copy, gather, scatter and side-injection gates on triples which, in three stages, maps the two banks (X_a, Y_a) to (−Y_a, X_a) while restoring every auxiliary value.
- `frames`: Frames and the common-frame identity: Invertible operators D_v chosen at each source, gate and sink so that the stored array is D_v applied to the logical array; because a common frame commutes with a pointwise gate, the network applies D_out S D_in^{−1} and intermediate frames cancel.
- `subspace-labels`: Nested subspace labels and rank budget: An assignment of nondegenerate subspaces of the m-dimensional space F^{⊗3} to the gates and terminals of the network, nested along every edge, whose total dimension change s is strictly less than the number of wires times m.
- `rank-deficit-recursion`: Recursive saving from s < Wm: The volume-normalized recurrence F_k ≤ (s/W)F_{k−1} + O(1): a call at parameter mf makes s calls at parameter f on streams of volume V/W, so s/W < m^τ yields cost O(V e^τ) with τ = 1 − 2^{−50} < 1.
- `address-shear`: Address shear: The array permutation Φ_M moving the entry at address (H, D) to (H + MD, D), where H and D are two chunks viewed as vectors of m fields over Z/q^b; the shear H ← H + D plus two linear-cost updates gives an interchange.
- `lower-triangular-factorization`: Lower triangular factorization: The factorization A = E₁ Π E₂ of any rational matrix of rank a into invertible lower triangular factors and a partial permutation Π with a ones (a reversed Bruhat factorization, after Grigor'ev).
- `matrix-shear-cost`: Cost of a rational matrix shear: A shear (H, D) ↦ (H + AD, D) by a rational matrix of rank a is performed with exactly a interchanges of field pairs plus O(V) triangular work.
- `rational-shear-interface`: Rational shear interface of the bit network: Assigning projection matrices P_U to the bit network's labels so that every routed role sees the endpoint shear I_m, while the edge differences have total rational rank s_b < W_b m.
- `power-width-interchange`: Power-width interchange recursion: The recursive procedure interchanging two chunks of e = m^k radix-q digits by splitting rows among the W roles, applying each edge shear via smaller interchanges, and running the XOR gates pointwise, in O(V e^τ) time with a depth-first fixed-tape schedule.
- `fast-chunk-interchange`: Fast address-chunk interchange: The procedure exchanging two disjoint u-bit address fields of an array in O(V u^τ) time for a fixed τ < 1, computing XOR combinations of data along the way though its final effect is an exact permutation.
- `phase-frames`: Binary phase frames: Frames 𝓒_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} for binary labels U, whose change along an edge is a product of one two-point kernel C_v = aI + bX_v per orthonormal residual vector, telescoping to C^{⊗m} on every role.
- `packed-selected-bit-addition`: Packed selected-bit addition: A procedure that XORs selected bits of one address chunk into corresponding bits of another, using a third chunk as restored scratch, by eight cyclic rotations of whole chunk ranges followed by deterministic sorting repair of a small exceptional set of addresses.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀ on the same bit position of up to d address chunks at once in O(V d^{λ'}) time with λ' < 1, by recursing through the complex network's phase frames, packed bit changes and an exact Gaussian-dyadic evaluation with one final truncation.
- `transform-layout`: Transform layout on K-bit chunks: The tape layout placing the selected address bits of all participating axes at a common offset in consecutive K-bit chunks, with polynomial coefficients in a contiguous suffix, so that each transform round is one simultaneous layer.
- `signed-packing`: Signed Kronecker packing: Multiplying two polynomials of 𝓡_r with fixed-point Gaussian coefficients by packing their signed integer numerators into large integers, multiplying with the O(N log N) multiplier, and unpacking and negacyclically reducing.
- `synthetic-convolution`: Normalized convolution over the polynomial ring: Computing 𝓜_r(f, g) = (f*g)/(rM) for arrays over 𝓡_r by two forward synthetic transforms kept in the same stored frequency order, packed pointwise ring products, and the opposite transform consuming that order.
- `exact-recovery`: Error below 1/2 and exact recovery: The precision argument showing the recovered convolution coefficients are within less than 1/2 of the true integers, so rounding, undoing the CRT map and propagating radix-2^b carries gives the exact 2n-bit product.
- `parameter-choice`: Parameter choice and cost table: The setting b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two box T ≈ 4n/b, prime axis lengths s_i near t_i, and fixed rationals τ, λ', ε, κ = 2^{−182}, under which every normalized cost is at most p^{1−2κ}.
- `main-theorem`: Integer multiplication below n log n: There is one deterministic fixed-alphabet multitape Turing machine computing the exact product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, by chaining radix-digit convolution, a CRT address map, Gaussian resampling with retained permutations, Bluestein chirps, a coefficient twist and synthetic transforms accelerated by fast chunk interchanges and simultaneous butterfly layers; this disproves the n log n optimality conjecture in that model.

## Sources (read them from disk)

- `sources/paper.tex`: source id `paper`, "Integer multiplication below n log n (OpenAI, 2026)"

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "KnownConcept": {
      "additionalProperties": false,
      "properties": {
        "aliases": {
          "description": "Other names and abbreviations for it, in the sources or in standard texts.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "gloss": {
          "description": "One precise sentence saying what it is.",
          "type": "string"
        },
        "name": {
          "description": "Display name in plain text, e.g. \"Fourier series\".",
          "type": "string"
        }
      },
      "required": [
        "name",
        "aliases",
        "gloss"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "known": {
      "description": "Concepts the reader knows that the sources rely on and no existing concept covers.",
      "items": {
        "$ref": "#/$defs/KnownConcept"
      },
      "type": "array"
    },
    "summary": {
      "description": "Two to four sentences: the subjects this reader has studied that bear on the sources,\nand how far into each.",
      "type": "string"
    }
  },
  "required": [
    "summary",
    "known"
  ],
  "title": "BackgroundAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0002-background.answer.json`, then run `exegenius submit 0002-background` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0002-background`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
