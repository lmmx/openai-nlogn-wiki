# exegenius task 0168-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the later page should do: use another letter, or say where the letter is used that it means something else here than on the earlier page. For the same thing, `note` may be empty.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $q$
   - on `subset-intersection-network`: $q$ (volume shrink factor): The factor by which the stream volume shrinks in each smaller call.
   - on [Subspace labels](subspace-labels.md): $q$ (second vector): A vector of F, the second argument of the bilinear form.
2. $a$
   - on `complex-phase-network`: $a$ (kernel scalar a): The first scalar of the two-point kernel $aI+bX$, not the real numerator part of a Gaussian dyadic.
   - on [Gaussian dyadics](gaussian-dyadics.md): $a$ (real numerator part): The integer real part of the numerator $a + bi$ of a Gaussian dyadic.
3. $b$
   - on `complex-phase-network`: $b$ (kernel scalar b): The second scalar of the two-point kernel $aI+bX$, not the imaginary numerator part of a Gaussian dyadic.
   - on [Gaussian dyadics](gaussian-dyadics.md): $b$ (imaginary numerator part): The integer imaginary part of the numerator $a + bi$ of a Gaussian dyadic.
4. $x$
   - on `radix-digit-convolution`: $x$ (integer x): The integer val(x) whose radix-2^d digits are the coefficients x_j.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $x$ (input vector): The input vector of q complex numbers, indexed from 0 to q-1.
5. $x$
   - on `radix-digit-convolution`: $x$ (integer x): The integer val(x) whose radix-2^d digits are the coefficients x_j.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $x$ (first input): The first binary string input, of length n.
6. $y$
   - on `radix-digit-convolution`: $y$ (integer y): The integer val(y) whose radix-2^d digits are the coefficients y_j.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $y$ (second input): The second binary string input, of length n.
7. $j$
   - on `radix-digit-convolution`: $j$ (digit index): The index of a digit, ranging over 0 to L-1 on this page.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $j$ (input index): The index of an input entry, ranging over 0 to q-1.
8. $j$
   - on `radix-digit-convolution`: $j$ (digit index): The index of a digit, ranging over 0 to L-1 on this page.
   - on [Cyclic convolution](cyclic-convolution.md): $j$ (index into b): The index of an entry of b, ranging over 0 to t-1.
9. $i$
   - on `radix-digit-convolution`: $i$ (digit index i): A digit index used in the convolution sum for the coefficients e_j.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $i$ (second input index): A second index of an input entry, used when the sums are exchanged.
10. $i$
   - on `radix-digit-convolution`: $i$ (digit index i): A digit index used in the convolution sum for the coefficients e_j.
   - on [Cyclic convolution](cyclic-convolution.md): $i$ (index into a): The index of an entry of a, ranging over 0 to t-1.
11. $y$
   - on `polynomial-ring-mod-yr-plus-1`: $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $y$ (ring variable): The variable of the polynomial ring in which y^r is identified with -1.
12. $p$
   - on `polynomial-ring-mod-yr-plus-1`: $p$ (power exponent): A non-negative integer exponent of a power y^p of the indeterminate.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $p$ (input records): The vector of q records that a transform takes as input.
13. $p$
   - on `polynomial-ring-convolution`: $p$ (index offset): The offset $i+j-k$ of a pair of indices $(i,j)$ from the target index $k$.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $p$ (input records): The vector of q records that a transform takes as input.
14. $p$
   - on `polynomial-ring-convolution`: $p$ (index offset): The offset $i+j-k$ of a pair of indices $(i,j)$ from the target index $k$.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $p$ (power exponent): A non-negative integer exponent of a power y^p of the indeterminate.
15. $p$
   - on `guard-width-bound`: $p$ (input fractional bits): The number of fractional bits in each input coefficient, a count.
   - on [Subspace labels](subspace-labels.md): $p$ (first vector): A vector of F, the first argument of the bilinear form.
16. $L$
   - on `packed-bit-addition`: $L$ (chunk width): The number of bits in each address chunk, a count equal to mu times K.
   - on [Subspace labels](subspace-labels.md): $L$ (smaller label): A nondegenerate subspace of F attached to a wire; on an edge, the label contained in the other.
17. $M$
   - on `packed-bit-addition`: $M$ (record count): The number of records, a count.
   - on [Subspace labels](subspace-labels.md): $M$ (larger label): On an edge, the label that contains the smaller label L.
18. $t$
   - on `prime-source-lengths`: $t$ (padded axis length): The padded axis length of an axis: a power of two, the axis length of the padded box.
   - on [Cyclic convolution](cyclic-convolution.md): $t$ (sequence length): The number of entries in each of the two sequences, a positive integer.

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

Write the answer to `exegenius/tasks/0168-overloads.answer.json`, then run `exegenius submit 0168-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
