# exegenius task 0002-background

Project directory: `/home/user/openai-nlogn-wiki/runs/C2` (paths below are relative to it)

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

- `big-o`: Big-O notation (known to the reader): Asymptotic upper-bound notation for running time.
- `polynomials`: Polynomials (known to the reader): Expressions in a variable with coefficients, added and multiplied termwise.
- `complex-numbers`: Complex numbers (known to the reader): Numbers a+bi with roots of unity and arithmetic.
- `multitape-tm`: Multitape Turing machine (known to the reader): Deterministic machine with finite alphabet and a fixed finite number of tapes, one cell read/written per tape per step.
- `multiplication-history`: Integer multiplication complexity and the n log n conjecture: Schönhage–Strassen gave O(n log n log log n) and conjectured n log n optimal; Harvey–van der Hoeven reached O(n log n).
- `convolution`: Convolution: Combining two coefficient sequences so each output sums products of entries whose indices add; this is polynomial multiplication.
- `dft-fft`: Discrete Fourier transform and butterflies: Evaluating a sequence at roots of unity, turning convolution into pointwise products, computed by log-depth layers of two-point butterfly operations.
- `digit-convolution-reduction`: Multiplication by radix-digit convolution: Split each integer into radix digits, convolve digit lists, then recover exact integer by rounding, rescaling and carry propagation.
- `cyclic-crt-axes`: Chinese-remainder map to prime cyclic axes: A Chinese-remainder address map placing the digit list on a product of cyclic axes of distinct prime lengths, preserving convolution.
- `multidim-transform`: Multidimensional transform: A Fourier transform on an array with several axes, applied along each axis in turn.
- `gaussian-resampling`: Gaussian resampling: Harvey–van der Hoeven identity expressing a Fourier transform of prime-length axes through a power-of-two tensor transform, with source and target permutations.
- `bluestein-chirp`: Bluestein chirp identity: Rewrites a Fourier transform of arbitrary length as a convolution multiplied by chirp phases.
- `poly-ring-negacyclic`: Polynomial ring modulo y^r + 1: Complex polynomials in y of degree below r with y^r = -1; powers of y act as roots of unity and multiplying by them is a signed shift of coefficients.
- `phase-twist`: Last-coordinate phase twist: Multiplying by diagonal phases so a cyclic coordinate becomes a negative-wrap (mod y^r+1) coordinate; removing the twist restores cyclic wrap.
- `synthetic-transforms`: Synthetic polynomial transforms: Nussbaumer-style transforms using powers of y as roots of unity so each twiddle multiplication is a shift.
- `normalized-ring-products`: Packed polynomial products: Pointwise polynomial products in the ring computed via signed packing (Kronecker substitution) and the standard O(n log n) multiplier as a subroutine.
- `tape-streams`: Tape scans and address layout: Arrays stored in address order on tapes; scans move data in linear time but rearranging address fields with growing digit counts is costly.
- `address-interchange-bottleneck`: Address rearrangement cost: Scanning Θ(n) bits at each of Θ(log n) levels costs n log n, so both movement and arithmetic must be cheapened.
- `linear-network-roles`: Linear networks, roles and frames: A fixed linear network exchanging two banks of values with signs and restoring auxiliary values; wires have roles and invertible frames D_v change the stored representation, cancelling across the network.
- `finite-subset-network`: Finite network from three-element subsets: Fixed network with nested subspaces attached to gates, built using three-element subsets and gather/scatter with cancelling auxiliary wires, giving s<Wm smaller calls.
- `recursive-saving`: Recursive saving giving a power of log: Calling parameter mf uses s<Wm calls at parameter f on volume V/W each, so cost per volume grows by factor s/W<m per multiplication of the parameter, giving a power saving.
- `address-shear-factorization`: Rational matrix shear and lower-triangular factorization: Every rational matrix factors as lower-triangular times partial permutation times lower-triangular, so an address shear (H,D)->(H+D,D) costs by rank.
- `controlled-shifts`: Controlled shifts and rational scalings: Linear-time stream operations adding control-field-dependent offsets to a target field.
- `packed-selected-bit-addition`: Packed selected-bit addition: Adds selected bit positions across grouped rectangles of packed records on tapes, used inside fast butterfly layers.
- `fast-address-interchange`: Fast address-field interchange: Interchanges two contiguous address fields via XOR combinations of data and address shears, with an exact final permutation.
- `fixed-point-dyadics`: Fixed-point complex dyadics: Complex numbers with power-of-two denominators used exactly in intermediate values and truncated once after a contractive layer.
- `fast-butterfly-layers`: Simultaneous butterfly layers: Applies H_0(u,v)=((u+v)/2,(u-v)/2) to selected coordinate bits of numerical arrays, via the linear network, at cost O(V d^λ').
- `precision-exact-recovery`: Precision analysis and exact recovery: Bounds the rounding error of the whole fixed-point pipeline strictly below 1/2, removes normalizations and propagates carries.
- `main-theorem`: Integer multiplication in O(n (lg n)^(1-κ)) time: Deterministic multitape TM multiplying n-bit integers in O(n(lg n)^{1-κ}), κ=2^{-182}, disproving the n log n conjecture in that model.

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
