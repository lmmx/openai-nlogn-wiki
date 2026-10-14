# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/P1` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Expressions Σ aₖ xᵏ with coefficients, their addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with i²=−1, with modulus, conjugate and unit-modulus phases e^{iθ}.
- `turing-machine-tapes`: Multitape Turing machine (known to the reader): A machine with finitely many states, a finite alphabet and one-dimensional tapes whose heads move one cell per step.
- `linear-algebra-basics`: Matrices, rank, subspaces and orthogonality: Matrices over a field, their rank, subspaces, orthogonal complements under a bilinear form, and tensor products of spaces.
- `modular-arithmetic`: Modular arithmetic and the Chinese remainder theorem: Arithmetic on residues mod q, units, inverses mod q, gcd, and the fact that coprime moduli split a residue ring into a product.
- `convolution`: Convolution and cyclic convolution: The product of two coefficient lists as polynomials; cyclic convolution wraps indices mod a length, so that it is multiplication in C[x]/(x^S−1).
- `dft`: Discrete Fourier transform and the convolution theorem: The length-q transform (F_q u)_k = (1/q) Σ u_j e^{−2πi jk/q} built from roots of unity; it turns convolution into pointwise product and is inverted by the opposite-sign transform.
- `fft-butterfly`: Butterfly and FFT recursion: The fast evaluation of a length-t transform by pairing entries z_k and z_{k+t/2}, applying a two-point butterfly, multiplying by twiddle roots and recursing on both halves.
- `multidimensional-transform`: Multidimensional transform (tensor product): A transform on an array indexed by several axes, equal to applying the one-dimensional transform along each axis in turn; convolution on a product of cyclic groups is diagonalised by it.
- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's 1971 conjecture that n log n is the optimal order of multiplication cost on multitape Turing machines; the paper refutes any eventual Ω(n log n) lower bound for a fixed machine.
- `nlogn-multiplier-subroutine`: The established O(n log n) multiplier as a subroutine: Harvey and van der Hoeven's existing O(N log N) integer multiplication, called as an ordinary black box on shorter records (not the improved algorithm).
- `fixed-point-disk-grid`: Fixed-point disk grid and truncation: Complex numbers of modulus at most 1 whose real and imaginary parts are multiples of 2^{−p}, stored as signed two's-complement numerators, with Q_p truncating toward zero.
- `contractions-and-error`: Contractions and error accumulation: A linear map is a contraction if it does not increase the maximum-modulus norm; approximate algorithms for contractions compose with errors that add.
- `guard-bits-dyadic`: Exact Gaussian dyadic arithmetic and guard bits: Intermediate values with power-of-two denominators are kept exact by allocating extra integer and fractional guard bits, and rounded only once after a whole layer.
- `tape-address-arrays`: Arrays, addresses, rows and volume on tape: Arrays with multi-field addresses stored in lexicographic order on a tape, with address fields, row fields, prefix and suffix, spectator fields and logical volume V in bits.
- `elementary-stream-operations`: Elementary stream operations: Linear-time tape scans: permuting two digit positions, moving a digit, splitting into streams and merging, and splitting whole rows cyclically into W streams.
- `controlled-shifts`: Controlled shifts: Updating a later address field by an offset computed from earlier fields (y ↦ y+a mod q^b), or multiplying it by a rational unit, in linear time.
- `row-splitting`: Row splitting among roles with padding: Distributing whole rows cyclically among the W wire roles, after padding the row count to a multiple of a power of W, so each role stream has volume V/W.
- `fixed-tape-recursion`: Depth-first recursion on fixed tapes: Running recursive calls with finitely many tapes by parking inactive role streams on a stack tape, copying the active one to the child, and restoring afterwards, at cost linear in the parent's volume.
- `linear-network-roles`: Linear network with roles and restored scratch: A fixed network of linear gates on wires (roles) that exchanges two banks of values with signs while restoring every auxiliary (scratch) wire whatever its initial contents.
- `triple-subset-gadget`: Three-subset gather, scatter and side-wire gadget: The scalar gadget on three-element subsets of [100]: copy, gather, scatter and side injection with intersection-size coefficients, scheduled in 8 rows so that y_S gains x_S independently of scratch values.
- `frames`: Frames and edge operators: Invertible operators D_v on a wire's address-indexed array attached to each network vertex; a common frame commutes with pointwise linear gates, so only edges D_v D_u⁻¹ need implementing and the endpoints determine the net operator.
- `subspace-labels-rank-deficit`: Nested subspace labels and rank deficit: Nondegenerate subspaces of a fixed m-dimensional space attached to gates and terminals, nested along edges, so that the total dimension change s over all edges is strictly less than W·m, where W is the wire count.
- `address-shear`: Address shear interface: The endpoint operator of the bit network: fields H, D over a residue ring updated by (H,D) ↦ (H+MD,D), with matrices M at vertices whose differences give rank-many smaller interchanges per edge.
- `triangular-factorization`: Lower triangular factorization and matrix shear cost: Every rational matrix factors as E₁ΠE₂ with E₁, E₂ lower triangular and Π a partial permutation with rank-many ones, so a shear by A costs rank(A) interchanges plus linear work.
- `recursive-power-saving`: Recursive power saving: When a size-mf call uses s calls of size f on streams of volume V/W with s<Wm, the normalized cost satisfies F_k ≤ (s/W)F_{k−1}+O(1), giving cost O(V e^τ) with τ<1 instead of a factor e.
- `address-chunk-interchange`: Fast address-chunk interchange: The first tape procedure: swapping two disjoint u-bit address chunks of an array by recursion on the bit network in O(V u^τ) time for a fixed τ<1, intermediate steps computing XORs but the final effect an exact permutation.
- `butterfly-and-phase-kernels`: Butterfly kernel H₀ and phase kernel C: The two-point butterfly H₀(u,v)=((u+v)/2,(u−v)/2) and the kernel C=aI+bX with a=(1+i)/2, b=(1−i)/2, related by H₀=b·S·C·S with S=diag(1,i), so a layer of H₀ equals phases times a layer of C.
- `binary-phase-interface`: Binary phase interface: The complex network with binary labels, in which each edge's frame change is a product of translation kernels aI+bX_v, one per residual basis vector, so that telescoping gives C⊗m on every role.
- `packed-selected-bit-addition`: Packed selected-bit addition: XORing corresponding selected bits of two address chunks across many chunks at once, using a temporary third chunk, a few cyclic shifts, and a deterministic repair of a small exceptional set of addresses.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The second tape procedure: applying H₀ at the same bit position in d address chunks of every record in O(V d^λ') time, evaluated exactly with guard bits and truncated once.
- `polynomial-ring-mod-y-r-plus-1`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree < r with y^r = −1; multiplication by a power of y is a signed shift of the coefficient list.
- `synthetic-polynomial-transform`: Synthetic polynomial transform: A multidimensional transform over the ring mod y^r+1 whose roots of unity are powers of y, so twiddle multiplications are signed shifts and only butterflies cost arithmetic.
- `frequency-order-retention`: Retained frequency order: Leaving transform outputs in the bit-reversed order the recursion writes them, so the pointwise product and the opposite transform consume that order without a separate permutation.
- `synthetic-transform-layout`: Transform layout for parallel layers: The tape layout that places the selected bits of the participating axes at a common offset in consecutive K-bit chunks, using bit moves and chunk interchanges, so each transform round is one simultaneous butterfly layer.
- `signed-packing`: Signed packing (Kronecker substitution): Evaluating integer-coefficient polynomials at 2^{4p} to turn polynomial products into integer products, with signed carries and centered extraction of coefficients.
- `synthetic-convolution`: Ring convolution from the retained transform layout: Normalized convolution over the ring: two forward synthetic transforms, pointwise ring products by signed packing, then the opposite transform, with error below √2 M(3ℓ+1)2^{−p}.
- `phase-twist`: Phase twist from cyclic to negacyclic: Multiplying coefficient k of the last cyclic axis by ζ^k with ζ=e^{πi/r} turns x^r−1 into y^r+1, so complex cyclic convolution is computed by ring convolution and the untwist.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's identity converting a Fourier transform of prime-ish length s into one of larger length t via Gaussian-weighted maps S and T, with a near-identity correction N.
- `resampling-permutations-retained`: Resampling with the permutations left in the transform: The paper's variant P_s F_s = 2^{2α²} B₀ P_t F_t A that keeps the coordinate permutations in the identity instead of executing two sorts per axis.
- `bluestein-chirp`: Bluestein chirp identity: Rewriting a transform as pointwise chirp phases around a cyclic convolution with a chirp kernel, which here also absorbs the target permutation.
- `permutation-cancellation`: Source permutation cancellation: The retained source permutation R cancels across two forward source transforms, their pointwise product and the opposite-sign transform, leaving (u*v)/S².
- `crt-address-map`: Chinese-remainder address map: An algebra isomorphism from cyclic convolution of length S=∏s_i (s_i pairwise coprime) to convolution on the product of cyclic axes, implemented by triangular controlled shifts.
- `integer-as-digit-convolution`: Integer product as radix-digit convolution: Writing both inputs in base 2^b with q digits, the integer product is the convolution of the digit lists; padding to length S exceeds the degree so no wraparound occurs and coefficients stay below 2^{3b}.
- `parameter-choice`: Parameter choices and padded box: The sizes p=6b, d=⌊b^ε⌋, K=⌊d^c⌋, T in [4n/b,8n/b), r=2^⌈(log₂T)/d⌉ and axis lengths t_i∈{r/2,r}, with α, γ, η and fixed rational exponents.
- `prime-source-lengths`: Prime source lengths: Distinct odd primes s_i in (1−2η)t_i < s_i ≤ (1−η)t_i near each power of two t_i, found by deterministic trial division, so that T/2<S<T and each ratio t_i/s_i leaves enough separation for resampling.
- `source-transform`: Source transform pipeline: The approximate source transform: resample with A along each axis, apply the chirp transform via ring convolution, compress with B₀, and rescale by 2^γ, equal to R F_s.
- `exact-recovery`: Exact recovery by scaling, rounding and carries: Removing the known normalizations S and 2^{2b+4}, proving the coefficient error is below 1/2, rounding to integers and propagating radix-2^b carries to the exact 2n-bit product.
- `multiplication-algorithm`: The multiplication algorithm: The six steps: form radix digits, apply the address map Φ, compute two source transforms, multiply pointwise, apply the opposite transform, rescale, round and carry.
- `cost-analysis`: Cost analysis and the exponent κ: The table of normalized costs per Tp, each at most p^{1−2κ}, with the smallest margin 2^{−181}=2κ, giving total O(n (lg n)^{1−κ}) for κ=2^{−182}.
- `integer-multiplication-below-nlogn`: Integer multiplication in O(n (lg n)^(1−κ)) time: The main theorem: one deterministic fixed-alphabet, fixed-tape Turing machine multiplies n-bit integers in O(n(lg n)^{1−κ}) worst-case time, refuting the n log n conjecture, via synthetic transforms accelerated by the interchange and butterfly procedures.

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
