# exegenius task 0713-support-tape-procedure

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

Claim: Each step

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "reads and writes at most one cell on each tape and moves each head by at most one cell"

Paragraph:

> The machine is the [Fixed-tape machine model](fixed-tape-model.md). Each step, so one scan of data of volume $V$, the number of stored bits, takes $O(V)$ steps.

### 2

Claim: An [array](array.md) is laid out on a tape in the order of its addresses,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "stored in lexicographic order, with the first coordinate most significant"

Paragraph:

> An [array](array.md) is laid out on a tape in the order of its addresses,. Butterflies act on selected address bits, so data must move between layouts; each move is a [permutation](permutation.md) of addresses.

### 3

Claim: The moves are built from Lemma 3 of the paper:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Each of the following operations on an array of volume V takes O(V ) steps on a fixed number of one-dimensional tapes"

Paragraph:

> The moves are built from Lemma 3 of the paper:. Its first operation is, with digits as bits.

### 4

Claim: Its first operation is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "any fixed permutation of the pair of digit values at two specified radix-q positions, whether or not the positions are adjacent"

Paragraph:

> The moves are built from Lemma 3 of the paper:. Its first operation is, with digits as bits.

### 5

Claim: Its cost is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "O(V uτ ) for a fixed τ < 1"

Paragraph:

> The first tape procedure, [Address-field interchange](address-interchange.md), moves data between layouts by swapping two disjoint address fields of $u$ bits. Its cost is, where $u$ is the field width and $\tau$ a fixed exponent in $(0,1)$. Since $u^{\tau}<u$ for $u>1$, the cost grows more slowly than the field width.

### 6

Claim: A full scan at every [transform level](transform-round.md) is too costly:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Scanning an array of Θ(n) stored bits at each of Θ(log n) transform levels already costs Θ(n log n)."

Paragraph:

> A full scan at every [transform level](transform-round.md) is too costly: The second tape procedure does the butterfly part of each [transform round](transform-round.md) in one pass, applying the butterfly. Its cost is. Here the letter $d$ changes meaning: it bounds the number of equal-width address chunks that one pass handles.

### 7

Claim: The second tape procedure does the butterfly part of each [transform round](transform-round.md) in one pass, applying the butterfly

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "simultaneously on selected coordinate bits of the numerical arrays"

Paragraph:

> A full scan at every [transform level](transform-round.md) is too costly: The second tape procedure does the butterfly part of each [transform round](transform-round.md) in one pass, applying the butterfly. Its cost is. Here the letter $d$ changes meaning: it bounds the number of equal-width address chunks that one pass handles.

### 8

Claim: Its cost is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "O(V dλ ) for a fixed λ′ < 1"

Paragraph:

> A full scan at every [transform level](transform-round.md) is too costly: The second tape procedure does the butterfly part of each [transform round](transform-round.md) in one pass, applying the butterfly. Its cost is. Here the letter $d$ changes meaning: it bounds the number of equal-width address chunks that one pass handles.

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

Write the answer to `exegenius/tasks/0713-support-tape-procedure.answer.json`, then run `exegenius submit 0713-support-tape-procedure` in the project directory. If submit rejects the answer, fix the answer and submit again.
