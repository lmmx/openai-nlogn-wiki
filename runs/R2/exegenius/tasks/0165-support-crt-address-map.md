# exegenius task 0165-support-crt-address-map

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

Claim: The paper's map targets a product of

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "distinct prime cyclic axes"

Paragraph:

> The map is applied to the radix-digit coefficient list produced by [reduction of integer product to digit convolution](radix-digit-reduction.md). The paper's map targets a product of. [Gaussian resampling](gaussian-resampling.md) expresses the Fourier transform on each prime-length axis through a multidimensional transform with power-of-two axis lengths, so the placement on prime axes is what lets it apply.

### 2

Claim: The paper's assembly section implements the map through

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "triangular controlled shifts and charged axis moves"

Paragraph:

> The paper's assembly section implements the map through. A shift or move rearranges the stored entries. The map's axis moves are costed in the [fixed-tape machine model and stream operations](fixed-tape-model.md), which counts each such step as data movement, since each step touches one cell per tape.

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

Write the answer to `exegenius/tasks/0165-support-crt-address-map.answer.json`, then run `exegenius submit 0165-support-crt-address-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
