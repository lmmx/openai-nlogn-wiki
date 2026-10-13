# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/A2` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on running time as a function of input size.
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi, with modulus and roots of unity e^(2πi/k).
- `tm-basics`: Turing machines and tapes (known to the reader): A finite-state machine reading and writing cells on tapes, one cell step at a time.
- `binary-integers`: Binary integers (known to the reader): Representing nonnegative integers as bit strings, most significant bit first.
- `fixed-tape-model`: Fixed-tape Turing machine model: The model: one fixed finite alphabet and a fixed finite number of one-dimensional tapes, where time counts steps and moving data over growing distances costs scans.
- `convolution`: Convolution: Combining two coefficient lists so that entry k sums products a_i b_j over i+j=k (linearly, cyclically, or with negative wrap).
- `multiplication-via-convolution`: Multiplication as digit convolution: Split each integer into radix-2^b digits; the product's digit coefficients are the convolution of the digit lists, followed by carry propagation.
- `dft`: Discrete Fourier transform: Linear map F_q sending a length-q vector to its averaged sums with roots of unity e^(-2πi jk/q); it turns convolution into pointwise product and is a contraction.
- `fft-butterfly`: Fast transforms and butterflies: Computing a transform of power-of-two length in about log levels of two-point butterfly operations, each level scanning all data.
- `schonhage-strassen-conjecture`: Schönhage–Strassen optimality conjecture: The 1971 O(n log n log log n) multitape multiplication and the conjecture that n log n is the optimal order of multiplication cost.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier: The unconditional O(n log n) multitape multiplication algorithm, used here as an ordinary subroutine on short inputs.
- `poly-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree below r with y^r = -1, so multiplying by a power of y is a signed shift of the coefficient list.
- `synthetic-transform`: Synthetic polynomial transform: A Fourier transform over the ring modulo y^r+1 using powers of y as roots of unity, so all root multiplications are exact signed shifts.
- `crt-prime-axes`: Chinese-remainder map to prime axes: Re-indexing the coefficient list onto a product of distinct prime cyclic axes by the Chinese remainder theorem so cyclic convolution is preserved.
- `gaussian-resampling`: Gaussian resampling: Expressing a Fourier transform of prime-like length through a power-of-two multidimensional transform via Gaussian-weighted resampling, with permutations on source and target.
- `bluestein-chirp`: Bluestein chirp identity: Rewriting a DFT of arbitrary length as a convolution with a chirp e^(πi j^2/q) and pre/post multiplications.
- `phase-twist`: Last-coordinate phase twist: Multiplying by a diagonal phase so that a cyclic coordinate becomes a polynomial modulo y^r+1, whose negative wrap yields the cyclic wrap after the twist is removed.
- `fixed-point-contraction`: Fixed-point dyadic arithmetic and contractions: Gaussian dyadic values on a 2^-p grid, one truncation per layer, and norm-nonincreasing linear maps whose errors add when composed.
- `kronecker-packing`: Signed packing (Kronecker substitution): Packing polynomial coefficients, possibly negative, into one integer so a ring product becomes one integer product, recovered exactly afterward.
- `linear-network`: Linear network with roles and frames: A fixed linear network exchanging two banks of values while restoring auxiliary values; arrays on wires carry invertible frames that cancel along routes and leave an endpoint operator.
- `subset-network`: Three-subset intersection construction: Nested subspaces attached to gates using three-element subsets, with gather/scatter and auxiliary wires cancelling unwanted intersection coefficients, giving s<Wm smaller calls.
- `recursive-power-saving`: Recursive rank saving: Recursing at parameter mf with s calls on streams of volume V/W where s<Wm, so cost per volume grows by s/W<m per factor m, giving a power saving.
- `matrix-shear`: Triangular factorization of address shears: Bruhat-style factorization into lower triangular maps so a shear (H,D)→(H+D,D) of address fields is done by ordered scans.
- `address-interchange`: Fast interchange of address chunks: Swapping two disjoint address fields of u digits in time O(V u^τ), τ<1, via XOR-combined intermediate data restoring an exact permutation.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H0(u,v)=((u+v)/2,(u-v)/2) on one bit in each of up to d address chunks at once on polynomial records in cost O(V d^λ'), λ'<1.
- `transform-layout`: Retained transform layout: Storing synthetic transform output in a layout where the parallel layers apply and keeping the frequency order so the opposite transform consumes it after pointwise product.
- `ring-convolution`: Exact normalized ring convolution: Convolution over the polynomial ring on the remaining axes: two forward transforms, pointwise ring products via signed packing, and the opposite transform.
- `resampling-no-sort`: Resampling with permutations left in the transform: Keeping the source and target coordinate permutations inside the transform identity so no separate full sorts are run, and the source permutation cancels across transforms.
- `precision-recovery`: Precision and exact recovery: Bounding rounding error so recovered coefficients are within 1/2 of integers, then rounding and propagating carries.
- `parameter-choice`: Fixed rational parameter choice: Conservative fixed exponents (τ, λ, c, ε, etc.) compatible across procedures, yielding κ=2^-182.
- `multiplication-algorithm`: The multiplication algorithm: Digits to source arrays via address map, two forward transforms, pointwise product, opposite transform, rescale, round, carry.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) time: A deterministic fixed-tape machine multiplying n-bit integers in O(n (lg n)^(1-κ)) time, refuting the n log n optimality conjecture in this model.

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
