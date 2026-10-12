# exegenius task 0154-support-simultaneous-butterfly-layer

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

Claim: The layer runs in $O(Vd^{\lambda'})$ tape steps

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the cost is $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$"

Paragraph:

> Applying the $D$ factors one at a time takes one pass over the array per selected bit. A pass that touches all $V$ stored bits costs $O(V)$ steps, so this method costs $O(VD)$, at most $O(Vd)$. Here $\lambda'$ is a fixed exponent below one. The layer runs in $O(Vd^{\lambda'})$ tape steps, where $V$ is the number of stored data bits. Since $\lambda'<1$, the layer saves a factor $d^{1-\lambda'}$, a power of $d$, over the factor-by-factor method.

### 2

Claim: The address bound behind this cost is proved in the source's tape-interchange section

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Section~\ref{sec:tape-interchange} proves the address bound"

Paragraph:

> The layer computes its chunk moves by the [linear network with restored auxiliary values](linear-network-exchange.md), which carries each input role to an output role with a prescribed sign and restores every auxiliary value. The address bound behind this cost is proved in the source's tape-interchange section, and the layer bound is stated in its fast-butterfly section.

### 3

Claim: , and the layer bound is stated in its fast-butterfly section

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Section~\ref{sec:fast-butterfly-layers} gives the numerical layout, precision hypotheses, and layer bound"

Paragraph:

> The layer computes its chunk moves by the [linear network with restored auxiliary values](linear-network-exchange.md), which carries each input role to an output role with a prescribed sign and restores every auxiliary value. The address bound behind this cost is proved in the source's tape-interchange section, and the layer bound is stated in its fast-butterfly section.

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

Write the answer to `exegenius/tasks/0154-support-simultaneous-butterfly-layer.answer.json`, then run `exegenius submit 0154-support-simultaneous-butterfly-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.
