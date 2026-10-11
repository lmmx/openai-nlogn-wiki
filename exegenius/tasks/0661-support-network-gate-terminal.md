# exegenius task 0661-support-network-gate-terminal

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

Claim: Each wire

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "carries one scalar"

Paragraph:

> A network carries values on *wires*. Each wire at a time. it in time order, and its sink. The source and the sink of a wire are its *terminals*.

### 2

Claim: wires, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "untouched wires retain their values"

Paragraph:

> wires, and. The wires that a gate touches are its *incidences*. For a scalar gate, the map acts at each *address*, a position in the arrays that the wires carry, and combines the values at one address using only the values at that same address. The gate is. A *pointwise linear gate*, also called a gate applied pointwise, is one whose combination is the same fixed linear combination at every address.

### 3

Claim: The gate is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "applied pointwise to matching addresses on the roles that it touches"

Paragraph:

> wires, and. The wires that a gate touches are its *incidences*. For a scalar gate, the map acts at each *address*, a position in the arrays that the wires carry, and combines the values at one address using only the values at that same address. The gate is. A *pointwise linear gate*, also called a gate applied pointwise, is one whose combination is the same fixed linear combination at every address.

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

Write the answer to `exegenius/tasks/0661-support-network-gate-terminal.answer.json`, then run `exegenius submit 0661-support-network-gate-terminal` in the project directory. If submit rejects the answer, fix the answer and submit again.
