# exegenius task 0192-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the page that changes should do: use another letter, or say where the letter is used that it means something else there than on the other page. For the same thing, `note` may be empty.
- `change` is the page that changes. Leave it out for the later page. Give the earlier page's id when its use of the letter is the odd one out, for instance when the sources use the letter as the later page does, and the earlier page binds it on the page, not in a name. A page that other pages take the letter from keeps it and says where its meaning changes.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $y$
   - on `radix-digit-reduction`: $y$ (second integer): The second of the two integers being multiplied.
   - on [Convolution](convolution.md): $y$ (indeterminate): A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
2. $m$
   - on `dft-fft`: $m$ (frequency index): The position of an entry in a transform's output list, ranging over $0\le m<n$.
   - on [Address fields and array layout on tapes](address-fields.md): $m$ (tape position): The position of an item in tape order, so the item sits in the m-th cell.
3. $u$
   - on `dft-fft`: $u$ (first butterfly input): The first input of a butterfly.
   - on [Address fields and array layout on tapes](address-fields.md): $u$ (field width): The number of bits in one address field.
4. $j$
   - on `bluestein-chirp`: $j$ (output index): The index of an output of the transform, ranging over 0 to n-1.
   - on [Convolution](convolution.md): $j$ (index j): An index into the entries of the input list $b$.
5. $k$
   - on `bluestein-chirp`: $k$ (input index): The index of an entry of the input list a, ranging over 0 to n-1.
   - on [Convolution](convolution.md): $k$ (output index): An index into the entries of the output list $c$.
6. $l$
   - on `bluestein-chirp`: $l$ (chirp list index): The index into the chirp list z, ranging over 0 to n-1.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $l$ (index into b): The index into $b$ paired with $i$ at output $k$, namely $(k-i)\bmod n$.
7. $c$
   - on `bluestein-chirp`: $c$ (wrap count): The number of wraps, 0 or 1, in the relation k+l=j+cn.
   - on [Convolution](convolution.md): $c$ (output list): The cyclic convolution of $a$ and $b$, a list of $n$ entries.
8. $\sigma$
   - on `ring-convolution-retained-order`: $\sigma$ (layout permutation): The permutation of addresses fixed by the layout, which moves the entry for frequency $m$ to address $\sigma(m)$.
   - on [Last-coordinate phase twist](phase-twist-convolution.md): $\sigma$ (last-axis exponent): An exponent of $x$ on the last cyclic axis, ranging over $0\le\sigma<r$.
9. $\sigma$
   - on `ring-convolution-retained-order`: $\sigma$ (layout permutation): The permutation of addresses fixed by the layout, which moves the entry for frequency $m$ to address $\sigma(m)$.
   - on [Gaussian resampling](gaussian-resampling.md): $\sigma$ (Gaussian width): The width parameter of the Gaussian weights, an integer with 2 at most sigma below the square root of P.
10. $\lambda$
   - on `recursive-power-saving`: $\lambda$ (power exponent): The exponent, below 1, of the fixed power of the call parameter that bounds the cost per bit.
   - on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): $\lambda$ (scalar): A scalar of the field over which F is a vector space.
11. $m$
   - on `recursive-power-saving`: $m$ (growth factor): The factor by which the call parameter grows from one call to the recursive call.
   - on [Address fields and array layout on tapes](address-fields.md): $m$ (tape position): The position of an item in tape order, so the item sits in the m-th cell.
12. $K$
   - on `recursive-power-saving`: $K$ (chunk bit count): The number of bits in one axis chunk.
   - on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): $K$ (number of factors): The number of factors in the tensor power F^{\otimes K}, a count of how many vectors each pure tensor has.
13. $\beta$
   - on `recursive-power-saving`: $\beta$ (threshold exponent): The exponent, equal to one half, in the threshold f at least d to the power beta below which the recursion stops.
   - on [Finite linear network with roles and frames](linear-network-roles.md): $\beta$ (edge head): The node at which an edge ends.
14. $\nu$
   - on `recursive-power-saving`: $\nu$ (recursion level): The number of levels of unrolling the recursion, so that after nu levels the weight is (s/W) to the power nu.
   - on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): $\nu$ (field dimension): The number of vectors in a basis of F, which counts the coordinates of each factor.
