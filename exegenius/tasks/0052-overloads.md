# exegenius task 0052-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the later page should do: use another letter, or say where the letter is used that it means something else here than on the earlier page. For the same thing, `note` may be empty.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $m$
   - on `discrete-fourier-transform`: $m$ (exponent): An integer exponent of omega, ranging over the values with $0<m<q$ in the primitivity condition.
   - on [Linear map](linear-map.md): $m$ (input count): The number of input coordinates of $L$.
2. $L$
   - on `tensor-product`: $L$ (first map): A linear map on vectors of length $s$.
   - on [Linear map](linear-map.md): $L$ (linear map): The rule that takes an input vector $u$ of $m$ complex numbers and returns an output vector $v$ of $k$ complex numbers.
3. $u$
   - on `tensor-product`: $u$ (array): An array with $s$ rows and $t$ columns, whose entries are $u_{hg}$.
   - on [Linear map](linear-map.md): $u$ (input vector): The vector of $m$ complex numbers that the linear map $L$ takes as input.
4. $m$
   - on `tensor-product`: $m$ (output column index): The index of an output column, which is the second coordinate of an output position.
   - on [Linear map](linear-map.md): $m$ (input count): The number of input coordinates of $L$.
5. $a$
   - on `radix-digit-convolution`: $a$ (digit list of x): The list of radix digits of the first input x, indexed from $a_0$ to $a_{d-1}$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $a$ (input vector): A vector of $q$ complex numbers, written $(a_0,\dots,a_{q-1})$, that the transform acts on.
6. $e$
   - on `radix-digit-convolution`: $e$ (digit position): The position of a digit in the digit list of an input, running from $0$ to $d-1$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $e$ (integer exponent): An integer exponent of omega in the full-period sum.
7. $z$
   - on `radix-digit-convolution`: $z$ (formal variable): A placeholder for the powers of a polynomial.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $z$ (integer to encode): A nonnegative integer below 2^k that is written in binary.
8. $b$
   - on `radix-digit-convolution`: $b$ (digit list of y): The list of radix digits of the second input y, indexed like $a$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $b$ (second vector): A second vector of $q$ complex numbers, used with $a$ in the convolution.
9. $c$
   - on `radix-digit-convolution`: $c$ (convolution): The list of coefficients of the product $a(z)b(z)$, which is the convolution of $a$ and $b$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $c$ (pointwise product): The entrywise product of the transforms of $a$ and $b$.
10. $p$
   - on `radix-digit-convolution`: $p$ (coefficient index): The index of a coefficient of $c$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $p$ (output position): An output position of a transformed vector, running from $0$ to $q-1$.
11. $s$
   - on `gaussian-resampling`: $s$ (source length): The number of coordinates of the source vector, the length of the transform on the source grid.
   - on [Gaussian function](gaussian-function.md): $s$ (input length): The number of input values in each vector that the weighted map takes.
12. $s$
   - on `gaussian-resampling`: $s$ (source length): The number of coordinates of the source vector, the length of the transform on the source grid.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $s$ (frequency index): The summation index over frequencies, running from $0$ to $q-1$.
13. $t$
   - on `gaussian-resampling`: $t$ (target length): The number of coordinates of the target vector, the length of the transform on the target grid.
   - on [Gaussian function](gaussian-function.md): $t$ (output length): The number of output values, indexed from 0 to t-1, that the weighted map returns.
14. $\theta$
   - on `gaussian-resampling`: $\theta$ (relative excess): The ratio t/s minus one, measuring how much longer the target is than the source.
   - on [Gaussian function](gaussian-function.md): $\theta$ (length gap): The relative gap t/s - 1 between the two lengths.
15. $\alpha$
   - on `gaussian-resampling`: $\alpha$ (Gaussian width): An integer, at least 2, that sets the width parameter of the Gaussian weights.
   - on [Gaussian function](gaussian-function.md): $\alpha$ (width parameter): An integer, at least 2, that sets how wide the Gaussian bell is.
16. $p$
   - on `gaussian-resampling`: $p$ (precision): The integer precision of the numerical approximation, which bounds how large theta must be.
   - on [Radix-digit convolution](radix-digit-convolution.md): $p$ (coefficient index): The index of a coefficient of $c$.
