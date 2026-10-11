# exegenius task 0685-support-opposite-transform

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

Claim: The source states this as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "conjugation changes the negative Fourier sign to the positive one"

Paragraph:

> For a vector $u$ of $q$ complex numbers, indexed by $j$ and $\ell$ from $0$ to $q-1$,
> $$(F_q^+ u)_\ell = \frac{1}{q}\sum_{j=0}^{q-1} \omega^{-j\ell}\, u_j, \qquad \omega = e^{-2\pi i/q}.$$
> The forward transform $F_q$ uses $\omega^{j\ell}$ in its place, with the same factor $1/q$. The source states this as.

### 2

Claim: The paper, *Integer multiplication below n log n*, uses the same sign convention for its synthetic transforms, whose entries are

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "short polynomials in a quotient where the required roots of unity act by exact signed permutations"

Paragraph:

> The paper, *Integer multiplication below n log n*, uses the same sign convention for its synthetic transforms, whose entries are. It writes the roots as.

### 3

Claim: It writes the roots as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "define ωt = y 2r/t"

Paragraph:

> The paper, *Integer multiplication below n log n*, uses the same sign convention for its synthetic transforms, whose entries are. It writes the roots as.

### 4

Claim: The paper states the result as two normalized synthetic forwards, pointwise

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "polynomial multiplication divided by r, and the normalized opposite transform give"

Paragraph:

> Let $f$ and $g$ be two [disk-grid ring arrays](array.md), whose entries are polynomials of degree less than $r$. The synthetic opposite transform acts on each [array](array.md) along its axes. Write $M$ for the number of cyclic addresses of each array; the letter $M$ changes meaning here. Here $f\ast g$ is the cyclic convolution along each axis, with wrap-around past $y^r$ contributing a sign. The paper states the result as two normalized synthetic forwards, pointwise $(f\ast g)/(rM^2)$.

### 5

Claim: , because

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the opposite transform consumes that order."

Paragraph:

> The product must keep the frequency order, which is the order in which a transform stores its entries by frequency., because

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

Write the answer to `exegenius/tasks/0685-support-opposite-transform.answer.json`, then run `exegenius submit 0685-support-opposite-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
