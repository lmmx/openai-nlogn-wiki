# exegenius task 0033-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the page that changes should do: use another letter, or say where the letter is used that it means something else there than on the other page. For the same thing, `note` may be empty.
- `change` is the page that changes. Leave it out for the later page. Give the earlier page's id when its use of the letter is the odd one out, for instance when the sources use the letter as the later page does, and the earlier page binds it on the page, not in a name. A page that other pages take the letter from keeps it and says where its meaning changes.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $s$
   - on `subset-network`: $s$ (smaller call total): The total number of smaller calls, counted as the sum of the ranks of all edge differences.
   - on [Frame of a network vertex](frame.md): $s$ (edge end vertex): The vertex at the end of an edge that starts at r.
2. $L$
   - on `subset-network`: $L$ (dimension loss): The total dimension lost on decreasing edges.
   - on [Linear algebra over a field](linear-algebra.md): $L$ (linear map): A linear map from $V$ into itself, that is, a map with $L(u+v)=L(u)+L(v)$ and $L(cu)=cL(u)$.

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
        "change": {
          "default": null,
          "description": "For different things: the page that changes, the later page if left out.",
          "type": [
            "string",
            "null"
          ]
        },
        "note": {
          "description": "For different things: what the page that changes should do.",
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

Write the answer to `exegenius/tasks/0033-overloads.answer.json`, then run `exegenius submit 0033-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
