# exegenius task 0141-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the page that changes should do: use another letter, or say where the letter is used that it means something else there than on the other page. For the same thing, `note` may be empty.
- `change` is the page that changes. Leave it out for the later page. Give the earlier page's id when its use of the letter is the odd one out, for instance when the sources use the letter as the later page does, and the earlier page binds it on the page, not in a name. A page that other pages take the letter from keeps it and says where its meaning changes.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $n$
   - on `fourier-transform`: $n$ (sequence length): The number of entries in the input and output sequences, the length of the transform; it is also the order of $\omega$.
   - on [Primitive roots of unity](roots-of-unity.md): $n$ (root order): The order of the root, a positive integer that counts the positions of the transform it labels.
2. $j$
   - on `fourier-transform`: $j$ (input index): The index of an input entry $a_j$, running from $0$ to $n-1$.
   - on [Primitive roots of unity](roots-of-unity.md): $j$ (earlier exponent): An integer exponent of the root, the smaller of two powers compared in the distinctness argument.
3. $k$
   - on `fourier-transform`: $k$ (output index): The index of an output entry $\hat a_k$, running from $0$ to $n-1$.
   - on [Primitive roots of unity](roots-of-unity.md): $k$ (power exponent): An integer exponent of the root, marking which power of $\omega$ is meant.
4. $b$
   - on `convolution-reduction`: $b$ (digit width): The number of bits in one digit, so each digit lies between 0 and 2^b-1.
   - on [Cyclic convolution](cyclic-convolution.md): $b$ (second input sequence): The second of the two input sequences, a list of r complex numbers.
5. $r$
   - on `polynomial-ring-y`: $r$ (coefficient count): The number of complex coefficients in the list of one element of the ring, a power of two.
   - on [Cyclic convolution](cyclic-convolution.md): $r$ (sequence length): The number of complex coefficients in each input sequence, so both sequences have length r.
6. $x$
   - on `synthetic-transform`: $x$ (input sequence): The sequence $x_0,\dots,x_{2r-1}$ of ring elements whose transform is taken.
   - on [Discrete Fourier transform](fourier-transform.md): $x$ (formal variable): The formal variable of $p$, a placeholder for a number to be substituted.
7. $x$
   - on `synthetic-transform`: $x$ (input sequence): The sequence $x_0,\dots,x_{2r-1}$ of ring elements whose transform is taken.
   - on [Cyclic convolution](cyclic-convolution.md): $x$ (formal variable): A formal variable, an indeterminate not evaluated at any number, used as the placeholder of the polynomials a(x) and b(x).
8. $A$
   - on `lower-triangular-factorization`: $A$ (input matrix): The rational m×m matrix that is factored.
   - on [Matrix rank](matrix-rank.md): $A$ (real matrix): The real matrix whose rank is taken.
9. $\beta$
   - on `address-interchange`: $\beta$ (matrix size): The number of rows and columns of each matrix of the network.
   - on [Linear network with restored auxiliary values](linear-network-exchange.md): $\beta$ (head vertex): A vertex of the network, the vertex where an edge from $\alpha$ ends.
10. $\lambda$
   - on `address-interchange`: $\lambda$ (level cost ratio): The ratio R/W, the cost factor per level.
   - on [Linear network with restored auxiliary values](linear-network-exchange.md): $\lambda$ (first example value): The value on the first wire at the address $\xi$ in the example.
11. $e$
   - on `chinese-remainder-address-map`: $e$ (list position): An index of a position in the list, running from $0$ to $N-1$.
   - on [Fast address interchange](address-interchange.md): $e$ (edge): An edge of the network, the wire segment between two consecutive vertices.
12. $D$
   - on `simultaneous-butterfly-layer`: $D$ (chunks per layer): The number of selected equal-width address chunks used in one layer, a count, at most d.
   - on [Tensor product](tensor-product.md): $D$ (selected chunk count): The number of address chunks, each contributing one selected address bit to the layer.
13. $W$
   - on `recursive-power-saving`: $W$ (role count): The number of roles of the network, the input wires that each carry a share of the data.
   - on [Fast address interchange](address-interchange.md): $W$ (wire count): The number of wires of the network, scratch wires included.
14. $s$
   - on `recursive-power-saving`: $s$ (smaller-call count): The number of smaller calls that the network makes.
   - on [Address shear](address-shear.md): $s$ (field index of H): An index running over the fields of H, labelling the row of a 1 in Π.
15. $m$
   - on `recursive-power-saving`: $m$ (parameter multiplier): The factor by which the parameter grows from a smaller call to the call above it.
   - on [Lower-triangular factorization](lower-triangular-factorization.md): $m$ (matrix size): The number of rows of A, so A is m×m; here m replaces its earlier meaning of digits per input.
16. $e$
   - on `recursive-power-saving`: $e$ (smaller-call parameter): The parameter of a smaller call.
   - on [Fast address interchange](address-interchange.md): $e$ (edge): An edge of the network, the wire segment between two consecutive vertices.
