# exegenius task 0229-support-synthetic-transform

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

Claim: Powers of $y$ can therefore serve as roots of unity

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Powers of $y$ then serve as roots of unity in the remaining axes, and multiplication by such a root is a signed shift of the coefficient list."

Paragraph:

> In that ring $y^r=-1$, so multiplying a record by $y^s$ moves each coefficient up $s$ places and negates those that wrap past degree $r-1$. Powers of $y$ can therefore serve as roots of unity.

### 2

Claim: Define $\omega_t=y^{2r/t}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "For a power of two $t$ dividing $2r$, define $\omega_t=y^{2r/t}$."

Paragraph:

> Let $t$ be the transform length, the number of ring elements along one axis, a power of two dividing $2r$. Define $\omega_t=y^{2r/t}$. Since $y^{2r}=1$ and $y^r=-1$, we get $\omega_t^t=1$ and $\omega_t^{t/2}=-1$.

### 3

Claim: A map that never increases size is a contraction, so both transforms are contractions

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Every power of $\omega_t$ is an isometry, and each transform entry is an average of $t$ such images."

Paragraph:

> The size of a ring element $\sum_k a_k y^k$ is $\max_k|a_k|$; the size of a list is the largest size of its entries. A signed shift only permutes coefficients and flips signs, so multiplying by a power of $\omega_t$ leaves size unchanged. An entry of $F_t^\pm z$ is $\frac1t$ times a sum of $t$ shifted entries of $z$; by the triangle inequality on each coefficient, it has size at most that of $z$. A map that never increases size is a contraction, so both transforms are contractions.

### 4

Claim: The ring has zero divisors, so the cancellation is verified directly

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The ring has zero divisors, so we verify character cancellation directly instead of dividing by $\omega_t^j-1$."

Paragraph:

> Over the complex numbers one cancels sums of roots of unity by dividing by $\omega_t^j-1$. The ring has zero divisors, so the cancellation is verified directly. For an integer $j$,
> $$\sum_{k=0}^{t-1}\omega_t^{jk}=\begin{cases}t,&t\mid j,\\0,&t\nmid j.\end{cases}$$
> If $t\nmid j$, write $j$ as $2^e$ times an odd number, with $0\le e<\log_2 t$. Replacing $k$ by $k+t/2^{e+1}$ modulo $t$ permutes the summands and multiplies each by $\omega_t^{jt/2^{e+1}}=y^{r\cdot\text{odd}}=-1$. The sum equals its own negative, so it is $0$.

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

Write the answer to `exegenius/tasks/0229-support-synthetic-transform.answer.json`, then run `exegenius submit 0229-support-synthetic-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0229-support-synthetic-transform`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
