# exegenius task 0430-attribute-g6

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

Executing a permutation of records on a tape costs a logarithmic factor beyond a linear pass (about tp log t per line for the length-t transform). Across all lines that would cancel the power-of-log saving the page is after, so the permutations are kept as index relabellings inside identities the algorithm uses anyway. The target permutation Q is never executed because the Bluestein chirp identity identity QF_t u = conj(a) . (a * (conj(a) . u)) / T rewrites the relabelled transform as two chirp phase multiplications around one Cyclic convolution (the wiki's name for the wrapped product of sequences) of length T; the relabelling becomes part of a convolution that is performed anyway. The source permutation R is never executed because it commutes with pointwise products (a permutation of a pointwise product is the pointwise product of the permutations), and the same R appears on both forward transforms and in front of the opposite transform. The identity R F^+ R = F^+ holds because multiplying indices by a unit t and then by its inverse just relabels the summation index, so (R F^+)[(R F u) . (R F v)] = u*v / S^2 with no R left to execute. The convolution is therefore computed without any sort.

Covers key points: 1, 2, 3, 4

Quotations:

1. "A sort on every line would undo the saving of a power of $\log n$, so the permutations stay inside the formula."
2. "the permutations of Gaussian resampling stay inside the transform identity, where one is absorbed by a convolution and the other cancels."
3. "They are kept inside the identity, never executed: carrying them out would sort $t$ records of about $p$ bits on a tape, costing about $tp\log t$, which would cancel the power saving."
4. "The identity converts the transform together with $Q$ into a Cyclic convolution, so $Q$ never has to be executed as a sort."
5. "The factor $s_i$ in the chirp is what encodes $Q$."
6. "An entrywise product pairs entries at the same position, so $\pi(a\cdot b)=(\pi a)\cdot(\pi b)$ for any permutation: scrambled forward outputs multiply to the scrambled product."
7. "Each $t_i$ is a unit modulo $s_i$ and $R$ applies $R_{t_i}$ on axis $i$, so tensoring gives $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$."
8. "with no $R$ left to execute."
9. "Keeping that order costs nothing: a pointwise product does not care how positions are listed, provided both factors use the same order, and the opposite transform can be run to read that order."
10. "Thus the retained source permutation cancels when computing a convolution, and no sort occurs across the whole chain."
11. "Executing $Q$ means sorting data on tapes, which costs a logarithmic factor beyond a linear pass, the kind of factor the power saving removes."

### Answer 2

Gaussian resampling rewrites a Discrete Fourier transform of prime length s as a Discrete Fourier transform of a larger power-of-two length t, wrapped in two contractions A and B_0, with P_sF_s = 2^{2\alpha^2} B_0 P_t F_t A (roz). The permutations P_s and P_t are not executed because executing one is a sort of records on a tape, which costs about tp log t and would cancel the power saving (roz). Instead they are removed by two different cancellations. (1) The target permutation Q is absorbed by the chirp identity QF_t u = conj(a) . (a * (conj(a) . u))/T, with a_j = exp(-pi i sum s_i j_i^2 / t_i) (pap). This rewrites Q F_t as two pointwise phase multiplications around one Cyclic convolution of length T. Since the integer product needs a Cyclic convolution anyway, Q becomes part of that formula and no step reorders the array (zom). (2) The source permutation R appears in both forward transforms and in the opposite transform. Each t_i is a unit modulo s_i, so R F^+ R = F^+ (zom), and a permutation commutes with pointwise products (zom). Hence (R F^+)[(R F u) . (R F v)] = F^+(F u . F v) = u*v/S^2, with no R executed (zom). The one-axis identity that Gaussian resampling rests on is imported from another paper and is not proved in the wiki (roz). I did not verify the error bounds or the full integer chain on the multiplication page, so the answer depends on those being correct.

Covers key points: 1, 2, 3, 4

Quotations:

1. "They are kept inside the identity, never executed: carrying them out would sort $t$ records of about $p$ bits on a tape, costing about $tp\log t$, which would cancel the power saving."
2. "The result is that there are linear contractions $A$ from length-$s$ to length-$t$ vectors and $B_0$ from length-$t$ to length-$s$ vectors, with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$."
3. "The identity converts the transform together with $Q$ into a Cyclic convolution, so $Q$ never has to be executed as a sort."
4. "$Q$ becomes part of a convolution formula, so no step reorders the array."
5. "so tensoring gives $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$."
6. "A permutation commutes with pointwise products, so the left side of the product identity equals $F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$."
7. "An entrywise product pairs entries at the same position, so $\pi(a\cdot b)=(\pi a)\cdot(\pi b)$ for any permutation: scrambled forward outputs multiply to the scrambled product."

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

Write the answer to `exegenius/tasks/0430-attribute-g6.answer.json`, then run `exegenius submit 0430-attribute-g6` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0430-attribute-g6`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
