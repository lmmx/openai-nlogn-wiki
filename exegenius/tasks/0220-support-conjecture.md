# exegenius task 0220-support-conjecture

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

Claim: In 1971 Schönhage and Strassen gave a multiplication algorithm running in $O(n\log n\log\log n)$ time, and proposed $n\log n$ as the optimal order of growth

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "and proposed $n\log n$ as the optimal order of growth"

Paragraph:

> In 1971 Schönhage and Strassen gave a multiplication algorithm running in $O(n\log n\log\log n)$ time, and proposed $n\log n$ as the optimal order of growth. This is a lower-bound statement, not a claim about one algorithm: for every multiplication machine there are a constant $c>0$ and a threshold such that the machine needs at least $c\,n\log n$ steps whenever $n$ exceeds the threshold. Both may depend on the machine, but not on $n$.

### 2

Claim: Equivalently, its running time divided by $n\log n$ must come arbitrarily close to zero for infinitely many $n$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Its negation requires one machine satisfying"

Paragraph:

> Refuting a "for every machine, for all large $n$" statement needs only one machine for which no constant $c>0$ works. Equivalently, its running time divided by $n\log n$ must come arbitrarily close to zero for infinitely many $n$. Beating $n\log n\log\log n$ is not enough; the time must fall below every constant multiple of $n\log n$ along some inputs.

### 3

Claim: After a sequence of improvements, Harvey and van der Hoeven reached an $O(n\log n)$ bound that holds without any unproved assumption

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Harvey and van der Hoeven reached the unconditional $O(n\log n)$ upper"

Paragraph:

> For decades the gap between $n\log n\log\log n$ and $n\log n$ was the open part. After a sequence of improvements, Harvey and van der Hoeven reached an $O(n\log n)$ bound that holds without any unproved assumption. That matches the conjectured order, so the best known algorithms were consistent with the conjecture.

### 4

Claim: Its time divided by $n\lg n$ is at most a constant times $(\lg n)^{-\kappa}$, which tends to zero for all large $n$, not merely along a subsequence

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The power saving proved here gives a limit of zero through all input lengths"

Paragraph:

> The main result gives the required machine. Its running time is $O(n(\lg n)^{1-\kappa})$, where $\kappa>0$ is a fixed constant, the amount by which the exponent of the logarithm is lowered. Its time divided by $n\lg n$ is at most a constant times $(\lg n)^{-\kappa}$, which tends to zero for all large $n$, not merely along a subsequence. This is stronger than the refutation needs. The conjecture is therefore false in this model, although the saving is tiny because $\kappa$ is extremely small.

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

Write the answer to `exegenius/tasks/0220-support-conjecture.answer.json`, then run `exegenius submit 0220-support-conjecture` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0220-support-conjecture`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
