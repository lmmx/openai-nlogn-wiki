# exegenius task 0174-support-gaussian-resampling

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

Claim: Let $C$ be a power of two, the same for all $n_0$ and $n_1$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The constant is uniform"

Paragraph:

> Let $n_0<n_1$ be integers, the lengths of the source and target transforms, with $\gcd(n_0,n_1)=1$ and $n_1$ a power of two. Let $F_{n_0}$ and $F_{n_1}$ be their normalized transforms, and let $P_s$ and $P_t$ be the source and target coordinate permutations, which reorder the outputs of $F_{n_0}$ and $F_{n_1}$. Let $C$ be a power of two, the same for all $n_0$ and $n_1$. Here $L_1:\mathbb C^{n_0}\to\mathbb C^{n_1}$ and $L_2:\mathbb C^{n_1}\to\mathbb C^{n_0}$ are linear contractions, maps that do not increase the size of a vector. Such contractions exist, and the identity is
> $$P_sF_{n_0}=C\,L_2\,P_tF_{n_1}\,L_1$$

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

Write the answer to `exegenius/tasks/0174-support-gaussian-resampling.answer.json`, then run `exegenius submit 0174-support-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
