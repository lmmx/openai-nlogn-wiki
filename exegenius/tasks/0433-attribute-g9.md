# exegenius task 0433-attribute-g9

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Say which quotation supports each key point a reader's answer makes. Each answer below was graded already: the key points it covers are listed under it, with the quotations the reader gave from the pages they read.

- For each answer, and each key point listed as covered, give the number of the quotation that supports it: the one the point rests on, not merely one on the same subject.
- If no quotation supports a covered key point, leave that key point out.
- Do not regrade: judge only the support for the key points listed.

## Question

Summarise in a few sentences how the algorithm turns two n-bit integers into their exact product, naming the main stages in order and saying why the final answer is exact rather than approximate.

## Key points

1. The inputs are cut into digits of about log n bits, so the product becomes a cyclic convolution of short integer coefficients. The length is chosen so that nothing wraps around.
2. A Chinese-remainder re-addressing places this length-S convolution on several axes of pairwise coprime prime lengths, and Gaussian resampling plus chirp identities express the prime-length Fourier transforms through power-of-two transforms, with the awkward coordinate permutations kept inside the identities and never executed.
3. The convolution is carried out by two forward transforms, a pointwise product and an opposite transform, using synthetic polynomial transforms over y^r+1 whose twiddle factors are cheap signed shifts. A phase twist converts the last cyclic axis to that ring.
4. After rescaling, the accumulated rounding error on each coefficient is below 1/2 because the working precision has spare bits. Rounding therefore gives the exact integer coefficients, and carry propagation produces the exact 2n-bit product.

## Answers

### Answer 1

Split each n-bit input into q = ceil(n/b) digits in radix 2^b, with b = ceil(log2 n). Viewing the product of the two digit sequences as a Cyclic convolution of a chosen length S (between T/2 and T, with T a power of two near 4n/b to 8n/b) means nothing wraps around, and every coefficient is a non-negative integer of at most 3b bits. Next, the Chinese-remainder address map map, a triangular set of controlled shifts, rewrites that length-S Cyclic convolution as one over several axes of pairwise coprime prime lengths. Each prime-length Discrete Fourier transform is then computed from power-of-two Discrete Fourier transforms by the Gaussian resampling identity (resampling plus a Bluestein chirp identity phase-convolution-phase identity), with the target permutation absorbed into the identity and the source permutation cancelling across the transforms, so no sort is executed. The two scaled digit arrays are transformed forward, multiplied pointwise, sent through the opposite transform, rescaled, and each coefficient is rounded to the nearest integer; the Chinese-remainder address map map is then undone. Finally carries are propagated in radix 2^b to write the exact 2n-bit product. The answer is exact rather than approximate because every stored value keeps p = 6b fractional bits and the accumulated error on each recovered coefficient is below 1/2; since the true coefficients are integers, rounding returns each one exactly, and carry propagation then gives the exact binary number. Confidence: the stages and the exactness argument agree across the pages I opened, but I did not re-derive the numeric constants and I did not open the pages for the synthetic transform, ring convolution, parameter choice or cost accounting that the error bounds cite.

Covers key points: 1, 2, 4

Quotations:

1. "Splitting each input into digits in a large power-of-two radix turns the integer product into a convolution of short integer sequences"
2. "Each digit polynomial has degree at most $q-1$, so the product polynomial has degree at most $2q-2$."
3. "So every coefficient is a nonnegative integer of at most $3b$ bits."
4. "$p=6b$ fractional bits for every stored value"
5. "The Chinese-remainder address map rewrites one Cyclic convolution of length $S$ as a convolution on several short axes of pairwise coprime lengths"
6. "Gaussian resampling expresses the Discrete Fourier transform of a source length $s$ through the transform of a nearby larger power-of-two length $t$, so that only power-of-two transforms need a fast algorithm."
7. "The identity converts the transform together with $Q$ into a Cyclic convolution, so $Q$ never has to be executed as a sort."
8. "because Fourier-type transforms turn it into pointwise multiplication"
9. "Cyclic convolution is the product of two sequences whose indices wrap around"
10. "Multiply corresponding coefficients exactly and truncate toward zero to $p$ fractional bits, obtaining the array $z$."
11. "Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits."
12. "Error tracking and exact recovery shows that the computed convolution coefficients lie within $1/2$ of the true integers, so rounding recovers them."
13. "The true coefficients are integers, so error strictly below $1/2$ makes the nearest integer the unique correct coefficient."

