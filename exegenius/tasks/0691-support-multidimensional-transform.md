# exegenius task 0691-support-multidimensional-transform

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

Claim: [Gaussian resampling](gaussian-resampling.md) uses it in place of the ordinary Fourier transforms of a convolution: the reduction

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "replaces the Fourier transforms needed for this convolution by multidimensional transforms whose"

Paragraph:

> A multidimensional transform is a Fourier transform taken over several [transform axes](transform-axis.md) at once, computed by transforming along one axis at a time. [Gaussian resampling](gaussian-resampling.md) uses it in place of the ordinary Fourier transforms of a convolution: the reduction axis lengths are powers of two.

### 2

Claim: In it,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "one coordinate is stored as the coefficient list of a polynomial modulo y r + 1, with r a power of two"

Paragraph:

> The multidimensional transform is written in the representation of [synthetic polynomial transforms](synthetic-transforms.md). In it,, so $y^r=-1$.: for an axis of length $t_\sigma$ dividing $2r$, the power $y^{2r/t_\sigma}$ is a $t_\sigma$-th root of unity, because its $t_\sigma$-th power is $y^{2r}=(y^r)^2=1$.

### 3

Claim: Consequently

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the transform calculation consists of address rearrangements, signed shifts, and two-point butterfly operations."

Paragraph:

> Multiplying a record by $y^s$, with $0\le s<r$, moves the coefficient at position $d$ to position $d+s$. If $d+s\ge r$, then $y^{d+s}=-y^{d+s-r}$, so the coefficient lands at $d+s-r$ with a minus sign. For $r=4$, $y\,(c_0+c_1y+c_2y^2+c_3y^3)=-c_3+c_0y+c_1y^2+c_2y^3$, since $y^4=-1$. This is a [cyclic shift](cyclic-shift.md) of the coefficient list with the wrapped entries negated. In this representation, the transform turns roots of unity into [signed cyclic shifts](cyclic-shift.md). Consequently

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

Write the answer to `exegenius/tasks/0691-support-multidimensional-transform.answer.json`, then run `exegenius submit 0691-support-multidimensional-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
