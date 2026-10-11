# exegenius task 0036-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the later page should do: use another letter, or say where the letter is used that it means something else here than on the earlier page. For the same thing, `note` may be empty.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $p$
   - on `chinese-remainder-map`: $p$ (cyclic position): A position on the cycle of length T, with 0 at most p less than T.
   - on [Radix-digit convolution](radix-digit-convolution.md): $p$ (coefficient position): The index of a coefficient of the product, running over $0,\dots,2d-2$.
2. $w$
   - on `chinese-remainder-map`: $w$ (output position): The position of an output coefficient of the convolution, with 0 at most w less than T.
   - on [Radix-digit convolution](radix-digit-convolution.md): $w$ (digit width): The number of bits in one digit.
3. $q$
   - on `prime-source-lengths`: $q$ (prime variable): A variable standing for a prime number.
   - on [Chinese-remainder map](chinese-remainder-map.md): $q$ (second cyclic position): A second position on the cycle of length T, with 0 at most q less than T.

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Verdict": {
      "additionalProperties": false,
      "properties": {
        "candidate": {
          "description": "Number of the candidate, as listed.",
          "format": "uint",
          "minimum": 0,
          "type": "integer"
        },
        "note": {
          "description": "For different things: what the later page should do.",
          "type": "string"
        },
        "same": {
          "description": "True if the two bindings denote the same thing.",
          "type": "boolean"
        }
      },
      "required": [
        "candidate",
        "same",
        "note"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "verdicts": {
      "items": {
        "$ref": "#/$defs/Verdict"
      },
      "type": "array"
    }
  },
  "required": [
    "verdicts"
  ],
  "title": "OverloadsAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0036-overloads.answer.json`, then run `exegenius submit 0036-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
