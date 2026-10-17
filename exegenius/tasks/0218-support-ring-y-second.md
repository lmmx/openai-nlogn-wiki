# exegenius task 0218-support-ring-y-second

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

Claim: We always keep the representative of degree below $r$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We always use representatives of degree less than $r$."

Paragraph:

> Write $\mathcal R_r=\mathbb C[y]/(y^r+1)$ for it, where $y$ is the ring variable, the indeterminate of the polynomials, and $r$ is the record length, the number of complex coefficients in a polynomial of the ring, always a power of two with $r\geq 2$. An element is
> $$z=\sum_{k=0}^{r-1}z_k y^k,\qquad z_k\in\mathbb C,$$
> so it is just a record of $r$ complex numbers. Addition is coefficientwise. Multiplication is ordinary polynomial multiplication followed by reduction modulo $y^r+1$, which means imposing $y^r=-1$. Consider a term of degree $r+j$ with $j\geq 0$, so that $j$ is the amount by which its degree exceeds $r$. Then
> $$y^{r+j}=y^{r}y^{j}=-y^{j},$$
> so the term, with its complex coefficient unchanged apart from the sign, lands at position $j$ with its sign flipped: it wraps around to the front. A product of two records has degree at most $2r-2$, so one such wrap suffices. For this sign flip the ring is also called the negacyclic ring. We always keep the representative of degree below $r$

### 2

Claim: The size of an element is measured by the largest coefficient modulus,
$$\|z\|_\infty=\max_{0\leq k<r}|z_k|.$$
A signed permutation of coefficients leaves this maximum unchanged, so multiplication by $y^a$ is an isometry for this norm

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "some signs; consequently it is an isometry for this norm."

Paragraph:

> The size of an element is measured by the largest coefficient modulus,
> $$\|z\|_\infty=\max_{0\leq k<r}|z_k|.$$
> A signed permutation of coefficients leaves this maximum unchanged, so multiplication by $y^a$ is an isometry for this norm Shifts therefore add no rounding error when coefficients are stored at fixed precision.

### 3

Claim: Taking one coordinate of a multidimensional array to be a record in $\mathcal R_r$ makes powers of $y$ available as roots of unity in the remaining axes, where a multiplication by such a root is a signed shift of the coefficient list

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "multiplication by such a root is a signed shift of the coefficient list"

Paragraph:

> Taking one coordinate of a multidimensional array to be a record in $\mathcal R_r$ makes powers of $y$ available as roots of unity in the remaining axes, where a multiplication by such a root is a signed shift of the coefficient list. Transforms built this way are described on [Synthetic polynomial transform](synthetic-transform.md). The ring also receives ordinary cyclic data once its coefficients are twisted by phases, as explained on [Phase twist](phase-twist.md).

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

Write the answer to `exegenius/tasks/0218-support-ring-y-second.answer.json`, then run `exegenius submit 0218-support-ring-y-second` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0218-support-ring-y-second`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
