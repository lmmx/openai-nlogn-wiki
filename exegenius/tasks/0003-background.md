# exegenius task 0003-background

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

## Correction

A person following the run said this of an earlier answer; follow it:

The reader has also taken the calculus such a degree requires: limits, convergence of sequences and series, and basic integrals.

## Existing concepts

- `big-o`: Big-O notation (known to the reader): Notation bounding how a function grows asymptotically, up to a constant factor, as its input grows.
- `polynomial`: Polynomials (known to the reader): Expressions sum of constant multiples of powers of a variable, whose coefficients can be listed in order.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + ib with real a and b and imaginary unit i satisfying i² = −1.
- `multitape-tm`: Multitape Turing machine (known to the reader): A Turing machine with several tapes, each with its own head, that reads and writes at most one cell per tape per step.
- `fixed-tape-model`: Fixed-tape machine model: A multitape Turing machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes, the same for every input length.
- `schonhage-strassen-conjecture`: Schonhage-Strassen optimality conjecture: The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers on a multitape Turing machine.
- `power-saving`: Power saving in the logarithmic factor: A bound of the form n times (lg n) raised to the power 1 − κ for a fixed κ > 0, which is smaller than n log n by a polynomial factor in log n.
- `linear-network`: Linear network: A fixed network of wires with gates that apply fixed linear maps to the values on their wires, used here to exchange two banks of values while restoring all auxiliary values.
- `frame`: Frame of a vertex: An invertible linear operator attached to a gate or terminal that sets how the array on each wire there is stored; changing frames along an edge cancels between the two ends of a route.
- `role-streams`: Role streams from a cyclic row split: Splitting the rows of an array cyclically among the W fixed wire roles of a network, so that each role carries an equal share of the volume and gates act pointwise on matching addresses.
- `subset-network`: Subset-intersection finite network: A linear network over three-element subsets of a fixed ground set, whose gather, scatter, copy and side wires implement the scalar exchange of two banks by intersection-size coefficients over F_2 or Z[i,1/2].
- `subspace-labels`: Nested subspace labels: Assignments of subspaces of a fixed space to the gates and terminals of a network, nested along edges, whose dimension drops measure the smaller operations needed on each edge.
- `address-shear`: Address shear: The address permutation that replaces the first of two address fields H by H + D, leaving D fixed, which is the endpoint operator of the bit network on arrays.
- `recursive-saving`: Rank-saving recursion: A recursive scheme in which an edge matrix of rank a costs a smaller calls and the total number s of smaller calls over W roles satisfies s < Wm, so that multiplying the parameter by m multiplies the cost by less than m per unit volume.
- `tape-interchange`: Fast interchange of address chunks: A fixed-tape procedure that swaps two disjoint equal-width address fields of an array in time O(V u^τ) for a fixed τ < 1, where V is the stored volume and u the field width, using XOR combinations of intermediate data.
- `gaussian-dyadic`: Gaussian dyadic numbers: Complex numbers whose real and imaginary parts are both dyadic rationals, that is, have power-of-two denominators.
- `butterfly-layer`: Simultaneous butterfly layer H₀: The map H₀(u,v) = ((u+v)/2, (u−v)/2) applied at once to a selected coordinate bit of every chunk, a two-point butterfly acting coefficientwise on polynomial records.
- `polynomial-ring`: Polynomial ring modulo yʳ + 1: The ring of complex polynomials of degree less than r, with multiplication reduced modulo y^r + 1; multiplication by a power of y permutes and sign-changes the coefficient list.
- `roots-of-unity`: Root of unity: A number whose some positive integer power equals one; here powers of y in the polynomial ring play this role.
- `synthetic-transform`: Synthetic polynomial transform: A discrete Fourier transform whose roots of unity are powers of y in the polynomial ring, so that each twiddle multiplication is a signed shift and the transform is computed by simultaneous butterfly layers.
- `fourier-transform`: Discrete Fourier transform: The map sending a vector u of length q to the vector whose k-th entry is (1/q) times the sum over j of u_j times exp(−2πijk/q).
- `multidim-transform`: Multidimensional transform with power-of-two axes: A transform on an array indexed by several coordinates, each with length a power of two, obtained as a tensor product of one-dimensional Fourier transforms.
- `gaussian-resampling`: Gaussian resampling: A rewriting of a Fourier transform of prime length as a transform with power-of-two axis lengths, with source and target coordinate permutations kept inside the transform identity.
- `cyclic-convolution`: Cyclic convolution: The product of two coefficient lists in the ring of polynomials modulo x^S − 1, in which exponents wrap around modulo S.
- `bluestein`: Bluestein's chirp identity: An identity writing a Fourier transform as a cyclic convolution sandwiched between pointwise multiplications by chirp sequences exp(−πi s j² / t).
- `crt-axis-map`: Chinese-remainder axis map: The bijection sending a coefficient index written in mixed radix with pairwise coprime lengths to coordinates on a product of cyclic axes, which turns one cyclic convolution into a multidimensional one.
- `radix-digit-convolution`: Radix-digit convolution: Writing each n-bit input as a polynomial in 2^b with about n/b nonnegative digits, so that integer multiplication becomes a convolution whose coefficients are bounded by a fixed power of two.
- `signed-packing`: Signed coefficient packing: Encoding a polynomial with signed integer coefficients as one integer by placing coefficients at fixed bit offsets, so that a polynomial product becomes an integer product.
- `multiplier-subroutine`: Established fast multiplier: The known deterministic O(n log n) multiplication algorithm of Harvey and van der Hoeven, used as a black-box subroutine on shorter integers.
- `exact-recovery`: Exact recovery by rounding and carries: Recovering the exact integer coefficients of a convolution by rounding the computed values, whose error is below one half, and then propagating carries in radix 2^b.
- `fixed-tape-multiplication`: Fixed-tape integer multiplication with a power saving: A deterministic fixed-tape Turing machine that multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, for a fixed κ = 2^(−182), disproving the n log n optimality conjecture in this model.

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

Write the answer to `exegenius/tasks/0003-background.answer.json`, then run `exegenius submit 0003-background` in the project directory. If submit rejects the answer, fix the answer and submit again.
