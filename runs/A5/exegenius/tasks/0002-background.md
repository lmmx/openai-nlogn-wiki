# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/A5` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on growth of a running time.
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi, with roots of unity as the unit-modulus examples.
- `multitape-tm`: Multitape Turing machine (known to the reader): A finite-state machine with finite alphabet and several one-dimensional tapes, each head moving at most one cell per step.
- `nlogn-conjecture`: Multiplication history and the n log n conjecture: Schönhage–Strassen multiplied n-bit integers in O(n log n log log n) and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).
- `convolution`: Convolution and multiplication: Multiplying integers by splitting into radix digits reduces to convolving short integer coefficient lists, i.e. multiplying polynomials.
- `dft`: Discrete Fourier transform: Evaluating a coefficient list at powers of a primitive root of unity; it turns cyclic convolution into pointwise products.
- `butterfly-fft`: FFT and two-point butterflies: Fast Fourier transform levels built from address rearrangements, root multiplications and two-point butterfly operations; each of Θ(log n) levels scanning Θ(n) bits costs Θ(n log n).
- `poly-ring-mod`: Polynomial ring modulo y^r + 1: Polynomials in y with complex coefficients reduced using y^r = -1; powers of y are roots of unity and multiplying by one is a signed cyclic shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms over the polynomial ring where roots of unity are powers of y, so root multiplication is a signed shift.
- `signed-packing`: Signed packing (Kronecker substitution): Exact polynomial products are computed by packing signed coefficients into one long integer and calling the established O(n log n) multiplier as an ordinary subroutine.
- `multidim-crt`: Prime cyclic axes and the Chinese remainder map: The coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map preserving convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven technique expressing a Fourier transform through a multidimensional transform whose axis lengths are powers of two.
- `bluestein-chirp`: Bluestein chirp identity: Converts a transform of arbitrary length into a cyclic convolution via multiplication by chirp phases.
- `phase-twist`: Last-coordinate phase twist: A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap yields the original cyclic wrap after untwisting.
- `fixed-point-precision`: Fixed-point precision and exact recovery: Records hold complex fixed-point coefficients; Gaussian dyadics are exact, one truncation follows a contractive layer, and the final error is below 1/2 so rounding and carries give the exact product.
- `tape-streams`: Tape arrays, scans and elementary streams: Arrays stored in address order on tapes with scans, controlled shifts and fixed rational scalings costing linear time.
- `address-interchange`: Fast interchange of address fields: Swapping two disjoint contiguous address fields of u bits in a Cartesian-product array in O(V u^τ) time, τ<1, using intermediate XOR combinations that end in an exact permutation.
- `matrix-shear`: Address shear and triangular factorization: The endpoint operator (H,D)->(H+D,D) on address fields, with rank reduction via lower-triangular (Bruhat) factorization.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: Applying H0(u,v)=((u+v)/2,(u−v)/2) coefficientwise on the same selected bit of up to d address chunks, in O(V d^λ') time with λ'<1.
- `linear-network-frames`: Linear networks, roles and frames: A fixed linear network exchanges banks of values with signs and restores auxiliary values; rows are spread over roles and each vertex stores D_v g in an invertible linear frame so intermediate frames cancel.
- `finite-subset-networks`: Finite networks from three-element subsets: Fixed networks with nested subspaces of an m-dimensional space built from three-element subset intersections, giving s<Wm smaller calls.
- `recursive-saving`: Recursive power saving: Calling a parameter-mf operation as s calls at parameter f on volume V/W raises normalized cost by s/W<m per multiplication of the parameter by m, yielding a power saving.
- `retained-permutations`: Resampling with permutations retained in the transform: Source and target coordinate permutations stay in the transform identity and cancel across forward, pointwise, and inverse transforms instead of being executed as sorts.
- `target`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic fixed-tape machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time, κ=2^−182, disproving the n log n conjecture in this model; chain: digit convolution, prime axes, resampling and chirps, polynomial ring transforms with fast tape procedures, then rounding and carries.

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
