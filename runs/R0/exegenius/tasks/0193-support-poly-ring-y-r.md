# exegenius task 0193-support-poly-ring-y-r

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

Claim: In the paper, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the coefficient list of a polynomial modulo $y^r+1$"

Paragraph:

> Here $y$ is the ring variable, the polynomial variable whose powers act as roots of unity. The ring degree $r$ is the number of complex coefficients in each element, a power of two. In the paper, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two.

### 2

Claim: , with $r$ a power of two

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "with $r$ a power of two"

Paragraph:

> Here $y$ is the ring variable, the polynomial variable whose powers act as roots of unity. The ring degree $r$ is the number of complex coefficients in each element, a power of two. In the paper, one coordinate is stored as the coefficient list of a polynomial modulo $y^r+1$, with $r$ a power of two.

### 3

Claim: The paper's multidimensional transforms have axis lengths that are powers of two

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "whose axis lengths are powers of two"

Paragraph:

> The paper's multidimensional transforms have axis lengths that are powers of two. A transform along one axis combines the entries that differ only in that coordinate, using roots of unity of the axis's length. Powers of $y$. By the two cases above, every root multiplication on such an axis is a signed shift, possibly negated.

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

Write the answer to `exegenius/tasks/0193-support-poly-ring-y-r.answer.json`, then run `exegenius submit 0193-support-poly-ring-y-r` in the project directory. If submit rejects the answer, fix the answer and submit again.
