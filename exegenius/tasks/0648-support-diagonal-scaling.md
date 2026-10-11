# exegenius task 0648-support-diagonal-scaling

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

Claim: It is the phase step of the argument: the paper's [simultaneous butterfly layer](simultaneous-butterfly-layer.md) combines each pair of entries whose addresses differ in the selected bits, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "becomes the simultaneous H0 layer after diagonal phase operations and a dyadic scale."

Paragraph:

> A diagonal scaling is a linear operator that multiplies each coordinate of a vector by its own fixed scalar. It is the phase step of the argument: the paper's [simultaneous butterfly layer](simultaneous-butterfly-layer.md) combines each pair of entries whose addresses differ in the selected bits, and

### 2

Claim: The paper says that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The diagonal operator SD multiplies the value stored at an address by the phase"

Paragraph:

> The phase operator of the butterfly layer is a diagonal scaling whose index set is the set of addresses. Let $w$ be the number of selected bits of an address, the count of bits that the layer acts on. For an address $\alpha$ with selected bits $\alpha_1,\dots,\alpha_w$, each $0$ or $1$, the scalar at $\alpha$ is the power $i^{\alpha_1+\cdots+\alpha_w}$ of the imaginary unit $i$. The paper says that determined by those bits, so the scalar depends on that address alone. stored at that address. With $w=2$, the addresses $00,01,10,11$ receive the phases $1,\,i,\,i,\,-1$.

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

Write the answer to `exegenius/tasks/0648-support-diagonal-scaling.answer.json`, then run `exegenius submit 0648-support-diagonal-scaling` in the project directory. If submit rejects the answer, fix the answer and submit again.
