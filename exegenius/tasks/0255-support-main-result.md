# exegenius task 0255-support-main-result

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

Claim: The machine is one deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, and is correct for every $n\ge1$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "There is one deterministic Turing machine $A$, with a fixed finite"

Paragraph:

> The machine is one deterministic Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, and is correct for every $n\ge1$. The saving is positive, however small: $(\lg n)^{1-\kappa}=\lg n/(\lg n)^{\kappa}$ and $(\lg n)^{\kappa}\to\infty$.

### 2

Claim: Beating that needs cheaper address movement and cheaper butterfly arithmetic

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We therefore need savings in both movement and arithmetic."

Paragraph:

> Scanning $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$. Beating that needs cheaper address movement and cheaper butterfly arithmetic

### 3

Claim: The fixed parameters are $\tau=1-2^{-50}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\delta=1/16$ and $\epsilon=2^{-75}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "\epsilon=2^{-75},\qquad \kappa=2^{-182}."

Paragraph:

> The margin $g_i$ of the $i$-th term is one minus its exponent. The fixed parameters are $\tau=1-2^{-50}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\delta=1/16$ and $\epsilon=2^{-75}$. The smallest margin belongs to chunk exchanges:
> $$g_2=\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}=2^{-181}=2\kappa,$$
> and the others are larger, e.g. $g_3=2^{-129}$, $g_7=2^{-75}$

### 4

Claim: $g_3=2^{-129}$, $g_7=2^{-75}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Thus $\min_i g_i=2^{-181}=2\kappa$."

Paragraph:

> The margin $g_i$ of the $i$-th term is one minus its exponent. The fixed parameters are $\tau=1-2^{-50}$, $\lambda'=1-2^{-54}$, $c=2^{-56}$, $\delta=1/16$ and $\epsilon=2^{-75}$. The smallest margin belongs to chunk exchanges:
> $$g_2=\epsilon c(1-\tau)=2^{-75}\cdot2^{-56}\cdot2^{-50}=2^{-181}=2\kappa,$$
> and the others are larger, e.g. $g_3=2^{-129}$, $g_7=2^{-75}$

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

Write the answer to `exegenius/tasks/0255-support-main-result.answer.json`, then run `exegenius submit 0255-support-main-result` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0255-support-main-result`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
