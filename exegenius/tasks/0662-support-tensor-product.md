# exegenius task 0662-support-tensor-product

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

Claim: The paper uses the same construction for an operator on several columns:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the tensor product of its one-column version"

Paragraph:

> The paper uses the same construction for an operator on several columns:, taken over the coordinates of those columns. It states the product rule as, which is the mixed-product rule above.

### 2

Claim: It states the product rule as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Taking tensor products preserves their product"

Paragraph:

> The paper uses the same construction for an operator on several columns:, taken over the coordinates of those columns. It states the product rule as, which is the mixed-product rule above.

### 3

Claim: The paper states the layer as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The intended operation is the tensor product of"

Paragraph:

> The tensor product takes its one-coordinate factor from the [Butterfly](butterfly.md) map $H_0$, which replaces a pair of values by its half-sum and half-difference. Its matrix is $\tfrac12 P$. The paper states the layer as this operator on each selected bit. Here $J$ is the number of selected bits. Applying $\tfrac12 P$ to bit $l$ gives $\tfrac12 P_{(l)}$, so the layer is $(\tfrac12 P)_{(1)}\cdots(\tfrac12 P)_{(J)}$, which equals $(\tfrac12 P)^{\otimes J}$ by the identity above. This single operator acts on the $J$ selected bits and leaves the others fixed, and the [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) applies it in one pass rather than one bit at a time.

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

Write the answer to `exegenius/tasks/0662-support-tensor-product.answer.json`, then run `exegenius submit 0662-support-tensor-product` in the project directory. If submit rejects the answer, fix the answer and submit again.
