# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/M1` (paths below are relative to it)

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
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with i²=-1, including roots of unity.
- `multitape-tm`: Multitape Turing machine (known to the reader): A Turing machine with finitely many tapes, a fixed alphabet, and one cell read/written per tape per step.
- `dft-convolution`: Discrete Fourier transform and cyclic convolution: The DFT maps a length-q sequence to averages weighted by roots of unity; it turns cyclic convolution into pointwise multiplication.
- `nlogn-conjecture`: The n log n conjecture and prior multiplication algorithms: Schönhage–Strassen proposed n log n as optimal multiplication time; Harvey and van der Hoeven reached O(n log n).
- `hh-multiplier`: O(n log n) multiplier as a subroutine: The established Harvey–van der Hoeven fixed-tape integer multiplier, called as an ordinary subroutine on short inputs.
- `radix-convolution`: Multiplication as convolution of radix digits: Splitting inputs into radix digits turns integer multiplication into convolution of short integer coefficient lists, later carried back to the binary product by carries.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: The coefficient list is placed on a product of distinct prime cyclic axes by a Chinese-remainder map preserving convolution.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven technique expressing a Fourier transform of coprime length through a power-of-two transform, here keeping the two coordinate permutations inside the transform formula.
- `bluestein-chirp`: Bluestein chirp identity: Converts a Fourier transform, including its target permutation, into a cyclic convolution with pointwise phase multiplications.
- `ring-ymr`: Polynomial ring modulo y^r + 1: Complex polynomials modulo y^r+1 with r a power of two, in which multiplying by a power of y is a signed shift of the coefficient list.
- `butterfly`: Two-point butterfly: The map (u,v)↦((u+v)/2,(u−v)/2) applied to a pair of values; the building block of fast transforms.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier transforms over the ring modulo y^r+1 using powers of y as roots of unity, so root multiplications are signed shifts, evaluated by butterfly layers with a retained frequency order.
- `signed-packing`: Signed packing (Kronecker substitution): Multiplying ring polynomials exactly by packing signed coefficients into one integer, calling the integer multiplier, and unpacking.
- `fixed-point-exactness`: Fixed-point precision, exact dyadics and error control: Values are complex numbers on a 2^-p grid; intermediate arithmetic is exact over Gaussian dyadics, with a single truncation, and total error is kept below 1/2 so rounding recovers integers.
- `array-streams`: Arrays on tape, address fields and volume: Arrays are stored in lexicographic order with implicit addresses split into fields; volume V is the number of stored data bits; permutations are realized by scans.
- `linear-networks-frames`: Linear networks, roles and frames: A fixed linear network of gates exchanges two banks of values with signs and restores auxiliary values; roles are wire places and frames are invertible operators giving the stored representation, cancelling so the endpoint operator is the desired one.
- `subset-networks`: Finite networks from three-element subsets: Construction using three-element subsets, gather, scatter and scratch wires, with nested subspaces at vertices so that the total number of smaller calls is below the number of roles times m.
- `recursive-saving`: Recursive power saving s < Wm: Using s calls at parameter f on volume V/W each, with s<Wm, makes the cost per volume grow by a factor below m when the parameter is multiplied by m, giving a power rather than linear growth.
- `lower-triangular-shear`: Lower triangular factorization and address shear: Any rational matrix factors as lower-triangular times partial permutation times lower-triangular, so edge operators and address shears (H,D)↦(H+D,D) can be done in tape order at cost scaling with rank.
- `address-interchange`: Fast address-chunk interchange: Interchanging two disjoint address fields of u bits in an array of volume V in time O(V u^τ) with τ<1, via XOR combinations of intermediate data that finally give an exact permutation.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Applying the butterfly on the same bit position of up to d address chunks at once, on complex polynomial records, in time O(V d^λ') with λ'<1, instead of d whole-array passes.
- `multiplication-algorithm`: Assembly of the integer multiplication algorithm: The pipeline: digits, Chinese-remainder prime axes, Gaussian resampling, chirp convolution, phase twist to the ring modulo y^r+1, synthetic transforms with fast layers, then rescaling, rounding and carries.
- `main-result`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time with κ=2^-182, refuting the n log n optimality conjecture in this model.

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
