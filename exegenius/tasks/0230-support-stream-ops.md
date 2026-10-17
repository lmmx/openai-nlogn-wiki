# exegenius task 0230-support-stream-ops

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

Claim: Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels therefore already costs $\Theta(n)\cdot\Theta(\log n)=\Theta(n\log n)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels already costs $\Theta(n\log n)$"

Paragraph:

> All four operations below run on the [Fixed finite-tape machine model](machine-model.md), where each head moves at most one cell per step, so one pass over the array costs time proportional to $V$. The data of the $n$-bit inputs occupy $V=\Theta(n)$ stored bits, so one pass costs $\Theta(n)$. A transform built from [Butterflies and the fast transform](butterfly.md) has $\Theta(\log n)$ levels, and one scan of the array per level costs $\Theta(n)$ each time. Scanning an array of $\Theta(n)$ stored bits at each of $\Theta(\log n)$ transform levels therefore already costs $\Theta(n)\cdot\Theta(\log n)=\Theta(n\log n)$, the bound to be beaten. So each rearrangement must cost one pass, not one pass per level.

### 2

Claim: For a fixed radix, each of the following takes $O(V)$ steps on a fixed number of one-dimensional tapes

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Each of the following operations on an array of volume $V$ takes $O(V)$ steps on a fixed number of one-dimensional tapes"

Paragraph:

> For a fixed radix, each of the following takes $O(V)$ steps on a fixed number of one-dimensional tapes:

### 3

Claim: The bounds include setting up counters and returning the work tapes to their initial state, and the constants depend on the radix, the pointwise map and $W$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The bounds include shape preparation, counter initialization and resets, and returning or clearing the visited portions of work tapes."

Paragraph:

> The bounds include setting up counters and returning the work tapes to their initial state, and the constants depend on the radix, the pointwise map and $W$

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

Write the answer to `exegenius/tasks/0230-support-stream-ops.answer.json`, then run `exegenius submit 0230-support-stream-ops` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0230-support-stream-ops`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
