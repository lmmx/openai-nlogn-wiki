# exegenius task 0169-support-fixed-point-precision

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

Claim: The source sets $p=6b$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "p=6b"

Paragraph:

> Each complex coefficient is stored as a pair of integer numerators $X$ over $2^p$, where $p$ is the working precision in bits; a numerator $X$ represents $X/2^p$. Scalings by known integers and powers of two are exact on numerators, so the only inexact steps are transforms, pointwise products and truncations. The source sets $p=6b$, where $b=\lceil\log_2 n\rceil$, so $n\le 2^b$.

### 2

Claim: , where $b=\lceil\log_2 n\rceil$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "b=\lceil\log_2n\rceil"

Paragraph:

> Each complex coefficient is stored as a pair of integer numerators $X$ over $2^p$, where $p$ is the working precision in bits; a numerator $X$ represents $X/2^p$. Scalings by known integers and powers of two are exact on numerators, so the only inexact steps are transforms, pointwise products and truncations. The source sets $p=6b$, where $b=\lceil\log_2 n\rceil$, so $n\le 2^b$.

### 3

Claim: Hence
$$\Phi^{+}(\Phi\xi\cdot\Phi\psi)=\frac1S\,\Phi^{+}\Phi(\xi*\psi)=\frac{\xi*\psi}{S^2}.$$
The source's transforms also carry a coordinate permutation, which cancels from this product

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "retained source permutation $R$ cancels when computing a convolution"

Paragraph:

