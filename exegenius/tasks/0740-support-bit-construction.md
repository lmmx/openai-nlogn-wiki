# exegenius task 0740-support-bit-construction

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

Claim: The paper gives the central coefficient as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "In the bit case, the central coefficient from xT to yS is |S ∩ T | mod 2."

Paragraph:

> The paper gives the central coefficient as That parity is odd for intersection one and for $S=T$, and even for intersections zero and two. The side route must cancel the odd off-diagonal case, and it does so because it.

### 2

Claim: The side route must cancel the odd off-diagonal case, and it does so because it

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "cancels exactly the intersection-one cases"

Paragraph:

> The paper gives the central coefficient as That parity is odd for intersection one and for $S=T$, and even for intersections zero and two. The side route must cancel the odd off-diagonal case, and it does so because it.

### 3

Claim: The paper's lemma for one forward invocation is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "For arbitrary initial values of its auxiliary wires, a forward invocation changes yS to"

Paragraph:

> The paper's lemma for one forward invocation is $\eta_S+\xi_S$, the result derived above, and it

### 4

Claim: $\eta_S+\xi_S$, the result derived above, and it

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "restores every auxiliary value."

Paragraph:

> The paper's lemma for one forward invocation is $\eta_S+\xi_S$, the result derived above, and it

### 5

Claim: The paper states its effect as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The inverse schedule with logical source Y and target X effects X ← X − Y"

Paragraph:

> 1. A forward invocation from $X$ to $Y$ gives $(X,\,Y)\mapsto(X,\,Y+X)$.
> 2. The [inverse schedule](schedule.md) from $Y$ to $X$ has $Y$ as its logical source and $X$ as its target. The paper states its effect as. Hence $(X,\,Y+X)\mapsto(-Y,\,Y+X)$, since $X-(Y+X)=-Y$.
> 3. A forward invocation from $X$ to $Y$ gives $(-Y,\,Y+X)\mapsto(-Y,\,(Y+X)+(-Y))=(-Y,\,X)$.

### 6

Claim: The paper states this as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "In the bit construction this is the permutation exchanging Xa"

Paragraph:

> Each invocation restores its auxiliary wires, so the scratch wires end at their starting values. Over $\mathbb F_2$ we have $-1=1$, so the result is $(X,Y)\mapsto(Y,X)$, the exchange of the two banks. The paper states this as and Ya.

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

Write the answer to `exegenius/tasks/0740-support-bit-construction.answer.json`, then run `exegenius submit 0740-support-bit-construction` in the project directory. If submit rejects the answer, fix the answer and submit again.
