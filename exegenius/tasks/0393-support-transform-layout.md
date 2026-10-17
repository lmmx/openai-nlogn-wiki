# exegenius task 0393-support-transform-layout

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

Claim: Every later round is then a single layer

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "we must place the selected bits of the participating axes at a common"

Paragraph:

> [Fixed-point Gaussian dyadic records](fixed-point.md) use $\Theta(p)$ bits per coefficient, so the $T$ coefficients occupy $\Theta(Tp)$ bits and one pass of a tape machine over them costs $O(Tp)$. The transform has $\ell$ rounds, and each round applies the two-point averaging and differencing step to one address bit of every axis. Done axis by axis this is about $D\ell$ passes, and since $d\ell=O(p)$ that is $O(Tp\cdot p)$. The layer does a round on $D$ axes in $O(Tpd^{\lambda'})$ rather than $D$ passes, but it acts on the same bit of $D$ consecutive $K$-bit chunks. Axis-major storage does not provide this: the bits of different axes are far apart. The record permutation $L$, built below, moves them together once. Every later round is then a single layer.

### 2

Claim: At most $D(b+1)=O(dK)$ bits move, so the moves cost $O(TpdK)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "listed slots, so the moves cost $O(TpdK)$."

Paragraph:

> Call an axis long if it has $\ell$ address bits and short if $\ell-1$. Put $b=(\ell-1)\bmod K$, the number of leftover low bits of an axis, and $q=\lfloor(\ell-1)/K\rfloor$, its number of whole chunks. Move to a prefix, one at a time, the top bit of each long axis and the $b$ lowest bits of each axis. What remains of each axis is exactly $q$ consecutive $K$-bit chunks. At most $D(b+1)=O(dK)$ bits move, so the moves cost $O(TpdK)$

### 3

Claim: This is at most $Dq-1$ exchanges, each done by the [fast address-chunk interchange](address-interchange.md) in $O(TpK^\tau)$ even for nonadjacent chunks

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "exchanges of width-$K$ address chunks, even when the chunks are"

Paragraph:

> Label each chunk by its axis and its rank from the high end of the axis, so the first chunk of axis 2 is $(2,1)$. The chunks are stored as $(1,1),\dots,(1,q),(2,1),\dots,(D,q)$ and must become $(1,1),(2,1),\dots,(D,1),(1,2),\dots,(D,q)$, so that the chunks of equal rank in all axes are adjacent. Scan the target positions from left to right and, at each one except the last, exchange the chunk there with the required one if they differ. This is at most $Dq-1$ exchanges, each done by the [fast address-chunk interchange](address-interchange.md) in $O(TpK^\tau)$ even for nonadjacent chunks. Since $DqK\le d\ell=O(p)$, the total is $O(Tp\,DqK^\tau)=O(Tp\,pK^{\tau-1})$. The prefix moves and exchanges define the record permutation $L$; recording them in reverse gives $L^{-1}$ at the same cost.

### 4

Claim: The cost is $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total."

Paragraph:

> There are $qK$ rounds on chunk bits and $b+1$ on prefix bits, $\ell$ in all. In a chunk round the selected bit has the same offset in the $D$ consecutive chunks of equal rank, so one layer performs it. The cost is $O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total A prefix round processes at most $D\le d$ bits individually, each in $O(Tp)$. There are at most $b+1\le K$ such rounds, so they cost $O(TpdK)$.

### 5

Claim: Starting from zero error, the $\ell$ rounds leave error less than $\sqrt2\,\ell\,2^{-p}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "zero error, at most $\ell$ rounds therefore"

Paragraph:

> Each round is the exact contraction $\mathcal H$ (which does not increase the norm of an error), the signed coefficient permutation $J_E$, and one truncation $Q_p$. Truncation toward zero is odd and acts separately on each real and imaginary part, so for the array $z$ entering the round $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$: the computed round equals one truncation after the exact round. That truncation moves each entry by less than $\sqrt2\,2^{-p}$, so by the triangle inequality each round adds less than $\sqrt2\,2^{-p}$ to the error. The permutations in $L$ are isometries and add none. Starting from zero error, the $\ell$ rounds leave error less than $\sqrt2\,\ell\,2^{-p}$.

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

Write the answer to `exegenius/tasks/0393-support-transform-layout.answer.json`, then run `exegenius submit 0393-support-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0393-support-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
