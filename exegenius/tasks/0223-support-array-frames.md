# exegenius task 0223-support-array-frames

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

Claim: So $G(D_vg_1,\dots,D_vg_t)=D_vG(g_1,\dots,g_t)$ for any arrays $g_1,\dots,g_t$: the gate applied to stored arrays gives the stored form of the logical output, and the invariant continues to the sinks

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the common frame commutes with the pointwise gate"

Paragraph:

> At a gate $G$ with $t$ input arrays, every incoming array has the common frame $D_v$, and a gate output combines the logical inputs $\varphi_1,\dots,\varphi_t$ with coefficients $c_j\in R$. Because $D_v$ is $R$-linear, $\sum_j c_jD_v\varphi_j=D_v\bigl(\sum_j c_j\varphi_j\bigr)$. So $G(D_vg_1,\dots,D_vg_t)=D_vG(g_1,\dots,g_t)$ for any arrays $g_1,\dots,g_t$: the gate applied to stored arrays gives the stored form of the logical output, and the invariant continues to the sinks.

### 2

Claim: The endpoint frames fix the operator on each route, so the

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "intermediate frames can then be chosen to make each edge change inexpensive."

Paragraph:

> The endpoint frames fix the operator on each route, so the

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

Write the answer to `exegenius/tasks/0223-support-array-frames.answer.json`, then run `exegenius submit 0223-support-array-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0223-support-array-frames`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
