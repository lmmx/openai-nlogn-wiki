# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/C5` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi, including roots of unity.
- `turing-machine-basics`: Turing machines and tapes (known to the reader): Machines with finite control reading and writing cells on tapes.
- `multitape-model`: Fixed multitape Turing machine model: One fixed finite alphabet and a fixed finite number of one-dimensional tapes; each step reads/writes one cell per tape and moves each head at most one cell, so moving data costs time.
- `nlogn-conjecture`: The n log n conjecture and history: Schönhage and Strassen proposed n log n as optimal multiplication cost; Schönhage–Strassen, Fürer and Harvey–van der Hoeven reduced upper bounds down to O(n log n).
- `hh-multiplier`: Established O(n log n) multiplier: The Harvey–van der Hoeven O(n log n) multiplication algorithm, used here only as an ordinary subroutine for small products.
- `dft-roots-of-unity`: Discrete Fourier transform and roots of unity: Evaluating a polynomial at all powers of a root of unity; the fast version is the FFT, built from layers of two-point butterflies.
- `cyclic-convolution`: Convolution and the convolution theorem: Multiplying polynomials (mod x^N−1 for cyclic) by transforming, multiplying pointwise, and inverse transforming; integer multiplication reduces to it by splitting into radix digits.
- `multidimensional-transform`: Multidimensional transforms: A transform on an array with several axes, applied axis by axis; axis lengths such as primes or powers of two determine cost and layout.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: A Chinese-remainder address map placing a coefficient list onto a product of distinct prime cyclic axes while preserving convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven identity expressing each Fourier transform on prime-length axes through a power-of-two tensor transform, with contraction bounds on the error.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a transform as a cyclic convolution by multiplying by chirp phases.
- `ring-y-r-plus-1`: Polynomial ring modulo y^r + 1: The ring of polynomials with complex coefficients in y modulo y^r+1, r a power of two; powers of y act as roots of unity and multiplying by one is a signed shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms whose roots of unity are powers of y in the ring, so multiplications by roots are signed shifts, leaving only shifts, address rearrangements and butterflies.
- `phase-twist`: Phase twist to the negative-wrap ring: A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap gives the original cyclic wrap after untwisting.
- `signed-packing`: Signed packing (Kronecker substitution): Packing polynomial coefficients into a single integer with signs so ring products reduce to integer products done by the established multiplier.
- `fixed-point-precision`: Fixed-point complex coefficients and exact recovery: Numerical arrays hold complex fixed-point dyadic numbers; errors are bounded below 1/2 so rounding recovers exact integer coefficients.
- `address-fields-layout`: Array addresses, fields and tape layout: Arrays are stored on tape in row-major address order; address bit-fields (chunks) are contiguous and permuting them costs more than scanning.
- `linear-network`: Linear networks with restored auxiliary values: A fixed network of gates exchanging two banks of values with signs, with roles for each wire, whose auxiliary values are restored so the effect is exact for arbitrary initial auxiliary contents.
- `frames`: Frames of a linear network: Invertible linear operators attached to sources, gates and sinks changing how a logical array is stored; intermediate frames cancel leaving an endpoint operator.
- `subset-subspace-labels`: Subset-intersection subspace labels: Subspaces of a fixed m-dimensional space attached to gates using three-element subsets, nested along edges so dimension drops count smaller calls and the total s<Wm.
- `recursive-saving`: Recursive power saving from s<Wm: A call at parameter mf makes s<Wm calls at parameter f on volume V/W streams, so per-volume cost grows by a factor below m, giving a power saving.
- `address-shear`: Address shear and triangular factorization: The endpoint operator (H,D)↦(H+D,D) on address fields; a rank-reducing lower-triangular factorization lets two further linear updates complete an interchange.
- `fast-address-interchange`: Fast interchange of address fields: Swaps two disjoint contiguous u-bit address fields of an array of stored volume V in cost O(V u^τ), τ<1, using XOR combinations whose final effect is an exact permutation.
- `butterfly-layer`: Two-point butterfly H₀: The operation (u,v)↦((u+v)/2,(u−v)/2) applied coefficientwise.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Applies H₀ simultaneously on the same selected bit of at most d address chunks in cost O(V d^λ′), via the linear network with phase frames and a single final truncation.
- `fast-synthetic-transform`: Synthetic transforms with retained frequency order: Forward synthetic transforms keep the same frequency order through their pointwise product and the opposite transform consumes it, using fast butterfly layers and interchanges.
- `retained-permutations`: Resampling with permutations left in the transform: The source and target coordinate permutations stay inside the transform identity and cancel across forward, product and inverse transforms instead of being sorted separately.
- `multiplication-assembly`: Assembling the exact product: Chain: radix digits, CRT prime axes, Gaussian resampling and chirps, phase twist, ring convolution; then rescale, round and propagate carries; cost table summed.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1−κ}) time with κ=2^{-182}, disproving the n log n conjecture in this model.

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

Keep any other files you make, such as scripts, in `exegenius/tasks/0002-background`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them.
