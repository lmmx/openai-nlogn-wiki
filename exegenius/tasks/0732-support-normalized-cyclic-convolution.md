# exegenius task 0732-support-normalized-cyclic-convolution

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

Claim: The source states the rule for length $S$:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The normalized convolution rule is Fs (u ∗ v) = S(Fs u) · (Fs v), while Fs+ Fs = I/S."

Paragraph:

> The source states the rule for length $S$: With $S = s$ it reads $F_s(f \ast g) = s\,(F_s f)(F_s g)$. Let $\ell$, $0 \le \ell \le s-1$, index the entries of $f \ast g$. A pair $j$ of $f$ and $j'$ of $g$ contributes $f_j g_{j'}$ to entry $\ell = (j+j') \bmod s$, and $\omega^s = 1$ gives $\omega^{\ell k} = \omega^{(j+j')k}$. Hence
> $$F_s(f \ast g)_k = \frac{1}{s}\sum_{j,\,j'} f_j\,g_{j'}\,\omega^{(j+j')k} = s\,(F_s f)_k\,(F_s g)_k,$$
> the last step because $(F_s f)_k (F_s g)_k = \frac{1}{s^2}\sum_{j,\,j'} f_j g_{j'}\,\omega^{(j+j')k}$. Dividing by $s$ gives $F_s(f \circledast g)_k = (F_s f)_k (F_s g)_k$.

### 2

Claim: The paper's middle transform $QFt$ is the Fourier-type factor of its equation (35), and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The factor QFt in (35) can be computed from a cyclic convolution and two pointwise phase"

Paragraph:

> The paper's middle transform $QFt$ is the Fourier-type factor of its equation (35), and multiplications. into normalized cyclic convolution.

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

Write the answer to `exegenius/tasks/0732-support-normalized-cyclic-convolution.answer.json`, then run `exegenius submit 0732-support-normalized-cyclic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
