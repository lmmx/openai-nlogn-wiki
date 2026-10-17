# exegenius task 0395-support-cost-accounting

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

Claim: - Prefix moves and single butterfly rounds are $O(dK)$ linear scans of cost $O(V)$ each, in [Tape layout for synthetic transforms](transform-layout.md).
- The layout rearranges the $d\ell=O(p)$ address bits of the records by exchanging width-$K$ chunks, so it needs $O(p/K)$ exchanges

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its positional layout uses $O(p/K)$ exchanges of width-$K$ chunks, because $d\ell=O(p)$."

Paragraph:

> - Prefix moves and single butterfly rounds are $O(dK)$ linear scans of cost $O(V)$ each, in [Tape layout for synthetic transforms](transform-layout.md).
> - The layout rearranges the $d\ell=O(p)$ address bits of the records by exchanging width-$K$ chunks, so it needs $O(p/K)$ exchanges Each chunk exchange costs $O(VK^\tau)$ by [Fast address-chunk interchange](address-interchange.md), and the normalized total is $O(p/K)K^\tau=O(pK^{\tau-1})$. The permutations of [Gaussian resampling](gaussian-resampling.md) are never executed, since they cancel ([Retained permutation cancellation](retained-permutations.md)), so no row charges them.
> - Each of at most $\ell$ simultaneous rounds costs $O(Vd^{\lambda'})$ by [Simultaneous butterfly layer](simultaneous-layer.md).
> - The [Chinese-remainder address map](crt-map.md) needs $O(d^2)$ adjacent axis moves. Each costs $O(V(1+\ell^\tau))$. Here $d^2\ell^\tau=p^{2\epsilon}p^{(1-\epsilon)\tau}$.
> - In [Gaussian resampling](gaussian-resampling.md), axis $i$ of length $t_i$ has at most $T/t_i$ lines, each costing $O(t_ip^{3/2+\delta}\alpha)$, totalling $O(dTp^{3/2+\delta}\alpha)$.
> - The chirp numerators of the [Bluestein chirp identity](chirp.md) have $O(p)$ bits and sum $d$ terms. The [Established O(n log n) multiplier](hvdh-multiplier.md), taking $O(N\log 2N)$ on $N$ bits, forms their squares and products in $O(dp^{1+\delta})$ per entry.
> - There are $T/r$ ring-product records, each needing four products on $O(rp)$ bits after [Signed packing](signed-packing.md). These calls have length $o(n)$. The total is $O(Tp\log(rp))$, and $\log(rp)=O(p^{1-\epsilon})$ because $r$ is at most $2^{O(p/d)}$.

### 2

Claim: Each costs $O(V(1+\ell^\tau))$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Each costs $O(V(1+\ell^\tau))$: peel a single excess bit when widths"

Paragraph:

> - Prefix moves and single butterfly rounds are $O(dK)$ linear scans of cost $O(V)$ each, in [Tape layout for synthetic transforms](transform-layout.md).
> - The layout rearranges the $d\ell=O(p)$ address bits of the records by exchanging width-$K$ chunks, so it needs $O(p/K)$ exchanges Each chunk exchange costs $O(VK^\tau)$ by [Fast address-chunk interchange](address-interchange.md), and the normalized total is $O(p/K)K^\tau=O(pK^{\tau-1})$. The permutations of [Gaussian resampling](gaussian-resampling.md) are never executed, since they cancel ([Retained permutation cancellation](retained-permutations.md)), so no row charges them.
> - Each of at most $\ell$ simultaneous rounds costs $O(Vd^{\lambda'})$ by [Simultaneous butterfly layer](simultaneous-layer.md).
> - The [Chinese-remainder address map](crt-map.md) needs $O(d^2)$ adjacent axis moves. Each costs $O(V(1+\ell^\tau))$. Here $d^2\ell^\tau=p^{2\epsilon}p^{(1-\epsilon)\tau}$.
> - In [Gaussian resampling](gaussian-resampling.md), axis $i$ of length $t_i$ has at most $T/t_i$ lines, each costing $O(t_ip^{3/2+\delta}\alpha)$, totalling $O(dTp^{3/2+\delta}\alpha)$.
> - The chirp numerators of the [Bluestein chirp identity](chirp.md) have $O(p)$ bits and sum $d$ terms. The [Established O(n log n) multiplier](hvdh-multiplier.md), taking $O(N\log 2N)$ on $N$ bits, forms their squares and products in $O(dp^{1+\delta})$ per entry.
> - There are $T/r$ ring-product records, each needing four products on $O(rp)$ bits after [Signed packing](signed-packing.md). These calls have length $o(n)$. The total is $O(Tp\log(rp))$, and $\log(rp)=O(p^{1-\epsilon})$ because $r$ is at most $2^{O(p/d)}$.

### 3

Claim: The setup costs at most $p^{A+C}=o(Tp)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "costs at most $p^{A+C}=o(Tp)$."

Paragraph:

> For setup, a visit is a node of the layer or address-layout recursions, or a round or group invocation inside them. They have constant branching, depth $O(\log p)$ and polynomially many rounds and groups. Fix an exponent $A$ with at most $p^A$ visits in total, and an exponent $C$ with descriptor setup of at most $p^C$ steps per visit. The setup costs at most $p^{A+C}=o(Tp)$ Per-record and per-line setup, $O(Tp^{A+C}/r)$ and $O(dTp^C/r)$, is $o(Tp)$ since $r$ exceeds every fixed power of $p$.

### 4

Claim: Below it the machine uses schoolbook multiplication; only finitely many lengths lie there, so their running times are bounded by one constant

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "many smaller lengths are included by enlarging the implicit constant."

Paragraph:

> The bound needs inputs beyond a cutoff chosen past all the size, precision, margin and layout conditions. Below it the machine uses schoolbook multiplication; only finitely many lengths lie there, so their running times are bounded by one constant With $\lg n=\max\{\lceil\log_2n\rceil,1\}$, within a constant factor of $\log n$ and at least $1$, the single machine therefore runs in $O(n(\lg n)^{1-\kappa})$ for every $n\ge1$.

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

Write the answer to `exegenius/tasks/0395-support-cost-accounting.answer.json`, then run `exegenius submit 0395-support-cost-accounting` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0395-support-cost-accounting`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
