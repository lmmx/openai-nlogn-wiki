# exegenius task 0232-support-hvdh-multiplier

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

Claim: The paper takes this bound from Harvey and van der Hoeven

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "We use the established $O(N\log N)$ integer multiplier of"

Paragraph:

> The multiplier runs in the [Fixed finite-tape machine model](machine-model.md), the same model as the main result, so a call costs its $O(N\log N)$ steps with no change of machine to account for. The paper takes this bound from Harvey and van der Hoeven; its proof is in their paper and is not reproduced here. It is the bound that Schönhage and Strassen conjectured optimal ([Schönhage–Strassen optimality conjecture](conjecture.md)), so it is the benchmark the main result beats.

### 2

Claim: These ring products go through signed packing

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "use signed packing and the established $O(n\log n)$ multiplier as an"

Paragraph:

> The multiplier is called on the first kind once the new algorithm reduces its [Fourier transforms](dft.md) to polynomial products over $\mathbb C[y]/(y^r+1)$. These ring products go through signed packing: [Signed packing](signed-packing.md) turns each into four integer products on $O(rp)$ bits, where $r$ is the record length and $p$ the number of fractional bits.

### 3

Claim: The second kind is the chirp numerators, which have $O(p)$ bits and are squared and multiplied directly

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Computing their squares and products with the previously established $O(N\log(2N))$ multiplier"

Paragraph:

> The second kind is the chirp numerators, which have $O(p)$ bits and are squared and multiplied directly.

### 4

Claim: First, each call is an ordinary subroutine call on records of $O(rp)$ bits, fewer than the input, so it is not a call of the improved algorithm on a smaller input

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "they do not call the improved algorithm being constructed."

Paragraph:

> First, each call is an ordinary subroutine call on records of $O(rp)$ bits, fewer than the input, so it is not a call of the improved algorithm on a smaller input Hence no recurrence for the new algorithm passes through the multiplier.

### 5

Claim: Second, whatever recursion the Harvey–van der Hoeven algorithm uses internally is already paid for by its $O(N\log N)$ bound

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "The internal recursion of the established integer"

Paragraph:

> Second, whatever recursion the Harvey–van der Hoeven algorithm uses internally is already paid for by its $O(N\log N)$ bound. Its cost is therefore charged as a separate term, not folded into a recurrence

### 6

Claim: Its cost is therefore charged as a separate term, not folded into a recurrence

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "already included in their separately charged running times."

Paragraph:

> Second, whatever recursion the Harvey–van der Hoeven algorithm uses internally is already paid for by its $O(N\log N)$ bound. Its cost is therefore charged as a separate term, not folded into a recurrence

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

Write the answer to `exegenius/tasks/0232-support-hvdh-multiplier.answer.json`, then run `exegenius submit 0232-support-hvdh-multiplier` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0232-support-hvdh-multiplier`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
