# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/M5` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable, with addition and multiplication.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi, including roots of unity.
- `turing-machine`: Turing machines and tapes (known to the reader): Machine model with a finite alphabet and tapes read and written by heads.
- `multitape-model`: Multitape Turing machine multiplication model: Fixed finite alphabet, fixed finite number of one-dimensional tapes; cost is the number of steps for bit-level multiplication.
- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture and history: Schönhage and Strassen proposed n log n as the optimal order for multiplying n-bit integers; Harvey–van der Hoeven reached O(n log n).
- `convolution`: Radix digits and convolution: Splitting integers into radix digits turns multiplication into convolution of short integer coefficient lists.
- `fourier-transform`: Discrete Fourier transform: Evaluates a coefficient list at roots of unity; it turns convolution into pointwise product.
- `multidimensional-transform`: Multidimensional transforms with power-of-two axes: A transform on an array with several axes, each of power-of-two length, applied axis by axis.
- `crt-address-map`: Chinese-remainder map to prime cyclic axes: A Chinese-remainder address map that places a coefficient list on a product of distinct prime cyclic axes while preserving convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven identity expressing a source Fourier transform through a power-of-two tensor transform, with source and target permutations.
- `bluestein-chirp`: Bluestein chirp identity: Converts a transform into a normalized cyclic convolution via multiplication by chirp phases.
- `polynomial-ring`: Polynomial ring modulo y^r + 1: Complex-coefficient polynomials in y reduced by y^r = -1, with r a power of two; negacyclic wrap.
- `phase-twist`: Phase twist to the polynomial ring: A phase multiplication that turns the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap gives the original cyclic wrap after untwisting.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms using powers of y as roots of unity, so root multiplications are signed shifts of coefficient lists.
- `butterfly`: Two-point butterfly: The operation H0(u,v) = ((u+v)/2, (u−v)/2) applied coefficientwise.
- `signed-packing`: Signed packing (Kronecker substitution): Packs polynomial coefficients into one integer so a polynomial product is computed by an ordinary integer multiplier.
- `tape-streams`: Tape array order and elementary stream operations: Arrays stored in address order on tapes with scans, address fields, controlled shifts and whole-chunk moves.
- `linear-network`: Linear network with roles and frames: A fixed linear network exchanging two banks of values; wires are roles, each gate has an invertible frame, and intermediate frames cancel, leaving an endpoint operator.
- `subset-network`: Finite networks from three-element subsets: Subspaces of a fixed m-dimensional space attached to gates, built from three-element subsets with gather, scatter and auxiliary wires, giving fewer than Wm smaller calls.
- `restored-auxiliaries`: Restoring auxiliary values: Scratch values with arbitrary initial contents are subtracted, used, and added back so the result is exact for any initial auxiliary values.
- `recursive-saving`: Recursive power saving: Because s/W < m, multiplying the parameter by m raises the per-volume cost by less than m, giving a cost of volume times a power of the parameter below 1.
- `address-shear`: Address shear and triangular factorization: The map (H,D) to (H+D,D) on two address fields, with matrix factorization into lower-triangular factors, which with two linear-cost updates completes an interchange.
- `address-interchange`: Fast address-field interchange: Interchanges two disjoint contiguous address fields of u bits in an array of stored bit volume V in time O(V u^τ) with τ<1, using XOR combinations of data.
- `fast-butterfly-layer`: Simultaneous butterfly layer: Applies H0 simultaneously on the same bit position in d address chunks of numerical arrays, cost O(V d^λ') with λ'<1, with a single truncation after the layer.
- `fixed-point-precision`: Fixed-point Gaussian dyadics and exact recovery: Complex coefficients stored in fixed point with exact Gaussian dyadic intermediates; error is shown below 1/2 so rounding recovers integer coefficients.
- `carry-propagation`: Rescaling and carry propagation: Removing known normalizations and digit scales and propagating carries turns recovered coefficients into the binary product.
- `transform-layout`: Transform layout with retained frequency order: Layout on tape in which forward synthetic transforms keep the same frequency order through pointwise product and the opposite transform consumes it.
- `target`: Multiplying n-bit integers in O(n (lg n)^(1-κ)) time: Deterministic multitape algorithm combining digit convolution, Chinese-remainder map, Gaussian resampling, chirps, synthetic transforms with fast tape procedures, and carries.

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
