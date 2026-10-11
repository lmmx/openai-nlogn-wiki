# exegenius task 0699-support-indicator-vector

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

Claim: In the bit construction,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "S, T are neighbors when |S ∩ T | = 1"

Paragraph:

> Call $S$ and $T$ *neighbors* when the construction links them. In the bit construction,. In the complex construction, an even intersection.

### 2

Claim: In the complex construction,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "neighbors are distinct triples with"

Paragraph:

> Call $S$ and $T$ *neighbors* when the construction links them. In the bit construction,. In the complex construction, an even intersection.

### 3

Claim: In the bit construction the form lives on $\mathbb{Q}^h$, the $h$-tuples of rational numbers:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "let F = Qh with bilinear form"

Paragraph:

> An indicator vector is compared with others by the [bilinear form](bilinear-form.md) of each construction. Let $J$ be the $h\times h$ matrix of all ones. In the bit construction the form lives on $\mathbb{Q}^h$, the $h$-tuples of rational numbers: $\langle x,y\rangle = x^{\top}(I-J/9)y$. Since $t_S^{\top}t_T=|S\cap T|$ and $t_S^{\top}Jt_T=|S|\,|T|=9$, this gives which is $0$ for neighbors.

### 4

Claim: Since $t_S^{\top}t_T=|S\cap T|$ and $t_S^{\top}Jt_T=|S|\,|T|=9$, this gives

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "⟨tS , tT ⟩ = |S ∩ T | − 1,"

Paragraph:

> An indicator vector is compared with others by the [bilinear form](bilinear-form.md) of each construction. Let $J$ be the $h\times h$ matrix of all ones. In the bit construction the form lives on $\mathbb{Q}^h$, the $h$-tuples of rational numbers: $\langle x,y\rangle = x^{\top}(I-J/9)y$. Since $t_S^{\top}t_T=|S\cap T|$ and $t_S^{\top}Jt_T=|S|\,|T|=9$, this gives which is $0$ for neighbors.

### 5

Claim: In the complex construction the form is the dot product on $\mathbb{F}_2^h$:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "take instead F = Fh2 with the ordinary dot product"

Paragraph:

> In the complex construction the form is the dot product on $\mathbb{F}_2^h$:. Then $t_S\cdot t_T=|S\cap T| \bmod 2$, which is $0$ for neighbors because their intersection is even.

### 6

Claim: On each edge the network takes

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the orthogonal complement of the smaller label inside the larger one"

Paragraph:

> On each edge the network takes. For a nondegenerate subspace $U$ of a nondegenerate space $V$, $V=U\oplus U^{\perp}$, so $\dim U^{\perp}=\dim V-\dim U$. The source checks and that. Orthogonality

### 7

Claim: The source checks

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "every triple line is nondegenerate"

Paragraph:

> On each edge the network takes. For a nondegenerate subspace $U$ of a nondegenerate space $V$, $V=U\oplus U^{\perp}$, so $\dim U^{\perp}=\dim V-\dim U$. The source checks and that. Orthogonality

### 8

Claim: and that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "neighboring triple lines are orthogonal"

Paragraph:

> On each edge the network takes. For a nondegenerate subspace $U$ of a nondegenerate space $V$, $V=U\oplus U^{\perp}$, so $\dim U^{\perp}=\dim V-\dim U$. The source checks and that. Orthogonality

### 9

Claim: Orthogonality

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "of the corresponding indicator vectors permits the subspace assignments."

Paragraph:

> On each edge the network takes. For a nondegenerate subspace $U$ of a nondegenerate space $V$, $V=U\oplus U^{\perp}$, so $\dim U^{\perp}=\dim V-\dim U$. The source checks and that. Orthogonality

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

Write the answer to `exegenius/tasks/0699-support-indicator-vector.answer.json`, then run `exegenius submit 0699-support-indicator-vector` in the project directory. If submit rejects the answer, fix the answer and submit again.
