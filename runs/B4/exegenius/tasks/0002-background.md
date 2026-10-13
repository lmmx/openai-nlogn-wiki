# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/B4` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bounds on running time.
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, and their products.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi, with modulus and roots of unity e^{2πi/k}.
- `turing-machine`: Turing machines and tapes (known to the reader): Machines with a finite alphabet, finite states and tapes read and written by heads.
- `multitape-model`: Fixed multitape Turing machine model: The bit-complexity model: one deterministic machine with a fixed finite alphabet and a fixed number of one-dimensional tapes, where moving data costs time.
- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen's O(n log n log log n) multiplication and their conjecture that n log n is optimal, followed by Fürer and Harvey–van der Hoeven reaching O(n log n).
- `dft-convolution`: Discrete Fourier transform and convolution: The DFT evaluates a sequence at roots of unity; pointwise multiplication of transforms corresponds to convolution of sequences, which is how products are computed.
- `radix-digit-reduction`: Multiplication as convolution of radix digits: Splitting each n-bit operand into short radix-2^b digits makes the integer product a convolution of digit lists, followed by carry propagation.
- `hvdh-multiplier`: Established O(n log n) multiplier (subroutine): The Harvey–van der Hoeven O(n log n) integer multiplier, used here only as an ordinary subroutine for short products.
- `cyclic-crt`: Chinese-remainder map to prime cyclic axes: Placing the digit list on a product of cyclic axes of distinct prime lengths by a Chinese-remainder address map that preserves convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's reduction of a Fourier transform of coprime length to a transform with power-of-two axis lengths, using Gaussian-weighted resampling maps that are contractions.
- `resampling-keep-permutations`: Resampling with permutations left in the transform: Keeping the source and target coordinate permutations inside the transform identity so they cancel across the forward and inverse transforms instead of being executed as sorts.
- `bluestein`: Bluestein's chirp identity: Rewriting a DFT as a convolution with a chirp (quadratic phase) sequence.
- `polynomial-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree below r with y^r = -1; multiplying by a power of y is a signed cyclic shift of the coefficient list.
- `coefficient-twist`: Coefficient twist from cyclic to negacyclic: Multiplying coefficient k by ζ^k with ζ = e^{πi/r} turns cyclic convolution of length r into multiplication modulo y^r+1, with the wrap sign cancelling.
- `synthetic-transform`: Synthetic polynomial transform: A Nussbaumer-style Fourier transform over the polynomial ring whose roots of unity are powers of y, so multiplications are signed shifts; computed by radix-two butterflies.
- `butterfly-h0`: Two-point butterfly H₀: The map (u,v) ↦ ((u+v)/2,(u−v)/2) applied coefficientwise; layers of these make up a radix-two transform.
- `signed-packing`: Signed packing (Kronecker substitution): Multiplying ring polynomials exactly by packing their integer coefficients, including negative ones, into long integers and calling the integer multiplier.
- `ring-convolution`: Exact normalized convolution over the polynomial ring: Convolution on the remaining axes via forward synthetic transforms, pointwise ring products by signed packing, and the opposite transform consuming the same frequency order.
- `stream-operations`: Tape streams, array order and elementary scans: Arrays stored in row-major address order on tapes, with linear-time scans, controlled shifts and affine updates of later fields from earlier ones.
- `linear-network-frames`: Linear network with roles and frames: A fixed linear network exchanging two banks of values with signs and restoring auxiliary wires; applied to arrays by giving each wire an invertible frame operator so that intermediate frames cancel and only an endpoint operator remains.
- `subset-intersection-labels`: Subset-intersection subspace labels: Nested subspaces spanned by tensor products of three-element-subset indicator vectors (Frankl–Wilson/Alon style), giving a network whose total edge rank s is less than W·m.
- `recursive-saving`: Recursive power saving from rank deficit: A call at parameter m·f uses s < W·m calls at parameter f on volume V/W, so normalized cost grows by factor s/W < m per level, giving cost V·(parameter)^{τ} with τ < 1.
- `lower-triangular-factorization`: Lower triangular (Bruhat-type) factorization and matrix shear: Every rational matrix of rank a factors as E₁ΠE₂ with E_i lower triangular and Π a partial permutation with a ones, so a shear costs only a smaller interchanges plus linear-time updates.
- `fast-address-interchange`: Fast interchange of address chunks: Interchanging two contiguous address fields of u bits in a Cartesian-product array, by XOR/shear combinations through the bit network, at cost O(V u^τ) for fixed τ < 1.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H₀ at the same bit position of up to d address chunks at once on records of complex fixed-point polynomials, using the complex phase network, at cost O(V d^λ′).
- `fixed-point-precision`: Fixed-point dyadic precision and exact recovery: Coefficients stored as p-bit grid values on the unit disk, with truncation errors tracked through contractions so the final integer coefficient error is below 1/2.
- `parameter-choice`: Fixed rational parameter choice: The conservative constants (τ, λ, λ′, ε, δ, κ = 2^{-182}) chosen compatibly so all terms in the cost table fit the main bound.
- `multiplication-algorithm`: Complete multiplication algorithm and cost: Digits → CRT address map → forward synthetic Gaussian-resampled transforms of both operands → pointwise product → inverse transform → rescale, round and carry to get the exact product.
- `main-theorem`: Multiplication in O(n (lg n)^{1-κ}) time: The deterministic multitape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}) time with κ = 2^{-182}, disproving the n log n optimality conjecture in this model.

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
