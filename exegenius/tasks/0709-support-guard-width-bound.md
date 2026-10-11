# exegenius task 0709-support-guard-width-bound

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

Claim: The bound keeps every intermediate value in [Gaussian dyadics](gaussian-dyadics.md), since

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Intermediate values are exact Gaussian dyadics"

Paragraph:

> The bound keeps every intermediate value in [Gaussian dyadics](gaussian-dyadics.md), since, so both denominators and magnitudes need limits. The paper starts with, where $p$ is the fractional precision.

### 2

Claim: The paper starts with

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "disk-valued coefficients in 2−p Z[i]"

Paragraph:

> The bound keeps every intermediate value in [Gaussian dyadics](gaussian-dyadics.md), since, so both denominators and magnitudes need limits. The paper starts with, where $p$ is the fractional precision.

### 3

Claim: The claim is that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "value at depth ℓ lies in 2−(p+ℓ) Z[i] and has modulus at most 2ℓ"

Paragraph:

> Let $\ell$ be the depth of a value, the number of operations on a chain that follows an operand from an input into it. The claim is that. Inputs have depth $0$. An operand of depth at most $\ell-1$ lies in $2^{-(p+\ell-1)}\mathbb{Z}[i]$ with modulus at most $2^{\ell-1}$, so a sum or difference of two such operands lies in $2^{-(p+\ell)}\mathbb{Z}[i]$ with modulus at most $2^\ell$, and a halving lies there with modulus at most $2^{\ell-2}$. For example, with $p=10$, $u=1$ and $v=2^{-10}$, the depth-2 value $(u+v)/2=(2^{10}+1)/2^{11}$ needs eleven fractional bits, so twelve reserved bits suffice.

### 4

Claim: Then

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A(e) ≤ sA(e/m) + E"

Paragraph:

> Each call divides the axis count by $m$, the splitting factor. A group of $e$ selected axes splits into $s$ calls on groups of $e/m$ axes. Let $A(e)$ bound the operations on any chain within such a group, and let $E=64(W+m+1)^3$ be the most gate operations charged at a node. Then at an internal node, and $A(e)\le 8e$ at a leaf. Let $k$ count the internal levels:

### 5

Claim: Let $k$ count the internal levels:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "There are at most k ≤ ⌈logm d⌉ internal levels."

Paragraph:

> Each call divides the axis count by $m$, the splitting factor. A group of $e$ selected axes splits into $s$ calls on groups of $e/m$ axes. Let $A(e)$ bound the operations on any chain within such a group, and let $E=64(W+m+1)^3$ be the most gate operations charged at a node. Then at an internal node, and $A(e)\le 8e$ at a leaf. Let $k$ count the internal levels:

### 6

Claim: Preprocessing adds at most $md$ earlier pieces,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "For the sufficiently large sizes under consideration, the earlier piece count is at most md."

Paragraph:

> Preprocessing adds at most $md$ earlier pieces, each of depth at most $8B^2d^{\nu+1}$, so their depths add to at most $8mB^2d^{\nu+2}$. The at most $d$ individual kernels, each of depth $8$, add $8d$. The two outer phases cost two operations each, the scalar phase two and one optional factor three, so phases add at most $9$.

### 7

Claim: Here $C_0=128mB^2$ and $C_1=\max\{20,\nu+3\}$;

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the choice twenty leaves an explicit additional margin"

Paragraph:

> Here $\lfloor x\rfloor$ is the largest integer not exceeding $x$, and the shift is by $t=\lfloor D/2\rfloor$ places.. Here $C_0=128mB^2$ and $C_1=\max\{20,\nu+3\}$;. Adding the counts,
> $$8mB^2d^{\nu+2}+8d+t+9\le 8mB^2d^{\nu+2}+18d\le 26mB^2d^{\nu+2}<128mB^2d^{\nu+3}\le C_0d^{C_1},$$
> using $d\ge1$, $mB^2\ge1$ and $C_1\ge\nu+3$. So every depth is at most $C_0d^{C_1}$, and $\Delta=\lceil C_0d^{C_1}\rceil$ bounds it.

### 8

Claim: The exponent $\varepsilon$ is chosen with $0<\varepsilon<1$ and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Choose ϵC1 < 1"

Paragraph:

> The exponent $\varepsilon$ is chosen with $0<\varepsilon<1$ and. The bound states the growth of $d$ with [Big-Theta notation](big-theta-notation.md): $d$ lies between two constant multiples of $p^{\varepsilon}$. Since $W$, $m$ and $s$ are fixed, $\Delta=O(p^{\varepsilon C_1})$. The bound states growth in the sense of [little-o notation](little-o-notation.md): $\Delta=o(p)$ means $\Delta/p\to0$, which holds because $\varepsilon C_1<1$.

### 9

Claim: Truncation (rounding toward zero to $2^{-p}\mathbb{Z}$) is safe:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "truncation cannot increase the absolute value of either component, and changes each by less than"

Paragraph:

> Truncation (rounding toward zero to $2^{-p}\mathbb{Z}$) is safe: $2^{-p}$.

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

Write the answer to `exegenius/tasks/0709-support-guard-width-bound.answer.json`, then run `exegenius submit 0709-support-guard-width-bound` in the project directory. If submit rejects the answer, fix the answer and submit again.
