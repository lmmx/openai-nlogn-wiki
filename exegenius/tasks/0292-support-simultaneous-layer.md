# exegenius task 0292-support-simultaneous-layer

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

Claim: Then $\mathcal P_\Gamma X_v\mathcal P_\Gamma^{-1}=X_{\Gamma v}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}."

Paragraph:

> A group of $e=mf$ selected axes ($e$ counts axes, not digits of a chunk) has $m$ slots of $f$ axes; a column holds one bit per slot, in $\mathbb F_2^m.$ $C^{\otimes e}$ is computed by the network of [Binary phase frames](phase-frames.md), with $W$ wires and $s$ smaller calls. Each edge changes the frame on every column by $\prod_\xi C_{v_\xi}^{\eta_\xi},$ with residual basis vectors $v_\xi$ indexed by $\xi,$ $\eta_\xi=\pm1,$ $C_v=aI+bX_v$ and $X_v$ shifting a column by $v.$ Let $\Gamma$ be an invertible $\mathbb F_2$-matrix with first columns $v_\xi$ and $\mathcal P_\Gamma:x\mapsto\Gamma x$ an address permutation. Then $\mathcal P_\Gamma X_v\mathcal P_\Gamma^{-1}=X_{\Gamma v}$, so the edge change is $\mathcal P_\Gamma(\prod_\xi C_{\mathbf 1_\xi}^{\eta_\xi})\mathcal P_\Gamma^{-1},$ $\mathbf 1_\xi$ the $\xi$-th standard basis vector. Apply $\mathcal P_\Gamma^{-1},$ then $(C^{\eta_\xi})^{\otimes f}$ to the $f$ bits of slot $\xi,$ then $\mathcal P_\Gamma:$ one child on $f=e/m$ axes per residual vector, exactly $s$ in all. Negative powers add no child: $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$ with $Z=\operatorname{diag}(1,-1).$

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

Write the answer to `exegenius/tasks/0292-support-simultaneous-layer.answer.json`, then run `exegenius submit 0292-support-simultaneous-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0292-support-simultaneous-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
