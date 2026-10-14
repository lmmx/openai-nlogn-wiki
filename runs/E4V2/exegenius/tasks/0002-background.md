# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/P2` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Sums of powers of an indeterminate with coefficients, multiplied by collecting terms.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, with modulus and the unit-modulus numbers e^{iθ}.
- `turing-machine`: Multitape Turing machine (known to the reader): A machine with a finite alphabet, a finite control and a fixed number of tapes, each read and written one cell per step by a head.
- `bitwise-xor`: Bitwise XOR and arithmetic mod 2 (known to the reader): Addition of bits modulo 2, so that x ⊕ x = 0.
- `integer-multiplication-problem`: Exact integer multiplication on a multitape Turing machine: Given x#y with x,y n-bit binary strings, output the 2n-bit binary product; cost is the number of steps of one fixed machine with a fixed alphabet and a fixed number of one-dimensional tapes, and lg n = max(⌈log₂ n⌉, 1).
- `optimality-conjecture`: Schönhage–Strassen n log n optimality conjecture: The 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers, which is stated here as an eventual lower bound T_A(n) ≥ c·n lg n for every fixed machine A; the paper refutes it.
- `harvey-hoeven-multiplier`: Established O(n log n) multiplier (Harvey–van der Hoeven): The previously known fixed-tape algorithm multiplying N-bit integers in O(N log N) time, used here only as an ordinary subroutine on short records and never recursively on the improved theorem.
- `dft`: Normalized discrete Fourier transform: The map sending a length-q vector u to (F_q u)_k = (1/q) Σ_j u_j e^{−2πi jk/q}; the opposite-sign transform F⁺ uses e^{+2πi jk/q}, and each is a contraction in the max-modulus norm.
- `cyclic-convolution`: Cyclic convolution and the convolution theorem: The convolution f*g on a cyclic group, which the Fourier transform turns into a pointwise product (F(u*v) = S·(Fu)·(Fv) with size normalizations), so convolution can be computed by transform, pointwise multiply, inverse transform.
- `multiplication-by-convolution`: Integer multiplication as convolution of radix digits: Write each operand as a polynomial in 2^b with radix-2^b digit coefficients; the product coefficients are a convolution of digit lists (each below 2³ᵇ), padded so cyclic convolution has no wraparound, and carries recover the integer product.
- `fft-butterfly`: Two-point butterfly and radix-2 fast Fourier transform: The butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) pairs entries half a block apart; a decimation-in-frequency transform of length 2^a applies butterflies and twiddle-factor multiplications over a levels and leaves the output in bit-reversed order.
- `linear-algebra-basics`: Matrix rank, subspaces and orthogonal complements: Vector subspaces, rank and dimension of a matrix, projections onto a subspace along its orthogonal complement, and bilinear forms (nondegenerate when no nonzero vector is orthogonal to the whole space).
- `tensor-product`: Tensor products of operators and arrays: The Kronecker product of linear maps or index sets, so an operator on several coordinates (columns, axes) acting identically on each is written as a tensor power.
- `multidimensional-transform`: Multidimensional transform on a tensor of axes: The tensor product F_{q₁}⊗…⊗F_{q_d} of one-dimensional Fourier transforms over d axes, computed one axis (line) at a time, with multidimensional cyclic convolution handled the same way.
- `fixed-point-disk-arithmetic`: Disk-grid fixed-point arithmetic, contractions and error: Complex numbers with real and imaginary parts that are multiples of 2^{−p} in the unit disk, stored as two signed two's-complement words; Q_p truncates toward zero, linear contractions do not increase the max norm, and errors of composed approximations add.
- `elementary-streams`: Array order and elementary stream scans: Arrays stored in lexicographic order on a tape, with address fields and rows; fixed digit permutations, digit moves, splitting into aligned streams, pointwise maps and merging are done in time linear in the volume with counters and rewinds charged.
- `controlled-cyclic-shifts`: Controlled cyclic shifts and fixed rational scalings: Updating a target address field y ↦ y + a(controls) mod q^b, where the controls precede the target on tape, by splitting each fiber into two pieces and merging in swapped order in linear time; also multiplication by fixed rational units mod q^b.
- `crt-address-map`: Chinese-remainder address map to distinct prime axes: An algebra isomorphism x ↦ Π x_i^{μ_i} turning one cyclic convolution of length S = Π s_i (pairwise coprime) into a d-dimensional cyclic convolution on prime axes, implemented as triangular controlled shifts plus axis reordering and zero padding.
- `gaussian-resampling`: Gaussian resampling with permutations left in the transform: Replaces a Fourier transform of length s (coprime to t, s<t) by one of length t via Gaussian-weighted contractions A and B₀, with P_s F_s = 2^{2α²} B₀ P_t F_t A, where the two coordinate permutations P_s, P_t stay inside the formula instead of being sorted separately; applied axis by axis for a tensor.
- `bluestein-chirp`: Bluestein chirp identity: Writes the (permuted) transform Q·F_t as pointwise multiplication by a chirp ā, a cyclic convolution with the chirp a, and another pointwise multiplication by ā, so a transform becomes a normalized cyclic convolution.
- `permutation-cancellation`: Source permutation cancellation: Because the coordinate permutation R commutes with pointwise products and R F⁺ R = F⁺, the retained permutation in R F_s cancels across two forward transforms, a pointwise product and the opposite transform, giving (u*v)/S².
- `polynomial-ring-mod`: Polynomial ring modulo yʳ + 1: The ring of complex polynomials of degree less than r with y^r = −1, where multiplying by a power of y permutes the coefficients with sign changes (a signed shift) and so acts as an isometry in the max coefficient norm.
- `coefficient-twist`: Coefficient twist from cyclic to negacyclic wrap: The isomorphism C[x]/(x^r−1) → C[y]/(y^r+1), x ↦ ζy with ζ = e^{πi/r}, which multiplies coefficient k by ζ^k so the negative wrap of the ring becomes the cyclic wrap after untwisting.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the polynomial ring with roots of unity ω_t = y^{2r/t}, so twiddle multiplications are signed shifts; computed by butterflies H₀ and twiddles, leaving outputs in bit-reversed frequency order that is retained through the pointwise product and consumed by the opposite transform.
- `signed-packing`: Signed packing of polynomial products (Kronecker substitution): Evaluating integer polynomials at B₀ = 2^{4p} to get integers, multiplying them with the established multiplier, and extracting signed coefficients by centered residues, then reducing modulo y^r + 1, to multiply ring elements in O(rp log(rp)).
- `scalar-exchange-network`: Linear exchange network with restored scratch wires: A fixed network of linear gates (copy, gather, scatter, side injection) built on triples of an h-element set that exchanges two banks of values (X,Y) ↦ (−Y,X) in three stages while restoring all scratch wires whatever their initial values.
- `frames`: Frames: changing array representation along network edges: Replacing each scalar by an array and attaching an invertible linear operator D_v (frame) to each vertex lets pointwise gates commute with the frame, so the net effect on a route is the endpoint operator D_sink D_source^{-1}.
- `subspace-labels-rank-saving`: Nested subspace labels and the total-rank saving: Subspaces of a bilinear space built from triple indicator vectors are attached to gates so adjacent labels are nested; edge cost is the dimension of the orthogonal residual, and the total s over all edges is less than (number of wires) × (space dimension).
- `rational-matrix-interface`: Bit-network rational matrix interface: Assigns rational matrices M_v to gates and terminals of the bit network so that endpoint differences equal the identity and the edge ranks sum to s_b < W_b·m, giving the exponent τ = 1 − 2^{-50} with s/W < m^τ.
- `lower-triangular-factorization`: Lower triangular factorization of a matrix: Every rational m×m matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones.
- `address-shear-cost`: Cost of a rational matrix shear: The address map (H,D) ↦ (H + AD, D) over Z/q^b for a matrix A of rank a is done with exactly a interchanges of b-digit fields plus linear work, by triangular controlled shifts around each pivot and the three-step swap trick.
- `fixed-tape-recursion-schedule`: Depth-first schedule of recursive calls on fixed tapes: Recursive calls on W role streams are run on a fixed set of tapes by parking inactive streams on a stack, copying the active stream to the child, and restoring on return, at O(V) extra cost per node.
- `power-width-interchange`: Recursive power-width chunk interchange: Splits rows cyclically into W role streams, applies the network with shear frames on each edge (s recursive interchanges of chunks of width e/m, each on volume V/W), giving F_k ≤ (s/W)F_{k−1} + O(1) and cost O(V e^τ), because s/W < m^τ.
- `chunk-interchange`: Fast interchange of address chunks: Exchanging two disjoint equal-width address chunks (p,h,g,d,z) ↦ (p,d,g,h,z) of u bits in O(V u^τ) time, τ < 1, for arbitrary shapes; internally the permutation is a sequence of XOR combinations.
- `phase-kernel`: Two-point phase kernel C: The 2×2 matrix C = H S H = aI + bX with a = (1+i)/2, b = (1−i)/2, satisfying C² = X, C⁴ = I and H₀ = b·S·C·S, so a butterfly equals a diagonal phase, a C kernel, and another phase.
- `phase-frame-interface`: Binary phase interface of the complex network: Using frames C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} for binary labels, every edge change is a product of translation kernels aI + bX_v, one per orthonormal residual basis vector, so s_c smaller calls of C^{⊗} suffice and the whole network realizes C^{⊗m} on every role.
- `packed-selected-bit-addition`: Packed selected-bit addition on one rectangle: XORs the selected bits of several chunks into another chunk with a few whole-chunk cyclic shifts that act as packed single-bit additions away from carry-prone guard values, then repairs the small explicitly identified bad set of addresses by sorting, restoring a third scratch chunk.
- `guard-width-exactness`: Exact Gaussian dyadic evaluation with guard bits: All intermediate values in one butterfly layer are exact Gaussian dyadics (real and imaginary parts with power-of-two denominators), so extra guard bits of width O(d^{C₁}) bound growth and a single truncation follows the completed contractive layer.
- `simultaneous-butterfly-layer`: Simultaneous normalized butterfly layer: Applies H₀ at once to the same bit position of D ≤ d address chunks of a polynomial-record array via the C-kernel network with phase frames, packed binary basis changes and row splitting among roles, in O(V d^{λ'}) time for a fixed λ' < 1 instead of D whole-array passes, with one final truncation.
- `synthetic-transform-layout`: Transform layout on which parallel layers apply: Places the selected bits of all axes at a common offset of consecutive K-bit chunks using prefix-slot moves and chunk exchanges, so each transform round is one simultaneous butterfly layer; total cost O(Tp[dK + pK^{τ−1} + ℓ d^{λ'}]).
- `synthetic-convolution`: Convolution over the polynomial ring from the retained transform layout: Normalized convolution M_r(f,g) = (f*g)/(rM): two forward synthetic transforms, pointwise ring products by signed packing in the retained stored order, and the opposite transform, with error below √2·M(3ℓ+1)·2^{−p}.
- `parameter-choice`: Parameter choice: precision, dimension, axis lengths and prime source lengths: For input length n, take b = ⌈log₂ n⌉, precision p = 6b, dimension d = ⌊b^ε⌋, chunk K = ⌊d^c⌋, power-of-two axis lengths t_i ∈ {r/2, r} with product T ≈ n/b, and distinct odd primes s_i just below t_i with T/2 < S < T so all resampling hypotheses hold.
- `precision-exact-recovery`: Precision, rounding and carry propagation: Tracks scales (the two factors S and 2^{2b+4}) and disk margins to show the recovered convolution coefficients have error below 1/2, rounds to nearest integers, and propagates radix-2^b carries to output the exact 2n-bit product.
- `multiplication-algorithm`: The multiplication algorithm: digits to transform, pointwise product and back: Convert operands to digit lists on a padded prime-axis box via Φ, apply the source transform (resample, chirp convolution through the twist, resample) to each, multiply pointwise, apply the opposite transform, scale by S and 2^{2b+4}, undo Φ, round and propagate carries.
- `time-bound-accounting`: Time-bound accounting and the exponent κ: Dividing the costs of all stages by Tp = Θ(n) gives a table of normalized costs, each a power of p of at most 1 − 2κ (the minimum margin is 2^{−181} = 2κ with κ = 2^{−182}), so the total is O(n (lg n)^{1−κ}).
- `main-theorem`: Power-saving integer multiplication theorem: One deterministic multitape Turing machine multiplies n-bit integers exactly in O(n (lg n)^{1−κ}) worst-case time with κ = 2^{−182}, disproving the n log n optimality conjecture in this model; it combines fast address interchange, fast simultaneous butterfly layers, and the resampling–chirp–synthetic-convolution reduction.

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
