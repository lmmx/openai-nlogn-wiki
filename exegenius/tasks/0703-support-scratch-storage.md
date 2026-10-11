# exegenius task 0703-support-scratch-storage

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

Claim: The paper accordingly allows any starting values:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We call all these auxiliary wires scratch wires; their initial values may be arbitrary."

Paragraph:

> A tape machine reuses its work space, so a scratch wire may hold an old value. The paper accordingly allows any starting values:

### 2

Claim: The paper's bit construction uses scalars in $\mathbb{F}_2$ and calls triples $S$ and $T$ neighbours when they share one element:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "scalars lie in F2 , and S, T are neighbors when |S ∩ T | = 1."

Paragraph:

> A triple is a three-element subset of the ground set. The paper's bit construction uses scalars in $\mathbb{F}_2$ and calls triples $S$ and $T$ neighbours when they share one element: Here $S\cap T$ is the set of elements in both $S$ and $T$, and $\ell\in S$ means that $\ell$ belongs to $S$.

### 3

Claim: The paper's count is

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "net target change is (J V + RG)x, independently of a, c."

Paragraph:

> Rows 0 to 5 therefore change $y$ by $-Ja-Rc+R(c+Gx)+J(a+Vx)$. The terms in $a$ and $c$ cancel, leaving $(JV+RG)x$. The paper's count is

### 4

Claim: So $JV+RG$ is the identity, which gives the paper's lemma:

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "For arbitrary initial values of its auxiliary wires, a forward invocation changes yS to"

Paragraph:

> Consider $x_T$ in $y_S$. Under $RG$ its coefficient is $|S\cap T| \bmod 2$, since $x_T$ reaches $y_S$ once per element of $S\cap T$. Under $JV$ it is 1 exactly when $|S\cap T|=1$. Their sum mod 2 is 1 when $T=S$, since $|S\cap S|=3$ is odd and $S$ is not its own neighbour, and 0 otherwise. So $JV+RG$ is the identity, which gives the paper's lemma: $y_S+x_S$ and

### 5

Claim: $y_S+x_S$ and

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "leaves every other value unchanged."

Paragraph:

> Consider $x_T$ in $y_S$. Under $RG$ its coefficient is $|S\cap T| \bmod 2$, since $x_T$ reaches $y_S$ once per element of $S\cap T$. Under $JV$ it is 1 exactly when $|S\cap T|=1$. Their sum mod 2 is 1 when $T=S$, since $|S\cap S|=3$ is odd and $S$ is not its own neighbour, and 0 otherwise. So $JV+RG$ is the identity, which gives the paper's lemma: $y_S+x_S$ and

### 6

Claim: On arrays, the gates act

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "pointwise at every address"

Paragraph:

> On arrays, the gates act. Scratch storage restores values at every address of the [address field](address-field.md) it occupies.

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

Write the answer to `exegenius/tasks/0703-support-scratch-storage.answer.json`, then run `exegenius submit 0703-support-scratch-storage` in the project directory. If submit rejects the answer, fix the answer and submit again.
