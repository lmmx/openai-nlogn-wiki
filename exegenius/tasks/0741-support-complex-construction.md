# exegenius task 0741-support-complex-construction

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

Claim: A forward invocation changes $y_S$ to $y_S+x_S$ and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "leaves every other value unchanged"

Paragraph:

> the old scratch values, the next four add $x$ to $y$, and the last two restore the scratch values. A forward invocation changes $y_S$ to $y_S+x_S$ and.

### 2

Claim: A value $x_T$ enters $C_\ell$ for each of the $|S\cap T|$ elements $\ell\in S\cap T$, and enters $C_*$ once, so scatter gives it the central coefficient $\varpi_{ST}$, which the source writes as

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "(|S ∩ T | − 1)/2"

Paragraph:

> The complex construction changes the neighbour rule of the [Bit construction](bit-construction.md) and keeps its copy step. A value $x_T$ enters $C_\ell$ for each of the $|S\cap T|$ elements $\ell\in S\cap T$, and enters $C_*$ once, so scatter gives it the central coefficient $\varpi_{ST}$, which the source writes as.

### 3

Claim: That coefficient is $0$ at intersection one, $-\tfrac12$ at intersection zero and $\tfrac12$ at intersection two, so the neighbours are the distinct triples with intersection zero or two:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The side cancels it for distinct triples with intersection zero or two"

Paragraph:

> Side injection subtracts $\varpi_{ST}W_{ST}$, so the two routes cancel for each neighbour. A side wire is needed exactly where the central coefficient is nonzero and $T\neq S$. That coefficient is $0$ at intersection one, $-\tfrac12$ at intersection zero and $\tfrac12$ at intersection two, so the neighbours are the distinct triples with intersection zero or two:. In the bit case, the central coefficient from $x_T$ to $y_S$ is, nonzero at intersection one, so the bit neighbours have intersection one.

### 4

Claim: In the bit case, the central coefficient from $x_T$ to $y_S$ is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "|S ∩ T | mod 2"

Paragraph:

> Side injection subtracts $\varpi_{ST}W_{ST}$, so the two routes cancel for each neighbour. A side wire is needed exactly where the central coefficient is nonzero and $T\neq S$. That coefficient is $0$ at intersection one, $-\tfrac12$ at intersection zero and $\tfrac12$ at intersection two, so the neighbours are the distinct triples with intersection zero or two:. In the bit case, the central coefficient from $x_T$ to $y_S$ is, nonzero at intersection one, so the bit neighbours have intersection one.

### 5

Claim: Starting from $(x,y)$,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "the three stages give (x, y + x), then (−y, y + x), then (−y, x)."

Paragraph:

> Stages 1 and 3 are forward invocations from $X$ to $Y$, and stage 2 is the inverse schedule. Starting from $(x,y)$, The net effect is,

### 6

Claim: The net effect is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "(Xa , Ya ) 7−→ (−Ya , Xa )"

Paragraph:

> Stages 1 and 3 are forward invocations from $X$ to $Y$, and stage 2 is the inverse schedule. Starting from $(x,y)$, The net effect is,

### 7

Claim: ,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "and restores every auxiliary value."

Paragraph:

> Stages 1 and 3 are forward invocations from $X$ to $Y$, and stage 2 is the inverse schedule. Starting from $(x,y)$, The net effect is,

### 8

Claim: The source gives

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "sc = Wc m − 2N + 2Lc = 1873807244636671267308000000 < Wc m."

Paragraph:

> Let $s_c$ be the total number of smaller calls. The source gives $L_c$ is the dimension lost on central-wire edges. By Lemma 6, so $L_c=792250767000000<N/2=2113976056500000$.

### 9

Claim: By Lemma 6,

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "L = Ich,"

Paragraph:

> Let $s_c$ be the total number of smaller calls. The source gives $L_c$ is the dimension lost on central-wire edges. By Lemma 6, so $L_c=792250767000000<N/2=2113976056500000$.

### 10

Claim: Dividing by $W_c$ gives $s_c/W_c<m$, the inequality

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "that the total number s of smaller calls satisfies s < W m"

Paragraph:

> The letter $m$ changes meaning here: it is the dimension of the label space, $m=h^3$. Dividing by $W_c$ gives $s_c/W_c<m$, the inequality that the rank-saving argument uses.

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

Write the answer to `exegenius/tasks/0741-support-complex-construction.answer.json`, then run `exegenius submit 0741-support-complex-construction` in the project directory. If submit rejects the answer, fix the answer and submit again.
