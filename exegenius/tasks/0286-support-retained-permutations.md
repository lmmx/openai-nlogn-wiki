# exegenius task 0286-support-retained-permutations

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

Claim: Its usual implementation sorts twice on each coordinate

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its usual implementation sorts twice on each"

Paragraph:

> Each prime-length transform is computed through a power-of-two one by [Gaussian resampling](gaussian-resampling.md). Its usual implementation sorts twice on each coordinate. For one axis, with $p$, $\alpha$, $\delta$ as there, let $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$ ($u,v$ are complex arrays here, not integers). That page gives linear contractions $A$, $B_0$ ($B_0$ is not the packing base) with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computed in time $O(tp^{3/2+\delta}\alpha)$ without executing $P_s$ or $P_t$.

### 2

Claim: If each $t_i\in\{r/2,r\}$ with $r=2^\ell$ and each entry has $O(p)$ bits, exposing and restoring all lines costs $O(Tp\,d^2(1+\ell^\tau))$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "using the equal-width chunk-swap bound $O(Vu^\tau)$ and the fixed-digit movement primitive"

Paragraph:

> Each axis is exposed as the innermost field by the [fast address-chunk interchange](address-interchange.md). If each $t_i\in\{r/2,r\}$ with $r=2^\ell$ and each entry has $O(p)$ bits, exposing and restoring all lines costs $O(Tp\,d^2(1+\ell^\tau))$. Since $t_i\ge r/2$, each tensor map invokes at most $\sum_iT/t_i\le 2dT/r$ lines, so setup work $O(p^\nu)$ per line, with $\nu$ a fixed exponent, totals $O(dTp^\nu/r)$. Dividing by $Tp$ gives $O(dp^{\nu-1}/r)\to0$ when $r$ outgrows every power of $p$ and $d$ is polynomially bounded in $p$, so setup is $o(Tp)$.

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

Write the answer to `exegenius/tasks/0286-support-retained-permutations.answer.json`, then run `exegenius submit 0286-support-retained-permutations` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0286-support-retained-permutations`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
