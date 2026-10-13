# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/M3` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Sums of powers of a variable with coefficients.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi, with roots of unity.
- `turing-machine`: Turing machines and tapes (known to the reader): Basic Turing machine with tapes, head moves and a finite alphabet.
- `multitape-model`: Fixed multitape Turing machine model: Deterministic machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes; the cost is the number of steps.
- `convolution`: Convolution and cyclic convolution: Combining two coefficient lists so that entry k sums products of entries whose indices add to k (cyclically or with wrap); integer multiplication reduces to it.
- `dft-roots-of-unity`: Fourier transform and roots of unity: Evaluating a coefficient list at roots of unity turns convolution into pointwise products; the fast version uses butterfly layers.
- `nlogn-conjecture`: The n log n conjecture and history of multiplication: Schönhage and Strassen's 1971 O(n log n log log n) bound and conjecture that n log n is optimal; Harvey and van der Hoeven reached O(n log n).
- `poly-ring-yr1`: Polynomial ring modulo y^r + 1: Polynomials in y with complex coefficients reduced using y^r = -1, so multiplying by a power of y is a signed shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms over the ring modulo y^r+1 where roots of unity are powers of y, so root multiplication is a signed shift; computed by address rearrangements, shifts and butterflies.
- `butterfly`: Two-point butterfly H₀: The map (u,v) -> ((u+v)/2,(u-v)/2) applied coefficientwise, the basic step of a transform layer.
- `radix-reduction`: Reduction of integer product to digit convolution: Split the inputs into radix digits so the product is a convolution of short integer coefficients, followed by carry propagation.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Placing the digit list on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven technique expressing each prime-length Fourier transform through a power-of-two multidimensional tensor transform, keeping source and target permutations in the identity.
- `bluestein-chirp`: Bluestein chirp identity: Converts the middle transform, with its target permutation, into a normalized cyclic convolution.
- `phase-twist`: Last-coordinate phase twist: A phase twist turning the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap equals the original cyclic wrap after untwisting.
- `signed-packing`: Signed packing (Kronecker substitution): Packing polynomial coefficients into one integer so a polynomial product is computed with the ordinary O(n log n) multiplier as a subroutine.
- `stream-operations`: Elementary stream operations and controlled shifts: Scans, array order, and shifts on tapes in linear time, forming the cost base for rearrangements.
- `linear-network`: Linear networks with roles and restored auxiliaries: A fixed linear network exchanging two banks of values with signs and restoring every auxiliary value; rows of an array are distributed cyclically among W roles and gates apply pointwise.
- `frames`: Frames and endpoint operators: Invertible linear operators D_v attached to gates; intermediate frames cancel so a route applies D_sink D_source^-1, leaving an endpoint operator such as an address shear or the H₀ layer.
- `finite-network-subspaces`: Finite networks with nested subspaces and rank saving: Network whose gates carry nested subspaces of an m-dimensional space built from three-element subset intersections, with total smaller calls s < W m.
- `recursive-saving`: Recursive power saving: A call at parameter m f uses s calls at f on volume V/W, raising the cost factor by s/W < m, giving a power of the logarithm.
- `address-interchange`: Fast interchange of address chunks: Procedure swapping two disjoint contiguous address fields of u bits in a Cartesian-product array via XOR combinations and address shears, in cost O(V u^τ), τ<1.
- `fast-butterfly-layer`: Simultaneous fast butterfly layers: Applying H₀ at the same bit position in each of d address chunks simultaneously on fixed-point complex polynomial records in cost O(V d^λ'), λ'<1.
- `complex-fixed-point`: Gaussian dyadics and fixed-point precision: Complex fixed-point numbers with power-of-two denominators; intermediate values exact, with one truncation after a contractive layer.
- `transform-layout`: Synthetic transforms on the retained layout: Layout on which parallel butterfly layers and address interchanges apply, giving transform cost and retaining frequency order through the pointwise product.
- `normalized-convolution`: Normalized convolution over the polynomial ring: Convolution on the remaining axes over the ring, via two forward transforms, pointwise polynomial products and the opposite transform.
- `exact-recovery`: Precision, rounding and carry propagation: Remove known normalizations and digit scales, show coefficient error is below 1/2, round and propagate carries to the exact binary product.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) time: Deterministic fixed-tape machine multiplying n-bit integers in O(n(lg n)^(1-κ)) with κ=2^-182, disproving the n log n optimality conjecture in this model.
- `lower-triangular-factorization`: Lower triangular (Bruhat) factorization: Every rational matrix of rank a factors as E1 Π E2 with E1, E2 lower triangular and Π a partial permutation with a ones, so a shear of rank a needs only a smaller interchanges, in tape order.

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

Keep any other files you make, such as scripts, in `exegenius/tasks/0002-background`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
