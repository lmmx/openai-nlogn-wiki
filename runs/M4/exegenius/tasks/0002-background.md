# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/M4` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper bound on growth of running time.
- `polynomials`: Polynomials (known to the reader): Sums of coefficients times powers of a variable.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with real and imaginary parts.
- `turing-machine`: Multitape Turing machine (known to the reader): A finite-state machine with several one-dimensional tapes.
- `convolution`: Convolution: Combining two coefficient lists so that entry k sums products of entries whose indices add to k (cyclically for cyclic convolution); equivalent to polynomial multiplication.
- `fourier-transform`: Discrete Fourier transform: Evaluation of a coefficient list at roots of unity, which turns convolution into pointwise multiplication.
- `nlogn-conjecture`: The n log n optimality conjecture and prior bounds: Schönhage and Strassen proposed n log n as the optimal multiplication time; Harvey and van der Hoeven reached O(n log n) in the multitape model.
- `radix-digit-reduction`: Reduction of integer multiplication to convolution: Split each integer into short radix digits so the product becomes a convolution of digit lists, followed by carry propagation.
- `crt-prime-axes`: Chinese-remainder map to prime cyclic axes: Index re-mapping that turns a long cyclic convolution into a multidimensional one over axes of distinct prime lengths.
- `gaussian-resampling`: Gaussian resampling: Expresses a Fourier transform of prime length through a multidimensional transform with power-of-two axis lengths.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a Fourier transform as a convolution with a chirp (quadratic-phase) sequence.
- `polynomial-ring-y-r`: Polynomial ring modulo y^r + 1: Polynomials in y with complex coefficients where y^r is identified with −1, so powers of y act as roots of unity and multiplying by one is a signed cyclic shift.
- `phase-twist`: Phase twist to the negacyclic ring: A diagonal phase multiplication turning the last cyclic coordinate into a polynomial modulo y^r+1, whose negative wrap yields the original cyclic wrap once the twist is removed.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring using powers of y as roots of unity, built from signed shifts and two-point butterflies.
- `butterfly-h0`: Butterfly map H_0: The two-point map (u,v) ↦ ((u+v)/2, (u−v)/2), the basic arithmetic step of a transform layer.
- `signed-packing`: Signed packing of polynomial products: Packing coefficients into long integers with signs so a polynomial product is computed by an ordinary O(n log n) integer multiplier.
- `linear-network-frames`: Linear networks with roles and frames: A fixed linear network exchanging two banks of values and restoring auxiliary values, applied pointwise on role arrays under invertible frame operators that cancel along routes to leave an endpoint operator.
- `subset-network`: Finite network from three-element subsets: A network labelled by nested subspaces built from three-element subset intersections, whose number s of smaller calls is less than W·m.
- `recursive-power-saving`: Recursive power saving: A recursive call at parameter m·f using s<W·m calls at parameter f on volume V/W makes the cost per volume grow as a power less than linear in the parameter.
- `address-interchange`: Fast interchange of address chunks: Exchanging two address fields of u bits by XOR-combinations (address shears) at cost O(V u^τ) with τ<1, though the final effect is an exact permutation.
- `fast-butterfly-layers`: Fast simultaneous butterfly layers: Applying the butterfly map to the same bit of up to d address chunks at once on numerical arrays, at cost O(V d^λ') with λ'<1.
- `exact-recovery`: Precision and exact recovery of the product: Fixed-point arithmetic with controlled error: removing known normalizations leaves coefficient error below 1/2, so rounding and carry propagation give the exact binary product.
- `main-multiplication`: Integer multiplication in O(n (lg n)^(1−κ)) time: A deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)) time, κ=2^−182, via radix digits, Chinese-remainder axes, Gaussian resampling, chirps, the twist to the polynomial ring, synthetic transforms accelerated by fast address interchange and butterfly layers, then exact recovery.
- `elementary-streams`: Elementary stream operations and controlled shifts: Linear-time tape scans that permute, move, split and merge digit streams, and add controlled offsets modulo a prime power.
- `matrix-shear`: Rational matrix shear and triangular factorization: The address map (H,D) ↦ (H+AD,D) for a rational matrix A is performed via a factorization A=E1ΠE2 into lower-triangular factors and a partial permutation, at cost depending on the rank of A.

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
