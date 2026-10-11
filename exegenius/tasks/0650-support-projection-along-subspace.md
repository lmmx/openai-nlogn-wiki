# exegenius task 0650-support-projection-along-subspace

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

Claim: The paper writes this map as $P_U$:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "For a nondegenerate rational subspace U ⊂ F, write PU for the projection onto U along U ⊥ ."

Paragraph:

> **Lemma 1.** If $U$ is nondegenerate, then $U \cap U^\perp = \{0\}$ and $\dim U^\perp = \dim W - \dim U$. So $U^\perp$ is complementary to $U$, and the projection onto $U$ along $U^\perp$ is defined. Write $\Theta_U$ for it. The paper writes this map as $P_U$:

### 2

Claim: The paper states:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "PV − PU is the identity on V ∩ U ⊥ and zero on its orthogonal complement."

Paragraph:

> The paper states: follows from Lemma 2.

### 3

Claim: Writing $P_{U^\perp} = I - P_U$, the paper's endpoint difference

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "For an input Xa the endpoint difference is PUa⊥ − (−PUa ) = Im"

Paragraph:

> The endpoint identity uses that $I - \Theta_U$ is the projection onto $U^\perp$ along $U$, since it fixes $U^\perp$ and sends $U$ to $0$. Writing $P_{U^\perp} = I - P_U$, the paper's endpoint difference is $P_{U^\perp} + P_U = I$.

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

Write the answer to `exegenius/tasks/0650-support-projection-along-subspace.answer.json`, then run `exegenius submit 0650-support-projection-along-subspace` in the project directory. If submit rejects the answer, fix the answer and submit again.
