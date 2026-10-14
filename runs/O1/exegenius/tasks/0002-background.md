# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/O1` (paths below are relative to it)

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

- `big-o-notation`: Big-O notation (known to the reader): Asymptotic upper bounds on running time up to constant factors.
- `polynomials`: Polynomials (known to the reader): Polynomials, their coefficients, products and remainders.
- `complex-numbers`: Complex numbers (known to the reader): Complex arithmetic, modulus, conjugation and roots of unity.
- `multitape-turing-machine`: Multitape Turing machine (known to the reader): A finite-control machine with a fixed finite alphabet and a fixed number of one-dimensional tapes, each head moving at most one cell per step.
- `linear-algebra`: Linear maps, matrices and rank: Vector spaces over a field (including the two-element field F₂ where addition is XOR), linear maps, matrices, subspaces, dimension and rank.
- `tensor-product`: Tensor product: The tensor product of vector spaces or linear maps, whose dimension is the product of the factors' dimensions; tensor powers act factorwise on multi-index arrays.
- `bilinear-form`: Nondegenerate bilinear forms and orthogonal complements: A symmetric bilinear form pairs vectors; a subspace is nondegenerate when the form restricted to it has no kernel, and then the space splits as the subspace plus its orthogonal complement.
- `nlogn-conjecture`: n log n optimality conjecture: Schönhage and Strassen's conjecture that n log n is the optimal order of growth for multiplying n-bit integers, here in the multitape Turing machine model.
- `hvdh-multiplier`: Harvey–van der Hoeven multiplier: The established deterministic O(n log n) multitape integer multiplier, used here only as an ordinary subroutine on short records.
- `array-layout`: Lexicographic array layout and logical volume: Arrays on a product of address fields are stored on tape in lexicographic order with addresses implicit, and their cost is measured against the logical volume V, the number of stored data bits.
- `elementary-stream-ops`: Elementary stream operations: Linear-time tape primitives: permuting or moving single digits, splitting on a digit and merging, and splitting rows cyclically into a fixed number of streams.
- `controlled-shifts`: Controlled shifts: Linear-time updates that add to a target address field an offset computed from earlier control fields (or multiply it by a fixed unit), implemented by splitting and remerging each fiber.
- `scratch-restoration`: Scratch restoration: The transparent-computation trick of subtracting a scratch register's effect, computing, adding, and uncomputing, so that the net result is independent of arbitrary initial scratch values.
- `triple-intersection`: Three-element-subset intersection construction: The Frankl–Wilson-style use of 3-subsets of a 100-element set, where gather and scatter produce coefficients depending on intersection size and side wires cancel the unwanted ones, giving y ← y + x.
- `bank-exchange-network`: Bank-exchange linear network: A fixed linear network of pointwise gates on wires (roles) that, in three stages, exchanges two banks of values with prescribed signs while restoring every auxiliary scratch wire.
- `role-streams`: Row splitting into role streams: Rows of an array are distributed cyclically among the network's W roles so each role stream has volume V/W, and recursive calls are scheduled depth-first on a fixed set of tapes by parking inactive streams on a stack.
- `frames`: Frames and the common-frame identity: Each network vertex gets an invertible linear operator (frame) giving the stored array's representation; since a common frame commutes with pointwise gates, the network implements the endpoint frame ratio on every role.
- `subspace-labels`: Subspace labels and orthogonal residuals: Nested nondegenerate subspaces of a fixed m-dimensional tensor space are attached to the network's vertices, and the dimension of each edge's orthogonal residual counts the smaller operations that edge needs.
- `rank-deficit`: Rank deficit and recursive power saving: The total number s of smaller calls satisfies s < Wm, so a recursion with parameter growth m and volume split W gives a cost factor e^τ with τ < 1 instead of e.
- `lower-triangular-factorization`: Lower triangular factorization: Every rational matrix of rank a factors as E₁ΠE₂ with invertible lower triangular E₁, E₂ and a partial permutation Π with a ones (a reversed Bruhat factorization).
- `address-shear`: Rational address shear: The address permutation (H,D) ↦ (H+AD, D) on two groups of fields, performed with exactly rank(A) smaller field interchanges plus linear work.
- `chunk-interchange`: Fast address-chunk interchange: A tape procedure that interchanges two disjoint u-bit address fields of an array in O(V u^τ) time for a fixed τ < 1, by running the bit network with shear frames and recursing on smaller interchanges.
- `dft`: Normalized discrete Fourier transform: The length-q transform averaging inputs times powers of e^{∓2πi/q}, normalized by 1/q so it is a contraction.
- `cyclic-convolution`: Cyclic convolution: Multiplication modulo x^S − 1 on coefficient arrays, which the Fourier transform turns into pointwise multiplication.
- `multidim-dft`: Multidimensional Fourier transform: The tensor product of one-dimensional transforms over several axes, applied to arrays indexed by a product of cyclic groups.
- `radix-digit-reduction`: Radix-digit reduction to convolution: Splitting each n-bit input into b-bit digits turns integer multiplication into convolution of short nonnegative integer coefficient lists, followed by carry propagation.
- `disk-grid`: Disk-grid fixed-point arithmetic: Complex values in the unit disk with real and imaginary parts on the grid 2^{-p}ℤ, computed exactly as Gaussian dyadics and truncated toward zero by Q_p.
- `contraction-error`: Error accounting through contractions: Since every exact map used is a contraction, errors of approximate subroutines add when composed, which bounds the final numerical error.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing a Fourier transform of prime length s through one of nearby power-of-two length t, via Gaussian-weighted contractions.
- `resampling-retained-permutations`: Resampling with retained permutations: A variant of Gaussian resampling that keeps the source and target coordinate permutations inside the transform identity instead of executing them as sorts.
- `prime-lengths`: Prime source lengths: Distinct odd primes s_i chosen just below the power-of-two axis lengths t_i, so their product fills a fixed fraction of the padded box while leaving the separation resampling needs.
- `crt-address-map`: Chinese-remainder address map: An algebra isomorphism from one cyclic convolution of length S = ∏ s_i to a multidimensional cyclic convolution on pairwise coprime axes, implemented by triangular controlled shifts and axis moves.
- `chirp-identity`: Bluestein chirp identity: Multiplying by quadratic phases (chirps) before and after a cyclic convolution computes a Fourier transform, here including its target permutation.
- `permutation-cancellation`: Source-permutation cancellation: The source permutation retained in both forward transforms cancels against the opposite-sign transform when computing a convolution.
- `polynomial-ring`: Polynomial ring modulo y^r + 1: Complex polynomials reduced modulo y^r + 1 with r a power of two, where multiplication by a power of y is a signed cyclic shift of coefficients.
- `coefficient-twist`: Coefficient phase twist: Multiplying coefficient k by e^{πik/r} turns cyclic convolution in the last axis into negacyclic multiplication modulo y^r + 1.
- `butterfly`: Normalized butterfly: The two-point map H₀(u,v) = ((u+v)/2, (u−v)/2), the basic step of radix-two decimation-in-frequency transforms.
- `synthetic-transform`: Synthetic polynomial transform: Nussbaumer's Fourier transform over the polynomial ring, where powers of y serve as roots of unity so twiddles are signed shifts and the transform is butterflies plus monomial multiplications.
- `phase-frames`: Binary phase frames: Frames for the complex network built from the kernel C = H·diag(1,i)·H and quadratic-form phases over F₂, so each edge change is one two-point kernel per orthonormal residual basis vector.
- `packed-selected-bit`: Packed selected-bit addition: XORing corresponding selected bits of two address chunks using eight cyclic shifts of whole chunks with guard values, then deterministically repairing the small set of exceptional addresses by sorting.
- `simultaneous-layer`: Simultaneous butterfly layer: Applying the butterfly H₀ on one selected bit in each of up to d address chunks at once in O(V d^λ′) time, λ′ < 1, by running the complex network with phase frames recursively and truncating once at the end.
- `synthetic-layout`: Synthetic transform layout and cost: The tape layout that places the selected bits of all axes at common offsets in consecutive chunks, so each synthetic transform round is one simultaneous layer, with frequencies left in a retained bit-reversed order.
- `signed-packing`: Signed Kronecker packing: Multiplying polynomials with signed coefficients by evaluating them at a large power of two, multiplying the resulting integers, and extracting centered coefficients.
- `ring-convolution`: Normalized convolution over the polynomial ring: Computing normalized cyclic convolution of arrays of ring elements by two forward synthetic transforms, pointwise packed products in the retained order, and the opposite transform.
- `exact-recovery`: Exact recovery by rounding and carries: Once the approximate coefficient error is below 1/2, rounding gives the exact integer coefficients, and radix carry propagation gives the binary product.
- `parameter-choice`: Parameter choice and cost table: Fixed rational exponents (τ, λ′, ε, c, δ, …) and size parameters chosen so every row of the normalized cost table is at most p^{1−2κ}.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: One deterministic fixed-alphabet multitape Turing machine multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^(−182), refuting the n log n optimality conjecture in that model.

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
