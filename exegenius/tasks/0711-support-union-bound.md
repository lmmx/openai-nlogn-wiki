# exegenius task 0711-support-union-bound

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

Claim: **Why a guard value is uniform.**

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the complete y, z ranges give the same guard distribution at each choice of spectator coordinates"

Paragraph:

> **Why a guard value is uniform.**. Fix the spectator coordinates. The rectangle is a product of ranges, so every pair of $y$ and $z$ values occurs. The guard $g_i$ depends only on $K-1$ bits of $y$, and every other bit is free, so each of the $2^{K-1}$ values of $g_i$ is reached by $|\Omega|/2^{K-1}$ addresses. Hence a uniform address has each guard value with probability $1/2^{K-1}$, and a guard is bad with probability $20/2^{K-1}$.

### 2

Claim: The paper applies the union bound to these events:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the union bound over the 2(f − 1) guards gives"

Paragraph:

> Let $E_i$ be the set of addresses whose $i$-th guard is bad, so $\Pr[E_i]=20/2^{K-1}$. The exceptional addresses form $E_1\cup\cdots\cup E_m$. The paper applies the union bound to these events:

### 3

Claim: Write $\delta_{\mathrm{bad}}$ for the capped bound $\min\{1,80(f-1)/2^K\}$:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Put δbad = min{1, 80(f − 1)2−K }."

Paragraph:

> A probability above one says nothing, so the bound is capped. Write $\delta_{\mathrm{bad}}$ for the capped bound $\min\{1,80(f-1)/2^K\}$:

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

Write the answer to `exegenius/tasks/0711-support-union-bound.answer.json`, then run `exegenius submit 0711-support-union-bound` in the project directory. If submit rejects the answer, fix the answer and submit again.
