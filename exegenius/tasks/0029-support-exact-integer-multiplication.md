# exegenius task 0029-support-exact-integer-multiplication

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

Claim: The unconditional upper bound on this model is $O(n\log n)$, reached by Harvey and van der Hoeven

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Harvey and van der Hoeven reached the unconditional O(n log n) upper bound"

Paragraph:

> The input is written as $x\#y$, where $\#$ is a separator symbol placed between the two inputs; it marks where $x$ ends and $y$ begins, and it is not a bit. A multiplier is a deterministic Turing machine that, on input $x\#y$, halts with the output on its tape. The cost of a multiplier is its worst-case running time as a function of $n$. The unconditional upper bound on this model is $O(n\log n)$, reached by Harvey and van der Hoeven. One machine therefore serves every input length, with a fixed finite alphabet and a fixed number of one-dimensional tapes. The main result saves a strict power of the logarithmic factor in this same fixed finite-tape model.

### 2

Claim: One machine therefore serves every input length, with a fixed finite alphabet and a fixed number of one-dimensional tapes

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "There is one deterministic Turing machine A, with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, that computes this exact product for every n ≥ 1 and every pair of n-bit inputs"

Paragraph:

> The input is written as $x\#y$, where $\#$ is a separator symbol placed between the two inputs; it marks where $x$ ends and $y$ begins, and it is not a bit. A multiplier is a deterministic Turing machine that, on input $x\#y$, halts with the output on its tape. The cost of a multiplier is its worst-case running time as a function of $n$. The unconditional upper bound on this model is $O(n\log n)$, reached by Harvey and van der Hoeven. One machine therefore serves every input length, with a fixed finite alphabet and a fixed number of one-dimensional tapes. The main result saves a strict power of the logarithmic factor in this same fixed finite-tape model.

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

Write the answer to `exegenius/tasks/0029-support-exact-integer-multiplication.answer.json`, then run `exegenius submit 0029-support-exact-integer-multiplication` in the project directory. If submit rejects the answer, fix the answer and submit again.
