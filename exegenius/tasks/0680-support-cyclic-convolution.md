# exegenius task 0680-support-cyclic-convolution

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

Claim: The paper notes that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional"

Paragraph:

> The first step is the coefficient layout, which follows Agarwal and Cooley's split. Write $d$ for the number of axes, and let axis $\kappa$, $1 \le \kappa \le d$, have length $n_\kappa$. A cyclic convolution of length $n = n_1 \cdots n_d$, with pairwise coprime $n_1, \dots, n_d$ (no common factor above 1), is split by the [Chinese remainder theorem](chinese-remainder-theorem.md) into a $d$-dimensional cyclic convolution. The paper notes that cyclic convolution. Its layout is motivated by the step, with coordinate powers that.

### 2

Claim: Its layout is motivated by the step

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "we first place the ordinary coefficient stream in its tensor order"

Paragraph:

> The first step is the coefficient layout, which follows Agarwal and Cooley's split. Write $d$ for the number of axes, and let axis $\kappa$, $1 \le \kappa \le d$, have length $n_\kappa$. A cyclic convolution of length $n = n_1 \cdots n_d$, with pairwise coprime $n_1, \dots, n_d$ (no common factor above 1), is split by the [Chinese remainder theorem](chinese-remainder-theorem.md) into a $d$-dimensional cyclic convolution. The paper notes that cyclic convolution. Its layout is motivated by the step, with coordinate powers that.

### 3

Claim: , with coordinate powers that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "make the change of order a sequence of controlled cyclic shifts"

Paragraph:

> The first step is the coefficient layout, which follows Agarwal and Cooley's split. Write $d$ for the number of axes, and let axis $\kappa$, $1 \le \kappa \le d$, have length $n_\kappa$. A cyclic convolution of length $n = n_1 \cdots n_d$, with pairwise coprime $n_1, \dots, n_d$ (no common factor above 1), is split by the [Chinese remainder theorem](chinese-remainder-theorem.md) into a $d$-dimensional cyclic convolution. The paper notes that cyclic convolution. Its layout is motivated by the step, with coordinate powers that.

### 4

Claim: The paper concludes:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Hence Φ is an isomorphism and preserves cyclic"

Paragraph:

> Then $\Phi(w^k) = \prod_\kappa \nu_\kappa^{\mu_\kappa k \bmod n_\kappa}$, so index $k$ lands at the position with axis exponents $\mu_\kappa k \bmod n_\kappa$. These positions are distinct for $0 \le k < n$. If $k$ and $k'$ collided, then $n_\kappa$ divides $\mu_\kappa(k-k')$ for every $\kappa$. Invertibility of $\mu_\kappa$ gives $k \equiv k' \pmod{n_\kappa}$ for every $\kappa$, and since the $n_\kappa$ are pairwise coprime, the Chinese remainder theorem gives $k \equiv k' \pmod n$, hence $k = k'$. So the $n$ images are distinct, there are $n = \prod_\kappa n_\kappa$ target monomials, and $\Phi$ is bijective. The paper concludes: convolution.

### 5

Claim: The paper's middle factor $QFt$ in equation (35) is a Fourier-type transform, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The factor QFt in (35) can be computed from a cyclic convolution"

Paragraph:

> The second step is the middle transform. Write $t$ for the even transform length, so $t$ counts the entries of each sequence transformed. Let $\omega = e^{2\pi i/t}$, and let $F_t u$ have entries $\sum_{j=0}^{t-1} \omega^{jk} u_j$. The paper's middle factor $QFt$ in equation (35) is a Fourier-type transform, and with two pointwise phase multiplications. On one axis, that is the following identity.

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

Write the answer to `exegenius/tasks/0680-support-cyclic-convolution.answer.json`, then run `exegenius submit 0680-support-cyclic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
