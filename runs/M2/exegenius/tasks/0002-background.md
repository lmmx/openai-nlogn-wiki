# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/M2` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on running time.
- `multitape-tm`: Multitape Turing machine (known to the reader): A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes.
- `complex-poly`: Complex numbers and polynomials (known to the reader): Arithmetic of complex numbers and polynomials.
- `convolution`: Convolution and multiplication by radix digits: Splitting integers into radix digits turns integer multiplication into convolution of short integer coefficient lists.
- `dft`: Discrete Fourier transform: Normalized transform (F_q u)_k = (1/q) Σ u_j e^{-2πi jk/q} that diagonalizes cyclic convolution and is a contraction in max norm.
- `nlogn-conjecture`: The n log n optimality conjecture and prior bounds: Schönhage and Strassen's O(n log n log log n) multiplier and conjecture that n log n is optimal, followed by the Harvey–van der Hoeven O(n log n) multiplier.
- `tape-streams`: Tape streams, array order and controlled shifts: Elementary linear-time scans, array layouts in lexicographic address order, whole-chunk moves and controlled shifts on tapes.
- `poly-ring`: Polynomial ring modulo y^r + 1: Complex polynomials of degree < r with y^r = -1, so multiplying by a power of y is a signed shift of the coefficient list.
- `synthetic-transform`: Synthetic polynomial transforms: Fourier transforms over the polynomial ring whose roots of unity are powers of y, computed by signed shifts and two-point butterflies (Nussbaumer).
- `signed-packing`: Signed packing (Kronecker substitution): Packing polynomial coefficients including negative ones into one integer so ring products reduce to integer multiplication by the O(n log n) multiplier.
- `ring-convolution`: Normalized convolution over the polynomial ring with retained frequency order: Convolution computed by two forward synthetic transforms, a pointwise product via packed products, and the opposite transform, keeping the same frequency order throughout.
- `bluestein`: Bluestein chirp identity: Rewrites a Fourier transform of arbitrary length as a cyclic convolution via chirp factors.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven reduction expressing a Fourier transform on prime lengths via a power-of-two multidimensional transform, here keeping source and target permutations inside the transform formula.
- `tensor-transform`: Multidimensional transform on power-of-two axes: A tensor-product Fourier transform over several axes of power-of-two length, with arbitrary growing dimension.
- `crt-map`: Chinese-remainder map to prime cyclic axes: Places the radix-digit coefficient list on a product of distinct prime cyclic axes so that convolution is preserved.
- `linear-network-frames`: Linear exchange networks with frames and roles: Fixed linear networks that exchange two banks of values and restore auxiliary values, applied pointwise to arrays whose representations are changed by invertible frame operators.
- `subset-network`: Three-subset networks with rank saving: Finite networks built from three-element subsets whose gates and terminals carry nested subspaces so that the total number s of smaller calls is less than W times m.
- `recursive-saving`: Recursive power saving: Recursion with s calls at parameter f on volume V/W, with s/W < m, yields a power-of-parameter saving over naive passes.
- `address-interchange`: Address interchange in time O(V u^τ): Interchanging two disjoint address fields of u bits via XOR combinations of intermediate streams, with exact final permutation.
- `simultaneous-butterfly`: Simultaneous butterfly layer in time O(V d^λ′): Applies H0(u,v)=((u+v)/2,(u-v)/2) coefficientwise on the same bit in up to d address chunks, using exact Gaussian dyadics and one final truncation.
- `fixed-point-precision`: Fixed-point precision and error control: Complex values stored on a 2^{-p} grid, with contractive maps, error accumulation and rounding so integer coefficients are recoverable.
- `multiplication-assembly`: Assembly of the multiplication algorithm: Chains digit convolution, CRT, Gaussian resampling, chirps, twist to the polynomial ring, rescaling, rounding and carry propagation, with parameters chosen so the cost table fits the theorem.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) on a multitape Turing machine: A deterministic multitape Turing machine multiplies two n-bit integers exactly in O(n(lg n)^{1-κ}) time with κ=2^{-182}, disproving the n log n optimality conjecture in this model.

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
