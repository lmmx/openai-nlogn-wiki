# exegenius task 0151-support-packed-bit-addition

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

Claim: The exceptions are few: $|B| \le \delta_{\text{bad}} M$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "|B| ≤ δbad M"

Paragraph:

> The construction first applies a constant number of cyclic shifts, whose composition is $S_0$. Outside a set $B$ of exceptional addresses, $S_0$ agrees with the exact map $T_0$ that performs the XORs. The fraction $\delta_{\text{bad}} = \min\{1, 80(f-1)2^{-K}\}$ is small when $K$ is large. The exceptions are few: $|B| \le \delta_{\text{bad}} M$.

### 2

Claim: The exact map $T_0$ preserves $B$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The ideal map T0 preserves all guard values and therefore preserves B"

Paragraph:

> The exact map $T_0$ preserves $B$. Since $S_0$ and $T_0$ agree outside $B$ and both are bijections, $T_0S_0^{-1}$ fixes every address outside $B$ and permutes $B$. Applying this correction after the shifts therefore gives $T_0$ exactly.

### 3

Claim: Under the asymptotic conditions of the lemma, the time is $O(V(L^\tau+1))$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "When Arect = O(p), R exceeds every fixed polynomial in p, f ≤ d ≤ p, and K/ log p → ∞, this is O(V (Lτ + 1))"

Paragraph:

> Under the asymptotic conditions of the lemma, the time is $O(V(L^\tau+1))$.

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

Write the answer to `exegenius/tasks/0151-support-packed-bit-addition.answer.json`, then run `exegenius submit 0151-support-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.
