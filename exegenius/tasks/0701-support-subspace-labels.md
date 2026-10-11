# exegenius task 0701-support-subspace-labels

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

Claim: The paper states that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A label is a nondegenerate subspace of a fixed bilinear"

Paragraph:

> Write $U$ for a label, a nondegenerate subspace of $E$, the fixed space with bilinear form $\langle\xi,\eta\rangle$. The paper states that space, and that labels are chosen.

### 2

Claim: space, and that labels are chosen

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "to make the changes of frame inexpensive"

Paragraph:

> Write $U$ for a label, a nondegenerate subspace of $E$, the fixed space with bilinear form $\langle\xi,\eta\rangle$. The paper states that space, and that labels are chosen.

### 3

Claim: The residual of the edge is $U\cap U'^\perp$,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the orthogonal complement of the smaller label inside the larger one"

Paragraph:

> Write $U'$ for the smaller label of an edge, so that $U'$ is contained in $U$, where $U$ is the larger label. The residual of the edge is $U\cap U'^\perp$,.

### 4

Claim: The paper defines it:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "For a nondegenerate rational subspace U ⊂ F, write PU for the projection onto U along U ⊥"

Paragraph:

> Let $\mathcal W=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ be the Hadamard matrix of order $2$, so $\mathcal W^2=I$. For a binary vector $z$, $\mathrm{hw}(z)$ is its Hamming weight, the number of ones. Labels compute their phase exponents with the [projection along a subspace](projection-along-subspace.md) $P_U$ onto $U$ along $U^\perp$, which is defined because labels are nondegenerate. The paper defines it:. Then
> $$C_U=\mathcal W^{\otimes m}\,\mathrm{diag}_x\bigl(i^{\,\mathrm{hw}(P_Ux)\bmod 4}\bigr)\,\mathcal W^{\otimes m},$$
> with $x\in\mathbb F_2^m$ an address and $\mathcal W^{\otimes m}$ the $m$-fold tensor power.

### 5

Claim: The paper writes

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Here (Xv f )(x) = f (x + v)"

Paragraph:

> Let $X_v$ be the translation $(X_vf)(x)=f(x+v)$ for a binary vector $v\in\mathbb F_2^m$; here $v$ is a binary vector, not a vertex. The paper writes. A kernel $\varpi I+\varsigma X_v$ has coefficients $\varpi,\varsigma$. The kernels implemented A Gaussian dyadic is a Gaussian integer divided by a power of two. The frame change across an edge is a product of such kernels, one for each, or its inverse.

### 6

Claim: The kernels implemented

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "below have Gaussian dyadic coefficients."

Paragraph:

> Let $X_v$ be the translation $(X_vf)(x)=f(x+v)$ for a binary vector $v\in\mathbb F_2^m$; here $v$ is a binary vector, not a vertex. The paper writes. A kernel $\varpi I+\varsigma X_v$ has coefficients $\varpi,\varsigma$. The kernels implemented A Gaussian dyadic is a Gaussian integer divided by a power of two. The frame change across an edge is a product of such kernels, one for each, or its inverse.

### 7

Claim: The frame change across an edge is a product of such kernels, one for each

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "vector in an orthonormal basis of the edge residual"

Paragraph:

> Let $X_v$ be the translation $(X_vf)(x)=f(x+v)$ for a binary vector $v\in\mathbb F_2^m$; here $v$ is a binary vector, not a vertex. The paper writes. A kernel $\varpi I+\varsigma X_v$ has coefficients $\varpi,\varsigma$. The kernels implemented A Gaussian dyadic is a Gaussian integer divided by a power of two. The frame change across an edge is a product of such kernels, one for each, or its inverse.

### 8

Claim: An edge therefore uses $\varrho$ kernels,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "including on decreasing edges."

Paragraph:

> Let $\varrho$ be the number of vectors in such a basis, $v_1,\dots,v_\varrho$, where the indices $s$ and $s'$ run over $\{1,\dots,\varrho\}$ and $v_s$ is the $s$-th vector. Orthonormality means $\langle v_s,v_{s'}\rangle=1$ if $s=s'$ and $0$ otherwise. A basis of the residual has $\dim U-\dim U'$ vectors, so $\varrho=\dim U-\dim U'$. An edge therefore uses $\varrho$ kernels,

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

Write the answer to `exegenius/tasks/0701-support-subspace-labels.answer.json`, then run `exegenius submit 0701-support-subspace-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.
