# exegenius task 0628-support-truncation

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

Claim: The paper

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "represents every intermediate coefficient exactly"

Paragraph:

> A layer, written $H$, is one pass that replaces each pair of values $s$ and $r$ by $((s+r)/2,(s-r)/2)$, for every pair of entries whose [addresses](address.md) differ in one of several selected bits. Truncation is taken over pairs chosen by their [addresses](address.md), one rounding per layer. The paper, so the only rounding in a layer is $Q_p$ applied to the exact result $Hw$. The layer's error is therefore $\|Q_p(Hw) - Hw\|_\infty$, one truncation error of the size above. It is not a sum over intermediate steps, because none of them rounds.

### 2

Claim: The paper does this

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "right by the number of added fractional bits, restore its sign, and write the result in w bits."

Paragraph:

> The exact value is held as an integer numerator over a larger power of two. To truncate, the procedure shifts the magnitude of the numerator right, which discards its low bits, and restores the sign. For example, $-13/16 = -0.8125$ with two fractional places kept: the magnitude $13$ shifted right by $2$ bits is $3$, and restoring the sign gives $-3/4 = -0.75$, the value toward zero on the grid. The paper does this Because the magnitude is rounded down and the sign is restored afterwards, the result is truncation toward zero.

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

Write the answer to `exegenius/tasks/0628-support-truncation.answer.json`, then run `exegenius submit 0628-support-truncation` in the project directory. If submit rejects the answer, fix the answer and submit again.
