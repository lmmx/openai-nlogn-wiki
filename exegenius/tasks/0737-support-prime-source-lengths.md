# exegenius task 0737-support-prime-source-lengths

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

Claim: The construction begins:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Take the power of two T in [4n/b, 8n/b)"

Paragraph:

> The construction begins:. This gives $4n/b\le T<8n/b$, and $T$ is a power of two. Here $\epsilon$ is the size exponent, a fixed constant, and $d=\lfloor b^{\epsilon}\rfloor$, where $\lfloor x\rfloor$ is the greatest integer at most $x$. The source sets. Since $\epsilon<1/2$, we get $d\to\infty$ and $d\ge2$ for large $n$.

### 2

Claim: The source sets

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "ϵ = 2−75"

Paragraph:

> The construction begins:. This gives $4n/b\le T<8n/b$, and $T$ is a power of two. Here $\epsilon$ is the size exponent, a fixed constant, and $d=\lfloor b^{\epsilon}\rfloor$, where $\lfloor x\rfloor$ is the greatest integer at most $x$. The source sets. Since $\epsilon<1/2$, we get $d\to\infty$ and $d\ge2$ for large $n$.

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

Write the answer to `exegenius/tasks/0737-support-prime-source-lengths.answer.json`, then run `exegenius submit 0737-support-prime-source-lengths` in the project directory. If submit rejects the answer, fix the answer and submit again.
