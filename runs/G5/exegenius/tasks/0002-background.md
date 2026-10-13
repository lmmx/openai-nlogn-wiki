# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/G5` (paths below are relative to it)

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
- `multitape-tm`: Turing machines with tapes (known to the reader): A Turing machine reads and writes cells on one or more tapes with moving heads, one step at a time.
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, multiplied by convolving coefficient lists.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, with modulus and phase.
- `roots-of-unity`: Roots of unity (known to the reader): Complex numbers ω with ω^t = 1; powers of a primitive one cycle through all of them.
- `modular-arithmetic`: Modular arithmetic (known to the reader): Arithmetic with remainders modulo an integer, including units, inverses and gcd.
- `binary-arithmetic`: Binary integers and XOR (known to the reader): Binary representation of integers, bitwise XOR, carries, and fixed-width two's-complement words.
- `linear-algebra`: Basic linear algebra (known to the reader): Matrices, rank, subspaces, tensor products and orthogonal projection.
- `fixed-tape-model`: Fixed finite-tape Turing machine model: The computation model: one fixed machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, whose steps move each head by at most one cell.
- `nlogn-conjecture`: Optimality conjecture for multiplication: Schönhage and Strassen's 1971 proposal that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine, which the paper refutes.
- `nlogn-multiplier`: Established n log n multiplier: The Harvey–van der Hoeven O(N log N) multiplication algorithm for N-bit integers, used here only as an ordinary subroutine on short inputs.
- `stream-scans`: Array order and linear-time stream scans: Arrays are stored in lexicographic address order on tape; splitting on a digit, moving a digit, applying a pointwise map and merging all cost O(V) for volume V.
- `controlled-shifts`: Controlled cyclic shifts and rational scalings: A target address field can be rotated by an offset computed from earlier control fields, or multiplied by a unit modulo q^b, in linear time.
- `convolution`: Cyclic convolution: The operation combining two coefficient arrays so that coefficient j of the result sums products of entries whose indices add to j modulo the length; it is polynomial multiplication with wraparound.
- `radix-digit-reduction`: Reducing integer multiplication to digit convolution: Writing each integer as a polynomial in 2^b with b-bit digits turns the product into a convolution of digit lists; padding avoids wraparound, and rounding plus carry propagation recover the bits.
- `dft`: Discrete Fourier transform and convolution theorem: The normalized transform (F_q u)_k = (1/q) Σ u_j e^{−2πi jk/q}, which turns cyclic convolution into pointwise multiplication.
- `fft-butterfly`: Radix-2 FFT butterflies: A length-t transform is computed in log t levels, each pairing entries k and k+t/2 with the two-point butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) and a twiddle multiplication.
- `multidimensional-transform`: Multidimensional transforms on power-of-two axes: A transform over several axes is the tensor product of one-dimensional transforms, applied axis by axis to an array indexed by a product of axis lengths.
- `crt-prime-axes`: Chinese-remainder map onto distinct prime axes: A ring isomorphism sends a length-S cyclic convolution to a multidimensional cyclic convolution on pairwise coprime axes s_i; on tape it is a sequence of triangular controlled shifts.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven technique expressing a Fourier transform of prime-like length s through one of a larger power-of-two length t, using Gaussian-weighted contractions A and B₀ and two coordinate permutations.
- `chirp-identity`: Bluestein chirp identity: A phase-weighted identity that rewrites a Fourier transform, including its frequency permutation, as a cyclic convolution with a chirp array a_j = exp(−πi Σ s_i j_i²/t_i) between pointwise phase multiplications.
- `retained-permutations`: Resampling with retained permutations: Instead of sorting twice per coordinate, the source and target coordinate permutations stay inside the transform formula R F_s = 2^γ B₀ Q F_t A; the source permutation then cancels across the two forward transforms and the opposite one.
- `polynomial-ring`: Polynomial ring modulo yʳ + 1: Complex polynomials of degree below r with y^r = −1, so that multiplying by a power of y is a signed shift of the coefficient list; powers of y serve as roots of unity.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform whose roots of unity are powers ω_t = y^{2r/t} of the ring variable, so twiddle multiplications are exact signed shifts and only butterflies cost arithmetic.
- `stored-frequency-order`: Retained frequency order of the transforms: The forward transform writes frequency j into slot rev(j), and the opposite transform consumes exactly that bit-reversed order, so no reordering sort is needed between the two.
- `coefficient-twist`: Phase twist to a negacyclic wrap: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} turns convolution modulo x^r − 1 into convolution modulo y^r + 1 on the last axis, and untwisting restores the cyclic wrap.
- `signed-packing`: Signed Kronecker packing of polynomial products: Ring elements are evaluated at B₀ = 2^{4p} as signed integers, multiplied with the established multiplier, and unpacked by centered residues and carries, giving exact polynomial products.
- `fixed-point-disk`: Disk-grid fixed-point arithmetic: Complex values in the unit disk stored as 2^{-p} times Gaussian-integer numerators in two's complement; layers are computed exactly in Gaussian dyadics with guard bits and then truncated toward zero by Q_p.
- `subset-gadgets`: Three-element subset gadgets: Copy, side-injection, gather and scatter maps on indicator vectors of three-element subsets whose net effect adds x_S to y_S, because central coefficients depend only on intersection sizes and side wires cancel the unwanted ones.
- `bank-exchange-network`: Linear bank-exchange network with restored scratch wires: A fixed network of linear gates on wires that, using three stages of the subset gadgets, exchanges two data banks (X,Y)→(−Y,X) while restoring every auxiliary scratch wire to its arbitrary initial value.
- `frames`: Frames and the common-frame identity: An invertible linear operator D_v on each wire's address-indexed array at each vertex; because gates are pointwise and linear they commute with a common frame, so the network realizes D_out S D_in^{-1}.
- `subspace-labels`: Nested subspace labels and orthogonal residuals: Each gate and terminal carries a nondegenerate subspace of a fixed bilinear space, adjacent labels are nested, and the orthogonal residual of an edge has dimension equal to the label change, so the total rank cost is Wm − 2N + 2L.
- `bit-network-interface`: Bit network and its rational matrix interface: Using XOR gates and projections P_U as frame matrices, the bit network permutes its roles and the endpoint matrices differ by the identity, so the net effect on arrays is the shear H ← H + D.
- `rank-saving`: Rank saving of the finite networks: The sum s of edge ranks is strictly less than the wire count W times the dimension m, so a recursive call on width m·f uses s calls on volume V/W each and the cost per volume grows by s/W < m, which gives the power saving.
- `two-point-kernel`: Two-point phase kernel C: The 2×2 kernel C = H S H = aI + bX with a = (1+i)/2, b = (1−i)/2, satisfying C² = X and C⁴ = I and related to the butterfly by H₀ = b S C S.
- `phase-interface`: Binary phase interface of the complex network: With Gaussian-dyadic scalars and binary labels, each edge's frame change is a product of translation kernels aI + bX_v, one per residual basis vector, and telescoping the frames yields C^{⊗m} on every role.
- `matrix-factorization`: Lower-triangular factorization of a matrix: Every rational m×m matrix of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
- `matrix-shear`: Rank-bounded matrix shear on address fields: The permutation (H,D) ↦ (H + AD, D) of address fields over Z/q^b costs exactly rank(A) interchanges of b-digit fields plus linear work, since triangular parts are controlled shifts.
- `power-width-interchange`: Recursive power-width interchange: For width e = m^k, a shear circuit built from the bit network turns one interchange of two e-digit chunks into s interchanges of width e/m on role streams of volume V/W, giving cost O(V e^τ).
- `address-interchange`: Fast address-chunk interchange: Exchanging two disjoint contiguous address fields of u bits in an array with product address set costs O(V u^τ) for a fixed τ < 1, although intermediate steps form XOR combinations of data.
- `packed-selected-bit-addition`: Packed selected-bit addition with repair: XORing one selected bit position of f chunks into another chunk is done by a few cyclic shifts of whole chunk ranges, followed by a deterministic repair of the small set of addresses where guard values fail.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The butterfly H₀ applied at once to the same bit position of up to d address chunks of polynomial-record arrays, computed via C^{⊗D} on the phase network, at cost O(V d^{λ'}) instead of d passes.
- `transform-layout`: Transform layout for parallel butterfly rounds: A positional address permutation moves the selected bits of all axes into common-offset consecutive K-bit chunks so each transform round is one simultaneous butterfly layer; it costs O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]).
- `ring-convolution`: Convolution from the retained transform layout: Two forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform, all in one retained order, give the normalized convolution (f*g)/(rM) over the polynomial ring with explicit error.
- `parameter-regime`: Parameter regime for input length n: All sizes are tied to b = ⌈log₂ n⌉: precision p = 6b, d = ⌊b^ε⌋ axes, K = ⌊d^c⌋, padded size T about n/b, record length r = 2^{⌈log₂T/d⌉} so that Tp = Θ(n) and r grows faster than any power of p.
- `prime-lengths`: Prime source lengths near powers of two: Distinct odd primes s_i with (1−2η)t_i < s_i ≤ (1−η)t_i are found by deterministic search, so S = ∏s_i lies in (T/2, T) and each ratio t_i/s_i leaves enough separation for Gaussian resampling.
- `precision-recovery`: Error analysis and exact recovery of the product: Every call returns disk-grid values with bounded error and norm margins; after removing the known scales the coefficient error is below 1/2, so rounding gives the exact integer coefficients and carries give the product.
- `multiplication-algorithm`: The multiplication algorithm: Digits are placed on prime axes by the CRT map, transformed by resampling, chirp and polynomial-ring convolution, multiplied pointwise, transformed back with the opposite sign, rescaled, rounded and carry-propagated to give the 2n-bit product.
- `time-bound`: Complete time bound and the power saving: Dividing costs by Tp, the seven dominant terms (layout moves, chunk exchanges, butterfly rounds, CRT layouts, Gaussian line maps, chirps, packed products) have exponents at most 1 − 2κ of p, giving O(n (log n)^{1−κ}).
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-tape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{−182}, beating the n log n conjecture by a power of the logarithm.

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
