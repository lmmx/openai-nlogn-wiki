# exegenius task 0151-support-address-interchange

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

Claim: The cost is $O(Vu^\tau)$ time

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$."

Paragraph:

> $V$ is the stored bit volume, the number of data bits the array holds. $u$ is the width of each field, the number of address bits in one field; the letter $u$ changes meaning here. $\tau$ is a fixed exponent with $0<\tau<1$. The cost is $O(Vu^\tau)$ time

### 2

Claim: The outer two are lower-triangular changes of $D$, each costing $O(V)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A lower triangular transformation of $H$, or of $D$, costs $O(V)$"

Paragraph:

> Swapping fields $H$ and $D$ takes three updates, $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$, which send $(H,D)$ to $(D,H)$. The outer two are lower-triangular changes of $D$, each costing $O(V)$. The middle one is a shear $(H,D)\mapsto(H+D,D)$.

### 3

Claim: Each edge needs $\operatorname{rank}G_e$ of these interchanges

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "An edge matrix of rank $a$ will require $a$ smaller interchanges."

Paragraph:

> Let $\beta\ge2$ be the size of the network's matrices; a field splits into $\beta$ pieces of width $u/\beta$. Each edge needs $\operatorname{rank}G_e$ of these interchanges

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

Write the answer to `exegenius/tasks/0151-support-address-interchange.answer.json`, then run `exegenius submit 0151-support-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
