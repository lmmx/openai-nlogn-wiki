# exegenius task 0227-support-dft

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

Claim: The normalized transform $F_q u$ has entries $(F_q u)_k = \frac1q\sum_{j=0}^{q-1} u_j\, e^{-2\pi i jk/q}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "(F_q u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{-2\pi i jk/q}"

Paragraph:

> Let $q\ge 1$ be the number of entries of a sequence, and let $u=(u_0,\dots,u_{q-1})$ be a sequence of $q$ complex numbers, with subscripts taken modulo $q$. The normalized transform $F_q u$ has entries $(F_q u)_k = \frac1q\sum_{j=0}^{q-1} u_j\, e^{-2\pi i jk/q}$. Writing $\omega = e^{2\pi i/q}$ for the primitive $q$-th root of unity, the weights are the powers $\omega^{-jk}$. The opposite transform $F_q^+$ uses $\omega^{+jk}$ instead. Because of the factor $1/q$, each output is an average of inputs multiplied by numbers of modulus one, so neither transform increases the largest entry modulus.

### 2

Claim: Because of the factor $1/q$, each output is an average of inputs multiplied by numbers of modulus one, so neither transform increases the largest entry modulus

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Each normalized Fourier transform above is a contraction"

Paragraph:

> Let $q\ge 1$ be the number of entries of a sequence, and let $u=(u_0,\dots,u_{q-1})$ be a sequence of $q$ complex numbers, with subscripts taken modulo $q$. The normalized transform $F_q u$ has entries $(F_q u)_k = \frac1q\sum_{j=0}^{q-1} u_j\, e^{-2\pi i jk/q}$. Writing $\omega = e^{2\pi i/q}$ for the primitive $q$-th root of unity, the weights are the powers $\omega^{-jk}$. The opposite transform $F_q^+$ uses $\omega^{+jk}$ instead. Because of the factor $1/q$, each output is an average of inputs multiplied by numbers of modulus one, so neither transform increases the largest entry modulus.

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

Write the answer to `exegenius/tasks/0227-support-dft.answer.json`, then run `exegenius submit 0227-support-dft` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0227-support-dft`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
