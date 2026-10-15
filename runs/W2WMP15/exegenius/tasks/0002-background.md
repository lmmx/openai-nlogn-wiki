# exegenius task 0002-background

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F4` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Expressions Σ a_k x^k with coefficients, added and multiplied by the usual rules.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, including modulus and unit-modulus numbers e^{iθ}.
- `multitape-tm`: Multitape Turing machine (known to the reader): A deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, each head moving at most one cell per step.
- `integer-multiplication-conjecture`: The n log n conjecture for integer multiplication: Schönhage and Strassen's 1971 proposal that n log n is the optimal multitape-Turing-machine time for multiplying two n-bit integers; the O(n log n) algorithm of Harvey and van der Hoeven met it from above, and this paper beats it by a power of the logarithm.
- `established-multiplier`: Established n log n multiplier: The known fixed-tape integer multiplier of Harvey and van der Hoeven running in O(N log N) on N-bit inputs, used here only as an ordinary subroutine on short operands (never recursively on the improved algorithm).
- `tape-address-model`: Arrays, addresses and volume on tapes: An array on address set [a₁]×…×[a_t] is stored on a tape in lexicographic order with the address implicit in position; its logical volume V is the number of stored data bits, and an adjacent group of address bits is an address field or chunk.
- `elementary-stream-ops`: Elementary stream operations: Linear-time (O(V)) tape scans that permute two radix-q digits, move a digit, split an array into aligned streams on a digit, apply a pointwise map and merge, or deal whole rows cyclically to W streams.
- `controlled-shift`: Controlled cyclic shifts: An update y ↦ y + a(controls) mod Q of a target field that follows its control fields on tape, done in O(V) by splitting each fiber at the offset and merging the two pieces in the opposite order; also multiplication by a fixed unit and negation of the target.
- `linear-algebra-basics`: Rank, subspaces and orthogonal complements: Matrix rank, subspaces, projections, bilinear forms and the orthogonal complement of a subspace inside a larger one, including over the two-element field F₂.
- `cyclic-convolution`: Cyclic convolution: The convolution u*v of arrays on Z/t₁×…×Z/t_D, where output index j sums u_k v_{j−k} with indices wrapping modulo each length; it is the product in the group algebra C[x₁,…]/(x₁^{t₁}−1,…), and integer multiplication is a convolution of digit lists.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q}, with an opposite-sign inverse F⁺ satisfying F⁺F = I/q, which turns cyclic convolution into a pointwise product: F(u*v) = q·(Fu)(Fv).
- `multidimensional-dft`: Multidimensional (tensor) transform: The tensor product F_t = ⊗ F_{t_i} of one-dimensional transforms applied along each axis of an array with axis lengths t₁,…,t_D; moving to many axes of power-of-two length is why the algorithm can use cheap butterflies.
- `butterfly`: Two-point butterfly: The 2×2 averaging step H₀(u,v) = ((u+v)/2, (u−v)/2) from which a power-of-two transform is built by pairing entries k and k+t/2 (decimation in frequency), with the second output multiplied by a twiddle root.
- `polynomial-ring-mod`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree < r with y^r = −1, in which multiplying by a power of y permutes the coefficients up to sign, so that powers of y serve as exact roots of unity.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier-type transform whose entries lie in C[y]/(y^r+1) and whose root of unity ω_t = y^{2r/t} acts as a signed coefficient shift, computed by radix-two butterfly rounds with twiddle monomials, leaving outputs in bit-reversed (retained) frequency order that the opposite transform consumes.
- `signed-packing`: Signed packing of polynomial products: A signed form of Kronecker substitution: evaluate polynomial coefficients at 2^{4p} to get integers, multiply with the established multiplier, and read the product coefficients back by centered residues and carries.
- `linear-network`: Linear exchange network with restored scratch wires: A fixed network of linear gates on wires (each with a role) that, for arbitrary initial scratch values, exchanges two banks of values with prescribed signs and restores every scratch wire; run in eight rows of copy, gather, scatter and side-injection steps.
- `common-frame-principle`: Frames on wire arrays: Replacing each scalar by an array and giving every vertex an invertible linear operator D_v (its frame) lets pointwise gates commute with frames, so intermediate frames cancel and only the endpoint operator D_out·D_in⁻¹ is applied to each role while each edge pays only the change of frame D_v D_u⁻¹.
- `subset-intersection-labels`: Subspace labels from three-element subsets: Attaching nested nondegenerate subspaces of F^{⊗3} (spanned by indicator vectors of 3-element subsets, with ⟨t_S,t_T⟩ = |S∩T|−1) to gates and terminals so that gather/scatter coefficients depend on intersection size and unwanted ones are cancelled by side wires; the total rank change of all edges is less than Wm.
- `address-shear`: Address shear and lower-triangular factorization: The address permutation (H,D) ↦ (H+AD, D) on two vectors of fields; a rank-a matrix factors as E₁ΠE₂ with lower-triangular E₁,E₂ so that it costs a single-pair swaps plus linear-time updates, and three shears D←D−H, H←H+D, D←H−D interchange H and D.
- `rank-saving-recurrence`: Recursive rank saving: Running the linear network with edge changes implemented by smaller calls on role streams of volume V/W gives a cost-per-volume recurrence F_k ≤ (s/W)F_{k−1}+O(1); because the number s of smaller calls satisfies s < Wm, this yields F_k = O(e^τ) with τ<1, a power saving in the parameter.
- `address-chunk-interchange`: Fast address-chunk interchange: The first tape procedure: swapping two disjoint contiguous address fields of u bits, (p,h,g,d,z) ↦ (p,d,g,h,z), in O(V u^τ) for a fixed τ<1 by building the swap from address shears executed through the bit network, with XOR combinations of intermediate data.
- `phase-frame-kernel`: Phase frames and the two-point kernel C: The complex version of the network uses frames built from Hamming-weight phases i^{wt(x) mod 4}; each edge change factors into two-point kernels C = aI+bX (a=(1+i)/2, b=(1−i)/2), so a simultaneous C-layer on e=mf axes needs s smaller layers on f axes, and H₀^{⊗D} = b^D S_D C^{⊗D} S_D.
- `packed-selected-bit-addition`: Packed selected-bit addition: A binary row addition y_j ← y_j ⊕ x_j on the same bit position in f address chunks at once, done with eight chunk-wide cyclic shifts whose segments cannot carry into each other except at a small explicit set of exceptional addresses, which are then repaired deterministically; it restores the third chunk's arbitrary contents.
- `fixed-point-truncation`: Fixed-point disk-grid arithmetic: Complex values stored as 2^{−p}(a+ib) with signed two's-complement words in the unit disk, exact Gaussian-dyadic intermediate results with guard bits, and one truncation Q_p toward zero that costs error less than √2·2^{−p} per coefficient while never increasing the norm.
- `fast-butterfly-layer`: Fast simultaneous butterfly layer: The second tape procedure: applying H₀ at the same bit offset in d address chunks of a polynomial-record array in cost O(V d^λ') with λ'<1, by evaluating the layer exactly through the phase-frame network with packed chunk moves before a single truncation.
- `ring-convolution`: Convolution over the polynomial ring: Normalized convolution on d−1 axes of arrays with entries in C[y]/(y^r+1): two forward synthetic transforms keeping the same frequency order, pointwise polynomial products (by signed packing) divided by r, and the opposite transform, all using the fast layers and chunk swaps.
- `phase-twist`: Coefficient (phase) twist: The map x_d ↦ ζy with ζ = e^{πi/r} that sends the cyclic last coordinate C[x_d]/(x_d^r−1) isomorphically to C[y]/(y^r+1) by multiplying coefficient k by ζ^k, so the negative wrap of the ring becomes the original cyclic wrap after untwisting.
- `bluestein-chirp`: Bluestein chirp identity: Writing a (permuted) transform as a chirp-weighted cyclic convolution QF_t u = ā · (a * (ā · u))/T with a_j = exp(−πi Σ s_i j_i²/t_i), so a Fourier transform with its target permutation becomes a normalized convolution.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven reduction that expresses a Fourier transform of length s (here a prime) through a power-of-two transform of length t>s via Gaussian-weighted contractions: P_s F_s = 2^{2α²} B₀ P_t F_t A, with the two coordinate permutations P_s,P_t left inside the identity.
- `permutation-cancellation`: Retained permutations and their cancellation: Instead of executing the source and target coordinate permutations of Gaussian resampling as sorts, they stay in the transform formula; the source permutation R cancels across the two forward transforms, the pointwise product and the opposite transform: RF⁺[(RFu)(RFv)] = (u*v)/S².
- `crt-address-map`: Chinese-remainder address map: The Agarwal–Cooley isomorphism Φ: C[x]/(x^S−1) → C[x₁..x_d]/(x_i^{s_i}−1), x ↦ ∏ x_i^{μ_i}, for pairwise coprime (prime) s_i with S = ∏ s_i, which turns one long cyclic convolution into one on distinct prime axes and is implemented by triangular controlled shifts.
- `radix-digit-convolution`: Integer product as digit convolution: Writing each n-bit input as a polynomial in 2^b with ⌈n/b⌉ digits, the integer product is the polynomial product, whose coefficients are below 2^{3b}; with enough zero padding the cyclic convolution has no wraparound, and carries recover the bits.
- `exact-recovery`: Rounding and carry propagation: The final steps that rescale by known factors (S, 2^{2b+4}), prove the accumulated coefficient error is below 1/2 so rounding gives the exact integer coefficients, and propagate radix-2^b carries to produce the 2n-bit product.
- `parameter-choice`: Parameter choices and prime source lengths: The size parameters b=⌈log₂n⌉, precision p=6b, number of axes d=⌊b^ε⌋, chunk width K=⌊d^c⌋, padded size T≈n/b, power-of-two axis lengths t_i∈{r/2,r}, and distinct primes s_i just below t_i with T/2 < ∏s_i < T, chosen so resampling hypotheses and all tape lemmas apply.
- `multiplication-algorithm`: The multiplication algorithm: The pipeline: form radix digits, apply the CRT address map Φ, run two source transforms (resampling plus chirp convolution plus resampling), multiply pointwise, run the opposite transform, rescale, round and propagate carries; inside the chirp convolution the last coordinate is twisted into C[y]/(y^r+1) and convolved with synthetic transforms.
- `time-accounting`: Cost accounting and the saving κ: Dividing every cost by V = Tp = Θ(n) gives a table of seven dominant powers of p (layout moves, chunk exchanges, simultaneous butterfly rounds, CRT layout, Gaussian line maps, chirps, packed products), each at most 1−2κ with κ = 2^{−182}, giving total O(n (lg n)^{1−κ}).
- `main-theorem`: Integer multiplication below n log n: A single deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n optimality conjecture; it works by reducing to convolution, using fast address interchange and fast simultaneous butterfly layers to save a power of the logarithm.

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
