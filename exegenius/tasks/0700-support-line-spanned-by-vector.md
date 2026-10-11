# exegenius task 0700-support-line-spanned-by-vector

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

Claim: The construction of the [subset-intersection network](subset-intersection-network.md) labels its edges with subspaces, chosen

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "to make the changes of frame inexpensive"

Paragraph:

> A line spanned by a vector is the set of all scalar multiples of one nonzero vector, a one-dimensional subspace. The construction of the [subset-intersection network](subset-intersection-network.md) labels its edges with subspaces, chosen, and its triple labels are lines of this kind.

### 2

Claim: The paper needs this when it writes

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "write PU for the projection onto U along U ⊥"

Paragraph:

> The source paper, *Integer multiplication below $n\log n$*, gives no reason for nondegeneracy. A nondegenerate line $U$ meets only in zero its [orthogonal complement](orthogonal-complement.md) $U^\perp$: a vector in both is in $U$ and orthogonal to all of $U$, so it is zero. The paper needs this when it writes for nondegenerate $U$.

### 3

Claim: The network is linear:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A wire carries one scalar."

Paragraph:

> The construction labels the edges of a [linear network](linear-network-frames.md) with nondegenerate subspaces. The network is linear:..

### 4

Claim: The paper writes this as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "ua = ta1 ⊗ ta2 ⊗ ta3"

Paragraph:

> For a triple $T$ of the ground set $[h]$, the indicator vector $t_T$ has entry 1 in each of the three positions of $T$ and 0 elsewhere. For a choice $\sigma=(\sigma_1,\sigma_2,\sigma_3)$ of three triples, put $u_\sigma = t_{\sigma_1}\otimes t_{\sigma_2}\otimes t_{\sigma_3}$ and $U_\sigma = \operatorname{span}\{u_\sigma\}$. Each label $U_\sigma$ is spanned by the vector $u_\sigma$, a [tensor product](tensor-product.md) of three indicator vectors. The paper writes this as, using $a$ for $\sigma$.

### 5

Claim: , and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "at stage 3 they end at F on Xa and Ua⊥ on Ya"

Paragraph:

> The data banks $X_\sigma$ and $Y_\sigma$ are the two banks of data wires indexed by $\sigma$ that carry the label $U_\sigma$ between stages., and.

### 6

Claim: The bit network uses the form on $\mathbb{Q}^h$ given by

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "⟨x, y⟩ = xT (I − J/9)y"

Paragraph:

> The bit network uses the form on $\mathbb{Q}^h$ given by, where $J$ is the all-one matrix and $I$ the identity matrix. Each entry of $Jt_T$ is 3. So $t_T^{\mathsf T}Jt_T=9$, while $t_T^{\mathsf T}t_T=3$. Hence $\langle t_T,t_T\rangle = 3-9/9 = 2$, the value the paper reports:

### 7

Claim: Hence $\langle t_T,t_T\rangle = 3-9/9 = 2$, the value the paper reports:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "⟨tT , tT ⟩ = 2."

Paragraph:

> The bit network uses the form on $\mathbb{Q}^h$ given by, where $J$ is the all-one matrix and $I$ the identity matrix. Each entry of $Jt_T$ is 3. So $t_T^{\mathsf T}Jt_T=9$, while $t_T^{\mathsf T}t_T=3$. Hence $\langle t_T,t_T\rangle = 3-9/9 = 2$, the value the paper reports:

### 8

Claim: The paper concludes:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Thus every triple line is nondegenerate"

Paragraph:

> The form on a tensor power multiplies over the three factors, so $\langle u_\sigma,u_\sigma\rangle = 2^3 = 8 \neq 0$, and each label is nondegenerate. The paper concludes:.

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

Write the answer to `exegenius/tasks/0700-support-line-spanned-by-vector.answer.json`, then run `exegenius submit 0700-support-line-spanned-by-vector` in the project directory. If submit rejects the answer, fix the answer and submit again.
