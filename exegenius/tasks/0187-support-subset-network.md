# exegenius task 0187-support-subset-network

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

Claim: With $Y$ as source and $X$ as target, the inverse schedule gives $X\gets X-Y$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The inverse schedule with logical source $Y$ and target $X$ effects"

Paragraph:

> Each gate adds a fixed combination of wires that it does not change, so the same rows run in reverse order with every gate negated undo a forward invocation. With $Y$ as source and $X$ as target, the inverse schedule gives $X\gets X-Y$.

### 2

Claim: So the banks go from $(X,Y)$ to $(-Y,X)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "and restores every auxiliary value"

Paragraph:

> Three invocations in turn, forward, inverse and forward, take $(X,Y)$ to $(X,\,Y+X)$, then to $(-Y,\,Y+X)$, then to $(-Y,\,X)$. So the banks go from $(X,Y)$ to $(-Y,X)$.

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

Write the answer to `exegenius/tasks/0187-support-subset-network.answer.json`, then run `exegenius submit 0187-support-subset-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
