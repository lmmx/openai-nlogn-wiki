# exegenius task 0712-support-transform-round

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

Claim: Address bits are processed

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "from most to least significant."

Paragraph:

> Address bits are processed The bit that receives $\beta_i$ is the highest unprocessed bit $h$ of axis $i$ (the letter $h$ changes meaning here). Let $x_v$ be the bit in still unprocessed slot $v$ of axis $i$; the twiddle index is $\nu_i=\sum_{v=0}^{h-1}2^v x_v$.

### 2

Claim: The twiddle for axis $i$ depends only on

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "that axis’s address bits."

Paragraph:

> The twiddle for axis $i$ depends only on The two entries paired by another axis's butterfly share their axis-$i$ address, so they receive the same twiddle $c$. Since $H_0(cu,cv)=c\,H_0(u,v)$, the factor moves past that butterfly. The axis steps may therefore be grouped:.

### 3

Claim: The axis steps may therefore be grouped:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "may be grouped as a parallel butterfly H, followed by one recordwise monomial operation JE"

Paragraph:

> The twiddle for axis $i$ depends only on The two entries paired by another axis's butterfly share their axis-$i$ address, so they receive the same twiddle $c$. Since $H_0(cu,cv)=c\,H_0(u,v)$, the factor moves past that butterfly. The axis steps may therefore be grouped:.

### 4

Claim: A *contraction* is a linear map that does not increase the array norm $\|X\|$, the largest modulus of any coefficient of any record:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the same notation denotes the maximum over all coefficients in all entries."

Paragraph:

> A *contraction* is a linear map that does not increase the array norm $\|X\|$, the largest modulus of any coefficient of any record: An *isometry* preserves it. A coefficient of $(u\pm v)/2$ has modulus at most $\max(|u|,|v|)\le\|X\|$, so each axis step is a contraction, and applying the axis steps in turn gives $\mathcal{B}$, also a contraction. Multiplying by $y^\eta$, so the round is a contraction: $\|\mathcal{M}_\eta\mathcal{B}X\|\le\|\mathcal{B}X\|\le\|X\|$.

### 5

Claim: Multiplying by $y^\eta$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "permutes the coefficients and changes some signs; consequently it is an isometry for this norm."

Paragraph:

> A *contraction* is a linear map that does not increase the array norm $\|X\|$, the largest modulus of any coefficient of any record: An *isometry* preserves it. A coefficient of $(u\pm v)/2$ has modulus at most $\max(|u|,|v|)\le\|X\|$, so each axis step is a contraction, and applying the axis steps in turn gives $\mathcal{B}$, also a contraction. Multiplying by $y^\eta$, so the round is a contraction: $\|\mathcal{M}_\eta\mathcal{B}X\|\le\|\mathcal{B}X\|\le\|X\|$.

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

Write the answer to `exegenius/tasks/0712-support-transform-round.answer.json`, then run `exegenius submit 0712-support-transform-round` in the project directory. If submit rejects the answer, fix the answer and submit again.
