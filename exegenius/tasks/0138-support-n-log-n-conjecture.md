# exegenius task 0138-support-n-log-n-conjecture

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

Claim: Schönhage and Strassen gave in 1971 a multitape Turing machine algorithm that runs in $O(n\log n\log\log n)$ time, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "proposed n log n as the optimal order of growth"

Paragraph:

> Schoolbook multiplication takes $O(n^2)$ bit operations, so the question is how far below that the best method can go. Schönhage and Strassen gave in 1971 a multitape Turing machine algorithm that runs in $O(n\log n\log\log n)$ time, and.

### 2

Claim: Later, Harvey and van der Hoeven reached an unconditional $O(n\log n)$ upper bound, one that holds without any extra hypothesis

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Harvey and van der Hoeven reached the unconditional O(n log n) upper bound"

Paragraph:

> Later, Harvey and van der Hoeven reached an unconditional $O(n\log n)$ upper bound, one that holds without any extra hypothesis. The conjecture therefore asks whether the extra $\log\log n$ factor, and any other gap, can be closed.

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

Write the answer to `exegenius/tasks/0138-support-n-log-n-conjecture.answer.json`, then run `exegenius submit 0138-support-n-log-n-conjecture` in the project directory. If submit rejects the answer, fix the answer and submit again.
