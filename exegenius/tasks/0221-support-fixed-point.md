# exegenius task 0221-support-fixed-point

Project directory: `/home/user/e2e-run` (paths below are relative to it)

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

Claim: Reserving $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component represents every intermediate coefficient exactly

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "represents every intermediate coefficient exactly"

Paragraph:

> So the components can be given room in advance. Let $\Delta$ be the number of extra bits reserved, at least the maximal depth reached in the layer. Reserving $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component represents every intermediate coefficient exactly, because the denominator and modulus bounds above then hold at every depth. The parameters keep $\Delta$ small compared with $p$, so each component still has $O(p)$ bits. The intermediate values are exact Gaussian dyadics

### 2

Claim: The intermediate values are exact Gaussian dyadics

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Intermediate values are exact Gaussian dyadics, whose real and imaginary parts have power-of-two denominators."

Paragraph:

> So the components can be given room in advance. Let $\Delta$ be the number of extra bits reserved, at least the maximal depth reached in the layer. Reserving $p+\Delta$ fractional bits and $\Delta+3$ integer and sign bits per real component represents every intermediate coefficient exactly, because the denominator and modulus bounds above then hold at every depth. The parameters keep $\Delta$ small compared with $p$, so each component still has $O(p)$ bits. The intermediate values are exact Gaussian dyadics

### 3

Claim: Only after the completed layer is one truncation $Q_p$ applied

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A single truncation follows the completed contractive layer."

Paragraph:

> Only after the completed layer is one truncation $Q_p$ applied The truncation $Q_p$ drops the bits below $2^{-p}$ in each real and imaginary part, returning the record to the $p$-bit grid, with error below $\sqrt2\,2^{-p}$ per complex coefficient. Rounding at every step would add one such error per step; here there is one per layer.

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

Write the answer to `exegenius/tasks/0221-support-fixed-point.answer.json`, then run `exegenius submit 0221-support-fixed-point` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0221-support-fixed-point`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
