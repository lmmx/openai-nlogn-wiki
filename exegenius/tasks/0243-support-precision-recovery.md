# exegenius task 0243-support-precision-recovery

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

Claim: Each [synthetic transform](synthetic-transform.md) has error below $L$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$\sqrt2\ell\,2^{-p}<L2^{-p}$"

Paragraph:

> The computation runs on [Fixed-point Gaussian dyadic records](fixed-point.md) with $p=6b$ fractional bits, where $b=\lceil\log_2n\rceil$ is the digit width. Write $h_p=2^{-p}$ and $L=\log_2T$. Norms are sup norms, an error of $a$ means error below $ah_p$, and every array stays in the unit disk (norm $\le1$). For large $n$, $S\le T<2^b$ and $L<b$. Each [synthetic transform](synthetic-transform.md) has error below $L$.

### 2

Claim: An exact multiplication by $M=T/r$ then gives $(f*g)/T$ and
$$E_{\rm ring}:=M(3L+2)<5TL$$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "E_{\rm ring}:=M(3L+2)<5TL."

Paragraph:

> The ring convolution $\mathcal M_r$ of [Phase twist](phase-twist.md) applies two forward synthetic transforms, a pointwise polynomial product divided by $r$ (truncation under $2$) and one opposite transform. Together they err by under $3L+2$. An exact multiplication by $M=T/r$ then gives $(f*g)/T$ and
> $$E_{\rm ring}:=M(3L+2)<5TL$$
>  With an operand of norm at most $.7$, the output norm stays below $.701$. The complex convolution adds two input twists and one output untwist, each under $4$, so it errs by under
> $$(E_{\rm ring}+4+4+4)h_p<6TLh_p.$$

### 3

Claim: As $2dp^2<TL$ eventually, scaling gives error under $E_sh_p$ with
$$E_s=9\cdot2^\gamma TL$$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "E_s=9\,2^\gamma TL,"

Paragraph:

> The computed source transform $\widetilde{\mathscr F}$ applies the expansion map $\mathcal A$ of [Gaussian resampling](gaussian-resampling.md), then $\widetilde{\mathscr C}$, then the compression map $\mathcal B_0$, then an exact scaling by $2^\gamma$. Each of $\mathcal A,\mathcal B_0$ is a contraction implemented along $d$ axes with error under $p^2$ each, so under $dp^2$. The error before scaling is under $2dp^2+8TL$. As $2dp^2<TL$ eventually, scaling gives error under $E_sh_p$ with
> $$E_s=9\cdot2^\gamma TL$$
>  where $b\ge2^{24}$ gives $\gamma\le b/4$ and keeps $E_sh_p<10^{-3}$.

### 4

Claim: where $b\ge2^{24}$ gives $\gamma\le b/4$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$b\ge2^{24}$ implies $\gamma\le b/4$"

Paragraph:

> The computed source transform $\widetilde{\mathscr F}$ applies the expansion map $\mathcal A$ of [Gaussian resampling](gaussian-resampling.md), then $\widetilde{\mathscr C}$, then the compression map $\mathcal B_0$, then an exact scaling by $2^\gamma$. Each of $\mathcal A,\mathcal B_0$ is a contraction implemented along $d$ axes with error under $p^2$ each, so under $dp^2$. The error before scaling is under $2dp^2+8TL$. As $2dp^2<TL$ eventually, scaling gives error under $E_sh_p$ with
> $$E_s=9\cdot2^\gamma TL$$
>  where $b\ge2^{24}$ gives $\gamma\le b/4$ and keeps $E_sh_p<10^{-3}$.

### 5

Claim: With $F_{\boldsymbol s}$ the transform with factor $1/S$ and $F_{\boldsymbol s}^+$ its opposite-sign version, the retained permutation cancels ([Retained permutation cancellation](retained-permutations.md)) and the exact opposite transform $G=RF_{\boldsymbol s}^+$ gives $G(U\cdot V_1)=(u*v)/S^2$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "=\frac{u*v}{S^2}."

Paragraph:

> With $F_{\boldsymbol s}$ the transform with factor $1/S$ and $F_{\boldsymbol s}^+$ its opposite-sign version, the retained permutation cancels ([Retained permutation cancellation](retained-permutations.md)) and the exact opposite transform $G=RF_{\boldsymbol s}^+$ gives $G(U\cdot V_1)=(u*v)/S^2$ The computed opposite transform is within $E_sh_p$ of $Gz$ and $G$ is a contraction, so
> $$\|\widetilde{\mathscr F}^{+}(z)-G(U\cdot V_1)\|\le\|\widetilde{\mathscr F}^{+}(z)-Gz\|+\|G(z-U\cdot V_1)\|<(3E_s+2)h_p.$$
> Exact multiplication by $S$ makes $\widetilde w$ approximate $w=(u*v)/S$ with error under $E_wh_p$, where
> $$E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L.$$

### 6

Claim: With $h_p=2^{-6b}$, $S\le T<2^b$, $L<b$ and $\gamma\le b/4$, the absolute error is under
$$2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\tfrac12$$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "\le448b\,2^{-3b/4}<\frac12."

Paragraph:

> The integer coefficients are $2^{2b+4}Sw$: $2^{2b+4}$ undoes the two digit scales and $S$ the remaining $1/S$. With $h_p=2^{-6b}$, $S\le T<2^b$, $L<b$ and $\gamma\le b/4$, the absolute error is under
> $$2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\tfrac12$$
>  Here $2^{2b+4}ST^2<2^{5b+4}$ uses about $5b$ of the $6b$ fractional bits. The true coefficients are integers, so error strictly below $1/2$ makes the nearest integer the unique correct coefficient.

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

Write the answer to `exegenius/tasks/0243-support-precision-recovery.answer.json`, then run `exegenius submit 0243-support-precision-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0243-support-precision-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
