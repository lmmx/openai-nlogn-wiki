# exegenius task 0177-support-main-theorem

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

Claim: The machine uses a fixed finite alphabet and a fixed number of one-dimensional tapes, and computes the exact product for every $n\ge1$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "There is one deterministic Turing machine $A$, with a fixed finite"

Paragraph:

> The machine uses a fixed finite alphabet and a fixed number of one-dimensional tapes, and computes the exact product for every $n\ge1$.

### 2

Claim: The smallest margin is $2^{-181}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Direct substitution gives"

Paragraph:

> The logarithmic factor drops by the fixed power $\kappa$ because $\kappa$ is set by the smallest margin in the sources' cost table. Each row of that table is a power $p$ with exponent one minus a margin, where $p=6\lceil\lg n\rceil$. The smallest margin is $2^{-181}$, which is $2\kappa$, so the largest power is $p^{1-2\kappa}$. A fixed power of $\log p$ is at most $p^{\kappa}$ for large $p$, so $p^{1-2\kappa}$ times it is $O(p^{1-\kappa})=O((\lg n)^{1-\kappa})$.

### 3

Claim: For the bit network, $s$ equals $Wm$ minus $N$, the number of negative source projections, plus twice the lost label dimension $L$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The sum of the rational ranks of all edge differences is"

Paragraph:

> Both procedures come from one fixed linear network with $W$ roles and $s$ child calls. For the bit network, $s$ equals $Wm$ minus $N$, the number of negative source projections, plus twice the lost label dimension $L$, so $s<Wm$ needs $N>2L$. A negative source projection is a source operator $-P_U$, where $P_U$ projects onto a label subspace along its orthogonal complement.

### 4

Claim: A call makes $s$ child calls on streams of volume $V/W$, and its own splitting, gates and reassembly cost $O(1)$ per unit volume

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "merging, gates, and triangular operations have total cost $O(V)$ because"

Paragraph:

> Let $e=m^t$ be the number of radix-$q$ digits in a chunk at recursion level $t$, where $m$ is the number of fields per chunk and $q$ is a fixed prime. Let $F(e)$ be the time divided by $V$ at that level. Here $e$, $t$ and $F$ change meaning. Each chunk is cut into $m$ fields of $e/m$ digits. A call makes $s$ child calls on streams of volume $V/W$, and its own splitting, gates and reassembly cost $O(1)$ per unit volume. Hence $F(e)\le (s/W)F(e/m)+O(e^\tau+1)$ with $F(1)=O(1)$, since the children cost $s(V/W)F(e/m)$ and dividing by $V$ gives $s/W$.

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

Write the answer to `exegenius/tasks/0177-support-main-theorem.answer.json`, then run `exegenius submit 0177-support-main-theorem` in the project directory. If submit rejects the answer, fix the answer and submit again.