17. $\ell$
   - on `recursive-power-saving`: $\ell$ (level index): The index of a level, counted from the top level, which is 0.
   - on [Fast address interchange](address-interchange.md): $\ell$ (level count): The number of levels, each dividing the field width by beta.
18. $\alpha$
   - on `recursive-power-saving`: $\alpha$ (saving exponent): The exponent of the saving, the value of $\log_m(s/W)$ that makes $s/W$ equal to $m^\alpha$.
   - on [Linear network with restored auxiliary values](linear-network-exchange.md): $\alpha$ (tail vertex): A vertex of the network, the vertex where an edge starts.
19. $s$
   - on `gaussian-resampling`: $s$ (source transform length): The length of the source transform, the count of entries of the sequences it acts on.
   - on [Address shear](address-shear.md): $s$ (field index of H): An index running over the fields of H, labelling the row of a 1 in Π.
20. $t$
   - on `gaussian-resampling`: $t$ (target transform length): The length of the target transform, a power of two, which is the count of its entries.
   - on [Address shear](address-shear.md): $t$ (field index of D): An index running over the fields of D, labelling the column of a 1 in Π.
21. $c$
   - on `gaussian-resampling`: $c$ (identity constant): A power of two that is the same for all s and t, the constant factor of the identity.
   - on [Cyclic convolution](cyclic-convolution.md): $c$ (cyclic convolution): The cyclic convolution of a and b, a sequence of r complex coefficients.
22. $\alpha$
   - on `bluestein-chirp`: $\alpha$ (wrapped coefficient): The coefficient at $y^{\sigma+n}$ in the twisted product, before the wrap.
   - on [Linear network with restored auxiliary values](linear-network-exchange.md): $\alpha$ (tail vertex): A vertex of the network, the vertex where an edge starts.
23. $\alpha$
   - on `rounding-recovery`: $\alpha$ (first digit array): The array of radix-2^b digits of the first integer, zero-padded to S entries.
   - on [Bluestein's chirp identity](bluestein-chirp.md): $\alpha$ (wrapped coefficient): The coefficient at $y^{\sigma+n}$ in the twisted product, before the wrap.
24. $\alpha$
   - on `rounding-recovery`: $\alpha$ (first digit array): The array of radix-2^b digits of the first integer, zero-padded to S entries.
   - on [Linear network with restored auxiliary values](linear-network-exchange.md): $\alpha$ (tail vertex): A vertex of the network, the vertex where an edge starts.
25. $\beta$
   - on `rounding-recovery`: $\beta$ (second digit array): The array of radix-2^b digits of the second integer, zero-padded to S entries.
   - on [Tensor product](tensor-product.md): $\beta$ (basis vector of X): A basis vector of X, one half of a basis pair of the tensor product.
26. $\beta$
   - on `rounding-recovery`: $\beta$ (second digit array): The array of radix-2^b digits of the second integer, zero-padded to S entries.
   - on [Fast address interchange](address-interchange.md): $\beta$ (matrix size): The number of rows and columns of each matrix of the network.
27. $\beta$
   - on `rounding-recovery`: $\beta$ (second digit array): The array of radix-2^b digits of the second integer, zero-padded to S entries.
   - on [Linear network with restored auxiliary values](linear-network-exchange.md): $\beta$ (head vertex): A vertex of the network, the vertex where an edge from $\alpha$ ends.
28. $S$
   - on `rounding-recovery`: $S$ (source length): The number of entries of each zero-padded array, which is also the length of the source transform.
   - on [Tensor product](tensor-product.md): $S$ (map on X): A linear map on X, the factor acting on the X-part of a pair.
29. $R$
   - on `rounding-recovery`: $R$ (coordinate permutation): The permutation retained during resampling, which reindexes an array by $(R\alpha)_j=\alpha_{ej}$.
   - on [Fast address interchange](address-interchange.md): $R$ (total edge rank): The sum of the edge matrix ranks, which counts the recursive calls in one level.
30. $e$
   - on `rounding-recovery`: $e$ (reindexing unit): A unit modulo S, an integer coprime to S, by which the indices of the permutation R are multiplied.
   - on [Chinese-remainder address map](chinese-remainder-address-map.md): $e$ (list position): An index of a position in the list, running from $0$ to $N-1$.
31. $e$
   - on `rounding-recovery`: $e$ (reindexing unit): A unit modulo S, an integer coprime to S, by which the indices of the permutation R are multiplied.
   - on [Fast address interchange](address-interchange.md): $e$ (edge): An edge of the network, the wire segment between two consecutive vertices.
32. $p$
   - on `rounding-recovery`: $p$ (fractional bit count): The number of fractional bits kept by each truncation, here p = 6b; the letter changes meaning from the pivot of earlier pages.
   - on [Discrete Fourier transform](fourier-transform.md): $p$ (coefficient polynomial): The polynomial $p(x)=\sum_{j} a_j x^j$ whose coefficient list is $a$.

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

Write the answer to `exegenius/tasks/0141-overloads.answer.json`, then run `exegenius submit 0141-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
