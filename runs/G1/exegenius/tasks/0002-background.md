# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/G1` (paths below are relative to it)

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

- `big-o-notation`: Big-O notation (known to the reader): Asymptotic upper bound notation O(f(n)) for running times.
- `polynomials`: Polynomials (known to the reader): Sums of powers of a variable with coefficients, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, with modulus, conjugation and unit-modulus phases e^{iθ}.
- `turing-machine-tapes`: Multitape Turing machines (known to the reader): A machine with a finite alphabet, finite control and a fixed number of one-dimensional tapes whose heads each move at most one cell per step.
- `nlogn-conjecture`: The n log n conjecture and multiplication history: Schönhage and Strassen conjectured that n log n is the optimal multiplication cost on multitape Turing machines; Schönhage–Strassen, Fürer and Harvey–van der Hoeven gave successively better upper bounds down to O(n log n).
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The established O(N log N) multitape algorithm for multiplying N-bit integers, used here only as an ordinary subroutine for short integers.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q} sending q complex values to their q frequency components.
- `cyclic-convolution`: Cyclic convolution: The product of two length-q sequences viewed as polynomials modulo x^q − 1, so that indices wrap around cyclically.
- `convolution-theorem`: Convolution theorem: The Fourier transform turns cyclic convolution into pointwise multiplication (up to normalization), so a convolution costs two forward transforms, a pointwise product and one inverse transform.
- `fft-butterfly`: FFT butterflies (decimation in frequency): The recursive FFT step that pairs entries z_k and z_{k+t/2}, replaces them by their half-sum and half-difference, multiplies one output by a root of unity and recurses on both halves.
- `integer-mult-as-convolution`: Integer multiplication as radix-digit convolution: Splitting each integer into digits in a fixed radix turns the product into a convolution of the digit sequences, whose coefficients are then carried into binary.
- `multidimensional-transform`: Multidimensional (tensor) transform: The Fourier transform on a product of axes, applied as the tensor product of one-dimensional transforms along each axis.
- `crt-axis-map`: Chinese-remainder address map: An isomorphism sending a cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to a convolution on d prime-length cyclic axes, implemented here by triangular controlled shifts.
- `fixed-point-arithmetic`: Fixed-point and Gaussian dyadic arithmetic: Complex values stored as signed two's-complement integers times 2^{−p}; additions, halvings and multiplications by i are exact with enough guard bits, and truncation Q_p to the grid has error below √2·2^{−p}.
- `contraction-error`: Linear contractions and error accumulation: A map that does not increase the maximum-modulus norm; applying contractions to approximate inputs never enlarges the input error, so errors of composed approximations add.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's identity expressing a prime-length Fourier transform through a power-of-two-length one via Gaussian-weighted contractions A and B_0; the two coordinate permutations are left inside the identity rather than sorted.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a Fourier transform as two pointwise multiplications by a chirp phase around a cyclic convolution with the chirp, so the middle transform (with its target permutation) becomes a convolution.
- `permutation-cancellation`: Cancellation of the retained source permutation: The coordinate permutation retained in the resampling identity cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S².
- `prime-axis-lengths`: Prime source lengths near powers of two: Choice of distinct primes s_i slightly below the power-of-two axis lengths t_i (using a prime-interval estimate) so that their product fills a fixed fraction of the padded box while each ratio t_i/s_i leaves room for resampling.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree below r in which y^r = −1, so multiplying by a power of y shifts the coefficient list with sign changes.
- `synthetic-roots`: Synthetic roots of unity: In the negacyclic ring, powers of y serve as roots of unity ω_t = y^{2r/t}, and multiplying by one is an exact signed shift of the coefficient list with no arithmetic.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the negacyclic ring (Nussbaumer–Quandalle) that uses powers of y as roots and is computed by butterflies, signed shifts and address rearrangements.
- `phase-twist`: Coefficient phase twist: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} turns cyclic convolution of length r into convolution modulo y^r + 1 (negative wrap), and untwisting restores the cyclic wrap.
- `kronecker-packing`: Signed Kronecker packing of polynomial products: Evaluating integer-coefficient polynomials at a large base B_0 packs them into integers so that one large integer multiplication yields all coefficients of the product, with signs handled by centered residues.
- `stream-operations`: Array layout and elementary tape streams: Arrays stored in lexicographic address order on tape, with linear-time scans that permute digit positions, split into aligned streams, apply pointwise maps and merge them back.
- `controlled-shifts`: Controlled cyclic shifts of an address field: A target address field is shifted cyclically by an offset computed from earlier control fields in linear time, which also gives multiplication by fixed units modulo q^b.
- `subset-intersection-gates`: Three-element subset gates (copy, gather, scatter, side wires): Fixed linear maps indexed by three-element subsets of {1..100} whose coefficients depend on intersection size; auxiliary side and center wires cancel the unwanted coefficients and are restored afterwards.
- `bank-exchange-network`: Scratch-restoring bank-exchange network: A fixed linear network of wires and gates that, in three stages, exchanges two banks of values with prescribed signs and restores every auxiliary scratch value whatever its initial content.
- `frames-network`: Frames: changing representation along a network: Arrays replace scalars on wires; each vertex has an invertible frame operator D_v, edges apply D_v D_u^{-1}, and pointwise linear gates commute with the common frame, so the whole network acts as D_out S D_in^{-1}.
- `subspace-rank-saving`: Subspace labels and the rank deficit: Nested subspaces of a fixed bilinear space attached to gates and terminals make each edge cost its rank in smaller operations; the total s of these ranks is strictly less than W·m, where W is the wire count and m the label-space dimension.
- `recursive-power-saving`: Recursive power saving: A call at parameter m·f uses s calls at parameter f on streams of volume V/W, so cost per volume obeys F_k ≤ (s/W)F_{k−1} + O(1) with s/W < m, giving cost O(V e^τ) for some fixed τ < 1.
- `lower-triangular-factorization`: Lower triangular (Bruhat-type) factorization: Every rational matrix A of rank a factors as E_1 Π E_2 with E_1, E_2 invertible lower triangular and Π a partial permutation matrix with a ones.
- `matrix-shear-cost`: Cost of a rational matrix shear: The address map (H,D) ↦ (H + AD, D) of rank a is performed with exactly a interchanges of pairs of b-digit fields plus linear work, by factoring A and using three controlled updates around each swap.
- `address-interchange`: Address-chunk interchange: The first tape procedure: it swaps two disjoint address chunks of u bits in a complete array of volume V in time O(V u^τ) for a fixed τ < 1, internally using XOR combinations of intermediate data yet ending as an exact permutation.
- `binary-phase-interface`: Phase frames and the C kernel: Over Gaussian dyadic values, the phase frame changes between binary subspace labels are products of two-point kernels aI + bX_v (a=(1+i)/2, b=(1−i)/2), one per orthonormal residual vector, and telescope to C^{⊗m} on every role.
- `packed-selected-bit-addition`: Packed selected-bit addition: Adds (XORs) the same bit position of f address chunks of one field into another, using a few cyclic shifts of whole chunks and a correction of an explicitly bounded set of exceptional addresses.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The second tape procedure: applies H_0(u,v) = ((u+v)/2,(u−v)/2) to one selected bit in each of up to d address chunks at once on polynomial records, in time O(V d^λ') for fixed λ' < 1, evaluated exactly and truncated once.
- `synthetic-transform-layout`: Tape layout of synthetic transforms: A layout placing the selected bits of the participating axes at a common offset in consecutive K-bit chunks so that simultaneous layers and chunk interchanges evaluate the synthetic transform while keeping a fixed frequency order.
- `synthetic-convolution`: Convolution over the polynomial ring: Two forward synthetic transforms, polynomial products of each record by signed packing, and the opposite transform consuming the same stored frequency order give the normalized ring convolution.
- `exact-recovery`: Exact recovery by rounding and carries: Scaling out the known normalizations, showing the total coefficient error is below 1/2, rounding to integers and propagating radix carries yields the exact 2n-bit product.
- `parameter-choice`: Parameter choice and time bound: Fixed rational exponents and sizes (p = 6⌈log n⌉, d ≈ p^ε, T ≈ n/log n, κ = 2^{−182}) make every cost row of the table a power of p below 1, so the total is O(n (lg n)^{1−κ}).
- `multiplication-algorithm`: The multiplication algorithm: Digits are placed on prime axes by the CRT map, transformed by Gaussian-resampled, chirped, synthetic transforms, multiplied pointwise, transformed back, rescaled, rounded and carried to give the exact product.
- `sub-nlogn-multiplication`: Integer multiplication below n log n: A deterministic fixed-tape Turing machine that multiplies n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture by replacing address rearrangement and Fourier layers with faster recursive tape procedures.

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
