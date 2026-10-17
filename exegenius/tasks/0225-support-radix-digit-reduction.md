# exegenius task 0225-support-radix-digit-reduction

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

Claim: Hence $2q-2<2n/b\le T/2<S$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "2q-2<2n/b\le T/2<S."

Paragraph:

> Each digit polynomial has degree at most $q-1$, so the product polynomial has degree at most $2q-2$. Since $\lceil m\rceil<m+1$, we have $q<n/b+1$ and so $2q-2<2n/b$. Also $2n/b\le T/2$ because $T\ge 4n/b$, and $T/2<S$. Hence $2q-2<2n/b\le T/2<S$

### 2

Claim: Since $q\le n\le 2^b$, this is below $2^b\cdot 2^{2b}=2^{3b}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "0\le c_j\le q(2^b-1)^2<2^{3b},"

Paragraph:

> Each $c_j$ is a sum of at most $q$ products $u_iv_k$, each between $0$ and $(2^b-1)^2$. Hence $0\le c_j\le q(2^b-1)^2$. Since $q\le n\le 2^b$, this is below $2^b\cdot 2^{2b}=2^{3b}$.

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

Write the answer to `exegenius/tasks/0225-support-radix-digit-reduction.answer.json`, then run `exegenius submit 0225-support-radix-digit-reduction` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0225-support-radix-digit-reduction`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
