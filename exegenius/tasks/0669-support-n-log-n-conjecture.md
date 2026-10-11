# exegenius task 0669-support-n-log-n-conjecture

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

Claim: Schönhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "O(n log n log log n)"

Paragraph:

> Schönhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in time on a multitape Turing machine, and they. Later, Harvey and van der Hoeven proved an, an upper bound showing that $n \log n$ is achievable. The conjecture asserts that nothing of smaller order is.

### 2

Claim: time on a multitape Turing machine, and they

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "proposed n log n as the optimal order of growth"

Paragraph:

> Schönhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in time on a multitape Turing machine, and they. Later, Harvey and van der Hoeven proved an, an upper bound showing that $n \log n$ is achievable. The conjecture asserts that nothing of smaller order is.

### 3

Claim: Later, Harvey and van der Hoeven proved an

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "unconditional O(n log n) bound"

Paragraph:

> Schönhage and Strassen proved in 1971 that two $n$-bit integers can be multiplied in time on a multitape Turing machine, and they. Later, Harvey and van der Hoeven proved an, an upper bound showing that $n \log n$ is achievable. The conjecture asserts that nothing of smaller order is.

### 4

Claim: In the paper's model,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes."

Paragraph:

> A lower bound on running time must refer to one machine, so the conjecture is stated for a fixed model. In the paper's model, Neither the alphabet nor the number of tapes grows with the input length. This is the [fixed-tape machine model](fixed-tape-model.md).

### 5

Claim: In the paper's wording,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "an eventual lower bound for every multiplication machine means"

Paragraph:

> In the paper's wording, this inequality for each fixed machine $A$, with its own $c_A$ and $N_A$. "Eventual" means that the inequality is required only from $N_A$ on, not at every input length.

### 6

Claim: The paper states the negation as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its negation requires one machine satisfying"

Paragraph:

> The conjecture is negated through the [limit inferior](limit-inferior.md) of the ratio $T_A(n)/(n\lg n)$. The paper states the negation as $\liminf_{n\to\infty} T_A(n)/(n\lg n) = 0$. For nonnegative terms, a limit inferior of zero means that the ratio falls below every positive $\varepsilon$ infinitely often. So the negation says that some machine $A$ has this property. For every positive $\varepsilon$ and every threshold $n_0$ on the input length, there is some $n \ge n_0$ with $T_A(n) < \varepsilon\, n \lg n$.

### 7

Claim: The paper gives its value as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "κ = 2−182"

Paragraph:

> The main theorem gives one fixed machine $A$ with $T_A(n) = O(n(\lg n)^{1-\kappa})$, where $\kappa$ is a fixed positive constant, the saving exponent. The paper gives its value as. Since $(\lg n)^{-\kappa} \to 0$, the ratio $T_A(n)/(n\lg n)$ is $O((\lg n)^{-\kappa})$ and tends to zero. Its limit inferior is therefore zero, so this machine satisfies the negation above. The paper states that its algorithm optimality conjecture of Schönhage and Strassen in this model.

### 8

Claim: The paper states that its algorithm

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "disproves the n log n"

Paragraph:

> The main theorem gives one fixed machine $A$ with $T_A(n) = O(n(\lg n)^{1-\kappa})$, where $\kappa$ is a fixed positive constant, the saving exponent. The paper gives its value as. Since $(\lg n)^{-\kappa} \to 0$, the ratio $T_A(n)/(n\lg n)$ is $O((\lg n)^{-\kappa})$ and tends to zero. Its limit inferior is therefore zero, so this machine satisfies the negation above. The paper states that its algorithm optimality conjecture of Schönhage and Strassen in this model.

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

Write the answer to `exegenius/tasks/0669-support-n-log-n-conjecture.answer.json`, then run `exegenius submit 0669-support-n-log-n-conjecture` in the project directory. If submit rejects the answer, fix the answer and submit again.
