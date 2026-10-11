# exegenius task 0654-support-permutation

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

Claim: The paper writes this map as $f$ and states:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "An address permutation f moves the entry at x to f (x)."

Paragraph:

> **Permutations of arrays.** Write $\xi$ for an address, the position of one entry of an array. Let $G$ be an array whose entries are stored at addresses. An address permutation $\sigma$ moves the entry at $\xi$ to $\sigma(\xi)$. The paper writes this map as $f$ and states: The moved array $G'$ holds the same entries at the new addresses, so $G'(\sigma(\xi))=G(\xi)$ for every address $\xi$. No entry is recomputed.

### 2

Claim: **Cost of a move.**

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes."

Paragraph:

> **Cost of a move.** A scan is one pass of a head over the cells of a tape, and the time of an operation is its number of steps. Moving one digit in a fixed radix is cheap: it. Moving whole fields whose digit counts grow needs more work. The paper realizes this interchange in its Section 4, where the bitwise exclusive or of two bits is 1 exactly when the bits differ.

### 3

Claim: Moving one digit in a fixed radix is cheap: it

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "needs a bounded number of scans"

Paragraph:

> **Cost of a move.** A scan is one pass of a head over the cells of a tape, and the time of an operation is its number of steps. Moving one digit in a fixed radix is cheap: it. Moving whole fields whose digit counts grow needs more work. The paper realizes this interchange in its Section 4, where the bitwise exclusive or of two bits is 1 exactly when the bits differ.

### 4

Claim: The paper realizes this interchange in its Section 4

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "by computing XOR combinations of intermediate data streams"

Paragraph:

> **Cost of a move.** A scan is one pass of a head over the cells of a tape, and the time of an operation is its number of steps. Moving one digit in a fixed radix is cheap: it. Moving whole fields whose digit counts grow needs more work. The paper realizes this interchange in its Section 4, where the bitwise exclusive or of two bits is 1 exactly when the bits differ.

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

Write the answer to `exegenius/tasks/0654-support-permutation.answer.json`, then run `exegenius submit 0654-support-permutation` in the project directory. If submit rejects the answer, fix the answer and submit again.