> Let $\xi_j=x_j/2^{b+2}$ and $\psi_j=y_j/2^{b+2}$; each entry lies in $[0,1/4)$. Let $\Phi$ be the forward transform of length $S$, with $(\Phi\xi)_m=\frac1S\sum_k\xi_k\omega^{mk}$, where $\omega$ is a primitive $S$-th root of unity, and let $\Phi^{+}$ be its opposite, with $\omega^{-mk}$ in its place. Two identities hold: $\Phi(\xi*\psi)=S\,\Phi\xi\cdot\Phi\psi$, since powers of $\omega$ multiply by adding exponents mod $S$; and $\Phi^{+}\Phi=I/S$, since $\sum_m\omega^{m(k-k')}$ is $S$ for $k=k'$ and $0$ otherwise. Hence
> $$\Phi^{+}(\Phi\xi\cdot\Phi\psi)=\frac1S\,\Phi^{+}\Phi(\xi*\psi)=\frac{\xi*\psi}{S^2}.$$
> The source's transforms also carry a coordinate permutation, which cancels from this product, so the identity holds for the transforms written here.

### 4

Claim: Each computed transform, after the source scale $2^\gamma$, has error below $E_s2^{-p}$ with $E_s=9\cdot 2^\gamma TL$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "E_s=9\,2^\gamma TL"

Paragraph:

> Each computed transform, after the source scale $2^\gamma$, has error below $E_s2^{-p}$ with $E_s=9\cdot 2^\gamma TL$; here $\gamma$ is the exponent of that scale (this letter changes meaning from the scratch-restoration page). Each factor of the pointwise product contributes $E_s2^{-p}$ and truncation adds $2\cdot2^{-p}$, and the opposite transform adds $E_s2^{-p}$ more, so the computed $\Phi^{+}$ result is within $(3E_s+2)2^{-p}$ of $(\xi*\psi)/S^2$. Multiplying by $S$ multiplies this error by $S$: it is below $S(3E_s+2)2^{-p}<28\cdot2^\gamma T^2L\cdot2^{-p}$, since $3E_s+2=27\cdot2^\gamma TL+2<28\cdot2^\gamma TL$. The second scaling by $2^{2b+4}S$ and $2^{-p}=2^{-6b}$ give a coefficient error below
> $$2^{2b+4}S\cdot 28\cdot2^\gamma T^2L\cdot2^{-6b}<448\,b\,2^{-b+\gamma}\le 448\,b\,2^{-3b/4},$$
> using $S<T<2^b$, $L<b$, and $\gamma\le b/4$ for large $b$. For large $b$ this is below $\tfrac12$. The coefficient $c_j=2^{2b+4}(\xi*\psi)_j$ is an integer, so rounding each computed value returns $c_j$ exactly.

### 5

Claim: The second scaling by $2^{2b+4}S$ and $2^{-p}=2^{-6b}$ give a coefficient error below
$$2^{2b+4}S\cdot 28\cdot2^\gamma T^2L\cdot2^{-6b}<448\,b\,2^{-b+\gamma}\le 448\,b\,2^{-3b/4},$$
using $S<T<2^b$, $L<b$, and $\gamma\le b/4$ for large $b$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "For example $b\ge2^{24}$ implies $\gamma\le b/4$."

Paragraph:

> Each computed transform, after the source scale $2^\gamma$, has error below $E_s2^{-p}$ with $E_s=9\cdot 2^\gamma TL$; here $\gamma$ is the exponent of that scale (this letter changes meaning from the scratch-restoration page). Each factor of the pointwise product contributes $E_s2^{-p}$ and truncation adds $2\cdot2^{-p}$, and the opposite transform adds $E_s2^{-p}$ more, so the computed $\Phi^{+}$ result is within $(3E_s+2)2^{-p}$ of $(\xi*\psi)/S^2$. Multiplying by $S$ multiplies this error by $S$: it is below $S(3E_s+2)2^{-p}<28\cdot2^\gamma T^2L\cdot2^{-p}$, since $3E_s+2=27\cdot2^\gamma TL+2<28\cdot2^\gamma TL$. The second scaling by $2^{2b+4}S$ and $2^{-p}=2^{-6b}$ give a coefficient error below
> $$2^{2b+4}S\cdot 28\cdot2^\gamma T^2L\cdot2^{-6b}<448\,b\,2^{-b+\gamma}\le 448\,b\,2^{-3b/4},$$
> using $S<T<2^b$, $L<b$, and $\gamma\le b/4$ for large $b$. For large $b$ this is below $\tfrac12$. The coefficient $c_j=2^{2b+4}(\xi*\psi)_j$ is an integer, so rounding each computed value returns $c_j$ exactly.

### 6

Claim: For large $b$ this is below $\tfrac12$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "448b\,2^{-3b/4}<\frac12"

Paragraph:

> Each computed transform, after the source scale $2^\gamma$, has error below $E_s2^{-p}$ with $E_s=9\cdot 2^\gamma TL$; here $\gamma$ is the exponent of that scale (this letter changes meaning from the scratch-restoration page). Each factor of the pointwise product contributes $E_s2^{-p}$ and truncation adds $2\cdot2^{-p}$, and the opposite transform adds $E_s2^{-p}$ more, so the computed $\Phi^{+}$ result is within $(3E_s+2)2^{-p}$ of $(\xi*\psi)/S^2$. Multiplying by $S$ multiplies this error by $S$: it is below $S(3E_s+2)2^{-p}<28\cdot2^\gamma T^2L\cdot2^{-p}$, since $3E_s+2=27\cdot2^\gamma TL+2<28\cdot2^\gamma TL$. The second scaling by $2^{2b+4}S$ and $2^{-p}=2^{-6b}$ give a coefficient error below
> $$2^{2b+4}S\cdot 28\cdot2^\gamma T^2L\cdot2^{-6b}<448\,b\,2^{-b+\gamma}\le 448\,b\,2^{-3b/4},$$
> using $S<T<2^b$, $L<b$, and $\gamma\le b/4$ for large $b$. For large $b$ this is below $\tfrac12$. The coefficient $c_j=2^{2b+4}(\xi*\psi)_j$ is an integer, so rounding each computed value returns $c_j$ exactly.

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

Write the answer to `exegenius/tasks/0169-support-fixed-point-precision.answer.json`, then run `exegenius submit 0169-support-fixed-point-precision` in the project directory. If submit rejects the answer, fix the answer and submit again.
