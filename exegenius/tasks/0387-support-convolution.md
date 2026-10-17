# exegenius task 0387-support-convolution

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

Claim: The normalized convolution is
$$\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}.$$
A fixed output coefficient is the average of $rM$ signed products of one coefficient of $f$ and one of $g$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Thus that coefficient averages $rM$ signed scalar products, and $\mathcal M_r$ is a bilinear contraction"

Paragraph:

> Let $M=\prod_{i<d}t_i$ be the number of addresses, and $T=rM$ the number of complex coefficients in an array. The normalized convolution is
> $$\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}.$$
> A fixed output coefficient is the average of $rM$ signed products of one coefficient of $f$ and one of $g$, so with $\|\cdot\|_\infty$ the largest modulus of a coefficient,
> $$\|\mathcal M_r(f,g)\|_\infty\le\|f\|_\infty\|g\|_\infty.$$
> Dividing by $T$ cancels the growth of a sum of $T$ products, which is the reason for the normalization.

### 2

Claim: Executing such a permutation is a sort of data on a tape, costing time proportional to the line length times a logarithm of it

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its two label-and-sort operations implement $P_t$ and $P_s^{-1}$, each costing $O(tp\log t)$."

Paragraph:

> Gaussian resampling lets the algorithm compute transforms of prime length through power-of-two lengths ([Gaussian resampling](gaussian-resampling.md)), but its formula reads the input and writes the output in permuted index order. Executing such a permutation is a sort of data on a tape, costing time proportional to the line length times a logarithm of it The extra logarithmic factor is what the power saving cannot afford, so the permutations stay inside the identities, and convolution is what lets them vanish. Write $\pi$ for a permutation of the indices, $F$ for the normalized Fourier transform of length $q$, and $F^+$ for the transform with the opposite sign in the exponent.

### 3

Claim: Thus the retained source permutation cancels when computing a convolution

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "retained source permutation $R$ cancels when computing a convolution."

Paragraph:

> Source side. Convolution is computed as a forward transform of each input, an entrywise product $\cdot$, and an opposite transform: $F(f*g)=q\,(Ff)\cdot(Fg)$ and $F^+F=I/q$, so $f*g=q^2F^+\bigl((Ff)\cdot(Fg)\bigr)$. An entrywise product pairs entries at the same position, so $\pi(a\cdot b)=(\pi a)\cdot(\pi b)$ for any permutation: scrambled forward outputs multiply to the scrambled product. The resampling permutation multiplies indices by a unit modulo the length, and for it $F^+\pi=\pi^{-1}F^+$, so applying the same $\pi$ in the opposite transform undoes the scramble. Thus the retained source permutation cancels when computing a convolution, and no sort occurs across the whole chain.

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

Write the answer to `exegenius/tasks/0387-support-convolution.answer.json`, then run `exegenius submit 0387-support-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0387-support-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
