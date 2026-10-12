# exegenius task 0156-support-bluestein-chirp

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

Claim: The ring therefore computes a cyclic convolution

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "its negative wrap gives precisely the original cyclic wrap after the twist is removed"

Paragraph:

> The cyclic form matters because of the polynomial ring. Let $\sigma$ be a coefficient position, from $0$ to $n-1$. In $\mathbb C[y]/(y^r+1)$ with $r=n$, a product term past the top coefficient picks up a minus sign, since $y^r=-1$. A phase twist removes this sign: multiply the coefficient of $y^\sigma$ by $\zeta^\sigma$ before the product, and by $\zeta^{-\sigma}$ after it. Let $\alpha$ be the coefficient at $y^{\sigma+n}$ in the twisted product. That term wraps to $-\alpha\zeta^{-\sigma}y^\sigma$ after the untwist, and $-\alpha\zeta^{-\sigma}=\alpha\zeta^{-(\sigma+n)}$ because $\zeta^n=-1$, which is the untwisted term moved to $y^\sigma$. The ring therefore computes a cyclic convolution.

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

Write the answer to `exegenius/tasks/0156-support-bluestein-chirp.answer.json`, then run `exegenius submit 0156-support-bluestein-chirp` in the project directory. If submit rejects the answer, fix the answer and submit again.
