# exegenius task 0288-support-subspace-labels

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

Claim: Each invocation also has $vz_{\rm b}$ side wires, one per ordered neighbour pair, where $z_{\rm b}=3\binom{97}2=13968$ counts a triple's neighbours (one shared element, two of the other $97$), so $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "W_{\rm b}&=2N+I(vz_{\rm b}+c_{\rm b})"

Paragraph:

> The deficit $W_{\rm b}m-s_{\rm b}=N-2L_{\rm b}=\frac{339}{539}N$ is positive because $L_{\rm b}/N<1/2$, but tiny beside $W_{\rm b}m$. Each invocation also has $vz_{\rm b}$ side wires, one per ordered neighbour pair, where $z_{\rm b}=3\binom{97}2=13968$ counts a triple's neighbours (one shared element, two of the other $97$), so $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})$. Since $Iv=3N$ and $Ic_{\rm b}=N/539$, this equals $N(2+3z_{\rm b}+\frac1{539})=\frac{22587335}{539}N$, so the relative deficit is $\frac{339}{22587335\,m}=\frac{339}{22587335000000}\approx1.5\cdot10^{-11}$.

### 2

Claim: Since $Iv=3N$ and $Ic_{\rm b}=N/539$, this equals $N(2+3z_{\rm b}+\frac1{539})=\frac{22587335}{539}N$, so the relative deficit is $\frac{339}{22587335\,m}=\frac{339}{22587335000000}\approx1.5\cdot10^{-11}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "=\frac{339}{22587335000000}"

Paragraph:

> The deficit $W_{\rm b}m-s_{\rm b}=N-2L_{\rm b}=\frac{339}{539}N$ is positive because $L_{\rm b}/N<1/2$, but tiny beside $W_{\rm b}m$. Each invocation also has $vz_{\rm b}$ side wires, one per ordered neighbour pair, where $z_{\rm b}=3\binom{97}2=13968$ counts a triple's neighbours (one shared element, two of the other $97$), so $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})$. Since $Iv=3N$ and $Ic_{\rm b}=N/539$, this equals $N(2+3z_{\rm b}+\frac1{539})=\frac{22587335}{539}N$, so the relative deficit is $\frac{339}{22587335\,m}=\frac{339}{22587335000000}\approx1.5\cdot10^{-11}$.

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

Write the answer to `exegenius/tasks/0288-support-subspace-labels.answer.json`, then run `exegenius submit 0288-support-subspace-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0288-support-subspace-labels`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
