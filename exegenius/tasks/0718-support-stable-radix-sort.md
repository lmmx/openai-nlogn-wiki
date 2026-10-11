# exegenius task 0718-support-stable-radix-sort

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

Claim: Hence

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "these keys are distinct and are exactly the ranks of the marked"

Paragraph:

> The *destination map* sends each exceptional address to the address its record must reach, and it permutes the exceptional set.. Hence holes. The full stream stays untouched while the sort runs, and bit first.

### 2

Claim: The full stream stays untouched while the sort runs, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "stable binary radix sorting scans only the extracted records and keys, least significant key"

Paragraph:

> The *destination map* sends each exceptional address to the address its record must reach, and it permutes the exceptional set.. Hence holes. The full stream stays untouched while the sort runs, and bit first.

### 3

Claim: The paper defines it as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Arect = ⌈log2 (2V )⌉"

Paragraph:

> The key width follows from the number of records. For $M \ge 2$, every rank from $0$ to $M-1$ fits in $\lceil \log_2 M \rceil$ binary digits, so the key width is $w = \lceil \log_2 M \rceil$. Here $A_{\mathrm{rect}}$ is the paper's size parameter for its integers. The paper defines it as. The paper's destination keys are, which gives $w \le A_{\mathrm{rect}}$.

### 4

Claim: The paper's destination keys are

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "padded to ⌈log2 M ⌉ ≤ Arect bits"

Paragraph:

> The key width follows from the number of records. For $M \ge 2$, every rank from $0$ to $M-1$ fits in $\lceil \log_2 M \rceil$ binary digits, so the key width is $w = \lceil \log_2 M \rceil$. Here $A_{\mathrm{rect}}$ is the paper's size parameter for its integers. The paper defines it as. The paper's destination keys are, which gives $w \le A_{\mathrm{rect}}$.

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

Write the answer to `exegenius/tasks/0718-support-stable-radix-sort.answer.json`, then run `exegenius submit 0718-support-stable-radix-sort` in the project directory. If submit rejects the answer, fix the answer and submit again.
