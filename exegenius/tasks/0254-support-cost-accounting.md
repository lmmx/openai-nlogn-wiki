# exegenius task 0254-support-cost-accounting

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

Claim: Each move peels one excess bit, exchanges the equal-width parts and restores it, costing $O(V(1+\ell^\tau))$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Each costs $O(V(1+\ell^\tau))$: peel a single excess bit when widths"

Paragraph:

> - Prefix moves and single butterfly rounds are $O(dK)$ linear scans, each $O(V)$, in [Tape layout for synthetic transforms](transform-layout.md).
> - The layout needs $O(p/K)$ chunk exchanges, as $d\ell=O(p)$, each costing $O(VK^\tau)$ by [Fast address-chunk interchange](address-interchange.md). The total is $O(p/K)K^\tau=O(pK^{\tau-1})$.
> - Each of at most $\ell$ rounds costs $O(Vd^{\lambda'})$ by [Simultaneous butterfly layer](simultaneous-layer.md).
> - The [Chinese-remainder address map](crt-map.md) needs $O(d^2)$ adjacent axis moves. Each move peels one excess bit, exchanges the equal-width parts and restores it, costing $O(V(1+\ell^\tau))$. Here $d^2\ell^\tau=p^{2\epsilon}p^{(1-\epsilon)\tau}$.
> - In [Gaussian resampling](gaussian-resampling.md), axis $i$ has at most $T/t_i$ lines of cost $O(t_ip^{3/2+\delta}\alpha)$ each, totalling $O(dTp^{3/2+\delta}\alpha)$.
> - A chirp numerator of the [Bluestein chirp identity](chirp.md) has $O(p)$ bits and sums $d$ terms. The [Established O(n log n) multiplier](hvdh-multiplier.md), at cost $O(N\log 2N)$ on $N$ bits, computes their squares and products in $O(dp^{1+\delta})$ per entry.
> - The $T/r$ ring-product records each need four products on $O(rp)$ bits after [Signed packing](signed-packing.md) by the established multiplier at length $o(n)$. The total is $O(Tp\log(rp))$, and $\log(rp)=O(p^{1-\epsilon})$ since $r\le 2^{O(p/d)}$.

### 2

Claim: Substitution gives $g_1>1/2$, $g_2=2^{-75}2^{-56}2^{-50}=2^{-181}$, $g_3=2^{-75}2^{-54}=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$, so the smallest margin is $2^{-181}=2\kappa$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Thus $\min_i g_i=2^{-181}=2\kappa$."

Paragraph:

> Substitution gives $g_1>1/2$, $g_2=2^{-75}2^{-56}2^{-50}=2^{-181}$, $g_3=2^{-75}2^{-54}=2^{-129}$, $g_4>2^{-51}$, $g_5>1/8$, $g_6>1/2$ and $g_7=2^{-75}$, so the smallest margin is $2^{-181}=2\kappa$

### 3

Claim: The total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})."

Paragraph:

> Each of the seven powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually, which the margin $2\kappa$ leaves room for. The total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ Schoolbook multiplication below a fixed cutoff is absorbed One machine thus runs in $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.

### 4

Claim: Schoolbook multiplication below a fixed cutoff is absorbed

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "many smaller lengths are included by enlarging the implicit constant."

Paragraph:

> Each of the seven powers is at most $1-2\kappa$, and any fixed power of $\log p$ is at most $p^\kappa$ eventually, which the margin $2\kappa$ leaves room for. The total is $O(Tp\,p^{1-\kappa})=O(n(\log n)^{1-\kappa})$ Schoolbook multiplication below a fixed cutoff is absorbed One machine thus runs in $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.

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

Write the answer to `exegenius/tasks/0254-support-cost-accounting.answer.json`, then run `exegenius submit 0254-support-cost-accounting` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0254-support-cost-accounting`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
