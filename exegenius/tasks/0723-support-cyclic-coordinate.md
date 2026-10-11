# exegenius task 0723-support-cyclic-coordinate

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

Claim: The proof uses these axes twice: radix-digit coefficients are placed on several prime axes by a [Chinese-remainder map](chinese-remainder-map.md)

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "a Chinese-remainder map that preserves convolution"

Paragraph:

> A cyclic coordinate is one axis of a multidimensional [cyclic convolution](cyclic-convolution.md), with its own cyclic length. The proof uses these axes twice: radix-digit coefficients are placed on several prime axes by a [Chinese-remainder map](chinese-remainder-map.md), and a [phase twist](phase-twist.md) acts on the last axis.

### 2

Claim: The paper takes $r=2^{\lceil \log_2 T/d\rceil}$, so $d\log_2 r$ lies in $[\log_2 T,\ \log_2 T+d)$ and $\varkappa$ is an integer in $[0,d)$:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "is an integer in [0, d), so at least one axis has length r; choose it as the last axis."

Paragraph:

> The lengths are set by the [padded transform box](padded-transform-box.md) of the paper's Section 9.2.1, where each length is $r/2$ or $r$. Let $\varkappa$ be the number of coordinates of length $r/2$. The box holds $T$ entries, the box size, a power of two ($T$ here, not the three-element subsets of other pages). The product of the lengths is $(r/2)^{\varkappa}r^{d-\varkappa}=r^d/2^{\varkappa}$, so $\varkappa=d\log_2 r-\log_2 T$. The paper takes $r=2^{\lceil \log_2 T/d\rceil}$, so $d\log_2 r$ lies in $[\log_2 T,\ \log_2 T+d)$ and $\varkappa$ is an integer in $[0,d)$: Thus fewer than $d$ coordinates are shortened, so one has length $r$; it is taken last: $n_d=r$. The twist acts on this coordinate, which must have length $r$ to match $y^r+1$.

### 3

Claim: The last coordinate then becomes polynomial:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A phase twist changes the last cyclic coordinate into a polynomial"

Paragraph:

> The last coordinate then becomes polynomial: modulo $y^r+1$. Let $\zeta=e^{\pi i/r}$, a phase factor with $\zeta^r=-1$. Let $\upsilon$ be a position on the last axis, an integer from $0$ to $r-1$. The twist is diagonal, $\zeta^\upsilon$, so it multiplies the coefficient at position $\upsilon$ by $\zeta^\upsilon$. Let $\upsilon'$ be a second such position. If $\upsilon+\upsilon'\ge r$, let $\upsilon''$ be the reduced position, so $\upsilon+\upsilon'=\upsilon''+r$ with $0\le\upsilon''<r$. The product of the two twisted monomials is $\zeta^{\upsilon+\upsilon'}y^{\upsilon+\upsilon'}=(-\zeta^{\upsilon''})(-y^{\upsilon''})$, since $\zeta^r=-1$ and $y^r=-1$. The two minus signs cancel, leaving $\zeta^{\upsilon''}y^{\upsilon''}$ with no sign.

### 4

Claim: The twist is diagonal,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "multiplying coefficient k by the nonzero number"

Paragraph:

> The last coordinate then becomes polynomial: modulo $y^r+1$. Let $\zeta=e^{\pi i/r}$, a phase factor with $\zeta^r=-1$. Let $\upsilon$ be a position on the last axis, an integer from $0$ to $r-1$. The twist is diagonal, $\zeta^\upsilon$, so it multiplies the coefficient at position $\upsilon$ by $\zeta^\upsilon$. Let $\upsilon'$ be a second such position. If $\upsilon+\upsilon'\ge r$, let $\upsilon''$ be the reduced position, so $\upsilon+\upsilon'=\upsilon''+r$ with $0\le\upsilon''<r$. The product of the two twisted monomials is $\zeta^{\upsilon+\upsilon'}y^{\upsilon+\upsilon'}=(-\zeta^{\upsilon''})(-y^{\upsilon''})$, since $\zeta^r=-1$ and $y^r=-1$. The two minus signs cancel, leaving $\zeta^{\upsilon''}y^{\upsilon''}$ with no sign.

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

Write the answer to `exegenius/tasks/0723-support-cyclic-coordinate.answer.json`, then run `exegenius submit 0723-support-cyclic-coordinate` in the project directory. If submit rejects the answer, fix the answer and submit again.
