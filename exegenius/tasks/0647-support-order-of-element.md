# exegenius task 0647-support-order-of-element

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

Claim: The paper's claim is that the image of $x$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "has order S, because each µi is a unit and the si are pairwise coprime."

Paragraph:

> The [Chinese-remainder map](chinese-remainder-map.md) applies this to pairwise coprime source lengths $s_1, \dots, s_d$ with product $S$. Here $x$ is the indeterminate of $\mathbb{C}[x]/(x^S-1)$, and $x_i$ is the indeterminate of axis $i$; the letter $x$ changes meaning from earlier pages. The map $\Phi$ sends $x$ to $\prod_i x_i^{\mu_i}$, where each $\mu_i$ is an inverse, modulo $s_i$, of the product of the lengths before axis $i$. The paper's claim is that the image of $x$ Its powers therefore run.

### 2

Claim: Its powers therefore run

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "through all target basis monomials exactly once."

Paragraph:

> The [Chinese-remainder map](chinese-remainder-map.md) applies this to pairwise coprime source lengths $s_1, \dots, s_d$ with product $S$. Here $x$ is the indeterminate of $\mathbb{C}[x]/(x^S-1)$, and $x_i$ is the indeterminate of axis $i$; the letter $x$ changes meaning from earlier pages. The map $\Phi$ sends $x$ to $\prod_i x_i^{\mu_i}$, where each $\mu_i$ is an inverse, modulo $s_i$, of the product of the lengths before axis $i$. The paper's claim is that the image of $x$ Its powers therefore run.

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

Write the answer to `exegenius/tasks/0647-support-order-of-element.answer.json`, then run `exegenius submit 0647-support-order-of-element` in the project directory. If submit rejects the answer, fix the answer and submit again.
