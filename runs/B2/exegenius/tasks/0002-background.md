# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/B2` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on growth.
- `polynomials`: Polynomials (known to the reader): Sums of powers of a variable with coefficients.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi, including roots of unity.
- `turing-machine-tapes`: Multitape Turing machine (known to the reader): Machine with a finite alphabet and several one-dimensional tapes.
- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture: The conjecture that n log n is the optimal order of cost for multiplying n-bit integers on a multitape Turing machine; refuting it needs one machine with liminf T(n)/(n lg n)=0.
- `convolution-dft`: Convolution and discrete Fourier transform: Integer multiplication reduces to convolution of digit lists, which Fourier transforms compute through pointwise products; normalized transforms are contractions.
- `nlogn-multiplier`: Harvey–van der Hoeven O(n log n) multiplication: The established unconditional O(n log n) multiplier, used only as an ordinary subroutine for polynomial products.
- `ring-mod-yr1`: Polynomial ring modulo y^r + 1: Polynomials in y reduced by y^r = -1, so powers of y are roots of unity and multiplying by one is a signed shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring using powers of y as roots, built from address rearrangements, signed shifts and two-point butterflies.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven reduction expressing a Fourier transform through a multidimensional transform with power-of-two axis lengths.
- `crt-address-map`: Chinese-remainder address map: Places the digit list on a product of distinct prime cyclic axes, preserving convolution.
- `bluestein-chirp`: Bluestein chirp conversion: Converts the middle transform, with its target permutation, into a normalized cyclic convolution.
- `phase-twist`: Last-coordinate phase twist: A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap gives the original cyclic wrap once the twist is removed.
- `signed-packing`: Signed coefficient packing: A form of Kronecker substitution that packs polynomial coefficients into integers so polynomial products use the integer multiplier.
- `tape-scans`: Array order and tape scans: Arrays stored in address order on tapes; scanning Θ(n) bits at each of Θ(log n) levels already costs Θ(n log n), so movement must be saved.
- `stream-operations`: Elementary stream operations and controlled shifts: Linear-time tape scans: digit swaps, moving digits, splitting rows into W role streams, and controlled shifts of a field.
- `linear-network-frames`: Linear networks with roles and frames: A fixed linear network exchanging two banks of values with signs, restoring all auxiliary values; roles are wire places and frames are invertible operators changing stored representation so only an endpoint operator remains.
- `finite-subspace-network`: Finite networks with a rank saving: Network construction using three-element subsets and nested subspaces, so that the sum s of edge ranks satisfies s<Wm.
- `address-shear`: Address shear and triangular factorization: Endpoint operator (H,D)→(H+D,D) on address fields, implemented via lower-triangular factorization and linear-cost controlled shifts.
- `address-interchange`: Fast address-field interchange: Interchanges two disjoint address fields of u bits in V stored bits at cost O(V u^τ), τ<1, via XOR combinations ending in an exact permutation.
- `fixed-point-dyadics`: Exact Gaussian dyadics and precision: Values are exact Gaussian dyadics with power-of-two denominators; truncation after contractive layers adds bounded error, tracked so the final error is below 1/2.
- `butterfly-layer`: Fast simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u-v)/2) simultaneously on selected bits of several address chunks at cost O(V d^λ'), λ'<1, using phase frames and dyadic scaling.
- `recursive-power-saving`: Recursive power saving: A call at parameter mf uses s calls at parameter f on volume V/W; since s/W<m, the normalized cost grows by less than m per scaling, giving a power saving.
- `tensor-resampling-chirps`: Tensor resampling with retained permutations: Multidimensional resampling identity RF_s = 2^γ B0 Q F_t A keeping the coordinate permutations, which cancel through chirp convolution and pointwise products.
- `exact-recovery`: Rounding and carry propagation: After removing normalizations, the recovered coefficient error is below 1/2, so rounding and carries give the exact binary product.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1-κ)), κ=2^-182, refuting the n log n conjecture; it chains digit convolution, CRT axes, resampling, chirps, phase twist and synthetic transforms, accelerated by fast address interchange and butterfly layers.

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
