# exegenius task 0630-support-array-norm

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

Claim: The source records this as: a disk array

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "has norm at most one."

Paragraph:

> An array is a disk array when every entry has modulus at most one, that is, lies within distance one of $0$ in the complex plane. Since $\|X\|$ is the largest modulus, this holds exactly when $\|X\| \le 1$. The source records this as: a disk array

### 2

Claim: For an array over the ring,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the same notation denotes the maximum over all coefficients in all entries."

Paragraph:

> The norm extends to arrays over the [polynomial ring](polynomial-ring-mod-yr-plus-1.md). Here $r$ is the number of coefficients in each representative, and the ring is $\mathbb{C}[y]/(y^r+1)$, the polynomials modulo $y^r+1$. Each element $h$ of the ring is written $h = \sum_{s=0}^{r-1} h_s y^s$, where $s$, running from $0$ to $r-1$, indexes the coefficient $h_s$. The norm of $h$ is $\max_s |h_s|$. For an array over the ring,

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

Write the answer to `exegenius/tasks/0630-support-array-norm.answer.json`, then run `exegenius submit 0630-support-array-norm` in the project directory. If submit rejects the answer, fix the answer and submit again.
