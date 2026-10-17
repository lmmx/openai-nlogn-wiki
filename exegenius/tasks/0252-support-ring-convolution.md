# exegenius task 0252-support-ring-convolution

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

Claim: A fixed output coefficient averages $rM$ signed scalar products

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$rM$ signed scalar products, and $\mathcal M_r$ is a bilinear"

Paragraph:

> For arrays over $\mathcal R_r$ define $\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}$. A fixed output coefficient averages $rM$ signed scalar products, so $\mathcal M_r$ is a bilinear contraction, $\|\mathcal M_r(f,g)\|_\infty\le\|f\|_\infty\|g\|_\infty$.

### 2

Claim: Each output entry is an average of images of the inputs under powers of $y$, so both are contractions

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Thus both transforms are contractions."

Paragraph:

> Let $F^-$, $F^+$ be the forward and opposite synthetic transforms. Each output entry is an average of images of the inputs under powers of $y$, so both are contractions Expansion of the finite sums gives $F^-(f*g)=M(F^-f)(F^-g)$. With $F^+F^-=I/M$ ([Discrete Fourier transform](dft.md)), it follows that $MF^+\bigl((F^-f)(F^-g)/r\bigr)=f*g/(rM)$. Write $P(u,v)=uv/r$ for the pointwise product. Each coefficient of $uv$ in $\mathcal R_r$ is a signed sum of $r$ products of coefficients, so $\|P(u,v)\|_\infty\le\|u\|_\infty\|v\|_\infty$, and $P$ is bilinear.

### 3

Claim: With $\ell=\log_2r$, each procedure maps disk grid arrays to disk grid arrays with error less than $\delta=\sqrt2\ell\,2^{-p}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$\sqrt2\ell\,2^{-p}$, returns disk grid coefficients in the same"

Paragraph:

> The transforms are laid out as in [Tape layout for synthetic transforms](transform-layout.md). Perform both forward transforms and retain their common $LB$ order, with $L$ the layout permutation of records and $B$ the bit-reversal order. Their exact counterparts are $LBF^-$ and the opposite map $\mathcal T_+=F^+B^{-1}L^{-1}$; permuting records preserves the norm, so $\mathcal T_+$ is a contraction. With $\ell=\log_2r$, each procedure maps disk grid arrays to disk grid arrays with error less than $\delta=\sqrt2\ell\,2^{-p}$. Multiply the $M$ record pairs pointwise there, apply the opposite procedure to that order, and multiply by $M$. Since $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so $\mathcal T_+$ applied to the pointwise product of the stored forward outputs equals $F^+P(F^-f,F^-g)$; its scaling by $M$ is $\mathcal M_r(f,g)$. The procedure keeps the retained order of [Retained frequency order](frequency-order.md), passing the product to the opposite transform without reordering.

### 4

Claim: The exact multiplication by $M$ gives total error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$, as claimed."

Paragraph:

> Let $u,v$ be the exact stored forward outputs and $\widetilde u,\widetilde v$ the returned ones, all disk arrays. By bilinearity, $P(\widetilde u,\widetilde v)-P(u,v)=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v)$. By the contraction bound for $P$, and norm at most $1$ of $\widetilde v$ and $u$, each term is less than $\delta$, so $\|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty<2\delta$. With $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$, truncation gives $\|\widetilde z-z_*\|_\infty<2\delta+\eta$, and $\widetilde z$ is a disk grid array. The opposite procedure returns $\widetilde h$ with $\|\widetilde h-\mathcal T_+\widetilde z\|_\infty<\delta$, and $\|\mathcal T_+(\widetilde z-z_*)\|_\infty\le\|\widetilde z-z_*\|_\infty$ since $\mathcal T_+$ is a contraction. The triangle inequality gives $\|\widetilde h-\mathcal T_+z_*\|_\infty<3\delta+\eta$. The exact multiplication by $M$ gives total error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$

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

Write the answer to `exegenius/tasks/0252-support-ring-convolution.answer.json`, then run `exegenius submit 0252-support-ring-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0252-support-ring-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
