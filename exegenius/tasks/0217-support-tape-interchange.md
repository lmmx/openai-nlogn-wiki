# exegenius task 0217-support-tape-interchange

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

Claim: The bound needs $s<W\mu$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "s<Wm"

Paragraph:

> The shear is carried by a bit network, a [Linear network](linear-network.md) whose wires each carry one bit. Each vertex holds a rational $\mu\times\mu$ matrix, where $\mu$ is its number of rows. An edge matrix, the head's matrix minus the tail's, of rank $a$ costs $a$ smaller calls, so $s$ is the sum of these ranks. Each smaller call acts on one of the $W$ [wire streams](role-streams.md), each of volume $V/W$. The bound needs $s<W\mu$, and the paper's explicit network has $W=W_{\rm b}$ and $s=s_{\rm b}$.

### 2

Claim: , and the paper's explicit network has $W=W_{\rm b}$ and $s=s_{\rm b}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "supplies these conditions with $W=W_{\rm b}$ and $s=s_{\rm b}$"

Paragraph:

> The shear is carried by a bit network, a [Linear network](linear-network.md) whose wires each carry one bit. Each vertex holds a rational $\mu\times\mu$ matrix, where $\mu$ is its number of rows. An edge matrix, the head's matrix minus the tail's, of rank $a$ costs $a$ smaller calls, so $s$ is the sum of these ranks. Each smaller call acts on one of the $W$ [wire streams](role-streams.md), each of volume $V/W$. The bound needs $s<W\mu$, and the paper's explicit network has $W=W_{\rm b}$ and $s=s_{\rm b}$.

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

Write the answer to `exegenius/tasks/0217-support-tape-interchange.answer.json`, then run `exegenius submit 0217-support-tape-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
