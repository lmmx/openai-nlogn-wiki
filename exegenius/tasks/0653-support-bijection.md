# exegenius task 0653-support-bijection

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

Claim: The paper uses this in its address-field interchange, which

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "interchanges two disjoint contiguous address fields of u bits in an array"

Paragraph:

> The paper uses this in its address-field interchange, which. Its update lines each change one chunk of each address, and. Two bijections of the rectangle, $S_0$ (the one its update lines compose to) and $T_0$ (the ideal one), agree outside $G$, the [Exceptional set](exceptional-set.md) of bad addresses, so they are compared on the complement of $G$. (The paper's $B$ is $G$.) $S_0(G^c)=T_0(G^c)=G^c$, so $S_0(G)=G$. Its intermediate steps are not moves:

### 2

Claim: Its update lines each change one chunk of each address, and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "so each line is a bijection of the rectangle"

Paragraph:

> The paper uses this in its address-field interchange, which. Its update lines each change one chunk of each address, and. Two bijections of the rectangle, $S_0$ (the one its update lines compose to) and $T_0$ (the ideal one), agree outside $G$, the [Exceptional set](exceptional-set.md) of bad addresses, so they are compared on the complement of $G$. (The paper's $B$ is $G$.) $S_0(G^c)=T_0(G^c)=G^c$, so $S_0(G)=G$. Its intermediate steps are not moves:

### 3

Claim: (The paper's $B$ is $G$.)

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The ideal map T0 preserves all guard values and therefore preserves B."

Paragraph:

> The paper uses this in its address-field interchange, which. Its update lines each change one chunk of each address, and. Two bijections of the rectangle, $S_0$ (the one its update lines compose to) and $T_0$ (the ideal one), agree outside $G$, the [Exceptional set](exceptional-set.md) of bad addresses, so they are compared on the complement of $G$. (The paper's $B$ is $G$.) $S_0(G^c)=T_0(G^c)=G^c$, so $S_0(G)=G$. Its intermediate steps are not moves:

### 4

Claim: Its intermediate steps are not moves:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Although its final effect is an exact permutation, its intermediate steps form pointwise XOR combinations of data."

Paragraph:

> The paper uses this in its address-field interchange, which. Its update lines each change one chunk of each address, and. Two bijections of the rectangle, $S_0$ (the one its update lines compose to) and $T_0$ (the ideal one), agree outside $G$, the [Exceptional set](exceptional-set.md) of bad addresses, so they are compared on the complement of $G$. (The paper's $B$ is $G$.) $S_0(G^c)=T_0(G^c)=G^c$, so $S_0(G)=G$. Its intermediate steps are not moves:

### 5

Claim: The paper states that

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "bijection of P: for fixed controls and spectators it is a cyclic permutation of the valid target interval"

Paragraph:

> The second use is a tape procedure, a fixed procedure on one-dimensional Turing machine tapes that rearranges the bits stored on them. Its padded address set $\Gamma$ is a set of integer addresses on which the step acts. The paper states that. For the valid interval $\{0,1,2,3\}$ and offset $1$, this is the map $f$ above, and rotating back by $-1$ undoes it. The paper also gives, so the stored data can be recovered after the step.

### 6

Claim: The paper also gives

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "An inverse is explicit"

Paragraph:

> The second use is a tape procedure, a fixed procedure on one-dimensional Turing machine tapes that rearranges the bits stored on them. Its padded address set $\Gamma$ is a set of integer addresses on which the step acts. The paper states that. For the valid interval $\{0,1,2,3\}$ and offset $1$, this is the map $f$ above, and rotating back by $-1$ undoes it. The paper also gives, so the stored data can be recovered after the step.

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

Write the answer to `exegenius/tasks/0653-support-bijection.answer.json`, then run `exegenius submit 0653-support-bijection` in the project directory. If submit rejects the answer, fix the answer and submit again.
