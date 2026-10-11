# exegenius task 0655-support-address-field

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

Claim: The paper's tape multiplication depends on these interchanges to change how an array's entries are laid out on the tape:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Fast address interchanges organize the layouts"

Paragraph:

> An address field is a run of bits in the [address](address.md) of an array, consecutive in position, and it is the unit that an address interchange exchanges with another field of the same width. The paper's tape multiplication depends on these interchanges to change how an array's entries are laid out on the tape:.

### 2

Claim: The paper also calls a field an address chunk or a chunk:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We use the bit network to interchange two equal address chunks on tape"

Paragraph:

> The paper also calls a field an address chunk or a chunk:, where the two chunks are the two fields that the interchange swaps.

### 3

Claim: An array is stored as one ordered stream:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "stored in lexicographic order, with the first coordinate most significant"

Paragraph:

> An array is stored as one ordered stream:. Lexicographic order is dictionary order: the first coordinate decides, and later coordinates break ties., so no address is written beside each bit. The addresses form a complete Cartesian product: every combination of coordinate values, each coordinate ranging over all its values, occurs as an address.

### 4

Claim: The paper's first procedure

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "interchanges two disjoint contiguous address fields of u bits in an array"

Paragraph:

> Write $\rho$ for the field width, the number of bits in each of the two fields being interchanged. The paper writes $u$ for this width; this page uses $\rho$ so that $u$ keeps its other meanings. Bit positions are numbered from 1 at the most significant bit, so position 1 is the leftmost. A field of $\rho$ bits is a run of $\rho$ consecutive positions, and two fields are disjoint when they share no position. The paper's first procedure,.

### 5

Claim: ,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "whose addresses form a complete Cartesian product"

Paragraph:

> Write $\rho$ for the field width, the number of bits in each of the two fields being interchanged. The paper writes $u$ for this width; this page uses $\rho$ so that $u$ keeps its other meanings. Bit positions are numbered from 1 at the most significant bit, so position 1 is the leftmost. A field of $\rho$ bits is a run of $\rho$ consecutive positions, and two fields are disjoint when they share no position. The paper's first procedure,.

### 6

Claim: The paper's definition is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "An address permutation f moves the entry at x to f (x)."

Paragraph:

> Each address field is moved by a [permutation](permutation.md) of addresses, because the interchange exchanges only the fields and not the entries' values. The paper's definition is

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

Write the answer to `exegenius/tasks/0655-support-address-field.answer.json`, then run `exegenius submit 0655-support-address-field` in the project directory. If submit rejects the answer, fix the answer and submit again.
