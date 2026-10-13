# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/A6` (paths below are relative to it)

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
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with i²=-1.
- `turing-tapes`: Basic Turing machines and tapes (known to the reader): Machine with finite states reading and writing tapes.
- `multitape-model`: Fixed multitape Turing machine model: Deterministic Turing machine with fixed finite alphabet and fixed finite number of one-dimensional tapes; the cost model where time counts bit-level tape steps and scans of n stored bits cost Θ(n).
- `nlogn-conjecture-history`: Multiplication history and the n log n conjecture: Schönhage–Strassen gave O(n log n log log n) and conjectured n log n optimal; Fürer and others improved the factor; Harvey–van der Hoeven reached O(n log n).
- `convolution-reduction`: Multiplication as convolution of radix digits: Splitting both integers into short radix digits turns the integer product into a convolution of digit lists, followed by carry propagation.
- `fourier-transform-butterflies`: Fourier transforms and butterfly operations: A discrete Fourier transform evaluates a sequence at roots of unity, turning cyclic convolution into pointwise products; fast versions use layers of two-point butterflies.
- `poly-ring-mod`: Polynomial ring modulo y^r + 1: Complex polynomials in y reduced by y^r=-1, with r a power of two; multiplying by a power of y is a signed cyclic shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms using powers of y as roots of unity so twiddle multiplications are signed shifts, computed by address rearrangements, shifts and butterflies.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven reduction expressing a Fourier transform of arbitrary axis length through a transform with power-of-two axes, with source and target permutations kept in the identity.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Placing the digit list on a product of distinct prime cyclic axes by a Chinese-remainder address map that preserves convolution.
- `bluestein-chirp`: Bluestein chirp conversion: Bluestein's identity rewrites a transform (with its target permutation) as a normalized cyclic convolution via chirp factors.
- `phase-twist`: Phase twist to the polynomial ring: A twist on the last cyclic coordinate makes its wraparound negative, turning it into a polynomial modulo y^r+1 whose negative wrap restores the cyclic wrap after untwisting.
- `signed-packing`: Signed packing of polynomial products: Kronecker-style packing of signed coefficients into integers so ring products are computed with the established O(n log n) multiplier as an ordinary subroutine.
- `tape-streams`: Array order, streams and controlled shifts: Elementary tape operations: scanning arrays in address order, stream operations and controlled shifts/rational scalings that cost linear time.
- `linear-network-frames`: Linear networks with roles and frames: A fixed linear network exchanging two banks of values with signs and restoring auxiliaries; wires are roles, rows are distributed among W roles, and invertible frames D_v change array representation so intermediate frames cancel.
- `subset-intersection-network`: Finite networks from three-element subsets: Construction attaching nested subspaces of an m-dimensional space to gates, using three-element subset intersection counts, gather/scatter and auxiliary wires, so total smaller calls s < W m.
- `recursive-power-saving`: Recursive power saving: A call at parameter mf uses s calls at parameter f on volume V/W streams; since s/W<m, cost per volume grows like a power less than 1 of the parameter instead of linearly.
- `address-interchange`: Fast interchange of address chunks: Interchanges two disjoint contiguous address fields of u bits in a Cartesian-product array in O(V u^τ) with τ<1, via XOR combinations and address shears, yielding an exact permutation.
- `simultaneous-butterfly`: Fast simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u-v)/2) on the same bit of at most d address chunks of polynomial records of complex fixed-point numbers in O(V d^λ'), λ'<1, using exact Gaussian dyadics and one final truncation.
- `precision-exact-recovery`: Precision, error bound and exact recovery: Fixed-point precision analysis showing the recovered coefficient error is below 1/2 so rounding, rescaling and carry propagation give the exact integer product.
- `main-result`: Integer multiplication in O(n (lg n)^{1-κ}) time: Deterministic multitape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}) time, κ=2^{-182}, by chaining digit convolution, prime axes, Gaussian resampling, chirps, a polynomial-ring twist, synthetic transforms accelerated by fast address interchanges and butterfly layers, then exact recovery.

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
