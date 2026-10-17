# exegenius task 0282-support-exchange-network

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

Claim: At every $a$,
$$(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x),$$
that is $(X_a,Y_a)\mapsto(-Y_a,X_a)$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$(x,y+x)$, then $(-y,y+x)$, then $(-y,x)$."

Paragraph:

> The inverse schedule, the forward one with target updates negated, performs $X\gets X-Y$ when $Y$ is the source bank and $X$ the target. Run forward $X\to Y$ at stage 1, inverse $Y\to X$ at stage 2 and forward $X\to Y$ at stage 3. At every $a$,
> $$(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x),$$
> that is $(X_a,Y_a)\mapsto(-Y_a,X_a)$, restoring all scratch wires.

### 2

Claim: , restoring all scratch wires

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "Each invocation restores its own auxiliary wires."

Paragraph:

> The inverse schedule, the forward one with target updates negated, performs $X\gets X-Y$ when $Y$ is the source bank and $X$ the target. Run forward $X\to Y$ at stage 1, inverse $Y\to X$ at stage 2 and forward $X\to Y$ at stage 3. At every $a$,
> $$(x,y)\mapsto(x,y+x)\mapsto(-y,y+x)\mapsto(-y,x),$$
> that is $(X_a,Y_a)\mapsto(-Y_a,X_a)$, restoring all scratch wires.

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

Write the answer to `exegenius/tasks/0282-support-exchange-network.answer.json`, then run `exegenius submit 0282-support-exchange-network` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0282-support-exchange-network`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
