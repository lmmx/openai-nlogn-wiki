# exegenius task 0002-background

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F1` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on growth of a function, ignoring constant factors.
- `polynomials`: Polynomials (known to the reader): Finite sums of coefficients times powers of a variable, added and multiplied coefficientwise.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with i²=−1, including unit-modulus roots of unity e^{2πi/k}.
- `tape-machines`: Turing machines and tapes (known to the reader): A finite-state machine reading and writing symbols on tapes with moving heads.
- `fixed-tape-model`: Fixed finite-tape machine model: The computation model: one fixed finite alphabet and a fixed number of one-dimensional tapes, each step touching one cell per tape, so extra tracks or work tapes change time only by a constant factor.
- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's proposal that n log n is the optimal order of growth for multiplying n-bit integers on multitape Turing machines.
- `nlogn-multiplier`: Established O(n log n) multiplier (Harvey–van der Hoeven): The known fixed-tape integer multiplier running in O(N log N) time on N-bit inputs, used here only as an ordinary subroutine on short records.
- `array-order`: Arrays in lexicographic tape order with address fields: A multidimensional array is stored on a tape in lexicographic order of its address (first coordinate most significant), so address fields are contiguous ranges of positions and an address is implicit in position.
- `stream-ops`: Elementary stream operations: Linear-time tape scans that permute digit values, move a digit, split an array by a digit, apply a pointwise map and merge, or split whole rows cyclically into a fixed number of equal streams.
- `controlled-shifts`: Controlled cyclic shifts and rational scalings: In linear time, update a target address field by adding an offset computed from earlier control fields modulo q^b (a cyclic shift of blocks), or multiply it by a fixed rational unit.
- `matrix-basics`: Matrix rank, subspaces and orthogonal complements: Rank of a matrix, subspaces of a vector space with a bilinear form, and the orthogonal complement of one subspace inside a larger one, whose dimension equals the change in dimension.
- `dft`: Discrete Fourier transform: The normalized map sending a length-q vector u to (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q}; its inverse-direction version uses the opposite sign, and both are contractions.
- `cyclic-convolution`: Cyclic convolution: Multiplication of polynomials (or arrays) modulo x^S − 1, where indices wrap around modulo the length on every axis.
- `convolution-theorem`: Convolution theorem for normalized transforms: The transform of a cyclic convolution equals the pointwise product of transforms (with a normalizing factor), so convolution can be computed by transform, pointwise product and inverse transform.
- `multidim-transform`: Multidimensional (tensor) transforms: A transform on a product of axes of lengths t_1,…,t_D, equal to the tensor product of the one-dimensional transforms applied along each axis in turn.
- `int-as-convolution`: Integer multiplication as digit convolution: Writing each input in radix 2^b digits makes the product's digit sequence a convolution of the two coefficient lists; with enough zero padding, cyclic convolution equals ordinary polynomial multiplication, and carrying recovers the integer.
- `fixed-point-disk-grid`: Fixed-point disk grid and error propagation: Complex values stored as pairs of signed fixed-point integers with p fractional bits in the unit disk; algorithms approximate linear contractions, truncation toward zero adds bounded error, and errors add under composition.
- `polynomial-ring-mod`: Polynomial ring modulo y^r + 1: Complex polynomials of degree below r with y^r = −1, so multiplication by a power of y is a signed cyclic shift of the coefficient list (negacyclic wraparound).
- `butterfly-fft`: Two-point butterfly and radix-2 FFT order: The butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) applied recursively by decimation in frequency, with twiddle multiplications, computes a transform of power-of-two length and leaves outputs in bit-reversed slot order.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier-type transform of arrays of ring polynomials in which the roots of unity are powers y^{2r/t}, so twiddle multiplications are exact signed shifts of coefficient lists and only butterflies cost arithmetic.
- `crt-axis-map`: Chinese-remainder address map: A ring isomorphism from cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to d-dimensional cyclic convolution on prime axes, implemented on tape by triangular prefix-controlled cyclic shifts.
- `gaussian-resampling`: Gaussian resampling with retained permutations: Harvey–van der Hoeven's identity expressing a Fourier transform of coprime length s through one of power-of-two length t via Gaussian-weighted maps A and B₀, here keeping the two coordinate permutations inside the formula instead of sorting.
- `chirp-identity`: Bluestein chirp identity: Rewrites a Fourier transform (with its frequency permutation) as pointwise multiplication by a quadratic phase, a cyclic convolution with the chirp array, and another pointwise phase multiplication.
- `permutation-cancellation`: Source-permutation cancellation: The coordinate permutation retained by resampling cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S² so no sort is executed.
- `negacyclic-twist`: Coefficient twist to negacyclic ring: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} maps cyclic convolution on the last axis to convolution in the ring of polynomials modulo y^r+1, whose negative wrap exactly cancels the twist.
- `network`: Linear exchange network with restored scratch wires: A fixed network of linear gates on wires (roles) that swaps two banks of values with prescribed signs and returns every auxiliary scratch wire to its arbitrary initial value, using a copy/gather/scatter/side-injection schedule.
- `frames`: Frames and the common-frame identity: Giving each array on a wire an invertible address-space operator (a frame) at every vertex; because a common frame commutes with a pointwise linear gate, the network's overall effect is the endpoint frames applied to each role, and each edge only changes the frame.
- `subset-labels`: Three-element-subset subspace labels: Subspaces of a tensor-cube bilinear space attached to gates, built from indicator vectors of three-element subsets with intersection-size pairings (Frankl–Wilson, Alon), so labels are nested along edges and neighbors are orthogonal.
- `rank-saving`: Rank deficit s < Wm: Summing the dimension changes (edge ranks) of all labels gives a total s of smaller calls strictly below W·m, where W is the number of wires and m the dimension, which is the source of the power saving.
- `bit-network`: Bit exchange network with shear interface: The F₂ network with rational labels whose frames are address shears: its endpoint operator is (H,D)→(H+D,D) on every role, using only XOR gates, with rank sum s_b < W_b m.
- `phase-network`: Complex phase network: The Z[i,1/2] network with binary labels whose frames are phase operators C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m}; each edge is a product of two-point kernels aI+bX_v and the endpoint operator is C^{⊗m} on every role, with s_c < W_c m.
- `lower-triangular`: Lower-triangular factorization of matrices: Every rational matrix A of rank a factors as E₁ΠE₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with a ones (a reversed-order Bruhat factorization).
- `matrix-shear`: Rational matrix shear as field interchanges: The map (H,D)→(H+AD,D) over Z/q^b for a rank-a rational matrix A is performed by triangular controlled shifts and exactly a interchanges of b-digit fields.
- `power-saving-recurrence`: Power-saving recurrence: Calling s smaller operations of parameter f/m on streams of volume V/W gives normalized cost F_k ≤ (s/W)F_{k−1}+O(1); since s/W < m^τ this solves to O(e^τ), a strict power saving.
- `power-interchange`: Power-width address interchange with rows: Interchanges two chunks of m^k digits using the bit network: split rows among the W roles, apply a matrix shear on each edge via recursive smaller interchanges, merge, then compose three shears into a swap.
- `chunk-interchange`: Fast interchange of address chunks: Exchanges two disjoint address chunks of u bits in an array (any prefix, gap and suffix) in O(V u^τ) tape steps for a fixed τ < 1, by padding rows and splitting the width in base m; the final effect is an exact permutation although intermediate steps form XOR combinations.
- `packed-bit-addition`: Packed selected-bit addition with deterministic repair: Performs y←y⊕x on the same bit position of f chunks at once using eight cyclic shifts of whole chunk ranges (a three-chunk rotation trick that restores a scratch chunk), then corrects the small explicitly identified set of addresses where guard values fail.
- `simultaneous-layer`: Simultaneous butterfly layer: Applies the two-point butterfly H₀ at one bit position in each of D address chunks at once in O(V d^{λ'}) time, by recursing on the complex phase network with packed basis changes, exact Gaussian-dyadic arithmetic and one final truncation.
- `transform-layout`: Synthetic transform layout and stored frequency order: Places selected bits of all participating axes at a common offset in consecutive chunks so each radix-two round is one simultaneous layer, and keeps the bit-reversed frequency order through the pointwise product to the opposite transform.
- `kronecker-packing`: Signed packing (Kronecker substitution): Multiplies two ring polynomials by evaluating them at B₀=2^{4p} as signed integers, multiplying with the O(N log N) integer multiplier, extracting centered coefficients and wrapping negacyclically.
- `ring-convolution`: Convolution over the polynomial ring from the retained layout: Computes normalized convolution of arrays of ring polynomials by two forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform consuming the same stored order.
- `complex-convolution`: Complex cyclic convolution by coefficient twist: Normalized cyclic convolution f*g/T of complex arrays on power-of-two axes, obtained by twisting the last axis into the polynomial ring and using the ring convolution.
- `source-transform`: Source transform procedure: Computes the transform of coprime length by applying the Gaussian map A line by line, the chirp transform through complex convolution, the map B₀, and an exact power-of-two scale, with the retained permutation R.
- `prime-lengths`: Choice of prime source lengths: Chooses distinct odd primes s_i just below the powers of two t_i (with t_i/s_i separated from 1) via a prime-interval lower bound, found by deterministic search, so S is a constant fraction of the padded box T.
- `parameter-balance`: Parameter choice and cost balance: Fixes p = Θ(log n), d = ⌊b^ε⌋ axes, chunk size K, ring dimension r = 2^{Θ(p/d)} and the tiny exponents so that every row of the cost table has normalized power of p at most 1 − 2κ, giving total O(n (log n)^{1−κ}).
- `exact-recovery`: Rounding and carry propagation to the exact product: Shows the recovered coefficient error is below 1/2, rounds to the integer convolution coefficients, and propagates radix-2^b carries to output exactly 2n product bits.
- `mult-algorithm`: The multiplication algorithm: Splits both inputs into digits, applies the coefficient-address map, computes the source transform of each, multiplies pointwise, applies the opposite-sign transform with scalings, rounds and propagates carries.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: There is one deterministic fixed-alphabet, fixed-tape Turing machine multiplying n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model.

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
