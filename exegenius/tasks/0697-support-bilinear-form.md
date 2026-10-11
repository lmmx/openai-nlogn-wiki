# exegenius task 0697-support-bilinear-form

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

Claim: The [subspace labels](subspace-labels.md) of the networks below are nondegenerate subspaces of one fixed form:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A label is a nondegenerate subspace of a fixed bilinear"

Paragraph:

> A bilinear form decides when two vectors are orthogonal. The [subspace labels](subspace-labels.md) of the networks below are nondegenerate subspaces of one fixed form: space.

### 2

Claim: on $E=\mathbb{Q}^h$, where $h$ is the size of the ground set and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "h = 100"

Paragraph:

> The form below is the label space of the paper's [bit network](bit-network.md). on $E=\mathbb{Q}^h$, where $h$ is the size of the ground set and:
> $$\langle x,y\rangle=x^{\top}(I-J/9)\,y,$$
>  Here $J$ has every entry 1, so $\Psi=I-J/9$.

### 3

Claim: :
$$\langle x,y\rangle=x^{\top}(I-J/9)\,y,$$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "where J is the all-one matrix."

Paragraph:

> The form below is the label space of the paper's [bit network](bit-network.md). on $E=\mathbb{Q}^h$, where $h$ is the size of the ground set and:
> $$\langle x,y\rangle=x^{\top}(I-J/9)\,y,$$
>  Here $J$ has every entry 1, so $\Psi=I-J/9$.

### 4

Claim: Neither is zero:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "This form has eigenvalues 1 and 1−h/9 = −91/9, so it is nondegenerate."

Paragraph:

> Let $\mathbf 1$ be the column of $h$ ones. Each row of $J$ sums to $h$, so $J\mathbf 1=h\mathbf 1$. If the entries of $x$ sum to 0, then $Jx=\mathbf 1(\mathbf 1^{\top}x)=0$. Hence $\Psi\mathbf 1=(1-h/9)\mathbf 1$ and $\Psi x=x$ for each such $x$. These vectors span $\mathbb{Q}^h$, since $\mathbf 1$ is not among them. So $\Psi$ has eigenvalues $1-h/9$ and $1$, and with $h=100$ the first is $-91/9$. Nondegeneracy is decided by the [eigenvalues](eigenvalue.md) of $\Psi$, since $\Psi$ is invertible exactly when none of them is zero. Neither is zero:

### 5

Claim: Since $J=\mathbf 1\mathbf 1^{\top}$, we have $\langle x,y\rangle=x^{\top}y-\frac19(\mathbf 1^{\top}x)(\mathbf 1^{\top}y)$, so
$$\langle t_S,t_T\rangle=|S\cap T|-\tfrac{3\cdot 3}{9}=|S\cap T|-1,$$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "⟨tS , tT ⟩ = |S ∩ T | − 1"

Paragraph:

> Write $[h]=\{1,\dots,h\}$ for the set of the first $h$ positive integers. For a triple $T$, a three-element subset of $[h]$, let $t_T$ be its indicator vector, with entry 1 at each element of $T$ and 0 elsewhere. For triples $S$ and $T$ (each a three-element subset of $[h]$, with indicator vector $t_S$ or $t_T$), $\mathbf 1^{\top}t_S=\mathbf 1^{\top}t_T=3$ and $t_S^{\top}t_T=|S\cap T|$, which counts the common elements. Since $J=\mathbf 1\mathbf 1^{\top}$, we have $\langle x,y\rangle=x^{\top}y-\frac19(\mathbf 1^{\top}x)(\mathbf 1^{\top}y)$, so
> $$\langle t_S,t_T\rangle=|S\cap T|-\tfrac{3\cdot 3}{9}=|S\cap T|-1,$$
> . Taking $S=T$ gives $\langle t_T,t_T\rangle=3-1=2$, as the paper records:

### 6

Claim: Taking $S=T$ gives $\langle t_T,t_T\rangle=3-1=2$, as the paper records:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "⟨tT , tT ⟩ = 2."

Paragraph:

> Write $[h]=\{1,\dots,h\}$ for the set of the first $h$ positive integers. For a triple $T$, a three-element subset of $[h]$, let $t_T$ be its indicator vector, with entry 1 at each element of $T$ and 0 elsewhere. For triples $S$ and $T$ (each a three-element subset of $[h]$, with indicator vector $t_S$ or $t_T$), $\mathbf 1^{\top}t_S=\mathbf 1^{\top}t_T=3$ and $t_S^{\top}t_T=|S\cap T|$, which counts the common elements. Since $J=\mathbf 1\mathbf 1^{\top}$, we have $\langle x,y\rangle=x^{\top}y-\frac19(\mathbf 1^{\top}x)(\mathbf 1^{\top}y)$, so
> $$\langle t_S,t_T\rangle=|S\cap T|-\tfrac{3\cdot 3}{9}=|S\cap T|-1,$$
> . Taking $S=T$ gives $\langle t_T,t_T\rangle=3-1=2$, as the paper records:

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

Write the answer to `exegenius/tasks/0697-support-bilinear-form.answer.json`, then run `exegenius submit 0697-support-bilinear-form` in the project directory. If submit rejects the answer, fix the answer and submit again.
