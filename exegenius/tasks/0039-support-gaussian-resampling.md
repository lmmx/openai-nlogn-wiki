# exegenius task 0039-support-gaussian-resampling

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

Claim: Second, the paper gives $\|N-I\|<1/2$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "∥N − I∥ < 1/2, so N is invertible by the Neumann series"

Paragraph:

> Second, the paper gives $\|N-I\|<1/2$, so $N$ is invertible. Its inverse is the Neumann series $N^{-1}=\sum_{r\ge 0}(I-N)^r$, where $r$ is the summation index. This series is the matrix analogue of a geometric series. Each term has norm at most $2^{-r}$, so the series converges, and multiplying its partial sums by $N$ leaves $I$ minus a term that tends to $0$.

### 2

Claim: The paper bounds $\|S/2\|<3/4$ and $\|N^{-1}/2\|<7/8$, and $\|2^{-(2\alpha^2-2)}D\|<1$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "∥D′ ∥ < 1"

Paragraph:

> Both factors are contractions, and the paper proves this for its parameter choices. $N-I$ is small because $D$ cancels the Gaussian factor at each selected coordinate, leaving only the small Gaussian weights of the other coordinates. The paper bounds $\|S/2\|<3/4$ and $\|N^{-1}/2\|<7/8$, and $\|2^{-(2\alpha^2-2)}D\|<1$. Since $\|C\|=1$, the norm of $B_0$ is at most $7/8$, so $\|B_0\|<1$.

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

Write the answer to `exegenius/tasks/0039-support-gaussian-resampling.answer.json`, then run `exegenius submit 0039-support-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
