# exegenius task 0157-support-rounding-recovery

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

Claim: The paper's assembly section does this

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "removes the known normalizations and digit scales"

Paragraph:

> Write $\rho_j$ for the integer that the $j$-th computed coefficient approximates, once the known scales are removed. The paper's assembly section does this.

### 2

Claim: The paper proves the resulting bound on the error under its parameter choice

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "proves that the recovered coefficient error is strictly below $1/2$"

Paragraph:

> Each truncation keeps $p=6b$ fractional bits, so it adds error below $2^{-p}$. Exact recovery by rounding inherits its error from each [simultaneous butterfly layer](simultaneous-butterfly-layer.md), which ends with one truncation. The paper proves the resulting bound on the error under its parameter choice.

### 3

Claim: The paper's assembly section gives the exact binary product this way

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "propagates carries to obtain the exact binary product"

Paragraph:

> Exact recovery by rounding inverts the [Signed Kronecker packing](kronecker-packing.md), which evaluates the coefficients at $2^b$. Let $\delta_j$ be the $j$-th radix-$2^b$ digit of the integer being formed and $\sigma_j$ the carry into position $j$. Set $\sigma_0=0$ and, for each $j$, choose $\delta_j$ and $\sigma_{j+1}$ so that $\rho_j+\sigma_j=\delta_j+2^b\sigma_{j+1}$ with $0\le\delta_j<2^b$. Multiplying the $j$-th relation by $2^{bj}$ and summing, the carries cancel in pairs, so the digits represent the same integer as $\sum_j\rho_j2^{bj}$, with the final carry written as further digits. The paper's assembly section gives the exact binary product this way.

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

Write the answer to `exegenius/tasks/0157-support-rounding-recovery.answer.json`, then run `exegenius submit 0157-support-rounding-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.
