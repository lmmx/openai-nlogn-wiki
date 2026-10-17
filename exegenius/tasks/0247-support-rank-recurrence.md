# exegenius task 0247-support-rank-recurrence

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

Claim: The children cost $s(V/W)F(f)$, so multiplying the parameter by $m$ multiplies the recursive cost per unit volume by $s/W$, less than $m$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "This strict inequality is the source of the power saving."

Paragraph:

> Let $F(f)$ be the time per unit volume at parameter $f$ ($F$ is not the label space here). The children cost $s(V/W)F(f)$, so multiplying the parameter by $m$ multiplies the recursive cost per unit volume by $s/W$, less than $m$

### 2

Claim: So an interchange costs $O(Vf^\tau)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The chunks can be interchanged in $O(Ve^\tau)$ time"

Paragraph:

> Unrolling $\log_m f$ levels, depth $j$ (here counting levels) contributes $(s/W)^j$, so $F(f)=O\big(\sum_{j=0}^{\log_m f}(s/W)^j\big)$. If $s/W<m^\tau$ with fixed $\tau<1$, this is $O(f^\tau)$: for $s/W\le1$ it has $1+\log_m f$ terms of at most $1$; otherwise its last term, below $m^{\tau\log_m f}=f^\tau$, dominates. So an interchange costs $O(Vf^\tau)$.

### 3

Claim: With $s/W\le m^\sigma$ for a fixed $\sigma<1$, the overheads again sum geometrically, and the [simultaneous butterfly layer](simultaneous-layer.md) page obtains cost $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1."

Paragraph:

> With $s/W\le m^\sigma$ for a fixed $\sigma<1$, the overheads again sum geometrically, and the [simultaneous butterfly layer](simultaneous-layer.md) page obtains cost $O(Vd^{\lambda'})$ for a fixed $\lambda'<1$

### 4

Claim: By the rank counts it is $(N-2L)/(Wm)$ (bit) or $(2N-2L)/(Wm)$ (complex), namely $339/22587335000000$ and $73/19906842167500$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "=\frac{339}{22587335000000}"

Paragraph:

> Write $s/W=m(1-\eta)$, with $\eta$ now the relative deficit $(Wm-s)/(Wm)$. By the rank counts it is $(N-2L)/(Wm)$ (bit) or $(2N-2L)/(Wm)$ (complex), namely $339/22587335000000$ and $73/19906842167500$. Both exceed $20\cdot2^{-50}\approx1.8\cdot10^{-14}$ Since $m<2^{20}$, $\ln m<20\ln 2<20$; as the exponential lies above its tangent at $0$, $m^{1-2^{-50}}=m\exp(-2^{-50}\ln m)>m(1-2^{-50}\ln m)>m(1-20\cdot2^{-50})>m(1-\eta)=s/W$ for either network. Hence $\tau=\sigma=1-2^{-50}$ gives $s/W<m^\tau$ (bit) and $s/W<m^\sigma$ (complex), exponents barely below $1$.

### 5

Claim: Both exceed $20\cdot2^{-50}\approx1.8\cdot10^{-14}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Both exact deficits displayed above are greater than $20\cdot2^{-50}$."

Paragraph:

> Write $s/W=m(1-\eta)$, with $\eta$ now the relative deficit $(Wm-s)/(Wm)$. By the rank counts it is $(N-2L)/(Wm)$ (bit) or $(2N-2L)/(Wm)$ (complex), namely $339/22587335000000$ and $73/19906842167500$. Both exceed $20\cdot2^{-50}\approx1.8\cdot10^{-14}$ Since $m<2^{20}$, $\ln m<20\ln 2<20$; as the exponential lies above its tangent at $0$, $m^{1-2^{-50}}=m\exp(-2^{-50}\ln m)>m(1-2^{-50}\ln m)>m(1-20\cdot2^{-50})>m(1-\eta)=s/W$ for either network. Hence $\tau=\sigma=1-2^{-50}$ gives $s/W<m^\tau$ (bit) and $s/W<m^\sigma$ (complex), exponents barely below $1$.

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

Write the answer to `exegenius/tasks/0247-support-rank-recurrence.answer.json`, then run `exegenius submit 0247-support-rank-recurrence` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0247-support-rank-recurrence`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
