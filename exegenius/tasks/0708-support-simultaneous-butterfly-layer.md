# exegenius task 0708-support-simultaneous-butterfly-layer

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

Claim: A transform round is one step of a multidimensional transform:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A round applies one current H0 on each participating axis."

Paragraph:

> A simultaneous butterfly layer applies the two-point map of a [butterfly](butterfly.md) to one selected bit of each of several transform axes at once, computing the exact result in one tape procedure. It is the step that lets a transform round apply its butterflies on all participating axes together, as the [main theorem](main-theorem.md) requires. A transform round is one step of a multidimensional transform:

### 2

Claim: Applying the one-axis factors in turn is costly:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "separate butterfly factors would require D whole-array passes"

Paragraph:

> Applying the one-axis factors in turn is costly:, where one pass reads and rewrites every stored record. The sources instead run the whole layer as, a fixed program of tape reads and writes. Three rewritings make this possible.

### 3

Claim: The sources instead run the whole layer as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "one fixed finite-alphabet multitape procedure"

Paragraph:

> Applying the one-axis factors in turn is costly:, where one pass reads and rewrites every stored record. The sources instead run the whole layer as, a fixed program of tape reads and writes. Three rewritings make this possible.

### 4

Claim: The inputs are

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "initially in the unit disk on the grid 2−p Z[i]"

Paragraph:

> Third, exact values and one truncation. Here $p$ is the working precision in bits. The inputs are. Here $s$ changes meaning and counts the individual factors $H_0$ applied. Each $H_0$ carries a factor $\frac12$, so $s$ factors refine the grid spacing to $2^{-(p+s)}$. A component in $[-1,1]$ on that grid is an integer multiple of $2^{-(p+s)}$, so it needs $p+s+O(1)$ bits.

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

Write the answer to `exegenius/tasks/0708-support-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0708-support-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.
