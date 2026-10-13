# exegenius task 0198-support-fixed-tape-multiplication

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

Claim: Its worst-case time is $O(n(\lg n)^{1-\kappa})$, with $\kappa=2^{-182}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$\kappa=2^{-182}$"

Paragraph:

> Its worst-case time is $O(n(\lg n)^{1-\kappa})$, with $\kappa=2^{-182}$. It achieves a [Power saving in the logarithmic factor](power-saving.md), which puts its time below $n\log n$ by a power of $\lg n$. It disproves the [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md) in this model.

### 2

Claim: The digit width is $b=\lceil\log_2 n\rceil$ and the precision is $p=6b$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$p=6b$"

Paragraph:

> The digit width is $b=\lceil\log_2 n\rceil$ and the precision is $p=6b$, the number of bits kept after each rounding. The digit width must grow for the rounding error to fall (see below), yet only as $\lg n$, so $p$ is of order $\lg n$. The stored volume $V=\Theta(n)$ holds about $n/b$ records of $p$ bits each.

### 3

Claim: A swap costs $O(Vu^{\tau})$ time

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$O(Vu^\tau)$"

Paragraph:

> It packs signed coefficients by [Signed coefficient packing](signed-packing.md), so that polynomial products become integer products. It computes its shorter products by the [Established fast multiplier](multiplier-subroutine.md), used as a black box. It recovers the exact binary product by [Exact recovery by rounding and carries](exact-recovery.md). It carries out its address rearrangements by [Fast interchange of address chunks](tape-interchange.md), which swaps two equal-width address fields of width $u$. A swap costs $O(Vu^{\tau})$ time, a power of the width.

### 4

Claim: The error is at most $448b\,2^{-3b/4}$, which is below $1/2$ for $b$ beyond a fixed cutoff

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "448b\,2^{-3b/4}<\frac12"

Paragraph:

> Here $2^{2b+4}$ reverses the digit scales, $2^{b}$ and $2^{2b}$ bound the record count and its square, $2^{-6b}=2^{-p}$ is the resolution of stored values, and $2^{b/4}$ bounds the remaining factor once $b\ge 2^{24}$. The factor $b$ counts carries. The error is at most $448b\,2^{-3b/4}$, which is below $1/2$ for $b$ beyond a fixed cutoff. The true coefficients are integers, so the nearest integer to each computed value is the true coefficient.

### 5

Claim: The true coefficients are integers, so the nearest integer to each computed value is the true coefficient

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The strict error below $1/2$ makes the nearest integer to"

Paragraph:

> Here $2^{2b+4}$ reverses the digit scales, $2^{b}$ and $2^{2b}$ bound the record count and its square, $2^{-6b}=2^{-p}$ is the resolution of stored values, and $2^{b/4}$ bounds the remaining factor once $b\ge 2^{24}$. The factor $b$ counts carries. The error is at most $448b\,2^{-3b/4}$, which is below $1/2$ for $b$ beyond a fixed cutoff. The true coefficients are integers, so the nearest integer to each computed value is the true coefficient.

### 6

Claim: The paper's table bounds the power of $p$ in each of seven dominant costs $V p^{e}$ by $1-2\kappa$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Each of the seven displayed powers is at most $1-2\kappa$"

Paragraph:

> The paper's table bounds the power of $p$ in each of seven dominant costs $V p^{e}$ by $1-2\kappa$. The margin $1-e$ is smallest, $2\kappa$, for the chunk-exchange row. So the seven terms sum to $O(Vp^{1-2\kappa}(\log p)^{O(1)})$, and since $(\log p)^{O(1)}\le p^{\kappa}$ for large $p$, the cost is $O(Vp^{1-\kappa})=O(n(\lg n)^{1-\kappa})$.

### 7

Claim: The margin $1-e$ is smallest, $2\kappa$, for the chunk-exchange row

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "2^{-181}=2\kappa"

Paragraph:

> The paper's table bounds the power of $p$ in each of seven dominant costs $V p^{e}$ by $1-2\kappa$. The margin $1-e$ is smallest, $2\kappa$, for the chunk-exchange row. So the seven terms sum to $O(Vp^{1-2\kappa}(\log p)^{O(1)})$, and since $(\log p)^{O(1)}\le p^{\kappa}$ for large $p$, the cost is $O(Vp^{1-\kappa})=O(n(\lg n)^{1-\kappa})$.

### 8

Claim: This factor is below the swap's gain $m^{\tau}$: $s/W<m^{\tau}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$s/W<m^\tau$"

Paragraph:

> The width falls by a factor $m$ at each recursion level: at depth $d$ the width is $m^{d}$, where $m$, a fixed integer, is that factor; this letter changes meaning here. Each recursive call acts on one role stream of volume $V/W$, and there are $s$ smaller calls, so each level multiplies the cost per unit volume by $s/W$. This factor is below the swap's gain $m^{\tau}$: $s/W<m^{\tau}$. Summing over the levels gives

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

Write the answer to `exegenius/tasks/0198-support-fixed-tape-multiplication.answer.json`, then run `exegenius submit 0198-support-fixed-tape-multiplication` in the project directory. If submit rejects the answer, fix the answer and submit again.
