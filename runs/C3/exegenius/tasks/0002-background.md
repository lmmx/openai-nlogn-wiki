# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/C3` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on growth of a function.
- `polynomials`: Polynomials (known to the reader): Sums of powers of a variable with coefficients.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi, with modulus and roots of unity e^{2πi/k}.
- `turing-machine`: Turing machines and tapes (known to the reader): Finite-state machine reading and writing cells of tapes.
- `tape-streams`: Fixed-tape machine model and tape streams: A machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes, where arrays are stored in address order and processed by sequential scans, so moving data costs time.
- `nlogn-conjecture`: The n log n conjecture and history of multiplication: Schönhage and Strassen proposed n log n as the optimal order for multiplying n-bit integers; the history runs from Karatsuba and Toom through Schönhage–Strassen and Fürer to Harvey–van der Hoeven's O(n log n).
- `convolution`: Convolution: The product of two coefficient lists as polynomials, cyclic when indices wrap around; integer multiplication is convolution of digits followed by carries.
- `dft`: Discrete Fourier transform: Evaluation of a coefficient list at powers of a root of unity, in normalized form (1/q)Σ u_j ω^{jk}; it turns convolution into pointwise product, and the opposite-sign transform inverts it.
- `radix-digit-reduction`: Reduction of integer multiplication to digit convolution: Split each operand into radix-2^b digits, take the convolution of the digit lists with scaled fixed-point values, round the coefficients and propagate carries.
- `fixed-point-dyadics`: Fixed-point complex values and Gaussian dyadics: Complex numbers stored as pairs of two's-complement integers over a power-of-two denominator 2^p, truncated toward zero, with contractive (norm ≤ 1) linear maps and error accumulation.
- `hvdh-multiplier`: Harvey–van der Hoeven O(n log n) multiplier as subroutine: The established O(N log N) integer multiplier, used as an ordinary subroutine for short integer products rather than recursively.
- `polynomial-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree less than r with y^r = -1, so multiplying by a power of y is a signed cyclic shift of the coefficient list; powers of y act as roots of unity.
- `synthetic-transform`: Synthetic polynomial transform: The Fourier transform over the polynomial ring using ω_t = y^{2r/t}, whose root multiplications are signed shifts and whose layers consist of two-point butterflies.
- `butterfly`: Two-point butterfly H₀: The map H_0(u,v) = ((u+v)/2, (u-v)/2) on a pair of values, the basic step of radix-two transforms.
- `address-fields`: Array addresses, fields and chunks: Arrays on tape are indexed by lexicographic address fields; chunks are contiguous groups of address digits, and rearranging them costs a pass over the data.
- `linear-network`: Linear exchange network with roles and frames: A fixed network of linear gates on wires (roles) that exchanges two banks of values while restoring auxiliary values; with a common invertible frame at each gate, arrays flow through pointwise and only endpoint frame operators remain.
- `subset-network`: Three-element-subset network with rank saving: A finite construction using three-element subsets, gather/scatter and auxiliary wires, with nested subspaces attached to gates so the total number s of smaller calls is below W·m.
- `recursive-power-saving`: Recursive power saving from s < Wm: A recursive call at parameter mf uses s calls on streams of volume V/W, so the cost per volume grows by s/W < m per factor m in the parameter, giving a power saving.
- `shear-factorization`: Lower triangular factorization of address shears: Bruhat-type factorization into lower triangular matrices, letting a rational matrix shear (H,D)→(H+D,D) on address fields be done with linear-time scans and rank-many smaller interchanges.
- `fast-interchange`: Fast interchange of address chunks: Interchanges two equal address chunks of u digits in time O(V u^τ) for a fixed τ < 1 via XOR-like linear combinations, ending in an exact permutation.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Applies H₀ on the same bit position in each of d address chunks of arrays of complex polynomial records in time O(V d^λ') with λ' < 1, evaluated exactly with one final truncation.
- `transform-layout`: Synthetic transform on a retained-order layout: Transforms on several axes are computed by simultaneous butterfly layers on a tape layout, with the frequency order kept through the pointwise product so the opposite transform consumes it.
- `signed-packing`: Signed packing (Kronecker substitution): Polynomial products over the ring are done by packing coefficients into signed integers and calling the integer multiplier, then unpacking.
- `ring-convolution`: Normalized convolution over the polynomial ring: Convolution on power-of-two axes over the polynomial ring via forward synthetic transforms, pointwise ring products and an opposite transform.
- `crt-address-map`: Chinese-remainder map to prime cyclic axes: The radix-digit coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map preserving convolution, implemented by controlled shifts and axis moves.
- `gaussian-resampling`: Gaussian resampling: Expresses a Fourier transform of coprime length as a power-of-two-length tensor transform with permutations, via Gaussian weights, with contraction and error bounds.
- `bluestein`: Bluestein's chirp identity: Rewrites a Fourier transform as a convolution using chirp factors.
- `retained-permutations`: Resampling with permutations left in the transform: The source and target coordinate permutations of resampling are kept inside the transform identity and cancel across the two forward transforms, product and inverse, so no separate sorts are run.
- `phase-twist`: Phase twist to the negacyclic last coordinate: A phase twist turns the last cyclic coordinate into a polynomial modulo y^r+1; its negative wrap yields the original cyclic wrap once the twist is removed.
- `precision-recovery`: Precision and exact recovery: Parameters are chosen so accumulated error in the recovered coefficients is below 1/2, so rounding returns the exact integer convolution, and carries yield the product.
- `multiplication-algorithm`: The multiplication algorithm and its cost: Digits are mapped by the CRT address map, transformed by two source transforms, multiplied pointwise, inverse transformed, scaled, rounded and carried; the cost table totals O(n(lg n)^{1-κ}) for a fixed rational parameter choice.
- `main-theorem`: Integer multiplication below n log n: A deterministic fixed-tape Turing machine multiplies two n-bit integers in O(n(lg n)^{1-κ}) time with κ = 2^{-182}, refuting the n log n optimality conjecture in this model.

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
