# exegenius task 0250-support-simultaneous-layer

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

Claim: With $\mathsf S=\operatorname{diag}(1,i),$ the [Two-point kernel C](phase-kernel.md) $C=aI+bX$ satisfies $H_0=b\,\mathsf SC\mathsf S,$ $C^2=X$ and $C^4=I$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "H_0=b\mathsf SC\mathsf S,\qquad C^2=X,\qquad C^4=I,\qquad"

Paragraph:

> With $\mathsf S=\operatorname{diag}(1,i),$ the [Two-point kernel C](phase-kernel.md) $C=aI+bX$ satisfies $H_0=b\,\mathsf SC\mathsf S,$ $C^2=X$ and $C^4=I$. With $x_1,\dots,x_D$ the selected bits of an address $x,$ this gives $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D,$ where the diagonal operator $\mathcal S_D$ acts on an array $z$ by $(\mathcal S_Dz)(x)=i^{x_1+\dots+x_D}z(x).$ Phases and $b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}$ are exact Gaussian dyadic, leaving $C^{\otimes D}.$

### 2

Claim: Then $\mathcal P_GX_v\mathcal P_G^{-1}=X_{Gv}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "\mathcal P_MX_v\mathcal P_M^{-1}=X_{Mv}."

Paragraph:

> A group of $e=mf$ axes has $m$ slots of $f$ axes; a column holds one bit per slot, in $\mathbb F_2^m.$ $C^{\otimes e}$ is computed by the network of [Binary phase frames](phase-frames.md), with $W$ wires and $s$ smaller calls. Each edge changes the frame on every column by $\prod_hC_{v_h}^{\eta_h},$ with residual basis vectors $v_h$ indexed by $h,$ $\eta_h=\pm1,$ $C_v=aI+bX_v$ and $X_v$ shifting a column by $v.$ Let $G$ be an invertible $\mathbb F_2$-matrix with first columns $v_h$ and $\mathcal P_G:x\mapsto Gx$ an address permutation. Then $\mathcal P_GX_v\mathcal P_G^{-1}=X_{Gv}$, so the edge change is $\mathcal P_G(\prod_hC_{e_h}^{\eta_h})\mathcal P_G^{-1},$ $e_h$ the $h$-th standard basis vector. Apply $\mathcal P_G^{-1},$ then $(C^{\eta_h})^{\otimes f}$ to the $f$ bits of slot $h,$ then $\mathcal P_G:$ one child on $f=e/m$ axes per residual vector, exactly $s$ in all. Negative powers add no child: $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$ with $Z=\operatorname{diag}(1,-1).$

### 3

Claim: Their number is fixed, so the basis change and its inverse on $e$ axis chunks cost $O(V((eK)^\tau+1))$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "O(V((eK)^\tau+1))"

Paragraph:

> Elimination writes $G$ as at most $m(m-1)+3m$ row additions (a swap is three). Each XORs selected bits of one slot into another; [Packed selected-bit addition](packed-bit-addition.md) XORs selected bits by cyclic shifts of whole chunk ranges plus a repair of exceptional addresses. Their number is fixed, so the basis change and its inverse on $e$ axis chunks cost $O(V((eK)^\tau+1))$ $(\tau<1)$ on a stream of volume $V.$

### 4

Claim: As $s/W\le m^\sigma,$ $\sigma<1,$ internal levels sum geometrically, leaves add $O(e^\sigma d^{\beta(1-\sigma)}),$ and $\log d$ pieces give $O(d^{\lambda'}).$ The paper's choice $\lambda'=1-2^{-54}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "\lambda'=1-2^{-54},"

Paragraph:

> Rows go to the $W$ wire roles by index mod $W,$ so children have volume $V/W$ if the row count stays divisible by $W$ through $\lceil\log_md\rceil$ levels. So the first $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ chunks get individual $C$ kernels, in $O(V\log d),$ and their bits form a row index of range at least $W^{\lceil\log_md\rceil}.$ Zero rows pad each block to a multiple of that, making the row count at depth $j$ divisible by $W^{\lceil\log_md\rceil-j};$ fewer rows are added than the block holds, so the volume at most doubles. With $\beta=\tfrac12$ and $F(e)$ the time divided by volume,
> $$F(e)\le \tfrac sW F(e/m)+O((eK)^\tau+1)\ (e\ge d^\beta),\qquad F(e)=O(e)\ (e<d^\beta),$$
> the recursion of [Recursive power saving](rank-recurrence.md). As $s/W\le m^\sigma,$ $\sigma<1,$ internal levels sum geometrically, leaves add $O(e^\sigma d^{\beta(1-\sigma)}),$ and $\log d$ pieces give $O(d^{\lambda'}).$ The paper's choice $\lambda'=1-2^{-54}$, barely beats $D$ passes.

### 5

Claim: So $p+\Delta$ fractional and $\Delta+3$ integer and sign bits per real component represent every intermediate coefficient exactly

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "represents every intermediate coefficient exactly and prevents overflow"

Paragraph:

> A depth-$\ell$ value lies in $2^{-(p+\ell)}\mathbb Z[i]$ with modulus at most $2^\ell,$ since addition at most doubles modulus and halving adds a denominator bit. So $p+\Delta$ fractional and $\Delta+3$ integer and sign bits per real component represent every intermediate coefficient exactly. As $d=\Theta(p^\epsilon)$ and $\epsilon C_1<1,$ $\Delta=o(p):$ the width is $O(p).$

### 6

Claim: Absolute row sums multiply under tensor products, so each row of $\mathcal H=H_0^{\otimes D}$ has absolute row sum one

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "absolute row sum one."

Paragraph:

> Absolute row sums multiply under tensor products, so each row of $\mathcal H=H_0^{\otimes D}$ has absolute row sum one Hence $\mathcal H$ maps disk arrays to disk arrays. Truncation toward zero cannot increase a component's absolute value and changes it by less than $2^{-p},$ so $Q_p$ keeps the disk, with $\|Q_p(\mathcal Hz)-\mathcal Hz\|_\infty<\sqrt2\,2^{-p}$.

### 7

Claim: Truncation toward zero cannot increase a component's absolute value and changes it by less than $2^{-p},$ so $Q_p$ keeps the disk, with $\|Q_p(\mathcal Hz)-\mathcal Hz\|_\infty<\sqrt2\,2^{-p}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "truncation cannot increase the absolute value of either component"

Paragraph:

> Absolute row sums multiply under tensor products, so each row of $\mathcal H=H_0^{\otimes D}$ has absolute row sum one Hence $\mathcal H$ maps disk arrays to disk arrays. Truncation toward zero cannot increase a component's absolute value and changes it by less than $2^{-p},$ so $Q_p$ keeps the disk, with $\|Q_p(\mathcal Hz)-\mathcal Hz\|_\infty<\sqrt2\,2^{-p}$.

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

Write the answer to `exegenius/tasks/0250-support-simultaneous-layer.answer.json`, then run `exegenius submit 0250-support-simultaneous-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0250-support-simultaneous-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
