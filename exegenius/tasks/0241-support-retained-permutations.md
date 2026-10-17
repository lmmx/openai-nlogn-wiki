# exegenius task 0241-support-retained-permutations

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

Claim: Each prime-length transform is computed through a power-of-two one by [Gaussian resampling](gaussian-resampling.md), whose usual implementation sorts twice on each coordinate

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its usual implementation sorts twice on each"

Paragraph:

> Each prime-length transform is computed through a power-of-two one by [Gaussian resampling](gaussian-resampling.md), whose usual implementation sorts twice on each coordinate. For one axis, with $p$ and $\alpha$ as there and $\delta$ the fixed exponent in its time bound, let $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$ ($u,v$ are complex arrays here, not integers). That page gives linear contractions $A$, $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computed in time $O(tp^{3/2+\delta}\alpha)$ without executing $P_s$ or $P_t$.

### 2

Claim: With entries of $O(p)$ bits, exposing and restoring all lines costs $O(Tp\,d^2(1+\ell^\tau))$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "then exposing and restoring all the lines costs"

Paragraph:

> Tensor this identity over the axes. Put $R=\bigotimes_iP_{s_i}$ (a permutation, not a ring), $Q=\bigotimes_iP_{t_i}$, $\mathcal A=\bigotimes_iA_i$, $\mathcal B_0=\bigotimes_iB_{0,i}$. By the product rule the left sides combine to $RF_{\boldsymbol s}$, and the right sides to $\mathcal B_0QF_{\boldsymbol t}\mathcal A$ times $d$ factors $2^{2\alpha^2}$, so $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$. Both $\mathcal A$ and $\mathcal B_0$ are contractions, applied one line at a time in a padded box of $T$ entries. Errors and times add over the $d$ passes: error below $dp^2$, time $O(dTp^{3/2+\delta}\alpha)$ with a constant independent of $d$. Each axis is exposed as the innermost field by the [fast address-chunk interchange](address-interchange.md). With $t_i\in\{t_{\max}/2,t_{\max}\}$, $t_{\max}=2^\ell$, at most $2dT/t_{\max}$ lines occur, since $t_i\ge t_{\max}/2$, so setup $O(p^g)$ per line ($g$ a fixed exponent) totals $O(dTp^g/t_{\max})=o(Tp)$ when $t_{\max}$ outgrows every power of $p$ and $d$ is polynomially bounded in $p$. With entries of $O(p)$ bits, exposing and restoring all lines costs $O(Tp\,d^2(1+\ell^\tau))$.

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

Write the answer to `exegenius/tasks/0241-support-retained-permutations.answer.json`, then run `exegenius submit 0241-support-retained-permutations` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0241-support-retained-permutations`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
