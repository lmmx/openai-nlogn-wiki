# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/A1` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on growth rate.
- `polynomials`: Polynomials (known to the reader): Sums of powers of a variable with coefficients.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with i²=-1, including roots of unity.
- `multitape-turing-machine`: Multitape Turing machine (known to the reader): A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes; running time counts steps.
- `convolution`: Convolution and cyclic convolution: Combining two coefficient lists so entry k sums products of entries whose indices add to k (cyclically modulo the length in the cyclic case); this is polynomial multiplication.
- `dft`: Fourier transform and roots of unity: The discrete Fourier transform evaluates a coefficient list at powers of a root of unity, turning convolution into pointwise product; fast algorithms compute it in layers of two-point butterflies.
- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage and Strassen's 1971 O(n log n log log n) multitape multiplication and their proposal that n log n is optimal; Harvey and van der Hoeven later reached O(n log n).
- `radix-digit-convolution`: Multiplication as radix-digit convolution: Split each integer into short radix digits so the product becomes a convolution of integer coefficient lists; carries then give the exact product.
- `tape-arrays-and-streams`: Arrays on tapes, scans and stored bit volume: Data is stored as arrays addressed by fields of bits in a fixed order on tapes; elementary scans and stream operations cost time linear in the stored bit volume.
- `ring-mod-yr`: Polynomial ring modulo y^r + 1: Complex polynomials in y of degree below r multiplied with y^r replaced by -1; powers of y act as roots of unity, so multiplying by one is a signed cyclic shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the ring modulo y^r+1 that use powers of y as roots of unity, so each transform consists of address rearrangements, signed shifts and butterflies (Nussbaumer; Quandalle and Nussbaumer).
- `controlled-shifts`: Controlled shifts and carries by packing: Elementary tape procedures that shift records by amounts given by control values, used to implement signed shifts and address maps.
- `signed-packing`: Signed coefficient packing (Kronecker substitution) and the n log n subroutine: Polynomial products over the ring are computed by packing signed coefficients into long integers and calling the established O(n log n) multiplier as an ordinary subroutine.
- `chinese-remainder-address-map`: Chinese-remainder map onto prime cyclic axes: A map placing the radix-digit coefficient list on a product of distinct prime cyclic axes that preserves convolution, implemented by triangular controlled shifts and axis moves.
- `gaussian-resampling`: Gaussian resampling: Harvey and van der Hoeven's identity expressing each Fourier transform of prime length through a multidimensional transform with power-of-two axis lengths; source and target permutations stay inside the identity instead of being executed as sorts.
- `bluestein-chirp`: Bluestein chirp conversion: Bluestein's chirp identity rewrites a Fourier transform as a convolution with chirp factors, so the middle transform with its target permutation becomes a normalized cyclic convolution.
- `phase-twist`: Last-coordinate phase twist: A phase twist changes the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap gives the original cyclic wrap once the twist is removed.
- `linear-networks-frames`: Linear networks with roles and frames: A fixed linear network of scalar gates exchanging banks of values and restoring auxiliary values is applied to row streams, one role per wire; a frame is an invertible operator giving the stored representation, and intermediate frames cancel leaving an endpoint operator.
- `restoring-auxiliary-values`: Restoring auxiliary values: Scratch registers with arbitrary initial contents are subtracted, used, added back and the computation reversed, so every auxiliary value is restored (transparent computation).
- `finite-subset-network`: Finite network from three-element subsets: A fixed small network built from three-element subsets of an m-dimensional ground set, with gather, scatter and auxiliary wires cancelling unwanted coefficients, assigning nested subspaces to gates so the number s of smaller calls satisfies s<Wm.
- `recursive-power-saving`: Recursive power saving: A recursive call at parameter mf uses s<Wm calls at parameter f on streams of volume V/W, so dividing by volume the cost grows by factor s/W<m per multiplication of the parameter by m, giving a power rather than a logarithmic saving.
- `address-shear`: Address shear and lower triangular factorization: The endpoint operator of the bit network updates two address fields by (H,D)↦(H+D,D); rank reduction via a Bruhat-type factorization into lower-triangular matrices makes such shears cheap on tape.
- `address-interchange`: Fast address-field interchange: Interchanging two disjoint contiguous address fields of u bits in a Cartesian-product array at cost O(V u^τ) for a fixed τ<1, via intermediate XOR combinations whose final effect is an exact permutation.
- `butterfly-layer`: Simultaneous butterfly layer: The map H₀(u,v)=((u+v)/2,(u−v)/2) applied coefficientwise to polynomial records at one chosen bit position in each of d address chunks at cost O(V d^λ′), using exact Gaussian dyadic intermediates and one truncation afterward.
- `transform-layout-convolution`: Synthetic transform layout and convolution: Forward synthetic transforms keep the same frequency order through the pointwise product and the opposite transform consumes it, so convolution over the ring is computed on the retained layout using fast butterfly layers and address interchanges.
- `precision-exact-recovery`: Precision, rounding and carry propagation: After removing known normalizations and digit scales, the recovered coefficient error is shown strictly below 1/2, so rounding gives exact integer coefficients and carries yield the binary product.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time with κ=2^−182, by chaining digit convolution, Chinese-remainder map, Gaussian resampling, chirps, twist, and synthetic transforms accelerated by fast interchanges and butterfly layers.

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
