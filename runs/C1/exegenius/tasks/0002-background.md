# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/C1` (paths below are relative to it)

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
- `polynomials`: Polynomials (known to the reader): Sums of powers of a variable with coefficients.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with i²=−1.
- `multitape-tm`: Multitape Turing machine (known to the reader): A deterministic Turing machine with a fixed finite alphabet and a fixed number of one-dimensional tapes.
- `nlogn-conjecture`: Schönhage–Strassen n log n conjecture: The 1971 conjecture that n log n is the optimal order of growth for multiplying n-bit integers.
- `dft-convolution`: Convolution and discrete Fourier transform: Convolution of coefficient lists is computed by transforming, multiplying pointwise and inverting the transform, using roots of unity.
- `radix-digit-convolution`: Multiplication as digit convolution: Splitting each input into radix digits turns the integer product into a convolution of short integer coefficients, followed by carry propagation.
- `tape-streams`: Elementary tape streams and scans: Array layouts on tapes with address fields, scans, controlled shifts and fixed rational scalings, each costing linear time in stored bit volume.
- `poly-ring-y-r-1`: Polynomial ring modulo y^r + 1: Polynomials in y with complex coefficients modulo y^r+1, where powers of y act as roots of unity and multiplication by them is a signed shift.
- `synthetic-transforms`: Synthetic polynomial transforms: Fourier-type transforms over the polynomial ring where roots of unity are powers of y, so root multiplications are signed shifts and the work is butterflies, shifts and address rearrangements.
- `gaussian-resampling`: Gaussian resampling: The Harvey–van der Hoeven identity expressing a transform of arbitrary axis length through a transform with power-of-two axis lengths.
- `crt-address-map`: Chinese-remainder address map: A map placing the coefficient list on a product of distinct prime cyclic axes that preserves convolution.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a transform as a normalized cyclic convolution via chirp phase factors.
- `signed-packing`: Signed packing (Kronecker substitution): Packing polynomial coefficients into one long integer with signs so ring products are computed by an ordinary O(n log n) integer multiplier.
- `fixed-point-precision`: Fixed-point precision and exact recovery: Complex fixed-point coefficients with dyadic intermediates, one truncation, and an error bound below 1/2 that allows exact rounding and carry propagation.
- `gate-frames`: Linear networks with frames and roles: A fixed linear network exchanging banks of values; roles are wire positions and an invertible frame operator per gate makes intermediate representations cancel.
- `finite-network-subspaces`: Finite networks with rank saving: Networks built from three-element subsets with nested subspaces so the number s of smaller calls satisfies s<Wm.
- `recursive-power-saving`: Recursive power saving: Recursive calls at parameter mf use s<Wm calls at parameter f on volume V/W each, giving cost per volume growth with an exponent below 1.
- `address-interchange`: Fast interchange of address chunks: Interchanges two address fields of u bits in cost O(V u^τ), τ<1, through XOR combinations whose final effect is an exact permutation.
- `fast-butterfly-layers`: Simultaneous butterfly layers: Applies H0(u,v)=((u+v)/2,(u−v)/2) simultaneously on selected address bits of d chunks at cost O(V d^λ'), λ'<1.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1−κ)) time: A fixed deterministic multitape Turing machine multiplies n-bit integers in O(n(lg n)^(1−κ)), κ=2^−182, disproving the n log n optimality conjecture in that model.

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
