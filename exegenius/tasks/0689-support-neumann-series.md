# exegenius task 0689-support-neumann-series

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

Claim: Its proof of invertibility is a norm bound followed by this series:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Thus ∥N − I∥ < 1/2, so N is invertible by the Neumann series."

Paragraph:

> Here the letter $N$ denotes the paper's operator, which changes its meaning from the earlier pages. The paper takes $J=N-I$, so that $I+J=N$. Its proof of invertibility is a norm bound followed by this series: The bound below one gives convergence, and the identity above shows that the limit inverts $N$.

### 2

Claim: The paper bounds the norm of $J$ by a power of two,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "∥N − I∥ < 2.01e−πα θ/2 < 2−α θ"

Paragraph:

> Here $\alpha$ and $\theta$ are parameters of the paper's construction, and the letter $\alpha$ changes meaning here. The paper's exponent is $\sigma=\alpha^2\theta$. The paper bounds the norm of $J$ by a power of two,. Its parameters satisfy. So $\|J\|<2^{-\sigma}$, with $\sigma>1$.

### 3

Claim: Its parameters satisfy

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "α2 θ > p/α2 > 1"

Paragraph:

> Here $\alpha$ and $\theta$ are parameters of the paper's construction, and the letter $\alpha$ changes meaning here. The paper's exponent is $\sigma=\alpha^2\theta$. The paper bounds the norm of $J$ by a power of two,. Its parameters satisfy. So $\|J\|<2^{-\sigma}$, with $\sigma>1$.

### 4

Claim: Rounding each iterate to precision $p$ keeps the records bounded:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "keeps every iterate in Dsp"

Paragraph:

> The paper applies the truncated series to rounded records. Each application of $J$ multiplies the size of an iterate by at most $\|J\|$, which is less than one, so the iterates shrink. Rounding each iterate to precision $p$ keeps the records bounded:.

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

Write the answer to `exegenius/tasks/0689-support-neumann-series.answer.json`, then run `exegenius submit 0689-support-neumann-series` in the project directory. If submit rejects the answer, fix the answer and submit again.
