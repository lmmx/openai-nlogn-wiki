# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/Q1` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic notation O(·), Ω(·), o(·) bounding a function's growth up to constant factors for large inputs.
- `polynomials`: Polynomials (known to the reader): Expressions Σ aⱼxʲ with coefficients in a ring, added and multiplied coefficientwise and by convolution of coefficient lists.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, including roots of unity e^{2πij/k} and the modulus |z|.
- `multitape-tm`: Multitape Turing machine (known to the reader): A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, each step reading, writing and moving every head by at most one cell.
- `modular-arithmetic`: Modular arithmetic and finite fields: Arithmetic in residue rings ℤ/qᵇℤ and in the two-element field 𝔽₂, where addition is XOR, used both for address fields and for scalar values.
- `linear-algebra`: Linear maps, matrices and rank: Vector spaces over a field, linear maps represented by matrices, invertibility, and the rank of a matrix as the dimension of its image.
- `tensor-product`: Tensor products: The tensor product of vector spaces or linear maps, so that an operator on a multi-index array acting as A₁ ⊗ … ⊗ A_d applies Aᵢ independently along each coordinate.
- `bilinear-forms`: Nondegenerate bilinear forms and orthogonal complements: A symmetric bilinear form ⟨x, y⟩ on a vector space, nondegenerate when only 0 is orthogonal to everything, together with orthogonal complements U^⊥ and orthogonal direct sums U ⊥ E.
- `nlogn-conjecture`: The n log n conjecture: Schönhage and Strassen's 1971 proposal that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The established deterministic multitape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short records.
- `cyclic-convolution`: Cyclic convolution: The product of polynomials modulo xˢ − 1 (or of arrays on a product of cyclic groups ℤ/tᵢℤ), where indices add with wraparound.
- `dft`: Normalized discrete Fourier transform: The map (F_q u)_k = (1/q) Σⱼ uⱼ e^{−2πijk/q} and its opposite-sign version F_q⁺, extended to several axes by tensor products, which turns cyclic convolution into pointwise products.
- `radix-reduction`: Radix-digit reduction: Writing each n-bit input as a polynomial in 2ᵇ with b-bit digits, so the product is recovered from the integer convolution of the digit lists followed by carry propagation.
- `array-layout`: Lexicographic array layout and logical volume: Arrays on address sets [a₁]×…×[a_t] stored on tape in lexicographic order with implicit addresses, with cost measured relative to the logical volume V (number of stored data bits).
- `elementary-streams`: Elementary stream operations: Linear-time O(V) tape scans that permute or move single radix-q digits of addresses, apply fixed pointwise maps to split streams, and split or merge whole rows cyclically into a fixed number of streams.
- `controlled-shifts`: Controlled shifts and rational scalings: O(V) tape procedures that add to an address field y an offset computed from earlier control fields modulo Q = qᵇ, or multiply y by a fixed rational unit, by splitting each fiber into pieces and merging them in a new order.
- `fixed-point`: Gaussian dyadic fixed-point arithmetic: Complex numbers whose real and imaginary parts have power-of-two denominators, stored as fixed-width two's-complement numerators on the p-bit disk grid, with truncation Q_p toward zero to 2^{−p}ℤ.
- `contraction-errors`: Contractions and error accounting: Linear maps of operator norm at most one do not amplify errors, so errors of approximate algorithms for contractions (and bilinear contractions) simply add when composed.
- `negacyclic-ring`: Polynomial ring modulo yʳ + 1: The ring ℂ[y]/(yʳ + 1) with r a power of two, in which y is a primitive 2r-th root of unity and multiplication by a power of y is a signed cyclic shift of the coefficient list.
- `normalized-butterfly`: Normalized butterfly H₀: The two-point map H₀(u, v) = ((u + v)/2, (u − v)/2), the radix-two butterfly of the transforms, which is a contraction with H₀² = I/2.
- `kernel-c`: Two-point kernel C: The Gaussian-dyadic 2×2 kernel C = H·diag(1, i)·H = aI + bX with a = (1 + i)/2, b = (1 − i)/2, satisfying C⁴ = I and H₀ = b·S·C·S, so a layer of H₀ equals a layer of C up to diagonal phases and a scale.
- `linear-network`: Linear network with wire roles: A fixed finite circuit of wires each carrying one scalar, with gates that apply fixed linear maps to the wires they touch; a wire's fixed place in the network is its role.
- `scratch-restoration`: Restoring scratch values: A gate schedule that first subtracts the effect of the arbitrary initial scratch values, then injects the data, then undoes its own auxiliary updates, so every scratch wire ends with its arbitrary initial value.
- `triple-construction`: Three-element subset construction: Indicator vectors of 3-element subsets of a 100-element set, whose pairings |S ∩ T| mod 2 and |S ∩ T| − 1 make intersecting (or neighbouring) triples orthogonal, following Alon's account of Frankl–Wilson.
- `bank-exchange`: Three-stage bank exchange: The scalar network that, using copy, gather, scatter and side-injection gates per coordinate stage, maps two banks (X, Y) to (−Y, X) (a pure swap over 𝔽₂) while restoring all scratch wires.
- `frames`: Frames and the common-frame identity: Assigning an invertible linear operator D_v (a frame) to each gate and terminal so that stored arrays are D_v applied to logical arrays; since a common frame commutes with pointwise gates, the network implements D_out·S·D_in⁻¹ and each route gets its endpoint operator.
- `subspace-labels`: Nested subspace labels and orthogonal residuals: Attaching to every gate and terminal of the network a nondegenerate subspace of the m-dimensional space F^{⊗3}, nested along each edge, whose orthogonal residual dimension counts the smaller operations that edge needs.
- `rank-deficit`: Rank deficit s < Wm: The key property of both finite networks: the total number s of smaller calls needed over all edges is strictly less than W·m, so s/W < m.
- `bit-interface`: Rational matrix interface of the bit network: Using projections P_U onto the labels as rational matrices on the XOR network so that each edge's matrix difference has rank equal to its residual and every route's endpoint difference is the identity Iₘ, giving the address shear on every role.
- `phase-interface`: Binary phase interface of the complex network: Using phase frames 𝒞_U = H^{⊗m}·diag(i^{q_U(x)})·H^{⊗m} on the complex network so that each edge's frame change is a product of one translation kernel aI + bX_v per orthonormal residual vector and the whole network yields C^{⊗m} on every role.
- `address-shear`: Address shear: The address permutation (H, D) ↦ (H + D, D) on two groups of address fields over ℤ/qᵇℤ; together with two linear-cost updates it yields the interchange (H, D) ↦ (D, H).
- `bruhat`: Lower triangular (Bruhat) factorization: Every rational matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
- `matrix-shear`: Matrix shear by rank-many interchanges: A shear (H, D) ↦ (H + AD, D) by a fixed rational matrix A of rank a is performed with exactly a smaller field interchanges plus O(V) triangular controlled shifts.
- `row-splitting`: Row splitting among wire roles: Distributing the rows of an array cyclically among the W roles of a network (padding to a multiple of W) so that every role stream has the same address shape and volume V/W and gates act pointwise.
- `power-saving-recursion`: Volume-normalized recursion and the power saving: The recurrence F(mf) ≤ (s/W)·F(f) + overhead for cost divided by volume, which, because s/W < m, gives cost O(V·e^τ) with τ < 1 instead of O(V·e) for a parameter e.
- `fixed-tape-schedule`: Fixed-tape depth-first schedule: Running the recursion on a fixed set of tapes by parking the inactive role streams on a stack tape before each child call and restoring them afterward, at O(V) cost per node.
- `power-width-interchange`: Power-width interchange: Interchanging two address chunks of e = mᵏ radix-q digits in O(V·e^τ) time by running the bit network on row-split role streams with shear frames and recursive smaller interchanges.
- `chunk-swap`: Fast address-chunk interchange: The tape procedure that interchanges two disjoint u-bit address fields of any array in O(V·u^τ) time with fixed τ = 1 − 2^{−50}, computing XOR combinations of data along the way.
- `packed-addition`: Packed selected-bit addition: XORing the selected bits of one address chunk into the corresponding bits of another using eight packed cyclic shifts guarded by a third chunk, then deterministically repairing the small set of addresses where guards overflow.
- `recursive-c-layer`: Recursive C-layer via phase frames: Computing C^{⊗e} on e selected address bits by running the complex network on row-split streams, implementing each edge's frame change by a binary change of basis and one recursive C^{⊗e/m} call per residual vector.
- `simultaneous-layer`: Simultaneous butterfly layer: The procedure applying H₀ on the same bit position in up to d address chunks of an array of polynomial records at once in O(V·d^{λ′}) time, λ′ < 1, evaluating exactly with guard bits and truncating once.
- `synthetic-transform`: Synthetic polynomial transform: The Nussbaumer–Quandalle Fourier transform over ℂ[y]/(yʳ + 1) using powers of y as roots of unity, computed by decimation-in-frequency butterflies and monomial twiddles and leaving outputs in bit-reversed order.
- `transform-layout`: Transform layout and cost: Rearranging the address bits of a multidimensional synthetic transform so that each round's selected bits sit at a common offset in consecutive K-bit chunks, letting every round use the simultaneous butterfly layer.
- `signed-packing`: Signed Kronecker packing: Multiplying two polynomials with signed Gaussian-integer coefficients by evaluating them at B₀ = 2^{4p} into single integers, multiplying with the established multiplier, and extracting centered coefficients before reducing modulo yʳ + 1.
- `synthetic-convolution`: Ring convolution from the retained layout: Computing normalized cyclic convolution of arrays over ℂ[y]/(yʳ + 1) by two forward synthetic transforms, pointwise products in their retained stored order, and one opposite transform.
- `coefficient-twist`: Coefficient twist: The map x ↦ ζy with ζ = e^{πi/r}, which turns cyclic convolution in the last coordinate into negacyclic multiplication modulo yʳ + 1 and back.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of prime length s through one of nearby power-of-two length t by convolving with Gaussian kernels, with well-conditioned resampling maps.
- `resampling-retained`: Resampling with retained permutations: The identity P_s F_s = 2^{2α²} B₀ P_t F_t A, in which the two coordinate permutations of Gaussian resampling are kept inside the transform identity instead of being executed as sorts.
- `tensor-resampling`: Tensor resampling interface: Applying the one-dimensional resampling maps line by line on every axis of a padded power-of-two box, moving axes into position with the fast chunk interchange.
- `bluestein`: Bluestein's chirp identity: The identity QF_t u = ā · (a ∗ (ā · u))/T with chirp a_j = exp(−πi Σ sᵢjᵢ²/tᵢ), which converts the permuted middle Fourier transform into a cyclic convolution.
- `source-perm-cancel`: Source permutation cancellation: The identity RF⁺[(RFu)·(RFv)] = (u ∗ v)/S², showing that the source permutation R kept from resampling cancels between the two forward transforms and the opposite transform.
- `source-transform`: Computed source transform: The procedure approximating RF_s on the prime-axis array by composing the Gaussian expansion A, the chirp transform (via twisted ring convolution), the compression B₀, and an exact scale 2^γ.
- `crt-map`: Chinese-remainder convolution map: The Agarwal–Cooley isomorphism ℂ[x]/(x^S − 1) → ⊗ᵢ ℂ[xᵢ]/(xᵢ^{sᵢ} − 1) for pairwise coprime sᵢ, placing the digit list on a product of prime cyclic axes and implemented on tape by triangular controlled shifts and axis moves.
- `parameters`: Size parameters and prime source lengths: The choices b = ⌈log₂ n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, power-of-two box T ≈ 4n/b split into d axes of length r or r/2, distinct odd primes sᵢ just below each tᵢ, and the fixed rational exponents ending in κ = 2^{−182}.
- `precision-recovery`: Precision analysis and exact recovery: The error bookkeeping showing that after undoing the normalizations S and the digit scales, every recovered convolution coefficient is within 1/2 of the true integer, so rounding and carry propagation give the exact product.
- `cost-accounting`: Cost table and the exponent κ: The accounting that bounds every stage's cost divided by Tp = Θ(n) by a power of p at most 1 − 2κ, so the whole algorithm runs in O(n·(log n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^{1−κ}) time: One deterministic fixed-alphabet, fixed-tape Turing machine computes the exact 2n-bit product of two n-bit integers in O(n·(lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n conjecture in that model.

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
