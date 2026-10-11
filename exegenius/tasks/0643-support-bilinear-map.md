# exegenius task 0643-support-bilinear-map

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

Claim: For arrays whose entries are records (polynomials in $y$ modulo $y^r+1$), the norm is the largest coefficient modulus:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "over Rr , the same notation denotes the maximum over all coefficients in all entries."

Paragraph:

> In the paper, $U$, $V$, and $W$ are spaces of [Array](array.md) values, so a bilinear map is applied to arrays. A bilinear map is a *bilinear contraction* when it is bounded in the [Array norm](array-norm.md): $\|\pi(\xi,\zeta)\|\le\|\xi\|\,\|\zeta\|$. For arrays whose entries are records (polynomials in $y$ modulo $y^r+1$), the norm is the largest coefficient modulus: A *disk array* is an array of norm at most one, so every entry has modulus at most one.

### 2

Claim: the bound $\|P(\xi,\zeta)\|\le\|\xi\|\,\|\zeta\|$,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "by the coefficient bound in"

Paragraph:

> The paper's error analysis works with an exact bilinear map $P$: the pointwise product, which multiplies the two entries at each address, with products of records taken modulo $y^r+1$ and then divided by $r$. the bound $\|P(\xi,\zeta)\|\le\|\xi\|\,\|\zeta\|$, Lemma 17, so $P$ is a bilinear contraction.

### 3

Claim: So

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "replacing one operand changes the output by at most the norm"

Paragraph:

> Let $\xi'$ and $\zeta'$ be computed approximations of $\xi$ and $\zeta$, and suppose all four are disk arrays. With one operand fixed, linearity gives $\pi(\xi',\zeta)-\pi(\xi,\zeta)=\pi(\xi'-\xi,\zeta)$, and if $\zeta$ is a disk array, $\|\pi(\xi'-\xi,\zeta)\|\le\|\xi'-\xi\|$. So of the difference.

### 4

Claim: Adding them gives
$$\|\pi(\xi',\zeta')-\pi(\xi,\zeta)\|\le\|\xi'-\xi\|+\|\zeta'-\zeta\|.$$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "When all four operands are in the disk, their two errors therefore add."

Paragraph:

> Splitting the change into two single-operand changes,
> $$\pi(\xi',\zeta')-\pi(\xi,\zeta)=\pi(\xi'-\xi,\zeta')+\pi(\xi,\zeta'-\zeta).$$
> The first term is bounded using the disk bound on $\zeta'$: $\|\pi(\xi'-\xi,\zeta')\|\le\|\xi'-\xi\|\,\|\zeta'\|\le\|\xi'-\xi\|$. The second is bounded by the disk bound on $\xi$: $\|\pi(\xi,\zeta'-\zeta)\|\le\|\xi\|\,\|\zeta'-\zeta\|\le\|\zeta'-\zeta\|$. Adding them gives
> $$\|\pi(\xi',\zeta')-\pi(\xi,\zeta)\|\le\|\xi'-\xi\|+\|\zeta'-\zeta\|.$$

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

Write the answer to `exegenius/tasks/0643-support-bilinear-map.answer.json`, then run `exegenius submit 0643-support-bilinear-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
