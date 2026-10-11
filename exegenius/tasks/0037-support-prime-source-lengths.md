# exegenius task 0037-support-prime-source-lengths

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

Claim: The primes must make $S$ fill a fixed fraction of $T$, and the construction does both, as the sources require

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "their product must occupy a fixed fraction of the padded box, while each ratio ti /si must leave enough separation for resampling."

Paragraph:

> A prime source length is an odd prime chosen just below the padded length of one axis. Here $a$ indexes the $d$ axes, $a=1,\dots,d$, and each $t_a$ is a power of two. The source length $s_a$ of axis $a$ is that odd prime. Write $S=\prod_a s_a$ for the product of the source lengths, the length of the cyclic convolution, and $T=\prod_a t_a$ for the padded box. The primes are sized for [Gaussian resampling](gaussian-resampling.md), which needs each ratio $t_a/s_a$ to leave separation. The primes must make $S$ fill a fixed fraction of $T$, and the construction does both, as the sources require.

### 2

Claim: For $0<\eta<1/4$ and $X>e^2/\eta$, the window $(1-2\eta)X<q\le(1-\eta)X$ holds many primes

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the interval (1 − 2η)x < q ≤ (1 − η)x contains at least ηx/(2 log x) primes"

Paragraph:

> Let $\eta$ be a window-width parameter with $0<\eta<1/4$; the choice $\eta=1/(4d)$ gives this for $d\ge2$. Let $X$ be a real number standing for a padded length; the letter $x$ means an input string on earlier pages, so it is not used here. Let $q$ denote a prime. For $0<\eta<1/4$ and $X>e^2/\eta$, the window $(1-2\eta)X<q\le(1-\eta)X$ holds many primes, where $\log$ is the natural logarithm.

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

Write the answer to `exegenius/tasks/0037-support-prime-source-lengths.answer.json`, then run `exegenius submit 0037-support-prime-source-lengths` in the project directory. If submit rejects the answer, fix the answer and submit again.
