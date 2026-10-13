# exegenius task 0197-support-signed-packing

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

Claim: Recovery needs $|\Upsilon_\eta|<\Theta/2$, which holds because $r<2^p$: the ring degree is at most the padded length, $r\le T$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "t_i\leq r\leq T<8n/b<2^{6b}=2^p"

Paragraph:

> Recovering the coefficients. Write $\Upsilon=J\Delta$, and $\Upsilon_\eta$ for its coefficient of $y^\eta$, with $\eta$ running over $0,\dots,2r-2$. Each $\Upsilon_\eta$ sums at most $r$ products $J_o\Delta_\tau$, so $|\Upsilon_\eta|\le r2^{2p}$. Recovery needs $|\Upsilon_\eta|<\Theta/2$, which holds because $r<2^p$: the ring degree is at most the padded length, $r\le T$, and $T<2^p$ for sufficiently large inputs by the choice of $p$ on the fixed-point page. Hence $|\Upsilon_\eta|\le r2^{2p}<2^{3p}<\Theta/2$. Since every $\Upsilon_\eta\Theta^\eta$ with $\eta\ge 1$ is a multiple of $\Theta$, $\Upsilon(\Theta)\equiv\Upsilon_0 \pmod{\Theta}$. As $|\Upsilon_0|<\Theta/2$, $\Upsilon_0$ is the unique integer in $[-\Theta/2,\Theta/2)$ congruent to $\Upsilon(\Theta)$ modulo $\Theta$. Subtracting it and dividing by $\Theta$ leaves the same form for $\Upsilon_1,\Upsilon_2,\dots$.

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

Write the answer to `exegenius/tasks/0197-support-signed-packing.answer.json`, then run `exegenius submit 0197-support-signed-packing` in the project directory. If submit rejects the answer, fix the answer and submit again.
