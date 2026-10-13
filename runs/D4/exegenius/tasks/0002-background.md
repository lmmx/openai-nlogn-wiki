# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/D4` (paths below are relative to it)

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
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with real and imaginary parts, including roots of unity.
- `turing-tapes`: Multitape Turing machines (known to the reader): Machines with finitely many tapes, heads, and a finite alphabet, one step reading and writing each tape.
- `fixed-tape-model`: Fixed-tape machine model and stream scans: The cost model: one fixed alphabet and a fixed number of one-dimensional tapes, where moving data by a bounded number of scans is cheap but permuting growing fields is not.
- `convolution-dft`: Convolution and the discrete Fourier transform: Convolution multiplies coefficient lists as polynomials; a Fourier transform at roots of unity turns it into pointwise products.
- `mult-to-convolution`: Integer multiplication as digit convolution: Splitting each n-bit integer into radix digits turns the product into a convolution of short integer coefficients, followed by carry propagation.
- `nlogn-conjecture`: History and the n log n conjecture: Schönhage–Strassen gave O(n log n log log n) and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).
- `ring-mod-y-r-plus-1`: Polynomial ring modulo y^r + 1: Complex polynomials in y reduced with y^r = −1, where powers of y act as roots of unity and multiplying by them is a signed shift.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms using powers of y in the ring as roots of unity, built from address rearrangements, signed shifts and butterflies.
- `butterfly`: Two-point butterfly: The operation H₀(u,v) = ((u+v)/2, (u−v)/2) on a pair of values, the building block of transform layers.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven reduction replacing arbitrary-length Fourier transforms by multidimensional transforms with power-of-two axis lengths.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Placing the radix-digit coefficient list on a product of distinct prime cyclic axes so that convolution is preserved.
- `bluestein-chirp`: Bluestein chirp conversion: Bluestein's chirp identity rewrites a transform of arbitrary length as a cyclic convolution.
- `phase-twist`: Coefficient twist to the negative wrap: Multiplying coefficients by phases turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap reproduces the cyclic wrap after untwisting.
- `signed-packing`: Signed packing (Kronecker substitution): Packing signed polynomial coefficients into one integer so that a polynomial product is computed by an ordinary integer multiplication.
- `polynomial-products`: Exact normalized polynomial products: Ring products in the transformed domain computed by signed packing and the established O(n log n) multiplier used as an ordinary subroutine.
- `fixed-point-dyadics`: Fixed-point complex coefficients and exact dyadics: Records hold complex fixed-point coefficients; layers are exact Gaussian dyadics with power-of-two denominators and a single truncation afterwards.
- `linear-network-frames`: Linear networks with frames and restored auxiliaries: A fixed linear network exchanges two banks of roles with signs; frames D_v change array representation along edges, intermediate frames cancel, and auxiliary values are restored.
- `subset-network`: Finite network from three-element subsets: A finite network with nested subspaces of an m-dimensional space attached to gates, built from three-element subset intersection counts, with total smaller calls s < Wm.
- `recursive-saving`: Recursive power saving: Applying the network at parameter mf uses s calls at parameter f on streams of volume V/W, and s < Wm makes the per-volume cost grow like a power below 1.
- `address-shear`: Address shear and triangular factorization: The endpoint operator (H,D) ↦ (H+D,D) on address fields over a residue ring, implemented via lower-triangular factorization.
- `fast-address-interchange`: Fast interchange of address chunks: Interchanging two disjoint contiguous address fields of u bits at cost O(V u^τ), τ<1, via XOR combinations that end as an exact permutation.
- `fast-butterfly-layers`: Simultaneous fast butterfly layers: Applying H₀ on the same selected bit of up to d address chunks at once at cost O(V d^λ′), λ′<1, with phase frames and a single truncation.
- `transform-layout`: Synthetic transform layout with retained frequency order: Layout on which the parallel layers apply; forward transforms keep the same frequency order through the pointwise product and the inverse consumes it.
- `permutation-cancellation`: Retained permutations cancelling: Source and target coordinate permutations are kept inside the transform identity and cancel across the forward transforms, product and inverse, avoiding full sorts.
- `exact-recovery`: Rounding, rescaling and carry propagation: Known normalizations and digit scales are removed, coefficient error is shown below 1/2, and carries yield the exact binary product.
- `multiplication-algorithm`: The assembled multiplication algorithm: Pipeline: digits to prime axes, resampling and chirps to power-of-two axes, phase twist to the ring, synthetic-transform convolution, then exact recovery.
- `main-theorem`: Integer multiplication below n log n: A deterministic fixed-tape Turing machine multiplies n-bit integers in O(n (lg n)^(1−κ)) time with κ=2^(−182), disproving the n log n optimality conjecture in this model.

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
