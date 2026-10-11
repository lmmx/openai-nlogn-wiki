# exegenius task 0646-support-cyclic-group

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

Claim: It supplies the algebra behind the cyclic axes of the proof: the first reduction places the radix-digit coefficient list on

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "prime cyclic axes by a Chinese-remainder map that preserves convolution."

Paragraph:

> A cyclic group is a group whose elements are all the powers of one fixed element, its generator. It supplies the algebra behind the cyclic axes of the proof: the first reduction places the radix-digit coefficient list on

### 2

Claim: The paper's argument rests on the claim that the image of the generator

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "has order S, because each µi is a unit and the si are pairwise coprime."

Paragraph:

> A *cyclic convolution* of two length-$S$ sequences is their product in the polynomials in $\rho$ modulo $\rho^S-1$. The paper's argument rests on the claim that the image of the generator The map $\Gamma$ sends $\rho$ to $\prod_i Y_i^{\mu_i}$, so $\Gamma(\rho^\sigma)=\prod_i Y_i^{\sigma\mu_i}$. This equals $1$ exactly when $s_i \mid \sigma\mu_i$ for every $i$. Since $\mu_i$ is invertible modulo $s_i$, this means $s_i \mid \sigma$ for every $i$, and since the $s_i$ are pairwise coprime, $S \mid \sigma$.

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

Write the answer to `exegenius/tasks/0646-support-cyclic-group.answer.json`, then run `exegenius submit 0646-support-cyclic-group` in the project directory. If submit rejects the answer, fix the answer and submit again.
