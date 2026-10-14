# exegenius task 0002-background

Project directory: `/tmp/claude-0/-home-user/979e8242-2c77-5242-991d-0bed1baea8dd/scratchpad/e6/F5` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Finite sums of coefficients times powers of a variable, added and multiplied coefficientwise.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with i² = −1, with modulus, conjugation and roots of unity e^{2πi/k}.
- `turing-machine-basics`: Turing machines and tapes (known to the reader): A finite-state machine with read/write heads moving over tapes of symbols from a finite alphabet.
- `binary-integers`: Binary integers (known to the reader): Nonnegative integers written as bit strings, with addition, shifting and two's-complement signed forms.
- `modular-arithmetic`: Modular arithmetic (known to the reader): Arithmetic on residues modulo m, including units, inverses and the Chinese remainder theorem.
- `linear-algebra-basics`: Matrices, rank and linear maps (known to the reader): Matrices as linear maps, rank, invertibility, subspaces, projections and tensor (Kronecker) products.
- `multitape-model`: Fixed-tape Turing machine model: The cost model: one fixed finite alphabet and one fixed finite number of one-dimensional tapes, where a step touches one cell per tape and time counts steps.
- `array-layout`: Arrays, address fields and logical volume: Data is stored as a stream in lexicographic address order over a product of fields; the logical volume V counts stored bits and rows are consecutive blocks over a suffix field.
- `elementary-streams`: Elementary stream operations: Linear-time scans on fixed tapes that permute digit values, move one digit, split a stream on a digit, apply a pointwise map to aligned streams and merge, or split whole rows cyclically among W streams.
- `controlled-shifts`: Controlled cyclic shifts and rational scalings: A later target field can be shifted cyclically by an offset computed from earlier control fields, or multiplied by a unit modulo q^b, in linear time by splitting and merging blocks.
- `cyclic-convolution`: Cyclic convolution: The convolution of two length-S sequences with indices added modulo S, which is polynomial multiplication in C[x]/(x^S − 1).
- `discrete-fourier-transform`: Normalized discrete Fourier transform: The map u ↦ (1/q) Σ_j u_j e^{−2πi jk/q} on length-q vectors; it turns cyclic convolution into pointwise product, is inverted by the opposite-sign transform up to scaling, and is a contraction in the maximum norm.
- `multidimensional-transform`: Multidimensional transforms and convolution on several axes: Tensor-product transforms and cyclic convolution on arrays indexed by a product of axes, applied one axis at a time, with the maximum-norm contraction property preserved.
- `fixed-point-numerics`: Fixed-point complex arithmetic and truncation error: Complex values are stored as pairs of signed integers over a 2^p grid inside the unit disk, truncated toward zero by Q_p; contractions pass errors through unchanged and errors of composed steps add.
- `radix-digit-convolution`: Integer multiplication as digit convolution: Writing each operand in radix 2^b turns the product into a convolution of short digit polynomials whose coefficients are small integers; carries then recover the binary product.
- `nlogn-multiplier`: Established O(n log n) integer multiplier: The Harvey–van der Hoeven multitape algorithm multiplying N-bit integers in O(N log N), used here only as a black-box subroutine on short records.
- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's 1971 proposal that n log n is the optimal order of growth for multitape multiplication, which a power saving in the log factor refutes.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: The ring of complex polynomials of degree below r with y^r = −1, where multiplying by y^a only permutes coefficients and flips some signs, so powers of y act as exact roots of unity.
- `signed-packing`: Signed packing (Kronecker substitution): A product of two disk-grid polynomials is computed exactly by evaluating their integer parts at a large base 2^{4p}, multiplying the resulting integers with the O(N log N) multiplier, and reading centered coefficients back out, then wrapping modulo y^r + 1.
- `coefficient-twist`: Phase twist from cyclic to negacyclic: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} maps the cyclic coordinate C[x]/(x^r − 1) isomorphically onto the polynomial ring modulo y^r + 1, so cyclic convolution is computed over the ring and untwisted.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the negacyclic ring in which the roots of unity are powers of y, ω_t = y^{2r/t}, so every twiddle multiplication is a signed shift of a coefficient list (Nussbaumer–Quandalle).
- `butterfly-recursion`: Decimation-in-frequency butterflies and bit-reversed frequency order: The transform is computed by log t rounds each pairing entries z_k and z_{k+t/2}, applying the two-point butterfly and a twiddle shift, which leaves frequency j stored at its bit-reversed position; the opposite transform consumes that order.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: A cyclic convolution of length S = s_1⋯s_d with pairwise coprime s_i becomes a convolution on the product of cyclic axes of lengths s_i via x ↦ ∏ x_i^{μ_i}, implemented by triangular controlled shifts and axis moves.
- `bluestein-chirp`: Bluestein chirp identity: A Fourier transform (including its target frequency permutation) equals a pointwise chirp phase, a cyclic convolution with the chirp, and another pointwise chirp phase, so it reduces to cyclic convolution.
- `permutation-cancellation`: Cancellation of the retained source permutation: The coordinate permutation R left inside the resampled transform cancels across two forward transforms, their pointwise product and the opposite transform, giving R F⁺[(R F u)·(R F v)] = u*v/S².
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's method expressing a Fourier transform of coprime length s through one of a nearby power-of-two length t via Gaussian-weighted contractions A and B₀, with the two coordinate permutations left inside the identity.
- `tensor-resampling-box`: Tensor resampling on a padded box: The one-dimensional resampling maps are applied line by line along each axis of a zero-padded power-of-two box, with axes exposed by chunk interchanges, giving error below d p² and cost O(d T p^{3/2+δ} α).
- `prime-lengths`: Choosing prime source lengths: Distinct odd primes s_i in (1−2η)t_i < s_i ≤ (1−η)t_i are found by trial division, so their product S fills at least half the padded box while each ratio t_i/s_i leaves the separation resampling needs.
- `size-parameters`: Size parameters of the multiplication: From n set b = ⌈log₂ n⌉, precision p = 6b, number of axes d = ⌊b^ε⌋, chunk width K = ⌊d^c⌋, box size T ≈ n/b, axis lengths t_i ∈ {r/2, r} with r = 2^ℓ, so that Tp = Θ(n) and r exceeds every fixed power of p.
- `gate-network-frames`: Role networks and frames: A fixed linear network of wires (roles) and pointwise gates is run on arrays; assigning each vertex an invertible frame D_v makes the implemented operator D_out S D_in⁻¹, so only changes of frame along edges cost work.
- `scratch-restoration`: Restoring arbitrary scratch values: A linear computation that first subtracts the effect of unknown scratch contents, adds in the real contribution, and undoes it, so the target changes correctly and every scratch value is restored whatever it started as.
- `subset-intersection-network`: Three-subset gather and scatter network: A fixed network on banks indexed by triples of 3-subsets whose gather, scatter, copy and side-injection gates have net coefficient depending on intersection size, cancelled by scratch wires, so three stages realize the signed exchange (X, Y) ↦ (−Y, X).
- `nondegenerate-subspaces`: Nondegenerate subspaces and orthogonal residuals: Subspaces of a bilinear space on which the form is nondegenerate, so the space splits as a subspace plus its orthogonal complement; the orthogonal residual of nested subspaces is the complement of the smaller inside the larger.
- `subspace-labels`: Subspace labels and the rank budget: Each gate and terminal of the network gets a nested nondegenerate subspace of an m-dimensional space, so an edge costs its dimension change, and the only decreasing edges are central wires, keeping the total below the wire count times m.
- `rank-saving-recurrence`: Rank saving and the power-saving recurrence: If a network of W wires has total edge rank s < W m, a call at parameter m·f makes s calls on streams of volume V/W at parameter f, so per-volume cost obeys F_k ≤ (s/W) F_{k−1} + O(1) and grows only like e^τ with τ < 1.
- `lower-triangular-factorization`: Lower-triangular factorization of a matrix: Every rational matrix A of rank a factors as E₁ Π E₂ with E₁, E₂ invertible lower triangular and Π a partial permutation with exactly a ones (a Bruhat-type factorization in reversed coordinate order).
- `matrix-shear-cost`: Cost of a rational matrix shear: The address map (H,D) ↦ (H + A D, D) over Z/q^b is performed with exactly rank(A) interchanges of b-digit fields plus linear work, using triangular steps and the trick that three updates turn H+D into a swap.
- `bit-network-interface`: Bit network as an address shear: Using projection matrices of the labels as frames, the XOR network turns the role exchange into the shear H ← H + D on every role, with total rational edge rank s_b < W_b m.
- `power-width-interchange`: Power-width address interchange: Two chunks of m^k radix-q digits are interchanged by splitting rows into W role streams, running the bit network with each edge shear done by recursive interchanges of chunks of 1/m the width, in O(V e^τ) time on fixed tapes.
- `chunk-interchange`: Fast interchange of address chunks: Two disjoint address chunks of u bits in an array with complete Cartesian address set can be exchanged in O(V u^τ) time for a fixed τ < 1, although the intermediate steps form XOR combinations of the data.
- `two-point-butterfly`: Two-point butterfly H₀ and the kernel C: The butterfly H₀(u,v) = ((u+v)/2, (u−v)/2) and its Gaussian dyadic relative C = H S H = aI + bX with a=(1+i)/2, b=(1−i)/2, C² = X and H₀ = b S C S, which lets H₀ layers be computed from C layers.
- `phase-interface`: Binary phase frames: For the complex network with binary labels, the frame C_U = H^{⊗m} diag(i^{wt(P_U x) mod 4}) H^{⊗m} makes each edge change a product of one two-point kernel aI + bX_v per residual basis vector, and the whole network equals C^{⊗m} on every role.
- `packed-selected-bit-addition`: Packed selected-bit addition: An XOR of the same bit position in f chunks of one address range into another is done together by a constant number of cyclic shifts of whole chunk ranges, followed by a deterministic repair of the small explicitly identified set of exceptional addresses.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: One H₀ butterfly applied at the same bit offset in D ≤ d address chunks at once, computed exactly via the phase network with recursive calls on 1/m of the axes and a single final truncation, in O(V d^{λ'}) time with λ' < 1.
- `transform-layout`: Transform layout and cost: A positional permutation moves selected bits of the d−1 axes to a common offset in K-bit chunks so each transform round is one simultaneous layer, giving a forward and opposite synthetic transform costing O(T p [dK + p K^{τ−1} + ℓ d^{λ'}]).
- `ring-convolution`: Convolution from the retained transform layout: Normalized convolution over the negacyclic ring is computed by two forward synthetic transforms, pointwise polynomial products in the retained frequency order, and the opposite transform, with explicit error bound.
- `source-transform`: Source Fourier transform procedure: The computed transform for a coprime-length source: linewise Gaussian map A, the chirp transform done by complex convolution through the phase twist, linewise map B₀, and an exact 2^γ rescale, approximating R F_s.
- `multiplication-algorithm`: The multiplication algorithm: Split the operands into radix digits, map them by Φ to prime axes, apply the source transform to each, multiply pointwise, apply the opposite transform, rescale by S and 2^{2b+4}, round to integers, undo Φ and propagate carries.
- `exact-recovery`: Precision and exact recovery: Disk-margin and error bookkeeping shows the recovered coefficient error stays below 1/2, so rounding gives the exact integer convolution coefficients and carries give the exact binary product.
- `time-accounting`: Cost table and the saving exponent κ: Dividing each cost by V = Tp, seven dominant terms have powers of p at most 1 − 2κ below one; the smallest margin 2^{-181} fixes κ = 2^{-182}, and any polylog factor is absorbed.
- `main-theorem`: Integer multiplication below n log n: A single deterministic fixed-tape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^{1−κ}) time with κ = 2^{-182}, using fast address interchange and fast simultaneous butterfly layers inside a Gaussian-resampling, chirp and synthetic-transform reduction.

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
