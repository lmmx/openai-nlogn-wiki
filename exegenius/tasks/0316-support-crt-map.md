# exegenius task 0316-support-crt-map

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

Claim: The parameters of [Parameter and prime-length choice](parameter-choice.md) give $T<2^p$

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$t_i\leq r\leq T<8n/b<2^{6b}=2^p$"

Paragraph:

> The scan keeps one binary counter per axis, so the counters have $\log_2T$ bits in total. The parameters of [Parameter and prime-length choice](parameter-choice.md) give $T<2^p$, so the counters and stored bounds $s_i$ have $O(p)$ bits. At each of the $T$ addresses, updating counters, testing validity and copying a record take $O(p)$ steps, so a scan costs $O(Tp)$.

### 2

Claim: Computing the offsets, for at most $T/t_i$ prefixes, is negligible next to $Tp$ because

Quotation, from Integer multiplication below n log n (OpenAI, 2026): "$t_i\ge r/2$ and $r$ exceeds every fixed power of $p$"

Paragraph:

> In this order the controls $a_j$, $j<i$, follow the target $a_i$. Reversing the axis order to $(a_1,\dots,a_d)$ puts the controls first. Update the targets for $i=d,d-1,\dots,1$, so no lower-index control has yet changed when axis $i$ is updated and the offset is computed from the original digits. Each update is a prefix-controlled cyclic shift of the valid interval $[0,s_i)$ and the identity on $[s_i,t_i)$, so zero padding stays zero. The map is implemented by these shifts, each of linear cost by [Controlled shifts and rational scalings](controlled-shifts.md). Computing the offsets, for at most $T/t_i$ prefixes, is negligible next to $Tp$ because.

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

Write the answer to `exegenius/tasks/0316-support-crt-map.answer.json`, then run `exegenius submit 0316-support-crt-map` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0316-support-crt-map`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
