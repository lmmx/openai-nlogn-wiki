# exegenius task 0392-support-multidim-transform

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

Claim: A multidimensional transform is the Fourier transform of an array with several coordinates, computed by transforming along one axis at a time; the argument uses it to replace the long Fourier transforms of the integer product by transforms whose axis lengths are powers of two

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "multidimensional transforms whose axis lengths are powers of two"

Paragraph:

> A multidimensional transform is the Fourier transform of an array with several coordinates, computed by transforming along one axis at a time; the argument uses it to replace the long Fourier transforms of the integer product by transforms whose axis lengths are powers of two.

### 2

Claim: In symbols, $F_{\boldsymbol q}:=\bigotimes_iF_{q_i}$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "F_{\boldsymbol q}:=\bigotimes_iF_{q_i}"

Paragraph:

> Let $d$ be the number of axes, $i$ an axis index with $1\le i\le d$, and $q_i$ the number of positions along axis $i$, so $\boldsymbol q=(q_1,\dots,q_d)$. An entry of the array $u$ has an index tuple $j=(j_1,\dots,j_d)$ with $0\le j_i<q_i$. A line along axis $i$ is the $q_i$ entries obtained by fixing all other coordinates. For operators $G_i$ on sequences of length $q_i$, the tensor product $\bigotimes_i G_i$ applies each $G_i$ to every line along axis $i$. The transform $F_{\boldsymbol q}$ is the tensor product of the one-dimensional normalized [Discrete Fourier transform](dft.md) matrices $F_{q_i}$ of lengths $q_i$. In symbols, $F_{\boldsymbol q}:=\bigotimes_iF_{q_i}$. With $k$ an output index tuple shaped like $j$,
> $$(F_{\boldsymbol q}u)_k=\frac1{\prod_i q_i}\sum_j u_j\,e^{-2\pi i\sum_i j_ik_i/q_i}.$$

### 3

Claim: Each pass has error less than $p^2$, and earlier errors do not grow in later passes, so the $d$ passes give error less than $dp^2$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The linewise implementations of $\mathcal A$ and $\mathcal B_0$ each have error less than $dp^2$."

Paragraph:

> A pass applies a line map to every line, so its norm is a maximum over lines; hence $\mathcal A$ and $\mathcal B_0$ are contractions. Each pass has error less than $p^2$, and earlier errors do not grow in later passes, so the $d$ passes give error less than $dp^2$. Summing over $T/t_i$ lines per axis, the line algorithms take $O(dTp^{3/2+\delta}\alpha)$.

### 4

Claim: Summing over $T/t_i$ lines per axis, the line algorithms take $O(dTp^{3/2+\delta}\alpha)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The total time spent in the one-dimensional algorithms for both maps is $O(dTp^{3/2+\delta}\alpha)$, with a constant independent of $d$."

Paragraph:

> A pass applies a line map to every line, so its norm is a maximum over lines; hence $\mathcal A$ and $\mathcal B_0$ are contractions. Each pass has error less than $p^2$, and earlier errors do not grow in later passes, so the $d$ passes give error less than $dp^2$. Summing over $T/t_i$ lines per axis, the line algorithms take $O(dTp^{3/2+\delta}\alpha)$.

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

Write the answer to `exegenius/tasks/0392-support-multidim-transform.answer.json`, then run `exegenius submit 0392-support-multidim-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0392-support-multidim-transform`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
