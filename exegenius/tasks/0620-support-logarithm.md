# exegenius task 0620-support-logarithm

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

Claim: Its convention rounds up and never goes below $1$:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Write lg n = max{⌈log2 n⌉, 1}."

Paragraph:

> Here $n$ is a positive [integer](integer.md), the number whose base-2 logarithm is taken, and $\lg n$ is defined for every such integer. The paper uses base $2$ and writes $\lg n$ for it; see [Base-2 logarithm](base-two-logarithm.md). Its convention rounds up and never goes below $1$: The ceiling $\lceil \log_2 n \rceil$ is the smallest integer that is at least $\log_2 n$, which is the same as the least power of two that is at least $n$.

### 2

Claim: The paper also writes plain $\log$ in one place, and there it means the natural logarithm, the logarithm to the base $e \approx 2.718$, not base $2$:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Here log is the natural logarithm."

Paragraph:

> The paper also writes plain $\log$ in one place, and there it means the natural logarithm, the logarithm to the base $e \approx 2.718$, not base $2$:

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

Write the answer to `exegenius/tasks/0620-support-logarithm.answer.json`, then run `exegenius submit 0620-support-logarithm` in the project directory. If submit rejects the answer, fix the answer and submit again.
