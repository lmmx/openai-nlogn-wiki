# exegenius task 0235-support-matrix-shear

Project directory: `/home/user/e2e-run` (paths below are relative to it)

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

Claim: For $A$ in a fixed finite set, it can be performed with exactly $a$ interchanges of $b$-digit fields and $O(V)$ further work

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "can be performed with exactly $a$ interchanges of pairs of $b$-digit"

Paragraph:

> Let $H=(H_1,\dots,H_m)$ and $D=(D_1,\dots,D_m)$ be two groups of fields, $H$ before $D$, where $m$ is the number of fields in each group. Let $A$ be a rational $m\times m$ matrix of rank $a$ (the letter $a$ changes meaning on this page). Each field is a residue modulo $q^b$, where $q$ is a fixed odd prime and $b$ is the number of base-$q$ digits per field. The shear is $(H,D)\mapsto(H+AD,D)$. For $A$ in a fixed finite set, it can be performed with exactly $a$ interchanges of $b$-digit fields and $O(V)$ further work. Lower triangular changes of coordinates are cheap, so all the rank of $A$ is pushed into a partial permutation.

### 2

Claim: Every such $A$ factors as $A=E_1\Pi E_2$, where $E_1,E_2$ are invertible lower triangular and $\Pi$ has exactly $a$ ones, at most one per row and column

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Every rational $m\times m$ matrix $A$ of rank $a$ has a factorization"

Paragraph:

> Every such $A$ factors as $A=E_1\Pi E_2$, where $E_1,E_2$ are invertible lower triangular and $\Pi$ has exactly $a$ ones, at most one per row and column. Elimination finds it. Take the topmost nonzero row and its rightmost nonzero entry, the pivot. Right multiplication by lower triangular elementary matrices clears the row to the left of the pivot, and left multiplication by such matrices clears the column below it; scaling makes the pivot one. Delete the pivot row and column and repeat. The pivots form $\Pi$, and has the rank of $A$ because $E_1,E_2$ are invertible.

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

Write the answer to `exegenius/tasks/0235-support-matrix-shear.answer.json`, then run `exegenius submit 0235-support-matrix-shear` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0235-support-matrix-shear`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
