# exegenius task 0351-grade-g6

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Grade answers to a question against its key points. Each answer was written by a different reader; grade each one on its own.

- For each answer, list the numbers of the key points it makes, correctly, in its own words or the key point's. Credit a key point only if the answer states it or clearly implies it; a vague gesture towards it does not count.
- List the numbers of the key points an answer contradicts: it states the opposite, or something incompatible. A key point an answer neither makes nor contradicts is missing; it needs no list.
- List any other claims in an answer that are wrong, briefly.
- An answer that says it cannot answer covers no key points.
- Grade what is written, not what the writer may have meant.

## Question

Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?

## Key points

1. Executing the permutations would mean sorting data on a tape, costing about t p log t per line, which would cancel the power saving.
2. The target permutation is absorbed by the chirp identity, because the chirp convolution already reads the permuted frequencies.
3. The source permutation is attached to both forward transforms and the opposite transform; dilating by a unit modulo s just permutes frequencies in the Fourier sum, so the opposite transform undoes it.
4. Pointwise products commute with applying the same permutation to both operands, so the product can be formed in permuted order and the permutation cancels, giving the plain convolution divided by S squared.

## Answers

### Answer A

Executing either permutation would be a sort, and the wiki treats sorting as the cost to avoid. The target permutation Q is not executed because, for even t_i and the chirp a, QF_t u = conj(a) . (a * (conj(a) . u)) / T, so Q is part of a convolution of length T that the algorithm computes anyway. The source permutation R is not executed because it cancels: F^+ R = R^{-1} F^+ gives R F^+ R = F^+. The R in the opposite transform and the R carried by the two forward transforms (through their pointwise product) cancel, and the convolution rule then returns u*v/S^2. So neither permutation needs a reordering step: the target one only changes which frequency is read inside a chirp convolution, and the source one cancels by the identity. The pages assert that the usual implementation sorts, but they do not explain what a sort costs on the tape machine, so the reason avoidance matters rests on that unexplained cost.

### Answer B

The algorithm computes a prime-length transform F_s from power-of-two transforms F_t, and the identity that does this (Gaussian resampling, page roz) has the coordinate reindexings P_s and P_t inside it. The wiki says these reindexings are never run as sorts, and the pages I read do not spell out why a sort would be costly on the tape machine; they only say the usual implementation sorts twice on each coordinate, and that the cost accounting charges chunk exchanges. The target permutation Q disappears because the Bluestein chirp identity identity writes QF_t u as two pointwise chirp phases around one convolution of length T, and a convolution is computed by transforms and pointwise products, so Q is just part of a convolution and is never executed. The source permutation R disappears because each t_i is a unit modulo s_i, so R acts as a unit-multiplier reindexing R_beta on each axis, and F^+ R_beta = R_beta^{-1} F^+ (Retained permutation cancellation, page zom). In (R F_s^+)[(R F_s u)(R F_s v)] the permutation R commutes with the pointwise product, so the expression becomes F_s^+ (F_s u . F_s v) with the two R factors gone, and the inverse-transform identity gives u*v/S^2. No sort is needed because the reindexing is absorbed algebraically (into a convolution for Q, and by commuting with the opposite transform for R), not executed. Confidence is moderate: I followed the algebra of the identities on pages zom, pap and roz, but I could not verify the cost reasons for avoiding sorts, and the key chirp and resampling identities are imported from cited literature.

### Answer C

The background does not cover this. The question depends on the terms Gaussian resampling and Discrete Fourier transforms, which are not defined anywhere in my background, so I cannot tell what they stand for. It also depends on coordinate permutations inside transform identities and on power-of-two transforms, which need the discrete Fourier transform or FFT. My background says I have not been taught the DFT or FFT as such, and I have not studied tensor products or the literature on fast integer multiplication, which the permutation and transform-identity reasoning would rely on. I can say only that polynomials, complex numbers, and divide and conquer are familiar to me, but that is not enough to explain why the permutations stay inside the identities or why the source and target permutations vanish without sorting.

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

Write the answer to `exegenius/tasks/0351-grade-g6.answer.json`, then run `exegenius submit 0351-grade-g6` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0351-grade-g6`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
