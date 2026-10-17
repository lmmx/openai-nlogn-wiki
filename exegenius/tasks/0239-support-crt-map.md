# exegenius task 0239-support-crt-map

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

Claim: The split is due to Agarwal and Cooley

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Agarwal and Cooley used the Chinese remainder theorem to convert one cyclic convolution into multidimensional cyclic convolution"

Paragraph:

> Let $d$ be the number of axes, $i$ index them, and the lengths $s_i$ be pairwise coprime (unrelated to $s_i$ on the chirp page). The Chinese-remainder address map rewrites a cyclic convolution of length $S=s_1\cdots s_d$ as a multidimensional one, moving the data on tape by controlled shifts only. The split is due to Agarwal and Cooley; the exponents below make the movement triangular.

### 2

Claim: The parameters of [Parameter and prime-length choice](parameter-choice.md) set $p=6b$, with $b$ the digit width, and give $T<8n/b<2^{6b}$ for large $n$, so $T<2^p$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$t_i\leq r\leq T<8n/b<2^{6b}=2^p$"

Paragraph:

> The scan keeps one binary counter per axis, holding $a_i<t_i$, so the counters have $\log_2T$ bits in total. The parameters of [Parameter and prime-length choice](parameter-choice.md) set $p=6b$, with $b$ the digit width, and give $T<8n/b<2^{6b}$ for large $n$, so $T<2^p$. Thus $\log_2T<p$: the counters and the stored bounds $s_i$ have $O(p)$ bits in total. At each of the $T$ addresses, updating counters, testing validity and copying a record then take $O(p)$ steps, so a scan costs $O(Tp)$.

### 3

Claim: Computing the offsets, for at most $T/t_i$ prefixes, is negligible next to $Tp$ because $t_i\ge r/2$ and $r$ exceeds every fixed power of $p$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$t_i\ge r/2$ and $r$ exceeds every fixed power of $p$"

Paragraph:

> In this order the controls $a_j$, $j<i$, follow the target $a_i$. Reversing the axis order to $(a_1,\dots,a_d)$ puts controls first. Update targets for $i=d,d-1,\dots,1$, so no lower-index control has yet changed when axis $i$ is updated. Each update is a prefix-controlled cyclic shift of the valid interval $[0,s_i)$ and the identity on $[s_i,t_i)$, so zero padding stays zero. The map is implemented by these shifts, each of linear cost by [Controlled shifts and rational scalings](controlled-shifts.md). Computing the offsets, for at most $T/t_i$ prefixes, is negligible next to $Tp$ because $t_i\ge r/2$ and $r$ exceeds every fixed power of $p$.

### 4

Claim: A [chunk interchange](address-interchange.md) exchanges two equal-width axes in $O(V\ell^\tau)$ time

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "equal width $L$ in $O(VL^\tau)$ time"

Paragraph:

> Let $V=Tp$ be the stream volume and $\tau<1$ a fixed exponent. A [chunk interchange](address-interchange.md) exchanges two equal-width axes in $O(V\ell^\tau)$ time. Axes have $\ell$ or $\ell-1$ address bits; for unequal widths, move the longer axis's leading bit aside, swap the equal-width remainder, and restore the bit, adding fixed linear passes. Reversing $d$ axes takes $O(d^2)$ adjacent swaps, so reordering dominates the $O(dTp)$ shifts and $O(Tp)$ scans. The inverse subtracts the same offsets for $i=1,\dots,d$, then reorders back and deletes the padding. The map, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$

### 5

Claim: The map, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "O\bigl(Tp\,d^2(1+\ell^\tau)\bigr)."

Paragraph:

> Let $V=Tp$ be the stream volume and $\tau<1$ a fixed exponent. A [chunk interchange](address-interchange.md) exchanges two equal-width axes in $O(V\ell^\tau)$ time. Axes have $\ell$ or $\ell-1$ address bits; for unequal widths, move the longer axis's leading bit aside, swap the equal-width remainder, and restore the bit, adding fixed linear passes. Reversing $d$ axes takes $O(d^2)$ adjacent swaps, so reordering dominates the $O(dTp)$ shifts and $O(Tp)$ scans. The inverse subtracts the same offsets for $i=1,\dots,d$, then reorders back and deletes the padding. The map, its inverse and the padding cost $O(Tp\,d^2(1+\ell^\tau))$

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

Write the answer to `exegenius/tasks/0239-support-crt-map.answer.json`, then run `exegenius submit 0239-support-crt-map` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0239-support-crt-map`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
