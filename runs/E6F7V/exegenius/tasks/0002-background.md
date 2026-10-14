# exegenius task 0002-background

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F7` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bounds such as O(f(n)) on running time.
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, with modulus, conjugation and the unit-modulus numbers e^{iθ}.
- `turing-machine`: Multitape Turing machine (known to the reader): A finite-state machine with several tapes, each with a head that reads and writes one cell and moves one cell per step; running time counts steps.
- `nlogn-history`: Multiplication complexity and the n log n conjecture: Schönhage and Strassen multiplied n-bit integers in O(n log n log log n) on multitape machines and conjectured that n log n is optimal; later work (Fürer, then Harvey–van der Hoeven) reached O(n log n), and the paper's theorem breaks the conjectured optimum.
- `fixed-tape-model`: Fixed finite-alphabet multitape model: The cost model of the paper: one machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, where a step touches one cell per tape; extra tracks or work tapes change time only by a constant factor.
- `established-multiplier`: Established O(n log n) multiplier (subroutine): The Harvey–van der Hoeven O(N log N) integer multiplier, used as a black-box subroutine on short operands (never recursively on the improved algorithm).
- `stream-operations`: Array order and elementary stream operations: Arrays are stored in lexicographic address order on a tape; digit moves, digit swaps, pointwise maps on split streams and cyclic splitting of rows into W streams all take O(V) steps for volume V on fixed tapes.
- `controlled-shifts`: Controlled shifts: A target address field is cyclically shifted (or multiplied by a fixed unit modulo q^b) by an offset computed from control fields that precede it, in O(V) time by splitting each fibre in two pieces and merging them in reverse order.
- `dft`: Discrete Fourier transform: The map u ↦ (1/q)Σ_j u_j e^{−2πi jk/q} that evaluates a length-q sequence at the q-th roots of unity; it is a contraction in the max-modulus norm and has an inverse of the same shape with the opposite sign.
- `cyclic-convolution`: Cyclic convolution and the convolution theorem: The product of two polynomials modulo x^q − 1 (indices added mod q); the Fourier transform turns it into a pointwise product, so convolution = transform, multiply pointwise, inverse transform.
- `multidimensional-dft`: Multidimensional transforms and convolutions: A tensor product of one-dimensional transforms (or convolutions) along several axes of a box of size t₁×…×t_D, applied one axis at a time.
- `radix-digit-convolution`: Integer multiplication as radix-digit convolution: Splitting each n-bit input into radix-2^b digits turns the product into a convolution of short digit polynomials, padded so that no cyclic wraparound occurs, followed by a left-to-right carry propagation that yields the 2n-bit product.
- `crt-map`: Chinese-remainder map to prime cyclic axes: For pairwise coprime lengths s_i with product S, the algebra isomorphism x ↦ Π x_i^{μ_i} turns one cyclic convolution of length S into a multidimensional cyclic convolution on prime axes; on tape it is a sequence of prefix-controlled cyclic shifts.
- `bluestein-chirp`: Bluestein chirp identity: A Fourier transform can be written as a pointwise phase (chirp) multiplication, a cyclic convolution with a chirp array, and another chirp multiplication; here it also absorbs the frequency permutation Q.
- `fixed-point-disk`: Fixed-point complex coefficients and truncation: Complex numbers stored as 2^{−p}(a+ib) with integer a, b inside the unit disk, written as signed two's-complement words; Q_p truncates real and imaginary parts toward zero to this grid, with error below √2·2^{−p} and no increase of norm.
- `error-accounting`: Contractions and error accounting: Normalized transforms and averaged convolutions are contractions in the max-modulus norm, so errors of composed approximate steps add (bilinear steps add the two operand errors) and a final error below 1/2 permits rounding to integers.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven technique that expresses a Fourier transform of coprime length s through a transform of the larger length t (a power of two) using Gaussian-weighted contractions A and B₀ and a Neumann-series inverse; the sorting permutations stay inside the transform identity.
- `permutation-cancellation`: Retained permutations and their cancellation: The source permutation R left in the resampling identity cancels across two forward transforms, the pointwise product and the opposite-sign transform, giving R F_s⁺[(R F_s u)·(R F_s v)] = (u*v)/S².
- `padded-box-tensor-resampling`: Tensor resampling on the padded box: Resampling in d dimensions applies the one-dimensional maps line by line on a zero-padded box of T = Πt_i entries, exposing each axis with address-chunk interchanges, at total cost O(d T p^{3/2+δ} α) plus O(Tp d²(1+ℓ^τ)) for movement.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree below r with multiplication reduced by y^r = −1; multiplying by a power of y just rotates the coefficient list with sign changes, so powers of y act as roots of unity.
- `butterfly`: Two-point butterfly: The map H₀(u,v) = ((u+v)/2, (u−v)/2) on a pair of values, the basic step of a radix-2 fast Fourier transform; applied to a coordinate bit it is a halving contraction.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the negacyclic ring using roots ω_t = y^{2r/t} (signed shifts), computed by decimation-in-frequency rounds of butterflies and monomial twiddles y^E; it is a contraction and satisfies character cancellation despite zero divisors.
- `retained-frequency-order`: Retained (bit-reversed) frequency order: The recursion writes frequencies in bit-reversed slots; both forward transforms keep this order through the pointwise product and the opposite transform consumes it, so no sort is executed.
- `phase-twist`: Coefficient twist from cyclic to negacyclic: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} maps ℂ[x]/(x^r − 1) isomorphically onto the negacyclic ring, turning the last cyclic axis into a polynomial ring; its negative wrap gives the cyclic wrap after untwisting.
- `signed-packing-product`: Signed packing of ring products: A signed form of Kronecker substitution evaluates polynomial records at 2^{4p}, multiplies the resulting integers with the established multiplier, extracts coefficients, wraps negacyclically and truncates, giving a ring product in O(rp log(rp)).
- `linear-algebra-prelims`: Subspaces, orthogonality and rank: Vector subspaces over the rationals or over the two-element field, bilinear forms, orthogonal complements, nondegeneracy, projections, matrix rank and tensor products.
- `xor-linear-network`: Linear network exchanging two banks with restored scratch values: A fixed network of pointwise linear gates on wires (data banks X, Y, scratch and central wires) that in three stages maps (X,Y) to (−Y,X) and returns every scratch wire to its arbitrary initial value, as in transparent computation.
- `frames`: Frames: changing the representation along a network: An invertible operator D_v on an array chosen at each source, gate and sink; every edge applies D_vD_u^{-1}, a common frame commutes with the pointwise linear gate, so the network implements D_out S D_in^{-1} and the endpoint frames fix the operator on every role.
- `subset-labels`: Subspace labels from three-element subsets: Frankl–Wilson style construction: indicator vectors of three-element subsets of [100] give intersection-size inner products; tensor cubes of these lines label gates by nested nondegenerate subspaces so that edge changes are small orthogonal residuals.
- `rank-deficit`: Rank deficit s < W m: The sum s of ranks of all edge differences (the number of smaller calls) is strictly less than W·m, where W is the number of wires and m the label-space dimension; the deficit comes from the loss L on decreasing edges being below N/2.
- `power-saving-recurrence`: Recursive power saving from the rank deficit: A call at parameter m·f makes s calls at parameter f on streams of volume V/W, giving F_k ≤ (s/W)F_{k−1}+O(1) with s/W < m, so the normalized cost is O(parameter^τ) for some τ < 1.
- `lower-triangular-factorization`: Lower-triangular (Bruhat) factorization: Every rational matrix of rank a factors as E₁ΠE₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
- `bit-shear-interface`: Address shear from the bit network: Using the permutation frame Φ_M that moves the entry at (H,D) to (H+MD,D), the bit network's endpoint matrices differ by the identity, so it implements the shear H ← H+D on every role, with total edge rank s_b < W_b·m.
- `matrix-shear-cost`: Cost of a rational matrix shear: For a rational matrix A of rank a, the shear (H,D) ↦ (H+AD,D) over ℤ/q^bℤ is done with exactly a interchanges of b-digit fields and O(V) other work, using triangular updates as controlled shifts.
- `power-width-interchange`: Recursive power-width address interchange: Two address chunks of m^k digits are interchanged in O(V e^τ) by splitting rows into W role streams, running the bit network whose edges are shears (smaller interchanges), and finishing with D←D−H, H←H+D, D←H−D; a depth-first schedule on fixed tapes realizes the recursion.
- `arbitrary-width-interchange`: Address-chunk interchange in time O(V u^τ): Exchanging two disjoint contiguous address fields of u bits (any width, any gaps, even one-bit payload) in O(V u^τ) for a fixed τ = 1 − 2^{−50} < 1, by peeling off high digits to make rows, padding, and splitting the width in base m; the intermediate steps are XOR combinations though the result is an exact permutation.
- `phase-frame-network`: Complex phase network and two-point kernels: The same network over Gaussian dyadic values with binary labels and phase frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m}; each edge change is a product of two-point kernels C = aI+bX (a=(1+i)/2, b=(1−i)/2), and telescoping gives C^{⊗m} on every role with s_c < W_c·m kernel factors.
- `packed-selected-bit-addition`: Packed selected-bit addition: A binary row addition (XOR) of selected bits across many address chunks at once, done by a constant number of whole-chunk cyclic shifts using a third chunk of arbitrary contents as temporary storage, followed by a deterministic repair of an explicitly bounded set of exceptional addresses.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer in time O(V d^λ′): Applying H₀ at once to the same bit position of D ≤ d address chunks of every polynomial record in O(V d^{λ'}) for fixed λ' < 1, via H₀^{⊗D} = b^D S_D C^{⊗D} S_D, the recursive phase network, packed bit moves, exact Gaussian dyadic arithmetic and one final truncation.
- `transform-layout`: Transform layout and cost: A positional layout permutation L places the selected bits of all axes at a common offset in consecutive K-bit chunks (prefix moves plus chunk exchanges), so each round is one simultaneous layer; the forward and opposite transforms cost O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]) with error below √2 ℓ 2^{−p}.
- `synthetic-convolution`: Convolution from the retained transform layout: Two forward synthetic transforms in layout order, a pointwise ring product divided by r, the opposite transform and an exact scaling by M compute the normalized convolution (f*g)/T over the negacyclic ring with error below √2 M(3ℓ+1)2^{−p}.
- `source-transform`: Computed source transform: The source Fourier transform R F_s is computed as 2^γ B₀ Q F_t A: Gaussian expansion on each line, the chirp transform (a twisted synthetic convolution) and Gaussian compression, then a power-of-two scaling, all with tracked disk margins and errors.
- `prime-axis-parameters`: Parameter choices and prime axis lengths: Fixed parameters b = ⌈log₂n⌉, p = 6b, d = ⌊b^ε⌋, K = ⌊d^c⌋, T ≈ n/b, r = 2^{⌈(log₂T)/d⌉}, axes of length r/2 or r, and distinct primes s_i just below t_i found by deterministic search, with ε = 2^{−75}, c = 2^{−56}, λ' = 1−2^{−54}, κ = 2^{−182}.
- `exact-recovery`: Precision budget and exact recovery: Scale bookkeeping (the two factors S) and the error bound 448 b 2^{−b+γ} < 1/2 show that each recovered convolution coefficient rounds to the true integer, which is below 2^{3b}, so carries give the exact product.
- `multiplication-algorithm`: The multiplication algorithm: Digit extraction, the address map Φ to prime axes, two source transforms, a truncated pointwise product, the opposite-sign transform, rescaling by S and 2^{2b+4}, rounding, inverse address map and carry propagation, producing the 2n-bit product.
- `cost-accounting`: Complete time bound and power margins: Dividing costs by V = Tp gives seven dominant terms (butterfly rounds, chunk exchanges, simultaneous layers, CRT layouts, Gaussian lines, chirps, packed products) each at most p^{1−2κ}; the smallest margin is 2^{−181} = 2κ, which absorbs log factors and gives O(n(log n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, refuting the n log n optimality conjecture in this model; the saving comes from faster address interchange and butterfly layers inside a Gaussian-resampling, Bluestein, synthetic-transform reduction.

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
