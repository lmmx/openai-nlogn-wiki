# exegenius task 0159-support-address-fields

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

Claim: Each entry is a fixed-width coefficient of $\Theta(\log n)$ bits, and the padded array holds $\Theta(n/\log n)$ entries, so $V=\Theta(n)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "a full padded array has $\Theta(V)$ stored bits"

Paragraph:

> Rearranging is not free. A layout's cost is counted in the [Fixed-tape machine model and stream operations](fixed-tape-model.md), where each step touches one cell per tape, so moving data is the cost to minimize. Write $V$ for the stored bit volume, the total number of bits the array holds. Each entry is a fixed-width coefficient of $\Theta(\log n)$ bits, and the padded array holds $\Theta(n/\log n)$ entries, so $V=\Theta(n)$. Scanning all $\Theta(n)$ stored bits at each of the $\Theta(\log n)$ levels costs $\Theta(n\log n)$.

### 2

Claim: Scanning all $\Theta(n)$ stored bits at each of the $\Theta(\log n)$ levels costs $\Theta(n\log n)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$"

Paragraph:

> Rearranging is not free. A layout's cost is counted in the [Fixed-tape machine model and stream operations](fixed-tape-model.md), where each step touches one cell per tape, so moving data is the cost to minimize. Write $V$ for the stored bit volume, the total number of bits the array holds. Each entry is a fixed-width coefficient of $\Theta(\log n)$ bits, and the padded array holds $\Theta(n/\log n)$ entries, so $V=\Theta(n)$. Scanning all $\Theta(n)$ stored bits at each of the $\Theta(\log n)$ levels costs $\Theta(n\log n)$.

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

Write the answer to `exegenius/tasks/0159-support-address-fields.answer.json`, then run `exegenius submit 0159-support-address-fields` in the project directory. If submit rejects the answer, fix the answer and submit again.
