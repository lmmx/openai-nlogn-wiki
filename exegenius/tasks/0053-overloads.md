# exegenius task 0053-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the page that changes should do: use another letter, or say where the letter is used that it means something else there than on the other page. For the same thing, `note` may be empty.
- `change` is the page that changes. Leave it out for the later page. Give the earlier page's id when its use of the letter is the odd one out, for instance when the sources use the letter as the later page does, and the earlier page binds it on the page, not in a name. A page that other pages take the letter from keeps it and says where its meaning changes.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $j$
   - on `gaussian-resampling`: $j$ (source index): An index of the entries of u, read modulo s.
   - on [Radix-digit convolution](radix-digit-convolution.md): $j$ (coefficient index): The power of X whose coefficient in W is taken.
2. $j$
   - on `gaussian-resampling`: $j$ (source index): An index of the entries of u, read modulo s.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $j$ (output index): The index of an output entry of the transform, running from 0 to q-1.
3. $k$
   - on `gaussian-resampling`: $k$ (target index): An index of the entries of g, read modulo t.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $k$ (input index): The index of an input entry of the transform, running from 0 to q-1.
4. $r$
   - on `gaussian-resampling`: $r$ (Neumann index): The summation index of the Neumann series $\sum_{r\ge0}E^r$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $r$ (shifted index): The index $(l-k) \bmod q$ for fixed $k$, which runs over $0,\dots,q-1$ as $l$ does.
5. $p$
   - on `gaussian-resampling`: $p$ (precision parameter): The integer precision parameter, greater than 100, in the hypotheses of the estimate.
   - on [Radix-digit convolution](radix-digit-convolution.md): $p$ (first integer): The first of the two integers being multiplied, below 2^{bm}.

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

Write the answer to `exegenius/tasks/0053-overloads.answer.json`, then run `exegenius submit 0053-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
