# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/G2` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on growth rate of a running time.
- `polynomials`: Polynomials (known to the reader): Expressions Σ a_k y^k added and multiplied by collecting powers.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with i²=-1, including unit-modulus roots of unity e^{2πi/k}.
- `multitape-turing-machine`: Multitape Turing machine (known to the reader): A machine with a fixed finite alphabet and a fixed number of one-dimensional tapes, each step reading, writing and moving one cell per tape.
- `xor-bits`: Bit XOR (known to the reader): Addition of bits modulo 2.
- `nlogn-conjecture`: The n log n conjecture and prior bounds: Schönhage–Strassen's 1971 bound O(n log n log log n), their conjecture that n log n is optimal, and Harvey–van der Hoeven's O(n log n) upper bound for multitape machines.
- `tape-streams`: Arrays as tape streams and elementary scans: Arrays stored in lexicographic address order on tapes, with logical volume V (number of stored bits), whose splitting, merging and digit moves cost linear time.
- `controlled-shift`: Controlled shifts and rational scalings: A linear-time tape operation that adds an offset, computed from earlier control fields, to a later address field modulo a prime power, or multiplies it by a rational unit.
- `fixed-point-dyadics`: Fixed-point and Gaussian dyadic arithmetic: Complex numbers stored as signed two's-complement grid numerators over 2^p, added and scaled exactly with guard bits and truncated once toward zero.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{-2πijk/q} on length-q vectors, a contraction in the max norm.
- `cyclic-convolution`: Cyclic convolution: The product of two coefficient arrays indexed by ℤ/tℤ (or a product of such groups) as in multiplication of polynomials modulo x^t−1; the Fourier transform turns it into pointwise multiplication.
- `multiplication-as-convolution`: Multiplication as convolution of radix digits: Splitting both integers into radix-2^b digits makes the product a convolution of the digit coefficient lists, followed by carry propagation.
- `multidimensional-transform`: Multidimensional transform: The tensor product of one-dimensional Fourier transforms along several axes, computing convolution on a product of cyclic groups.
- `crt-address-map`: Chinese-remainder address map: An algebra isomorphism Φ sending x to Π x_i^{μ_i} that turns cyclic convolution of length S=Πs_i (pairwise coprime) into convolution on the product of cyclic axes, implemented by triangular controlled shifts.
- `ring-mod-y-r-plus-1`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree below r in which y^r = −1, so powers of y are roots of unity and multiplying by y^a is a signed cyclic shift of coefficients.
- `two-point-butterfly`: Two-point butterfly layer: The map H₀(u,v)=((u+v)/2,(u−v)/2) applied to pairs, whose repeated layers build a radix-2 fast Fourier transform.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the ring ℂ[y]/(y^r+1) using ω_t = y^{2r/t} as root of unity, so multiplications by roots are exact signed shifts and only butterflies remain.
- `kronecker-packing`: Signed packing for ring products: Multiplying two polynomials in the ring by packing signed coefficients into big integers (Kronecker substitution) and calling an O(N log N) integer multiplier.
- `nlogn-multiplier`: The established O(N log N) multiplier: The Harvey–van der Hoeven fixed-tape multiplier with cost O(N log 2N) on N-bit inputs, used only as an ordinary subroutine on short inputs.
- `linear-algebra-orthogonality`: Subspaces, bilinear forms and orthogonal complements: A subspace of a vector space with a nondegenerate bilinear form, its orthogonal complement, the projection onto it, and the dimension (rank) of the difference of two nested subspaces.
- `linear-network`: Linear network with restored scratch wires: A fixed circuit of linear gates on wires that exchanges two banks of values with a sign while arbitrary initial values on auxiliary scratch wires are cancelled and restored.
- `triple-subset-gadgets`: Triple-subset intersection gadgets: Gather, scatter and side-injection gates indexed by three-element subsets of a 100-element set, whose coefficients depend on intersection size and whose side wires cancel the unwanted terms.
- `frames`: Frames on wire arrays: Invertible linear operators D_v on each wire's address-indexed array so that stored array = D_v applied to the logical array, commuting with pointwise gates so only edge changes D_v D_u^{-1} cost anything.
- `rank-deficit-labels`: Nested subspace labels and the rank deficit: Subspaces attached to gates and terminals so that adjacent labels are nested and the total rank s of all edge changes is strictly below the wire count times dimension, s < Wm.
- `recursive-power-saving`: Recursive power saving from the rank deficit: A call at parameter m·f uses s calls at parameter f on streams of volume V/W, so cost per volume grows like m^τ rather than m, with τ<1 because s/W<m.
- `lower-triangular-factorization`: Lower triangular factorization: Every rational matrix A of rank a equals E₁ΠE₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
- `matrix-shear`: Matrix shear on address fields: The address permutation (H,D)→(H+AD,D) modulo a prime power, which costs exactly rank(A) interchanges of b-digit fields plus linear work.
- `fast-chunk-interchange`: Fast interchange of address chunks: Swapping two disjoint contiguous address fields of u bits in an array of volume V in time O(V u^τ) for fixed τ<1, via XOR combinations of intermediate streams that finally form an exact permutation.
- `phase-frames`: Binary phase frames and the two-point kernel C: Frames C_U=H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} over Gaussian dyadics, whose edge changes are products of translation kernels aI+bX, composing to C^{⊗m} on every role.
- `packed-selected-bit-addition`: Packed selected-bit addition: Adding corresponding selected bits of two address chunks using a third temporary chunk, via cyclic whole-chunk shifts plus a deterministic correction of an explicit small set of exceptional addresses.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: One H₀ butterfly at the same bit offset in up to d address chunks applied to all polynomial records at cost O(V d^{λ'}) for fixed λ'<1, evaluated exactly in dyadics with one final truncation.
- `synthetic-transform-layout`: Synthetic transform tape layout: A tape layout placing the selected bits of the participating axes at a common offset in consecutive K-bit chunks so that parallel layers apply, with the frequency order retained.
- `synthetic-convolution`: Normalized convolution over the ring: Convolution of arrays over ℂ[y]/(y^r+1) as inverse transform of the pointwise product of forward transforms in the same frequency order, scaled by 1/T, with polynomial products done by signed packing.
- `phase-twist`: Last-coordinate phase twist: The isomorphism x_d→ζy, ζ=e^{πi/r}, from ℂ[x_d]/(x_d^r−1) to ℂ[y]/(y^r+1) that turns cyclic wrap into negacyclic wrap and back.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven method that expresses a Fourier transform of length s (coprime lengths) through a transform whose axis lengths are powers of two, via contractive Gaussian maps.
- `resampling-without-sorting`: Resampling with permutations left in the transform: The identity P_s F_s = 2^{2α²} B₀ P_t F_t A (and its tensor form) keeping both coordinate permutations inside the formula instead of sorting twice on each coordinate.
- `bluestein-chirp`: Bluestein chirp identity: A Fourier transform (with its permutation) rewritten as a pointwise chirp multiplication, a cyclic convolution with the chirp, and another chirp multiplication; the source permutation cancels across the product of two transforms.
- `error-and-exact-recovery`: Error bounds and exact recovery: Contraction-based accumulation of approximation errors through all steps, removal of known normalizations and scales, showing the coefficient error is below 1/2 so rounding gives exact integers.
- `parameter-choice`: Parameter choice and cost table: Fixed rational exponents (τ=σ=1−2^{−50}, ε=2^{−75}, κ=2^{−182}, …) and sizes p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T≈n/b, r=2^{⌈log₂T/d⌉} making every cost term a power of p below one.
- `multiplication-algorithm`: The multiplication algorithm: Digit extraction, the Chinese-remainder map, two forward source transforms, pointwise product, opposite transform, rescaling, rounding and carry propagation yielding the exact 2n-bit product.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplying two n-bit integers in O(n(lg n)^{1−κ}) time with κ=2^{−182}, refuting the n log n optimality conjecture in this model.

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
