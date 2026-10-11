# exegenius task 0632-support-supremum

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

Claim: The paper defines the operator norm as a supremum over all vectors: $$\|L\| = \sup_{\|u\| \le 1} \|Lu\|.$$ The paper writes this as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "∥L∥ = sup∥u∥≤1 ∥Lu∥"

Paragraph:

> For a linear map $L$, meaning a map that preserves sums and scalar multiples, the largest factor by which $L$ stretches a vector is its operator norm $\|L\|$. Here $u$ is one input vector, a finite list of complex numbers; earlier pages used the letter $u$ for a single array entry, so its meaning changes on this page. The paper defines the operator norm as a supremum over all vectors: $$\|L\| = \sup_{\|u\| \le 1} \|Lu\|.$$ The paper writes this as. The set of inputs is restricted by the [Array norm](array-norm.md) of $u$, the norm of a vector, which must be at most one. So $\|L\|$ is defined even when no vector attains the largest value.

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

Write the answer to `exegenius/tasks/0632-support-supremum.answer.json`, then run `exegenius submit 0632-support-supremum` in the project directory. If submit rejects the answer, fix the answer and submit again.
