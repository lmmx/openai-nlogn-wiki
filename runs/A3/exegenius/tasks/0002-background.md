# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/A3` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with roots of unity.
- `multitape-tm`: Multitape Turing machine (known to the reader): A deterministic machine with finite alphabet and a fixed number of one-dimensional tapes; time is the number of steps.
- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen multiplied n-bit integers in O(n log n log log n) on a multitape machine and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).
- `convolution-dft`: Convolution and the discrete Fourier transform: Convolution of coefficient lists is computed by transforming, multiplying pointwise, and transforming back using roots of unity.
- `radix-digit-reduction`: Multiplication as digit convolution: Splitting the inputs into radix digits turns integer multiplication into convolution of short integer coefficients, followed by carry propagation.
- `signed-packing`: Signed coefficient packing (Kronecker substitution): Packing polynomial coefficients into one long integer so a polynomial product becomes an integer product.
- `hh-nlogn-multiplier`: Established O(n log n) multiplier as subroutine: The Harvey–van der Hoeven O(n log n) algorithm, called as an ordinary subroutine for small polynomial products without recursively invoking the new theorem.
- `stream-operations`: Elementary stream operations on tapes: Array order, scans, controlled shifts and rational scalings that a fixed-tape machine performs in linear time.
- `poly-ring-mod-yr1`: Polynomial ring modulo y^r + 1: Polynomials in y with complex coefficients reduced using y^r = −1; powers of y act as roots of unity and multiplying by one is a signed cyclic shift of the coefficient list.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring where powers of y serve as roots of unity, built from address rearrangements, signed shifts and two-point butterflies (Nussbaumer).
- `exact-ring-products`: Exact normalized polynomial products: Convolution over the ring using the forward synthetic transforms, pointwise polynomial products via signed packing and the O(n log n) multiplier, and the opposite transform.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Placing the coefficient list on a product of distinct prime cyclic axes by a Chinese-remainder map that preserves convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven identity expressing a Fourier transform on prime-length axes through a multidimensional transform with power-of-two axis lengths; the coordinate permutations are retained in the identity.
- `bluestein-chirp`: Bluestein chirp identity: Converts a Fourier transform (with its target permutation) into a cyclic convolution via multiplication by chirp phases.
- `phase-twist`: Last-coordinate phase twist: A phase twist turning the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap yields the original cyclic wrap once the twist is removed.
- `linear-networks-frames`: Linear networks, roles and frames: A fixed linear network exchanging two banks of values with signs and restoring auxiliary values; roles are wire positions and invertible frames D_v change the stored representation so intermediate frames cancel and only an endpoint operator remains.
- `subset-network-construction`: Finite network from three-element subsets: Subspaces of a fixed m-dimensional space attached to gates, built from three-element subsets with gather/scatter and auxiliary wires, giving a total number of smaller calls s less than W·m.
- `recursive-saving`: Recursive power saving s < Wm: Recursing at parameter m·f uses s calls at parameter f on volume V/W each; since s/W < m the volume-normalized cost grows by less than a factor m per level, giving a power of the parameter below the first power.
- `restoring-auxiliary`: Restoring auxiliary values: Scratch registers with arbitrary initial contents are subtracted, used, re-added and the computation reversed so the final effect is exact for any initial auxiliary values.
- `address-shear`: Address shear and triangular factorization: Fields updated by (H,D) -> (H+D,D) over a residue ring; rational matrix shears are factored into lower-triangular pieces (Bruhat factorization) so they can be implemented cheaply in tape order.
- `address-interchange`: Fast interchange of address fields: Exchanging two disjoint contiguous u-bit address fields of an array with volume V in O(V u^τ) time for fixed τ<1, using XOR combinations of intermediate data though the final effect is an exact permutation.
- `butterfly-layer`: Simultaneous butterfly layer H₀: Applying H_0(u,v)=((u+v)/2,(u−v)/2) coefficientwise on selected address bits of numerical arrays of complex fixed-point polynomial records, via the recursive network, in O(V d^λ') time.
- `fixed-point-precision`: Fixed-point precision and exact recovery: Gaussian dyadic intermediates with a single truncation after a contractive layer; the recovered coefficient error is kept below 1/2 so rounding and carries give the exact integer product.
- `transform-layout`: Transform layout with retained frequency order and permutations: Tape layout on which the parallel layers apply; permutations from resampling and chirps are kept inside the transform and cancel across forward, pointwise product and opposite transforms rather than being sorted.
- `main-algorithm`: Multiplication algorithm and its cost: Chain the reductions: digits, prime axes, Gaussian resampling and chirps, phase twist, ring convolution with fast interchanges and butterfly layers, then rescaling, rounding and carries; the cost table fits n(lg n)^(1−κ).
- `main-result`: Integer multiplication below n log n: A fixed deterministic multitape Turing machine multiplies two n-bit integers in O(n (lg n)^(1−κ)) worst-case time with κ = 2^−182, refuting the n log n optimality conjecture in this model.

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
