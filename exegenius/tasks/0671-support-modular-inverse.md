# exegenius task 0671-support-modular-inverse

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

Claim: The axis lengths are the paper's pairwise coprime source lengths:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Let s1 , . . . , sd be the pairwise coprime source lengths"

Paragraph:

> Let $d$ be the number of axes. For an axis index $i$ with $1 \le i \le d$ (here $i$ is not the imaginary unit), let $M_i$ be the length of axis $i$, the number of values its coordinate takes. The axis lengths are the paper's pairwise coprime source lengths:, so $M_i = s_i$, and any two distinct axis lengths are coprime. Let $S = \prod_{i=1}^d M_i$. For each $i$, let $P_i = \prod_{j<i} M_j$ be the product of the lengths before axis $i$, where $j$ is an axis index with $1 \le j < i$; $P_1 = 1$ is the empty product. Each factor $M_j$ with $j<i$ is coprime to $M_i$, so $P_i$ is coprime to $M_i$. Let $\mu_i$ be the inverse of $P_i$ modulo $M_i$, which exists.

### 2

Claim: The paper asserts that this image has order $S$ (a unit is an integer with an inverse modulo $M_i$):

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "because each µi is a unit and the si are pairwise coprime"

Paragraph:

> Each inverse $\mu_i$ computes exponents in a [cyclic group](cyclic-group.md) of order $S$. Let $\xi$ be a generator of that group, and for each axis $i$ let $\xi_i$ be a generator of a cyclic group of order $M_i$, so $\xi_i^{M_i} = 1$. The paper's map sends $\xi$ to $\prod_i \xi_i^{\mu_i}$, with $\xi_i$ playing the role of the paper's $x_i$. The order of an element is its least positive power equal to $1$. The paper asserts that this image has order $S$ (a unit is an integer with an inverse modulo $M_i$):.

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

Write the answer to `exegenius/tasks/0671-support-modular-inverse.answer.json`, then run `exegenius submit 0671-support-modular-inverse` in the project directory. If submit rejects the answer, fix the answer and submit again.
