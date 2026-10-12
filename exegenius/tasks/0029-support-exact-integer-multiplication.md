# exegenius task 0029-support-exact-integer-multiplication

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

Claim: Schönhage and Strassen proved in 1971 that the problem can be solved in $O(n\log n\log\log n)$ time

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "two n-bit integers can be multiplied in O(n log n log log n) time on a multitape Turing machine"

Paragraph:

> Schönhage and Strassen proved in 1971 that the problem can be solved in $O(n\log n\log\log n)$ time. Harvey and van der Hoeven later reached the unconditional $O(n\log n)$ upper bound.

### 2

Claim: Harvey and van der Hoeven later reached the unconditional $O(n\log n)$ upper bound

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "unconditional O(n log n) upper bound"

Paragraph:

> Schönhage and Strassen proved in 1971 that the problem can be solved in $O(n\log n\log\log n)$ time. Harvey and van der Hoeven later reached the unconditional $O(n\log n)$ upper bound.

### 3

Claim: The target result improves the $O(n\log n)$ bound

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We obtain a strict power saving in the logarithmic factor, in the same fixed finite-tape model"

Paragraph:

> The target result improves the $O(n\log n)$ bound. This model is a Turing machine with.

### 4

Claim: This model is a Turing machine with

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "a fixed finite alphabet and a fixed finite number of one-dimensional tapes"

Paragraph:

> The target result improves the $O(n\log n)$ bound. This model is a Turing machine with.

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

Write the answer to `exegenius/tasks/0029-support-exact-integer-multiplication.answer.json`, then run `exegenius submit 0029-support-exact-integer-multiplication` in the project directory. If submit rejects the answer, fix the answer and submit again.
