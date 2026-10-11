# exegenius task 0726-support-cost-table

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

Claim: It is the step that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "makes all terms in its cost table fit Theorem 1."

Paragraph:

> The cost table is the last accounting step of the proof. It lists the separate running-time terms of the algorithm, each a power of one size parameter, whose sum bounds the total time. It is the step that

### 2

Claim: Write $p = 6b$ for the working precision in bits (

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "p = 6b"

Paragraph:

> Write $b = \lceil \log_2 n \rceil$ for the rounded-up base-2 logarithm of $n$, the number of bits of $n$ (the letter $b$ changes meaning here). Write $p = 6b$ for the working precision in bits (), so $p = \Theta(\log n)$. Write $T$ for the number of cells of the padded box (the letter $T$ changes meaning here). The paper takes, so $4n/b \le T < 8n/b$. Since $2^{b-1} < n \le 2^b$ and $b \ge 8$, we have $4n/b > 2^{b/2}$ and $8n/b \le 2^b$, so $b/2 < \log_2 T < b$.

### 3

Claim: The paper takes

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Take the power of two T in [4n/b, 8n/b)"

Paragraph:

> Write $b = \lceil \log_2 n \rceil$ for the rounded-up base-2 logarithm of $n$, the number of bits of $n$ (the letter $b$ changes meaning here). Write $p = 6b$ for the working precision in bits (), so $p = \Theta(\log n)$. Write $T$ for the number of cells of the padded box (the letter $T$ changes meaning here). The paper takes, so $4n/b \le T < 8n/b$. Since $2^{b-1} < n \le 2^b$ and $b \ge 8$, we have $4n/b > 2^{b/2}$ and $8n/b \le 2^b$, so $b/2 < \log_2 T < b$.

### 4

Claim: The volume of the box is $\Upsilon = Tp = \Theta(n)$ (

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "T p = Θ(n)"

Paragraph:

> The volume of the box is $\Upsilon = Tp = \Theta(n)$ (). Write $d = \lfloor b^{\epsilon} \rfloor = \Theta(p^{\epsilon})$ for the number of axes of the box (the letter $d$ changes meaning here), and $K = \lfloor d^{c} \rfloor = \Theta(p^{\epsilon c})$ for the number of bits in each address chunk, a run of consecutive address bits (the letter $K$ changes meaning here).

### 5

Claim: The paper sets

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "let r = 2⌈(log2 T )/d⌉ and ℓ = log2 r"

Paragraph:

> Write $\ell = \lceil \log_2 T/d \rceil$ for the exponent with $r = 2^{\ell}$ (the letter $\ell$ changes meaning here). The paper sets. Each axis length is $r/2$ or $r$. With $k = d\ell - \log_2 T$, the ceiling gives $d(\ell-1) < \log_2 T \le d\ell$, so $0 \le k < d$. The construction chooses $k$ axis lengths to be $r/2$ (). The product is $2^{d\ell-k} = T$, and since $k < d$, one axis has length $r$, so $\ell$ is the largest axis exponent. For example, with $T = 2^{10}$ and $d = 3$, we get $\ell = 4$, $r = 16$, $k = 2$, and axis lengths $8, 8, 16$.

### 6

Claim: The construction chooses $k$ axis lengths to be $r/2$ (

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "of the d axis lengths to be r/2 and the others to be r"

Paragraph:

> Write $\ell = \lceil \log_2 T/d \rceil$ for the exponent with $r = 2^{\ell}$ (the letter $\ell$ changes meaning here). The paper sets. Each axis length is $r/2$ or $r$. With $k = d\ell - \log_2 T$, the ceiling gives $d(\ell-1) < \log_2 T \le d\ell$, so $0 \le k < d$. The construction chooses $k$ axis lengths to be $r/2$ (). The product is $2^{d\ell-k} = T$, and since $k < d$, one axis has length $r$, so $\ell$ is the largest axis exponent. For example, with $T = 2^{10}$ and $d = 3$, we get $\ell = 4$, $r = 16$, $k = 2$, and axis lengths $8, 8, 16$.

### 7

Claim: The layout uses

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "O(p/K) exchanges of width-K chunks"

Paragraph:

> The second row bounds the cost of the chunk exchanges that produce the [transform layout](transform-layout.md). The layout uses, each costing $O(\Upsilon K^{\tau})$, giving $pK^{\tau-1}$.

### 8

Claim: The paper's bound for this work is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "its O(T dp1+δ ) cost"

Paragraph:

> The chirp row covers chirp factors (phase factors quadratic in the position) and twists. The paper's bound for this work is, and dividing by $\Upsilon$ gives $dp^{\delta}$.

### 9

Claim: A record product is four integer products on $O(rp)$-bit integers, each costing $O(rp\log(rp))$ with the [established multiplier](established-multiplier.md), so the normalized cost is $\log(rp) = \ell + \log p$, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "log(rp) = O(p1−ϵ + log p) = O(p1−ϵ )"

Paragraph:

> The packed row multiplies the $T/r$ records, each a polynomial with $r$ coefficients of $p$ bits. A record product is four integer products on $O(rp)$-bit integers, each costing $O(rp\log(rp))$ with the [established multiplier](established-multiplier.md), so the normalized cost is $\log(rp) = \ell + \log p$, and.

### 10

Claim: The smallest margin is $2^{-181} = 2\kappa$ with $\kappa = 2^{-182}$, so

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Each of the seven displayed powers is at most 1 − 2κ by (45)."

Paragraph:

> Since $\epsilon(2-\tau) < 2^{-74}$, the fourth exceeds $2^{-51}$. The smallest margin is $2^{-181} = 2\kappa$ with $\kappa = 2^{-182}$, so

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

Write the answer to `exegenius/tasks/0726-support-cost-table.answer.json`, then run `exegenius submit 0726-support-cost-table` in the project directory. If submit rejects the answer, fix the answer and submit again.
