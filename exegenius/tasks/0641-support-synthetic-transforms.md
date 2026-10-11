# exegenius task 0641-support-synthetic-transforms

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

Claim: The source's main result is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "a deterministic algorithm that multiplies two n-bit integers in"

Paragraph:

> Synthetic polynomial transforms are Fourier-type transforms whose roots of unity are powers of a polynomial variable $y$, so multiplying a value by a root only moves its coefficients and changes some signs. They are the normalized Fourier transforms that the convolutions in the proof of [Integer multiplication below n log n](main-theorem.md) need, and the sign-and-shift roots make those transforms cost only moves and additions. The source's main result is $O(n(\lg n)^{1-\kappa})$ time, where $\kappa$ is a fixed positive constant.

### 2

Claim: The source says

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "These are the synthetic polynomial transforms of Nussbaumer and Quandalle"

Paragraph:

> A synthetic polynomial transform is a polynomial-ring form of the [Discrete Fourier transform](discrete-fourier-transform.md), with its roots taken in $R_r$. The source says, and attributes the method: of Nussbaumer and Quandalle.

### 3

Claim: , and attributes the method:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The polynomial roots and radix-two butterflies belong to the fast polynomial-transform method"

Paragraph:

> A synthetic polynomial transform is a polynomial-ring form of the [Discrete Fourier transform](discrete-fourier-transform.md), with its roots taken in $R_r$. The source says, and attributes the method: of Nussbaumer and Quandalle.

### 4

Claim: The source states the cost as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the transform calculation consists of address rearrangements, signed"

Paragraph:

> This replacement is a [two-point butterfly](butterfly.md): it forms the sum and the difference of two entries, after one of them is multiplied by a twiddle. Since $\gamma<\eta$, the exponent $\gamma N/(2\eta)$ is below $N$, so $\theta = y^{r\gamma/\eta}$, because $(2r/N)\cdot\gamma N/(2\eta) = r\gamma/\eta$. Thus $\theta$ is a signed shift by $r\gamma/\eta$ places. This number is an integer because $\eta$ is a power of two at most $N/2$, and $N/2$ divides $r$ since $N$ divides $2r$. Forming $\theta W$ is therefore a signed shift with no multiplication. The butterfly costs one record addition and one record subtraction, each of $r$ coefficient additions. In a complex transform the same twiddle would be a genuine complex multiplication. The source states the cost as.

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

Write the answer to `exegenius/tasks/0641-support-synthetic-transforms.answer.json`, then run `exegenius submit 0641-support-synthetic-transforms` in the project directory. If submit rejects the answer, fix the answer and submit again.
