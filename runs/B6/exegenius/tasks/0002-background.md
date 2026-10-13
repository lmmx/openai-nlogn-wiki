# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/B6` (paths below are relative to it)

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
- `multitape-turing-machine`: Multitape Turing machine (known to the reader): Deterministic machine with a fixed finite alphabet and a fixed number of one-dimensional tapes; running time counts bit steps.
- `multiplication-history`: Schönhage–Strassen conjecture and prior bounds: Multiplication of n-bit integers was known in O(n log n log log n), then n log n 2^O(log* n), then O(n log n) (Harvey–van der Hoeven); Schönhage and Strassen conjectured n log n is optimal.
- `convolution-dft`: Convolution and the discrete Fourier transform: Convolution of coefficient lists is computed by transforming, multiplying pointwise, and inverse transforming with the normalized DFT.
- `integer-to-convolution`: Radix-digit reduction of integer multiplication to convolution: Splitting integers into radix digits turns the product into a convolution of short integer coefficient lists, followed by carry propagation.
- `kronecker-signed-packing`: Signed Kronecker packing: Packing polynomial coefficients, including negative ones, into one integer so that a single integer product yields the polynomial product.
- `hh-subroutine`: Harvey–van der Hoeven O(n log n) multiplier as subroutine: The established O(N log N) fixed-tape integer multiplier, used as an ordinary subroutine on small inputs, not recursively.
- `negacyclic-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree < r with y^r = -1; powers of y act as roots of unity and multiplying by one is a signed cyclic shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style Fourier transforms over the negacyclic ring where roots of unity are powers of y, so the work is address rearrangement, signed shifts and two-point butterflies.
- `coefficient-twist`: Coefficient twist to negacyclic convolution: Mapping x to ζy with ζ=e^{πi/r} turns cyclic convolution of length r into negacyclic ring convolution, multiplying coefficient k by ζ^k.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a Fourier transform of arbitrary length as a convolution multiplied by chirp phases.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Places the digit coefficient list on a product of distinct prime-length cyclic axes in a way preserving convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven technique expressing a Fourier transform of coprime-length axes through a multidimensional power-of-two tensor transform, with source and target permutations.
- `fixed-point-gaussian-dyadics`: Fixed-point Gaussian dyadic numerics: Numbers 2^{-p}(a+ib) in a disk, stored as two's-complement records; intermediate values are exact and a single truncation follows a contractive layer.
- `tape-streams`: Array order and elementary tape scans: Arrays stored in address order on tape; linear-time scans, pointwise operations and field updates.
- `bank-exchange-network`: Fixed linear network exchanging two banks with restored auxiliaries: A fixed network of linear gates on role wires that swaps two data banks with signs and restores every auxiliary value.
- `subset-intersection-labels`: Three-element subset construction with nested subspaces: Gather/scatter on three-element subsets with intersection-count pairings, plus side wires, give nested subspace labels with total rank deficit s < Wm.
- `frames`: Frames and pointwise gates on arrays: Invertible linear operators D_v giving the stored representation of each wire array; pointwise gates commute with a common frame so intermediate frames cancel.
- `recursive-power-saving`: Recursive rank saving: Edge operators of rank a need a smaller calls; since the total s of calls satisfies s<Wm, parameter growth by m raises cost per volume by s/W<m, giving a power saving.
- `address-shear`: Address shear and Bruhat factorization: Updating fields (H,D) to (H+D,D) over a residue ring and factoring matrices into triangular pieces that can be applied in tape order.
- `fast-address-interchange`: Fast interchange of address chunks: Interchanges two disjoint contiguous u-bit address fields of an array of volume V in O(V u^τ), τ<1, using XOR combinations that cancel to an exact permutation.
- `simultaneous-butterfly-layers`: Simultaneous butterfly layers: Apply H_0(u,v)=((u+v)/2,(u-v)/2) coefficientwise on the same selected bit in each of d address chunks in O(V d^λ'), λ'<1, with phase frames and a single truncation.
- `synthetic-layout`: Synthetic transform tape layout: Layout of roots, butterflies and stored frequency order on tape so the parallel layers apply and the same frequency order persists through the pointwise product.
- `normalized-polynomial-products`: Exact normalized ring products: Pointwise product of ring elements by signed packing and the O(n log n) multiplier, returning rounded results.
- `resampling-permutations-in-transform`: Resampling with permutations left in the transform: Keeps source and target coordinate permutations inside the transform identity so they cancel and avoid full sorts.
- `exact-recovery`: Precision and exact recovery: Removing normalizations, showing coefficient error is below 1/2, rounding and propagating carries to get the exact binary product.
- `main-theorem`: Sub-n log n integer multiplication algorithm: Deterministic multitape Turing machine multiplying n-bit integers in O(n (lg n)^{1-κ}), κ=2^{-182}, by reducing to convolution, resampling, chirps and synthetic transforms accelerated by fast address interchange and butterfly layers.

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
