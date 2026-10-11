# exegenius task 0734-support-normalization-scales

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

Claim: Each output is an average of $q$ terms, each an input times a complex number of modulus one, so the transform never increases the largest modulus of its input:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "normalized Fourier transform above is a contraction"

Paragraph:

> The normalized transform $F_q$ of length $q$ sends a vector $f=(f_0,\dots,f_{q-1})$ to
> $$(F_q f)_\ell=\frac1q\sum_{s=0}^{q-1} f_s\,e^{-2\pi i s\ell/q},\qquad 0\le \ell<q,$$
> where $s$ and $\ell$ are the input and output indices. $F_q^+$ is the same sum with $e^{+2\pi i s\ell/q}$ in place of $e^{-2\pi i s\ell/q}$. Each output is an average of $q$ terms, each an input times a complex number of modulus one, so the transform never increases the largest modulus of its input:.

### 2

Claim: The paper states them as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The normalized convolution rule is Fs (u ∗ v) = S(Fs u) · (Fs v), while Fs+ Fs = I/S."

Paragraph:

> For vectors $f$ and $g$ of length $q$, let $f\ast g$ be their cyclic convolution, $(f\ast g)_\ell=\sum_{s+\nu\equiv \ell \pmod q} f_s g_\nu$, where $\nu$ is a second input index from $0$ to $q-1$, and let $f\cdot g$ be their entrywise product. Two rules hold:
> $$F_q(f\ast g)=q\,(F_qf)\cdot(F_qg),\qquad F_q^+F_q=\tfrac1q\,I,$$
> where $I$ is the identity. The paper states them as with $S$ read as $q$.

### 3

Claim: Here $p$ is the precision, with grid spacing $2^{-p}$, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Their coefficients are exact p-bit grid values of norm less than 1/4."

Paragraph:

> The digits carry a second scale. Let $\hat f$ and $\hat g$ be the integer digit arrays of the two inputs, with entries from $0$ to $2^b-1$, where $b$ is the digit width. The algorithm stores each entry as $\sigma$ times its digit, with the digit scale $\sigma=2^{-b-2}$, so the stored arrays are $f=\sigma\hat f$ and $g=\sigma\hat g$. Each stored value then has modulus below $\sigma 2^b=\frac14$. Here $p$ is the precision, with grid spacing $2^{-p}$, and

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

Write the answer to `exegenius/tasks/0734-support-normalization-scales.answer.json`, then run `exegenius submit 0734-support-normalization-scales` in the project directory. If submit rejects the answer, fix the answer and submit again.
