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

- `big-o-notation`: Big-O notation (known to the reader): A way of stating that a function grows no faster than a constant multiple of another function, beyond some input size.
- `complex-numbers`: Complex numbers (known to the reader): Numbers of the form a + bi with real a and b and imaginary unit i, with the usual addition and multiplication.
- `polynomials`: Polynomials (known to the reader): Finite sums of constant multiples of powers of a variable, with coefficients drawn from a number system.
- `turing-machine`: Multitape Turing machine (known to the reader): An abstract machine with a finite control and a fixed number of tapes, each with its own head that reads and writes one cell per step.
- `linear-algebra`: Linear algebra over a field: The theory of vector spaces, linear maps, invertible operators, subspaces, and the rank of a linear map.
- `conjecture-n-log-n`: Schönhage–Strassen optimality conjecture: The conjecture of Schönhage and Strassen that n log n is the optimal order of growth of the cost of multiplying two n-bit integers on a multitape Turing machine.
- `integer-multiplication-problem`: Exact integer multiplication: The task of computing the exact 2n-bit binary representation of the product of two n-bit binary integers given as input.
- `fixed-tape-machine`: Fixed-tape machine model: A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, where a step moves each head by at most one cell.
- `fast-multiplier`: Established fast multiplier: The known deterministic multitape algorithm that multiplies two n-bit integers in O(n log n) time, used here as a black-box subroutine.
- `radix-convolution`: Multiplication as digit convolution: The reduction of integer multiplication to the convolution of the coefficient lists of the integers written in a fixed radix.
- `cyclic-convolution`: Cyclic convolution: The product of two coefficient sequences in which indices wrap around modulo a fixed length.
- `roots-of-unity`: Roots of unity: Complex numbers z with z^m = 1 for some positive integer m, whose powers cycle through a finite set.
- `dft`: Discrete Fourier transform: The linear map that sends a sequence of n complex numbers to its values at the n-th roots of unity, weighted by powers of a root of unity.
- `gaussian-dyadic`: Gaussian dyadic number: A complex number whose real and imaginary parts are both dyadic rationals, meaning fractions with power-of-two denominators.
- `butterfly`: Two-point butterfly: The map (u, v) to ((u+v)/2, (u-v)/2) applied to a pair of values, the basic step of a radix-two Fourier transform.
- `multidim-transform`: Multidimensional power-of-two transform: A Fourier-type transform over an array whose axis lengths are all powers of two, which replaces a one-dimensional transform of other lengths.
- `gaussian-resampling`: Gaussian resampling: The identity of Harvey and van der Hoeven that rewrites a Fourier transform of one length as a transform over power-of-two axes, with Gaussian weights.
- `negacyclic-ring`: Negacyclic polynomial ring: The ring of polynomials with complex coefficients reduced modulo y^r + 1, where y^r is identified with -1.
- `synthetic-transform`: Synthetic polynomial transform: A transform whose roots of unity are powers of a polynomial variable, so that multiplying by a root is a signed cyclic shift of a coefficient list.
- `chirp`: Bluestein chirp identity: Bluestein's identity that turns a Fourier transform into a convolution by multiplying with chirp factors before and after.
- `phase-twist`: Last-coordinate phase twist: A multiplication of the last cyclic coordinate by a root-of-unity phase, which turns the cyclic wrap into the negacyclic wrap of the polynomial ring.
- `signed-packing`: Signed coefficient packing: The encoding of a polynomial with signed coefficients as a single integer by evaluating it at a large power of two, so that polynomial products become integer products.
- `crt-map`: Chinese-remainder address map: The map that places a coefficient list on a product of distinct prime cyclic axes so that convolution is preserved.
- `linear-network`: Linear network that restores auxiliary values: A fixed network of linear gates that exchanges two banks of values with prescribed signs and returns every auxiliary value to its starting state.
- `frame`: Frame of a network vertex: An invertible linear operator attached to a vertex of a linear network that changes how the array stored on each wire is represented.
- `scratch-restoration`: Scratch-register restoration: The technique of subtracting an initial register value, computing, adding the result, and reversing the computation so that scratch registers return to their arbitrary starting contents.
- `subset-network`: Subset-intersection network: A linear network whose subspace labels come from intersection sizes of three-element subsets, so that the total number of smaller calls is less than the number of wires times the dimension.
- `address-interchange`: Fast address interchange: A tape procedure that swaps two equal-width address fields in an array by computing XOR combinations of intermediate data, at cost proportional to the volume times a power of the field width.
- `rank-saving`: Rank-saving recursion: The recursive construction in which the number of smaller calls is less than the wire count times the parameter, which gives a strict power saving in each level of the recursion.
- `cost-recurrence`: Volume-normalized cost recurrence: The recurrence obtained by dividing a procedure's cost by its stored volume, which shows that the recursive contribution shrinks by a fixed factor at each level.
- `butterfly-layer`: Simultaneous butterfly layer: A single tape procedure that applies the two-point butterfly to the same selected bit position in several equal-width address chunks at once, at cost sublinear in the number of chunks.
- `exact-recovery`: Exact recovery by rounding: The step that rounds the approximate convolution coefficients to integers, after the known normalizations are removed, and shows that each error is below one half.
- `main-theorem`: Deterministic fixed-tape sub-quasilinear multiplication: A deterministic fixed-tape multitape Turing machine that multiplies two n-bit integers exactly in O(n (lg n)^(1-kappa)) time with kappa = 2^(-182), which disproves the n log n optimality conjecture in this model.

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
