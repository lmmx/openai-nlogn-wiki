# exegenius task 0152-support-prime-source-lengths

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

Claim: First, their product must fill a fixed fraction of the padded box

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "their product must occupy a fixed fraction of the padded box"

Paragraph:

> Two requirements fix how close $s_i$ must be to $t_i$. First, their product must fill a fixed fraction of the padded box. Second, the ratio $t_i/s_i$ must leave enough separation for [Gaussian resampling](gaussian-resampling.md), which moves between transforms of length $s_i$ and of length $t_i$.

### 2

Claim: A prime-interval result, based on explicit estimates of Rosser and Schoenfeld, shows that it contains many primes, at least a fixed multiple of $t/\log t$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "contains at least ηx/(2 log x) primes"

Paragraph:

> We use the window
> $$(1-2\eta)\,t_i < s_i \le (1-\eta)\,t_i,$$
> where the constant $\eta$, with $0<\eta<1/4$, sets the width of the window. For $t$ large enough, such a window contains primes. A prime-interval result, based on explicit estimates of Rosser and Schoenfeld, shows that it contains many primes, at least a fixed multiple of $t/\log t$. We choose distinct odd primes, one per axis, from these windows.

### 3

Claim: We choose distinct odd primes, one per axis, from these windows

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We may therefore choose distinct odd primes satisfying"

Paragraph:

> We use the window
> $$(1-2\eta)\,t_i < s_i \le (1-\eta)\,t_i,$$
> where the constant $\eta$, with $0<\eta<1/4$, sets the width of the window. For $t$ large enough, such a window contains primes. A prime-interval result, based on explicit estimates of Rosser and Schoenfeld, shows that it contains many primes, at least a fixed multiple of $t/\log t$. We choose distinct odd primes, one per axis, from these windows.

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

Write the answer to `exegenius/tasks/0152-support-prime-source-lengths.answer.json`, then run `exegenius submit 0152-support-prime-source-lengths` in the project directory. If submit rejects the answer, fix the answer and submit again.
