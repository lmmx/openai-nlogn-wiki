# exegenius task 0354-grade-g9

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

Split each n-bit input into q = ceiling(n/b) digits in radix 2^b, where b = ceiling(log2 n). Their product is the wrap-around product (the wiki's Cyclic convolution) of the two digit sequences, padded to a length S that is a product of distinct odd primes with T/2 < S < T, and no wrap-around occurs because the padded length is large enough. The sequence is then reindexed onto prime-length axes by a fixed reindexing map (the Chinese-remainder address map page). Each prime-length transform (the wiki's Discrete Fourier transform) is computed through a power-of-two transform, using a resampling identity with fixed linear contractions and phase multipliers (Gaussian resampling and Bluestein chirp identity), with the permutations kept inside the identity so none is executed as a sort. The stages in order are: radix digits; reindexing onto prime axes; two forward transforms of the two sequences; pointwise product of the transforms; one opposite transform; rescaling by S and by 2^(2b+4)S; rounding each entry to the nearest integer; undoing the reindexing; and carry propagation in radix 2^b, which outputs exactly 2n bits. The result is exact rather than approximate because all values are kept to p = 6b fractional bits and the accumulated error on each coefficient is below 1/2; the true coefficients are integers, so rounding returns them exactly, and carry propagation then gives the exact binary product. I am not fully sure of the constants: the wiki's exactness bound is stated only for digit widths b at least 2^24, and I did not see why the prime-length detour is needed.

### Answer B

Each n-bit input is cut into q = ceil(n/b) radix-2^b digits, with b = ceil(log2 n), so the product is the wrapped product (the wiki's Cyclic convolution) of the two digit sequences. With a cyclic length S that is a product of distinct odd primes and satisfies T/2 < S < T, nothing wraps and every coefficient is below 2^{3b}. Stage 1: the index map Phi (page Chinese-remainder address map) moves this cyclic product onto a multi-axis array with prime axis lengths s_i. Stage 2: the two source transforms (the wiki's Discrete Fourier transforms) are computed through power-of-two transforms, using a resampling identity (Gaussian resampling) and chirp phases (Bluestein chirp identity), with the coordinate permutations left implicit so that none is executed. Stage 3: the two transforms are multiplied pointwise and truncated to p = 6b fractional bits, the opposite transform is applied, and the result is scaled by 2^{2b+4} S, rounded to the nearest integer, mapped back by Phi inverse, and carry-propagated in radix 2^b to give the exact 2n-bit product. Why it is exact: the page bounds the total error on each scaled coefficient by 448b 2^{gamma-b}, which is below 1/2 once gamma <= b/4; since the true coefficients are integers, rounding to the nearest integer recovers each one exactly. Confidence is moderate: I followed the stage order and checked the no-wraparound inequality, the coefficient bound, the two-point transform example, the chirp identity, and the final scaling arithmetic, but I took the component error bounds and the gamma <= b/4 step on the wiki's word.

### Answer C

The background does not cover this question. The reader knows Karatsuba multiplication and polynomials, and can see that an integer written in a base is a polynomial in that base, so multiplying two integers resembles multiplying two polynomials. But the reader has not been taught the discrete Fourier transform or FFT, the specific literature on fast integer multiplication, or numerical error analysis. The algorithm the question asks about, its stages, and the reason its output is exact rather than approximate all depend on those topics, so the reader cannot name the stages in order or justify exactness from this background without guessing.

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

Write the answer to `exegenius/tasks/0354-grade-g9.answer.json`, then run `exegenius submit 0354-grade-g9` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0354-grade-g9`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
