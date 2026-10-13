# exegenius task 0183-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the page that changes should do: use another letter, or say where the letter is used that it means something else there than on the other page. For the same thing, `note` may be empty.
- `change` is the page that changes. Leave it out for the later page. Give the earlier page's id when its use of the letter is the odd one out, for instance when the sources use the letter as the later page does, and the earlier page binds it on the page, not in a name. A page that other pages take the letter from keeps it and says where its meaning changes.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $n$
   - on `schonhage-strassen-conjecture`: $n$ (input length): The number of bits in each of the two integers being multiplied, which is the length the worst-case time is measured against.
   - on [Fixed-tape machine model](fixed-tape-model.md): $n$ (input length in bits): The count of bits in each input of the machine, the length in bits of each input.
2. $\kappa$
   - on `schonhage-strassen-conjecture`: $\kappa$ (power-saving constant): A fixed constant greater than 0 that does not depend on $n$.
   - on [Fixed-tape machine model](fixed-tape-model.md): $\kappa$ (fixed exponent saving): A fixed constant equal to $2^{-182}$, the same for every input length $n$.
3. $m$
   - on `subspace-labels`: $m$ (space dimension): The dimension of the space E, which counts the basis vectors of E.
   - on [Gaussian dyadic numbers](gaussian-dyadic.md): $m$ (integer numerator): The integer numerator of a dyadic rational written as $m/2^k$.
4. $x$
   - on `subspace-labels`: $x$ (tail vertex): A vertex of the network, a gate or terminal; it is the tail of an edge from x to y.
   - on [Linear network](linear-network.md): $x$ (first bank value): The value of the first bank, held on one wire.
5. $y$
   - on `subspace-labels`: $y$ (head vertex): A vertex at the head of the edge from x, the vertex the edge enters.
   - on [Linear network](linear-network.md): $y$ (second bank value): The value of the second bank, held on one wire.
6. $s$
   - on `subspace-labels`: $s$ (smaller call count): The total number of smaller calls, which counts the smaller operations over all edges.
   - on [Frame of a vertex](frame.md): $s$ (route length): The number of edges in a route, so that the route has $s+1$ vertices.
7. $a$
   - on `recursive-saving`: $a$ (edge rank): The rank of one edge matrix, which is summed over all edges to give the total number of smaller calls.
   - on [Gaussian dyadic numbers](gaussian-dyadic.md): $a$ (real part): The real part of the Gaussian dyadic number $z$.
8. $s$
   - on `recursive-saving`: $s$ (smaller call count): The total number of smaller calls, counted as the sum of the edge ranks over all edges.
   - on [Frame of a vertex](frame.md): $s$ (route length): The number of edges in a route, so that the route has $s+1$ vertices.
9. $u$
   - on `tape-interchange`: $u$ (field width): The number of bits in each of the two address fields, their common width.
   - on [Gaussian dyadic numbers](gaussian-dyadic.md): $u$ (first input value): The first value of an input pair to the butterfly map $H_0$.
10. $u$
   - on `tape-interchange`: $u$ (field width): The number of bits in each of the two address fields, their common width.
   - on [Frame of a vertex](frame.md): $u$ (tail vertex): The vertex at which an edge starts, so that the frame change $D_vD_u^{-1}$ starts from its frame $D_u$.
11. $V$
   - on `tape-interchange`: $V$ (stored volume): The number of data units in the array, the stored volume.
   - on [Role streams from a cyclic row split](role-streams.md): $V$ (node volume): The number of bits the node holds once its rows are padded.
12. $m$
   - on `tape-interchange`: $m$ (matrix size): The number of rows of each rational matrix held at a vertex of the network, and the parameter of the recursion.
   - on [Nested subspace labels](subspace-labels.md): $m$ (space dimension): The dimension of the space E, which counts the basis vectors of E.
13. $m$
   - on `tape-interchange`: $m$ (matrix size): The number of rows of each rational matrix held at a vertex of the network, and the parameter of the recursion.
   - on [Gaussian dyadic numbers](gaussian-dyadic.md): $m$ (integer numerator): The integer numerator of a dyadic rational written as $m/2^k$.
14. $b$
   - on `radix-digit-convolution`: $b$ (digit width): The number of bits in each radix digit.
   - on [Cyclic convolution](cyclic-convolution.md): $b$ (second coefficient list): The second input list, whose j-th coefficient is b_j.
15. $j$
   - on `fourier-transform`: $j$ (input index): An index running over the entries of u, from 0 to q-1.
   - on [Cyclic convolution](cyclic-convolution.md): $j$ (second index): An index into the second list, running over 0 to S-1.
16. $a$
   - on `fourier-transform`: $a$ (first vector): A vector of length q, the first input of the convolution.
   - on [Cyclic convolution](cyclic-convolution.md): $a$ (first coefficient list): The first input list, whose i-th coefficient is a_i.
