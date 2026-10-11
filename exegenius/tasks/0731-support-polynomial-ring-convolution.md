# exegenius task 0731-support-polynomial-ring-convolution

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

Claim: The paper uses one layout,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the forward entry with frequency address j is stored at L(Bj)"

Paragraph:

> The product pairs frequency $j$ of $\varphi$ with frequency $j$ of $\psi$ only if both transforms store each frequency at the same position. The paper uses one layout,, where the $B$ is the paper's layout map, not the base below. operands, so the product is formed in stored order, and the opposite transform.

### 2

Claim: operands, so the product is formed in stored order, and the opposite transform

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "consumes that same order after a pointwise product"

Paragraph:

> The product pairs frequency $j$ of $\varphi$ with frequency $j$ of $\psi$ only if both transforms store each frequency at the same position. The paper uses one layout,, where the $B$ is the paper's layout map, not the base below. operands, so the product is formed in stored order, and the opposite transform.

### 3

Claim: Each input is a disk array, which

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "has norm at most one."

Paragraph:

> Each input is a disk array, which Let $\varphi_1$ and $\varphi_2$ be the real and imaginary integer polynomials of $\varphi$, and let $\psi_1$ and $\psi_2$ be those of $\psi$. Then $\varphi=2^{-p}(\varphi_1+i\varphi_2)$ and $\psi=2^{-p}(\psi_1+i\psi_2)$, with all four of degree less than $r$ and coefficients of absolute value at most $2^p$. Then $\varphi\psi=2^{-2p}N$ with $N=(\varphi_1\psi_1-\varphi_2\psi_2)+i(\varphi_1\psi_2+\varphi_2\psi_1)$. Four integer products, $\varphi_1(B)\psi_1(B)$, $\varphi_2(B)\psi_2(B)$, $\varphi_1(B)\psi_2(B)$ and $\varphi_2(B)\psi_1(B)$, give the four polynomial products. Signs are handled by

### 4

Claim: Signs are handled by

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Multiply the four pairs of absolute values using the established multiplier and restore each product’s sign."

Paragraph:

> Each input is a disk array, which Let $\varphi_1$ and $\varphi_2$ be the real and imaginary integer polynomials of $\varphi$, and let $\psi_1$ and $\psi_2$ be those of $\psi$. Then $\varphi=2^{-p}(\varphi_1+i\varphi_2)$ and $\psi=2^{-p}(\psi_1+i\psi_2)$, with all four of degree less than $r$ and coefficients of absolute value at most $2^p$. Then $\varphi\psi=2^{-2p}N$ with $N=(\varphi_1\psi_1-\varphi_2\psi_2)+i(\varphi_1\psi_2+\varphi_2\psi_1)$. Four integer products, $\varphi_1(B)\psi_1(B)$, $\varphi_2(B)\psi_2(B)$, $\varphi_1(B)\psi_2(B)$ and $\varphi_2(B)\psi_1(B)$, give the four polynomial products. Signs are handled by

### 5

Claim: Write $r=2^\ell$ with $\ell<p$;

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Let r = 2ℓ < 2p with integers"

Paragraph:

> Let $h=\varphi_1\psi_1$, with coefficients $h_j$. Each $h_j$ is a sum of at most $r$ products of integers bounded by $2^p$, so $|h_j|\le r2^{2p}$. Write $r=2^\ell$ with $\ell<p$; gives $r<2^p$. A real numerator coefficient is a sum of at most $2r$ such products, so it is below $2r\cdot2^{2p}<2^{3p+1}\le2^{4p-1}=B/2$ for $p\ge2$. So the blocks of $h(B)=\sum_j h_jB^j$ do not overlap.

### 6

Claim: So

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "subtract the coefficient at j + r from the one at j"

Paragraph:

> Since $y^r=-1$, the coefficient at $j+r$ wraps to position $j$ with a minus sign. So for $0\le j<r$. This reduces $N$ modulo $y^r+1$, and dividing its coefficients by $r2^{2p}$ gives $\varphi\psi/r$ exactly. Then $Q_p$ truncates the real and imaginary part of each coefficient toward zero to $2^{-p}\mathbb Z$, so the output lies on the $2^{-p}$ grid that the next step reads in fixed width.

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

Write the answer to `exegenius/tasks/0731-support-polynomial-ring-convolution.answer.json`, then run `exegenius submit 0731-support-polynomial-ring-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
