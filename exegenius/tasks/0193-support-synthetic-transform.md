# exegenius task 0193-support-synthetic-transform

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

Claim: For $r=4$, using $y^4=-1$,
$$y\,(a_0+a_1y+a_2y^2+a_3y^3)=-a_3+a_0y+a_1y^2+a_2y^3.$$
Each such multiplication is a signed shift of the coefficient list

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "multiplication by such a root is a signed shift of the coefficient list"

Paragraph:

> Multiplying by $y^\mu$ moves each coefficient $\mu$ places up, and a coefficient that passes position $r-1$ returns with its sign reversed. For $r=4$, using $y^4=-1$,
> $$y\,(a_0+a_1y+a_2y^2+a_3y^3)=-a_3+a_0y+a_1y^2+a_2y^3.$$
> Each such multiplication is a signed shift of the coefficient list.

### 2

Claim: Signed shifts and sums keep them Gaussian dyadic, and halving $m/2^f$ gives $m/2^{f+1}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "halving adds at most one denominator bit"

Paragraph:

> Assume the input coefficients are Gaussian dyadic numbers. Signed shifts and sums keep them Gaussian dyadic, and halving $m/2^f$ gives $m/2^{f+1}$. Each layer halves at most once, so after $L$ layers every denominator is at most $2^L$ times that of the inputs, and all intermediate values stay exact Gaussian dyadic numbers.

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

Write the answer to `exegenius/tasks/0193-support-synthetic-transform.answer.json`, then run `exegenius submit 0193-support-synthetic-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
