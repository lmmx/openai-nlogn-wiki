# exegenius task 0629-support-array

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

Claim: The paper's elementary array operations, such as fixed permutations of digit values, each

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "takes O(V ) steps on a fixed number of one-dimensional tapes"

Paragraph:

> An array is a finite collection of entries, each stored at an [address](address.md) and carrying a [payload](payload.md). The paper's tape procedures act on arrays. A tape procedure is a procedure run on a multitape Turing machine that rearranges an array held on its tapes. Here $V$ is the number of stored data bits, the paper's logical volume. The paper's elementary array operations, such as fixed permutations of digit values, each. The [address-field interchange](address-interchange.md) and the [linear networks](linear-network-frames.md) of the argument are likewise operations on arrays, and their costs are measured by $V$.

### 2

Claim: The paper's array is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "stored in lexicographic order, with the first coordinate most significant."

Paragraph:

> The entries of an array are indexed by their [address](address.md). Each entry carries a [payload](payload.md), the record data stored at its address. The paper's array is Lexicographic order compares two addresses by their first coordinate and, when those agree, by the next coordinate, and so on. The order fixes every address, so the paper can state: it is not stored beside every data bit.

### 3

Claim: The order fixes every address, so the paper can state:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "An address is implicit in an entry’s position in this ordered stream;"

Paragraph:

> The entries of an array are indexed by their [address](address.md). Each entry carries a [payload](payload.md), the record data stored at its address. The paper's array is Lexicographic order compares two addresses by their first coordinate and, when those agree, by the next coordinate, and so on. The order fixes every address, so the paper can state: it is not stored beside every data bit.

### 4

Claim: The paper's term disk array names an array that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "has norm at most one."

Paragraph:

> The paper's term disk array names an array that Here the [norm](array-norm.md) of an array is the maximum modulus over all coefficients in all its entries, so every coefficient of a disk array has modulus at most one.

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

Write the answer to `exegenius/tasks/0629-support-array.answer.json`, then run `exegenius submit 0629-support-array` in the project directory. If submit rejects the answer, fix the answer and submit again.
