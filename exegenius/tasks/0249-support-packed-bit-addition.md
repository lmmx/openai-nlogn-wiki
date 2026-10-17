# exegenius task 0249-support-packed-bit-addition

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

Claim: Ten values are excluded at each end, twenty per guard

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "There are exactly twenty excluded values for each guard in"

Paragraph:

> Ten values are excluded at each end, twenty per guard. At fixed spectator coordinates $y$ and $z$ range over all $2^L$ values, so each guard takes every value equally often and a fraction $20/2^{K-1}$ fail it. A union bound over the $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$, $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$.

### 2

Claim: That is at most sixteen swaps and eight rotations

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "There are at most sixteen swaps and eight rotations in $S_0$."

Paragraph:

> A rotation needs its target after its controls: swap it rightmost, rotate, undo the swap. That is at most sixteen swaps and eight rotations. It rotates chunks by [Controlled shifts and rational scalings](controlled-shifts.md) in $O(V)$ time and swaps by [Fast address-chunk interchange](address-interchange.md) in $O(VL^\tau)$, for $\tau<1$.

### 3

Claim: Movement costs $O(V(L^\tau+1))$, scans $O(MA_{\rm rect}^3+V)$, and radix passes $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$, so the time is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "With $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$, its time is"

Paragraph:

> Movement costs $O(V(L^\tau+1))$, scans $O(MA_{\rm rect}^3+V)$, and radix passes $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect}))$, so the time is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$. Per $V$ the extra terms are $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$, both tending to zero when $A_{\rm rect}=O(p)$, $R$ exceeds every polynomial in $p$, $f\le d\le p$, $K/\log p\to\infty$; the cost is $O(V(L^\tau+1))$.

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

Write the answer to `exegenius/tasks/0249-support-packed-bit-addition.answer.json`, then run `exegenius submit 0249-support-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0249-support-packed-bit-addition`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
