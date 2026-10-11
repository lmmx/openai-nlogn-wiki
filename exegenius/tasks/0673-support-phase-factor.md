# exegenius task 0673-support-phase-factor

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

Claim: The paper states it:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "i swaps the real and imaginary components and changes one sign."

Paragraph:

> The phase factors used here are built from the fourth [roots of unity](root-of-unity.md) $1, i, -1, -i$. Multiplying by $i$ swaps the parts and changes one sign: $i(1+2i) = -2+i$. The paper states it:

### 2

Claim: The paper states

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "In particular, C = iZC −1 Z."

Paragraph:

> Let $C=\tfrac12\begin{pmatrix}1+i&1-i\\1-i&1+i\end{pmatrix}$ be the forward kernel, and $Z=\mathrm{diag}(1,-1)$ the sign matrix. The paper states Conjugating by $Z$ gives $ZCZ = iC^{-1}$, so $C^{-1} = -i\,ZCZ$ since $1/i=-i$.

### 3

Claim: The paper's sign matrices,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "together with the scalar i27f at each affected sink, turn every endpoint kernel into a forward one."

Paragraph:

> A scalar correction is a fixed constant phase factor applied at each sink of a [network of gates and terminals](network-gate-terminal.md). An endpoint kernel is the kernel that a network applies to a role at its end. The paper's sign matrices,

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

Write the answer to `exegenius/tasks/0673-support-phase-factor.answer.json`, then run `exegenius submit 0673-support-phase-factor` in the project directory. If submit rejects the answer, fix the answer and submit again.