17. $b$
   - on `fourier-transform`: $b$ (second vector): A vector of length q, the second input of the convolution.
   - on [Cyclic convolution](cyclic-convolution.md): $b$ (second coefficient list): The second input list, whose j-th coefficient is b_j.
18. $c$
   - on `fourier-transform`: $c$ (cyclic product): The cyclic convolution of a and b, a vector of length q.
   - on [Cyclic convolution](cyclic-convolution.md): $c$ (cyclic convolution): The cyclic convolution of a and b, a list of S coefficients.
19. $q$
   - on `tensor-product`: $q$ (basis count of F): The number of basis vectors of $F$, its dimension.
   - on [Discrete Fourier transform](fourier-transform.md): $q$ (transform length): The number of entries of u, which is the length of the transform.
20. $i$
   - on `tensor-product`: $i$ (basis index of E): The index of a basis vector $e_i$, running from $1$ to $p$.
   - on [Cyclic convolution](cyclic-convolution.md): $i$ (first index): An index into the first list, running over 0 to S-1.
21. $j$
   - on `tensor-product`: $j$ (basis index of F): The index of a basis vector $f_j$, running from $1$ to $q$.
   - on [Discrete Fourier transform](fourier-transform.md): $j$ (input index): An index running over the entries of u, from 0 to q-1.
22. $j$
   - on `tensor-product`: $j$ (basis index of F): The index of a basis vector $f_j$, running from $1$ to $q$.
   - on [Cyclic convolution](cyclic-convolution.md): $j$ (second index): An index into the second list, running over 0 to S-1.
23. $S$
   - on `tensor-product`: $S$ (map on E): A linear map of $E$.
   - on [Cyclic convolution](cyclic-convolution.md): $S$ (list length): The number of coefficients in each list, which fixes the wraparound modulus.
24. $H_0$
   - on `butterfly-layer`: $H_0$ (simultaneous butterfly layer): The map applied at once to one selected bit of each of d chunks, acting as a two-point butterfly on each selected bit.
   - on [Tensor product](tensor-product.md): $H_0$ (butterfly): The two-point butterfly map, given by a $2\times 2$ matrix on $(u,v)$.
25. $H_0$
   - on `butterfly-layer`: $H_0$ (simultaneous butterfly layer): The map applied at once to one selected bit of each of d chunks, acting as a two-point butterfly on each selected bit.
   - on [Gaussian dyadic numbers](gaussian-dyadic.md): $H_0$ (butterfly map): The two-point map sending a pair $u, v$ to $((u+v)/2, (u-v)/2)$.
26. $r$
   - on `butterfly-layer`: $r$ (record length): The number of complex coefficients in each polynomial record stored at an address.
   - on [Discrete Fourier transform](fourier-transform.md): $r$ (summation index): A second summation index running over the entries of b, from 0 to q-1.
27. $e$
   - on `butterfly-layer`: $e$ (chunk length): The number of positions in each of the two chunks being interchanged.
   - on [Tensor product](tensor-product.md): $e$ (general vector of E): A general vector of $E$.
28. $r$
   - on `roots-of-unity`: $r$ (reduced length): The number of complex coefficients of a reduced polynomial, a power of two.
   - on [Discrete Fourier transform](fourier-transform.md): $r$ (summation index): A second summation index running over the entries of b, from 0 to q-1.
29. $r$
   - on `polynomial-ring`: $r$ (coefficient count): The number of complex coefficients in each polynomial record, which is a power of two.
   - on [Root of unity](roots-of-unity.md): $r$ (reduced length): The number of complex coefficients of a reduced polynomial, a power of two.
30. $r$
   - on `polynomial-ring`: $r$ (coefficient count): The number of complex coefficients in each polynomial record, which is a power of two.
   - on [Discrete Fourier transform](fourier-transform.md): $r$ (summation index): A second summation index running over the entries of b, from 0 to q-1.
31. $i$
   - on `polynomial-ring`: $i$ (coefficient position): The position of a coefficient in a coefficient list, running from 0 to r-1.
   - on [Cyclic convolution](cyclic-convolution.md): $i$ (first index): An index into the first list, running over 0 to S-1.
32. $k$
   - on `polynomial-ring`: $k$ (shift count): The number of places a coefficient is shifted when the element is multiplied by y^k, with 0 \le k < r.
   - on [Discrete Fourier transform](fourier-transform.md): $k$ (output index): An index running over the entries of the transform, from 0 to q-1.
33. $k$
   - on `polynomial-ring`: $k$ (shift count): The number of places a coefficient is shifted when the element is multiplied by y^k, with 0 \le k < r.
   - on [Cyclic convolution](cyclic-convolution.md): $k$ (output index): The index of an output coefficient c_k, running over 0 to S-1.
