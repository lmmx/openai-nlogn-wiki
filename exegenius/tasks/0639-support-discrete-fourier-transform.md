# exegenius task 0639-support-discrete-fourier-transform

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

Claim: The exponent has a negative sign, and the paper uses the same sign:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The first identity uses the negative Fourier sign in our definition of Fq"

Paragraph:

> Each output is a weighted sum of all $q$ inputs, with weights $\omega^{s\ell}$, times $1/q$. The discrete Fourier transform $F_q$ is a linear map under the definitions of [linear algebra basics](linear-algebra-basics.md). The exponent has a negative sign, and the paper uses the same sign:.

### 2

Claim: The paper gives the reason for the normalization:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "normalized Fourier transform above is a contraction, since each output averages inputs multiplied"

Paragraph:

> The vector norm is $\|f\| = \max_s |f_s|$, the largest modulus of a coordinate. A linear map $K$ on $q$-vectors is a contraction when $\|Kf\| \le \|f\|$ for every $f$. The paper gives the reason for the normalization: by complex numbers of modulus one. Since $|\omega^{s\ell}| = 1$,

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

Write the answer to `exegenius/tasks/0639-support-discrete-fourier-transform.answer.json`, then run `exegenius submit 0639-support-discrete-fourier-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
