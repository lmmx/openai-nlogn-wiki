# exegenius task 0041-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the page that changes should do: use another letter, or say where the letter is used that it means something else there than on the other page. For the same thing, `note` may be empty.
- `change` is the page that changes. Leave it out for the later page. Give the earlier page's id when its use of the letter is the odd one out, for instance when the sources use the letter as the later page does, and the earlier page binds it on the page, not in a name. A page that other pages take the letter from keeps it and says where its meaning changes.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $z$
   - on `radix-digit-convolution`: $z$ (indeterminate): A formal symbol that is not a number, the variable of the polynomials U, V and W.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $z$ (integer to represent): A nonnegative integer less than $2^k$, whose binary representation is padded to length $k$.
2. $q$
   - on `discrete-fourier-transform`: $q$ (entry count): The number of complex entries in each input and output vector.
   - on [Cyclic convolution](cyclic-convolution.md): $q$ (sequence length): The number of entries in each of the two sequences a and b, and the modulus of the wrap-around.
3. $a$
   - on `discrete-fourier-transform`: $a$ (first vector): The first vector of the convolution, of length $q$.
   - on [Cyclic convolution](cyclic-convolution.md): $a$ (first sequence): The first of the two sequences of length q being convolved, with entries a_0 through a_{q-1}.
4. $b$
   - on `discrete-fourier-transform`: $b$ (second vector): The second vector of the convolution, of length $q$.
   - on [Cyclic convolution](cyclic-convolution.md): $b$ (second sequence): The second of the two sequences of length q being convolved, with entries b_0 through b_{q-1}.
5. $t$
   - on `discrete-fourier-transform`: $t$ (shifted index): The index $(l-k)\bmod q$ for fixed $k$, running over $0,\dots,q-1$.
   - on [Cyclic convolution](cyclic-convolution.md): $t$ (output index): The index of an output entry of the cyclic convolution, running from 0 to q-1.
6. $s$
   - on `gaussian-resampling`: $s$ (source length): The number of entries in each source vector, the length of the source vectors.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $s$ (binary string): A generic binary string whose integer value is taken by the function val.
7. $t$
   - on `gaussian-resampling`: $t$ (target length): The number of entries in each target vector, the length of the target vectors.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $t$ (shifted index): The index $(l-k)\bmod q$ for fixed $k$, running over $0,\dots,q-1$.
8. $t$
   - on `gaussian-resampling`: $t$ (target length): The number of entries in each target vector, the length of the target vectors.
   - on [Cyclic convolution](cyclic-convolution.md): $t$ (output index): The index of an output entry of the cyclic convolution, running from 0 to q-1.
9. $u$
   - on `gaussian-resampling`: $u$ (source vector): A length-s vector, the input of the maps S, T and N.
   - on [Radix-digit convolution](radix-digit-convolution.md): $u$ (first integer): The integer whose i-th digit is u_i.
10. $b$
   - on `gaussian-resampling`: $b$ (target vector): A length-t vector, the input of the maps C and P_t.
   - on [Radix-digit convolution](radix-digit-convolution.md): $b$ (digit bit count): The number of bits in one radix digit.
11. $b$
   - on `gaussian-resampling`: $b$ (target vector): A length-t vector, the input of the maps C and P_t.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $b$ (second vector): The second vector of the convolution, of length $q$.
12. $b$
   - on `gaussian-resampling`: $b$ (target vector): A length-t vector, the input of the maps C and P_t.
   - on [Cyclic convolution](cyclic-convolution.md): $b$ (second sequence): The second of the two sequences of length q being convolved, with entries b_0 through b_{q-1}.
13. $j$
   - on `gaussian-resampling`: $j$ (source entry index): The index of an entry of a source vector, which is read modulo s.
   - on [Radix-digit convolution](radix-digit-convolution.md): $j$ (coefficient index): The index of a coefficient of W.
14. $j$
   - on `gaussian-resampling`: $j$ (source entry index): The index of an entry of a source vector, which is read modulo s.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $j$ (output index): The index of an output entry, running from $0$ to $q-1$.
15. $k$
   - on `gaussian-resampling`: $k$ (target entry index): The index of an entry of a target vector.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $k$ (padded output length): The number of bits in a padded binary output, that is, the length to which a binary representation is padded.
16. $k$
   - on `gaussian-resampling`: $k$ (target entry index): The index of an entry of a target vector.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $k$ (input index): The index of an input entry, running from $0$ to $q-1$.
17. $i$
   - on `gaussian-resampling`: $i$ (summation index): The summation index running over all integers in the expansion of $(Nu)_j$.
   - on [Radix-digit convolution](radix-digit-convolution.md): $i$ (digit index): An index of the digits of u and v, running from 0 to m-1.
18. $M$
   - on `gaussian-resampling`: $M$ (last partial-sum index): The last index of a partial sum of the Neumann series.
   - on [Operator norm](operator-norm.md): $M$ (second linear map): Another linear map, composed with L in the product LM.
19. $A$
   - on `transform-identity`: $A$ (first contraction): The linear contraction from length-$s$ to length-$t$ vectors, equal to $S'$ on this page.
   - on [Gaussian resampling](gaussian-resampling.md): $A$ (source contraction map): The map A=S from length-s to length-t vectors in the factored identity.
20. $v$
   - on `transform-identity`: $v$ (generic length-t vector): A generic vector of $t$ coordinates, the input of the permutation $P_t$.
   - on [Radix-digit convolution](radix-digit-convolution.md): $v$ (second integer): The integer whose i-th digit is v_i.
21. $S'$
   - on `transform-identity`: $S'$ (scaled gathering map): The map $S/2$, the gathering map $S$ scaled by one half.
   - on [Operator norm](operator-norm.md): $S'$ (scaled Gaussian map): Half of a Gaussian resampling map, used as the map A.
22. $J'$
   - on `transform-identity`: $J'$ (scaled inverse): The map $N^{-1}/2$, the inverse of $N$ scaled by one half.
   - on [Operator norm](operator-norm.md): $J'$ (scaled inverse map): Half the inverse of an invertible map close to the identity.

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

Write the answer to `exegenius/tasks/0041-overloads.answer.json`, then run `exegenius submit 0041-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
