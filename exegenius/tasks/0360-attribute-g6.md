# exegenius task 0360-attribute-g6

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Say which quotation supports each key point a reader's answer makes. Each answer below was graded already: the key points it covers are listed under it, with the quotations the reader gave from the pages they read.

- For each answer, and each key point listed as covered, give the number of the quotation that supports it: the one the point rests on, not merely one on the same subject.
- If no quotation supports a covered key point, leave that key point out.
- Do not regrade: judge only the support for the key points listed.

## Question

Gaussian resampling is used so that Fourier transforms of prime length can be done with power-of-two transforms. Why does the algorithm leave the coordinate permutations inside the transform identities instead of executing them, and why do the source permutation and the target permutation both disappear without any sorting?

## Key points

1. Executing the permutations would mean sorting data on a tape, costing about t p log t per line, which would cancel the power saving.
2. The target permutation is absorbed by the chirp identity, because the chirp convolution already reads the permuted frequencies.
3. The source permutation is attached to both forward transforms and the opposite transform; dilating by a unit modulo s just permutes frequencies in the Fourier sum, so the opposite transform undoes it.
4. Pointwise products commute with applying the same permutation to both operands, so the product can be formed in permuted order and the permutation cancels, giving the plain convolution divided by S squared.

## Answers

### Answer 1

Executing either permutation would be a sort, and the wiki treats sorting as the cost to avoid. The target permutation Q is not executed because, for even t_i and the chirp a, QF_t u = conj(a) . (a * (conj(a) . u)) / T, so Q is part of a convolution of length T that the algorithm computes anyway. The source permutation R is not executed because it cancels: F^+ R = R^{-1} F^+ gives R F^+ R = F^+. The R in the opposite transform and the R carried by the two forward transforms (through their pointwise product) cancel, and the convolution rule then returns u*v/S^2. So neither permutation needs a reordering step: the target one only changes which frequency is read inside a chirp convolution, and the source one cancels by the identity. The pages assert that the usual implementation sorts, but they do not explain what a sort costs on the tape machine, so the reason avoidance matters rests on that unexplained cost.

Covers key points: 2, 3

Quotations:

1. "the permutations of Gaussian resampling stay inside the transform identity, where one is absorbed by a convolution and the other cancels."
2. "So $Q$ is part of a convolution of length $T$ and never executed."
3. "Hence $F_q^+R_\beta=R_\beta^{-1}F_q^+$."
4. "so tensoring gives $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$"
5. "which stay in the identity, never executed as sorts."
6. "The permutation needs no separate step: it only changes which frequency is read"
7. "A convolution is thus computed by two forward transforms, a pointwise product, one opposite transform, and a known rescaling."

### Answer 2

The algorithm computes a prime-length transform F_s from power-of-two transforms F_t, and the identity that does this (Gaussian resampling, page roz) has the coordinate reindexings P_s and P_t inside it. The wiki says these reindexings are never run as sorts, and the pages I read do not spell out why a sort would be costly on the tape machine; they only say the usual implementation sorts twice on each coordinate, and that the cost accounting charges chunk exchanges. The target permutation Q disappears because the Bluestein chirp identity identity writes QF_t u as two pointwise chirp phases around one convolution of length T, and a convolution is computed by transforms and pointwise products, so Q is just part of a convolution and is never executed. The source permutation R disappears because each t_i is a unit modulo s_i, so R acts as a unit-multiplier reindexing R_beta on each axis, and F^+ R_beta = R_beta^{-1} F^+ (Retained permutation cancellation, page zom). In (R F_s^+)[(R F_s u)(R F_s v)] the permutation R commutes with the pointwise product, so the expression becomes F_s^+ (F_s u . F_s v) with the two R factors gone, and the inverse-transform identity gives u*v/S^2. No sort is needed because the reindexing is absorbed algebraically (into a convolution for Q, and by commuting with the opposite transform for R), not executed. Confidence is moderate: I followed the algebra of the identities on pages zom, pap and roz, but I could not verify the cost reasons for avoiding sorts, and the key chirp and resampling identities are imported from cited literature.

Covers key points: 2, 3, 4

Quotations:

1. "the permutations of Gaussian resampling stay inside the transform identity, where one is absorbed by a convolution and the other cancels"
2. "Each $t_i$ is a unit modulo $s_i$, and $R$ applies $R_{t_i}$ on axis $i$, so tensoring gives"
3. "So $Q$ is part of a convolution of length $T$ and never executed."
4. "so the target permutation $Q$ is absorbed into a Cyclic convolution of length $T$ and never executed."
5. "The permutation needs no separate step: it only changes which frequency is read, and the sign of the cross term $2j_ik_i$ already matches it."
6. "the transform of a convolution is a pointwise product of transforms"
7. "Permutations commute with pointwise products"
8. "which stay in the identity, never executed as sorts"

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

Write the answer to `exegenius/tasks/0360-attribute-g6.answer.json`, then run `exegenius submit 0360-attribute-g6` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0360-attribute-g6`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
