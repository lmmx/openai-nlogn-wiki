# exegenius task 0188-support-tape-interchange

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

Claim: The interchange costs $O(Vu^{\tau})$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its cost is $O(Vu^\tau)$ for a fixed $\tau<1$"

Paragraph:

> Let $H$ and $D$ be the two fields, each of $u$ bits, and let $V$ be the stored volume, the number of data units in the array. Here $u$ and $V$ are rebound. The exponent $\tau$ is a fixed number below 1 that sets the saving. The interchange costs $O(Vu^{\tau})$.

### 2

Claim: The paper's explicit network satisfies $s<Wm$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "supplies these conditions with $W=W_{\rm b}$ and $s=s_{\rm b}$"

Paragraph:

> The shear is carried by a bit network, a [Linear network](linear-network.md) whose wires each carry one bit. Each vertex holds a rational $m\times m$ matrix, where $m$ is its number of rows. An edge matrix, the head's matrix minus the tail's, of rank $a$ costs $a$ smaller calls, so $s$ is the sum of these ranks. Each smaller call acts on one of the $W$ [wire streams](role-streams.md), each of volume $V/W$. The paper's explicit network satisfies $s<Wm$.

### 3

Claim: For the explicit network the paper computes $\eta>20\cdot2^{-50}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Both exact deficits displayed above are greater than $20\cdot2^{-50}$."

Paragraph:

> The bound needs $\lambda<m^{\tau}$ for one fixed $\tau<1$, not merely $\lambda<m$. Write $\eta=(Wm-s)/(Wm)$, so $\lambda=m(1-\eta)$. For the explicit network the paper computes $\eta>20\cdot2^{-50}$ Take $\tau=1-2^{-50}$. Since $m<2^{20}$, $\ln m<20$, so $m^{-2^{-50}}=\exp(-2^{-50}\ln m)>1-20\cdot2^{-50}>1-\eta$, and hence $\lambda<m^{\tau}$. If $\lambda\le1$ the sum is at most $d+1$. If $\lambda>1$ it is $O(\lambda^d)$, and $\lambda^d<m^{d\tau}$. As $m\ge2$, $F_d=O(m^{d\tau})$, which for width $u=m^d$ is $O(u^{\tau})$ per unit volume.

### 4

Claim: For any initial auxiliary values, a forward invocation from $X$ to $Y$ adds $x_S$ into $y_S$ and changes no other value

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "a forward invocation changes $y_S$ to $y_S+x_S$ and leaves every other value unchanged"

Paragraph:

> For any initial auxiliary values, a forward invocation from $X$ to $Y$ adds $x_S$ into $y_S$ and changes no other value. The shear is such an invocation, with $D$ as $X$ and $H$ as $Y$, so it is exact for any initial auxiliary contents. A forward, inverse, forward schedule of these invocations exchanges the two banks and returns every auxiliary wire to its starting value.

### 5

Claim: A forward, inverse, forward schedule of these invocations exchanges the two banks and returns every auxiliary wire to its starting value

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "restores every auxiliary value"

Paragraph:

> For any initial auxiliary values, a forward invocation from $X$ to $Y$ adds $x_S$ into $y_S$ and changes no other value. The shear is such an invocation, with $D$ as $X$ and $H$ as $Y$, so it is exact for any initial auxiliary contents. A forward, inverse, forward schedule of these invocations exchanges the two banks and returns every auxiliary wire to its starting value.

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

Write the answer to `exegenius/tasks/0188-support-tape-interchange.answer.json`, then run `exegenius submit 0188-support-tape-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
