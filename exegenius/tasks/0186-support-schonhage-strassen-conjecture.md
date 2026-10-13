# exegenius task 0186-support-schonhage-strassen-conjecture

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

Claim: Schönhage and Strassen's 1971 algorithm multiplies two $n$-bit integers on a multitape Turing machine in $O(n\log n\log\log n)$ time

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Sch\"onhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in $O(n\log n\log\log n)$ time on a multitape Turing machine"

Paragraph:

> Schönhage and Strassen's 1971 algorithm multiplies two $n$-bit integers on a multitape Turing machine in $O(n\log n\log\log n)$ time. They proposed $n\log n$ as the optimal order of growth.

### 2

Claim: They proposed $n\log n$ as the optimal order of growth

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "proposed $n\log n$ as the optimal order of growth"

Paragraph:

> Schönhage and Strassen's 1971 algorithm multiplies two $n$-bit integers on a multitape Turing machine in $O(n\log n\log\log n)$ time. They proposed $n\log n$ as the optimal order of growth.

### 3

Claim: Harvey and van der Hoeven later gave an unconditional $O(n\log n)$ upper bound

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper bound"

Paragraph:

> Harvey and van der Hoeven later gave an unconditional $O(n\log n)$ upper bound for the same problem. Since the conjecture concerns multitape machines, this gives an $O(n\log n)$ multitape algorithm. The open part of the conjecture is therefore the matching lower bound: every multitape machine needs $\Omega(n\log n)$ worst-case time to multiply $n$-bit integers.

### 4

Claim: The target result obtains a strict power saving in the logarithmic factor

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We obtain a strict power saving in the logarithmic factor"

Paragraph:

> The conjecture is posed for multitape machines and is contrasted with the [fixed-tape machine model](fixed-tape-model.md), in which the target result is measured. The target result, [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md), computes the integer product exactly on one fixed-tape machine. Its worst-case time is $O(n(\lg n)^{1-\kappa})$ for a fixed constant $\kappa>0$, and its exponent $1-\kappa$ on $\lg n$ is less than 1. The target result obtains a strict power saving in the logarithmic factor, which is why it is compared with the conjecture.

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

Write the answer to `exegenius/tasks/0186-support-schonhage-strassen-conjecture.answer.json`, then run `exegenius submit 0186-support-schonhage-strassen-conjecture` in the project directory. If submit rejects the answer, fix the answer and submit again.
