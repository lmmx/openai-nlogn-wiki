# exegenius task 0135-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the later page should do: use another letter, or say where the letter is used that it means something else here than on the earlier page. For the same thing, `note` may be empty.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $u$
   - on `address-interchange`: $u$ (field width): The number of bits in each address field.
   - on [Fixed-tape machine model](fixed-tape-model.md): $u$ (field size): The number of cells in each of two disjoint fields, which counts the cells of a field.
2. $U$
   - on `subspace-labels`: $U$ (label): A nondegenerate subspace of F, the label attached to a wire.
   - on [Bilinear form](bilinear-form.md): $U$ (ambient vector space): The vector space over F2 on which the bilinear form is defined.
3. $W$
   - on `subset-intersection-network`: $W$ (volume shrink factor): The factor by which the stream volume shrinks, so each smaller call works on a stream of 1/W of the volume.
   - on [Bilinear form](bilinear-form.md): $W$ (subspace): A subspace of U whose restricted form is tested for nondegeneracy.
4. $a$
   - on `complex-phase-network`: $a$ (kernel scalar a): The coefficient of the identity in a two-point kernel $aI+bX$.
   - on [Gaussian dyadics](gaussian-dyadics.md): $a$ (real numerator part): The integer real part of the numerator $a + bi$ of a Gaussian dyadic.
5. $b$
   - on `complex-phase-network`: $b$ (kernel scalar b): The coefficient of the swap in a two-point kernel $aI+bX$.
   - on [Gaussian dyadics](gaussian-dyadics.md): $b$ (imaginary numerator part): The integer imaginary part of the numerator $a + bi$ of a Gaussian dyadic.
6. $j$
   - on `discrete-fourier-transform`: $j$ (input index): The index of an input entry, ranging over 0 to q-1.
   - on [Cyclic convolution](cyclic-convolution.md): $j$ (index into b): The index of an entry of b, ranging over 0 to t-1.
7. $k$
   - on `discrete-fourier-transform`: $k$ (output index): The index of an output entry, ranging over 0 to q-1.
   - on [Cyclic convolution](cyclic-convolution.md): $k$ (index into c): The index of an entry of the output sequence c, ranging over 0 to t-1.
8. $i$
   - on `discrete-fourier-transform`: $i$ (second input index): A second index of an input entry, used when the sums are exchanged.
   - on [Cyclic convolution](cyclic-convolution.md): $i$ (index into a): The index of an entry of a, ranging over 0 to t-1.
9. $t$
   - on `radix-digit-convolution`: $t$ (indeterminate): The indeterminate of the digit polynomials P(t) and Q(t).
   - on [Cyclic convolution](cyclic-convolution.md): $t$ (sequence length): The number of entries in each of the two sequences, a positive integer.
10. $a$
   - on `synthetic-transforms`: $a$ (input records): The input vector of q records a_0 through a_{q-1}; the letter changes meaning from the cyclic convolution page.
   - on [Cyclic convolution](cyclic-convolution.md): $a$ (first input sequence): The first sequence of t complex numbers, indexed from 0 to t-1.
11. $y$
   - on `polynomial-ring-mod-yr-plus-1`: $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $y$ (ring variable): The variable of the ring C[y]/(y^r+1), where y^r equals -1; the letter changes meaning from the multiplication page's second input.
12. $k$
   - on `polynomial-ring-mod-yr-plus-1`: $k$ (power exponent): The exponent of a power y^k, a non-negative integer.
   - on [Cyclic convolution](cyclic-convolution.md): $k$ (index into c): The index of an entry of the output sequence c, ranging over 0 to t-1.
13. $k$
   - on `polynomial-ring-mod-yr-plus-1`: $k$ (power exponent): The exponent of a power y^k, a non-negative integer.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $k$ (output index): The index of an output entry, ranging over 0 to q-1.
14. $d$
   - on `chinese-remainder-map`: $d$ (number of axes): The number of cyclic axes, a count of the lengths m_i.
   - on [Radix-digit convolution](radix-digit-convolution.md): $d$ (digit width): The number of bits in each radix-2^d digit.
15. $x$
   - on `chinese-remainder-map`: $x$ (position): A coefficient position, an integer from 0 to N-1.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $x$ (input vector): The input vector of q complex numbers, indexed from 0 to q-1.
16. $x$
   - on `chinese-remainder-map`: $x$ (position): A coefficient position, an integer from 0 to N-1.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $x$ (first input): The first binary string input, of length n.
