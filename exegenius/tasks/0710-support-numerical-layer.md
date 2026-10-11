# exegenius task 0710-support-numerical-layer

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

Claim: One axis at a time needs

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "separate butterfly factors would require D whole-array passes"

Paragraph:

> Let $V$ be the number of stored bits. One axis at a time needs, each scanning all $V$ stored bits. A row is the address suffix at one fixed prefix and row index., so per role.

### 2

Claim: , so

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "each contains V /W bits"

Paragraph:

> Let $V$ be the number of stored bits. One axis at a time needs, each scanning all $V$ stored bits. A row is the address suffix at one fixed prefix and row index., so per role.

### 3

Claim: The paper requires

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "that the total number s of smaller calls satisfies s < W m."

Paragraph:

> The paper requires That is $s/W<m$, so $\log_m(s/W)<1$. Otherwise the exponent is at least one and nothing is saved. The layer costs $O(V d^{\lambda'})$, where $\lambda'$ is a fixed exponent below one..

### 4

Claim: Its operations are

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "complex additions, subtractions, halvings, sign"

Paragraph:

> The layer is exact. Its operations are changes and multiplication by $i$. Each keeps Gaussian dyadics closed: sums use the larger power of two as denominator, halving doubles it, and the rest leave it alone. The inputs lie on $2^{-p}\mathbb{Z}[i]$, so.

### 5

Claim: The inputs lie on $2^{-p}\mathbb{Z}[i]$, so

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Intermediate values are exact Gaussian dyadics"

Paragraph:

> The layer is exact. Its operations are changes and multiplication by $i$. Each keeps Gaussian dyadics closed: sums use the larger power of two as denominator, halving doubles it, and the rest leave it alone. The inputs lie on $2^{-p}\mathbb{Z}[i]$, so.

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

Write the answer to `exegenius/tasks/0710-support-numerical-layer.answer.json`, then run `exegenius submit 0710-support-numerical-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.
