# exegenius task 0028-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the later page should do: use another letter, or say where the letter is used that it means something else here than on the earlier page. For the same thing, `note` may be empty.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $k$
   - on `radix-digit-convolution`: $k$ (digit width): The number of bits in one digit; the letter changes meaning from the padded length on the earlier page.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $k$ (padded length): The number of bits in the padded binary representation bin_k, that is, the length it pads to.
2. $x$
   - on `radix-digit-convolution`: $x$ (first integer): The integer represented by the first input string.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $x$ (first input): A binary string of length n, the first factor of the product.
3. $y$
   - on `radix-digit-convolution`: $y$ (second integer): The integer represented by the second input string.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $y$ (second input): A binary string of length n, the second factor of the product.
4. $m$
   - on `radix-digit-convolution`: $m$ (coefficient position): The index of a coefficient of the product polynomial, running over $0,\dots,2d-2$; the letter changes meaning from the integer argument of $\mathrm{bin}_k$.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $m$ (padded integer): The nonnegative integer, below 2^k, whose binary representation is taken.
5. $d$
   - on `chinese-remainder-map`: $d$ (cyclic axis count): The number of cyclic axes, which is the number of coordinates of a box point.
   - on [Radix-digit convolution](radix-digit-convolution.md): $d$ (digit count): The number of digit positions in each padded input.
6. $n$
   - on `chinese-remainder-map`: $n$ (position): A position in the cyclic convolution, ranging over 0 to T-1.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $n$ (input length): The number of bits in each of the inputs x and y.
7. $i$
   - on `prime-source-lengths`: $i$ (axis index): An index from $1$ to $d$ labelling the axes.
   - on [Gaussian resampling](gaussian-resampling.md): $i$ (imaginary unit): The imaginary unit, with i squared equal to -1.
8. $x$
   - on `prime-source-lengths`: $x$ (padded length variable): A real number standing for a large power-of-two padded length in the prime-count statement.
   - on [Radix-digit convolution](radix-digit-convolution.md): $x$ (first integer): The integer represented by the first input string.
9. $x$
   - on `prime-source-lengths`: $x$ (padded length variable): A real number standing for a large power-of-two padded length in the prime-count statement.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $x$ (first input): A binary string of length n, the first factor of the product.

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

Write the answer to `exegenius/tasks/0028-overloads.answer.json`, then run `exegenius submit 0028-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
