# exegenius task 0735-support-middle-transform

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

Claim: Gaussian resampling bridges the two: it

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "expresses each source Fourier transform through a power-of-two tensor transform."

Paragraph:

> The reason for the target length is the shape of the transforms., whereas the synthetic transforms use powers of two. Gaussian resampling bridges the two: it

### 2

Claim: Write $s$ for the source length and $t$ for the target length, with

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "gcd(s, t) = 1"

Paragraph:

> Write $s$ for the source length and $t$ for the target length, with, and let $t$ be even. Let $F_t$ be the normalized discrete Fourier transform of length $t$, with input index $j$ and output index $k$, both running over $\{0,\dots,t-1\}$:
> $$(F_tu)_k=\frac1t\sum_{j=0}^{t-1}u_j\,e^{-2\pi i jk/t}.$$
> A coordinate permutation is a reindexing of the entries of a vector, and the sources use the reindexing $k\mapsto -sk \bmod t$ on outputs. that map. The middle transform $\mathcal M_t$ is the operator defined by $(\mathcal M_t u)_k=(F_t u)_{-sk \bmod t}$. Since $e^{-2\pi i j(-sk)/t}=e^{2\pi i sjk/t}$, it can be written directly as
> $$(\mathcal M_t u)_k=\frac1t\sum_{j=0}^{t-1}u_j\,e^{2\pi i sjk/t}.$$
> So $\mathcal M_t$ is a discrete Fourier transform whose frequency is multiplied by $-s$.

### 3

Claim: The method therefore shows its claim:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The factor QFt in (35) can be computed from a cyclic convolution and two pointwise phase"

Paragraph:

> The middle transform is computed through [Bluestein's chirp identity](bluestein-chirp-identity.md), which writes it as this cyclic convolution with phases. For each integer $j$, let $\varsigma_j=\exp(-\pi i s j^2/t)$ be the chirp factor. Because $t$ is even, $\varsigma_{j+t}=\varsigma_j$, and $|\varsigma_j|=1$. A pointwise phase multiplication multiplies each entry by a complex number of modulus one, so multiplying by $\varsigma_j$ or by its complex conjugate $\overline{\varsigma_j}$ is one. The identity $2jk=j^2+k^2-(j-k)^2$ gives
> $$\overline{\varsigma_k}\,\varsigma_{k-j}\,\overline{\varsigma_j}=\exp\Big(\pi i s\,\frac{k^2-(k-j)^2+j^2}{t}\Big)=e^{2\pi i sjk/t},$$
> and therefore
> $$(\mathcal M_t u)_k=\frac{\overline{\varsigma_k}}{t}\sum_{j=0}^{t-1}\varsigma_{k-j}\,\big(\overline{\varsigma_j}\,u_j\big).$$
> The sum is a cyclic convolution of $\varsigma$ with the phase-multiplied input $\overline{\varsigma_j}u_j$. The method therefore shows its claim: multiplications. Here $\mathrm{QFt}$ is the paper's name for this operator, and the middle transform is one cyclic convolution bracketed by two phase multiplications, one before and one after.

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

Write the answer to `exegenius/tasks/0735-support-middle-transform.answer.json`, then run `exegenius submit 0735-support-middle-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
