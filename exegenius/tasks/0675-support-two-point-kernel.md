# exegenius task 0675-support-two-point-kernel

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

Claim: The [simultaneous butterfly layer](simultaneous-butterfly-layer.md) is built from such kernels: in the paper *Integer multiplication below n log n*, its [phase frames](phase-factor.md) are written as a

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "product of two-point kernels on selected directions"

Paragraph:

> A two-point kernel is the $2\times 2$ operator that acts on the two entries of an array whose addresses differ in one bit. The [simultaneous butterfly layer](simultaneous-butterfly-layer.md) is built from such kernels: in the paper *Integer multiplication below n log n*, its [phase frames](phase-factor.md) are written as a.

### 2

Claim: The paper uses kernels of this kind, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "kernels implemented below have Gaussian dyadic coefficients"

Paragraph:

> The kernel $K$ has coefficients in [Gaussian dyadics](gaussian-dyadics.md) when $\delta$ and $\kappa$ are. Sums and products of Gaussian dyadics are again Gaussian dyadics, so a computation that uses only Gaussian dyadic coefficients is exact and involves no rounding. A kernel is multiplied by a [phase factor](phase-factor.md), such as $i$, and its coefficients remain Gaussian dyadic. The paper uses kernels of this kind, and, so the values computed with them stay exact.

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

Write the answer to `exegenius/tasks/0675-support-two-point-kernel.answer.json`, then run `exegenius submit 0675-support-two-point-kernel` in the project directory. If submit rejects the answer, fix the answer and submit again.
