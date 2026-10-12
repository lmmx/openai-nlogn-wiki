# exegenius task 0173-support-tensor-product

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

Claim: Each selected bit therefore contributes one factor $\mathbb{C}^2$, so the layer is $H_0\otimes\cdots\otimes H_0\otimes\mathrm{id}$ with $D$ copies of $H_0$, and $\mathrm{id}$ on all other address fields, as the source's layer keeps them,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "preserving all other address fields"

Paragraph:

> An address bit is one binary digit of an address, so it takes the value 0 or 1. An array indexed by one bit is a pair of values $(u,v)$, a vector of $\mathbb{C}^2$ as in the example, and $H_0$ acts on that pair. Let $D$ be the number of selected chunks, each contributing one selected address bit. The address set is a product of index sets, and an array on a product is the tensor product of arrays on its factors. Each selected bit therefore contributes one factor $\mathbb{C}^2$, so the layer is $H_0\otimes\cdots\otimes H_0\otimes\mathrm{id}$ with $D$ copies of $H_0$, and $\mathrm{id}$ on all other address fields, as the source's layer keeps them,.

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

Write the answer to `exegenius/tasks/0173-support-tensor-product.answer.json`, then run `exegenius submit 0173-support-tensor-product` in the project directory. If submit rejects the answer, fix the answer and submit again.
