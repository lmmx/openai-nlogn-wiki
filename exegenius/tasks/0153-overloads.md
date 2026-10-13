# exegenius task 0153-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the page that changes should do: use another letter, or say where the letter is used that it means something else there than on the other page. For the same thing, `note` may be empty.
- `change` is the page that changes. Leave it out for the later page. Give the earlier page's id when its use of the letter is the odd one out, for instance when the sources use the letter as the later page does, and the earlier page binds it on the page, not in a name. A page that other pages take the letter from keeps it and says where its meaning changes.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $y$
   - on `radix-digit-reduction`: $y$ (second input integer): The second of the two integers being multiplied, written with n bits.
   - on [Convolution](convolution.md): $y$ (indeterminate): A symbol with no value, used as the variable of the polynomials whose coefficients are the lists.
2. $b$
   - on `radix-digit-reduction`: $b$ (digit width): The number of bits in each radix digit.
   - on [Convolution](convolution.md): $b$ (input list b): The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
3. $m$
   - on `dft-fft`: $m$ (frequency index): The index of a transform value $A_m$, ranging over $0\le m<n$; this letter does not denote a cell position.
   - on [Address fields and array layout on tapes](address-fields.md): $m$ (tape position): The position of an item in tape order, which is also the item's address written in binary.
4. $u$
   - on `dft-fft`: $u$ (butterfly input u): The first input of a butterfly; this letter does not denote the field width.
   - on [Address fields and array layout on tapes](address-fields.md): $u$ (field width): The number of bits in one address field.
5. $\alpha$
   - on `scratch-restoration`: $\alpha$ (starting scratch value): The value a scratch wire holds before the procedure runs, which may be any value.
   - on [Finite linear network with roles and frames](linear-network-roles.md): $\alpha$ (edge tail): The node at which an edge starts.
6. $m$
   - on `address-shear-factorization`: $m$ (field count): The number of address fields in each vector.
   - on [Address fields and array layout on tapes](address-fields.md): $m$ (tape position): The position of an item in tape order, which is also the item's address written in binary.
7. $u$
   - on `address-shear-factorization`: $u$ (numerator): The integer numerator of a rational entry u/v.
   - on [Address fields and array layout on tapes](address-fields.md): $u$ (field width): The number of bits in one address field.
8. $v$
   - on `bluestein-chirp`: $v$ (twisted convolution): The cyclic convolution of the twisted lists, whose entry at output j is v_j.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $v$ (butterfly input v): The second input of a butterfly.
9. $j$
   - on `bluestein-chirp`: $j$ (output index): The index of an output of the transform, running from 0 to n-1.
   - on [Convolution](convolution.md): $j$ (index j): An index into the entries of the input list $b$.
10. $k$
   - on `bluestein-chirp`: $k$ (input index): The index of an input a_k of the transform, running from 0 to n-1.
   - on [Convolution](convolution.md): $k$ (output index): An index into the entries of the output list $c$.
11. $t$
   - on `bluestein-chirp`: $t$ (chirp index): The integer at which the chirp z_t is read.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $t$ (block offset): The position of an entry within the first half of a block.
12. $h$
   - on `bluestein-chirp`: $h$ (wrap count): The number of multiples of n by which k+l exceeds j, either 0 or 1.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $h$ (block size): The number of entries in a block, a power of two from 2 to $n$.
