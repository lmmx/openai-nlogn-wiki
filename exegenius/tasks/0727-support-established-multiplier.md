# exegenius task 0727-support-established-multiplier

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

Claim: The source describes the multiplier as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the fixed-tape integer multiplier of Harvey and van"

Paragraph:

> We write $\log$ for the base-2 logarithm. Here $N$ is the number of bits in each input. The source describes the multiplier as der Hoeven, with. Since $\log(2N)=\log N+1$ and $\log N\ge 1$ for $N\ge 2$, we get $\log(2N)\le 2\log N$, so the cost is $O(N\log N)$ for $N\ge 2$.

### 2

Claim: der Hoeven, with

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "cost O(N log(2N )) on N -bit inputs"

Paragraph:

> We write $\log$ for the base-2 logarithm. Here $N$ is the number of bits in each input. The source describes the multiplier as der Hoeven, with. Since $\log(2N)=\log N+1$ and $\log N\ge 1$ for $N\ge 2$, we get $\log(2N)\le 2\log N$, so the cost is $O(N\log N)$ for $N\ge 2$.

### 3

Claim: The source states this step as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "with an established integer multiplier."

Paragraph:

> The construction packs the coefficients of each polynomial into one large integer, multiplies two such integers with this multiplier, and unpacks the result (see [signed coefficient packing](signed-packing.md)). The source states this step as

### 4

Claim: The source says these calls

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "are ordinary subroutine calls; they do not invoke the improved theorem recursively."

Paragraph:

> The multiplier is an earlier algorithm, not the new theorem. The source says these calls So the construction does not call itself. Each call is charged its $O(N\log N)$ cost on its own inputs, taken as given. If a call used the new theorem, its cost would refer to the bound being proved.

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

Write the answer to `exegenius/tasks/0727-support-established-multiplier.answer.json`, then run `exegenius submit 0727-support-established-multiplier` in the project directory. If submit rejects the answer, fix the answer and submit again.
