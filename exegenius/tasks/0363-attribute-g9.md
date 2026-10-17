# exegenius task 0363-attribute-g9

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

Split each n-bit input into q = ceiling(n/b) digits in radix 2^b, where b = ceiling(log2 n). Their product is the wrap-around product (the wiki's Cyclic convolution) of the two digit sequences, padded to a length S that is a product of distinct odd primes with T/2 < S < T, and no wrap-around occurs because the padded length is large enough. The sequence is then reindexed onto prime-length axes by a fixed reindexing map (the Chinese-remainder address map page). Each prime-length transform (the wiki's Discrete Fourier transform) is computed through a power-of-two transform, using a resampling identity with fixed linear contractions and phase multipliers (Gaussian resampling and Bluestein chirp identity), with the permutations kept inside the identity so none is executed as a sort. The stages in order are: radix digits; reindexing onto prime axes; two forward transforms of the two sequences; pointwise product of the transforms; one opposite transform; rescaling by S and by 2^(2b+4)S; rounding each entry to the nearest integer; undoing the reindexing; and carry propagation in radix 2^b, which outputs exactly 2n bits. The result is exact rather than approximate because all values are kept to p = 6b fractional bits and the accumulated error on each coefficient is below 1/2; the true coefficients are integers, so rounding returns them exactly, and carry propagation then gives the exact binary product. I am not fully sure of the constants: the wiki's exactness bound is stated only for digit widths b at least 2^24, and I did not see why the prime-length detour is needed.

Covers key points: 1, 2, 4

Quotations:

1. "The multiplication algorithm chains the reductions of the earlier pages to turn two $n$-bit integers into their exact $2n$-bit product."
2. "and the product is their convolution modulo $x^S-1$, as in [Multiplication as radix-digit convolution](vub)."
3. "Multiplication therefore reduces to a [Cyclic convolution](fam) of length $S$ on short integer coefficients."
4. "If the ordinary product has degree below $q$, nothing wraps and $f*g$ is the ordinary product."
5. "moving the data on tape by controlled shifts and axis reorderings only."
6. "A convolution is thus computed by two forward transforms, a pointwise product, one opposite transform, and a known rescaling."
7. "Gaussian resampling expresses a Discrete Fourier transform of length $s$, the source length, through one of a nearby larger length $t$ (a power of two there), so that only power-of-two transforms need a fast algorithm."
8. "The permuted transform is thus reduced to one [Cyclic convolution](fam) of length $T$ between two pointwise phase multiplications."
9. "The source permutation $R$ cancels"
10. "Multiply by $2^{2b+4}S$, round to the nearest integers"
11. "Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits."
12. "Exactness is shown by [Error tracking and exact recovery](mes): the error on these coefficients is below $1/2$, so rounding is exact."
13. "The true coefficients are integers, so error strictly below $1/2$ makes the nearest integer the unique correct coefficient."

### Answer 2

Each n-bit input is cut into q = ceil(n/b) radix-2^b digits, with b = ceil(log2 n), so the product is the wrapped product (the wiki's Cyclic convolution) of the two digit sequences. With a cyclic length S that is a product of distinct odd primes and satisfies T/2 < S < T, nothing wraps and every coefficient is below 2^{3b}. Stage 1: the index map Phi (page Chinese-remainder address map) moves this cyclic product onto a multi-axis array with prime axis lengths s_i. Stage 2: the two source transforms (the wiki's Discrete Fourier transforms) are computed through power-of-two transforms, using a resampling identity (Gaussian resampling) and chirp phases (Bluestein chirp identity), with the coordinate permutations left implicit so that none is executed. Stage 3: the two transforms are multiplied pointwise and truncated to p = 6b fractional bits, the opposite transform is applied, and the result is scaled by 2^{2b+4} S, rounded to the nearest integer, mapped back by Phi inverse, and carry-propagated in radix 2^b to give the exact 2n-bit product. Why it is exact: the page bounds the total error on each scaled coefficient by 448b 2^{gamma-b}, which is below 1/2 once gamma <= b/4; since the true coefficients are integers, rounding to the nearest integer recovers each one exactly. Confidence is moderate: I followed the stage order and checked the no-wraparound inequality, the coefficient bound, the two-point transform example, the chirp identity, and the final scaling arithmetic, but I took the component error bounds and the gamma <= b/4 step on the wiki's word.

Covers key points: 1, 2, 4

Quotations:

1. "Each input splits into $q=\lceil n/b\rceil$ radix-$2^b$ digits $a_j$, and the product is their convolution modulo $x^S-1$, as in [Multiplication as radix-digit convolution](vub)."
2. "so convolution modulo $x^S-1$ has no wraparound, and every coefficient $c_j\le q(2^b-1)^2<2^{3b}$."
3. "$S$ is the length of the Cyclic convolution, a product of distinct odd primes with $T/2<S<T$."
4. "Hence $\Phi$ is an isomorphism and preserves [Cyclic convolution](fam)."
5. "The source permutation $R$ cancels: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=u*v/S^2$."
6. "The permuted transform is thus reduced to one [Cyclic convolution](fam) of length $T$ between two pointwise phase multiplications."
7. "Multiply by $2^{2b+4}S$, round to the nearest integers, and apply $\Phi^{-1}$."
8. "Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits."
9. "Exactness is shown by [Error tracking and exact recovery](mes): the error on these coefficients is below $1/2$, so rounding is exact."
10. "448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\tfrac12"
11. "The true coefficients are integers, so error strictly below $1/2$ makes the nearest integer the unique correct coefficient."

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

Write the answer to `exegenius/tasks/0363-attribute-g9.answer.json`, then run `exegenius submit 0363-attribute-g9` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0363-attribute-g9`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
