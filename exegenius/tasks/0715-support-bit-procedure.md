# exegenius task 0715-support-bit-procedure

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

Claim: The transform needs this:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Θ(log n) transform levels already costs Θ(n log n)."

Paragraph:

> The cost of the procedure is measured by its [running time cost](running-time-cost.md). Here $V$ is the stored bit volume, so the cost is $V u^{\tau}$: a power of the field width below linear. The transform needs this: A linear-cost interchange would save nothing, so the recursion needs a power of $u$ below linear.

### 2

Claim: So $(h,d)$ becomes $(h\oplus d,\,d)$, the shear, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "It uses just one interchange."

Paragraph:

> After step 1, $D=d\oplus h$. The swap gives $H=d\oplus h$ and $D=h$. Step 3 gives $D=(d\oplus h)\oplus h=d$. So $(h,d)$ becomes $(h\oplus d,\,d)$, the shear, and

### 3

Claim: Since $\Phi_{M'}\Phi_M=\Phi_{M'+M}$, the frames along a route telescope,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Thus the intermediate frames cancel"

Paragraph:

> The middle shear is computed by a [bit network](bit-network.md), a fixed circuit of wires and gates. of the inputs. Each vertex has an invertible frame $\Phi_M$, which moves the entry at $(H,D)$ to $(H+MD,\,D)$. Since $\Phi_{M'}\Phi_M=\Phi_{M'+M}$, the frames along a route telescope,, and the route acts only through its endpoint matrices. The construction supplies endpoint matrices with, so every route acts as $\Phi_I$, the shear.

### 4

Claim: The construction supplies endpoint matrices with

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Mout(ρ(w)) − Min(w) = Im"

Paragraph:

> The middle shear is computed by a [bit network](bit-network.md), a fixed circuit of wires and gates. of the inputs. Each vertex has an invertible frame $\Phi_M$, which moves the entry at $(H,D)$ to $(H+MD,\,D)$. Since $\Phi_{M'}\Phi_M=\Phi_{M'+M}$, the frames along a route telescope,, and the route acts only through its endpoint matrices. The construction supplies endpoint matrices with, so every route acts as $\Phi_I$, the shear.

### 5

Claim: A shear by a matrix of rank $a$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "can be performed with exactly a interchanges of pairs of b-digit fields"

Paragraph:

> Each edge $e$ has a matrix $A_e$, the difference of its endpoint matrices. A shear by a matrix of rank $a$, where $b$ is the number of digits in each field. The bit procedure counts its interchanges by the [matrix rank](matrix-rank.md) of each edge matrix.

### 6

Claim: Each call acts on one of the $W$ role streams,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "stream of volume V /W"

Paragraph:

> Let $W$ be the number of wires and $s=\sum_e \operatorname{rank}A_e$. Each call acts on one of the $W$ role streams,. The construction gives, where $m$ is the recursion base. Neither $s$ nor $W$ depends on $u$.

### 7

Claim: The construction gives

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "s < W m"

Paragraph:

> Let $W$ be the number of wires and $s=\sum_e \operatorname{rank}A_e$. Each call acts on one of the $W$ role streams,. The construction gives, where $m$ is the recursion base. Neither $s$ nor $W$ depends on $u$.

### 8

Claim: Since $s/W<m$,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Choose a rational number τ ∈ (0, 1) with s/W < mτ"

Paragraph:

> Take $u=m^k$, so $k$ is the number of levels. Each level divides the field width by $m$, multiplies the number of calls by $s$, and divides each volume by $W$. After $k$ levels there are $s^k$ calls on volume $V/W^k$, so the leaf volume is $V(s/W)^k$. Since $s/W<m$,. Then $\log_m(s/W)<\tau$, and
> $$
> V\left(\frac{s}{W}\right)^{k}=V\,u^{\log_m(s/W)}\le V\,u^{\tau},
> $$
> using $u\ge 1$.

### 9

Claim: Each call's other work is linear in its volume:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "triangular operations have total cost O(V ) because their number is fixed."

Paragraph:

> Each call's other work is linear in its volume: Level $j$ has $s^j$ calls of volume $V/W^j$, so it costs $O(V(s/W)^j)$. Let $\theta=\max(0,\log_m(s/W))$ be the capped logarithm of $s/W$, which is below $\tau$. Summing over $k$ levels gives $O(Vk\max(1,s/W)^k)=O(V\log u\cdot u^{\theta})$. Since $\log u=O(u^{\tau-\theta})$, the total is $O(Vu^{\tau})$.

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

Write the answer to `exegenius/tasks/0715-support-bit-procedure.answer.json`, then run `exegenius submit 0715-support-bit-procedure` in the project directory. If submit rejects the answer, fix the answer and submit again.