17. $p$
   - on `gaussian-resampling`: $p$ (precision): The integer precision of the numerical approximation, which bounds how large theta must be.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $p$ (output position): An output position of a transformed vector, running from $0$ to $q-1$.
18. $S$
   - on `gaussian-resampling`: $S$ (source-to-target Gaussian map): The Gaussian map sending length-s vectors to length-t vectors, with entries (Su)_k given by a Gaussian-weighted sum over j.
   - on [Gaussian function](gaussian-function.md): $S$ (Gaussian map): The linear map from vectors of s values to vectors of t values whose weights are Gaussians.
19. $T$
   - on `gaussian-resampling`: $T$ (target-to-source Gaussian map): The Gaussian map sending length-s vectors to length-t vectors, with entries (Tu)_k given by a second Gaussian-weighted sum over j.
   - on [Gaussian function](gaussian-function.md): $T$ (second Gaussian map): The second Gaussian-weighted map, built like S with the roles of the two grids exchanged.
20. $A$
   - on `gaussian-resampling`: $A$ (source-to-target contraction): The contraction S/2, mapping length-s vectors to length-t vectors.
   - on [Operator norm](operator-norm.md): $A$ (contraction A): A linear map that is a contraction, used as a factor on the Gaussian resampling page.
21. $B_0$
   - on `gaussian-resampling`: $B_0$ (target-to-source contraction): The contraction D' N^{-1} C / 2, mapping length-t vectors back to length-s vectors.
   - on [Operator norm](operator-norm.md): $B_0$ (contraction B_0): A linear map that is a contraction, used as a factor on the Gaussian resampling page.
22. $F_s$
   - on `transform-identity`: $F_s$ (source transform): The normalized transform $F_q$ with $q=s$, acting on vectors of $s$ coordinates.
   - on [Convolution theorem](convolution-theorem.md): $F_s$ (normalized transform): The discrete Fourier transform applied along every axis of the array, normalized by 1/S.
23. $d$
   - on `transform-identity`: $d$ (coordinate count): The number of coordinates of the grid, a count.
   - on [Convolution theorem](convolution-theorem.md): $d$ (number of axes): The number of axes of an array, which counts its dimensions.
24. $d$
   - on `transform-identity`: $d$ (coordinate count): The number of coordinates of the grid, a count.
   - on [Radix-digit convolution](radix-digit-convolution.md): $d$ (digit count): The number of radix digits of each input.
25. $s_i$
   - on `transform-identity`: $s_i$ (source axis length): The number of entries along coordinate $i$ of the source grid, a count.
   - on [Convolution theorem](convolution-theorem.md): $s_i$ (axis length): The length of axis i of the array, which counts the positions along that axis.
26. $A$
   - on `transform-identity`: $A$ (source-to-target contraction): The tensor product of the one-dimensional contractions $A$, mapping source arrays to target arrays.
   - on [Operator norm](operator-norm.md): $A$ (contraction A): A linear map that is a contraction, used as a factor on the Gaussian resampling page.
27. $B_0$
   - on `transform-identity`: $B_0$ (target-to-source contraction): The tensor product of the one-dimensional contractions $B_0$, mapping target arrays to source arrays.
   - on [Operator norm](operator-norm.md): $B_0$ (contraction B_0): A linear map that is a contraction, used as a factor on the Gaussian resampling page.
28. $u$
   - on `transform-identity`: $u$ (source array): An array on the source grid of shape $s_1\times\cdots\times s_d$.
   - on [Linear map](linear-map.md): $u$ (input vector): The vector of $m$ complex numbers that the linear map $L$ takes as input.
29. $u$
   - on `transform-identity`: $u$ (source array): An array on the source grid of shape $s_1\times\cdots\times s_d$.
   - on [Tensor product](tensor-product.md): $u$ (array): An array with $s$ rows and $t$ columns, whose entries are $u_{hg}$.
30. $v$
   - on `transform-identity`: $v$ (second source array): A second array on the source grid of shape $s_1\times\cdots\times s_d$.
   - on [Linear map](linear-map.md): $v$ (output vector): The vector of $k$ complex numbers that the linear map $L$ returns.

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

Write the answer to `exegenius/tasks/0052-overloads.answer.json`, then run `exegenius submit 0052-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
