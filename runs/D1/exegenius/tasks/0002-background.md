# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/D1` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Polynomials, their coefficients and products.
- `complex-numbers`: Complex numbers (known to the reader): Complex arithmetic, modulus and roots of unity as points on the unit circle.
- `multitape-tm`: Multitape Turing machine (known to the reader): A Turing machine with finite alphabet and finitely many tapes, each step moving heads by at most one cell.
- `convolution`: Convolution and cyclic convolution: The product of two coefficient lists as polynomials, with indices optionally wrapped around cyclically.
- `dft`: Discrete Fourier transform and roots of unity: The transform evaluating a coefficient list at powers of a primitive root of unity; it turns convolution into pointwise product.
- `butterfly`: Two-point butterfly and fast transform levels: The radix-2 step mapping (u,v) to ((u+v)/2,(u-v)/2); a fast transform applies lg n levels of these, each costing a scan of the data.
- `radix-digit-reduction`: Integer product as radix-digit convolution: Splitting each operand into radix-2^b digits turns the integer product into a convolution of digit lists, followed by carry propagation.
- `nlogn-multiplier`: Known O(n log n) multiplier and the n log n conjecture: Harvey and van der Hoeven's O(n log n) multitape multiplication, used as an ordinary subroutine, and the Schönhage-Strassen conjecture that n log n is optimal.
- `tape-layout-streams`: Address fields, streams and scans on tape: Arrays stored in lexicographic address order on tape, with fields of address digits, processed by linear scans, controlled shifts and cyclic splitting into role streams.
- `fixed-point-dyadic`: Fixed-point Gaussian dyadic records: Complex numbers stored with p fractional bits (real and imaginary parts multiples of 2^-p), with exact intermediate dyadics and a single truncation.
- `negacyclic-ring`: Polynomial ring modulo y^r+1: Complex polynomials of degree below r with y^r = -1, so powers of y act as roots of unity and multiplication by y^a is a signed shift of coefficients.
- `synthetic-transform`: Synthetic polynomial transforms: Fourier transforms over the ring modulo y^r+1 using powers of y as roots, computed by signed shifts and butterflies and retaining one stored frequency order for the inverse.
- `signed-packing`: Signed packing (Kronecker substitution): Evaluating polynomial products over the ring as a single integer product by packing signed coefficients into one integer, then unpacking.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: A reindexing of the coefficient list onto a product of cyclic axes of distinct prime lengths that preserves convolution, giving a multidimensional convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey-van der Hoeven technique expressing a Fourier transform of prime length through a power-of-two tensor transform, with source and target permutations.
- `bluestein-chirp`: Bluestein chirp identity and phase twist: Rewriting a transform as a cyclic convolution via chirps; a phase twist turns the last cyclic axis into a negacyclic polynomial modulo y^r+1.
- `permutation-cancellation`: Retaining permutations in the transform: The source permutation from resampling cancels across the two forward transforms, the pointwise product and the inverse transform, avoiding separate full sorts.
- `linear-network-frames`: Linear exchange networks with roles and frames: A fixed linear network exchanging two banks of values and restoring auxiliary values; applied to arrays via rows distributed over wire roles, with an invertible frame per gate so intermediate frames cancel.
- `subset-intersection-network`: Three-element-subset subspace construction: Finite network over subsets of size three whose gates and terminals carry nested subspaces of a fixed m-dimensional space, using intersection counts so that the number s of smaller calls satisfies s<Wm.
- `recursive-power-saving`: Recursive rank saving gives a power saving: A call at parameter mf uses s<Wm calls at parameter f on streams of volume V/W, so cost per volume grows as a power below the first, giving exponent <1.
- `address-shear`: Address shear and triangular factorization: The endpoint operator (H,D) -> (H+D,D) on address fields, with matrix shears implemented through lower-triangular (Bruhat-type) factorization in tape order.
- `address-interchange`: Fast address-field interchange costing O(V u^τ): Exchanging two disjoint address fields of u digits in an array of volume V in time O(V u^τ) with τ<1, via XOR-like combinations that end in an exact permutation.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer on selected bits: Applying H_0 on the same bit position of up to d address chunks at once on polynomial records, with a complex phase network, in time O(V d^λ') with λ'<1, exact until one final truncation.
- `precision-exact-recovery`: Precision, rounding and carry recovery: Tracking contractive error bounds through all transforms so the recovered convolution coefficients err by less than 1/2, then rounding and propagating carries.
- `parameter-cost-accounting`: Parameter choice and total cost accounting: A fixed rational choice of exponents (including κ=2^-182) makes each cost term, divided by volume, a power of p below one so the total is O(n (lg n)^(1-κ)).
- `main-result`: Integer multiplication in O(n (lg n)^(1-κ)): A deterministic multitape Turing machine multiplies n-bit integers in O(n (lg n)^(1-κ)) time with κ=2^-182, disproving the n log n optimality conjecture in this model.
- `packed-selected-bit-addition`: Packed selected-bit addition: Adding (XOR) selected bit positions at positions rho+iK of grouped address chunks in one packed pass, the primitive behind changing address bits in the butterfly layer.

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
