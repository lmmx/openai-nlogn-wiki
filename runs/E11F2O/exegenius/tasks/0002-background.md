# exegenius task 0002-background

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F2` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, with addition, multiplication and evaluation.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, including roots of unity e^{2πi/q} and absolute value.
- `turing-machine-tapes`: Turing machines and tapes (known to the reader): A finite-state machine with read/write heads moving one cell at a time on tapes; running time counts steps.
- `n-log-n-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's conjecture that n log n is the optimal order of growth for the time to multiply two n-bit integers on a multitape Turing machine.
- `fixed-tape-model`: Fixed finite-tape Turing machine model: One machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes; each step reads and writes one cell per tape and moves each head by at most one cell, and cost is the number of steps.
- `stream-arrays`: Arrays, address fields and elementary scans: Arrays with a product address set are stored in lexicographic order on tape, with addresses implicit in position; fixed permutations of digits, digit moves, pointwise maps and cyclic row splits cost O(V) for V stored bits.
- `controlled-shifts`: Controlled cyclic shifts and rational scalings: A linear-time tape operation that adds an offset computed from earlier control fields to a later target field modulo q^b, or multiplies it by a fixed unit, by splitting and re-merging blocks.
- `radix-digit-convolution`: Integer multiplication as digit convolution: Writing each integer as a polynomial in a power of two 2^b, the product's digit-coefficient list is the convolution of the two digit lists, followed by carry propagation.
- `dft-cyclic-convolution`: Normalized DFT and cyclic convolution: The length-q discrete Fourier transform with 1/q normalization turns cyclic convolution into pointwise multiplication; its inverse uses the opposite sign of the exponent.
- `multidim-transform`: Multidimensional (tensor) Fourier transform: The tensor product of one-dimensional transforms along several axes; a transform on an array with axis lengths t_1,…,t_d is applied axis by axis.
- `crt-axis-map`: Chinese-remainder map to prime cyclic axes: An algebra isomorphism sending one cyclic convolution of length S = s_1⋯s_d (pairwise coprime) to a convolution on a product of d cyclic axes, implemented by triangular controlled cyclic shifts.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of coprime length s through a Fourier transform of a larger power-of-two length t, using Gaussian-weighted interpolation maps A and B₀.
- `fixed-point-disk-grid`: Fixed-point disk-grid arithmetic and contractions: Complex numbers stored as signed two's-complement integers scaled by 2^{-p} inside the unit disk; truncation Q_p toward zero costs error below √2·2^{-p}, and contractions never increase the sup norm so errors add up predictably.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree below r with y^r = −1, where multiplication by a power of y is a signed shift of the coefficient list.
- `synthetic-transform`: Synthetic Fourier transform modulo y^r + 1: A Fourier transform over the ring modulo y^r + 1 whose roots of unity are powers of y, so twiddle multiplications are signed coefficient shifts; it satisfies a character-cancellation identity despite zero divisors.
- `butterfly-layers`: Radix-2 butterfly layers and stored frequency order: Decimation in frequency: each level combines entries k and k+t/2 by the two-point butterfly H₀ and a twiddle monomial, leaving frequencies stored in bit-reversed order, which the opposite transform consumes directly.
- `coefficient-twist`: Twist from cyclic to negacyclic convolution: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} is a ring isomorphism from the cyclic ring (x^r = 1) to the ring modulo y^r + 1, so its negative wrap yields the cyclic wrap after untwisting.
- `nlogn-subroutine`: Established n log n multiplier as a subroutine: The Harvey–van der Hoeven O(N log N) integer multiplier is used as an ordinary subroutine on short inputs and does not invoke the improved theorem recursively.
- `signed-kronecker-packing`: Signed Kronecker packing of polynomial products: Multiplying two polynomial records exactly by evaluating their integer-coefficient parts at a large power of two, multiplying the resulting integers with the established multiplier, and recovering signed coefficients by centered carries.
- `bluestein-chirp`: Bluestein's chirp identity: Rewrites a Fourier transform as a pointwise phase multiplication, a cyclic convolution with a chirp array, and another pointwise phase multiplication.
- `resampling-no-sort`: Resampling with the permutations left in the transform: The tensor form of Gaussian resampling in which the source and target coordinate permutations R and Q stay inside the transform identity, so they need not be executed as separate sorts.
- `chirp-permutation-cancel`: Chirp identity and source-permutation cancellation: A chirp-convolution formula for Q·F_t that leaves the target permutation unexecuted, together with the fact that the source permutation R cancels across the two forward transforms, the pointwise product and the opposite transform.
- `triple-gadget`: Three-element subset intersection gadget: Gather, scatter and side-injection updates indexed by three-element subsets of a 100-element set, whose coefficients depend on intersection size; side wires cancel the unwanted intersection-one (or intersection-zero/two) contributions.
- `bank-exchange-network`: Linear network that exchanges two banks and restores scratch values: A fixed network of linear gates with three stages whose net effect is (X, Y) ↦ (−Y, X) on two banks, restoring every auxiliary scratch value whatever its initial contents.
- `frames`: Frames and the common-frame identity: An invertible operator D_v on each wire's address-indexed array at every network vertex; since gates are pointwise and linear they commute with a shared frame, so the whole network implements D_out S D_in⁻¹ and only edge changes D_v D_u⁻¹ cost anything.
- `bilinear-orthogonal`: Orthogonal complements and projections in a bilinear space: In a vector space with a nondegenerate symmetric bilinear form, a subspace U has an orthogonal complement U⊥ and a projection P_U along it; the residual of nested subspaces has dimension equal to the difference of their dimensions.
- `subspace-labels`: Nested subspace labels and the rank saving: Subspaces of an m-dimensional space attached to gates and terminals so adjacent labels are nested; edge dimension changes count the smaller operations needed, and their total s is strictly below W·m.
- `triangular-factorization`: Lower-triangular rank factorization: Every rational square matrix of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation matrix with exactly a ones (a Bruhat factorization with coordinate order reversed).
- `matrix-shear`: Cost of a rational matrix shear: The address update (H, D) ↦ (H + AD, D) over Z/q^b is performed with exactly rank(A) interchanges of pairs of b-digit fields plus linear extra work, using triangular factors and controlled shifts.
- `power-width-interchange`: Power-width chunk interchange in O(Ve^τ) time: Recursively interchanges two chunks of e = m^k digits by running the bank-exchange network on W role streams of volume V/W, each edge costing rank-many smaller interchanges; since s/W < m^τ the cost per volume is O(e^τ).
- `chunk-swap`: Chunk interchange in O(Vu^τ) time: Interchanges two disjoint address chunks of u bits in any bit array in O(V u^τ) steps for a fixed τ < 1, by padding rows and splitting the width in base m into power-width pieces; intermediate steps are XOR combinations but the final effect is an exact permutation.
- `phase-kernel-network`: Two-point kernel C and the complex phase network: The Gaussian-dyadic two-point kernel C = H S H = aI + bX (a = (1+i)/2, b = (1−i)/2) satisfies H₀ = b S C S; the complex bank-exchange network with binary labels makes C^{⊗m} on every role from products of translation kernels, one per residual basis vector.
- `packed-selected-bits`: Packed XOR of selected bits across address chunks: A binary row addition y ← y ⊕ x on the selected bit of each of f chunks at once, done by a constant number of cyclic shifts of whole chunk ranges followed by deterministic repair of a small explicit set of bad addresses, using a third chunk as restored temporary space.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer in O(Vd^λ') time: Applies the normalized butterfly H₀ to one bit position in each of d address chunks of polynomial records in one pass, exactly in Gaussian dyadics followed by a single truncation, in O(V d^λ') for a fixed λ' < 1 instead of d whole-array passes.
- `transform-layout`: Layout and cost of the synthetic transform: A positional layout permutation puts the selected bits of all axes at a common offset in K-bit chunks so each transform round is one simultaneous layer; the forward transform keeps its output order for the pointwise product and the opposite transform.
- `ring-convolution`: Convolution over the polynomial ring from the retained layout: Normalized convolution of arrays over the ring modulo y^r + 1: two forward synthetic transforms, pointwise ring products by signed packing, then the opposite transform consuming the same frequency order, with error O(M ℓ 2^{-p}).
- `source-transform`: Source transform via resampling, chirp and ring convolution: The computed procedure for a source Fourier transform of prime lengths: Gaussian maps A, then a chirp transform evaluated by a twisted ring convolution, then B₀ and an exact power-of-two scale, with exact counterpart R F_s.
- `parameter-choice`: Choice of sizes, precision and prime axis lengths: Fixing b = ⌈log₂ n⌉, precision p = 6b, axis count d = ⌊b^ε⌋, padded size T ≈ n/b, record length r, power-of-two axis lengths t_i, and distinct odd prime lengths s_i just below t_i, so that Tp = Θ(n) and all hypotheses of the interfaces hold.
- `exact-recovery`: Exact recovery: scaling, rounding and carries: Removing the known normalizations S and 2^{2b+4}, showing the recovered coefficient error is below 1/2 so rounding gives exact convolution coefficients, then propagating radix-2^b carries to the 2n-bit product.
- `multiplication-algorithm`: The multiplication algorithm: Split into radix digits, map by Φ to prime axes, take two source transforms, multiply pointwise, apply the opposite-sign transform with the two scalings by S, round, undo Φ, and propagate carries to output the 2n-bit product.
- `cost-accounting`: Cost accounting and the saving exponent κ: A table of costs divided by Tp, each at most p^{1−2κ} thanks to the slack in the chosen exponents (seven dominant margins, the smallest 2^{-181} = 2κ), giving O(n (log n)^{1−κ}) overall.
- `main-theorem`: Multiplying n-bit integers in O(n (lg n)^(1−κ)) time: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{-182}, using fast address-chunk interchange and simultaneous butterfly layers to speed synthetic transforms inside a Gaussian-resampling multiplication.

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