17. $z$
   - on `chinese-remainder-map`: $z$ (target position): The position of the convolution output whose sum is being formed.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $z$ (integer to encode): A nonnegative integer less than 2^{2n} whose binary representation is taken.
18. $t$
   - on `bluestein-chirp-identity`: $t$ (reduced index): The index $(k-j) \bmod q$ in $\{0,\ldots,q-1\}$ at which the chirp sequence $b$ is evaluated.
   - on [Cyclic convolution](cyclic-convolution.md): $t$ (sequence length): The number of entries in each of the two sequences, a positive integer.
19. $F$
   - on `polynomial-ring-convolution`: $F$ (forward transform): The forward synthetic transform, whose entry m is the sum of a_j omega^{jm} over the input records.
   - on [Signed coefficient packing](signed-packing.md): $F$ (packed integer of f): The integer $f(2^w)$ obtained by packing the coefficients of $f$ into blocks of width $w$.
20. $G$
   - on `polynomial-ring-convolution`: $G$ (opposite transform): The opposite transform, which uses the inverse root omega^{-1} in place of omega and divides by N.
   - on [Signed coefficient packing](signed-packing.md): $G$ (packed integer of g): The integer $g(2^w)$ obtained by packing the coefficients of $g$ into blocks of width $w$.
21. $u$
   - on `simultaneous-butterfly-layer`: $u$ (first input): The first value of the pair that the two-point map takes as input.
   - on [Bilinear form](bilinear-form.md): $u$ (first vector): A vector of U, the first argument of the form.
22. $u$
   - on `simultaneous-butterfly-layer`: $u$ (first input): The first value of the pair that the two-point map takes as input.
   - on [Address-field interchange](address-interchange.md): $u$ (field width): The number of bits in each address field.
23. $u$
   - on `simultaneous-butterfly-layer`: $u$ (first input): The first value of the pair that the two-point map takes as input.
   - on [Fixed-tape machine model](fixed-tape-model.md): $u$ (field size): The number of cells in each of two disjoint fields, which counts the cells of a field.
24. $u$
   - on `simultaneous-butterfly-layer`: $u$ (first input): The first value of the pair that the two-point map takes as input.
   - on [Gaussian dyadics](gaussian-dyadics.md): $u$ (first coefficient): The first coefficient of a pair on which the two-point map $H_0$ acts.
25. $v$
   - on `simultaneous-butterfly-layer`: $v$ (second input): The second value of the pair that the two-point map takes as input.
   - on [Bilinear form](bilinear-form.md): $v$ (second vector): A vector of U, the second argument of the form.
26. $v$
   - on `simultaneous-butterfly-layer`: $v$ (second input): The second value of the pair that the two-point map takes as input.
   - on [Gaussian dyadics](gaussian-dyadics.md): $v$ (second coefficient): The second coefficient of a pair on which the two-point map $H_0$ acts.
27. $u$
   - on `guard-width-bound`: $u$ (first example input): The first of two input coefficients in the worked example, with depth 0.
   - on [Gaussian dyadics](gaussian-dyadics.md): $u$ (first coefficient): The first coefficient of a pair on which the two-point map $H_0$ acts.
28. $u$
   - on `guard-width-bound`: $u$ (first example input): The first of two input coefficients in the worked example, with depth 0.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $u$ (first input): The first value of the pair that the two-point map takes as input.
29. $u$
   - on `guard-width-bound`: $u$ (first example input): The first of two input coefficients in the worked example, with depth 0.
   - on [Bilinear form](bilinear-form.md): $u$ (first vector): A vector of U, the first argument of the form.
30. $u$
   - on `guard-width-bound`: $u$ (first example input): The first of two input coefficients in the worked example, with depth 0.
   - on [Address-field interchange](address-interchange.md): $u$ (field width): The number of bits in each address field.
31. $u$
   - on `guard-width-bound`: $u$ (first example input): The first of two input coefficients in the worked example, with depth 0.
   - on [Fixed-tape machine model](fixed-tape-model.md): $u$ (field size): The number of cells in each of two disjoint fields, which counts the cells of a field.
32. $v$
   - on `guard-width-bound`: $v$ (second example input): The second of two input coefficients in the worked example, with depth 0.
   - on [Gaussian dyadics](gaussian-dyadics.md): $v$ (second coefficient): The second coefficient of a pair on which the two-point map $H_0$ acts.
