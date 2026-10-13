# exegenius task 0166-support-gaussian-resampling

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

Claim: Gaussian resampling is the reduction of Harvey and van der Hoeven that replaces each prime-length Fourier transform needed for a convolution

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "by multidimensional transforms whose axis lengths are powers of two"

Paragraph:

> Gaussian resampling is the reduction of Harvey and van der Hoeven that replaces each prime-length Fourier transform needed for a convolution. A standard FFT of length $2m$ splits into two transforms of length $m$. A prime-length transform has no such split.

### 2

Claim: Each normalized transform is a contraction

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "since each output averages inputs multiplied by complex numbers of modulus one"

Paragraph:

> Let $p$ be the length of a prime axis, the number of entries in a list on that axis, and let $Q$ be a power of two, the number of entries in the list that replaces it, chosen slightly above $p$. Let $F_p$ and $F_Q$ be the normalized discrete Fourier transforms, $(F_p f)_k=\frac1p\sum_{j=0}^{p-1}f_j e^{-2\pi i jk/p}$ and likewise $F_Q$. Let $\pi_p$ and $\pi_Q$ be the coordinate reorderings used in the paper's identity. A contraction is a linear map that does not increase the largest modulus of an entry. Each normalized transform is a contraction.

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

Write the answer to `exegenius/tasks/0166-support-gaussian-resampling.answer.json`, then run `exegenius submit 0166-support-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
