# exegenius task 0670-support-fixed-tape-model

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

Claim: As the paper puts it,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A machine has one fixed finite alphabet and one fixed finite number of one-dimensional tapes."

Paragraph:

> A fixed-tape machine is constrained in three ways: its alphabet is fixed, its number of tapes is fixed, and its tapes are one-dimensional. As the paper puts it, A one-dimensional tape is a row of cells. Each step is local: a step For example, if a tape holds 1011 with its head on the first cell, one step can overwrite that 1 with 0 and move to the second cell, but cannot reach the fourth. Reaching a cell $k$ cells away therefore takes at least $k$ steps.

### 2

Claim: Each step is local: a step

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "reads and writes at most one cell on each tape and moves each head by at most one cell."

Paragraph:

> A fixed-tape machine is constrained in three ways: its alphabet is fixed, its number of tapes is fixed, and its tapes are one-dimensional. As the paper puts it, A one-dimensional tape is a row of cells. Each step is local: a step For example, if a tape holds 1011 with its head on the first cell, one step can overwrite that 1 with 0 and move to the second cell, but cannot reach the fourth. Reaching a cell $k$ cells away therefore takes at least $k$ steps.

### 3

Claim: That method shows that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "two n-bit integers can be multiplied in O(n log n log log n)"

Paragraph:

> Costs in this model are measured against [Schönhage–Strassen multiplication](schonhage-strassen.md). That method shows that time on a multitape machine. Its authors. This model restricts [the n log n optimality conjecture](n-log-n-conjecture.md) to one machine at a time.

### 4

Claim: Its authors

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "conjectured n log n as the optimal order of multiplication cost"

Paragraph:

> Costs in this model are measured against [Schönhage–Strassen multiplication](schonhage-strassen.md). That method shows that time on a multitape machine. Its authors. This model restricts [the n log n optimality conjecture](n-log-n-conjecture.md) to one machine at a time.

### 5

Claim: The paper's Theorem 1 supplies such a machine:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "There is one deterministic Turing machine A, with a fixed finite alphabet and a fixed"

Paragraph:

> The paper's Theorem 1 supplies such a machine: finite number of one-dimensional tapes, and its worst-case running time satisfies $T_A(n)=O(n(\lg n)^{1-\kappa})$, where $\kappa=2^{-182}$. The method behind this bound

### 6

Claim: The method behind this bound

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "uses linear combinations of intermediate data to reduce the"

Paragraph:

> The paper's Theorem 1 supplies such a machine: finite number of one-dimensional tapes, and its worst-case running time satisfies $T_A(n)=O(n(\lg n)^{1-\kappa})$, where $\kappa=2^{-182}$. The method behind this bound

### 7

Claim: The theorem refutes an eventual $\Omega(n\log n)$ lower bound

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "for every fixed multiplication machine in"

Paragraph:

> The theorem refutes an eventual $\Omega(n\log n)$ lower bound this model.

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

Write the answer to `exegenius/tasks/0670-support-fixed-tape-model.answer.json`, then run `exegenius submit 0670-support-fixed-tape-model` in the project directory. If submit rejects the answer, fix the answer and submit again.
