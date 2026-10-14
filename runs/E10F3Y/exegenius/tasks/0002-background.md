# exegenius task 0002-background

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F3` (paths below are relative to it)

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

- `big-o-notation`: Big-O notation (known to the reader): Asymptotic upper bounds on running time such as O(n log n).
- `polynomials`: Polynomials (known to the reader): Finite sums of terms c_k y^k, which can be added, multiplied and reduced modulo another polynomial.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, with modulus, conjugation and unit-modulus phases e^{iθ}.
- `multitape-turing-machine`: Multitape Turing machine (known to the reader): A machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes whose heads each move at most one cell per step.
- `schonhage-strassen-conjecture`: Schönhage–Strassen optimality conjecture: The 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine; the best earlier bound was the unconditional O(n log n) of Harvey and van der Hoeven.
- `hh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The established fixed-tape algorithm multiplying N-bit integers in O(N log N) time, used here as an ordinary subroutine for short integer products.
- `cyclic-convolution`: Cyclic convolution: For arrays indexed by a product of cyclic groups, the product whose entry at address j is the sum of u_k v_{j−k} with all indices taken modulo the axis lengths.
- `radix-digit-convolution`: Integer product as digit convolution: Splitting two integers into radix-2^b digits turns their product into a convolution of the digit sequences followed by carry propagation.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q} (and its opposite-sign version) that turns cyclic convolution into pointwise multiplication.
- `multidimensional-transform`: Multidimensional transform: The tensor product of one-dimensional transforms applied along each axis of an array whose axis lengths are t_1,…,t_D; convolution on the product of cyclic groups becomes pointwise multiplication.
- `fft-butterfly`: Two-point butterfly and radix-two recursion: The operation H₀(u,v) = ((u+v)/2, (u−v)/2) on a pair of entries, and the decimation-in-frequency recursion that builds a length-2^a transform from a, such layers interleaved with twiddle multiplications.
- `contraction-error`: Contractions and error accumulation: A linear map that does not increase the sup norm is a contraction; approximating contractions on a fixed-point grid of 2^{−p} spacing adds errors without amplifying them.
- `crt-axis-map`: Chinese-remainder map to prime axes: An algebra isomorphism from cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to convolution on the product of cyclic axes of lengths s_i, implemented by triangular controlled shifts.
- `prime-axis-lengths`: Prime axis lengths near powers of two: Choosing distinct odd primes s_i slightly below the powers of two t_i so their product fills a fixed fraction of the padded box and each ratio t_i/s_i leaves room for resampling.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's identity expressing a Fourier transform of prime-product length s as a transform of power-of-two length t, between two cheap Gaussian-weighted linear contractions A and B₀.
- `chirp-identity`: Bluestein chirp identity: A Fourier transform of even length t can be written as pointwise multiplication by a chirp phase a, a cyclic convolution with a, and another chirp multiplication.
- `permutation-cancellation`: Retained permutations cancel in a convolution: The coordinate permutations left inside the resampled transform cancel across two forward transforms, a pointwise product and an opposite-sign transform, so no full sort is executed.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: The complex polynomials of degree below r with y^r = −1; multiplying by a power of y just shifts the coefficient list and flips some signs.
- `phase-twist`: Coefficient phase twist: Substituting x_d ↦ ζy with ζ = e^{πi/r} multiplies coefficient k by ζ^k and turns cyclic convolution of length r into negacyclic polynomial multiplication, exactly undone by untwisting.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the negacyclic ring using ω_t = y^{2r/t} as root of unity, so each twiddle multiplication is a signed shift and only butterflies cost arithmetic.
- `bit-reversed-order`: Stored bit-reversed frequency order: The recursion writes outputs in bit-reversed order (record permutation B_t), and the opposite transform consumes that same order, so no reordering is needed between the forward transforms and the inverse.
- `kronecker-packing`: Signed Kronecker packing: Packing the coefficients of two polynomials into big signed integers (evaluation at 2^{4p}), multiplying with the fast integer multiplier and unpacking the coefficients.
- `ring-convolution`: Convolution over the polynomial ring: Normalized convolution of arrays with entries in the negacyclic ring: forward synthetic transforms, pointwise polynomial products by Kronecker packing, and the opposite transform in the retained order.
- `tape-stream-operations`: Arrays and elementary stream operations on tape: Arrays stored in lexicographic address order, with linear-time scans that split on a digit, apply a pointwise map and merge, or distribute whole rows among streams.
- `controlled-shift`: Controlled shifts and rational scalings: Adding to a later address field an offset computed from earlier control fields, or multiplying it by a rational unit, in linear time by splitting and re-merging blocks.
- `exchange-network`: Bank-exchange network with restored scratch wires: A fixed network of linear gates on wires, built from three-element subsets, that swaps two banks X and Y with a sign and returns every auxiliary scratch wire to its arbitrary initial value.
- `frames`: Frames on network wires: Choosing an invertible operator D_v on the array carried by a wire at each gate, so a pointwise linear gate commutes with it and the intermediate frames cancel, leaving only the endpoint operator on every role.
- `subspace-labels`: Nested subspace labels and orthogonal residuals: Subspaces of a fixed m-dimensional bilinear space attached to gates and terminals, nested along edges; an edge's orthogonal residual has dimension equal to the number of smaller operations the edge needs.
- `rank-saving`: Strict rank saving: The total rank s of all edge changes in the fixed network is strictly less than W·m (wires times label dimension), which makes each recursive level cost a factor s/W < m.
- `matrix-factorization`: Lower-triangular factorization of a matrix: Every rational m×m matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
- `matrix-shear`: Cost of a matrix shear on address fields: The map (H,D) ↦ (H+AD,D) over Z/q^b for a rational matrix A of rank a is done with exactly a interchanges of b-digit fields plus linear extra work.
- `power-width-interchange`: Power-width chunk interchange: Interchanging two address chunks of m^k digits by running the bit network on W cyclic role streams, with one smaller interchange per unit of edge rank, giving the recurrence F_k ≤ (s/W)F_{k−1} + O(1) and cost O(V e^τ).
- `chunk-interchange`: Address chunk interchange: Swapping two disjoint equal-width bit chunks of an address array in O(V u^τ) steps for a fixed τ < 1, by XOR combinations whose final effect is an exact permutation.
- `phase-frames`: Phase frames and the two-point kernel C: The complex network uses frames diagonalized by Hadamard matrices with phases i^{wt}; an edge change becomes a product of kernels C = H S H = aI + bX, which are translations of the array, and H₀ = b S C S.
- `packed-selected-bit-addition`: Packed selected-bit addition: XORing corresponding selected bits of two address chunks by constantly many cyclic shifts of whole chunk ranges plus a deterministic repair of an explicitly small set of exceptional addresses, using a third chunk as restored scratch.
- `guard-bits`: Exact dyadic intermediates with one truncation: Intermediate values in a butterfly layer are exact Gaussian dyadics held with enough guard bits, and a single truncation to the 2^{−p} grid follows the whole contractive layer.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀ to one selected bit in each of D address chunks at once, on arrays of ring records, in O(V d^{λ′}) with λ′ < 1 instead of D whole-array passes, via the recursive complex network on packed bit changes.
- `transform-layout`: Transform layout and cost: Placing the selected bits of all participating axes at a common offset in K-bit chunks, so each round of the synthetic transform uses the simultaneous layer, at total normalized cost dK + pK^{τ−1} + ℓd^{λ′}.
- `parameter-choice`: Parameter choice for the multiplier: Fixed rational exponents (τ, σ, λ′, c, ε, δ, κ) and sizes b = ⌈log₂n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, T ≈ n/b, r = 2^ℓ, with prime axis lengths s_i < t_i.
- `exact-recovery`: Exact recovery by rounding and carries: Removing the known normalizations S and 2^{2b+4}, showing the recovered coefficient error is below 1/2, rounding to integers, and propagating radix carries to output the exact 2n-bit product.
- `multiplication-algorithm`: The multiplication algorithm: Digits are placed on prime axes by the CRT map, transformed by resampling plus chirp convolution over the polynomial ring for both operands, multiplied pointwise, transformed with opposite sign, rescaled, rounded and carried.
- `time-bound`: Complete time bound: Dividing costs by the volume Tp, seven dominant terms with powers of p below one (margins g₁,…,g₇) show total time O(n (lg n)^{1−κ}); the smallest margin is 2κ.
- `main-theorem`: Sub-n-log-n integer multiplication: A single deterministic multitape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model.

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
