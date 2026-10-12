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

- `integer-multiplication-target`: Integer multiplication in O(n(lg n)^(1-κ)) time: A deterministic multitape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1-κ)) worst-case time for a fixed κ = 2^(-182) > 0, beating the n log n conjecture in this model.
- `big-o`: Big-O notation (known to the reader): Notation O(g) for the set of functions bounded above by a constant multiple of g for all sufficiently large inputs.
- `multitape-tm`: Multitape Turing machine (known to the reader): A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, each with its own head that moves at most one cell per step.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with a, b real and i² = −1, used for the roots of unity and the coefficients of the transforms.
- `polynomials`: Polynomials (known to the reader): Expressions a₀ + a₁y + … + a_k y^k over a coefficient ring, with the usual addition and multiplication.
- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture: The conjecture of Schönhage and Strassen that n log n is the optimal order of growth of the time to multiply two n-bit integers on a multitape Turing machine.
- `harvey-hoeven-multiplier`: Harvey–van der Hoeven O(n log n) multiplication: The unconditional O(n log n) multiplication algorithm on a multitape Turing machine, used in this result as an ordinary subroutine.
- `matrix-rank`: Matrix rank: The rank of a matrix is the maximum number of linearly independent rows or columns; the number of nonzero pivots in elimination.
- `fourier-transform`: Discrete Fourier transform: The map sending a length-n sequence to its values at the n-th roots of unity, i.e. the sums of the sequence weighted by powers of a root of unity.
- `roots-of-unity`: Primitive roots of unity: A complex number ω is a primitive n-th root of unity when ω^n = 1 and no smaller positive power equals 1.
- `cyclic-convolution`: Cyclic convolution: The product of two sequences in which indices are taken modulo a fixed length, so each coefficient of the result is a sum of products over residues.
- `convolution-reduction`: Multiplication as convolution of digits: Writing each integer in radix 2^b digits so that the integer product becomes a convolution of the digit sequences, which is then carried back to binary.
- `chinese-remainder-address-map`: Chinese-remainder address map: A rearrangement that places a digit sequence on a product of distinct prime cyclic axes while preserving convolution, implemented with address interchanges.
- `gaussian-resampling`: Gaussian resampling: An identity that expresses a Fourier transform of length given by a prime as a multidimensional transform with power-of-two axis lengths, with the source and target permutations kept in the identity.
- `bluestein-chirp`: Bluestein's chirp identity: The identity that converts a Fourier transform into a cyclic convolution by multiplying by chirp factors before and after it.
- `polynomial-ring-y`: Polynomial ring modulo yʳ + 1: The ring of complex polynomials in y reduced modulo y^r + 1, where multiplying by a power of y is a signed cyclic shift of the coefficient list.
- `synthetic-transform`: Synthetic polynomial transform: A transform over a polynomial ring in which the roots of unity are powers of y, so that each transform stage uses only signed shifts and butterfly additions.
- `kronecker-packing`: Signed Kronecker packing: Encoding a polynomial with bounded signed coefficients as an integer by evaluating it at a large power of two, so that polynomial products become integer products.
- `butterfly-operation`: Butterfly operation: The two-point map (u, v) ↦ ((u + v)/2, (u − v)/2) applied to a pair of values, the basic step of a fast transform.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: A butterfly operation applied at once on one selected address bit of every record, with exact Gaussian dyadic intermediates and a single truncation after the layer.
- `linear-network-exchange`: Linear network with restored auxiliary values: A fixed linear network that exchanges banks of values with prescribed signs and restores every auxiliary value, with each gate acting on the stored array through a frame operator that cancels between edges.
- `lower-triangular-factorization`: Lower-triangular factorization: The factorization A = E₁ΠE₂ of a rational matrix into invertible lower-triangular factors and a partial permutation matrix with one 1 per pivot.
- `address-shear`: Address shear: The permutation (H, D) ↦ (H + AD, D) on two ordered groups of address fields, which is performed with as many pairwise interchanges as the rank of A.
- `address-interchange`: Fast address interchange: A tape procedure that swaps two disjoint contiguous address fields of an array in time O(V u^τ) for width u, computed through XOR combinations of intermediate data.
- `recursive-power-saving`: Recursive power saving: The mechanism in which a network with s smaller calls on W roles and parameter m gives a recursion with cost ratio s/W < m, so that repeated recursion saves a power of the parameter.
- `rounding-recovery`: Exact recovery by rounding: The step in which the approximate convolution coefficients are rounded to integers, provided the error is strictly below 1/2, and carries are then propagated to give the exact binary product.

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