33. $v$
   - on `guard-width-bound`: $v$ (second example input): The second of two input coefficients in the worked example, with depth 0.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $v$ (second input): The second value of the pair that the two-point map takes as input.
34. $v$
   - on `guard-width-bound`: $v$ (second example input): The second of two input coefficients in the worked example, with depth 0.
   - on [Bilinear form](bilinear-form.md): $v$ (second vector): A vector of U, the second argument of the form.
35. $k$
   - on `recovery-and-error`: $k$ (coefficient index): The index of a coefficient of the convolution.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $k$ (power exponent): The exponent of a power y^k, a non-negative integer.
36. $k$
   - on `recovery-and-error`: $k$ (coefficient index): The index of a coefficient of the convolution.
   - on [Cyclic convolution](cyclic-convolution.md): $k$ (index into c): The index of an entry of the output sequence c, ranging over 0 to t-1.
37. $k$
   - on `recovery-and-error`: $k$ (coefficient index): The index of a coefficient of the convolution.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $k$ (output index): The index of an output entry, ranging over 0 to q-1.
38. $k$
   - on `recovery-and-error`: $k$ (coefficient index): The index of a coefficient of the convolution.
   - on [Gaussian dyadics](gaussian-dyadics.md): $k$ (denominator exponent): The non-negative integer exponent that sets the common denominator $2^k$.
39. $x$
   - on `packed-bit-addition`: $x$ (source chunk): The first address chunk, whose selected bits are XORed into the chunk y.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $x$ (input vector): The input vector of q complex numbers, indexed from 0 to q-1.
40. $x$
   - on `packed-bit-addition`: $x$ (source chunk): The first address chunk, whose selected bits are XORed into the chunk y.
   - on [Subspace labels](subspace-labels.md): $x$ (first argument): A vector of F, the first argument of the bilinear form.
41. $y$
   - on `packed-bit-addition`: $y$ (target chunk): The second address chunk, whose selected bits are replaced by their XOR with the bits of x.
   - on [Subspace labels](subspace-labels.md): $y$ (second argument): A vector of F, the second argument of the bilinear form.
42. $z$
   - on `packed-bit-addition`: $z$ (temporary chunk): The third address chunk, which supplies temporary bits and is restored unchanged.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $z$ (example values): The stored values in the $D=2$ example, indexed by the two selected bits.
43. $f$
   - on `packed-bit-addition`: $f$ (selected count): The number of selected positions in each chunk.
   - on [Tensor product](tensor-product.md): $f$ (basis vector of Q): A basis vector of the second factor Q, paired with a basis vector e of P to form a basis vector of the tensor product.
44. $i$
   - on `packed-bit-addition`: $i$ (selected index): An index from 0 to f minus 1 counting the selected positions.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $i$ (second input index): A second index of an input entry, used when the sums are exchanged.
45. $i$
   - on `packed-bit-addition`: $i$ (selected index): An index from 0 to f minus 1 counting the selected positions.
   - on [Cyclic convolution](cyclic-convolution.md): $i$ (index into a): The index of an entry of a, ranging over 0 to t-1.
46. $i$
   - on `packed-bit-addition`: $i$ (selected index): An index from 0 to f minus 1 counting the selected positions.
   - on [Complex phase network](complex-phase-network.md): $i$ (imaginary unit): The imaginary unit, with i squared equal to -1.
47. $R$
   - on `packed-bit-addition`: $R$ (record bit count): The number of bits in each record.
   - on [Subspace labels](subspace-labels.md): $R$ (orthogonal residual): The orthogonal residual of an edge, the orthogonal complement of the smaller label inside the larger one.
48. $B$
   - on `packed-bit-addition`: $B$ (exceptional set): The set of addresses where S_0 may disagree with the exact map T_0.
   - on [Bilinear form](bilinear-form.md): $B$ (bilinear form): The function that takes two vectors of U and returns a scalar, linear in each argument.
49. $i$
   - on `prime-source-lengths`: $i$ (axis index): The index of an axis, so that $s_i$ and $t_i$ belong to the same axis.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $i$ (second input index): A second index of an input entry, used when the sums are exchanged.
50. $i$
   - on `prime-source-lengths`: $i$ (axis index): The index of an axis, so that $s_i$ and $t_i$ belong to the same axis.
   - on [Cyclic convolution](cyclic-convolution.md): $i$ (index into a): The index of an entry of a, ranging over 0 to t-1.

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

Write the answer to `exegenius/tasks/0135-overloads.answer.json`, then run `exegenius submit 0135-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