### Answer 2

Each n-bit integer is cut into q = ceil(n/b) digits in radix 2^b, with b = ceil(log2 n), so the product of the two digit polynomials has coefficients c_j that are integers below 2^(3b). A Cyclic convolution of length S, with T/2 < S < T, has no wraparound for this product, so it returns the c_j exactly. Next, the isomorphism Phi (Chinese-remainder address map) rewrites the length-S Cyclic convolution as a Cyclic convolution over short axes of distinct prime lengths. Each prime-length transform is then computed through a nearby power-of-two transform, sandwiched between resampling maps and chirp phases, with the permutations left implicit (Gaussian resampling, Bluestein chirp identity, Multidimensional transforms). The scaled digit arrays of the two inputs are transformed, multiplied pointwise and truncated to p = 6b fractional bits, inverse-transformed, rescaled by S, and then multiplied by 2^(2b+4) S and rounded to the nearest integers. Phi^-1 removes the padding, and carry propagation turns the coefficients into the 2n output bits. The result is exact rather than approximate because the total computed error on each coefficient is below 1/2 (Error tracking and exact recovery), so rounding returns the true integer c_j. The carry step is exact integer arithmetic.

Covers key points: 1, 2, 4

Quotations:

1. "Key idea: the product is a [Cyclic convolution](fam) of short integer coefficients; a [Discrete Fourier transform](kur) turns it into pointwise multiplication; prime-length transforms are computed through power-of-two ones by resampling and chirps; and the total error stays below $1/2$, so rounding recovers exact integers."
2. "Evaluating them at $x=2^b$ returns $u$ and $u'$, so $uu'$ is the value at $2^b$ of their product."
3. "So every coefficient is a nonnegative integer of at most $3b$ bits."
4. "The reason for the split is that a transform of length $S$ has no power-of-two structure, while over coprime axes it becomes a product of short one-axis transforms, each treated separately."
5. "Gaussian resampling expresses the Discrete Fourier transform of a source length $s$ through the transform of a nearby larger power-of-two length $t$, so that only power-of-two transforms need a fast algorithm."
6. "The permuted transform is thus reduced to one [Cyclic convolution](fam) of length $T$ between two pointwise phase multiplications."
7. "A multidimensional transform is the Discrete Fourier transform of an array with several coordinates, computed by transforming along one axis at a time"
8. "A convolution is thus two forward transforms, a pointwise product, an opposite transform and a rescaling."
9. "Multiply by $2^{2b+4}S$, round to the nearest integers"
10. "Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits."
11. "Error tracking and exact recovery shows that the computed convolution coefficients lie within $1/2$ of the true integers, so rounding recovers them."
12. "The true coefficients are integers, so error strictly below $1/2$ makes the nearest integer the unique correct coefficient."
13. "The product is below $2^{2n}$, so all bits above position $2n-1$ are zero and exactly $2n$ bits are output."
14. "Rounding at every step would add one such error per step; here there is one per layer."

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Attribution": {
      "additionalProperties": false,
      "properties": {
        "answer": {
          "description": "Number of the answer, as listed.",
          "format": "uint",
          "minimum": 0,
          "type": "integer"
        },
        "support": {
          "items": {
            "$ref": "#/$defs/Support"
          },
          "type": "array"
        }
      },
      "required": [
        "answer",
        "support"
      ],
      "type": "object"
    },
    "Support": {
      "additionalProperties": false,
      "description": "The quotation that supports one covered key point.",
      "properties": {
        "point": {
          "description": "Number of the key point.",
          "format": "uint",
          "minimum": 0,
          "type": "integer"
        },
        "quotation": {
          "description": "Number of the quotation under the answer.",
          "format": "uint",
          "minimum": 0,
          "type": "integer"
        }
      },
      "required": [
        "point",
        "quotation"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "answers": {
      "description": "One entry for every answer listed.",
      "items": {
        "$ref": "#/$defs/Attribution"
      },
      "type": "array"
    }
  },
  "required": [
    "answers"
  ],
  "title": "AttributeAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0433-attribute-g9.answer.json`, then run `exegenius submit 0433-attribute-g9` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0433-attribute-g9`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
