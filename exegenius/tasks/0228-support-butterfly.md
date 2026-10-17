# exegenius task 0228-support-butterfly

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

Claim: Later transforms consist of address rearrangements, signed shifts and these steps

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "two-point butterfly operations"

Paragraph:

> A butterfly is the two-point step $H_0(u,v)=(\frac{u+v}{2},\frac{u-v}{2})$ applied to a pair of values (here $u,v$ are just those two values). Here $t$ is the transform length, a power of two. Repeated over the address bits of an array, with twiddle multiplications between layers, it computes the [Discrete Fourier transform](dft.md) of an array in $\log_2 t$ layers instead of $t^2$ operations. Later transforms consist of address rearrangements, signed shifts and these steps.

### 2

Claim: The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for $0\le k<t/2$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$"

Paragraph:

> Let $z_k$, for positions $0\le k<t$, be the input values, and let $\omega_t=e^{2\pi i/t}$. The transform is $(F_tz)_m=\frac1t\sum_j z_j\omega_t^{-jm}$, where $m$ is the output index. The decimation-in-frequency step pairs $z_k$ with $z_{k+t/2}$ for $0\le k<t/2$; these positions differ exactly in the highest address bit. Splitting the sum over $j=k$ and $j=k+t/2$, since $\omega_t^{t/2}=-1$ the second part carries the factor $(-1)^m$. Write $m=2h+b$, where $b\in\{0,1\}$ is the lowest bit of $m$ and $h$ is the remaining index. Then
> $$(F_tz)_{2h+b}=\frac1{t/2}\sum_{k=0}^{t/2-1}(\omega_t^2)^{-hk}\,\omega_t^{-bk}\,\frac{z_k+(-1)^bz_{k+t/2}}{2}.$$
> The pair enters only through $\frac{z_k+z_{k+t/2}}2$ (for $b=0$) and $\frac{z_k-z_{k+t/2}}2$ (for $b=1$), the two outputs of $H_0$. Store them in the slots they came from, so the highest address bit now holds $b$. After multiplying the $b=1$ output by the twiddle factor $\omega_t^{-k}$, each branch needs the same transform of length $t/2$ with output index $h$, because $\omega_t^2$ is the primitive $(t/2)$-th root of unity.

### 3

Claim: The address bits from high to low therefore hold the bits of $m$ from low to high

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "contain the frequency bits from low to high"

Paragraph:

> Number the address bits from the highest down. Layer one leaves bit $0$ of $m$ in the highest address bit. Within each branch, layer two repeats the argument for $h$: it pairs entries differing in the next address bit and leaves bit $1$ of $m$ there. Inductively, each layer leaves the next higher bit of $m$ in the next lower address bit. The address bits from high to low therefore hold the bits of $m$ from low to high, so output $m$ lands at the bit-reversed position of $m$.

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

Write the answer to `exegenius/tasks/0228-support-butterfly.answer.json`, then run `exegenius submit 0228-support-butterfly` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0228-support-butterfly`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
