# exegenius task 0652-support-floor-function

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

Claim: The paper's square-root machine likewise returns the floor of a square root:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "returns binn (⌊ a⌋)"

Paragraph:

> The paper's division machine computes exactly this. The letters $q$, $a$ and $b$ in that quotation are the paper's own, for the quotient, dividend and divisor; they do not keep the meanings they have on other pages of this wiki. The paper's square-root machine likewise returns the floor of a square root:

### 2

Claim: The paper uses this step:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its floor q0 differs from q = ⌊a/b⌋ by at most one."

Paragraph:

> An approximate quotient is corrected to the exact floor with one exact integer computation. The paper uses this step: The remainder $r_0=a-bq_0$ is then computed exactly, and $q_0$ is decremented or incremented by one when $r_0$ falls outside $[0,b)$.

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

Write the answer to `exegenius/tasks/0652-support-floor-function.answer.json`, then run `exegenius submit 0652-support-floor-function` in the project directory. If submit rejects the answer, fix the answer and submit again.
