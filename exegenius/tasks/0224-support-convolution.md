# exegenius task 0224-support-convolution

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

Claim: So the output coefficient is the average of $rM$ signed products of one coefficient of $f$ and one of $g$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Thus that coefficient averages $rM$ signed scalar products, and $\mathcal M_r$ is a bilinear contraction"

Paragraph:

> Fix one output address and one output coefficient. Each of the $M$ addresses of $f$ determines the address of $g$ it pairs with, and each of the $r$ coefficient indices of $f$ determines the index of $g$ modulo $r$, with a sign $\pm1$ from the wrap. So the output coefficient is the average of $rM$ signed products of one coefficient of $f$ and one of $g$.

### 2

Claim: Stored values lie on a grid of $p$ fractional bits, so the computed output only approximates $\mathcal M_r(f,g)$, and the procedure that computes it returns its components at a width larger than the input's by $\log_2 M$ bits

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Put $m_M=\log_2M$ and $w_M=w+m_M$."

Paragraph:

> It does not make the computed result exact. Stored values lie on a grid of $p$ fractional bits, so the computed output only approximates $\mathcal M_r(f,g)$, and the procedure that computes it returns its components at a width larger than the input's by $\log_2 M$ bits

### 3

Claim: When $g$ is a disk array this is at most $\|f-f'\|_\infty$: replacing one operand changes the output by at most the norm distance between its two values

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "If the other operand is a disk array, replacing one operand changes the output by at most the norm distance between its two values."

Paragraph:

> The bound does control how errors propagate. The map $\mathcal M_r$ is linear in each argument, so if $f'$ is $f$ with rounding errors, then $\mathcal M_r(f,g)-\mathcal M_r(f',g)=\mathcal M_r(f-f',g)$, of size at most $\|f-f'\|_\infty\|g\|_\infty$. When $g$ is a disk array this is at most $\|f-f'\|_\infty$: replacing one operand changes the output by at most the norm distance between its two values

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

Write the answer to `exegenius/tasks/0224-support-convolution.answer.json`, then run `exegenius submit 0224-support-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0224-support-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
