# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/P4` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, with modulus, conjugation and the unit-modulus numbers e^{iθ}.
- `turing-tapes`: Turing machines and tapes (known to the reader): A finite-state machine with read/write heads moving over one-dimensional tapes.
- `multitape-model`: Fixed-tape Turing machine model: The paper's cost model: one fixed finite alphabet, a fixed finite number of one-dimensional tapes, each step reads/writes one cell per tape and moves each head by at most one cell, so moving data far costs time.
- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's 1971 conjecture that Θ(n log n) is the optimal time to multiply two n-bit integers on a multitape Turing machine; Harvey and van der Hoeven reached O(n log n), and this paper refutes optimality.
- `established-multiplier`: Established near-linear integer multiplier: The Harvey–van der Hoeven fixed-tape multiplier running in O(N log N) on N-bit inputs, used only as an ordinary subroutine on short records (it does not invoke the improved theorem).
- `linear-algebra-basics`: Matrices, rank, subspaces and projections: Linear maps as matrices, rank, invertibility, lower-triangular matrices, subspaces, direct sums, and projection onto a subspace along a complement.
- `tensor-products`: Tensor products of vectors, spaces and operators: The tensor (Kronecker) product of vectors, spaces and operators, which acts factor by factor on coordinates of a multi-index.
- `f2-vectors`: Binary vectors, XOR and Hamming weight: Vectors over the two-element field with addition equal to XOR, dot product mod 2, and Hamming weight wt(x), the number of ones.
- `bilinear-orthogonality`: Nondegenerate bilinear forms and orthogonal complements: A symmetric bilinear form defines orthogonality; for a nondegenerate subspace the space splits as the subspace plus its orthogonal complement, and over F₂ a nonalternating form has an orthonormal basis.
- `dft`: Discrete Fourier transform: The normalized transform (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q} on length-q vectors, together with its opposite-sign inverse-like partner F_q⁺.
- `multidim-dft`: Multidimensional transform and cyclic convolution on a product of axes: The tensor product of one-dimensional DFTs along several axes of a box of coordinates, acting on arrays indexed by a product of cyclic groups.
- `cyclic-convolution`: Cyclic convolution and the convolution theorem: Convolution of arrays indexed by cyclic groups; the DFT turns it into pointwise multiplication (up to normalization), so convolution can be computed by transform, pointwise product, inverse transform.
- `fft-butterfly`: Butterfly step and decimation-in-frequency recursion: The two-point step H₀(u,v) = ((u+v)/2,(u−v)/2) paired with a twiddle multiplication; applying it recursively on halves computes a length-2^a transform in a levels.
- `multiplication-as-convolution`: Integer multiplication as convolution of radix digits: Writing each integer as a polynomial in a radix 2^b with small digits, the product's digit coefficients are the (non-wrapping) convolution of the digit lists, followed by carry propagation.
- `contraction-error-budget`: Max-modulus norm, contractions and error propagation: Under the maximum-modulus norm, normalized transforms and permutations are contractions (never increase norm), so approximation errors of composed steps add up without amplification.
- `disk-grid-truncation`: Disk grid and truncation: Fixed-point complex numbers with p fractional bits inside the unit disk, and the operator that truncates real and imaginary parts toward zero to that grid, never increasing norm and causing error below √2·2^{−p}.
- `fixed-point-arithmetic`: Streaming fixed-point and Gaussian dyadic arithmetic: Signed two's-complement fixed-point addition, sign change, halving and multiplication by i on tapes in linear bit time, kept exact by reserving guard bits; values are Gaussian dyadics (complex numbers with power-of-two denominators).
- `address-fields-volume`: Arrays, address fields, rows and logical volume: Arrays on a product of ranges [a₁]×…×[a_t] are stored in lexicographic order with implicit addresses; V is the number of stored bits, and a row is the full block at a fixed prefix and row index.
- `stream-ops`: Linear-time stream operations: Splitting a stream on a digit, applying a fixed pointwise map to aligned streams, merging, moving one digit, and splitting rows cyclically into W streams all cost O(V) on a fixed number of tapes.
- `controlled-shifts`: Controlled cyclic shifts and rational scalings: Updating a target field y ↦ y + a(controls) mod Q, with the controls earlier on the tape than the target, costs O(V) by splitting and re-merging blocks; multiplication by rational units mod q^b is also linear.
- `fixed-tape-dfs-schedule`: Depth-first recursion schedule on fixed tapes: Recursive calls on W role streams are run on one fixed set of tapes by parking the inactive streams on a stack, copying the active stream to the child, and restoring afterwards, costing O(V) per node.
- `subset-pairing-formulas`: Triple-intersection pairing formulas: Using indicator vectors of three-element subsets of a 100-element set, intersection sizes appear as bilinear pairings (|S∩T|−1 over the rationals, |S∩T| mod 2 over F₂), following Alon's presentation of Frankl–Wilson.
- `scalar-exchange-network`: Linear network exchanging two banks with restored scratch: A fixed network of linear gates (copy, gather, scatter, side injection) on banks X and Y that sends (X,Y) to (−Y,X) in three stages while restoring every auxiliary scratch wire to its arbitrary initial value.
- `network-frames`: Frames and the common-frame identity: Replace each wire's scalar by an array and give each gate/terminal an invertible frame operator; since a common frame commutes with pointwise linear gates, the whole network acts as D_out S D_in⁻¹, so only endpoint frames matter and each edge can be implemented by D_v D_u⁻¹.
- `subspace-labels-rank-saving`: Nested subspace labels and the rank deficit: Gates and terminals are labeled by nested subspaces of an m-dimensional space built from tensor powers of triple indicator vectors; the total dimension change over edges is below W·m (W = number of wires), which is the strict saving that powers the recursion.
- `address-shear`: Address shear: The invertible permutation of array entries sending address (H,D) to (H+MD,D) for a matrix M, which composes additively and, combined with two linear-cost updates, interchanges the H and D fields.
- `bit-network-interface`: Bit network and rational shear interface: The bit-valued network (XOR gates, W_b wires) with rational projection matrices on gates so that every route's endpoint difference is the identity (the shear H ← H+D) while the total rank of edge differences s_b is below W_b·m.
- `phase-kernel`: Phase kernel C = aI + bX: The two-point Gaussian dyadic kernel C = H S H = aI + bX with a=(1+i)/2, b=(1−i)/2, satisfying C²=X, C⁴=I, C⁻¹ = −iZCZ and H₀ = b S C S, which relates a normalized butterfly to C.
- `complex-network-interface`: Complex phase network interface: The Gaussian-dyadic version of the network with binary-vector labels and phase frames i^{wt(P_U x) mod 4}; each edge's frame change is a product of translation kernels aI+bX_v over an orthonormal basis of the residual, and telescoping gives C^{⊗m} on every role with total length s_c below W_c·m.
- `lower-factorization`: Lower-triangular factorization of a matrix: Every rational matrix A of rank a factors as E₁ Π E₂ with E₁,E₂ invertible lower triangular and Π a partial permutation with exactly a ones (a Bruhat-type factorization in reversed coordinate order).
- `matrix-shear-cost`: Cost of a rational matrix shear: The shear (H,D)↦(H+AD,D) of rank a is performed with exactly a interchanges of b-digit fields plus O(V) further work, using triangular factors as linear-time controlled shifts and one interchange per pivot.
- `rank-deficit-recurrence`: Strict rank deficit gives a power saving: If a call at parameter m·f makes s calls at parameter f, each on a stream of volume V/W, then normalized cost obeys F_k ≤ (s/W)F_{k−1}+O(1); since s/W < m^τ with τ<1 the solution is O(e^τ), a power-of-the-width saving.
- `row-splitting-roles`: Rows distributed cyclically among wire roles: To run the network on an array, whole rows are dealt cyclically into W role streams (padding the row count to a multiple of W per prefix), each of volume V/W with identical remaining shape, and gates act pointwise on matching addresses.
- `power-width-interchange`: Power-width interchange with rows: Using the bit network on W role streams with address shears applied recursively on every edge, two chunks of e = m^k digits are interchanged in O(V e^τ) time, via the XOR combinations of intermediate data whose net effect is an exact permutation.
- `chunk-swap`: Fast address-chunk interchange: Arbitrary-width interchange of two disjoint address chunks of u bits in O(V u^τ) with fixed τ<1: peel off top digits to supply rows, pad rows, decompose the rest in base m and apply the power-width interchange to each piece.
- `packed-rotations`: Carry-free packed controlled rotations: Eight cyclic shifts of whole chunk ranges, conditioned on parities and a control bit, flip the parity of u when the control is 1 and restore the auxiliary w, so that XORs on f selected bit positions can be done at once as long as the K-bit segments have unused guard room.
- `exceptional-address-repair`: Deterministic repair of exceptional addresses: The packed rotations fail only on a set of addresses whose guard values are near the segment boundary, a fraction at most 80(f−1)2^{−K} of all addresses; these records are extracted, sorted by destination rank with stable radix sort, and reinserted, keeping the bound worst-case.
- `packed-selected-bit-addition`: Packed selected-bit addition on one rectangle: One fixed multitape procedure XORs the selected bit (offset ρ of each of f chunks of K bits) of chunk x into chunk y while restoring chunk z, in time O(V(L^τ+1)) plus negligible repair terms; this performs a binary row addition used for change of basis.
- `guard-width`: Guard width for exact intermediate values: The whole recursive C-layer is evaluated exactly with p + Δ fractional bits and Δ + 3 integer bits, where Δ = ⌈C₀ d^{C₁}⌉ bounds the arithmetic depth via A(e) ≤ sA(e/m)+E; since ε·C₁<1, Δ = o(p) and widths stay O(p).
- `phase-frame-layer`: Recursive phase-frame layer on slots: To apply C^{⊗e} on e = m·f selected bits, group the bits into m slots of f chunks, change binary basis by packed row additions, apply the f-fold inverse or forward child on each residual-basis slot (s_c children in total), and change back; inverses cost no extra child since C⁻¹ = −iZCZ.
- `simultaneous-layer`: Simultaneous normalized butterfly layer: H₀ is applied at once to the same bit offset of D ≤ d address chunks of every polynomial record in O(V d^{λ'}) time with λ'<1, via H₀^{⊗D} = b^D S_D C^{⊗D} S_D, the recursive phase-frame layer on rows split among wire roles, exact evaluation and one final truncation.
- `polynomial-ring-negacyclic`: Polynomial ring modulo y^r + 1: Polynomials with complex coefficients of degree below r, with y^r = −1; multiplying by a power y^a is an exact signed cyclic shift of the coefficient list (an isometry), and the wrap-around carries a minus sign (negacyclic).
- `synthetic-roots`: Synthetic root of unity ω_t = y^{2r/t}: Powers of y serve as roots of unity of order t dividing 2r in the ring modulo y^r+1, so multiplying by ω_t^j costs only a signed shift of the coefficient list.
- `synthetic-transform`: Synthetic polynomial transform: The normalized transforms F_t^± over the polynomial ring using synthetic roots, computed by radix-two butterflies plus monomial twiddles (Nussbaumer–Quandalle); character cancellation gives F⁺F⁻ = I/t even though the ring has zero divisors.
- `frequency-order`: Retained stored frequency order: The decimation-in-frequency recursion writes frequency j in slot rev(j) (bit-reversed); the forward transform B·F⁻ keeps this order and the opposite procedure consumes it directly, so no sort is needed between the pointwise product and the inverse.
- `transform-layout`: Transform layout and cost: A positional permutation L moves chosen bit slots to a prefix and groups the remaining bits into K-bit chunks so each transform round is a simultaneous butterfly layer; cost O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]) with error below √2·ℓ·2^{−p}.
- `signed-packing`: Signed Kronecker packing for ring products: Two disk-grid polynomials in the ring mod y^r+1 are multiplied exactly by evaluating coefficients at B₀=2^{4p} as signed integers, multiplying with the established multiplier, extracting centered coefficients, wrapping negacyclically and truncating, in O(rp log(rp)).
- `synthetic-convolution`: Convolution from the retained transform layout: Normalized convolution over the polynomial ring: two forward synthetic transforms keep their layout, records are multiplied pointwise by signed packing, and the opposite transform consumes the same order; error below √2·M(3ℓ+1)2^{−p}.
- `coefficient-twist`: Coefficient twist from cyclic to negacyclic: The isomorphism x_d ↦ ζy with ζ = e^{πi/r} sends cyclic convolution of length r to the ring modulo y^r+1, multiplying coefficient k by ζ^k; the negative wrap exactly cancels the factor ζ^r, so untwisting recovers the cyclic result.
- `gaussian-resampling`: Gaussian resampling with retained permutations: Harvey–van der Hoeven resampling replaces a Fourier transform of coprime length s by one of length t (a power of two) using Gaussian-weighted maps A and B₀; here the two coordinate permutations stay in the identity P_s F_s = 2^{2α²} B₀ P_t F_t A instead of being executed as sorts.
- `tensor-resampling`: Tensor interface for resampling: The resampling identity is applied along each of d axes (lines) of a padded power-of-two box, with axes exposed and restored by chunk interchanges; total cost O(dTp^{3/2+δ}α) for the line maps plus O(Tp d²(1+ℓ^τ)) for data movement.
- `bluestein-chirp`: Bluestein chirp identity: A DFT (here with a frequency permutation) equals pre-multiplication by a chirp phase, a cyclic convolution with the chirp, and post-multiplication by the conjugate chirp, so the middle transform becomes a normalized cyclic convolution.
- `source-permutation-cancel`: Cancellation of the source permutation: The permutation R retained from resampling cancels across the two forward source transforms, their pointwise product and the opposite-sign transform: (R F⁺)[(R F u)·(R F v)] = (u*v)/S².
- `crt-address-map`: Chinese-remainder map to prime cyclic axes: With pairwise coprime lengths s_i, the map x ↦ ∏ x_i^{μ_i} is an isomorphism from cyclic convolution of length ∏s_i to multidimensional cyclic convolution on the prime axes, implemented by triangular controlled shifts on padded axes.
- `chirp-transform`: Middle transform computed by chirp and complex convolution: The padded power-of-two transform Q F_t is computed by chirp phase products, a complex cyclic convolution obtained through the coefficient twist and synthetic convolution, and a final chirp product, with error below 8TL·2^{−p}.
- `source-transform`: Source transform procedure: The computed transform of a prime-axes source array: expand axes by A, apply the chirp transform on power-of-two axes, compress with B₀, and scale by 2^γ; its exact counterpart is R F_s, and the opposite-sign version is obtained by conjugation.
- `parameter-choice`: Size parameters of the algorithm: From the input length n: b = ⌈log₂ n⌉, working precision p = 6b, number of axes d = ⌊b^ε⌋, chunk width K = ⌊d^c⌋, padded box size T ≈ n/b, axis lengths r or r/2, resampling parameter α, with fixed tiny rationals ε, c, τ, λ', δ.
- `prime-lengths`: Distinct prime source lengths near powers of two: Pairwise-distinct odd primes s_i with (1−2η)t_i < s_i ≤ (1−η)t_i are found by trial division; they give gcd(s_i,t_i)=1, T/2 < S < T and the separation t_i/s_i − 1 needed by Gaussian resampling.
- `exact-recovery`: Exact recovery by rounding and carry propagation: The scaled computed convolution has error below 1/2, so rounding each real part to the nearest integer yields the true integer coefficients, and radix carries propagated least significant first produce the exact 2n-bit product.
- `multiplication-algorithm`: The complete multiplication algorithm: Convert the inputs to radix digits, apply the CRT map to prime axes, compute the two source transforms, multiply pointwise, compute the opposite transform, rescale by S and 2^{2b+4}, round, undo the CRT map and propagate carries to output the exact product.
- `cost-analysis`: Cost analysis and the exponent κ: Dividing all costs by Tp = Θ(n) gives a table of seven dominant terms whose powers of p are all at most 1 − 2κ for κ = 2^{−182}, so the total is O(n (lg n)^{1−κ}) with schoolbook multiplication for small inputs.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, by reducing to convolution over the polynomial ring with fast chunk interchanges and simultaneous butterfly layers, disproving the n log n optimality conjecture.

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
