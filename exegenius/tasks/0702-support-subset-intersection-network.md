# exegenius task 0702-support-subset-intersection-network

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

Claim: The side route is what

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "cancels exactly the intersection-one cases;"

Paragraph:

> So $\eta_S\leftarrow\eta_S+\xi_S$ for every $S$, and no $\xi_T$ with $T\neq S$ reaches $\eta_S$. The side route is what

### 2

Claim: The paper states the result, with signs, as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "(Xa , Ya ) 7−→ (−Ya , Xa )"

Paragraph:

> The inverse schedule runs the rows in reverse order with the banks renamed. This is valid because each row writes only wires it does not read, so over $\mathbb F_2$ each row is its own inverse. The paper states the result, with signs, as; over $\mathbb F_2$ the signs disappear, so the banks are swapped.

### 3

Claim: For an edge with labels $U'\subseteq U$, the residual is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the orthogonal complement of the smaller label inside the larger one"

Paragraph:

> Each wire carries an array, and changing an array's representation along an edge costs work. The network labels its wires with [subspace labels](subspace-labels.md): nondegenerate subspaces of a fixed bilinear space $E$. A subspace is *nondegenerate* when the form restricted to it has no nonzero vector orthogonal to all of it. For an edge with labels $U'\subseteq U$, the residual is, namely $U\cap U'^{\perp}$, and the cost of the edge is its dimension:

### 4

Claim: , namely $U\cap U'^{\perp}$, and the cost of the edge is its dimension:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "its dimension is the absolute change in label dimension."

Paragraph:

> Each wire carries an array, and changing an array's representation along an edge costs work. The network labels its wires with [subspace labels](subspace-labels.md): nondegenerate subspaces of a fixed bilinear space $E$. A subspace is *nondegenerate* when the form restricted to it has no nonzero vector orthogonal to all of it. For an edge with labels $U'\subseteq U$, the residual is, namely $U\cap U'^{\perp}$, and the cost of the edge is its dimension:

### 5

Claim: The decreasing edges are the central-wire edges, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "central-wire edges from time 3 to time 4; their dimension loss is h."

Paragraph:

> The total cost is the sum of residual dimensions over all edges, and it is small only if the decreasing edges lose little. edges small. The decreasing edges are the central-wire edges, and

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

Write the answer to `exegenius/tasks/0702-support-subset-intersection-network.answer.json`, then run `exegenius submit 0702-support-subset-intersection-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
