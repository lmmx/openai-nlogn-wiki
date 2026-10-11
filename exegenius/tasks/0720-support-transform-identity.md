# exegenius task 0720-support-transform-identity

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

Claim: The usual implementation of Gaussian resampling

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "sorts twice on each coordinate."

Paragraph:

> The usual implementation of Gaussian resampling This identity keeps both permutations in the formula, so they need not be The original proof uses two [label-and-sort operations](stable-radix-sort.md), This identity avoids the [label-and-sort operations](stable-radix-sort.md), since $P_s$ and $P_t$ remain in the formula.

### 2

Claim: This identity keeps both permutations in the formula, so they need not be

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "executed as separate full sorts."

Paragraph:

> The usual implementation of Gaussian resampling This identity keeps both permutations in the formula, so they need not be The original proof uses two [label-and-sort operations](stable-radix-sort.md), This identity avoids the [label-and-sort operations](stable-radix-sort.md), since $P_s$ and $P_t$ remain in the formula.

### 3

Claim: The original proof uses two [label-and-sort operations](stable-radix-sort.md),

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "each costing O(tp log t)."

Paragraph:

> The usual implementation of Gaussian resampling This identity keeps both permutations in the formula, so they need not be The original proof uses two [label-and-sort operations](stable-radix-sort.md), This identity avoids the [label-and-sort operations](stable-radix-sort.md), since $P_s$ and $P_t$ remain in the formula.

### 4

Claim: The integer product needs lengths of a different kind:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The transform lengths needed for the integer product are pairwise coprime,"

Paragraph:

> The integer product needs lengths of a different kind: whereas the synthetic The identity depends on $s$ and $t$ being [coprime](coprime.md), so it pairs a transform of length $s$ with one of length $t$. Here $F_s$ is the normalized discrete Fourier transform of length $s$, $(F_su)_k=\frac1s\sum_{j=0}^{s-1}u_je^{-2\pi ijk/s}$, and $F_t$ is the one of length $t$.

### 5

Claim: whereas the synthetic

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "transforms use powers of two."

Paragraph:

> The integer product needs lengths of a different kind: whereas the synthetic The identity depends on $s$ and $t$ being [coprime](coprime.md), so it pairs a transform of length $s$ with one of length $t$. Here $F_s$ is the normalized discrete Fourier transform of length $s$, $(F_su)_k=\frac1s\sum_{j=0}^{s-1}u_je^{-2\pi ijk/s}$, and $F_t$ is the one of length $t$.

### 6

Claim: The lemma of the source assumes $2\le\alpha<p$, $\gcd(s,t)=1$ and $\theta>p/\alpha^4$, and states:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "There are linear contractions A : Cs → Ct and B0 : Ct → Cs satisfying"

Paragraph:

> Write $\theta=t/s-1$ (the letter $\theta$ changes meaning here). The lemma of the source assumes $2\le\alpha<p$, $\gcd(s,t)=1$ and $\theta>p/\alpha^4$, and states:
> $$P_sF_s=2^{2\alpha^2}\,B_0\,P_tF_t\,A.\qquad(33)$$

### 7

Claim: The proof starts from the Gaussian identity, which the source proves:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "TPs Fs = Pt Ft S,"

Paragraph:

> The proof starts from the Gaussian identity, which the source proves: that is, $\Gamma P_sF_s=P_tF_t\Sigma$, for the resampling maps $\Gamma,\Sigma:\mathbb{C}^s\to\mathbb{C}^t$ (the source's $T$ and $S$).

### 8

Claim: The source's Gaussian estimate gives

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "∥N − I∥ < 2.01e−πα θ/2"

Paragraph:

> Let $N$ be the near-identity map of Gaussian resampling on $\mathbb{C}^s$. The source's Gaussian estimate gives, which is below $2.01e^{-\pi/2}<1/2$ once $\alpha^2\theta>1$. $\alpha^2\theta>p/\alpha^2>1$: the first inequality multiplies $\theta>p/\alpha^4$ by $\alpha^2$, the second uses $\alpha^2<p$. The invertibility of $N$ is proved with the [Neumann series](neumann-series.md): writing $N=I+E$ with $\|E\|<1$, the series $\sum_{k\ge 0}(-E)^k$ inverts $N$.

### 9

Claim: For a coordinate permutation $\Pi$, which rearranges entries by position, $(\Pi u)\cdot(\Pi u')=\Pi(u\cdot u')$, because

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "a coordinate permutation commutes with pointwise"

Paragraph:

> Permutations pass through pointwise products. For vectors $u,u'$, the pointwise product $u\cdot u'$ has entries $u_ju'_j$. For a coordinate permutation $\Pi$, which rearranges entries by position, $(\Pi u)\cdot(\Pi u')=\Pi(u\cdot u')$, because products.

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

Write the answer to `exegenius/tasks/0720-support-transform-identity.answer.json`, then run `exegenius submit 0720-support-transform-identity` in the project directory. If submit rejects the answer, fix the answer and submit again.
