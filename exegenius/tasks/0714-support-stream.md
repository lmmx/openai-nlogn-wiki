# exegenius task 0714-support-stream

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

Claim: The recursion that saves a factor at each level works on streams:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A recursive call at parameter mf therefore uses s calls at parameter f , each on a stream of volume V /W ."

Paragraph:

> A stream is the order in which a procedure reads or writes a sequence of records on a tape, one position at a time. The recursion that saves a factor at each level works on streams:

### 2

Claim: A stream lists the entries of an [Array](array.md) in address order, since the array

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "is stored in lexicographic order, with the first coordinate most significant"

Paragraph:

> A stream lists the entries of an [Array](array.md) in address order, since the array. A stream position counts records from 0 within the stream and is not an address; the stream stores no addresses, because

### 3

Claim: A stream position counts records from 0 within the stream and is not an address; the stream stores no addresses, because

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "An address is implicit in an entry’s position in this ordered stream; it is not stored beside every data bit."

Paragraph:

> A stream lists the entries of an [Array](array.md) in address order, since the array. A stream position counts records from 0 within the stream and is not an address; the stream stores no addresses, because

### 4

Claim: Each stream is scanned by a [Tape procedure](tape-procedure.md) in a fixed number of passes:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Each stream is scanned a fixed number of times"

Paragraph:

> Each stream is formed by splitting an array on a specified digit of the [Mixed-radix digits](mixed-radix-digits.md) system. Each stream is scanned by a [Tape procedure](tape-procedure.md) in a fixed number of passes:, so the work is linear in the volume. The lemma states, including.

### 5

Claim: The lemma states

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Each of the following operations on an array of volume V takes O(V ) steps on a fixed number of one-dimensional tapes"

Paragraph:

> Each stream is formed by splitting an array on a specified digit of the [Mixed-radix digits](mixed-radix-digits.md) system. Each stream is scanned by a [Tape procedure](tape-procedure.md) in a fixed number of passes:, so the work is linear in the volume. The lemma states, including.

### 6

Claim: , including

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "splitting on a specified radix-q digit, applying a fixed pointwise map to aligned streams, and merging them back"

Paragraph:

> Each stream is formed by splitting an array on a specified digit of the [Mixed-radix digits](mixed-radix-digits.md) system. Each stream is scanned by a [Tape procedure](tape-procedure.md) in a fixed number of passes:, so the work is linear in the volume. The lemma states, including.

### 7

Claim: Since a step still touches at most one cell per tape,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Fixed tracks and finitely many work tapes change time by a fixed factor."

Paragraph:

> A fixed track is one of a fixed number of extra tracks that a tape carries beside its data, so each cell holds a tuple of symbols. Since a step still touches at most one cell per tape,

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

Write the answer to `exegenius/tasks/0714-support-stream.answer.json`, then run `exegenius submit 0714-support-stream` in the project directory. If submit rejects the answer, fix the answer and submit again.
