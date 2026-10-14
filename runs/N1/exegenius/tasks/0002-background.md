# exegenius task 0002-background

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N1` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bounds on running time up to a constant factor.
- `polynomials`: Polynomials (known to the reader): Finite sums of coefficients times powers of an indeterminate, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with real a, b, including roots of unity and the modulus.
- `multitape-turing-machine`: Multitape Turing machine (known to the reader): A Turing machine with a fixed finite alphabet and a fixed number of one-dimensional tapes, each head moving at most one cell per step.
- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
- `hvdh-multiplier`: Established O(n log n) multiplier: Harvey and van der Hoeven's fixed-tape O(n log n) integer multiplication algorithm, used here only as an ordinary subroutine on short records.
- `cyclic-convolution`: Cyclic convolution: The product of coefficient arrays in which indices add modulo the array length, i.e. polynomial multiplication modulo x^S − 1.
- `radix-digit-convolution`: Radix-digit convolution: Writing each input as a polynomial in 2^b, so that the product becomes a convolution of small digit coefficients followed by carry propagation.
- `dft`: Normalized discrete Fourier transform: The map sending a length-q vector to its averages against the q-th roots of unity; it is a contraction and turns cyclic convolution into pointwise multiplication.
- `stream-array-layout`: Array streams and logical volume: Arrays are stored on tape in lexicographic order of their address fields with implicit addresses, and the logical volume V is the number of stored data bits.
- `elementary-stream-ops`: Elementary stream operations: Linear-time tape operations that permute or move a single fixed-radix digit of the address, split and merge streams on a digit, and split rows cyclically into a fixed number of streams.
- `controlled-shifts`: Controlled shifts: A linear-time update adding to a later address field an offset computed from earlier control fields (or scaling it by a fixed unit), implemented by splitting and remerging blocks.
- `crt-address-map`: Chinese-remainder address map: The isomorphism x ↦ ∏ x_i^{μ_i} that turns one cyclic convolution of length S = ∏ s_i into a multidimensional cyclic convolution on distinct prime axes, implemented by triangular controlled shifts and axis moves.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of prime length s through one of nearby power-of-two length t, using Gaussian-weighted contractions.
- `retained-permutations`: Resampling with retained permutations: Keeping the coordinate permutations P_s and P_t inside the resampling identity P_sF_s = 2^{2α²}B₀P_tF_tA instead of sorting, and letting the source permutation cancel across forward transforms, pointwise product, and opposite transform.
- `tensor-resampling`: Tensor resampling interface: Applying the one-dimensional resampling maps line by line along each of d axes of a padded power-of-two box, with axis exposure done by chunk interchanges.
- `bluestein-chirp`: Bluestein's chirp identity: Writing a Fourier transform, including its frequency permutation, as pointwise multiplication by a chirp, a cyclic convolution with the chirp, and another chirp multiplication.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree below r with y^r = −1, where multiplication by a power of y is a signed cyclic shift of coefficients.
- `phase-twist`: Coefficient phase twist: The map x_d ↦ ζy with ζ = e^{πi/r} that converts cyclic convolution along the last axis into negacyclic multiplication modulo y^r + 1.
- `butterfly`: Normalized butterfly H₀: The two-point map (u, v) ↦ ((u+v)/2, (u−v)/2), the basic step of radix-two Fourier transforms.
- `gaussian-dyadics`: Gaussian dyadics and fixed-point truncation: Complex numbers whose real and imaginary parts have power-of-two denominators, stored exactly in fixed-point words and truncated toward zero to the p-bit grid only at the end of a layer.
- `synthetic-fft`: Synthetic polynomial transform: A radix-two Fourier transform over the ring modulo y^r + 1 whose roots of unity are powers of y, so twiddles are signed shifts; its output is stored in bit-reversed frequency order.
- `linear-network`: Linear bank-exchange network: A fixed finite network of linear gates on wires (roles) that exchanges two banks of values with prescribed signs while restoring every auxiliary scratch value.
- `scratch-restoration`: Restoration of arbitrary scratch values: An eight-row schedule that subtracts the effect of unknown scratch contents, adds the intended computation, and uncomputes, so scratch wires may start with arbitrary values.
- `triple-gadget`: Three-element-subset gather and scatter: Gates indexed by three-element subsets of [100]: gather and scatter produce coefficients depending on intersection size, and side wires cancel the unwanted ones so the net effect is y ← y + x.
- `frame-invariant`: Frames and the common-frame identity: Storing each wire's array through an invertible operator (frame) that is common at each gate, so pointwise gates commute with frames and only endpoint frames determine the net operator.
- `subspace-labels`: Nested subspace labels: Nondegenerate subspaces of a fixed bilinear space attached to gates and terminals, nested along each edge, whose orthogonal residual dimensions count the smaller operations an edge needs.
- `rank-deficit`: Rank deficit of the network: The property that the total number s of smaller calls over all edges is strictly less than the wire count W times the label dimension m.
- `address-shear`: Address shear: The array permutation moving the entry at address (H, D) to (H + MD, D) for a matrix M acting on two groups of address fields.
- `bit-motif-interface`: Rational matrix interface: The bit network with XOR gates and rational projection matrices on its vertices, whose endpoint matrices differ by the identity on every role and whose edge ranks sum to s_b < W_b·m.
- `lower-triangular-factorization`: Lower triangular factorization: Writing any rational matrix of rank a as E₁ΠE₂ with invertible lower triangular E₁, E₂ and a partial permutation Π with a ones, a reversed Bruhat factorization.
- `matrix-shear-cost`: Cost of a rational matrix shear: A shear (H, D) ↦ (H + AD, D) by a fixed rational matrix of rank a costs exactly a interchanges of smaller field pairs plus linear work.
- `row-splitting`: Row splitting among roles: Distributing rows of an array cyclically among the W wire roles so that each role stream has the same address shape and volume V/W.
- `volume-recurrence`: Volume-normalized recurrence: The recurrence F_k ≤ (s/W)F_{k−1} + O(1) for cost divided by volume, which yields a power saving because s/W < m.
- `chunk-interchange`: Fast address chunk interchange: A fixed-tape procedure that exchanges two equal-width contiguous address chunks of u bits in O(Vu^τ) time with τ < 1, via XOR combinations of data driven by the bit network.
- `phase-frames`: Binary phase frames: Frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} attached to binary labels, whose edge changes factor into one two-point kernel aI + bX_v per residual basis vector.
- `complex-motif-interface`: Binary phase interface: The complex network with binary labels: after endpoint corrections it applies the tensor power of the kernel C on every role using s_c < W_c·m smaller kernel calls.
- `packed-selected-bit`: Packed selected-bit addition: XORing selected bits of one address chunk into another by eight packed cyclic shifts with guard bits, followed by deterministic repair of an explicitly bounded set of exceptional addresses.
- `simultaneous-layer`: Simultaneous butterfly layer: Applying H₀ on the same bit position in up to d address chunks at once in O(Vd^{λ'}) time, λ' < 1, by recursing through the complex network and evaluating the layer exactly before one truncation.
- `transform-layout`: Transform layout: A positional permutation of address bits placing the bits used in each transform round at a common offset in consecutive K-bit chunks, so simultaneous layers apply and the frequency order is retained.
- `signed-packing`: Signed coefficient packing: A signed Kronecker substitution that evaluates integer polynomials at B₀ = 2^{4p}, multiplies with the established multiplier, and recovers coefficients by centered residues, giving products in the ring modulo y^r + 1.
- `synthetic-convolution`: Convolution from the retained transform layout: Normalized convolution over the polynomial ring computed by two forward synthetic transforms, pointwise packed products in the stored order, and the opposite transform consuming that order.
- `exact-recovery`: Exact recovery by rounding and carries: Undoing known scales, rounding each approximate coefficient whose error is below 1/2 to the exact integer, and propagating radix-2^b carries to obtain the binary product.
- `cost-table`: Parameter choice and cost table: Fixed rational parameters (τ = 1 − 2^{-50}, ε = 2^{-75}, κ = 2^{-182}, …) under which every term of the cost per bit is at most p^{1−2κ}.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-alphabet multitape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{-182}, refuting the n log n lower-bound conjecture in this model.

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
