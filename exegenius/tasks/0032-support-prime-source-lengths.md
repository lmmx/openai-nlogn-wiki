# exegenius task 0032-support-prime-source-lengths

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

Claim: The primes are chosen so that $S$ fills a fixed fraction of $T$ and each ratio leaves room for resampling

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "their product must occupy a fixed fraction of the padded box, while each ratio ti /si must leave enough separation for resampling."

Paragraph:

> The primes are chosen so that $S$ fills a fixed fraction of $T$ and each ratio leaves room for resampling. Take $\eta=1/(4d)$, which gives $0<\eta<1/4$ for $d\ge2$. Each prime is taken in the window $(1-2\eta)t_i<s_i\le(1-\eta)t_i$, so each ratio $s_i/t_i$ lies in $(1-2\eta,1-\eta]$. The primes are sized for [Gaussian resampling](gaussian-resampling.md), which needs each ratio $t_i/s_i$ to leave separation.

### 2

Claim: For $0<\eta<1/4$ and $x>e^2/\eta$, the interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the interval (1 − 2η)x < q ≤ (1 − η)x contains at least ηx/(2 log x) primes"

Paragraph:

> Let $x$ be a real number standing for a padded length; the letter $x$ means an input string on earlier pages, and it changes meaning here. Let $q$ denote a prime. For $0<\eta<1/4$ and $x>e^2/\eta$, the interval $(1-2\eta)x<q\le(1-\eta)x$ contains at least $\eta x/(2\log x)$ primes, where $\log$ is the natural logarithm.

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

Write the answer to `exegenius/tasks/0032-support-prime-source-lengths.answer.json`, then run `exegenius submit 0032-support-prime-source-lengths` in the project directory. If submit rejects the answer, fix the answer and submit again.
