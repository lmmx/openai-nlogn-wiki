# exegenius task 0668-support-limit-inferior

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

Claim: The $n\log n$ optimality conjecture says that for each fixed machine $A$ there are a constant $\delta_A > 0$ and a threshold $\Gamma_A$ with
$$T_A(n) \ge \delta_A\, n\lg n \quad \text{whenever } n \ge \Gamma_A.$$
The paper states it as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "for each fixed machine A, there are constants cA > 0 and NA such that TA (n) ≥ cA n lg n"

Paragraph:

> **Use in the paper.** Here $\lg$ is the [base-2 logarithm](base-two-logarithm.md), and $A$ is a fixed machine whose running time $T_A(n)$ is the largest number of steps it takes on an input of $n$ bits. Below, $\delta$ is a real number greater than zero and $\Gamma$ is a threshold on input length, both arbitrary. The $n\log n$ optimality conjecture says that for each fixed machine $A$ there are a constant $\delta_A > 0$ and a threshold $\Gamma_A$ with
> $$T_A(n) \ge \delta_A\, n\lg n \quad \text{whenever } n \ge \Gamma_A.$$
> The paper states it as.

### 2

Claim: The paper states it as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its negation requires one machine satisfying lim inf n→∞ TA (n)/(n lg n) = 0."

Paragraph:

> Let $\rho_n = T_A(n)/(n\lg n)$ for $n \ge 2$. The limit inferior is applied to this ratio against the order that the authors of [Schönhage–Strassen multiplication](schonhage-strassen.md) conjectured optimal. The negation for $A$ says that for every such $\delta$ and every such $\Gamma$, some $n \ge \Gamma$ has $\rho_n < \delta$. The quantifier over every threshold asks for infinitely many small ratios, which is what the limit inferior captures. By the zero criterion, the negation is equivalent to $\liminf_{n\to\infty} \rho_n = 0$. The paper states it as

### 3

Claim: The page uses this bound without proof:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We give a deterministic algorithm that multiplies two n-bit integers in O(n(lg n)1−κ )"

Paragraph:

> The main theorem gives the fixed machine $A$ a time bound. Here $\kappa = 2^{-182}$ is a fixed exponent with $0 < \kappa < 1$, and $C$ is a constant, so $T_A(n) \le C\, n(\lg n)^{1-\kappa}$ for all large $n$. The page uses this bound without proof:.

### 4

Claim: The paper says

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The algorithm is exact for every input length and disproves the n log n"

Paragraph:

> This refutes the conjecture. Suppose it held for $A$ with $\delta_A$ and $\Gamma_A$; then $\rho_n \ge \delta_A$ for every $n \ge \Gamma_A$. But the zero criterion with $\varepsilon = \delta_A$ gives infinitely many $n$ with $\rho_n < \delta_A$, and one of them is at least $\Gamma_A$. The paper says.

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

Write the answer to `exegenius/tasks/0668-support-limit-inferior.answer.json`, then run `exegenius submit 0668-support-limit-inferior` in the project directory. If submit rejects the answer, fix the answer and submit again.
