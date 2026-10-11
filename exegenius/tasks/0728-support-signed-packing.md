# exegenius task 0728-support-signed-packing

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

Claim: The paper calls the same block base $B_0$ and reads each coefficient the same way:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "next coefficient by its centered residue modulo B0"

Paragraph:

> Signed coefficient packing recovers its coefficients from centered residues under [congruence modulo $B$](congruence-modulo.md). Let $\sigma$ be the unique integer in $[-B/2, B/2)$ with $f(B)\,g(B) \equiv \sigma \pmod B$, the centered residue of $f(B)\,g(B)$ modulo $B$. Since $h(B) = h_0 + B\sum_{j\ge 1} h_j B^{j-1}$ and $|h_0| < B/2$, the residue $\sigma$ equals $h_0$. Subtract $\sigma$, divide by $B$, and repeat to read $h_1$, then $h_2$, and so on. The paper calls the same block base $B_0$ and reads each coefficient the same way:. Negative coefficients are recovered this way, with no extra sign bit.

### 2

Claim: The paper uses the same subroutine:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "To multiply the polynomial records, we use the fixed-tape integer multiplier of Harvey and van"

Paragraph:

> Signed coefficient packing computes its integer products with the [Established O(n log n) multiplier](established-multiplier.md), used as an ordinary subroutine. The paper uses the same subroutine: der Hoeven. The packing does not depend on how that multiplier works inside.

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

Write the answer to `exegenius/tasks/0728-support-signed-packing.answer.json`, then run `exegenius submit 0728-support-signed-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.
