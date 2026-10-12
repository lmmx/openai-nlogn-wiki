# exegenius task 0183-support-polynomial-ring-convolution

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

Claim: Both forward transforms keep the same frequency order, so one index $\lambda$ pairs $\Phi(a)_\lambda$ with $\Phi(b)_\lambda$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The two forward synthetic transforms retain the same frequency order"

Paragraph:

> Let $\rho = y^{2r/q}$, a synthetic root of unity: since $y$ has order $2r$, $\rho^q = 1$. The index $\lambda$ runs from $0$ to $q-1$ and labels the frequency of an entry. Let $\Phi$ be the forward transform, $\Phi(a)_\lambda = \sum_j a_j\rho^{j\lambda}$, and let $\Psi$ be the opposite transform, which takes an array $Y$ of $q$ records to $\Psi(Y)_k = \frac{1}{q}\sum_\lambda Y_\lambda\rho^{-k\lambda}$, dividing by $q$ and using the inverse root $\rho^{-1}$. Both forward transforms keep the same frequency order, so one index $\lambda$ pairs $\Phi(a)_\lambda$ with $\Phi(b)_\lambda$.

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

Write the answer to `exegenius/tasks/0183-support-polynomial-ring-convolution.answer.json`, then run `exegenius submit 0183-support-polynomial-ring-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
