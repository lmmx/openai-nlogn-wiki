# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/C4` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound notation.
- `polynomials`: Polynomials (known to the reader): Polynomials and arithmetic on them.
- `complex-numbers`: Complex numbers (known to the reader): Complex arithmetic, modulus, roots of unity.
- `turing-tapes`: Basic Turing machines and tapes (known to the reader): Turing machines with tapes and heads.
- `multitape-model`: Fixed multitape machine model and scans: A Turing machine with one fixed finite alphabet and a fixed number of one-dimensional tapes; moving data is paid for by scanning tapes, so a pass over n bits costs Θ(n).
- `conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen's 1971 O(n log n log log n) multiplication and their conjecture that n log n is optimal, with Harvey–van der Hoeven's O(n log n) the previous best.
- `dft-convolution`: Discrete Fourier transform and cyclic convolution: The length-q DFT (normalized by 1/q) turns cyclic convolution into pointwise multiplication; inverse transform has opposite sign in the exponent.
- `radix-digit-convolution`: Multiplication as convolution of radix digits: Writing both integers in a radix turns their product into a convolution of short integer coefficient lists, followed by carry propagation.
- `kronecker-packing`: Signed Kronecker packing: Packing polynomial coefficients (including negative ones) into one large integer so that a polynomial product becomes an integer product.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier as subroutine: The established O(N log N) fixed-tape integer multiplier, used as an ordinary subroutine for short polynomial records.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: A Chinese-remainder address map placing the coefficient list on a product of distinct prime cyclic axes, preserving convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven's method expressing a Fourier transform of coprime length through a power-of-two tensor transform, via Gaussian-weighted interpolation.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a DFT of arbitrary length as a cyclic convolution sandwiched between pointwise phase (chirp) multiplications.
- `ring-y-r`: Polynomial ring modulo y^r + 1: The ring of polynomials over ℂ modulo y^r+1, where powers of y are roots of unity and multiplication by y^a is a signed cyclic shift of coefficients; norm is the max coefficient modulus.
- `synthetic-transform`: Synthetic polynomial transforms: Nussbaumer–Quandalle transforms over the ring with roots of unity ω_t = y^{2r/t} acting as signed shifts, computed by radix-two butterflies; frequency order is retained through the pointwise product.
- `phase-twist`: Phase twist to the polynomial ring: A phase multiplication converting the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap yields the original cyclic wrap after untwisting.
- `retained-permutations`: Retained permutations cancelling in transforms: Keeping the source and target coordinate permutations of resampling inside the transform formula so that they cancel across the forward transforms, product and inverse instead of being sorted.
- `fixed-point-precision`: Fixed-point precision and exact recovery: Complex values are stored on a 2^{-p} grid with truncation errors; composing contractive approximations adds errors, and final coefficient error below 1/2 lets rounding and carries recover the exact integer product.
- `gaussian-dyadics`: Exact Gaussian dyadic arithmetic with single truncation: Intermediate values are kept exactly as complex numbers with power-of-two denominators, with one truncation after a completed contractive layer.
- `butterfly-h0`: Simultaneous butterfly layer H₀: The two-point butterfly H₀(u,v)=((u+v)/2,(u−v)/2) applied coefficientwise to selected coordinate bits of many address chunks at once.
- `linear-network-frames`: Linear exchange networks with frames and roles: A fixed linear network of gates on wires (roles) exchanging two banks of values and restoring auxiliary values; with invertible frames D_v per vertex, gates act pointwise and intermediate frames cancel, leaving an endpoint operator on each role array.
- `subset-intersection-network`: Three-element subset construction with rank saving: Subspaces of an m-dimensional space labelled by three-element subsets, using gather/scatter and auxiliary wires, make adjacent edge operators nested so the total number s of smaller calls is less than W·m.
- `recursive-power-saving`: Recursive power saving from s < Wm: A recursive call at parameter mf uses s calls at parameter f on volume V/W each, so the per-volume cost multiplies by s/W < m, giving cost V·(parameter)^θ with θ<1.
- `lower-triangular-shear`: Address shear and lower triangular factorization: Bruhat-style factorization into lower triangular factors with reversed coordinate order; a shear (H,D)→(H+D,D) updates later fields from earlier ones in linear time on tape.
- `chunk-interchange`: Interchange of address chunks in time O(Vu^τ): Interchanging two disjoint contiguous u-bit address fields of an array by XOR combinations of intermediate data and the bit network, with exact final permutation for arbitrary auxiliary values.
- `phase-frames`: Phase frames for simultaneous butterflies: Diagonal phase frames express a tensor product of the auxiliary kernel C on many selected bits via smaller groups of bits separated by binary changes of basis implemented as whole-chunk moves.
- `fast-butterfly-layer`: Fast simultaneous butterfly layer in time O(Vd^λ′): Applying H₀ to the same bit in d address chunks of the polynomial array in cost O(V d^λ′) instead of d full passes.
- `transform-layout`: Synthetic transform layout and convolution: Layout on tape on which the parallel layers apply and the pointwise-multiplied transforms are inverted, with polynomial products by signed packing and the Harvey–van der Hoeven multiplier.
- `tensor-resampling`: Tensor resampling over growing dimension: Applying one-dimensional resampling maps line by line over many coordinates, with axis movement done by chunk interchange.
- `parameter-choice`: Compatible parameter choice and cost accounting: A fixed rational choice (τ, λ′, ε, κ=2^{-182}, ...) making all cost terms fit the final bound.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape machine multiplying n-bit integers exactly in O(n(lg n)^{1−κ}) with κ=2^{-182}, refuting the n log n optimality conjecture; built from radix convolution, CRT axes, Gaussian resampling, chirps, the polynomial ring and fast chunk and butterfly operations.

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
