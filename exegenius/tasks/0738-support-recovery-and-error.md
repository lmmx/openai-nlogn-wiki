# exegenius task 0738-support-recovery-and-error

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

Claim: The source sets $b=\lceil\log_2 n\rceil$ and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "p = 6b,"

Paragraph:

> The source sets $b=\lceil\log_2 n\rceil$ and and. The error analysis bounds the error over the $T$ entries of the [Padded transform box](padded-transform-box.md). Write $h_p=2^{-p}$ for the size of one unit in the last place: a value with $p$ fractional bits is a multiple of $h_p$, and an error of $a$ units is an absolute error below $a\,h_p$.

### 2

Claim: and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Take the power of two T in [4n/b, 8n/b)"

Paragraph:

> The source sets $b=\lceil\log_2 n\rceil$ and and. The error analysis bounds the error over the $T$ entries of the [Padded transform box](padded-transform-box.md). Write $h_p=2^{-p}$ for the size of one unit in the last place: a value with $p$ fractional bits is a multiple of $h_p$, and an error of $a$ units is an absolute error below $a\,h_p$.

### 3

Claim: A computed unit phase lies within $2h_p$ of the exact one, and truncation adds $2h_p$, so

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "(2∥x∥ + 2)hp < 4hp"

Paragraph:

> This analysis bounds the error of the [Phase twist](phase-twist.md) at each end by $4h_p$. A computed unit phase lies within $2h_p$ of the exact one, and truncation adds $2h_p$, so for every operand of norm at most $1$. The complex convolution therefore has error $E_{\rm ring}$ plus three twists,.

### 4

Claim: The complex convolution therefore has error $E_{\rm ring}$ plus three twists,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "(Ering + 4 + 4 + 4)hp < 6T Lhp"

Paragraph:

> This analysis bounds the error of the [Phase twist](phase-twist.md) at each end by $4h_p$. A computed unit phase lies within $2h_p$ of the exact one, and truncation adds $2h_p$, so for every operand of norm at most $1$. The complex convolution therefore has error $E_{\rm ring}$ plus three twists,.

### 5

Claim: Its norm is at most $.262<.5$, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Finally let the input to a source transform have norm at most .5."

Paragraph:

> , so the computed transforms of $\sigma\delta$ and $\sigma\delta'$ have norm below $.26$ and error below $E_sh_p$ each. Their pointwise product, truncated, has error below $(2E_s+2)h_p$, since each factor's error is weighted by a norm at most $1$, and truncation adds $2h_p$. Its norm is at most $.262<.5$, and

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

Write the answer to `exegenius/tasks/0738-support-recovery-and-error.answer.json`, then run `exegenius submit 0738-support-recovery-and-error` in the project directory. If submit rejects the answer, fix the answer and submit again.
