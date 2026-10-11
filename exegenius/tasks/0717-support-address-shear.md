# exegenius task 0717-support-address-shear

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

Claim: Interchanging address chunks reduces to shears, so their cost enters the main bound:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A compatible choice of rational parameters makes all terms in its cost table fit Theorem 1."

Paragraph:

> An address shear is the map $(H,D)\mapsto(H+D,D)$, which adds one address field to another and leaves the second unchanged. Interchanging address chunks reduces to shears, so their cost enters the main bound: Theorem 1 of [Integer multiplication below n log n](main-theorem.md) gives the time $O(n(\lg n)^{1-\kappa})$, where $\lg$ is the base-2 logarithm.

### 2

Claim: , so that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the triangular factors remain invertible there"

Paragraph:

> The shear is computed with [modular inverses](modular-inverse.md) modulo $q$ of the denominators., so that.

### 3

Claim: The outer stages are lower-triangular, each updating a field from earlier ones:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "updates a later field using earlier fields in linear time"

Paragraph:

> With $M=E_1\Pi E_2$, the shear runs in three stages: replace $D$ by $E_2D$ and $H$ by $E_1^{-1}H$; for each 1 at position $(i,j)$ of $\Pi$, update $H_i\leftarrow H_i+D_j$; replace $H$ by $E_1H$ and $D$ by $E_2^{-1}D$. The result is $H+MD$, with $D$ unchanged. The outer stages are lower-triangular, each updating a field from earlier ones:. With $m$ fixed, each costs $O(V)$.

### 4

Claim: , and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Msink(ρ(w)) − Msource(w) = Im for every input role w."

Paragraph:

> The shear is used by the [bit procedure](bit-procedure.md), which interchanges two fields. It is computed by the [Linear networks and frames](linear-network-frames.md) of the bit procedure., and On every role, the shear is realised as the [endpoint operator](endpoint-operator.md) of the bit network.. Composition follows the rules of [linear algebra basics](linear-algebra-basics.md).

### 5

Claim: Let $s$ be the total number of smaller calls and $W$ the number of wires, with

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "that the total number s of smaller calls satisfies s < W m."

Paragraph:

> Ranks govern the recursion. Let $s$ be the total number of smaller calls and $W$ the number of wires, with A call on volume $V$ splits it into $W$ streams of volume $V/W$, each handled by one smaller call. Triangular and splitting work costs $O(V)$ per call With $F_k$ the time per unit volume at depth $k$, this gives $F_k\le (s/W)F_{k-1}+O(1)$.

### 6

Claim: Triangular and splitting work costs $O(V)$ per call

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "because their number is fixed."

Paragraph:

> Ranks govern the recursion. Let $s$ be the total number of smaller calls and $W$ the number of wires, with A call on volume $V$ splits it into $W$ streams of volume $V/W$, each handled by one smaller call. Triangular and splitting work costs $O(V)$ per call With $F_k$ the time per unit volume at depth $k$, this gives $F_k\le (s/W)F_{k-1}+O(1)$.

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

Write the answer to `exegenius/tasks/0717-support-address-shear.answer.json`, then run `exegenius submit 0717-support-address-shear` in the project directory. If submit rejects the answer, fix the answer and submit again.
