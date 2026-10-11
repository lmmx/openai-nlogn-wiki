# exegenius task 0744-support-main-theorem

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

Claim: Schönhage and Strassen

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "proposed n log n as the optimal order of growth"

Paragraph:

> Schönhage and Strassen. The theorem refutes [The n log n optimality conjecture](n-log-n-conjecture.md) in this model. Its bound is $n\lg n$ times $(\lg n)^{-\kappa}$, which is below half of $n\lg n$ only once $\lg n>2^{2^{182}}$.

### 2

Claim: The node's own work is the omitted term:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Pushing, popping, copying, resetting and clearing at this node cost its own volume times"

Paragraph:

> Let $F_k$ be the time per unit volume of a call at parameter $m^k$, which has $k$ levels of recursion beneath it. Its $s$ children cost $(s/W)F_{k-1}$ per unit volume in total. The node's own work is the omitted term: a fixed constant, an $O(1)$ term at each level. So $F_k\le (s/W)F_{k-1}+O(1)$, with $F_0=O(1)$.

### 3

Claim: The source sets

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "p = 6b"

Paragraph:

> Let $b=\lceil\log_2 n\rceil$ be the bit length of $n$. Here $p=6b$ is the working precision in bits, so $p=\Theta(\lg n)$. The source sets. Here $\epsilon$ is a fixed exponent with $0<\epsilon<1$. The numerical layer has a bound $d$ on its number of selected axes, with $d=\Theta(p^{\epsilon})$. The source writes. The source gives no reason for this choice. Since the cost per unit volume is a power of the parameter, a power of $p$ for $d$ makes it a power of $\lg n$.

### 4

Claim: The source writes

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "d = Θ(pϵ )"

Paragraph:

> Let $b=\lceil\log_2 n\rceil$ be the bit length of $n$. Here $p=6b$ is the working precision in bits, so $p=\Theta(\lg n)$. The source sets. Here $\epsilon$ is a fixed exponent with $0<\epsilon<1$. The numerical layer has a bound $d$ on its number of selected axes, with $d=\Theta(p^{\epsilon})$. The source writes. The source gives no reason for this choice. Since the cost per unit volume is a power of the parameter, a power of $p$ for $d$ makes it a power of $\lg n$.

### 5

Claim: The levels are few:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "There are at most k ≤ ⌈logm d⌉ internal levels"

Paragraph:

> The levels are few:. Since $m^{\lceil\log_m d\rceil}<m\cdot m^{\log_m d}=md$, the top parameter is $e=m^k\le md$. So the cost per unit volume is $O(d^{\tau})=O(p^{\epsilon\tau})=O((\lg n)^{\epsilon\tau})$. A compatible choice of rational parameters.

### 6

Claim: A compatible choice of rational parameters

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "makes all terms in its cost table fit Theorem 1"

Paragraph:

> The levels are few:. Since $m^{\lceil\log_m d\rceil}<m\cdot m^{\log_m d}=md$, the top parameter is $e=m^k\le md$. So the cost per unit volume is $O(d^{\tau})=O(p^{\epsilon\tau})=O((\lg n)^{\epsilon\tau})$. A compatible choice of rational parameters.

### 7

Claim: It is a power of two with

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Take the power of two T in [4n/b, 8n/b)"

Paragraph:

> Let $C$ be the number of cells of the padded box, the array the transforms act on. It is a power of two with, so the transforms have $\Theta(\lg n)$ levels. A full scan per level therefore costs $\Theta(n\lg n)$, the conjectured order and no better. Each stage instead costs $V$ times a power of its parameter, as in

### 8

Claim: Each stage instead costs $V$ times a power of its parameter, as in

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its cost is O(V uτ ) for a fixed τ < 1."

Paragraph:

> Let $C$ be the number of cells of the padded box, the array the transforms act on. It is a power of two with, so the transforms have $\Theta(\lg n)$ levels. A full scan per level therefore costs $\Theta(n\lg n)$, the conjectured order and no better. Each stage instead costs $V$ times a power of its parameter, as in

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

Write the answer to `exegenius/tasks/0744-support-main-theorem.answer.json`, then run `exegenius submit 0744-support-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
