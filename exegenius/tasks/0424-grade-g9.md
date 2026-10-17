# exegenius task 0424-grade-g9

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Grade answers to a question against its key points. Each answer was written by a different reader; grade each one on its own.

- For each answer, list the numbers of the key points it makes, correctly, in its own words or the key point's. Credit a key point only if the answer states it or clearly implies it; a vague gesture towards it does not count.
- List the numbers of the key points an answer contradicts: it states the opposite, or something incompatible. A key point an answer neither makes nor contradicts is missing; it needs no list.
- List any other claims in an answer that are wrong, briefly.
- An answer that says it cannot answer covers no key points.
- Grade what is written, not what the writer may have meant.

## Question

Summarise in a few sentences how the algorithm turns two n-bit integers into their exact product, naming the main stages in order and saying why the final answer is exact rather than approximate.

## Key points

1. The inputs are cut into digits of about log n bits, so the product becomes a cyclic convolution of short integer coefficients. The length is chosen so that nothing wraps around.
2. A Chinese-remainder re-addressing places this length-S convolution on several axes of pairwise coprime prime lengths, and Gaussian resampling plus chirp identities express the prime-length Fourier transforms through power-of-two transforms, with the awkward coordinate permutations kept inside the identities and never executed.
3. The convolution is carried out by two forward transforms, a pointwise product and an opposite transform, using synthetic polynomial transforms over y^r+1 whose twiddle factors are cheap signed shifts. A phase twist converts the last cyclic axis to that ring.
4. After rescaling, the accumulated rounding error on each coefficient is below 1/2 because the working precision has spare bits. Rounding therefore gives the exact integer coefficients, and carry propagation produces the exact 2n-bit product.

## Answers

### Answer A

Split each n-bit input into q = ceil(n/b) digits in radix 2^b, with b = ceil(log2 n). Viewing the product of the two digit sequences as a Cyclic convolution of a chosen length S (between T/2 and T, with T a power of two near 4n/b to 8n/b) means nothing wraps around, and every coefficient is a non-negative integer of at most 3b bits. Next, the Chinese-remainder address map map, a triangular set of controlled shifts, rewrites that length-S Cyclic convolution as one over several axes of pairwise coprime prime lengths. Each prime-length Discrete Fourier transform is then computed from power-of-two Discrete Fourier transforms by the Gaussian resampling identity (resampling plus a Bluestein chirp identity phase-convolution-phase identity), with the target permutation absorbed into the identity and the source permutation cancelling across the transforms, so no sort is executed. The two scaled digit arrays are transformed forward, multiplied pointwise, sent through the opposite transform, rescaled, and each coefficient is rounded to the nearest integer; the Chinese-remainder address map map is then undone. Finally carries are propagated in radix 2^b to write the exact 2n-bit product. The answer is exact rather than approximate because every stored value keeps p = 6b fractional bits and the accumulated error on each recovered coefficient is below 1/2; since the true coefficients are integers, rounding returns each one exactly, and carry propagation then gives the exact binary number. Confidence: the stages and the exactness argument agree across the pages I opened, but I did not re-derive the numeric constants and I did not open the pages for the synthetic transform, ring convolution, parameter choice or cost accounting that the error bounds cite.

### Answer B

Each n-bit integer is cut into q = ceil(n/b) digits in radix 2^b, with b = ceil(log2 n), so the product of the two digit polynomials has coefficients c_j that are integers below 2^(3b). A Cyclic convolution of length S, with T/2 < S < T, has no wraparound for this product, so it returns the c_j exactly. Next, the isomorphism Phi (Chinese-remainder address map) rewrites the length-S Cyclic convolution as a Cyclic convolution over short axes of distinct prime lengths. Each prime-length transform is then computed through a nearby power-of-two transform, sandwiched between resampling maps and chirp phases, with the permutations left implicit (Gaussian resampling, Bluestein chirp identity, Multidimensional transforms). The scaled digit arrays of the two inputs are transformed, multiplied pointwise and truncated to p = 6b fractional bits, inverse-transformed, rescaled by S, and then multiplied by 2^(2b+4) S and rounded to the nearest integers. Phi^-1 removes the padding, and carry propagation turns the coefficients into the 2n output bits. The result is exact rather than approximate because the total computed error on each coefficient is below 1/2 (Error tracking and exact recovery), so rounding returns the true integer c_j. The carry step is exact integer arithmetic.

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Grade": {
      "additionalProperties": false,
      "properties": {
        "contradicted": {
          "description": "Numbers of the key points the answer contradicts.",
          "items": {
            "format": "uint",
            "minimum": 0,
            "type": "integer"
          },
          "type": "array"
        },
        "covered": {
          "description": "Numbers of the key points the answer makes.",
          "items": {
            "format": "uint",
            "minimum": 0,
            "type": "integer"
          },
          "type": "array"
        },
        "label": {
          "description": "The answer's letter.",
          "type": "string"
        },
        "wrong": {
          "description": "Wrong claims in the answer that contradict no key point.",
          "items": {
            "type": "string"
          },
          "type": "array"
        }
      },
      "required": [
        "label",
        "covered",
        "contradicted",
        "wrong"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "grades": {
      "items": {
        "$ref": "#/$defs/Grade"
      },
      "type": "array"
    }
  },
  "required": [
    "grades"
  ],
  "title": "GradeAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0424-grade-g9.answer.json`, then run `exegenius submit 0424-grade-g9` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0424-grade-g9`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
