# exegenius task 0707-support-complex-phase-network

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

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

Claim: The identity $H\,\mathrm{diag}(1,-1)\,H=\begin{pmatrix}0&1\\1&0\end{pmatrix}$,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "tensored over the coordinates in supp(v)"

Paragraph:

> For $b\in\{0,1\}$ and $\varepsilon\in\{1,-1\}$, $i^{\varepsilon b}=\frac{1+i\varepsilon}{2}+\frac{1-i\varepsilon}{2}(-1)^b$, since both sides equal $1$ at $b=0$ and $i\varepsilon$ at $b=1$. With $b=[v\cdot x]$, $\mathrm{diag}_x\big(i^{\varepsilon_v[v\cdot x]}\big)=\frac{1+i\varepsilon_v}{2}I+\frac{1-i\varepsilon_v}{2}\,\mathrm{diag}_x\big((-1)^{[v\cdot x]}\big)$. The identity $H\,\mathrm{diag}(1,-1)\,H=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, turns the sign $(-1)^{[v\cdot x]}$, a product of one-coordinate signs over $\mathrm{supp}(v)$, into $X_v$. So conjugating by $H^{\otimes m}$ gives $\frac{1+i\varepsilon_v}{2}I+\frac{1-i\varepsilon_v}{2}X_v$. For $\varepsilon_v=1$ this is $K_v$, and for $\varepsilon_v=-1$ it is $\tau_1 I+\tau_0X_v=K_v^{-1}$.

### 2

Claim: The paper chooses its intermediate labels for this reason,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "to make the changes of frame inexpensive"

Paragraph:

> Since $(H^{\otimes m})^2=I$ and diagonal operators multiply pointwise, $C_VC_U^{-1}=H^{\otimes m}\,\mathrm{diag}_x\big(i^{q_V(x)-q_U(x)}\big)\,H^{\otimes m}=\prod_{v\in\mathcal O}K_v^{\varepsilon_v}$. Each edge therefore costs one two-point kernel per basis vector. The paper chooses its intermediate labels for this reason,.

### 3

Claim: The paper's version applies

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "After source and sink diagonal corrections, and undoing the signed bank exchange"

Paragraph:

> The paper's version applies before it telescopes, and concludes that. Those corrections are outside this page; the computation above is the telescoping step along the route $U_\delta$.

### 4

Claim: before it telescopes, and concludes that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "phase frames gives C ⊗m on every role"

Paragraph:

> The paper's version applies before it telescopes, and concludes that. Those corrections are outside this page; the computation above is the telescoping step along the route $U_\delta$.

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

Write the answer to `exegenius/tasks/0707-support-complex-phase-network.answer.json`, then run `exegenius submit 0707-support-complex-phase-network` in the project directory. If submit rejects the answer, fix the answer and submit again.
