# exegenius task 0742-support-rank-saving-recursion

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

Claim: A gate's label is shared by its wires:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the latter assignment being common to every wire at that gate"

Paragraph:

> A wire runs from its source vertex, through the gates that touch it in time order, to its sink vertex. A touching of a gate and a wire is an [Incidence](incidence.md). A gate's label is shared by its wires:. The recursion runs on the wires of the [Subset-intersection network](subset-intersection-network.md); each wire's fixed place is its role.

### 2

Claim: Hence

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The number of recursive calls is the sum of the edge ranks, exactly s."

Paragraph:

> An edge $\varphi$ is a segment of a wire between consecutive vertices, with tail label $U_{\rm t}$ and head label $U_{\rm h}$. Its signed change is $\Delta_\varphi=\dim U_{\rm h}-\dim U_{\rm t}$ (the letter $\Delta$ changes meaning here). Its rank is the rational rank of $P_{\rm h}-P_{\rm t}$, the dimension over $\mathbb Q$ of its column span. For nested labels, with $U$ inside $U'$ and $U$ nondegenerate, $U'=U\oplus(U'\cap U^\bot)$, and $P_{U'}-P_U$ is zero on $U$ and on $U'^\bot$ and the identity on $U'\cap U^\bot$. So its rank is $\dim U'-\dim U$. Reversing an edge negates the matrix, so every edge has rank $|\Delta_\varphi|$. Rank-saving recursion reduces its calls to the [Address-field interchange](address-interchange.md), one per unit of edge rank. Hence

### 3

Claim: The sinks then contribute $Wm-\mu$, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Thus the signed dimension changes will sum to W m − 2N"

Paragraph:

> Along a wire, the signed change telescopes across each [Incidence](incidence.md) to the sink dimension minus the source dimension. In the bit construction each sink label is the orthogonal complement of its source label, so each wire's two dimensions sum to $m$. Let $\mu$ be the sum of the source dimensions (the paper writes $N$ for $\mu$). The sinks then contribute $Wm-\mu$, and, that is, $\sum_\varphi\Delta_\varphi=Wm-2\mu$.

### 4

Claim: Summing,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "of absolute changes is W m − 2N + 2L."

Paragraph:

> Call an edge decreasing when its head label is smaller. For a decreasing edge $\varphi$, let $\mathrm{loss}_\varphi=\dim U_{\rm t}-\dim U_{\rm h}>0$ be its dimension loss, and let $\mathcal L$ be the total of these losses. On a decreasing edge $|\Delta_\varphi|=-\Delta_\varphi=\Delta_\varphi+2\,\mathrm{loss}_\varphi$; on other edges $|\Delta_\varphi|=\Delta_\varphi$. Summing, So $\sum_\varphi|\Delta_\varphi|=Wm-2\mu+2\mathcal L$.

### 5

Claim: Hence the smaller calls are counted for the [Bit construction](bit-construction.md) as $s=Wm-\mu+2\mathcal L$, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its deficit from Wb m is N − 2Lb > 0."

Paragraph:

> In the [Bit construction](bit-construction.md), the $\mu$ first-stage source edges are exceptions., so each such edge has rank one (its matrix is $2P_U$ for a line $U$) while its signed change is zero. Hence the smaller calls are counted for the [Bit construction](bit-construction.md) as $s=Wm-\mu+2\mathcal L$, and

### 6

Claim: The paper's instance uses

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "with the ground-set size changed to h = 100."

Paragraph:

> The paper's instance uses $\mathcal L/\mu=100/539$, and So $s=Wm-\frac{339}{539}\mu<Wm$. The same signed-sum identity is checked on the [Complex construction](complex-construction.md), with ratio $101/539$.

### 7

Claim: $\mathcal L/\mu=100/539$, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "In particular, both are smaller than 1/2."

Paragraph:

> The paper's instance uses $\mathcal L/\mu=100/539$, and So $s=Wm-\frac{339}{539}\mu<Wm$. The same signed-sum identity is checked on the [Complex construction](complex-construction.md), with ratio $101/539$.

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

Write the answer to `exegenius/tasks/0742-support-rank-saving-recursion.answer.json`, then run `exegenius submit 0742-support-rank-saving-recursion` in the project directory. If submit rejects the answer, fix the answer and submit again.
