# exegenius task 0215-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the page that changes should do: use another letter, or say where the letter is used that it means something else there than on the other page. For the same thing, `note` may be empty.
- `change` is the page that changes. Leave it out for the later page. Give the earlier page's id when its use of the letter is the odd one out, for instance when the sources use the letter as the later page does, and the earlier page binds it on the page, not in a name. A page that other pages take the letter from keeps it and says where its meaning changes.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $x$
   - on `frame`: $x$ (route vertex): The l-th vertex x_l of a route, running from the source x_0 to the sink x_r.
   - on [Linear network](linear-network.md): $x$ (first bank value): The value of the first bank, held on one wire.
2. $m$
   - on `subspace-labels`: $m$ (label dimension): The dimension of the common space $E$, a count of the basis vectors of $E$; on the dyadic page $m$ means an integer numerator instead.
   - on [Gaussian dyadic numbers](gaussian-dyadic.md): $m$ (integer numerator): The integer numerator of a dyadic rational written as $m/2^k$.
3. $s$
   - on `recursive-saving`: $s$ (smaller call count): The total number of smaller calls, summed over all edges of the network.
   - on [Nested subspace labels](subspace-labels.md): $s$ (smaller-call total): The total number of smaller calls, the sum of the drops over all edges; the letter changes meaning here and is not the route length of the frame page.
4. $u$
   - on `tape-interchange`: $u$ (field width): The number of bits in each of the two address fields H and D.
   - on [Gaussian dyadic numbers](gaussian-dyadic.md): $u$ (first input value): The first value of an input pair to the butterfly map $H_0$.
5. $u$
   - on `tape-interchange`: $u$ (field width): The number of bits in each of the two address fields H and D.
   - on [Frame of a vertex](frame.md): $u$ (tail vertex): A vertex of the network, the start of an edge from u to v.
6. $V$
   - on `tape-interchange`: $V$ (stored volume): The number of data units in the array being permuted.
   - on [Role streams from a cyclic row split](role-streams.md): $V$ (node volume): The number of bits the node holds once its rows are padded.
7. $\tau$
   - on `tape-interchange`: $\tau$ (saving exponent): A fixed exponent below 1 that sets the saving in the cost per unit of width.
   - on [Nested subspace labels](subspace-labels.md): $\tau$ (head vertex): The vertex at which an edge ends.
8. $b$
   - on `radix-digit-convolution`: $b$ (exact-recovery digit width): The same digit width as $\beta$ on this page, the number of bits in each radix digit.
   - on [Cyclic convolution](cyclic-convolution.md): $b$ (second coefficient list): The second input list, whose j-th coefficient is b_j.
9. $j$
   - on `fourier-transform`: $j$ (input index): The position of an entry of u, running from 0 to q-1 in the transform sum.
   - on [Cyclic convolution](cyclic-convolution.md): $j$ (second index): An index into the second list, running over 0 to S-1.
10. $q$
   - on `tensor-product`: $q$ (basis size of F): The number of basis vectors of F, which counts the vectors f_1 through f_q.
   - on [Discrete Fourier transform](fourier-transform.md): $q$ (vector length): The number of entries of u, which is the length of every vector in the transform.
11. $i$
   - on `tensor-product`: $i$ (basis index of E): An index of the basis vectors e_i of E, running from 1 to p.
   - on [Cyclic convolution](cyclic-convolution.md): $i$ (first index): An index into the first list, running over 0 to S-1.
12. $j$
   - on `tensor-product`: $j$ (basis index of F): An index of the basis vectors f_j of F, running from 1 to q.
   - on [Discrete Fourier transform](fourier-transform.md): $j$ (input index): The position of an entry of u, running from 0 to q-1 in the transform sum.
13. $j$
   - on `tensor-product`: $j$ (basis index of F): An index of the basis vectors f_j of F, running from 1 to q.
   - on [Cyclic convolution](cyclic-convolution.md): $j$ (second index): An index into the second list, running over 0 to S-1.
14. $A$
   - on `multidim-transform`: $A$ (input array): The array whose entries A_{j_1…j_d} are the input to the transform.
   - on [Tensor product](tensor-product.md): $A$ (linear map on E): A linear map of the space E, one factor of the tensor product of maps.
15. $i$
   - on `polynomial-ring`: $i$ (coefficient index): The index of a coefficient, running from 0 to r-1.
   - on [Cyclic convolution](cyclic-convolution.md): $i$ (first index): An index into the first list, running over 0 to S-1.
16. $M$
   - on `signed-packing`: $M$ (coefficient count): The number of coefficients of $P$, which counts its slots in the packed integer.
   - on [Simultaneous butterfly layer H₀](butterfly-layer.md): $M$ (record length): The number of complex coefficients in each polynomial record stored at an address.
17. $\sigma$
   - on `signed-packing`: $\sigma$ (slot width): The number of bits each slot holds, so each coefficient occupies a slot of this many bits.
   - on [Synthetic polynomial transform](synthetic-transform.md): $\sigma$ (twiddle exponent): The exponent of a twiddle factor $y^\sigma$, an integer from 0 to 2r-1 that counts the places a coefficient moves.
18. $t$
   - on `gaussian-resampling`: $t$ (target length): The length of the longer target transform, a count of its coordinates, with s < t.
   - on [Discrete Fourier transform](fourier-transform.md): $t$ (second summation index): The position of an entry of b, running from 0 to q-1 in the convolution sum.
19. $p$
   - on `gaussian-resampling`: $p$ (integer precision): The integer precision in the hypotheses of the identity, a count of bits.
   - on [Tensor product](tensor-product.md): $p$ (basis size of E): The number of basis vectors of E, which counts the vectors e_1 through e_p.
20. $A$
   - on `gaussian-resampling`: $A$ (first contraction): Half of K, one of the two contractions in the rewriting.
   - on [Multidimensional transform with power-of-two axes](multidim-transform.md): $A$ (input array): The array whose entries A_{j_1…j_d} are the input to the transform.
21. $A$
   - on `gaussian-resampling`: $A$ (first contraction): Half of K, one of the two contractions in the rewriting.
   - on [Tensor product](tensor-product.md): $A$ (linear map on E): A linear map of the space E, one factor of the tensor product of maps.
22. $B$
   - on `gaussian-resampling`: $B$ (second contraction): The scaled map 2 to the power 1 minus 2 sigma squared times Delta Gamma inverse Lambda, the second contraction.
   - on [Multidimensional transform with power-of-two axes](multidim-transform.md): $B$ (transformed array): The array whose entries B_{k_1…k_d} are the output of the transform.
23. $p$
   - on `bluestein`: $p$ (chirp index): An integer index at which the chirp and the phase twist are evaluated.
   - on [Gaussian resampling](gaussian-resampling.md): $p$ (integer precision): The integer precision in the hypotheses of the identity, a count of bits.
24. $p$
   - on `bluestein`: $p$ (chirp index): An integer index at which the chirp and the phase twist are evaluated.
   - on [Tensor product](tensor-product.md): $p$ (basis size of E): The number of basis vectors of E, which counts the vectors e_1 through e_p.
25. $\lambda$
   - on `crt-axis-map`: $\lambda$ (coefficient index): The position of a coefficient in the list, running from 0 to S-1.
   - on [Quotient ring by several relations](quotient-ring.md): $\lambda$ (multiplier): The polynomial multiplier of the i-th relation in a sum that belongs to the ideal.

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

Write the answer to `exegenius/tasks/0215-overloads.answer.json`, then run `exegenius submit 0215-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
