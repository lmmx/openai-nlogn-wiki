# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/K1` (paths below are relative to it)

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

- `big-o-notation`: Big-O notation (known to the reader): Asymptotic upper-bound notation O(f(n)) used to state running times up to constant factors.
- `polynomials`: Polynomials (known to the reader): Finite sums of powers of a variable multiplied by coefficients, which the construction stores as lists of coefficients.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a + bi with a and b real and i² = −1, with the usual modulus |a + bi|.
- `turing-machine-tapes`: Turing machines and tapes (known to the reader): Finite-state machines that read and write symbols on one or more tapes, with running time counted in steps.
- `fixed-tape-model`: Fixed-tape machine model: A Turing machine with one fixed finite alphabet and a fixed finite number of one-dimensional tapes, where each step moves every head by at most one cell.
- `integer-multiplication-problem`: Exact integer multiplication: The task of reading two n-bit binary strings x and y after a separator # and writing the 2n-bit binary representation of their product exactly, for every n.
- `sch-conjecture`: Schönhage–Strassen optimality conjecture: The proposal that n log n is the optimal order of growth for multiplying integers, which the target result refutes in the fixed-tape model.
- `harvey-hoeven-multiplier`: Harvey–van der Hoeven multiplier: The known unconditional O(n log n) bit-complexity algorithm for multiplying integers, which the construction calls as an ordinary subroutine.
- `linear-subspaces`: Subspaces, rank and orthogonal complement: Subspaces of a vector space over a field, their dimensions, the rank of a linear map, and the orthogonal complement of a subspace with respect to a bilinear form.
- `stream-scans`: Linear-time tape stream operations: Scans that permute, split, merge, or shift the entries of an array with V stored data bits in O(V) steps, where addresses are implicit in the position of each entry.
- `cyclic-convolution`: Cyclic convolution: The product of two coefficient arrays indexed by Z/tZ in which indices wrap around modulo the length t.
- `polynomial-ring-mod`: Polynomial ring modulo y^r + 1: The ring of complex polynomials in y reduced modulo y^r + 1, so that y^r equals −1 and products that overflow degree r wrap around with a sign.
- `gaussian-dyadics`: Gaussian dyadic numbers: Complex numbers whose real and imaginary parts are dyadic rationals with power-of-two denominators, so that they are stored exactly in binary.
- `approximate-contraction`: Approximate contraction: A map between arrays whose norm in the maximum-coefficient norm is at most one, computed with a stated error bound so that the errors of composed approximate steps add.
- `truncation`: Truncation to a fixed-point grid: Rounding each real and imaginary coefficient part toward zero onto a grid of spacing 2^−p, which does not increase the maximum-coefficient norm.
- `bank-exchange-network`: Bank-exchange network: A fixed linear network of wires with pointwise gates and scratch wires that exchanges two banks of values with prescribed signs and restores every scratch value.
- `three-element-subsets`: Three-element subset construction: The set of three-element subsets of a fixed ground set together with the intersection-size relation that decides which triples are joined by a wire.
- `scratch-restoring-exchange`: Scratch-restoring exchange: A three-stage gate schedule built from copy, gather, side-injection and scatter gates that adds one bank into another and exchanges two banks with a sign, leaving any initial scratch values unchanged.
- `frames`: Frame change for linear gates: An invertible operator D_v attached to each gate, source and sink, so that a wire's stored array is D_v applied to its logical array and a pointwise linear gate commutes with a common frame.
- `rank-saving-recursion`: Rank-saving recursion: The fact that the total rank s of the edge changes is less than W times m, so that multiplying the recursion parameter by m multiplies the recursive cost by s/W < m, a strict power saving.
- `address-shear`: Address shear: The update that replaces an address field H by H + D, with D another field, and which is the endpoint operator the bit network applies to every role.
- `bruhat-factorization`: Bruhat factorization for shears: The factorization of a singular matrix into lower-triangular factors after reversing the coordinate order, so that a shear becomes a sequence of updates of later fields from earlier ones.
- `fast-address-interchange`: Fast address-chunk interchange: A tape procedure that swaps two disjoint equal-width address chunks of u bits in a stored array of volume V in O(V u^τ) time for a fixed τ < 1, by recursive calls to the bit network.
- `complex-phase-network`: Complex phase network: The fixed linear network over Gaussian dyadic values and binary subspaces that exchanges complex coefficients while restoring every scratch value.
- `simultaneous-butterfly-layer`: Simultaneous butterfly layer: The operation that applies the two-point butterfly H_0(u, v) = ((u + v)/2, (u − v)/2) to D selected address bits at once on arrays of complex polynomial records, at cost O(V d^λ′) with λ′ < 1.
- `radix-digit-convolution`: Radix-digit convolution: The reduction of an integer product to the cyclic convolution of its base-2^b digit sequences, whose coefficients are short integers before carries are propagated.
- `fourier-transform`: Normalized discrete Fourier transform: The map on length-q vectors whose k-th output is (1/q) times the sum over j of u_j e^(−2πijk/q), which is a contraction in the maximum-modulus norm.
- `chinese-remainder-axes`: Chinese remainder axis layout: The algebra isomorphism that places a cyclic convolution of pairwise coprime length S on a product of cyclic axes, so that the change of coefficient order is a sequence of controlled shifts.
- `gaussian-resampling`: Gaussian resampling: The identity that expresses a Fourier transform of a length that is not a power of two through a tensor transform with power-of-two axis lengths, using Gaussian-weighted resampling.
- `sort-free-resampling`: Sort-free Gaussian resampling: Gaussian resampling in which the source and target coordinate permutations remain inside the transform formula, so they are never executed as separate full sorts.
- `bluestein-chirp`: Bluestein's chirp identity: The identity that writes a transform with quadratic phase factors (chirps) as a pointwise multiplication by a chirp, a cyclic convolution, and a second pointwise multiplication by the conjugate chirp.
- `permutation-cancellation`: Permutation cancellation: The identity that the retained source permutation cancels across the two forward transforms, their pointwise product and the inverse transform, leaving a plain cyclic convolution.
- `signed-kronecker-packing`: Signed Kronecker packing: Encoding a polynomial with signed integer coefficients as a single integer by placing the coefficients at fixed bit spacing, so that one integer product computes the polynomial product.
- `synthetic-polynomial-transform`: Synthetic polynomial transform: A transform over the polynomial ring in which the roots of unity are powers of y, so that multiplying by a root is a signed shift of a coefficient list, computed with radix-two butterflies.
- `phase-twist`: Phase twist to negacyclic wrap: A phase multiplication of the last cyclic coordinate that turns the cyclic wrap-around into the negative wrap of the polynomial ring, so that the original cyclic product is recovered once the twist is removed.
- `normalized-ring-convolution`: Normalized convolution over the polynomial ring: The bilinear map sending arrays f and g of ring elements to (f * g)/T, computed from the retained transform layout and bounded in the maximum-coefficient norm.
- `rounding-carry-recovery`: Rounding and carry recovery: The step that removes the known normalizations and digit scales, rounds each recovered coefficient (with error below 1/2), and propagates carries to obtain the exact binary product.
- `multiplication-pipeline`: Transform pipeline for integer product: The sequence of reductions (digit packing, Chinese remainder layout, sort-free Gaussian resampling, chirps, phase twist, normalized ring convolution, cancellation and carry recovery) that computes the exact product of two integers.
- `parameter-choice-cost`: Parameter choice and cost accounting: The fixing of rational exponents, including τ = σ = 1 − 2^−50 and κ = 2^−182, so that every term of the cost table is within the bound O(n(lg n)^(1−κ)) after division by the stored volume V.
- `sub-linearithmic-integer-multiplication`: Sub-linearithmic integer multiplication on a fixed tape machine: A single deterministic fixed-alphabet machine with a fixed number of one-dimensional tapes multiplies two n-bit integers exactly in O(n(lg n)^(1−κ)) worst-case time, with κ = 2^−182, disproving the n log n optimality conjecture in this model.

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
