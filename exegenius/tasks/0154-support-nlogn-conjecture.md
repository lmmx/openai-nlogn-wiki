# exegenius task 0154-support-nlogn-conjecture

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check whether each quotation on a page of an explanatory wiki supports the claim it is attached to. Writers back claims taken from the sources with a quotation copied from them; a quotation can exist in the source and still not support what it is attached to.

- Judge each claim against its quotation alone, not against what you know or what the source may say elsewhere.
- `supported`: the quotation states the claim or directly implies it.
- `partial`: the quotation supports part of the claim, or a weaker version of it.
- `unsupported`: the quotation does not address what the claim asserts.
- `contradicted`: the quotation says something incompatible with the claim.
- For every label but `supported`, say in one line what is missing or wrong.
- Label every quotation listed, each once.

## Quotations

### 1

Claim: Schönhage and Strassen's 1971 algorithm runs in $O(n\log n\log\log n)$ time

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "two $n$-bit integers can be multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine"

Paragraph:

> Schönhage and Strassen's 1971 algorithm runs in $O(n\log n\log\log n)$ time. Harvey and van der Hoeven reached $O(n\log n)$. Their algorithm also runs on a multitape machine, so $O(n\log n)$ is achievable in the model the conjecture is stated for, and the conjecture asks whether that cost can be beaten. The conjecture is posed against the chain of upper bounds traced in [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md).

### 2

Claim: Harvey and van der Hoeven reached $O(n\log n)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper bound"

Paragraph:

> Schönhage and Strassen's 1971 algorithm runs in $O(n\log n\log\log n)$ time. Harvey and van der Hoeven reached $O(n\log n)$. Their algorithm also runs on a multitape machine, so $O(n\log n)$ is achievable in the model the conjecture is stated for, and the conjecture asks whether that cost can be beaten. The conjecture is posed against the chain of upper bounds traced in [Schönhage–Strassen to Harvey–van der Hoeven multiplication](ss-hh-background.md).

### 3

Claim: The paper proves

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "T_A(n)=O\!\left(n(\lg n)^{1-\kappa}\right)"

Paragraph:

> The conjecture fails in the fixed-tape model used here. Let $A$ be the deterministic Turing machine of the paper's main theorem, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, so $A$ is one of the machines the conjecture quantifies over. Let $T_A(n)$ be its worst-case running time on pairs of $n$-bit inputs. Let $\kappa=2^{-182}$ be a fixed positive constant. The paper proves, which has the power $1-\kappa<1$ on the logarithm where the conjecture has power $1$. So $A$ runs in $o(n\log n)$ time and the conjecture fails in this model..

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Label": {
      "additionalProperties": false,
      "properties": {
        "label": {
          "$ref": "#/$defs/Verdict"
        },
        "mark": {
          "description": "Number of the quotation, as listed.",
          "format": "uint",
          "minimum": 0,
          "type": "integer"
        },
        "reason": {
          "description": "What is missing or wrong; may be empty for `supported`.",
          "type": "string"
        }
      },
      "required": [
        "mark",
        "label",
        "reason"
      ],
      "type": "object"
    },
    "Verdict": {
      "oneOf": [
        {
          "const": "supported",
          "description": "The quotation states the claim or directly implies it.",
          "type": "string"
        },
        {
          "const": "partial",
          "description": "The quotation supports part of the claim, or a weaker version.",
          "type": "string"
        },
        {
          "const": "unsupported",
          "description": "The quotation does not address what the claim asserts.",
          "type": "string"
        },
        {
          "const": "contradicted",
          "description": "The quotation says something incompatible with the claim.",
          "type": "string"
        }
      ]
    }
  },
  "additionalProperties": false,
  "properties": {
    "labels": {
      "items": {
        "$ref": "#/$defs/Label"
      },
      "type": "array"
    }
  },
  "required": [
    "labels"
  ],
  "title": "SupportAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0154-support-nlogn-conjecture.answer.json`, then run `exegenius submit 0154-support-nlogn-conjecture` in the project directory. If submit rejects the answer, fix the answer and submit again.
