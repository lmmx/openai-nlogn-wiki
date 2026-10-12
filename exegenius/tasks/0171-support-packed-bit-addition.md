# exegenius task 0171-support-packed-bit-addition

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

Claim: So $|Z| \le \delta M$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "|B| ≤ δbad M"

Paragraph:

> The construction first applies a constant number of cyclic shifts, whose composition is $\sigma$. Let $T$ be the exact map that performs the XORs on every record, and let $Z$ be the set of exceptional addresses, where $\sigma$ and $T$ disagree. The fraction $\delta = \min\{1, 80(\mu-1)2^{-K}\}$ is small when $K$ is large. So $|Z| \le \delta M$.

### 2

Claim: The exact map $T$ preserves $Z$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The ideal map T0 preserves all guard values and therefore preserves B"

Paragraph:

> The exact map $T$ preserves $Z$. Since $T$ preserves $Z$, it also maps addresses outside $Z$ to addresses outside $Z$. As $\sigma$ and $T$ agree outside $Z$ and both are bijections, the correction $T\sigma^{-1}$ fixes every address outside $Z$ and permutes $Z$. Applying the correction after the shifts therefore gives $T$ exactly.

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

Write the answer to `exegenius/tasks/0171-support-packed-bit-addition.answer.json`, then run `exegenius submit 0171-support-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.