13. $k$
   - on `phase-twist-convolution`: $k$ (last-axis exponent): An exponent on the last axis, with $0\le k<r$, indexing one coefficient.
   - on [Bluestein's chirp identity](bluestein-chirp.md): $k$ (input index): The index of an input a_k of the transform, running from 0 to n-1.
14. $k$
   - on `phase-twist-convolution`: $k$ (last-axis exponent): An exponent on the last axis, with $0\le k<r$, indexing one coefficient.
   - on [Convolution](convolution.md): $k$ (output index): An index into the entries of the output list $c$.
15. $l$
   - on `phase-twist-convolution`: $l$ (second last-axis exponent): A second exponent on the last axis, with $0\le l<r$, paired with $k$ in a product.
   - on [Bluestein's chirp identity](bluestein-chirp.md): $l$ (paired index): The index of the chirp z_l paired with k in the twisted sum, running from 0 to n-1.
16. $l$
   - on `phase-twist-convolution`: $l$ (second last-axis exponent): A second exponent on the last axis, with $0\le l<r$, paired with $k$ in a product.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $l$ (paired index): The index into $b$ paired with the index $i$ at output $k$, namely $(k-i)\bmod n$.
17. $z$
   - on `phase-twist-convolution`: $z$ (cyclic variable): The variable of the cyclic ring $\mathbb C[z]/(z^r-1)$, whose exponents wrap modulo $r$.
   - on [Bluestein's chirp identity](bluestein-chirp.md): $z$ (chirp): The chirp zeta to the power minus t squared, read at an integer index t.
18. $\zeta$
   - on `phase-twist-convolution`: $\zeta$ (twist root): The root of unity $e^{\pi \mathrm i/r}$, whose $r$-th power is $-1$, used to rescale coefficients.
   - on [Bluestein's chirp identity](bluestein-chirp.md): $\zeta$ (chirp root of unity): A primitive 2n-th root of unity whose square is omega, from which the chirp phases are built.
19. $j$
   - on `phase-twist-convolution`: $j$ (cyclic product index): The exponent $j$, with $0\le j<r$, of the cyclic product $z^j$.
   - on [Bluestein's chirp identity](bluestein-chirp.md): $j$ (output index): The index of an output of the transform, running from 0 to n-1.
20. $j$
   - on `phase-twist-convolution`: $j$ (cyclic product index): The exponent $j$, with $0\le j<r$, of the cyclic product $z^j$.
   - on [Convolution](convolution.md): $j$ (index j): An index into the entries of the input list $b$.
21. $j$
   - on `phase-twist-convolution`: $j$ (cyclic product index): The exponent $j$, with $0\le j<r$, of the cyclic product $z^j$.
   - on [Polynomial ring modulo $y^r+1$](poly-ring-y-r.md): $j$ (reduction offset): The exponent left after removing $y^r$ from a power $y^{r+j}$, ranging over $0\le j<r$.
22. $h$
   - on `phase-twist-convolution`: $h$ (wrap flag): The flag $h\in\{0,1\}$ recording whether the exponent $k+l$ wrapped past $r$.
   - on [Bluestein's chirp identity](bluestein-chirp.md): $h$ (wrap count): The number of multiples of n by which k+l exceeds j, either 0 or 1.
23. $h$
   - on `phase-twist-convolution`: $h$ (wrap flag): The flag $h\in\{0,1\}$ recording whether the exponent $k+l$ wrapped past $r$.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $h$ (block size): The number of entries in a block, a power of two from 2 to $n$.
24. $v$
   - on `phase-twist-convolution`: $v$ (remaining-axis index): An index tuple with one coordinate per remaining cyclic axis, each wrapping modulo its length.
   - on [Bluestein's chirp identity](bluestein-chirp.md): $v$ (twisted convolution): The cyclic convolution of the twisted lists, whose entry at output j is v_j.
25. $v$
   - on `phase-twist-convolution`: $v$ (remaining-axis index): An index tuple with one coordinate per remaining cyclic axis, each wrapping modulo its length.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $v$ (butterfly input v): The second input of a butterfly.
26. $B$
   - on `signed-packing`: $B$ (block base): The base $B=2^{4p}$ in which each coefficient of a packed integer is a block.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $B$ (transform of b): The transform of the input list $b$.
27. $u$
   - on `signed-packing`: $u$ (packed polynomial): A polynomial in $\mathbb Z[y]$ with coefficients of absolute value at most $2^p$, whose packed integer is $u(B)$.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $u$ (butterfly input u): The first input of a butterfly; this letter does not denote the field width.
28. $u$
   - on `signed-packing`: $u$ (packed polynomial): A polynomial in $\mathbb Z[y]$ with coefficients of absolute value at most $2^p$, whose packed integer is $u(B)$.
   - on [Address fields and array layout on tapes](address-fields.md): $u$ (field width): The number of bits in one address field.
29. $v$
   - on `signed-packing`: $v$ (second packed polynomial): The second input polynomial in $\mathbb Z[y]$, with coefficients $v_t$ of absolute value at most $2^p$.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $v$ (butterfly input v): The second input of a butterfly.
30. $h$
   - on `signed-packing`: $h$ (product polynomial): The ordinary product $h=uv$ in $\mathbb Z[y]$ whose coefficients are recovered from the packed product.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $h$ (block size): The number of entries in a block, a power of two from 2 to $n$.
31. $k$
   - on `signed-packing`: $k$ (product coefficient index): The exponent $k$ of a coefficient $h_k$ of the product polynomial, running over $0,\dots,2r-2$.
   - on [Convolution](convolution.md): $k$ (output index): An index into the entries of the output list $c$.
32. $j$
   - on `signed-packing`: $j$ (coefficient position): The position of a coefficient $u_j$ of a packed polynomial, which is also its block exponent.
   - on [Convolution](convolution.md): $j$ (index j): An index into the entries of the input list $b$.
33. $t$
   - on `signed-packing`: $t$ (second coefficient position): The position of a coefficient $v_t$ of the second input polynomial.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $t$ (block offset): The position of an entry within the first half of a block.
34. $a$
   - on `signed-packing`: $a$ (real part a): The real component $a\in\mathbb Z[y]$ of a record, whose coefficients are $2^p$ times the real parts of the record's coefficients.
   - on [Convolution](convolution.md): $a$ (input list a): The first input coefficient list, with entries $a_0,\dots,a_{n-1}$.
35. $b$
   - on `signed-packing`: $b$ (imaginary part b): The imaginary component $b\in\mathbb Z[y]$ of a record, whose coefficients are $2^p$ times the imaginary parts of the record's coefficients.
   - on [Convolution](convolution.md): $b$ (input list b): The second input coefficient list, with entries $b_0,\dots,b_{n-1}$.
36. $c$
   - on `signed-packing`: $c$ (real part c): The real component $c\in\mathbb Z[y]$ of the second record $g$.
   - on [Convolution](convolution.md): $c$ (output list): The cyclic convolution of $a$ and $b$, a list of $n$ entries.
37. $t_T$
   - on `subset-intersection-construction`: $t_T$ (indicator vector of T): The indicator vector of the triple $T$.
   - on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): $t_T$ (triple indicator): The vector of F that has entry 1 on the three elements of the triple T and 0 elsewhere.
38. $m$
   - on `subset-intersection-construction`: $m$ (label space dimension): The dimension of $\mathcal F$, which counts the coordinates of a label space.
   - on [Address fields and array layout on tapes](address-fields.md): $m$ (tape position): The position of an item in tape order, which is also the item's address written in binary.
39. $\alpha$
   - on `subset-intersection-construction`: $\alpha$ (index): An ordered triple of triples $(T_1,T_2,T_3)$.
   - on [Finite linear network with roles and frames](linear-network-roles.md): $\alpha$ (edge tail): The node at which an edge starts.
40. $f$
   - on `recursive-power-saving`: $f$ (call parameter): The parameter of a call, counting field digits for an address interchange or selected axes for a numerical layer.
   - on [Finite linear network with roles and frames](linear-network-roles.md): $f$ (logical array): The logical array that a node stores in the form D_nu f.
41. $m$
   - on `recursive-power-saving`: $m$ (growth factor): The factor by which the parameter grows in one recursive call.
   - on [Three-element subset intersection construction](subset-intersection-construction.md): $m$ (label space dimension): The dimension of $\mathcal F$, which counts the coordinates of a label space.
42. $m$
   - on `recursive-power-saving`: $m$ (growth factor): The factor by which the parameter grows in one recursive call.
   - on [Address fields and array layout on tapes](address-fields.md): $m$ (tape position): The position of an item in tape order, which is also the item's address written in binary.
43. $\lambda$
   - on `recursive-power-saving`: $\lambda$ (power exponent): The fixed exponent below 1 of the power that bounds the cost per stored bit.
   - on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): $\lambda$ (scalar): A scalar of the field over which F is a vector space.
44. $K$
   - on `recursive-power-saving`: $K$ (chunk bit count): The number of address bits in one axis chunk.
   - on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): $K$ (number of factors): The number of factors in the tensor power F^{\otimes K}, a count of how many vectors each pure tensor has.
45. $\beta$
   - on `recursive-power-saving`: $\beta$ (threshold exponent): The fixed exponent 1/2 giving the threshold d^beta below which the recursion stops.
   - on [Finite linear network with roles and frames](linear-network-roles.md): $\beta$ (edge head): The node at which an edge ends.
46. $\nu$
   - on `recursive-power-saving`: $\nu$ (recursion depth): The number of levels the recursion has been unrolled.
   - on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): $\nu$ (field dimension): The number of vectors in a basis of F, which counts the coordinates of each factor.
47. $\nu$
   - on `recursive-power-saving`: $\nu$ (recursion depth): The number of levels the recursion has been unrolled.
   - on [Finite linear network with roles and frames](linear-network-roles.md): $\nu$ (network node): A source, gate or sink of the network, which carries one frame.
48. $\tau$
   - on `fast-address-interchange`: $\tau$ (cost exponent): A fixed exponent below 1 in the interchange cost $O(Vu^\tau)$, chosen so that $s/W<m^\tau$.
   - on [Recursive power saving from s<Wm](recursive-power-saving.md): $\tau$ (interchange exponent): The fixed exponent below 1 in the cost O(V u^tau) of an address interchange.
49. $D$
   - on `fast-butterfly-layers`: $D$ (selected chunk count): The number of selected address chunks.
   - on [Address shear and lower-triangular factorization](address-shear-factorization.md): $D$ (second field vector): The vector of m address fields $(D_1,\ldots,D_m)$ that the shear reads.
50. $d$
   - on `fast-butterfly-layers`: $d$ (chunk-count bound): An upper bound on D, the number of selected address chunks.
   - on [Recursive power saving from s<Wm](recursive-power-saving.md): $d$ (axis-count parameter): The paper's parameter giving the number of axes, which sets the chunk width and the threshold d^beta.
51. $d$
   - on `fast-butterfly-layers`: $d$ (chunk-count bound): An upper bound on D, the number of selected address chunks.
   - on [Address shear and lower-triangular factorization](address-shear-factorization.md): $d$ (second field content): The content of the field D_g in a pair (h,d).
52. $K$
   - on `fast-butterfly-layers`: $K$ (chunk width): The number of consecutive address bits in each chunk.
   - on [Recursive power saving from s<Wm](recursive-power-saving.md): $K$ (chunk bit count): The number of address bits in one axis chunk.
53. $K$
   - on `fast-butterfly-layers`: $K$ (chunk width): The number of consecutive address bits in each chunk.
   - on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): $K$ (number of factors): The number of factors in the tensor power F^{\otimes K}, a count of how many vectors each pure tensor has.
54. $X$
   - on `fast-butterfly-layers`: $X$ (bit-flip matrix): The 2 by 2 matrix that swaps the two basis values.
   - on [Fixed-point precision and exact recovery](fixed-point-precision.md): $X$ (integer numerator): An integer numerator storing a complex coefficient; it represents the value X/2^p.
55. $\Phi$
   - on `fast-butterfly-layers`: $\Phi$ (phase matrix): The diagonal matrix diag(1, i) of phases.
   - on [Fixed-point precision and exact recovery](fixed-point-precision.md): $\Phi$ (forward transform): The forward transform of length S, whose entries are the normalized sums (1/S) times the sum of xi_k omega^{mk}.
56. $\Phi$
   - on `fast-butterfly-layers`: $\Phi$ (phase matrix): The diagonal matrix diag(1, i) of phases.
   - on [Recursive power saving from s<Wm](recursive-power-saving.md): $\Phi$ (normalized cost): The cost of a call at parameter f divided by the volume V it works on.
57. $i$
   - on `fast-butterfly-layers`: $i$ (imaginary unit): The imaginary unit, with i squared equal to -1.
   - on [Convolution](convolution.md): $i$ (index i): An index into the entries of the input list $a$.
58. $C$
   - on `fast-butterfly-layers`: $C$ (two-point kernel): The 2 by 2 kernel that each butterfly applies to its pair of values.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $C$ (transform of c): The transform of the convolution list $c$.
59. $C$
   - on `fast-butterfly-layers`: $C$ (two-point kernel): The 2 by 2 kernel that each butterfly applies to its pair of values.
   - on [Recursive power saving from s<Wm](recursive-power-saving.md): $C$ (outside-work constant): A constant bounding the outside work at a node of parameter mf.
60. $\sigma$
   - on `fast-butterfly-layers`: $\sigma$ (recursion exponent): The fixed exponent 1 minus 2^{-50}, below 1, with s/W < m^sigma.
   - on [Recursive power saving from s<Wm](recursive-power-saving.md): $\sigma$ (leaf exponent): A fixed exponent with max{0, log_m(s/W)} at most sigma below lambda, used to bound the leaf costs.
61. $e$
   - on `main-theorem`: $e$ (chunk digit count): The number of radix-$q$ digits in a chunk at a recursion level, $e=m^t$.
   - on [Chinese-remainder map to prime cyclic axes](crt-address-map.md): $e$ (list index): An index of an entry of the list, an integer from 0 to N-1.
62. $e$
   - on `main-theorem`: $e$ (chunk digit count): The number of radix-$q$ digits in a chunk at a recursion level, $e=m^t$.
   - on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): $e$ (imaginary part e): The imaginary component $e\in\mathbb Z[y]$ of the second record $g$.
63. $e$
   - on `main-theorem`: $e$ (chunk digit count): The number of radix-$q$ digits in a chunk at a recursion level, $e=m^t$.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $e$ (power exponent): An integer with $0\le e<2r$, the exponent of the power $y^e$ that multiplies a coefficient list.
64. $e$
   - on `main-theorem`: $e$ (chunk digit count): The number of radix-$q$ digits in a chunk at a recursion level, $e=m^t$.
   - on [Three-element subset intersection construction](subset-intersection-construction.md): $e$ (element): An element of the ground set $[h]$.
65. $t$
   - on `main-theorem`: $t$ (recursion level): The recursion level of a chunk, so that a chunk at this level has $m^t$ digits.
   - on [Discrete Fourier transform and butterflies](dft-fft.md): $t$ (block offset): The position of an entry within the first half of a block.
66. $t$
   - on `main-theorem`: $t$ (recursion level): The recursion level of a chunk, so that a chunk at this level has $m^t$ digits.
   - on [Bluestein's chirp identity](bluestein-chirp.md): $t$ (chirp index): The integer at which the chirp z_t is read.
67. $t$
   - on `main-theorem`: $t$ (recursion level): The recursion level of a chunk, so that a chunk at this level has $m^t$ digits.
   - on [Signed coefficient packing (Kronecker substitution)](signed-packing.md): $t$ (second coefficient position): The position of a coefficient $v_t$ of the second input polynomial.
68. $F$
   - on `main-theorem`: $F$ (time per volume): The time divided by $V$ at a recursion level, as a function of the chunk digit count $e$.
   - on [Tensor product of vector spaces](tensor-product-of-vector-spaces.md): $F$ (vector space): The vector space whose tensor powers are formed, here Q^h in the bit network.
69. $\rho$
   - on `main-theorem`: $\rho$ (recursion ratio): The ratio $(s/W)/m^\tau$, which is below one for a suitable rational $\tau<1$.
   - on [Finite linear network with roles and frames](linear-network-roles.md): $\rho$ (role permutation): The permutation of roles that the scalar network applies, sending input role w to output role rho(w).

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

Write the answer to `exegenius/tasks/0153-overloads.answer.json`, then run `exegenius submit 0153-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
