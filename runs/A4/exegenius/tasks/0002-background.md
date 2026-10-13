# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/A4` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Polynomials and their arithmetic.
- `complex-numbers`: Complex numbers (known to the reader): Complex numbers, roots of unity, and their arithmetic.
- `turing-tapes`: Turing machines and tapes (known to the reader): Basic Turing machines with tapes, head scans and running time.
- `multitape-model`: Fixed multitape Turing machine model: Deterministic Turing machine with a fixed finite alphabet and fixed finite number of one-dimensional tapes; the model in which time is measured.
- `elementary-scans`: Array order and elementary tape scans: Storing arrays in address order on tapes and performing basic scans, copies and streams in linear time.
- `convolution-dft`: Convolution and Fourier transforms: Cyclic convolution of sequences, computed by transforming, multiplying pointwise and inverse-transforming using roots of unity.
- `radix-digit-reduction`: Multiplication as convolution of radix digits: Split each integer into digits in a radix, so the product becomes a convolution of short integer coefficient lists followed by carry propagation.
- `known-nlogn`: Established O(n log n) multiplication and history: Schönhage–Strassen O(n log n log log n), Fürer, and Harvey–van der Hoeven O(n log n) multiplication on multitape machines, with n log n conjectured optimal; the O(n log n) multiplier is used as a subroutine.
- `kronecker-packing`: Signed coefficient packing (Kronecker substitution): Encode a polynomial with bounded integer coefficients as one integer by evaluating at a power of two with signed digits, so a polynomial product becomes an integer product.
- `ring-mod-yr`: Polynomial ring modulo y^r + 1: Complex polynomials in y reduced modulo y^r+1, so y^r = −1; multiplying by a power of y is a signed cyclic shift of the coefficient list and powers of y act as roots of unity.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring where roots of unity are powers of y, so root multiplication is a signed shift (Nussbaumer, Quandalle).
- `butterfly-h0`: Two-point butterfly H₀: The map H0(u,v) = ((u+v)/2,(u−v)/2) applied coefficientwise; the basic arithmetic step of a transform layer.
- `multidim-transform`: Multidimensional transform with power-of-two axes: Fourier transform on an array indexed by several axes, computed one axis at a time by butterflies; axis lengths are powers of two.
- `crt-prime-axes`: Chinese-remainder map to distinct prime cyclic axes: Re-index the digit list over a product of cyclic axes of distinct prime lengths by the Chinese remainder theorem, preserving convolution; implemented by triangular controlled shifts and axis moves.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven technique expressing a Fourier transform over prime axes via a power-of-two tensor transform, with source and target permutations kept inside the identity.
- `bluestein-chirp`: Bluestein's chirp identity: Rewrites a DFT of arbitrary length as a cyclic convolution with a chirp sequence, here converting the middle transform and its permutation into normalized cyclic convolution.
- `phase-twist`: Last-coordinate phase twist: Multiply by roots-of-unity phases so a cyclic coordinate becomes a polynomial modulo y^r+1, whose negative wrap equals the original cyclic wrap after untwisting.
- `fixed-point-precision`: Fixed-point complex coefficients and exact recovery: Numerical records use complex fixed-point numbers (Gaussian dyadics); with total error below 1/2, rounding recovers exact integer coefficients and carries give the binary product.
- `linear-network-frames`: Linear networks, roles and frames: A fixed linear gate network exchanges banks of values with signs and restores auxiliary values; roles are wire positions applied pointwise to role streams, and frames D_v are invertible operators changing stored representation along edges so intermediate frames cancel.
- `subset-finite-network`: Finite networks from three-element subsets: Fixed networks with nested subspaces attached to gates built from 3-element subsets (Frankl–Wilson style intersection counts, index-code gather/scatter, cancelling auxiliary wires), using s < W m smaller calls.
- `recursive-saving`: Recursive power saving from s < Wm: A call at parameter mf makes s calls at parameter f on streams of volume V/W; since s/W < m the per-volume cost grows slower than the parameter, giving a power saving.
- `address-shear`: Address shear and restoration of scratch values: The endpoint operator (H,D)↦(H+D,D) on address fields over a residue ring, obtained via a Bruhat-type factorization; scratch registers are restored for arbitrary initial contents.
- `address-interchange`: Fast interchange of address chunks: Tape procedure swapping two disjoint address fields of u bits in an array of stored volume V at cost O(V u^τ), τ<1, via XOR combinations that net to an exact permutation.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Tape procedure applying H0 simultaneously on one selected bit in each of d address chunks of numerical arrays at cost O(V d^λ'), using phase frames and one truncation after the contractive layer.
- `synthetic-layout`: Synthetic transforms on tape layouts: Layout storing roots, butterflies and frequency order so that the two forward transforms keep the same frequency order through the pointwise product and the opposite transform consumes it.
- `ring-products`: Exact polynomial-ring products: Products in the ring modulo y^r+1 computed by signed packing and the established O(n log n) multiplier as subroutine, giving normalized convolution.
- `fast-multiplication`: Integer multiplication in O(n (lg n)^(1−κ)) time: Deterministic fixed-tape algorithm: digit convolution, CRT prime axes, Gaussian resampling, Bluestein chirps, phase twist, synthetic transforms with fast interchanges and butterfly layers, then rounding and carries; time O(n (lg n)^(1−κ)), κ=2^−182, disproving the n log n conjecture in this model.

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
