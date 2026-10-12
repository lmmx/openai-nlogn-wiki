# exegenius task 0169-support-n-log-n-conjecture

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

Claim: In 1971 Schönhage and Strassen gave a multitape Turing machine algorithm running in $O(n\log n\log\log n)$ time

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Schönhage and Strassen proved in 1971 that two n-bit integers can be multiplied in O(n log n log log n) time on a multitape Turing machine"

Paragraph:

> Schoolbook multiplication takes $O(n^2)$ bit operations, so the question is how far below that the best method can go. In 1971 Schönhage and Strassen gave a multitape Turing machine algorithm running in $O(n\log n\log\log n)$ time. They also proposed that $n\log n$ is the optimal order of growth.

### 2

Claim: They also proposed that $n\log n$ is the optimal order of growth

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "proposed n log n as the optimal order of growth"

Paragraph:

> Schoolbook multiplication takes $O(n^2)$ bit operations, so the question is how far below that the best method can go. In 1971 Schönhage and Strassen gave a multitape Turing machine algorithm running in $O(n\log n\log\log n)$ time. They also proposed that $n\log n$ is the optimal order of growth.

### 3

Claim: Harvey and van der Hoeven later reached an unconditional $O(n\log n)$ upper bound, meaning one that needs no extra unproven hypothesis

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Harvey and van der Hoeven reached the unconditional O(n log n) upper bound"

Paragraph:

> Harvey and van der Hoeven later reached an unconditional $O(n\log n)$ upper bound, meaning one that needs no extra unproven hypothesis. The open question is whether this upper bound is also optimal: whether no exact method can do asymptotically better than $n\log n$.

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

Write the answer to `exegenius/tasks/0169-support-n-log-n-conjecture.answer.json`, then run `exegenius submit 0169-support-n-log-n-conjecture` in the project directory. If submit rejects the answer, fix the answer and submit again.
