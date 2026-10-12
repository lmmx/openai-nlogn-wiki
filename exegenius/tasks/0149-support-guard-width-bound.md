# exegenius task 0149-support-guard-width-bound

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

Claim: The guard count bounds the depth of every intermediate coefficient

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The guard-width calculation above bounds both denominator and magnitude growth by ⌈C0 dC1 ⌉."

Paragraph:

> Inside a layer, each value comes from elementary operations: complex addition and subtraction, halving, sign change, and multiplication by $i$. The *depth* of an intermediate coefficient is the largest number of these operations on a chain from an input coefficient to it, where a chain follows an operand into any result that uses it. Write $\ell$ for the depth of a value, the number of operations on its longest chain. Let $C_0$ and $C_1$ be constants fixed by the network construction, and let $\Delta = \lceil C_0 d^{C_1} \rceil$ be the guard count. The guard count bounds the depth of every intermediate coefficient The paper sets $C_1 = 20$.

### 2

Claim: The paper sets $C_1 = 20$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the choice twenty leaves an explicit additional margin"

Paragraph:

> Inside a layer, each value comes from elementary operations: complex addition and subtraction, halving, sign change, and multiplication by $i$. The *depth* of an intermediate coefficient is the largest number of these operations on a chain from an input coefficient to it, where a chain follows an operand into any result that uses it. Write $\ell$ for the depth of a value, the number of operations on its longest chain. Let $C_0$ and $C_1$ be constants fixed by the network construction, and let $\Delta = \lceil C_0 d^{C_1} \rceil$ be the guard count. The guard count bounds the depth of every intermediate coefficient The paper sets $C_1 = 20$.

### 3

Claim: The whole layer is evaluated exactly, with one truncation toward zero at the end

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The procedure evaluates the entire layer exactly before this final truncation."

Paragraph:

> The bound makes a fixed register width enough. Since every depth is at most $\Delta$, each intermediate coefficient has at most $p+\Delta$ fractional bits, and each real component has absolute value at most $2^{\Delta}$. That largest value, $2^{\Delta}$, takes $\Delta+1$ bits, and a sign bit makes $\Delta+2$. The paper reserves $\Delta+3$ integer and sign bits per real component, one more than this count. Halving shifts the numerator into reserved zero bits, so no bit is lost. The whole layer is evaluated exactly, with one truncation toward zero at the end

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

Write the answer to `exegenius/tasks/0149-support-guard-width-bound.answer.json`, then run `exegenius submit 0149-support-guard-width-bound` in the project directory. If submit rejects the answer, fix the answer and submit again.
