# exegenius task 0219-support-machine-model

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

Claim: A machine has a single finite alphabet and a finite number of one-dimensional tapes, both fixed independently of the input

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes."

Paragraph:

> A machine has a single finite alphabet and a finite number of one-dimensional tapes, both fixed independently of the input. Each tape is a one-way or two-way infinite line of cells, each holding one symbol, with one head per tape. In one step the machine reads and writes at most one cell on each tape and moves each head by at most one cell. Time is the number of steps.

### 2

Claim: **Constant factors are free, structure is not.** Splitting each cell into a fixed number of tracks, or adding finitely many work tapes, changes the running time only by a fixed factor

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Fixed tracks and finitely many work tapes change time by a fixed factor."

Paragraph:

> **Constant factors are free, structure is not.** Splitting each cell into a fixed number of tracks, or adding finitely many work tapes, changes the running time only by a fixed factor Since the target bound is an exponent saving, not a constant improvement, such factors do not matter, and an algorithm may keep several arrays side by side on separate tapes or tracks.

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

Write the answer to `exegenius/tasks/0219-support-machine-model.answer.json`, then run `exegenius submit 0219-support-machine-model` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0219-support-machine-model`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
