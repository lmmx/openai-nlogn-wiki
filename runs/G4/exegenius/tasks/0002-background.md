# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/G4` (paths below are relative to it)

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
- `polynomial`: Polynomials (known to the reader): Expressions Σ a_k x^k with addition and multiplication, including coefficient lists.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi, with modulus, conjugate and roots of unity e^{2πi/q}.
- `turing-machine`: Turing machines and tapes (known to the reader): Machines with a finite control, tapes of cells and read/write heads that move one cell per step.
- `fixed-tape-model`: Fixed-tape Turing machine model: The model where one machine has a fixed finite alphabet and a fixed finite number of one-dimensional tapes, each step touching one cell per tape, so time counts head movement as well as arithmetic.
- `elementary-stream-ops`: Elementary stream operations on tape arrays: Linear-time scans on an array stored in lexicographic order: swapping or moving one digit, splitting into streams by a digit or cyclically by rows, applying a pointwise map, and merging back.
- `controlled-shift`: Controlled shifts and rational scalings: An O(V) tape operation that adds an offset computed from earlier fields to a later field modulo q^b (a cyclic shift), or multiplies it by a fixed rational unit.
- `convolution`: Convolution: The product of two coefficient lists, cyclic when indices wrap around modulo the length, equal to polynomial multiplication modulo x^S − 1.
- `radix-digit-convolution`: Integer multiplication as digit convolution: Writing each n-bit integer as a polynomial in 2^b with digits of b bits, so the integer product is a convolution of digit lists followed by carry propagation.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ u_j e^{−2πijk/q}, which turns convolution into pointwise multiplication.
- `fft-butterfly`: Radix-2 butterflies and FFT: Computing a power-of-two transform by repeated two-point butterflies (u,v) ↦ ((u+v)/2,(u−v)/2) followed by twiddle multiplications and smaller transforms (decimation in frequency).
- `linear-subspaces`: Subspaces, rank and orthogonal complements: Linear algebra over Q or F_2: subspaces, matrix rank, bilinear forms, orthogonal complements and projections.
- `fixed-point-precision`: Fixed-point disk arithmetic and truncation error: Storing complex numbers of modulus at most 1 as signed binary numerators over 2^p, truncating toward zero, and tracking how contractions and bilinear maps propagate the errors.
- `nlogn-multiplier`: Established O(n log n) integer multiplier: The Harvey–van der Hoeven fixed-tape multiplier with cost O(N log N) on N-bit inputs, used only as an ordinary subroutine on short records.
- `synthetic-ring`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree below r with y^r = −1, where multiplying by a power of y is a signed shift of the coefficient list.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform whose roots of unity are ω_t = y^{2r/t} in the ring modulo y^r + 1, so twiddles are signed shifts, computed by butterfly rounds with outputs left in bit-reversed order.
- `signed-packing`: Signed packing of polynomial products: Kronecker substitution: evaluating ring polynomials at 2^{4p} to multiply them with the integer multiplier, then reading coefficients back by centered residues.
- `phase-kernel-c`: Two-point kernel C and phase frames: The matrix C = H S H = aI + bX with C^2 = X and H_0 = b S C S, so a butterfly layer is a phase-conjugated tensor power of C.
- `frames-on-arrays`: Frames on pointwise linear networks: Replacing scalars on wires by arrays and assigning each gate an invertible frame operator that commutes with the gate, so edges only change representation and the endpoint operators telescope.
- `exchange-network`: Subset-intersection exchange network: A fixed linear network of copy, gather, scatter and side wires indexed by three-element subsets that swaps two banks X and Y with a sign and restores arbitrary scratch values.
- `subspace-labels`: Subspace labels and the rank budget: Nested nondegenerate subspaces attached to gates so each edge's dimension change counts the smaller operations needed, with total dimension lost small enough to give a strict deficit.
- `recursive-power-saving`: Recursive power saving from a rank deficit: If a call at parameter mf is made from s calls at parameter f on streams of volume V/W with s < Wm, the normalized cost grows like m^τ per level with τ < 1.
- `bit-network-interface`: Bit network shear interface: The bit version of the network with rational matrices M_v at gates such that the endpoint difference is the identity, i.e. the shear H ← H + D, with rank sum s_b < W_b m.
- `triangular-factorization`: Lower triangular (Bruhat-type) factorization: Every rational matrix A of rank a factors as E_1 Π E_2 with lower triangular invertible E_1, E_2 and a partial permutation Π with a ones.
- `matrix-shear`: Cost of a rational matrix shear: The map (H,D) ↦ (H + AD, D) over Z/q^b costs exactly rank(A) interchanges of b-digit fields plus O(V) other work.
- `power-width-interchange`: Power-width address interchange: Swapping two chunks of m^k digits by running the bit network with matrix shears as edges, each edge recursing into smaller interchanges, in time O(V e^τ).
- `chunk-interchange`: Fast chunk interchange: Exchanging two equal-width address fields of u bits in an arbitrary array in O(V u^τ) time for a fixed τ < 1, even though intermediate steps XOR data together.
- `complex-phase-network`: Complex phase network: The complex-scalar version of the exchange network with binary labels whose phase frames i^{wt(Px)} reduce to translation kernels aI + bX_v, giving C^{⊗m} on every role with s_c < W_c m.
- `packed-selected-bit-addition`: Packed selected-bit addition: Adding corresponding selected bits of two address chunks (a binary row addition) by a constant number of cyclic shifts of whole chunk ranges plus a deterministic repair of a small exceptional address set.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H_0 to the same bit position in up to d address chunks at once, exactly in dyadic arithmetic and truncating once, in O(V d^λ') time for λ' < 1.
- `synthetic-transform-layout`: Synthetic transform layout and cost: Placing the selected bits of all axes at a common offset in K-bit chunks so each transform round is a simultaneous layer, with the output frequency order retained for reuse.
- `synthetic-convolution`: Convolution from the retained transform layout: Normalized convolution over the polynomial ring by two forward synthetic transforms, pointwise ring products via signed packing, and the opposite transform consuming the same stored order.
- `convolution-twist`: Coefficient twist to the negacyclic ring: The map x_d ↦ ζy with ζ = e^{πi/r} that turns cyclic convolution in the last coordinate into convolution modulo y^r + 1, so complex cyclic convolution reduces to the synthetic one.
- `gaussian-resampling`: Gaussian resampling: Relating a Fourier transform of coprime length s to one of larger power-of-two length t via Gaussian-weighted contractions A and B_0, as P_sF_s = 2^{2α²} B_0 P_t F_t A.
- `tensor-resampling`: Multidimensional resampling on a padded box: Applying the one-dimensional resampling maps along each axis of the padded power-of-two box, exposing each axis by chunk interchanges, with permutations left inside the transform.
- `chirp-identity`: Bluestein chirp identity: Writing a Fourier transform (with its target permutation) as a pointwise chirp phase, a cyclic convolution with the chirp, and another chirp phase.
- `permutation-cancellation`: Source permutation cancellation: The coordinate permutation retained from resampling cancels across the two forward transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S².
- `crt-axis-map`: Chinese-remainder axis map: Mapping a cyclic convolution of length S = ∏ s_i with pairwise coprime s_i to a multidimensional cyclic convolution via x ↦ ∏ x_i^{μ_i}, implemented by triangular controlled shifts and axis moves.
- `parameter-choices`: Parameter choices: Choosing b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two axis lengths t_i near r and distinct primes s_i just below them, so Tp = Θ(n) and all hypotheses hold.
- `exact-recovery`: Exact recovery of the integer product: Showing the accumulated numerical error on the recovered coefficients is below 1/2, rounding to integers, and propagating radix carries to the exact 2n-bit product.
- `multiplication-algorithm`: The multiplication algorithm: Digit polynomials are mapped by the CRT map to prime axes, transformed by resampling plus chirp-convolution (via the twist and synthetic convolution), multiplied pointwise, inverse transformed, rescaled, rounded and carried.
- `cost-accounting`: Complete time bound: Summing the normalized costs of layouts, butterfly rounds, resampling, chirps and packed products, each at most p^{1−2κ}, to get O(n (log n)^{1−κ}).
- `sub-nlogn-multiplication`: Sub-n log n integer multiplication: A deterministic multitape Turing machine multiplies two n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, disproving the n log n optimality conjecture in that model.

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
