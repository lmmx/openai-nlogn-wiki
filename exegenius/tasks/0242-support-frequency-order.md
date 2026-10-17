# exegenius task 0242-support-frequency-order

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

Claim: The additive group of $\mathcal R_r$ has no two-torsion (no nonzero element equals its negative), so the sum is zero

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Hence the sum is zero, since the additive group of"

Paragraph:

> The ring has zero divisors, so we cannot divide by $\omega_t^j-1$; directly, $\sum_{k}\omega_t^{jk}$ equals $t$ if $t\mid j$ and $0$ otherwise. For $t\nmid j$ write $j=2^vj_0$ with $j_0$ odd and $0\le v<a$. Replacing $k$ by $k+t/2^{v+1}$ modulo $t$ permutes the summands and multiplies the sum by $y^{rj_0}=-1$, so the sum equals its negative. The additive group of $\mathcal R_r$ has no two-torsion (no nonzero element equals its negative), so the sum is zero. Expanding the composite gives $F_t^+F_t^-=t^{-1}I$.

### 2

Claim: Let $B_t$ be the permutation moving the entry at $j$ to $\operatorname{rev}_a(j)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Let $B_t$ denote this record permutation: it moves the entry at $j$ to $\operatorname{rev}_a(j)$."

Paragraph:

> Call a position's address bits, high to low, slots $a-1,\dots,0$. A pair differs only in the highest unprocessed slot, where $H_0$ writes $b$. After $s$ rounds, $s$ being the number of completed rounds, slots $a-1,\dots,a-s$ hold frequency bits $0,\dots,s-1$ and the rest index a sequence of length $t/2^s$; the next round writes bit $s$ into slot $a-1-s$. After $a$ rounds $(F_t^-z)_j$ sits at slot $\operatorname{rev}_a(j)$, where $\operatorname{rev}_a$ reverses the $a$ binary digits of $j$. Let $B_t$ be the permutation moving the entry at $j$ to $\operatorname{rev}_a(j)$

### 3

Claim: The product at slot $s$ is therefore the product of the two entries of that one frequency, and the result stays in the same bit-reversed order

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "retain the same frequency order through their pointwise product"

Paragraph:

> The pointwise product multiplies two transformed arrays slot by slot, each slot a product in $\mathcal R_r$, and never moves an entry between slots. Both arrays come from the same procedure $B_tF_t^-$, so slot $s$ of each holds the entry of frequency $\operatorname{rev}_a(s)$. The product at slot $s$ is therefore the product of the two entries of that one frequency, and the result stays in the same bit-reversed order. The opposite procedure takes this order as its input.

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

Write the answer to `exegenius/tasks/0242-support-frequency-order.answer.json`, then run `exegenius submit 0242-support-frequency-order` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0242-support-frequency-order`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
