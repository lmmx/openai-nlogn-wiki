# exegenius task 0002-background

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e5/N2` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bounds on running time up to constant factors.
- `polynomials`: Polynomials (known to the reader): Expressions built from a variable and coefficients using addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, with their arithmetic, modulus and conjugation.
- `turing-machines`: Multitape Turing machines (known to the reader): A finite-control machine with a fixed number of one-dimensional tapes whose heads move one cell per step.
- `modular-arithmetic`: Modular arithmetic (known to the reader): Arithmetic on integers modulo a fixed modulus.
- `linear-algebra-rank`: Matrices, linear maps and rank: A matrix represents a linear map between coordinate spaces, and its rank is the dimension of its image.
- `binary-field-xor`: The field F₂ and XOR: The two-element field F₂, in which addition is XOR of bits, so that vectors of bits form spaces over F₂.
- `bilinear-forms`: Symmetric bilinear forms and orthogonal complements: A symmetric bilinear form pairs vectors to scalars; it defines orthogonality, orthogonal complements and nondegenerate subspaces.
- `tensor-products`: Tensor products: The tensor product combines vector spaces or operators so that an operator on several coordinates acts factorwise on each.
- `gaussian-dyadics`: Gaussian dyadic numbers: Complex numbers whose real and imaginary parts are fractions with power-of-two denominators, i.e. the ring ℤ[i,1/2], on which the networks compute exactly.
- `cyclic-convolution`: Cyclic convolution: The convolution of two sequences indexed modulo a length, equivalently the product of polynomials modulo xᴸ − 1, possibly over several axes.
- `dft`: Discrete Fourier transform: The linear map taking a length-q vector to its averages against the powers of a q-th root of unity; it turns cyclic convolution into pointwise multiplication.
- `multidimensional-dft`: Multidimensional Fourier transforms: The tensor product of one-dimensional discrete Fourier transforms along each axis of a multidimensional array.
- `butterfly-h0`: Normalized butterfly H₀: The two-point map H₀(u,v) = ((u+v)/2, (u−v)/2), the basic step of radix-two transforms, applied coefficientwise to polynomial records.
- `nlogn-conjecture`: n log n optimality conjecture: Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers, here read as an eventual Ω(n lg n) lower bound for every fixed multitape machine.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The previously established fixed-tape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine and as the source of the Gaussian-resampling method.
- `multiplication-as-convolution`: Integer multiplication as digit convolution: Writing each integer in radix 2ᵇ makes its product the convolution of the digit sequences, followed by carry propagation.
- `tape-array-layout`: Arrays as address-ordered tape streams: An array over a product of address fields is stored on tape in lexicographic order with addresses implicit, and its logical volume V is its number of stored data bits.
- `elementary-stream-ops`: Elementary stream operations: Linear-time tape procedures that permute or move single radix digits of addresses, split and merge streams by a digit, and split whole rows cyclically into a fixed number of streams.
- `controlled-shifts`: Controlled shifts and rational scalings: In linear time a tape machine can add to an address field an offset computed from earlier fields, modulo its range, or multiply that field by a fixed rational unit.
- `linear-network`: Linear networks, wires and roles: A fixed finite network of wires carrying scalars, acted on by pointwise linear gates; a wire's fixed place in the network is its role.
- `scratch-restoration`: Restoring arbitrary scratch values: A schedule that subtracts the effect of the old auxiliary values, adds the source effect, and undoes the auxiliary updates, so the net effect is independent of arbitrary initial scratch contents.
- `subset-construction`: Three-element subset construction: Gates indexed by 3-subsets of a 100-element set: gather and scatter through central wires give coefficients depending on intersection size, and side wires between neighbouring subsets cancel the unwanted ones, so a forward invocation adds x to y.
- `bank-exchange`: Three-stage bank exchange: Applying forward, inverse and forward invocations along the three tensor coordinates sends the two data banks (X,Y) to (−Y,X) while restoring every auxiliary wire.
- `frames`: Frames and the common-frame identity: Each network vertex gets an invertible operator (its frame) describing how the stored array represents the logical one; since a common frame commutes with a pointwise gate, the whole network implements D_out·S·D_in⁻¹ and intermediate frames cancel.
- `subspace-labels`: Subspace labels and orthogonal residuals: Each gate and terminal is labelled by a nondegenerate subspace of a fixed m-dimensional bilinear space, adjacent labels are nested, and the dimension of the orthogonal residual on an edge counts the smaller operations that edge needs.
- `rank-deficit`: Rank deficit s < Wm: The decisive property of each finite network: the total number s of smaller calls needed on its edges is strictly less than the number of wires W times the label dimension m.
- `volume-normalized-recurrence`: Volume-normalized recursion: Dividing cost by data volume, a call at parameter mf makes s calls at parameter f each on volume V/W, so the normalized cost grows by s/W < m per factor m, giving cost O(V·f^τ) with τ < 1.
- `motif-exponents`: Explicit exponents τ and σ: The fixed rational exponents τ = σ = 1 − 2⁻⁵⁰ for the address and butterfly recurrences, justified because both relative rank deficits exceed 20·2⁻⁵⁰.
- `address-shear`: Address shear: The array permutation Φ_M moving the entry at address (H,D) to (H+MD,D) for two vectors H, D of address fields and a matrix M; shears compose additively.
- `bit-network-interface`: Rational matrix interface of the bit network: Assigning projection matrices onto the labels as shear frames makes the XOR bit network apply the shear H ← H + D on every role, with total edge rank s_b < W_b·m.
- `lower-triangular-factorization`: Lower triangular factorization: Every rational matrix of rank a factors as E₁ΠE₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with a ones (a reversed-order Bruhat factorization).
- `matrix-shear-cost`: Cost of a rational matrix shear: A shear (H,D) ↦ (H+AD,D) by a fixed rational matrix of rank a costs exactly a interchanges of smaller field pairs plus linear work, using the triangular factorization and controlled shifts.
- `power-width-interchange`: Power-width chunk interchange: For chunks of e = mᵏ digits with enough rows, splitting rows among the W roles and running the bit network with recursive shears interchanges the chunks in O(V e^τ) time on fixed tapes via a depth-first schedule.
- `chunk-interchange`: Fast address chunk interchange: A fixed tape procedure interchanging two disjoint u-bit address chunks of an array in O(V u^τ) time with τ < 1, by forming XOR combinations of data rather than moving it directly.
- `phase-kernel-c`: Two-point kernel C: The Gaussian dyadic kernel C = H·diag(1,i)·H = aI + bX with a = (1+i)/2, b = (1−i)/2, satisfying H₀ = b·S·C·S, so layers of C convert into normalized butterfly layers.
- `phase-frames`: Binary phase frames: For a binary label U, the frame C_U = H^⊗m · diag(i^{q_U(x)}) · H^⊗m with q_U(x) the Hamming weight of the projection of x mod 4; between nested labels it changes by one translation kernel aI + bX_v per orthonormal residual vector.
- `binary-phase-interface`: Binary phase interface of the complex network: With phase frames on the complex network, s_c translation kernels in total suffice, and after endpoint diagonal corrections and undoing the bank exchange the network applies C^⊗m on every role.
- `packed-selected-bit-addition`: Packed selected-bit addition: XORing bit x into bit y at regularly spaced positions of two address chunks via eight cyclic shifts using a third guard chunk, then deterministically repairing the small explicitly identified set of exceptional addresses.
- `layer-recursion`: Batched recursion for a common layer: Applying C on e = mf selected axes by splitting them into m slots, changing basis with packed row additions, splitting rows among the W roles and recursing s times on volume V/W each.
- `guard-width`: Guard width for exact layer evaluation: An explicit bound on denominator and magnitude growth inside one accelerated layer, giving a coefficient width of O(p) bits so all intermediate Gaussian dyadic values are exact.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀ on the same bit position of up to d address chunks at once, exactly in Gaussian dyadics followed by one truncation, in O(V d^λ′) time with λ′ < 1 instead of d separate passes.
- `fixed-point-grid`: Disk grid values and truncation: Complex values in the unit disk with coordinates in 2⁻ᵖℤ, stored as fixed-width two's-complement words, with truncation Q_p and an error notion that adds along compositions of contractions.
- `negacyclic-ring`: Polynomial ring modulo yʳ + 1: The ring of complex polynomials of degree below r modulo yʳ + 1, in which powers of y are roots of unity and multiplying by one is a signed shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer's normalized Fourier transforms over ℂ[y]/(yʳ+1) using ω_t = y^{2r/t} as root of unity, so they need only signed shifts and butterflies.
- `transform-layout`: Transform layout and stored frequency order: A tape layout placing the selected bits of participating axes at a common offset in consecutive K-bit chunks so simultaneous layers apply, with the frequency order retained for the opposite transform.
- `signed-packing`: Signed coefficient packing: A signed Kronecker substitution packing polynomial coefficients into one integer so the O(n log n) multiplier computes exact products in ℂ[y]/(yʳ+1).
- `synthetic-convolution`: Normalized convolution over the polynomial ring: Computing the normalized cyclic convolution of arrays over ℂ[y]/(yʳ+1) by two forward synthetic transforms, pointwise packed products, and the opposite transform reading the retained frequency order.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of length s through one of a nearby length t via Gaussian-weighted contractions, here with the source and target coordinate permutations kept in the formula instead of sorted.
- `tensor-resampling`: Tensor resampling interface: The tensor product of the one-dimensional resampling identities, RF_s = 2^γ B₀ Q F_t A, applied one coordinate line at a time with chunk interchanges moving axis fields.
- `bluestein-chirp`: Bluestein chirp identity: Writing a Fourier transform, including its target permutation, as pointwise multiplication by a chirp, a cyclic convolution with the chirp, and another chirp multiplication.
- `permutation-cancellation`: Source permutation cancellation: The retained source permutation R cancels across the two forward transforms, their pointwise product and the opposite-sign transform, giving (u∗v)/S² without a separate sort.
- `crt-map`: Chinese-remainder address map: The Agarwal–Cooley isomorphism turning a cyclic convolution of length S = ∏sᵢ into a multidimensional cyclic convolution on pairwise coprime axes, implemented on tape by triangular controlled shifts.
- `coefficient-twist`: Coefficient twist: The map x ↦ ζy with ζ = e^{πi/r}, which turns a length-r cyclic coordinate into the negacyclic ring ℂ[y]/(yʳ+1) by scaling coefficient k by ζᵏ, preserving convolution.
- `parameter-choice`: Fixed rational parameter choice: The conservative constants τ = σ = 1 − 2⁻⁵⁰, λ′ = 1 − 2⁻⁵⁴, c = 2⁻⁵⁶, ε = 2⁻⁷⁵, κ = 2⁻¹⁸², and sizes p = 6⌈log₂ n⌉, d = ⌊b^ε⌋, K = ⌊d^c⌋ that satisfy all layer and cost conditions.
- `multiplication-algorithm`: The multiplication algorithm: Split the inputs into radix-2ᵇ digits, map them by the CRT map, compute two forward resampled source transforms, multiply pointwise, apply the inverse transform, rescale, round and propagate carries.
- `exact-recovery`: Precision and exact recovery: Error bookkeeping showing every call stays in the disk and the recovered coefficients have error below 1/2, so rounding gives the exact integer convolution.
- `time-bound`: Complete time bound: The cost table, normalized by V = Tp = Θ(n), whose every dominant term is a power of p at most 1 − 2κ, giving total time O(n (log n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-alphabet multitape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n (lg n)^{1−κ}) worst-case time with κ = 2⁻¹⁸², disproving the n log n optimality conjecture in that model.

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
