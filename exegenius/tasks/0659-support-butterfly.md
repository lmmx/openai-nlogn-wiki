# exegenius task 0659-support-butterfly

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

Claim: Two applications therefore halve the pair:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "H02 = I/2"

Paragraph:

> For example, $H_0(3,1)=(2,1)$ and $H_0(2,1)=(3,1)/2$. Two applications therefore halve the pair:, that is, $H_0^2=\tfrac12\,\mathrm{id}$.

### 2

Claim: When each entry is a record, $H_0$ acts

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "H0 acts coefficientwise"

Paragraph:

> When each entry is a record, $H_0$ acts. For each coefficient position $d$, the two output coefficients at $d$ are $H_0$ of the two input coefficients at $d$, one from each record of the pair.

### 3

Claim: The paper's level applies the butterfly, then

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "one recordwise monomial operation"

Paragraph:

> The butterfly is followed by a signed [Cyclic shift](cyclic-shift.md) of each record, which rotates the coefficients and negates those that wrap around. The paper's level applies the butterfly, then.

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

Write the answer to `exegenius/tasks/0659-support-butterfly.answer.json`, then run `exegenius submit 0659-support-butterfly` in the project directory. If submit rejects the answer, fix the answer and submit again.
