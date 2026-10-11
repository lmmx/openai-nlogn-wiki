# exegenius task 0694-support-matrix-rank

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

Claim: The paper's Lemma 9 states that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Every rational m × m matrix A of rank a has a"

Paragraph:

> Write $E_1$ and $E_2$ for the invertible lower triangular factors, which have zeros above the diagonal. Write $\Pi$ for the partial permutation matrix, which has at most one 1 in each row and column. The paper's Lemma 9 states that factorization $A = E_1 \Pi E_2$. The paper proves it by elimination: Each step places one 1 in $\Pi$, and one.

### 2

Claim: The paper proves it by elimination:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Each step isolates a rank-one block and leaves the remaining rank in the active submatrix."

Paragraph:

> Write $E_1$ and $E_2$ for the invertible lower triangular factors, which have zeros above the diagonal. Write $\Pi$ for the partial permutation matrix, which has at most one 1 in each row and column. The paper's Lemma 9 states that factorization $A = E_1 \Pi E_2$. The paper proves it by elimination: Each step places one 1 in $\Pi$, and one.

### 3

Claim: Each step places one 1 in $\Pi$, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Π has exactly a entries equal to"

Paragraph:

> Write $E_1$ and $E_2$ for the invertible lower triangular factors, which have zeros above the diagonal. Write $\Pi$ for the partial permutation matrix, which has at most one 1 in each row and column. The paper's Lemma 9 states that factorization $A = E_1 \Pi E_2$. The paper proves it by elimination: Each step places one 1 in $\Pi$, and one.

### 4

Claim: Applying them around one update per one of $\Pi$ gives $(H + AJ, J)$, so the shear

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "can be performed with exactly a interchanges"

Paragraph:

> Let $H = (H_1, \ldots, H_m)$ and $J = (J_1, \ldots, J_m)$ be vectors of $m$ address fields, each a block of digits. An interchange swaps an $H$ field with a $J$ field. The shear for $A$ sends $(H, J)$ to $(H + AJ, J)$. the update $H_i \leftarrow H_i + J_j$. Let $\gamma$ and $\delta$ be the values of $H_i$ and $J_j$ before the update (these letters change meaning here). Three steps do it: $J_j \leftarrow J_j + H_i$ gives $\delta + \gamma$; swap $H_i$ with $J_j$; then $J_j \leftarrow H_i - J_j$ gives $\delta$. So $(\gamma, \delta)$ becomes $(\gamma + \delta, \delta)$ with one interchange. costs linear work, as does $J$. Applying them around one update per one of $\Pi$ gives $(H + AJ, J)$, so the shear.

### 5

Claim: The paper shows that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its deficit from"

Paragraph:

> The circuit has $W$ wires, counting its scratch wires.. Each terminal and gate $v$ carries a rational $m \times m$ matrix $M_v$. The edge matrix of $e$ is $A_e = M_{\mathrm{head}(e)} - M_{\mathrm{tail}(e)}$, the difference of its end matrices. The rank of an edge matrix prices each edge change in the [linear network](linear-network-frames.md). the total cost. The paper shows that $Wm$ is positive, so the total is below $Wm$.

### 6

Claim: The paper's Lemma 10 ends with

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the number of recursive calls is the rational rank a"

Paragraph:

> The paper's Lemma 10 ends with, which the [Rank-saving recursion](rank-saving-recursion.md) page turns into the saving.

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

Write the answer to `exegenius/tasks/0694-support-matrix-rank.answer.json`, then run `exegenius submit 0694-support-matrix-rank` in the project directory. If submit rejects the answer, fix the answer and submit again.
