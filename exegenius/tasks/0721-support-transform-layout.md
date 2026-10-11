# exegenius task 0721-support-transform-layout

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

Claim: A round's *selected bits* are the bits on which its [butterfly](butterfly.md) acts, defined by

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "H0 (u, v) = ((u + v)/2, (u − v)/2)"

Paragraph:

> A round's *selected bits* are the bits on which its [butterfly](butterfly.md) acts, defined by. A round applies one such butterfly on each participating axis.

### 2

Claim: Otherwise

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "separate butterfly factors would require D whole-array passes."

Paragraph:

> The shape makes one pass enough. A pass applies a two-point map at one bit position in each chunk, so the selected bits are handled together only when they share an offset. Otherwise

### 3

Claim: Numbering the chunks from the highest down, the layout exchanges chunks so that the $D$ chunks with the same number are adjacent:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "exchange the chunk currently there with the required chunk if they differ."

Paragraph:

> The remaining bits of each axis, at positions $(\lg r-1)\bmod K$ to $\lg r-2$, form $\lfloor(\lg r-1)/K\rfloor$ consecutive $K$-bit chunks, where $\lfloor x\rfloor$ is the largest integer not exceeding $x$. Numbering the chunks from the highest down, the layout exchanges chunks so that the $D$ chunks with the same number are adjacent: The transform layout is built from [address-field interchange](address-interchange.md) moves of whole chunks, together with single-bit moves. Each movement is

### 4

Claim: Each movement is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "included in the transform cost."

Paragraph:

> The remaining bits of each axis, at positions $(\lg r-1)\bmod K$ to $\lg r-2$, form $\lfloor(\lg r-1)/K\rfloor$ consecutive $K$-bit chunks, where $\lfloor x\rfloor$ is the largest integer not exceeding $x$. Numbering the chunks from the highest down, the layout exchanges chunks so that the $D$ chunks with the same number are adjacent: The transform layout is built from [address-field interchange](address-interchange.md) moves of whole chunks, together with single-bit moves. Each movement is

### 5

Claim: Every axis has the same remaining positions, so the chunks with the same number share this offset:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "in each of the D consecutive chunks with the same chunk index j."

Paragraph:

> A round on the bit at position $\varsigma$, counted from the least significant end, with $(\lg r-1)\bmod K\le\varsigma\le\lg r-2$, selects offset $(\varsigma-((\lg r-1)\bmod K))\bmod K$ within its chunk. Every axis has the same remaining positions, so the chunks with the same number share this offset:

### 6

Claim: , and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Pointwise multiplication commutes with applying the same record permutation"

Paragraph:

> The transform layout is the output order retained by the [forward procedure](forward-transform.md) for a pointwise product and the following opposite procedure., and, so the outputs can be multiplied in their [retained order](transform-identity.md). The transform layout is consumed by the [opposite transform](opposite-transform.md).

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

Write the answer to `exegenius/tasks/0721-support-transform-layout.answer.json`, then run `exegenius submit 0721-support-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.