34. $\rho$
   - on `synthetic-transform`: $\rho$ (primitive root of unity): A primitive $S$-th root of unity, the root by which the transform's powers are taken.
   - on [Order of an element](order-of-element.md): $\rho$ (exponent): A positive integer exponent of $\gamma$.
35. $\zeta$
   - on `synthetic-transform`: $\zeta$ (normalized cyclic product): The normalized cyclic convolution of $\xi$ and $\eta$, a list of $S$ coefficients.
   - on [Root of unity](roots-of-unity.md): $\zeta$ (root of unity): The primitive q-th root of unity y^(2r/q) in the polynomial ring, for a power of two q dividing 2r.
36. $N$
   - on `gaussian-resampling`: $N$ (near-identity map): The composite of the selection map, the spreading map and the diagonal correction, a map from length-s vectors to themselves that is close to the identity.
   - on [Discrete Fourier transform](fourier-transform.md): $N$ (operation count): The number of operations the FFT uses on a vector of length q.
37. $\nu$
   - on `bluestein`: $\nu$ (twisted second sequence): The sequence $\nu_p=\overline{\chi_p}\,\tau_p$ indexed by $p$, the second input of the cyclic convolution.
   - on [Gaussian resampling](gaussian-resampling.md): $\nu$ (power exponent): The positive integer exponent with t = 2^nu in the application.
38. $k$
   - on `crt-axis-map`: $k$ (coefficient index): A position in the list of S coefficients, an integer with 0 <= k < S.
   - on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): $k$ (shift count): The number of places a coefficient is shifted when the element is multiplied by y^k, with 0 \le k < r.
39. $k$
   - on `crt-axis-map`: $k$ (coefficient index): A position in the list of S coefficients, an integer with 0 <= k < S.
   - on [Discrete Fourier transform](fourier-transform.md): $k$ (output index): An index running over the entries of the transform, from 0 to q-1.
40. $k$
   - on `crt-axis-map`: $k$ (coefficient index): A position in the list of S coefficients, an integer with 0 <= k < S.
   - on [Cyclic convolution](cyclic-convolution.md): $k$ (output index): The index of an output coefficient c_k, running over 0 to S-1.
41. $a_i$
   - on `crt-axis-map`: $a_i$ (axis digit): The digit of k on axis i in its mixed-radix expansion, an integer with 0 <= a_i < s_i.
   - on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): $a_i$ (coefficient): The complex coefficient of y^i in an element of the ring.
42. $i$
   - on `crt-axis-map`: $i$ (axis index): The index of an axis, running from 1 to d.
   - on [Polynomial ring modulo yʳ + 1](polynomial-ring.md): $i$ (coefficient position): The position of a coefficient in a coefficient list, running from 0 to r-1.
43. $i$
   - on `crt-axis-map`: $i$ (axis index): The index of an axis, running from 1 to d.
   - on [Cyclic convolution](cyclic-convolution.md): $i$ (first index): An index into the first list, running over 0 to S-1.
44. $j$
   - on `crt-axis-map`: $j$ (axis index): A second index of an axis, running from 1 to d, used in the digit sums.
   - on [Discrete Fourier transform](fourier-transform.md): $j$ (input index): An index running over the entries of u, from 0 to q-1.
45. $j$
   - on `crt-axis-map`: $j$ (axis index): A second index of an axis, running from 1 to d, used in the digit sums.
   - on [Cyclic convolution](cyclic-convolution.md): $j$ (second index): An index into the second list, running over 0 to S-1.
46. $m$
   - on `fixed-tape-multiplication`: $m$ (width factor): A fixed integer by which the address width falls at each recursion level.
   - on [Gaussian dyadic numbers](gaussian-dyadic.md): $m$ (integer numerator): The integer numerator of a dyadic rational written as $m/2^k$.
47. $m$
   - on `fixed-tape-multiplication`: $m$ (width factor): A fixed integer by which the address width falls at each recursion level.
   - on [Radix-digit convolution](radix-digit-convolution.md): $m$ (digit count): The number of radix digits in each input, $\lceil n/b \rceil$.
48. $m$
   - on `fixed-tape-multiplication`: $m$ (width factor): A fixed integer by which the address width falls at each recursion level.
   - on [Fast interchange of address chunks](tape-interchange.md): $m$ (matrix size): The number of rows of each rational matrix held at a vertex of the network, and the parameter of the recursion.
49. $m$
   - on `fixed-tape-multiplication`: $m$ (width factor): A fixed integer by which the address width falls at each recursion level.
   - on [Nested subspace labels](subspace-labels.md): $m$ (space dimension): The dimension of the space E, which counts the basis vectors of E.

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

Write the answer to `exegenius/tasks/0183-overloads.answer.json`, then run `exegenius submit 0183-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
