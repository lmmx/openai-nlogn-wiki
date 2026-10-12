# exegenius task 0170-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the page that changes should do: use another letter, or say where the letter is used that it means something else there than on the other page. For the same thing, `note` may be empty.
- `change` is the page that changes. Leave it out for the later page. Give the earlier page's id when its use of the letter is the odd one out, for instance when the sources use the letter as the later page does, and the earlier page binds it on the page, not in a name. A page that other pages take the letter from keeps it and says where its meaning changes.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $n$
   - on `fourier-transform`: $n$ (sequence length): The count of entries in the input and output sequences, which is also the order of the root omega.
   - on [Primitive roots of unity](roots-of-unity.md): $n$ (root order): The order of the root, a positive integer that counts the positions of the transform it labels.
2. $j$
   - on `fourier-transform`: $j$ (input index): The position of an input entry, running from 0 to n-1.
   - on [Primitive roots of unity](roots-of-unity.md): $j$ (earlier exponent): An integer exponent of the root, the smaller of two powers compared in the distinctness argument.
3. $k$
   - on `fourier-transform`: $k$ (output index): The position of an output entry, running from 0 to n-1.
   - on [Primitive roots of unity](roots-of-unity.md): $k$ (power exponent): An integer exponent of the root, marking which power of $\omega$ is meant.
4. $b$
   - on `convolution-reduction`: $b$ (digit width): The number of bits in one digit, so each digit of an input lies between 0 and 2^b-1.
   - on [Cyclic convolution](cyclic-convolution.md): $b$ (second input sequence): The second of the two input sequences, a list of r complex numbers.
5. $A$
   - on `lower-triangular-factorization`: $A$ (rational matrix): The rational $m\times m$ matrix being factorized.
   - on [Matrix rank](matrix-rank.md): $A$ (real matrix): The real matrix whose rank is taken.
6. $d$
   - on `chinese-remainder-address-map`: $d$ (axis count): The number of prime cyclic axes on which the list is placed.
   - on [Fast address interchange](address-interchange.md): $d$ (matrix size): The size of the network's matrices; each field splits into d pieces.
7. $D$
   - on `simultaneous-butterfly-layer`: $D$ (chunks per layer): The number of selected equal-width address chunks used in one layer, a count, at most d.
   - on [Tensor product](tensor-product.md): $D$ (selected chunk count): The number of selected chunks, each contributing one selected address bit; here D replaces its earlier meaning.
8. $W$
   - on `recursive-power-saving`: $W$ (input role count): The number of input roles of the network, which counts the fixed places where values enter and not the scratch wires.
   - on [Fast address interchange](address-interchange.md): $W$ (wire count): The number of wires of the network, scratch wires included.
9. $s$
   - on `recursive-power-saving`: $s$ (smaller-call count): The number of smaller calls made by one call, the recursive calls the network makes at one level.
   - on [Address shear](address-shear.md): $s$ (field index of H): An index running over the fields of H, labelling the row of a 1 in Π.
10. $m$
   - on `recursive-power-saving`: $m$ (parameter factor): The factor by which the parameter grows from one level to the next.
   - on [Lower-triangular factorization](lower-triangular-factorization.md): $m$ (row count): The number of rows of $A$, which is also its number of columns.
11. $\gamma$
   - on `recursive-power-saving`: $\gamma$ (saving exponent): The fixed exponent of the saving, the power of the parameter by which the cost grows, equal to log base m of s/W.
   - on [Tensor product](tensor-product.md): $\gamma$ (basis vector of Y): A basis vector of Y, the second entry of a basis pair of X tensor Y.
12. $\gamma$
   - on `recursive-power-saving`: $\gamma$ (saving exponent): The fixed exponent of the saving, the power of the parameter by which the cost grows, equal to log base m of s/W.
   - on [Fast address interchange](address-interchange.md): $\gamma$ (cost ratio): The ratio R/W of the calls per level to the wires, which multiplies the cost of the recursion.
13. $C$
   - on `gaussian-resampling`: $C$ (identity constant): The power-of-two constant in the identity, the same for all n_0 and n_1.
   - on [Fast address interchange](address-interchange.md): $C$ (level constant): A constant bounding the work of one level, per stored bit.
14. $L_1$
   - on `gaussian-resampling`: $L_1$ (first contraction): The linear contraction from C^{n_0} to C^{n_1}.
   - on [Chinese-remainder address map](chinese-remainder-address-map.md): $L_1$ (axis length): The prime length of the first axis; the lengths of the other axes are L_2 to L_d.
15. $\gamma$
   - on `bluestein-chirp`: $\gamma$ (wrapped coefficient): The coefficient of y^{sigma+n} in the twisted product, the term that wraps past the top coefficient.
   - on [Tensor product](tensor-product.md): $\gamma$ (basis vector of Y): A basis vector of Y, the second entry of a basis pair of X tensor Y.
16. $\gamma$
   - on `bluestein-chirp`: $\gamma$ (wrapped coefficient): The coefficient of y^{sigma+n} in the twisted product, the term that wraps past the top coefficient.
   - on [Fast address interchange](address-interchange.md): $\gamma$ (cost ratio): The ratio R/W of the calls per level to the wires, which multiplies the cost of the recursion.

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

Write the answer to `exegenius/tasks/0170-overloads.answer.json`, then run `exegenius submit 0170-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
