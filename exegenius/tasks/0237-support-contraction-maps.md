# exegenius task 0237-support-contraction-maps

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

Claim: Linearity gives $Lu'-Lu=L(u'-u)$, so the output error is at most the input error

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "A linear contraction propagates an input error without increasing it."

Paragraph:

> Suppose a computed input $u'$ replaces the exact input $u$. Linearity gives $Lu'-Lu=L(u'-u)$, so the output error is at most the input error

### 2

Claim: If all four operands have norm at most $1$ (every entry in the unit disk), the two input errors simply add

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "When all four operands are in the disk, their two errors therefore add."

Paragraph:

> For a bilinear contraction, replace operands $f,g$ by $f',g'$. Adding and subtracting $\mathcal M(f,g')$ gives
> $$\mathcal M(f',g')-\mathcal M(f,g)=\mathcal M(f'-f,g')+\mathcal M(f,g'-g),$$
> so the output error is at most $\|f'-f\|\,\|g'\|+\|f\|\,\|g'-g\|$. If all four operands have norm at most $1$ (every entry in the unit disk), the two input errors simply add

### 3

Claim: Errors of successive steps also add: insert the exact map at the computed input and apply its contraction bound to the accumulated input error

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Composing such algorithms adds their errors"

Paragraph:

> Errors of successive steps also add: insert the exact map at the computed input and apply its contraction bound to the accumulated input error. Only the exact map must be a contraction; the computed approximation may be nonlinear.

### 4

Claim: Each output entry averages inputs multiplied by complex numbers of modulus one

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Each normalized Fourier transform above is a contraction, since each"

Paragraph:

> Contraction applies to the normalized [Discrete Fourier transform](dft.md),
> $$(F_q u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{-2\pi i jk/q},$$
> where $F_q$ is the transform on sequences of $q$ entries. Each output entry averages inputs multiplied by complex numbers of modulus one, so by the triangle inequality its modulus is at most the largest input modulus. For $q=2$ the outputs are $(u_0+u_1)/2$ and $(u_0-u_1)/2$, both of modulus at most $\max(|u_0|,|u_1|)$. The factor $1/q$ is what makes this work: the unnormalized sum could grow by a factor $q$.

### 5

Claim: A fixed output coefficient averages $T$ signed products of one entry of $f$ with one entry of $g$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Thus that coefficient averages"

Paragraph:

> Bilinear contraction applies to the normalized [Cyclic convolution](convolution.md) $f*g/T$, where $T$ counts all entries involved. A fixed output coefficient averages $T$ signed products of one entry of $f$ with one entry of $g$, each of modulus at most $\|f\|\,\|g\|$, hence $\|f*g/T\|\le\|f\|\,\|g\|$.

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

Write the answer to `exegenius/tasks/0237-support-contraction-maps.answer.json`, then run `exegenius submit 0237-support-contraction-maps` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0237-support-contraction-maps`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
