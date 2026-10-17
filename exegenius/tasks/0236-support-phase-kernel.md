# exegenius task 0236-support-phase-kernel

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

Claim: Equivalently $C=H\mathsf SH$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "C=H\mathsf SH=aI+bX"

Paragraph:

> Since $a^2+b^2=\frac{i}{2}-\frac{i}{2}=0$ and $2ab=1$, we get $C^2=(a^2+b^2)I+2ab\,X=X$, and therefore $C^4=X^2=I$. In terms of eigenvectors, $X$ has eigenvalue $1$ on $(1,1)$ and $-1$ on $(1,-1)$, while $C$ has eigenvalues $a+b=1$ and $a-b=i$ on the same vectors. Equivalently $C=H\mathsf SH$. Thus $C$ applies the phase $\mathsf S$ in the basis where $X$ is diagonal, and one application of $C$ is "half" a flip.

### 2

Claim: The kernel $C$ is obtained from the two-point step of [Butterflies and the fast transform](butterfly.md) by conjugating with $\mathsf S$ and rescaling:
$$H_0=b\,\mathsf S\,C\,\mathsf S,\qquad C^2=X$$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "H_0=b\mathsf SC\mathsf S,\qquad C^2=X"

Paragraph:

> The kernel $C$ is obtained from the two-point step of [Butterflies and the fast transform](butterfly.md) by conjugating with $\mathsf S$ and rescaling:
> $$H_0=b\,\mathsf S\,C\,\mathsf S,\qquad C^2=X$$
> . One can check the first identity by multiplying out: $\mathsf SC\mathsf S=\begin{pmatrix}a&ib\\ib&-a\end{pmatrix}$, and multiplying by $b$ uses $ab=\frac12$ and $ib^2=\frac12$.

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

Write the answer to `exegenius/tasks/0236-support-phase-kernel.answer.json`, then run `exegenius submit 0236-support-phase-kernel` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0236-support-phase-kernel`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
