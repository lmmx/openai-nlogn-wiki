# exegenius task 0002-background

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F6` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bounds on running time such as O(n log n).
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, including roots of unity and modulus.
- `turing-machines`: Turing machines and tapes (known to the reader): Machines with a finite control reading and writing symbols on tapes, one cell at a time.
- `multitape-streams`: Fixed-tape model and elementary stream scans: The fixed-alphabet, fixed-number-of-tapes machine model in which arrays are streams in lexicographic order, and splitting, merging, digit moves and row splits cost O(V) for volume V.
- `controlled-shifts`: Controlled cyclic shifts and rational scalings: Updating a target address field by an offset computed from earlier control fields (a cyclic rotation of blocks), or multiplying it by a unit modulo q^b, in O(V) time.
- `hvdh-multiplier`: Established O(n log n) integer multiplier: The Harvey–van der Hoeven multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short inputs.
- `convolution-multiplication`: Integer multiplication as convolution of radix digits: Writing each integer as a polynomial in 2^b with small digit coefficients turns the product into a convolution of digit lists, with carries propagated afterwards.
- `discrete-fourier-transform`: Normalized discrete Fourier transform and convolution theorem: The transform F_q averaging inputs times roots of unity e^(−2πijk/q) (with inverse-sign version F_q⁺), which turns cyclic convolution into pointwise products up to a normalization.
- `radix-two-fft`: Radix-two FFT butterflies: The decimation-in-frequency recursion that pairs entries k and k+t/2, applies the two-point butterfly H₀ = ½[[1,1],[1,−1]] and a twiddle multiplication, then recurses on both halves, leaving outputs in bit-reversed order.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree below r with y^r = −1, so multiplying by a power of y is a signed cyclic shift of the coefficient list and powers of y serve as roots of unity.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring modulo y^r + 1 using ω_t = y^(2r/t) as root of unity, so twiddle multiplications are signed coefficient shifts; their forward and opposite versions invert each other up to 1/t.
- `fixed-point-precision`: Fixed-point disk-grid arrays and truncation: Complex coefficients of modulus at most 1 stored with p fractional bits per component; truncation Q_p toward zero costs error below √2·2^(−p) and never increases the norm.
- `signed-kronecker-packing`: Signed packing of polynomial products: Computing products of ring polynomials exactly by evaluating each at a large power of two (signed Kronecker substitution), multiplying the resulting integers with the established multiplier and unpacking the coefficients.
- `linear-algebra-spaces`: Subspaces, orthogonal complements and projections: Vector subspaces of a space with a nondegenerate bilinear form, orthogonal complements, orthogonal projections P_U and tensor products of such spaces.
- `lower-triangular-factorization`: Lower-triangular (Bruhat) factorization: Every m×m rational matrix A of rank a factors as E₁ΠE₂ with E₁, E₂ invertible lower triangular and Π a partial permutation matrix with exactly a ones.
- `bank-exchange-network`: Linear network exchanging two banks with restored scratch wires: A fixed network of linear gates on wires (roles) that, using gather, scatter, copy and side-injection steps over triples, adds one bank into the other three times to exchange X and Y up to sign while restoring all scratch wires whatever their initial values.
- `frames-on-arrays`: Frames and the common-frame identity: Replacing scalars by arrays, each vertex of the network gets an invertible operator (frame) on its array; since pointwise linear gates commute with a common frame, the network implements D_out S D_in^(−1) and each edge only changes frame.
- `subspace-labels`: Nested subspace labels with a rank deficit: Nondegenerate subspaces built from three-element subsets are attached to gates and terminals so adjacent labels are nested; the orthogonal residual dimensions total fewer than W·m, which bounds the number of smaller calls.
- `recursive-power-saving`: Recursive power saving from s < Wm: A call at parameter m·f makes s calls at parameter f on streams of volume V/W, so normalized cost satisfies F_k ≤ (s/W)F_(k−1)+O(1) with s/W < m^τ, giving cost O(V e^τ) with τ < 1.
- `bit-shear-interface`: Rational matrix interface and address shear: Using frames Φ_M that move the entry at (H,D) to (H+MD,D), the bit network turns the exchange into the shear H ← H+D on every role, with total edge rank s_b < W_b·m.
- `matrix-shear-cost`: Cost of a rational matrix shear: The address map (H,D) → (H+AD,D) over Z/q^b with A of rank a costs exactly a interchanges of b-digit fields plus O(V) work, by factoring A and using one swap per pivot.
- `power-width-interchange`: Power-width chunk interchange with rows: Interchanging two chunks of e = m^k digits by splitting rows into W role streams, running the bit network with shear edges implemented by smaller interchanges, then applying D←D−H, H←H+D, D←H−D; cost O(V e^τ).
- `chunk-interchange`: Fast interchange of address chunks: Interchanging two disjoint address fields of u bits in an array in O(V u^τ) time for a fixed τ < 1, although the intermediate steps XOR data together; arbitrary widths are handled by padding and a base-m decomposition.
- `phase-frames`: Phase frames and the two-point kernel C: With C = H S H = aI+bX (a=(1+i)/2, b=(1−i)/2) one has H₀^(⊗D) = b^D S_D C^(⊗D) S_D, and phase frames of binary labels make each network edge a product of translation kernels, one per residual basis vector.
- `packed-selected-bit-addition`: Packed changes of selected address bits: Adding (XOR) selected bits of one address chunk into another using a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small explicitly identified set of exceptional addresses.
- `guard-bits`: Exact Gaussian dyadics and guard width: Intermediate values in a butterfly layer are exact Gaussian dyadics whose denominators and magnitudes grow by at most a bounded number of guard bits, so one truncation follows the completed layer.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀(u,v) = ((u+v)/2,(u−v)/2) to the same bit position in d address chunks at once, on polynomial records, in O(V d^λ') time with λ' < 1 instead of d whole-array passes.
- `synthetic-transform-layout`: Synthetic transform layout on tape: A positional address permutation placing the selected bits of all participating axes at a common offset in consecutive K-bit chunks so that each FFT round is one simultaneous layer; total cost O(Tp[dK + pK^(τ−1) + ℓ d^λ']).
- `synthetic-convolution`: Convolution over the polynomial ring from retained frequency order: Convolving arrays over the ring by transforming both operands, multiplying pointwise in the retained stored frequency order, and applying the opposite transform, with error below √2·M(3ℓ+1)·2^(−p).
- `coefficient-twist`: Cyclic-to-negacyclic coefficient twist: Multiplying coefficient k of the last cyclic coordinate by ζ^k with ζ = e^(πi/r) maps cyclic convolution of length r to the ring modulo y^r + 1, so the ring convolution computes complex cyclic convolution.
- `crt-cyclic-convolution`: Chinese-remainder map to distinct prime cyclic axes: An algebra isomorphism sending x to the product of x_i^(μ_i) turns one cyclic convolution of length S = s₁…s_d into a d-dimensional cyclic convolution over pairwise coprime axes, implemented by triangular controlled shifts.
- `gaussian-resampling`: Gaussian resampling without sorting: Rewrites the prime-length transform P_s F_s as 2^(2α²) B₀ P_t F_t A with contractions A, B₀ and power-of-two length t, keeping the two coordinate permutations inside the transform identity instead of sorting.
- `tensor-resampling`: Tensor resampling on the padded box: Applying the one-dimensional resampling maps line by line along each of d axes of the zero-padded power-of-two box, exposing each axis with chunk interchanges, for error below d·p² and total line cost O(dTp^(3/2+δ)α).
- `bluestein-chirp`: Bluestein chirp identity: Writes the permuted transform Q F_t as chirp multiplication, a cyclic convolution with the chirp array a, and chirp multiplication again, so the frequency permutation is never executed.
- `permutation-cancellation`: Cancellation of the retained source permutation: Because a coordinate permutation R commutes with pointwise products, applying R F_s to both operands and R F_s⁺ to their pointwise product yields (u*v)/S², so the source permutation never has to be undone.
- `parameter-choice`: Size parameters and prime axis lengths: For input length n choose b = ⌈log₂n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, a power-of-two T near 4n/b split into d axis lengths r/2 or r, and distinct odd primes s_i just below the t_i with T/2 < S < T.
- `multiplication-algorithm`: The multiplication algorithm: Split into radix digits, map by the CRT address map, apply the source transform (resampling, chirp convolution via ring convolution) to both operands, multiply pointwise, apply the opposite transform, undo scales, round and propagate carries.
- `exact-recovery`: Precision, rounding and carry recovery: Disk margins keep every intermediate array in the unit disk, accumulated approximation errors stay below 1/2 per coefficient so rounding returns exact integer product coefficients, and carry propagation gives the 2n-bit product.
- `time-bound-accounting`: Cost table and exponent margins: Dividing each phase's cost by Tp = Θ(n) gives seven dominant powers of p, each at most 1−2κ for the fixed rational exponents, so the total is O(n (log n)^(1−κ)).
- `multiplication-below-nlogn`: Integer multiplication below n log n: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^(−182), refuting the n log n optimality conjecture, by combining fast address interchange and simultaneous butterfly layers inside the Gaussian-resampling and synthetic-transform reduction.

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
