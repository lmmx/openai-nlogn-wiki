# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/O2` (paths below are relative to it)

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

- `big-o-notation`: Big-O notation (known to the reader): Asymptotic upper-bound notation O(f(n)) for running times up to constant factors.
- `polynomials`: Polynomials (known to the reader): Expressions Σ a_k x^k with coefficients in a ring, added and multiplied term by term.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, including unit-modulus phases e^{iθ}.
- `multitape-turing-machine`: Multitape Turing machine (known to the reader): A Turing machine with a finite alphabet and several one-dimensional tapes, each with its own head moving one cell per step.
- `linear-algebra-bilinear`: Nondegenerate bilinear spaces: A vector space with a symmetric bilinear form having no nonzero vector orthogonal to everything, so each nondegenerate subspace U splits the space as U ⊥ U^⊥ with an orthogonal projection P_U.
- `tensor-products`: Tensor products: The tensor product of vector spaces or linear maps, used to build multidimensional transforms, label spaces F^{⊗3}, and operators acting independently on several coordinates.
- `fixed-tape-model`: Fixed finite-tape machine model and stream operations: The model of one machine with a fixed alphabet and fixed number of tapes, where arrays are stored in lexicographic address order and elementary scans (digit moves, row splits, pointwise maps) cost time linear in the logical volume V of stored bits.
- `controlled-shifts`: Controlled shifts and rational scalings: A linear-time stream operation that adds to a later address field an offset computed from earlier fields, or multiplies it by a fixed rational unit, modulo q^b, by splitting and re-merging blocks.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πijk/q} and its opposite-sign inverse F_q^+, contractions for the max norm, applied axis by axis on multidimensional arrays.
- `cyclic-convolution`: Cyclic convolution: The product in ℂ[x]/(x^S − 1): coefficient lists are combined with indices added modulo S, and transforms turn it into pointwise multiplication.
- `radix-digit-convolution`: Multiplication by radix-digit convolution: Splitting each n-bit input into radix-2^b digits turns integer multiplication into convolution of short integer coefficient lists followed by carry propagation.
- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's 1971 proposal that Θ(n log n) is the optimal order of n-bit integer multiplication on multitape Turing machines; disproving it requires one machine with T(n)/(n lg n) → 0.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The 2021 deterministic multitape algorithm multiplying N-bit integers in O(N log N) time via Gaussian resampling and Nussbaumer polynomial transforms; here it is both the base of the reduction and an ordinary subroutine.
- `gaussian-dyadics`: Gaussian dyadic fixed-point arithmetic: Exact arithmetic on complex numbers whose real and imaginary parts have power-of-two denominators, stored as signed fixed-point words on the p-bit disk grid and truncated toward zero by Q_p.
- `error-accounting`: Disk-grid approximation and error accounting: Each routine approximates a linear contraction on the p-bit disk grid with an error bound in units of 2^−p, and composed errors add because contractions do not amplify input errors.
- `butterfly-h0`: Normalized butterfly H₀: The two-point map H₀(u, v) = ((u+v)/2, (u−v)/2), the radix-two step of a Fourier transform, applied coefficientwise to polynomial records.
- `ring-y-r-plus-1`: Polynomial ring ℂ[y]/(y^r + 1): The ring R_r of complex polynomials of degree below r with y^r = −1, where powers of y are 2r-th roots of unity and multiplying by them is a signed cyclic shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer–Quandalle Fourier transforms over arrays of R_r elements using ω_t = y^{2r/t} as roots of unity, computed by radix-two decimation-in-frequency rounds of butterflies and monomial twiddles, with outputs left in bit-reversed stored frequency order.
- `signed-packing`: Signed packing (Kronecker substitution): Multiplying two polynomial records of R_r by packing their signed fixed-point coefficients into large integers, calling the O(N log N) integer multiplier, and unpacking the exact product.
- `bank-exchange-network`: Bank-exchange linear network: A fixed linear network of wires (roles) and pointwise gates—copy, gather, scatter, side injection on a schedule of eight rows over three stages—that maps two data banks (X, Y) to (−Y, X) while restoring arbitrary initial scratch values.
- `triple-intersection-construction`: Three-element subset intersection construction: Indexing data by 3-element subsets of a 100-element set so that gather/scatter through central wires yields coefficients depending on |S ∩ T| (mod 2 or minus one), with side wires cancelling unwanted neighbor terms, as in Frankl–Wilson/Alon and index-code decoding.
- `frames`: Frames and the common-frame identity: Assigning each network vertex an invertible operator D_v on wire arrays so that stored data is D_v g; pointwise gates commute with a common frame, so a route from role w to ρ(w) applies only D_sink D_source^{−1} and intermediate frames cancel.
- `subspace-labels`: Subspace labels and orthogonal residuals: Nested nondegenerate subspaces of the m-dimensional space F^{⊗3} attached to gates and terminals; on each edge the orthogonal residual's dimension counts the smaller operations needed for that edge's frame change.
- `rank-saving`: Rank saving s < Wm: The decisive inequality that the total number s of smaller calls over all edges (sum of residual dimensions or ranks) is strictly less than the wire count W times the label dimension m.
- `power-saving-recursion`: Volume-normalized recursion: Splitting rows cyclically among W roles makes each of s child calls act on volume V/W, so cost per bit obeys F_k ≤ (s/W)F_{k−1} + O(1), and s/W < m^τ yields a power saving e^τ in the parameter.
- `address-shears`: Address shears (H, D) ↦ (H + MD, D): Array permutations Φ_M that add a rational matrix M times one address-field vector D to another H modulo q^b; the bit network's rational matrix interface makes the endpoint operator the shear H ← H + D on every role.
- `lower-triangular-factorization`: Lower triangular (Bruhat) factorization: Writing a rank-a rational matrix as E₁ Π E₂ with invertible lower triangular E₁, E₂ and a partial permutation Π with a ones, so a matrix shear costs a field interchanges plus linear-time triangular updates.
- `fast-interchange`: Fast address-chunk interchange in O(V u^τ): The first tape procedure: exchanging two disjoint u-bit address fields of a stored array in O(V u^τ) time, τ = 1 − 2^−50, by recursively applying the bit network with XOR gates and row splits, rather than by data movement alone.
- `phase-frames`: Binary phase frames: The complex network's frames 𝒞_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} for binary labels U, whose edge changes factor into one two-point kernel C = aI + bX per orthonormal residual vector and telescope to C^{⊗m} on every role.
- `packed-selected-bit-addition`: Packed selected-bit addition: A tape operation XORing the selected bits of one address chunk into the corresponding bits of another, using a temporary chunk, whole-chunk cyclic shifts and a sorted correction of a small explicit exceptional set.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer in O(V d^λ′): The second tape procedure: applying H₀ on the same bit of up to d address chunks at once in O(V d^λ′) time, λ′ < 1, by recursing through the complex phase network, then converting C^{⊗D} to H₀^{⊗D} with diagonal phases and a dyadic scale before one final truncation.
- `synthetic-transform-layout`: Synthetic transform tape layout and cost: Arranging the axes of a multidimensional synthetic transform so that each round's selected bits sit at a common offset in K-bit chunks, letting simultaneous butterfly layers and chunk interchanges compute every round.
- `synthetic-convolution`: Normalized convolution over the polynomial ring: Computing the normalized cyclic convolution of R_r-valued arrays by two forward synthetic transforms kept in their stored frequency order, pointwise signed-packed polynomial products, and the opposite transform consuming that order.
- `coefficient-twist`: Coefficient phase twist: The isomorphism x_d ↦ ζy (ζ = e^{πi/r}) turning cyclic convolution along the last axis into negacyclic multiplication in ℂ[y]/(y^r+1), whose negative wrap reproduces the cyclic wrap after untwisting.
- `crt-address-map`: Chinese-remainder address map: The Agarwal–Cooley isomorphism x ↦ Π x_i^{μ_i} turning one cyclic convolution of length S = Π s_i (distinct primes s_i near powers of two) into a multidimensional cyclic convolution, implemented on tape by triangular controlled shifts.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven identity expressing a Fourier transform of prime length s through one of nearby power-of-two length t, sandwiched between Gaussian-kernel contractions A and B₀ and a power-of-two scale.
- `retained-permutations`: Resampling with retained permutations: Keeping the source and target coordinate permutations R, Q inside the resampling identity R F_s = 2^γ B₀ Q F_t A rather than sorting, so the target permutation is absorbed by the chirp and the source permutation cancels across forward and inverse transforms in a convolution.
- `bluestein-chirp`: Bluestein chirp identity: Writing a (permuted) Fourier transform as pointwise multiplication by a chirp ā, cyclic convolution with the chirp a, and multiplication by ā again, so the middle power-of-two transform becomes a convolution.
- `exact-recovery`: Exact recovery by rounding and carries: Removing known normalizations and digit scales, bounding the total coefficient error strictly below 1/2 so rounding recovers the exact integer convolution, then propagating radix-2^b carries to output the 2n-bit product.
- `parameter-choice`: Parameter choice and cost table: The fixed rational exponents (τ = σ = 1 − 2^−50, λ′ = 1 − 2^−54, c = 2^−56, ε = 2^−75, …) and sizes (b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋) under which every per-bit cost term is at most p^{1−2κ}, giving κ = 2^−182.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-tape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) time with κ = 2^−182, via radix digits, a CRT map, Gaussian resampling with retained permutations, Bluestein chirps, a phase twist and synthetic transforms accelerated by fast interchanges and simultaneous butterfly layers, disproving the n log n conjecture in this model.

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
