# exegenius task 0251-support-transform-layout

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

Claim: A simultaneous layer needs a round's selected bits at a common offset in consecutive $K$-bit chunks

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "we must place the selected bits of the participating axes at a common"

Paragraph:

> A simultaneous layer needs a round's selected bits at a common offset in consecutive $K$-bit chunks.

### 2

Claim: At most $D(b+1)=O(dK)$ slots move, so the moves cost $O(TpdK)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "listed slots, so the moves cost $O(TpdK)$."

Paragraph:

> Call an axis long if it has $\ell$ address bits and short if $\ell-1$. Put $b=(\ell-1)\bmod K$ and $q=\lfloor(\ell-1)/K\rfloor$, so $\ell-1=qK+b$ (new meanings: $b$ counts leftover low bits of an axis, $q$ its whole chunks). Move to a prefix one at a time the top bit of each long axis and the $b$ lowest bits of each axis. At most $D(b+1)=O(dK)$ slots move, so the moves cost $O(TpdK)$

### 3

Claim: This needs at most $Dq-1$ exchanges, each made by the [fast address-chunk interchange](address-interchange.md) at cost $O(TpK^\tau)$, even for nonadjacent chunks

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "exchanges of width-$K$ address chunks, even when the chunks are"

Paragraph:

> To group chunk 1 of every axis, then chunk 2, etc., scan target positions left to right, exchanging the chunk there with the required one if different. This needs at most $Dq-1$ exchanges, each made by the [fast address-chunk interchange](address-interchange.md) at cost $O(TpK^\tau)$, even for nonadjacent chunks. Since $DqK\le d\ell=O(p)$, the exchanges cost $O(Tp\,DqK^\tau)=O(Tp\,(DqK)K^{\tau-1})=O(Tp\,pK^{\tau-1})$. The prefix moves and exchanges define the record permutation $L$; reversing them gives $L^{-1}$.

### 4

Claim: A chunk round's selected bits share an offset in $D$ consecutive chunks, so one layer does it at cost $O(Tpd^{\lambda'})$; the chunk rounds cost $O(Tp\ell d^{\lambda'})$ in total

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$O(Tpd^{\lambda'})$ per round and $O(Tp\ell d^{\lambda'})$ in total."

Paragraph:

> There are $b+1$ rounds on prefix slots and $qK$ on chunks, $\ell$ in all. A chunk round's selected bits share an offset in $D$ consecutive chunks, so one layer does it at cost $O(Tpd^{\lambda'})$; the chunk rounds cost $O(Tp\ell d^{\lambda'})$ in total A prefix round handles at most $D$ bits individually at $O(Tp)$ each, so costs $O(Tpd)$; at most $b+1\le K$ such rounds cost $O(TpdK)$.

### 5

Claim: By the triangle inequality each round raises the error by less than $\sqrt2\,2^{-p}$, so from zero error the $\ell$ rounds leave error below $\sqrt2\,\ell\,2^{-p}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "zero error, at most $\ell$ rounds therefore"

Paragraph:

> Each round is the contraction $\mathcal H$ (norm-nonincreasing), the signed coefficient permutation $J_E$, and one truncation $Q_p$. Truncation toward zero is odd and acts separately on each real and imaginary part, so for the array $z$ entering a round $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$: one truncation follows the exact round. The exact round does not increase the norm of the computed-versus-exact difference, and truncation moves each entry by less than $\sqrt2\,2^{-p}$; the permutations in $L$ are isometries and add no error. By the triangle inequality each round raises the error by less than $\sqrt2\,2^{-p}$, so from zero error the $\ell$ rounds leave error below $\sqrt2\,\ell\,2^{-p}$.

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

Write the answer to `exegenius/tasks/0251-support-transform-layout.answer.json`, then run `exegenius submit 0251-support-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0251-support-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
