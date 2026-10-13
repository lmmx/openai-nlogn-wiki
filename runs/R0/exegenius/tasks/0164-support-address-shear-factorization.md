# exegenius task 0164-support-address-shear-factorization

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

Claim: A lower-triangular transformation costs $O(V)$, where $V$ is the stored bit volume

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "earlier fields in linear time"

Paragraph:

> A lower-triangular transformation costs $O(V)$, where $V$ is the stored bit volume. Update coordinates from last to first, so each becomes a fixed combination of earlier, still unchanged, coordinates. The coefficients come from the finitely many matrices, not from $V$, and the paper's lemma states that such an update of a later field takes linear time in the stored bits. So each pass is linear, and $m$ is fixed.

### 2

Claim: The paper shows $N>2L_{\rm b}$, so $s_{\rm b}<W_{\rm b}m$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The sum of the rational ranks of all edge differences is"

Paragraph:

> Each edge of the bit network carries such a matrix. The interchange count of the network is $s_{\rm b}$, the sum of their ranks. The network's rank budget, which counts dimension changes along its edges (its motif-residual lemma), gives $s_{\rm b}=W_{\rm b}m-N+2L_{\rm b}$, where $W_{\rm b}$ is the number of wires, $N$ the total source dimension and $L_{\rm b}$ the total dimension lost on decreasing edges. The paper shows $N>2L_{\rm b}$, so $s_{\rm b}<W_{\rm b}m$. Per wire, the interchanges are fewer than $m$, which the recurrence turns into a saving of a power of the chunk width (the chunk length).

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

Write the answer to `exegenius/tasks/0164-support-address-shear-factorization.answer.json`, then run `exegenius submit 0164-support-address-shear-factorization` in the project directory. If submit rejects the answer, fix the answer and submit again.