15. $\nu$
   - on `recursive-power-saving`: $\nu$ (recursion level): The number of levels of unrolling the recursion, so that after nu levels the weight is (s/W) to the power nu.
   - on [Finite linear network with roles and frames](linear-network-roles.md): $\nu$ (network node): A source, gate or sink of the network, which carries one frame.
16. $\tau$
   - on `fast-address-interchange`: $\tau$ (cost exponent): A fixed exponent below 1 in the interchange cost $O(Vu^\tau)$, chosen so that $s/W<m^\tau$.
   - on [Recursive power saving from s<Wm](recursive-power-saving.md): $\tau$ (interchange exponent): The fixed exponent below 1 in the cost O(V u^tau) of an address interchange of u-bit fields.
17. $\tau$
   - on `fast-address-interchange`: $\tau$ (cost exponent): A fixed exponent below 1 in the interchange cost $O(Vu^\tau)$, chosen so that $s/W<m^\tau$.
   - on [Address shear and lower-triangular factorization](address-shear-factorization.md): $\tau$ (column of a one): The column of a 1 in Pi, which names the field D_tau that the update reads.
18. $d$
   - on `fast-butterfly-layers`: $d$ (chunk bound): An upper bound on the chunk count, so that the chunk count is at most d; on the recursive-power-saving page the letter d means the axis-count parameter.
   - on [Recursive power saving from s<Wm](recursive-power-saving.md): $d$ (axis-count parameter): The paper's parameter counting the axes of the array.
19. $s$
   - on `fast-butterfly-layers`: $s$ (child-call count): The number of child calls into which one node of the recursion reduces its group of selected chunks.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $s$ (butterfly exponent): The exponent of the twiddle factor $\omega^s$ of a butterfly.
20. $s$
   - on `fast-butterfly-layers`: $s$ (child-call count): The number of child calls into which one node of the recursion reduces its group of selected chunks.
   - on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): $s$ (reduced exponent): The exponent of the power $y^s$ that equals a given power of $y$, with $0\le s<2r$.
21. $s$
   - on `fast-butterfly-layers`: $s$ (child-call count): The number of child calls into which one node of the recursion reduces its group of selected chunks.
   - on [Three-element subset intersection construction](subset-intersection-construction.md): $s$ (total rank): The total rank of the edge matrices over all edges, which counts the smaller calls.
22. $\sigma$
   - on `fast-butterfly-layers`: $\sigma$ (fixed exponent): The fixed exponent $1-2^{-50}$ bounding s/W by a power of m; on the recursive-power-saving page the letter sigma means the leaf exponent.
   - on [Recursive power saving from s<Wm](recursive-power-saving.md): $\sigma$ (leaf exponent): An exponent at least max{0, log_m(s/W)} and below lambda, used to bound the leaf cost.
23. $\sigma$
   - on `fast-butterfly-layers`: $\sigma$ (fixed exponent): The fixed exponent $1-2^{-50}$ bounding s/W by a power of m; on the recursive-power-saving page the letter sigma means the leaf exponent.
   - on [Address shear and lower-triangular factorization](address-shear-factorization.md): $\sigma$ (row of a one): The row of a 1 in Pi, which names the field H_sigma that the update changes.
24. $\ell$
   - on `main-theorem`: $\ell$ (chunk digit count): The number of radix-q digits in a chunk at a recursion level, equal to m^k.
   - on [Finite linear network with roles and frames](linear-network-roles.md): $\ell$ (row index): The index of a row at a fixed prefix, which selects the role that receives the row.
25. $p$
   - on `main-theorem`: $p$ (logarithmic scale): The logarithmic scale 6 times the ceiling of lg n, the power in each row of the cost table.
   - on [Fixed-point precision and exact recovery](fixed-point-precision.md): $p$ (working precision): The number of bits of precision, the power of two 2^p in each numerator's denominator.
26. $p$
   - on `main-theorem`: $p$ (logarithmic scale): The logarithmic scale 6 times the ceiling of lg n, the power in each row of the cost table.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $p$ (input index): The index of an entry of the input list $z$, running from $0$ to $L-1$.
27. $p$
   - on `main-theorem`: $p$ (logarithmic scale): The logarithmic scale 6 times the ceiling of lg n, the power in each row of the cost table.
   - on [Finite linear network with roles and frames](linear-network-roles.md): $p$ (gate input count): The number of input arrays of a gate, counting the arrays it combines.

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

Write the answer to `exegenius/tasks/0192-overloads.answer.json`, then run `exegenius submit 0192-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
