# exegenius task 0234-support-controlled-shifts

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

Claim: It costs $O(V)$ if each control used in the offset has $O(b)$ digits and the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "costs $O(V)$ if the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values"

Paragraph:

> Fix a prime $q$ (on this page $q$ is a prime, not a sequence length), and let $b\ge1$ be the number of base-$q$ digits of a field. Put $Q=q^b$, the number of values a field can take, and let $V$ be the array volume, the number of stored data bits. The target field has value $y\in[Q]=\{0,\dots,Q-1\}$ and follows a fixed number of control fields. The update is
> $$y\longmapsto y+a \pmod Q,$$
> where $a\in[Q]$ is the offset, prepared from the control values. It costs $O(V)$ if each control used in the offset has $O(b)$ digits and the offset can be prepared in $b^{O(1)}$ time from the fixed number of control values. A fixed rational linear combination of the controls, reduced modulo $Q$, qualifies.

### 2

Claim: This is again one split and one merge

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Reversing the roles of this split and merge implements multiplication by $c^{-1}$ modulo $Q$."

Paragraph:

> **Inverse scaling.** Multiplication by $c^{-1}$ must put at position $y$ the block from position $y'=cy-jQ$, with $j=\lfloor cy/Q\rfloor$. The positions $y$ sharing one $j$ form a consecutive range, and their sources $y'$ increase in steps of $c$ through a single class of residues modulo $c$, namely $y'\equiv -jQ$. So the roles of split and merge are exchanged: split the input into $c$ streams by the residue of its position modulo $c$, then write the output range by range, filling range $j$ from the stream of class $-jQ \bmod c$. Different $j$ give different classes because $\gcd(Q,c)=1$, so each stream is consumed by exactly one range, in order. This is again one split and one merge

### 3

Claim: **Negation and units.** Negation sends block $y$ to block $Q-y$: it leaves block $0$ fixed and reverses the other $Q-1$ blocks

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Negation leaves the block at zero fixed and reverses the order of the other $Q-1$ blocks."

Paragraph:

> **Negation and units.** Negation sends block $y$ to block $Q-y$: it leaves block $0$ fixed and reverses the other $Q-1$ blocks Push them onto a temporary tape and pop them, then reverse each popped block again on a second tape to restore its bits.

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

Write the answer to `exegenius/tasks/0234-support-controlled-shifts.answer.json`, then run `exegenius submit 0234-support-controlled-shifts` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0234-support-controlled-shifts`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
