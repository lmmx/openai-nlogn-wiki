# exegenius task 0676-support-gaussian-integer

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

Claim: Each entry of the paper's frame and of its inverse is a Gaussian integer divided by a power of two,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "so both preserve arrays over Z[i, 1/2]."

Paragraph:

> Each entry of the paper's frame and of its inverse is a Gaussian integer divided by a power of two, Gaussian integers keep exact the entries of the paper's [kernels](two-point-kernel.md) and their inverses:

### 2

Claim: Gaussian integers keep exact the entries of the paper's [kernels](two-point-kernel.md) and their inverses:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The kernels implemented below have Gaussian dyadic coefficients."

Paragraph:

> Each entry of the paper's frame and of its inverse is a Gaussian integer divided by a power of two, Gaussian integers keep exact the entries of the paper's [kernels](two-point-kernel.md) and their inverses:

### 3

Claim: The paper states that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Gaussian integer coefficient Hj is a sum of exactly r signed products of Gaussian integer input"

Paragraph:

> Reduction modulo $y^r+1$ subtracts, for each position $j$ from $0$ to $r-1$, the coefficient at $j+r$ from the coefficient at $j$. The paper states that coefficients, where a signed product is a product multiplied by $+1$ or $-1$. So each reduced coefficient is a Gaussian integer.

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

Write the answer to `exegenius/tasks/0676-support-gaussian-integer.answer.json`, then run `exegenius submit 0676-support-gaussian-integer` in the project directory. If submit rejects the answer, fix the answer and submit again.
