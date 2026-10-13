# exegenius task 0195-support-gaussian-resampling

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

Claim: Their size is bounded by $\|I-N\|<2^{-\sigma^2\theta}$,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The exact Gaussian identity and inverse estimate proved in"

Paragraph:

> In $(Nu)_j$ the term with index $j$ is exactly $u_j$, because $e^{\pi\sigma^2\delta_j^2}$ cancels the Gaussian factor at $k=\rho_j$. The other terms form $((N-I)u)_j$, where $I$ is the identity map. Their size is bounded by $\|I-N\|<2^{-\sigma^2\theta}$, their Theorem 4.2 and Lemma 4.6.

### 2

Claim: The usual implementation sorts twice on each coordinate; the sources keep both permutations in the identity and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "compute that formula directly."

Paragraph:

> The usual implementation sorts twice on each coordinate; the sources keep both permutations in the identity and

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

Write the answer to `exegenius/tasks/0195-support-gaussian-resampling.answer.json`, then run `exegenius submit 0195-support-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
