# exegenius task 0027-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the page that changes should do: use another letter, or say where the letter is used that it means something else there than on the other page. For the same thing, `note` may be empty.
- `change` is the page that changes. Leave it out for the later page. Give the earlier page's id when its use of the letter is the odd one out, for instance when the sources use the letter as the later page does, and the earlier page binds it on the page, not in a name. A page that other pages take the letter from keeps it and says where its meaning changes.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $a$
   - on `linear-network`: $a$ (bank index): A triple of subsets $a=(a_1,a_2,a_3)$ that indexes each value of the two banks.
   - on [Linear algebra over a field](linear-algebra.md): $a$ (scalar): An arbitrary scalar in F.
2. $T$
   - on `linear-network`: $T$ (subset T): A three-element subset of $[h]$ used as a varying coordinate, not the linear map of the earlier page.
   - on [Linear algebra over a field](linear-algebra.md): $T$ (linear map): A linear map of V into itself, the map whose rank and invertibility are discussed.
3. $S$
   - on `linear-network`: $S$ (subset S): A three-element subset of $[h]$ used as the varying target coordinate of an invocation.
   - on [Linear algebra over a field](linear-algebra.md): $S$ (inverse map): The linear map that inverts T, when T is invertible.
4. $v$
   - on `frame`: $v$ (vertex): A source, gate or sink of the network, at which a frame is attached; here the letter names a vertex, not the triple count of the linear-network page.
   - on [Linear algebra over a field](linear-algebra.md): $v$ (vector): An arbitrary vector in V.
5. $u$
   - on `frame`: $u$ (edge start vertex): The vertex at which an edge starts, so that the edge runs from $u$ to $v$; here the letter names a vertex.
   - on [Linear algebra over a field](linear-algebra.md): $u$ (vector): An arbitrary vector in V.

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

Write the answer to `exegenius/tasks/0027-overloads.answer.json`, then run `exegenius submit 0027-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
