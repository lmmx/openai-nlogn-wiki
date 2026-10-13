# exegenius task 0002-background

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

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
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi, with roots of unity.
- `turing-machine-tapes`: Multitape Turing machine (known to the reader): Finite-state machine with tapes read and written one cell per step.
- `fixed-tape-model`: Fixed-tape machine model and stream operations: Machine with one fixed finite alphabet and a fixed number of one-dimensional tapes; each step touches one cell per tape, so data movement (scans, shifts, permutations) is the cost to minimize.
- `convolution`: Convolution: Product of polynomials / combination of coefficient lists where entries sum by index (cyclic if indices wrap).
- `dft-fft`: Discrete Fourier transform and butterflies: Evaluation of a coefficient list at roots of unity, computed in log-many levels of two-point butterfly operations; turns convolution into pointwise product.
- `nlogn-conjecture`: The n log n optimality conjecture: Schönhage–Strassen's proposal that n log n is the optimal order of cost for multiplying n-bit integers.
- `ss-hh-background`: Schönhage–Strassen to Harvey–van der Hoeven multiplication: Chain of multitape algorithms from O(n log n log log n) to the unconditional O(n log n) bound, using transforms over rings with cheap roots of unity.
- `radix-digit-reduction`: Reduction of integer product to digit convolution: Splitting the inputs into radix digits turns the integer product into a convolution of short integer coefficients, followed by carry propagation.
- `crt-address-map`: Chinese-remainder map to prime cyclic axes: Places the coefficient list on a product of distinct prime cyclic axes by a map preserving convolution, implemented via triangular controlled shifts and axis moves.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven reduction expressing each Fourier transform of prime-length axes through a multidimensional transform with power-of-two axis lengths.
- `bluestein-chirp`: Bluestein's chirp identity: Rewrites a discrete Fourier transform as a cyclic convolution via chirp phases.
- `poly-ring-y-r`: Polynomial ring modulo $y^r+1$: Complex-coefficient polynomials in y reduced by y^r = -1, so multiplying by a power of y is a signed shift of the coefficient list and powers of y serve as roots of unity.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms over the polynomial ring where root multiplications are signed shifts, leaving address rearrangements, shifts and butterflies.
- `signed-packing`: Signed coefficient packing (Kronecker substitution): Packs polynomial coefficients into one integer so polynomial products are done by an ordinary n log n integer multiplier.
- `phase-twist-convolution`: Last-coordinate phase twist: Twisting the last cyclic coordinate into a polynomial modulo y^r+1 whose negative wrap equals the original cyclic wrap after untwisting.
- `ring-convolution-retained-order`: Convolution with retained transform order and cancelled permutations: Two forward synthetic transforms keep the same frequency order through the pointwise product, and the opposite transform consumes it, so retained permutations cancel without separate sorts.
- `address-fields`: Address fields and array layout on tapes: Arrays stored in tape order with addresses forming a Cartesian product of digit fields; rearranging fields costs time.
- `linear-network-roles`: Finite linear network with roles and frames: Fixed linear network exchanging two banks of values with prescribed signs and restoring auxiliary values; wires have roles, rows are distributed cyclically among roles, and invertible frame operators cancel along routes leaving an endpoint operator.
- `subset-intersection-construction`: Three-element subset intersection construction: Gather/scatter with auxiliary wires cancelling unwanted coefficients, using indicator-vector orthogonality to assign subspaces; gives s<Wm smaller calls.
- `recursive-power-saving`: Recursive power saving from s<Wm: Recursive call at parameter mf uses s calls at parameter f on streams of volume V/W; since s/W<m the volume-normalized cost grows as a power, giving a fixed power saving.
- `address-shear-factorization`: Address shear and lower-triangular factorization: Endpoint operator (H,D)->(H+D,D) over a residue ring, with rank reduction via a singular-matrix Bruhat factorization into lower-triangular factors.
- `scratch-restoration`: Restoring auxiliary scratch values: Subtract initial register value, compute, add result, reverse, so the permutation is exact for arbitrary initial auxiliary values.
- `fast-address-interchange`: Fast interchange of address fields: Interchange two disjoint contiguous u-bit address fields in an array in O(V u^τ) for fixed τ<1, via XOR combinations that end as an exact permutation.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u-v)/2) on selected address bits of polynomial-valued arrays with exact Gaussian dyadics in O(V d^λ') with λ'<1, one truncation at the end.
- `fixed-point-precision`: Fixed-point precision and exact recovery: Complex fixed-point coefficients; bounding error below 1/2 so rounding recovers exact integer coefficients and carry propagation yields the product.
- `main-theorem`: Integer multiplication in O(n(lg n)^{1-κ}) time: Deterministic fixed-tape Turing machine multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, by reducing to ring convolution with fast address interchanges and simultaneous butterfly layers, disproving the n log n conjecture in this model.

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
