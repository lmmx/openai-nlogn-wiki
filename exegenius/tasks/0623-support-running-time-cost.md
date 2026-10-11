# exegenius task 0623-support-running-time-cost

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

Claim: In this model, the machine's alphabet and tape count are fixed:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes."

Paragraph:

> Running time cost is defined on a [fixed-tape machine](fixed-tape-model.md), a machine whose alphabet and number of tapes do not grow with the input. In this model, the machine's alphabet and tape count are fixed: The alphabet is the finite set of symbols that any cell may hold. A tape is a row of cells, and each tape has a head that sits on one cell at a time. The inputs here are binary strings, so each cell holds $0$ or $1$.

### 2

Claim: A step

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "reads and writes at most one cell on each tape and moves each head by at most one cell."

Paragraph:

> One step is one local move. A step A head that must cross $5$ cells therefore needs at least $5$ steps.

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

Write the answer to `exegenius/tasks/0623-support-running-time-cost.answer.json`, then run `exegenius submit 0623-support-running-time-cost` in the project directory. If submit rejects the answer, fix the answer and submit again.
