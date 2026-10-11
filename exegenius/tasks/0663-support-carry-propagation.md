# exegenius task 0663-support-carry-propagation

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

Claim: The paper sets $b$ this way for sufficiently large $n$:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "b = ⌈log2 n⌉"

Paragraph:

> Carry propagation takes its digit width $b = \lceil \log_2 n \rceil$ from the [base-2 logarithm](base-two-logarithm.md) of $n$. The paper sets $b$ this way for sufficiently large $n$:. Carry propagation computes its digit count by the [ceiling function](ceiling-function.md): $N = \lceil n/b \rceil$ is the number of digits in each input (the paper writes $q$ for $N$).

### 2

Claim: The paper states the same bound:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "0 ≤ cj ≤ q(2b − 1)2 < 23b"

Paragraph:

> Each $c_t$ is a sum of at most $N$ products of two digits, each at most $(Q_0-1)^2$, so $0 \le c_t \le N(Q_0-1)^2 < NQ_0^2 \le Q_0^3$. The paper states the same bound:.

### 3

Claim: The paper gives the same order, to

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Propagate radix-2b carries in increasing coefficient order"

Paragraph:

> The recurrence reads $c_t$ only after $\gamma_t$ is known, and $\gamma_t$ depends on all lower coefficients, so the positions must be processed from $t = 0$ upward. The paper gives the same order, to, and.

### 4

Claim: , and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "so this carry scan proceeds from least to most significant"

Paragraph:

> The recurrence reads $c_t$ only after $\gamma_t$ is known, and $\gamma_t$ depends on all lower coefficients, so the positions must be processed from $t = 0$ upward. The paper gives the same order, to, and.

### 5

Claim: The leftover carry is written out the same way:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "drain the final O(b)-bit carry in the same order"

Paragraph:

> Coefficients vanish past the end. The product of two polynomials of degree $N-1$ has degree at most $2N-2$, so $c_t = 0$ for $t \ge 2N-1$. Then $\gamma_{2N-1} < Q_0^2$ gives $\gamma_{2N} \le Q_0-1$, and $\gamma_{2N+1} = 0$. The leftover carry is written out the same way:. Its digits are $\sigma_{2N-1}$ and $\sigma_{2N}$, and $\sigma_t = 0$ for $t \ge 2N+1$, since then $c_t + \gamma_t = 0$. Taking $\tau = 2N+1$ in the identity, where every $c_t$ with $t \ge 2N+1$ is zero, gives $\sum_t c_t Q_0^t = \sum_t \sigma_t Q_0^t$. Each $\sigma_t$ lies in $\{0, \dots, Q_0-1\}$, so it is a $b$-bit block. Writing $\sigma_{2N}, \dots, \sigma_0$ from the top, each in $b$ bits, gives a binary string whose value is the product.

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

Write the answer to `exegenius/tasks/0663-support-carry-propagation.answer.json`, then run `exegenius submit 0663-support-carry-propagation` in the project directory. If submit rejects the answer, fix the answer and submit again.
