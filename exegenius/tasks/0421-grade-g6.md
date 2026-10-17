# exegenius task 0421-grade-g6

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

Executing a permutation of records on a tape costs a logarithmic factor beyond a linear pass (about tp log t per line for the length-t transform). Across all lines that would cancel the power-of-log saving the page is after, so the permutations are kept as index relabellings inside identities the algorithm uses anyway. The target permutation Q is never executed because the Bluestein chirp identity identity QF_t u = conj(a) . (a * (conj(a) . u)) / T rewrites the relabelled transform as two chirp phase multiplications around one Cyclic convolution (the wiki's name for the wrapped product of sequences) of length T; the relabelling becomes part of a convolution that is performed anyway. The source permutation R is never executed because it commutes with pointwise products (a permutation of a pointwise product is the pointwise product of the permutations), and the same R appears on both forward transforms and in front of the opposite transform. The identity R F^+ R = F^+ holds because multiplying indices by a unit t and then by its inverse just relabels the summation index, so (R F^+)[(R F u) . (R F v)] = u*v / S^2 with no R left to execute. The convolution is therefore computed without any sort.

### Answer B

Gaussian resampling rewrites a Discrete Fourier transform of prime length s as a Discrete Fourier transform of a larger power-of-two length t, wrapped in two contractions A and B_0, with P_sF_s = 2^{2\alpha^2} B_0 P_t F_t A (roz). The permutations P_s and P_t are not executed because executing one is a sort of records on a tape, which costs about tp log t and would cancel the power saving (roz). Instead they are removed by two different cancellations. (1) The target permutation Q is absorbed by the chirp identity QF_t u = conj(a) . (a * (conj(a) . u))/T, with a_j = exp(-pi i sum s_i j_i^2 / t_i) (pap). This rewrites Q F_t as two pointwise phase multiplications around one Cyclic convolution of length T. Since the integer product needs a Cyclic convolution anyway, Q becomes part of that formula and no step reorders the array (zom). (2) The source permutation R appears in both forward transforms and in the opposite transform. Each t_i is a unit modulo s_i, so R F^+ R = F^+ (zom), and a permutation commutes with pointwise products (zom). Hence (R F^+)[(R F u) . (R F v)] = F^+(F u . F v) = u*v/S^2, with no R executed (zom). The one-axis identity that Gaussian resampling rests on is imported from another paper and is not proved in the wiki (roz). I did not verify the error bounds or the full integer chain on the multiplication page, so the answer depends on those being correct.

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

Write the answer to `exegenius/tasks/0421-grade-g6.answer.json`, then run `exegenius submit 0421-grade-g6` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0421-grade-g6`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
