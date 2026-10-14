# exegenius task 0002-background

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N4` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper-bound notation for growth rates of running times.
- `polynomials`: Polynomials (known to the reader): Formal sums of coefficient multiples of powers of a variable, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with real a, b, including modulus, conjugation and the exponential e^{iθ}.
- `multitape-turing-machine`: Multitape Turing machine (known to the reader): A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, each head moving at most one cell per step.
- `matrix-rank`: Linear maps and matrix rank: Matrices represent linear maps between vector spaces, and the rank of a matrix is the dimension of its image.
- `tensor-product`: Tensor products: The tensor product of vector spaces or operators builds a multi-index space or acts independently on each index; the paper's label space and simultaneous butterfly layers are tensor products.
- `bilinear-form`: Nondegenerate bilinear forms: A bilinear form pairs vectors into scalars; it is nondegenerate when no nonzero vector is orthogonal to everything, which lets a subspace split off its orthogonal complement.
- `n-log-n-conjecture`: n log n optimality conjecture: Schönhage and Strassen's conjecture that n-bit integer multiplication needs order n log n time, here read as an eventual Ω(n lg n) lower bound for every fixed multitape machine.
- `harvey-van-der-hoeven-multiplier`: Harvey–van der Hoeven multiplier: The previously established deterministic multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short records.
- `elementary-streams`: Arrays on tape and elementary stream operations: Multi-index arrays are stored in lexicographic address order with implicit addresses, and fixed digit permutations, digit moves, splits into streams and merges each cost O(V) for logical bit volume V.
- `controlled-shifts`: Controlled shifts: Linear-time updates that add to, or cyclically shift, a later address field by an amount computed from earlier fields, possible because the target field follows its control fields in tape order.
- `cyclic-convolution`: Cyclic convolution: The product of polynomials modulo x^S − 1 (or its multidimensional analogue), where exponents wrap around cyclically.
- `radix-digit-convolution`: Multiplication as digit convolution: Splitting each integer into radix-2^b digits turns their product into the convolution of short digit sequences, followed by carry propagation.
- `discrete-fourier-transform`: Normalized discrete Fourier transform: The map sending a length-q vector to the averages of its entries multiplied by powers of a q-th root of unity; it is a contraction and diagonalizes cyclic convolution.
- `crt-address-map`: Chinese-remainder address map: An algebra isomorphism x ↦ ∏ x_i^{μ_i} that turns a cyclic convolution of length S = ∏ s_i into a multidimensional cyclic convolution on pairwise coprime axes, implemented by triangular controlled shifts.
- `fixed-point-approximation`: Fixed-point approximation and error accounting: Complex values are stored on the grid 2^{-p}(ℤ+iℤ) in the unit disk, truncated toward zero, and errors of approximate contractions add when composed.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of coprime length s through one of a nearby length t, using Gaussian-weighted contractions, so prime-length axes become power-of-two axes.
- `retained-permutations`: Retained transform permutations: Instead of sorting, the source and target coordinate permutations of resampling stay inside the transform identity; the target one is absorbed by the chirp and the source one cancels across forward transforms, pointwise product and inverse transform.
- `bluestein-chirp`: Bluestein's chirp identity: A Fourier transform equals pointwise multiplication by a quadratic-phase chirp, a cyclic convolution with the chirp, and another chirp multiplication.
- `negacyclic-ring`: Polynomial ring ℂ[y]/(yʳ+1): The ring of complex polynomials of degree below r with y^r = −1, in which multiplying by a power of y is a signed shift of the coefficient list and powers of y act as roots of unity.
- `coefficient-twist`: Coefficient phase twist: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} maps cyclic convolution modulo x^r − 1 isomorphically onto negacyclic multiplication modulo y^r + 1.
- `butterfly-h0`: Normalized butterfly H₀: The two-point map H₀(u,v) = ((u+v)/2, (u−v)/2), the radix-two step of fast Fourier-type transforms, applied coefficientwise to polynomial records.
- `gaussian-dyadics`: Gaussian dyadic numbers: Complex numbers whose real and imaginary parts are rationals with power-of-two denominators, the ring ℤ[i,1/2], in which the butterfly layers are computed exactly.
- `synthetic-transform`: Synthetic polynomial transform: Nussbaumer's Fourier transform over ℂ[y]/(y^r+1) using powers of y as roots of unity, so it needs only signed shifts, butterflies and address rearrangements, with a stored frequency order consumed by the inverse transform.
- `signed-packing`: Signed Kronecker packing: Packing the signed fixed-point coefficients of two ring elements into large integers so one call to the O(N log N) multiplier yields their exact polynomial product.
- `linear-network`: Linear network with wire roles: A fixed finite circuit of linear gates on wires, each wire's fixed place called its role, which in three stages exchanges two data banks (X,Y) ↦ (−Y,X) with prescribed signs.
- `scratch-restoration`: Restoration of scratch values: A gate schedule that subtracts the effect of arbitrary initial auxiliary values, performs the update, and undoes its copies so every scratch wire ends with its initial value.
- `triple-intersection-construction`: Three-element subset construction: Data indexed by 3-element subsets of a 100-set are combined by gather/scatter through central wires, giving coefficients depending on intersection size, and side wires cancel the unwanted ones so the net effect is y ← y + x.
- `frames`: Frames and the common-frame identity: Each network vertex gets an invertible operator D_v on the wire's array; edges apply D_v D_u^{-1}, pointwise gates commute with a common frame, so the whole network implements D_out S D_in^{-1} on rows split cyclically among the roles.
- `subspace-labels`: Subspace labels and orthogonal residuals: Nested nondegenerate subspaces of a fixed m-dimensional bilinear space are attached to the network's vertices, and the dimension of the orthogonal residual on each edge counts the smaller operations needed there.
- `rank-saving`: Rank saving s < Wm: The key finite fact: the total number s of smaller calls over all edges of a network with W wires and label dimension m is strictly less than Wm.
- `recursive-power-saving`: Recursive power saving: Splitting the work into s calls each on volume V/W gives the normalized recurrence F_k ≤ (s/W)F_{k−1} + O(1), and s/W < m^τ with τ < 1 yields cost O(V e^τ) instead of O(V e).
- `address-shear`: Address shear: The address permutation (H,D) ↦ (H+D,D) on two field groups, which together with two linear-cost updates gives the interchange (H,D) ↦ (D,H).
- `lower-triangular-factorization`: Lower triangular factorization: Every rational matrix of rank a factors as E₁ΠE₂ with invertible lower triangular E₁, E₂ and a partial permutation Π with a ones, a reordered Bruhat factorization.
- `rational-matrix-interface`: Rational matrix interface: The XOR bit network with projection matrices as frames, whose endpoint differences are the identity on every role, so it implements the address shear with total edge rank s_b < W_b m.
- `chunk-interchange`: Fast address-chunk interchange: The first tape procedure: exchanging two disjoint u-bit address fields of an array in O(V u^τ) time with τ < 1, by recursively running the bit network with shears as edge frames.
- `binary-phase-interface`: Binary phase interface: The complex network over Gaussian dyadics with binary labels, whose edge frames are products of two-point kernels C = HSH and whose endpoints telescope to a tensor power of C, convertible to the H₀ layer.
- `packed-selected-bit-addition`: Packed selected-bit addition: Changing selected address bits in several chunks at once by whole-chunk cyclic shifts and moves, followed by a deterministic repair of an explicitly bounded set of exceptional addresses.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The second tape procedure: applying H₀ at the same bit position of up to d address chunks at once in O(V d^{λ'}) time with λ' < 1, computed exactly in Gaussian dyadics and truncated once.
- `synthetic-convolution`: Convolution over the polynomial ring: Normalized cyclic convolution of arrays over ℂ[y]/(y^r+1) computed by two forward synthetic transforms on a tape layout using chunk interchanges and simultaneous layers, packed pointwise products, and the opposite transform.
- `exact-recovery`: Exact recovery by rounding and carries: Removing known scales, bounding the coefficient error strictly below 1/2, rounding to integers and propagating carries gives the exact binary product.
- `parameter-choice`: Parameter choice and cost balance: Fixed rational exponents (τ, λ′, c, ε, δ, …) and sizes d ≈ p^ε, K ≈ d^c make every normalized cost-table term at most p^{1−2κ}, with smallest margin 2^{−181} = 2κ.
- `main-theorem`: Integer multiplication in O(n(lg n)^(1−κ)) time: A single deterministic fixed-tape Turing machine computes the exact product of two n-bit integers in O(n(lg n)^{1−κ}) worst-case time with κ = 2^{−182}, refuting the n log n lower-bound conjecture in this model.

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
