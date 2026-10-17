# exegenius task 0216-overloads

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the page that changes should do: use another letter, or say where the letter is used that it means something else there than on the other page. For the same thing, `note` may be empty.
- `change` is the page that changes. Leave it out for the later page. Give the earlier page's id when its use of the letter is the odd one out, for instance when the sources use the letter as the later page does, and the earlier page binds it on the page, not in a name. A page that other pages take the letter from keeps it and says where its meaning changes.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $T$
   - on `radix-digit-reduction`: $T$ (padded length): A power of two with 4n/b <= T < 8n/b.
   - on [Cyclic convolution](convolution.md): $T$ (coefficient count): The total number of complex coefficients in an array.
2. $q$
   - on `radix-digit-reduction`: $q$ (digit count): The number of radix-2^b digits in each input.
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
3. $q$
   - on `stream-ops`: $q$ (radix): The number of values one digit can take.
   - on [Discrete Fourier transform](dft.md): $q$ (sequence length): The number of entries of a sequence.
4. $q$
   - on `stream-ops`: $q$ (radix): The number of values one digit can take.
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
5. $q$
   - on `controlled-shifts`: $q$ (prime modulus base): A fixed prime; on this page it is not a sequence length.
   - on [Elementary stream operations](stream-ops.md): $q$ (radix): The number of values one digit can take.
6. $q$
   - on `controlled-shifts`: $q$ (prime modulus base): A fixed prime; on this page it is not a sequence length.
   - on [Discrete Fourier transform](dft.md): $q$ (sequence length): The number of entries of a sequence.
7. $q$
   - on `controlled-shifts`: $q$ (prime modulus base): A fixed prime; on this page it is not a sequence length.
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
8. $b$
   - on `controlled-shifts`: $b$ (field digit count): The number of base-$q$ digits of a field.
   - on [Butterflies and the fast transform](butterfly.md): $b$ (lowest bit): The lowest bit of the output index m.
9. $B$
   - on `controlled-shifts`: $B$ (suffix bit count): The number of bits following the target field.
   - on [Elementary stream operations](stream-ops.md): $B$ (entries per row): The number of entries in each row.
10. $m$
   - on `matrix-shear`: $m$ (fields per group): The number of fields in each of the groups H and D.
   - on [Butterflies and the fast transform](butterfly.md): $m$ (output index): The index of an output of the transform.
11. $a$
   - on `matrix-shear`: $a$ (rank of A): The rank of the rational matrix A.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $a$ (offset): The offset in [Q] added to the target field, prepared from the control values.
12. $b$
   - on `phase-kernel`: $b$ (kernel coefficient b): The complex constant (1-i)/2, the coefficient of the bit flip in C.
   - on [Butterflies and the fast transform](butterfly.md): $b$ (lowest bit): The lowest bit of the output index m.
13. $d$
   - on `crt-map`: $d$ (number of axes): The number of axes of the target ring.
   - on [Cyclic convolution](convolution.md): $d$ (axis count): The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
14. $t_i$
   - on `crt-map`: $t_i$ (padded axis length): The padded length of axis i, either r/2 or r.
   - on [Cyclic convolution](convolution.md): $t_i$ (axis length): The length of cyclic axis i.
15. $V$
   - on `crt-map`: $V$ (stream volume): The volume of the stream being moved, Tp bits.
   - on [Elementary stream operations](stream-ops.md): $V$ (array volume): The number of radix-q digits an array stores.
16. $T$
   - on `crt-map`: $T$ (padded record count): The number of padded records, the product of the t_i.
   - on [Cyclic convolution](convolution.md): $T$ (coefficient count): The total number of complex coefficients in an array.
17. $k$
   - on `crt-map`: $k$ (coefficient index): The index of a coefficient of the length-S sequence.
   - on [Multidimensional transforms](multidim-transform.md): $k$ (output index tuple): An output index tuple shaped like j.
18. $\alpha$
   - on `gaussian-resampling`: $\alpha$ (Gaussian width parameter): An integer, with 2 <= alpha < sqrt p, that is the width parameter of the Gaussian weights.
   - on [Multidimensional transforms](multidim-transform.md): $\alpha$ (resampling parameter): An integer resampling parameter with 2<=alpha<sqrt p.
19. $\delta$
   - on `gaussian-resampling`: $\delta$ (exponent slack): A fixed constant 0 < delta < 1/8 that is the slack in the exponents of the time bounds.
   - on [Multidimensional transforms](multidim-transform.md): $\delta$ (time-bound slack): A fixed constant with 0<delta<1/8 that sets the slack in the exponent 3/2+delta of p in the time bound.
20. $k$
   - on `gaussian-resampling`: $k$ (output coordinate index): A coordinate index of a vector in C^t, taken modulo t.
   - on [Multidimensional transforms](multidim-transform.md): $k$ (output index tuple): An output index tuple shaped like j.
21. $t$
   - on `gaussian-resampling`: $t$ (target length): The larger length, a power of two in the application, of the transform used instead of the length-s one.
   - on [Butterflies and the fast transform](butterfly.md): $t$ (transform length): The number of positions in the sequence being transformed, a power of two.
22. $\boldsymbol s$
   - on `retained-permutations`: $\boldsymbol s$ (source length tuple): The tuple of the prime axis lengths $s_i$.
   - on [Multidimensional transforms](multidim-transform.md): $\boldsymbol s$ (source lengths): The tuple of source axis lengths (s_1,...,s_d).
23. $\boldsymbol t$
   - on `retained-permutations`: $\boldsymbol t$ (padded length tuple): The tuple of the power-of-two axis lengths $t_i$.
   - on [Bluestein chirp identity](chirp.md): $\boldsymbol t$ (axis lengths): The tuple (t_1,...,t_d) of axis lengths, where t_i is the even number of entries along axis i.
24. $\boldsymbol t$
   - on `retained-permutations`: $\boldsymbol t$ (padded length tuple): The tuple of the power-of-two axis lengths $t_i$.
   - on [Multidimensional transforms](multidim-transform.md): $\boldsymbol t$ (padded lengths): The tuple of padded power-of-two axis lengths (t_1,...,t_d).
25. $h$
   - on `retained-permutations`: $h$ (summation index): The index of summation in the Fourier sum, substituted by ck.
   - on [Butterflies and the fast transform](butterfly.md): $h$ (remaining index): The output index m with its lowest bit removed.
26. $g$
   - on `retained-permutations`: $g$ (setup degree): A fixed exponent such that setup work per line is O(p^g).
   - on [Contractions and bilinear contractions](contraction-maps.md): $g$ (second operand): The second operand of the bilinear map.
27. $u$
   - on `retained-permutations`: $u$ (first array): A complex array (not an integer) in the resampling and convolution identities of this page.
   - on [Discrete Fourier transform](dft.md): $u$ (input sequence): A sequence of q complex numbers to be transformed.
28. $L$
   - on `precision-recovery`: $L$ (log of padded length): The base-2 logarithm of the padded length $T$.
   - on [Contractions and bilinear contractions](contraction-maps.md): $L$ (linear map): A linear map whose norm bound is being defined.
29. $u$
   - on `precision-recovery`: $u$ (scaled digit array): The array of scaled radix digits of the first input, each stored as its value times $2^{-b-2}$ (not the integer).
   - on [Discrete Fourier transform](dft.md): $u$ (input sequence): A sequence of q complex numbers to be transformed.
30. $u$
   - on `precision-recovery`: $u$ (scaled digit array): The array of scaled radix digits of the first input, each stored as its value times $2^{-b-2}$ (not the integer).
   - on [Multiplication as radix-digit convolution](radix-digit-reduction.md): $u$ (first input): The first of the two integers being multiplied.
31. $v$
   - on `precision-recovery`: $v$ (scaled digit array): The array of scaled radix digits of the second input (not the integer).
   - on [Multiplication as radix-digit convolution](radix-digit-reduction.md): $v$ (second input): The second of the two integers being multiplied.
32. $\tau$
   - on `parameter-choice`: $\tau$ (chunk-interchange exponent): The exponent in the cost of a chunk interchange.
   - on [Chinese-remainder address map](crt-map.md): $\tau$ (chunk-swap exponent): A fixed exponent below 1 in the cost of a chunk interchange.
33. $V$
   - on `parameter-choice`: $V$ (bit volume): The number of bits of the logical array the layer acts on.
   - on [Chinese-remainder address map](crt-map.md): $V$ (stream volume): The volume of the stream being moved, Tp bits.
34. $V$
   - on `parameter-choice`: $V$ (bit volume): The number of bits of the logical array the layer acts on.
   - on [Elementary stream operations](stream-ops.md): $V$ (array volume): The number of radix-q digits an array stores.
35. $c$
   - on `parameter-choice`: $c$ (chunk-width exponent): The exponent of the address-chunk width (a new meaning of c).
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $c$ (scaling integer): A fixed positive integer prime to q by which the target field is multiplied; not the machine constant.
36. $\delta$
   - on `parameter-choice`: $\delta$ (resampling slack): The slack in the exponent of the resampling cost.
   - on [Multidimensional transforms](multidim-transform.md): $\delta$ (time-bound slack): A fixed constant with 0<delta<1/8 that sets the slack in the exponent 3/2+delta of p in the time bound.
37. $\delta$
   - on `parameter-choice`: $\delta$ (resampling slack): The slack in the exponent of the resampling cost.
   - on [Gaussian resampling](gaussian-resampling.md): $\delta$ (exponent slack): A fixed constant 0 < delta < 1/8 that is the slack in the exponents of the time bounds.
38. $F$
   - on `subspace-labels`: $F$ (one-factor label space): The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $F$ (base space): A space of dimension h with a nondegenerate form, whose triple power is the label space.
39. $X$
   - on `subspace-labels`: $X$ (X bank): The bank of data wires $X_a$.
   - on [Linear exchange network with restored scratch wires](exchange-network.md): $X$ (bank X): The first data bank, with entries X_a.
40. $Y$
   - on `subspace-labels`: $Y$ (Y bank): The bank of data wires $Y_a$.
   - on [Linear exchange network with restored scratch wires](exchange-network.md): $Y$ (bank Y): The second data bank, with entries Y_a.
41. $A$
   - on `subspace-labels`: $A$ (exposed factor space): The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $A$ (ambient space): A finite-dimensional space with a nondegenerate form, containing the subspace P.
42. $P$
   - on `subspace-labels`: $P$ (earlier tensor line): The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $P$ (subspace of A): A subspace of A, later taken nondegenerate.
43. $B$
   - on `subspace-labels`: $B$ (complement of P): The orthogonal complement of $P$ inside $A$.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $B$ (orthogonal complement): The orthogonal complement of P in A.
44. $F$
   - on `rank-recurrence`: $F$ (time per unit volume): The running time of a call at a given parameter divided by the volume of its stream.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $F$ (one-factor label space): The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
45. $F$
   - on `rank-recurrence`: $F$ (time per unit volume): The running time of a call at a given parameter divided by the volume of its stream.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $F$ (base space): A space of dimension h with a nondegenerate form, whose triple power is the label space.
46. $j$
   - on `rank-recurrence`: $j$ (recursion depth): The number of recursion levels between the top call and a given call.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $j$ (stage number): The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
47. $u$
   - on `address-interchange`: $u$ (chunk width): The number of bits in each of the two interchanged address chunks.
   - on [Discrete Fourier transform](dft.md): $u$ (input sequence): A sequence of q complex numbers to be transformed.
48. $V$
   - on `address-interchange`: $V$ (array volume): The number of bits stored in the array.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $V$ (larger label): A label containing the label $U$ at the other end of an edge.
49. $p$
   - on `address-interchange`: $p$ (prefix): The part of an address before the first chunk.
   - on [Fixed-point Gaussian dyadic records](fixed-point.md): $p$ (fractional bits): The number of fractional bits of the grid on which stored values lie.
50. $h$
   - on `address-interchange`: $h$ (first chunk): The first of the two address chunks being interchanged.
   - on [Butterflies and the fast transform](butterfly.md): $h$ (remaining index): The output index m with its lowest bit removed.
51. $h$
   - on `address-interchange`: $h$ (first chunk): The first of the two address chunks being interchanged.
   - on [Linear exchange network with restored scratch wires](exchange-network.md): $h$ (ground-set size): The size of the ground set [h] whose three-element subsets index the data.
52. $d$
   - on `address-interchange`: $d$ (second chunk): The second of the two address chunks being interchanged.
   - on [Cyclic convolution](convolution.md): $d$ (axis count): The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
53. $q$
   - on `address-interchange`: $q$ (digit radix): The fixed prime that is the radix of the digits.
   - on [Elementary stream operations](stream-ops.md): $q$ (radix): The number of values one digit can take.
54. $q$
   - on `address-interchange`: $q$ (digit radix): The fixed prime that is the radix of the digits.
   - on [Discrete Fourier transform](dft.md): $q$ (sequence length): The number of entries of a sequence.
55. $q$
   - on `address-interchange`: $q$ (digit radix): The fixed prime that is the radix of the digits.
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
56. $q$
   - on `address-interchange`: $q$ (digit radix): The fixed prime that is the radix of the digits.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $q$ (prime modulus base): A fixed prime; on this page it is not a sequence length.
57. $k$
   - on `address-interchange`: $k$ (recursion levels): The number of recursion levels, with e = m^k.
   - on [Fixed-point Gaussian dyadic records](fixed-point.md): $k$ (depth): The number of operations in sequence since the layer began that produced a value.
58. $M$
   - on `address-interchange`: $M$ (vertex matrix): The rational m by m matrix carried by a terminal or gate of the network.
   - on [Cyclic convolution](convolution.md): $M$ (address count): The number of cyclic addresses of an array, the product of the axis lengths.
59. $x$
   - on `address-interchange`: $x$ (stream row): The row number within a role stream.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $x$ (vector of F): A vector of $F$, the first argument of the bilinear form.
60. $j$
   - on `address-interchange`: $j$ (recursion level): The index of a recursion level in the unrolled recurrence.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $j$ (wrap count): The integer part of cy/Q, counting how often cy wraps past Q.
61. $j$
   - on `address-interchange`: $j$ (recursion level): The index of a recursion level in the unrolled recurrence.
   - on [Recursive power saving](rank-recurrence.md): $j$ (recursion depth): The number of recursion levels between the top call and a given call.
62. $j$
   - on `address-interchange`: $j$ (recursion level): The index of a recursion level in the unrolled recurrence.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $j$ (stage number): The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
63. $v$
   - on `phase-frames`: $v$ (binary vector): A vector of F_2^m; in the main argument a basis vector of an edge residual. Here v does not mean the triple count.
   - on [Linear exchange network with restored scratch wires](exchange-network.md): $v$ (number of triples): The number of three-element subsets of [h].
64. $E$
   - on `phase-frames`: $E$ (edge residual): The subspace added to U to reach V, orthogonal to U; here E is not the first space of a tensor product.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $E$ (first space): The first of the two finite-dimensional vector spaces being tensored.
65. $k$
   - on `phase-frames`: $k$ (column count): The number of columns of an address; here k changes meaning from the fixed-point page.
   - on [Fixed-point Gaussian dyadic records](fixed-point.md): $k$ (depth): The number of operations in sequence since the layer began that produced a value.
66. $c$
   - on `packed-bit-addition`: $c$ (control bit): A bit, 0 or 1, that gates the eight additions.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $c$ (scaling integer): A fixed positive integer prime to q by which the target field is multiplied; not the machine constant.
67. $u$
   - on `packed-bit-addition`: $u$ (first integer): The integer updated by lines 1, 3, 6 and 8 of the eight additions.
   - on [Discrete Fourier transform](dft.md): $u$ (input sequence): A sequence of q complex numbers to be transformed.
68. $u$
   - on `packed-bit-addition`: $u$ (first integer): The integer updated by lines 1, 3, 6 and 8 of the eight additions.
   - on [Fast address-chunk interchange](address-interchange.md): $u$ (chunk width): The number of bits in each of the two interchanged address chunks.
69. $w$
   - on `packed-bit-addition`: $w$ (second integer): The integer updated by lines 2, 4, 5 and 7, restored at the end.
   - on [Fast address-chunk interchange](address-interchange.md): $w$ (wire index): The index of an input wire of the network.
70. $R$
   - on `packed-bit-addition`: $R$ (record bits): The number of bits in the record at each address.
   - on [Elementary stream operations](stream-ops.md): $R$ (row count): The number of rows in the array of item 4.
71. $R$
   - on `packed-bit-addition`: $R$ (record bits): The number of bits in the record at each address.
   - on [Frames on wire arrays](array-frames.md): $R$ (scalar ring): The ring of scalars carried by the wires.
72. $L$
   - on `packed-bit-addition`: $L$ (chunk bits): The number of bits in each of the chunks x, y, z, equal to fK.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $L$ (total dimension loss): The total number of dimensions lost on decreasing edges.
73. $K$
   - on `packed-bit-addition`: $K$ (segment spacing): The spacing between selected positions, at least 6, which is the length of each segment.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $K$ (later tensor line): The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
74. $f$
   - on `packed-bit-addition`: $f$ (selected bit count): The number of selected bits per chunk.
   - on [Recursive power saving](rank-recurrence.md): $f$ (call parameter): The size parameter of a call: the number of digits in each interchanged chunk, or the number of selected axes of a layer.
75. $M$
   - on `packed-bit-addition`: $M$ (address count): The number of addresses.
   - on [Fast address-chunk interchange](address-interchange.md): $M$ (vertex matrix): The rational m by m matrix carried by a terminal or gate of the network.
76. $\rho$
   - on `packed-bit-addition`: $\rho$ (selected-bit offset): The offset of the lowest selected position, 0 <= rho < K.
   - on [Fast address-chunk interchange](address-interchange.md): $\rho$ (role map): The map sending input wire w to its output role.
77. $g$
   - on `packed-bit-addition`: $g$ (guard value): The guard value of a segment, any g_i or h_i: its high K-1 bits.
   - on [Fast address-chunk interchange](address-interchange.md): $g$ (gap): The part of an address between the two chunks.
78. $q$
   - on `packed-bit-addition`: $q$ (address): An address of a record after S_0; q' is its destination T_0 S_0^{-1}(q).
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $q$ (prime modulus base): A fixed prime; on this page it is not a sequence length.
79. $q$
   - on `packed-bit-addition`: $q$ (address): An address of a record after S_0; q' is its destination T_0 S_0^{-1}(q).
   - on [Elementary stream operations](stream-ops.md): $q$ (radix): The number of values one digit can take.
80. $q$
   - on `packed-bit-addition`: $q$ (address): An address of a record after S_0; q' is its destination T_0 S_0^{-1}(q).
   - on [Discrete Fourier transform](dft.md): $q$ (sequence length): The number of entries of a sequence.
81. $q$
   - on `packed-bit-addition`: $q$ (address): An address of a record after S_0; q' is its destination T_0 S_0^{-1}(q).
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
82. $q$
   - on `packed-bit-addition`: $q$ (address): An address of a record after S_0; q' is its destination T_0 S_0^{-1}(q).
   - on [Fast address-chunk interchange](address-interchange.md): $q$ (digit radix): The fixed prime that is the radix of the digits.
83. $D$
   - on `simultaneous-layer`: $D$ (selected chunk count): The number of address chunks, at most d, on which the layer acts.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $D$ (source group): The second group of m fields, which is left unchanged by the shear.
84. $z$
   - on `simultaneous-layer`: $z$ (array): The array of records that the operators act on.
   - on [Fast address-chunk interchange](address-interchange.md): $z$ (suffix): The part of an address after the second chunk.
85. $e$
   - on `simultaneous-layer`: $e$ (group axis count): The number of selected axes in a group, e = mf.
   - on [Fast address-chunk interchange](address-interchange.md): $e$ (chunk digit count): The number of radix-q digits in a chunk.
86. $h$
   - on `simultaneous-layer`: $h$ (slot index): The index of a slot and of the residual basis vector placed in it.
   - on [Butterflies and the fast transform](butterfly.md): $h$ (remaining index): The output index m with its lowest bit removed.
87. $h$
   - on `simultaneous-layer`: $h$ (slot index): The index of a slot and of the residual basis vector placed in it.
   - on [Fast address-chunk interchange](address-interchange.md): $h$ (first chunk): The first of the two address chunks being interchanged.
88. $h$
   - on `simultaneous-layer`: $h$ (slot index): The index of a slot and of the residual basis vector placed in it.
   - on [Linear exchange network with restored scratch wires](exchange-network.md): $h$ (ground-set size): The size of the ground set [h] whose three-element subsets index the data.
89. $X_v$
   - on `simultaneous-layer`: $X_v$ (column shift): The operator shifting a column by v.
   - on [Binary phase frames](phase-frames.md): $X_v$ (translation): The operator shifting an array by the vector v: (X_v f)(x)=f(x+v).
90. $G$
   - on `simultaneous-layer`: $G$ (basis-change matrix): An invertible F_2 matrix whose first columns are the residual vectors.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $G$ (second space): The second of the two finite-dimensional vector spaces being tensored.
91. $A$
   - on `simultaneous-layer`: $A$ (chain length bound): A(e) bounds the number of arithmetic operations along a chain from an input to an intermediate coefficient.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $A$ (shear matrix): A rational m by m matrix, taken from a fixed finite set, that the shear applies.
92. $A$
   - on `simultaneous-layer`: $A$ (chain length bound): A(e) bounds the number of arithmetic operations along a chain from an input to an intermediate coefficient.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $A$ (exposed factor space): The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
93. $A$
   - on `simultaneous-layer`: $A$ (chain length bound): A(e) bounds the number of arithmetic operations along a chain from an input to an intermediate coefficient.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $A$ (ambient space): A finite-dimensional space with a nondegenerate form, containing the subspace P.
94. $E$
   - on `simultaneous-layer`: $E$ (per-invocation bound): The bound 64(W+m+1)^3 on the operations added by one invocation of the network.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $E$ (first space): The first of the two finite-dimensional vector spaces being tensored.
95. $E$
   - on `simultaneous-layer`: $E$ (per-invocation bound): The bound 64(W+m+1)^3 on the operations added by one invocation of the network.
   - on [Binary phase frames](phase-frames.md): $E$ (edge residual): The subspace added to U to reach V, orthogonal to U; here E is not the first space of a tensor product.
96. $B$
   - on `simultaneous-layer`: $B$ (level factor): The number s+E by which each recursion level multiplies the chain bound.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $B$ (suffix bit count): The number of bits following the target field.
97. $B$
   - on `simultaneous-layer`: $B$ (level factor): The number s+E by which each recursion level multiplies the chain bound.
   - on [Elementary stream operations](stream-ops.md): $B$ (entries per row): The number of entries in each row.
98. $B$
   - on `simultaneous-layer`: $B$ (level factor): The number s+E by which each recursion level multiplies the chain bound.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $B$ (complement of P): The orthogonal complement of $P$ inside $A$.
99. $B$
   - on `simultaneous-layer`: $B$ (level factor): The number s+E by which each recursion level multiplies the chain bound.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $B$ (orthogonal complement): The orthogonal complement of P in A.
100. $\nu$
   - on `simultaneous-layer`: $\nu$ (exponent of m): The least j at least 1 with m^j at least B.
   - on [Fast address-chunk interchange](address-interchange.md): $\nu$ (high digit count): The number of top digits of each chunk set aside to form the row field.
101. $D$
   - on `transform-layout`: $D$ (transformed axes): The number of transformed axes, d-1.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $D$ (source group): The second group of m fields, which is left unchanged by the shear.
102. $D$
   - on `transform-layout`: $D$ (transformed axes): The number of transformed axes, d-1.
   - on [Simultaneous butterfly layer](simultaneous-layer.md): $D$ (selected chunk count): The number of address chunks, at most d, on which the layer acts.
103. $K$
   - on `transform-layout`: $K$ (chunk width): The number of bits in an address chunk.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $K$ (later tensor line): The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
104. $K$
   - on `transform-layout`: $K$ (chunk width): The number of bits in an address chunk.
   - on [Packed selected-bit addition](packed-bit-addition.md): $K$ (segment spacing): The spacing between selected positions, at least 6, which is the length of each segment.
105. $\tau$
   - on `transform-layout`: $\tau$ (interchange exponent): The fixed exponent below 1 in the cost of the chunk interchange.
   - on [Fast address-chunk interchange](address-interchange.md): $\tau$ (saving exponent): The fixed exponent below 1 in the cost, equal to 1 - 2^{-50}.
106. $\ell$
   - on `transform-layout`: $\ell$ (long-axis address bits): The base-2 logarithm of r, the number of address bits of a long axis.
   - on [Simultaneous butterfly layer](simultaneous-layer.md): $\ell$ (depth): The depth of a value, the number of operations in sequence that produced it.
107. $B$
   - on `transform-layout`: $B$ (bit reversal): The bit-reversal permutation applied along every axis.
   - on [Elementary stream operations](stream-ops.md): $B$ (entries per row): The number of entries in each row.
108. $B$
   - on `transform-layout`: $B$ (bit reversal): The bit-reversal permutation applied along every axis.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $B$ (suffix bit count): The number of bits following the target field.
109. $B$
   - on `transform-layout`: $B$ (bit reversal): The bit-reversal permutation applied along every axis.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $B$ (complement of P): The orthogonal complement of $P$ inside $A$.
110. $B$
   - on `transform-layout`: $B$ (bit reversal): The bit-reversal permutation applied along every axis.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $B$ (orthogonal complement): The orthogonal complement of P in A.
111. $B$
   - on `transform-layout`: $B$ (bit reversal): The bit-reversal permutation applied along every axis.
   - on [Simultaneous butterfly layer](simultaneous-layer.md): $B$ (level factor): The number s+E by which each recursion level multiplies the chain bound.
112. $b$
   - on `transform-layout`: $b$ (leftover low bits): The number of low address bits of an axis left over after whole K-bit chunks.
   - on [Butterflies and the fast transform](butterfly.md): $b$ (lowest bit): The lowest bit of the output index m.
113. $b$
   - on `transform-layout`: $b$ (leftover low bits): The number of low address bits of an axis left over after whole K-bit chunks.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $b$ (field digit count): The number of base-$q$ digits of a field.
114. $b$
   - on `transform-layout`: $b$ (leftover low bits): The number of low address bits of an axis left over after whole K-bit chunks.
   - on [Two-point kernel C](phase-kernel.md): $b$ (kernel coefficient b): The complex constant (1-i)/2, the coefficient of the bit flip in C.
115. $q$
   - on `transform-layout`: $q$ (whole chunks): The number of whole K-bit chunks per axis.
   - on [Discrete Fourier transform](dft.md): $q$ (sequence length): The number of entries of a sequence.
116. $q$
   - on `transform-layout`: $q$ (whole chunks): The number of whole K-bit chunks per axis.
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
117. $q$
   - on `transform-layout`: $q$ (whole chunks): The number of whole K-bit chunks per axis.
   - on [Fast address-chunk interchange](address-interchange.md): $q$ (digit radix): The fixed prime that is the radix of the digits.
118. $q$
   - on `transform-layout`: $q$ (whole chunks): The number of whole K-bit chunks per axis.
   - on [Elementary stream operations](stream-ops.md): $q$ (radix): The number of values one digit can take.
119. $q$
   - on `transform-layout`: $q$ (whole chunks): The number of whole K-bit chunks per axis.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $q$ (prime modulus base): A fixed prime; on this page it is not a sequence length.
120. $q$
   - on `transform-layout`: $q$ (whole chunks): The number of whole K-bit chunks per axis.
   - on [Packed selected-bit addition](packed-bit-addition.md): $q$ (address): An address of a record after S_0; q' is its destination T_0 S_0^{-1}(q).
121. $L$
   - on `transform-layout`: $L$ (layout permutation): The record permutation made by the prefix moves and chunk exchanges.
   - on [Contractions and bilinear contractions](contraction-maps.md): $L$ (linear map): A linear map whose norm bound is being defined.
122. $L$
   - on `transform-layout`: $L$ (layout permutation): The record permutation made by the prefix moves and chunk exchanges.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $L$ (total dimension loss): The total number of dimensions lost on decreasing edges.
123. $L$
   - on `transform-layout`: $L$ (layout permutation): The record permutation made by the prefix moves and chunk exchanges.
   - on [Packed selected-bit addition](packed-bit-addition.md): $L$ (chunk bits): The number of bits in each of the chunks x, y, z, equal to fK.
124. $z$
   - on `transform-layout`: $z$ (round input): The array entering a round.
   - on [Fast address-chunk interchange](address-interchange.md): $z$ (suffix): The part of an address after the second chunk.
125. $z$
   - on `transform-layout`: $z$ (round input): The array entering a round.
   - on [Simultaneous butterfly layer](simultaneous-layer.md): $z$ (array): The array of records that the operators act on.
126. $M$
   - on `ring-convolution`: $M$ (number of records): The number of polynomial records, one per cyclic address of the remaining axes.
   - on [Cyclic convolution](convolution.md): $M$ (address count): The number of cyclic addresses of an array, the product of the axis lengths.
127. $M$
   - on `ring-convolution`: $M$ (number of records): The number of polynomial records, one per cyclic address of the remaining axes.
   - on [Fast address-chunk interchange](address-interchange.md): $M$ (vertex matrix): The rational m by m matrix carried by a terminal or gate of the network.
128. $M$
   - on `ring-convolution`: $M$ (number of records): The number of polynomial records, one per cyclic address of the remaining axes.
   - on [Packed selected-bit addition](packed-bit-addition.md): $M$ (address count): The number of addresses.
129. $T$
   - on `ring-convolution`: $T$ (number of coefficients): The number of complex coefficients in an array, T = rM.
   - on [Cyclic convolution](convolution.md): $T$ (coefficient count): The total number of complex coefficients in an array.
130. $T$
   - on `ring-convolution`: $T$ (number of coefficients): The number of complex coefficients in an array, T = rM.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $T$ (a triple): A three-element subset of $[h]$ (not the padded size used on other pages).
131. $P$
   - on `ring-convolution`: $P$ (pointwise product): The pointwise product of records, P(u,v) = uv/r.
   - on [Elementary stream operations](stream-ops.md): $P$ (prefix values): The number of prefix values indexing the first axis of the array.
132. $P$
   - on `ring-convolution`: $P$ (pointwise product): The pointwise product of records, P(u,v) = uv/r.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $P$ (earlier tensor line): The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
133. $P$
   - on `ring-convolution`: $P$ (pointwise product): The pointwise product of records, P(u,v) = uv/r.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $P$ (subspace of A): A subspace of A, later taken nondegenerate.
134. $L$
   - on `ring-convolution`: $L$ (layout permutation): The permutation of records produced by the tape layout.
   - on [Contractions and bilinear contractions](contraction-maps.md): $L$ (linear map): A linear map whose norm bound is being defined.
135. $L$
   - on `ring-convolution`: $L$ (layout permutation): The permutation of records produced by the tape layout.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $L$ (total dimension loss): The total number of dimensions lost on decreasing edges.
136. $L$
   - on `ring-convolution`: $L$ (layout permutation): The permutation of records produced by the tape layout.
   - on [Packed selected-bit addition](packed-bit-addition.md): $L$ (chunk bits): The number of bits in each of the chunks x, y, z, equal to fK.
137. $B$
   - on `ring-convolution`: $B$ (bit-reversal order): The bit-reversal order in which forward outputs are written.
   - on [Tape layout for synthetic transforms](transform-layout.md): $B$ (bit reversal): The bit-reversal permutation applied along every axis.
138. $B$
   - on `ring-convolution`: $B$ (bit-reversal order): The bit-reversal order in which forward outputs are written.
   - on [Elementary stream operations](stream-ops.md): $B$ (entries per row): The number of entries in each row.
139. $B$
   - on `ring-convolution`: $B$ (bit-reversal order): The bit-reversal order in which forward outputs are written.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $B$ (suffix bit count): The number of bits following the target field.
140. $B$
   - on `ring-convolution`: $B$ (bit-reversal order): The bit-reversal order in which forward outputs are written.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $B$ (complement of P): The orthogonal complement of $P$ inside $A$.
141. $B$
   - on `ring-convolution`: $B$ (bit-reversal order): The bit-reversal order in which forward outputs are written.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $B$ (orthogonal complement): The orthogonal complement of P in A.
142. $B$
   - on `ring-convolution`: $B$ (bit-reversal order): The bit-reversal order in which forward outputs are written.
   - on [Simultaneous butterfly layer](simultaneous-layer.md): $B$ (level factor): The number s+E by which each recursion level multiplies the chain bound.
143. $\ell$
   - on `ring-convolution`: $\ell$ (log of record length): The base-2 logarithm of the record length r.
   - on [Tape layout for synthetic transforms](transform-layout.md): $\ell$ (long-axis address bits): The base-2 logarithm of r, the number of address bits of a long axis.
144. $\ell$
   - on `ring-convolution`: $\ell$ (log of record length): The base-2 logarithm of the record length r.
   - on [Simultaneous butterfly layer](simultaneous-layer.md): $\ell$ (depth): The depth of a value, the number of operations in sequence that produced it.
145. $\eta$
   - on `ring-convolution`: $\eta$ (truncation error): The error bound sqrt2 * 2^{-p} for one truncation.
   - on [Recursive power saving](rank-recurrence.md): $\eta$ (relative deficit): The relative rank deficit (Wm - s)/(Wm) of a network, the fraction by which the number of smaller calls falls short of Wm.
146. $K$
   - on `ring-convolution`: $K$ (layout chunk width): The width of the address chunks used by the tape layout.
   - on [Tape layout for synthetic transforms](transform-layout.md): $K$ (chunk width): The number of bits in an address chunk.
147. $K$
   - on `ring-convolution`: $K$ (layout chunk width): The width of the address chunks used by the tape layout.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $K$ (later tensor line): The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
148. $K$
   - on `ring-convolution`: $K$ (layout chunk width): The width of the address chunks used by the tape layout.
   - on [Packed selected-bit addition](packed-bit-addition.md): $K$ (segment spacing): The spacing between selected positions, at least 6, which is the length of each segment.
149. $b$
   - on `multiplication-algorithm`: $b$ (digit width): The number of bits in one radix digit, the ceiling of log2 n.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $b$ (field digit count): The number of base-$q$ digits of a field.
150. $b$
   - on `multiplication-algorithm`: $b$ (digit width): The number of bits in one radix digit, the ceiling of log2 n.
   - on [Butterflies and the fast transform](butterfly.md): $b$ (lowest bit): The lowest bit of the output index m.
151. $b$
   - on `multiplication-algorithm`: $b$ (digit width): The number of bits in one radix digit, the ceiling of log2 n.
   - on [Tape layout for synthetic transforms](transform-layout.md): $b$ (leftover low bits): The number of low address bits of an axis left over after whole K-bit chunks.
152. $b$
   - on `multiplication-algorithm`: $b$ (digit width): The number of bits in one radix digit, the ceiling of log2 n.
   - on [Two-point kernel C](phase-kernel.md): $b$ (kernel coefficient b): The complex constant (1-i)/2, the coefficient of the bit flip in C.
153. $t_i$
   - on `multiplication-algorithm`: $t_i$ (padded axis length): The power-of-two length of axis i; their product is T.
   - on [Cyclic convolution](convolution.md): $t_i$ (axis length): The length of cyclic axis i.
154. $F_{\boldsymbol t}$
   - on `multiplication-algorithm`: $F_{\boldsymbol t}$ (padded-axis transform): The discrete Fourier transform on the axes t_i, normalized by 1/T.
   - on [Bluestein chirp identity](chirp.md): $F_{\boldsymbol t}$ (normalized transform): The normalized multidimensional discrete Fourier transform with axis lengths t.
155. $\mathcal M_{\mathbb C}$
   - on `multiplication-algorithm`: $\mathcal M_{\mathbb C}$ (normalized convolution): The normalized cyclic convolution f*g/T.
   - on [Phase twist](phase-twist.md): $\mathcal M_{\mathbb C}$ (complex convolution): The normalized complex cyclic convolution of two arrays.
156. $\mathcal A$
   - on `multiplication-algorithm`: $\mathcal A$ (input resampling map): The Gaussian resampling map applied first in the source transform.
   - on [Multidimensional transforms](multidim-transform.md): $\mathcal A$ (input map): The tensor product of the one-dimensional input maps A_i.
157. $\mathcal B_0$
   - on `multiplication-algorithm`: $\mathcal B_0$ (output resampling map): The resampling map applied after the chirp transform.
   - on [Multidimensional transforms](multidim-transform.md): $\mathcal B_0$ (output map): The tensor product of the one-dimensional output maps B_{0,i}.
158. $\gamma$
   - on `multiplication-algorithm`: $\gamma$ (resampling scale exponent): The exponent of the exact scale 2^gamma applied at the end of the source transform.
   - on [Multidimensional transforms](multidim-transform.md): $\gamma$ (scalar exponent): The total exponent 2d alpha^2 of the power of two multiplying the tensored identity.
159. $\gamma$
   - on `multiplication-algorithm`: $\gamma$ (resampling scale exponent): The exponent of the exact scale 2^gamma applied at the end of the source transform.
   - on [Linear exchange network with restored scratch wires](exchange-network.md): $\gamma$ (initial central values): The initial values of the central wires.
160. $R$
   - on `multiplication-algorithm`: $R$ (retained permutation): The retained coordinate permutation of the source axes.
   - on [Elementary stream operations](stream-ops.md): $R$ (row count): The number of rows in the array of item 4.
161. $R$
   - on `multiplication-algorithm`: $R$ (retained permutation): The retained coordinate permutation of the source axes.
   - on [Multidimensional transforms](multidim-transform.md): $R$ (source permutation): The tensor product of the source index permutations P_{s_i}; here not the scalar ring.
162. $R$
   - on `multiplication-algorithm`: $R$ (retained permutation): The retained coordinate permutation of the source axes.
   - on [Frames on wire arrays](array-frames.md): $R$ (scalar ring): The ring of scalars carried by the wires.
163. $R$
   - on `multiplication-algorithm`: $R$ (retained permutation): The retained coordinate permutation of the source axes.
   - on [Packed selected-bit addition](packed-bit-addition.md): $R$ (record bits): The number of bits in the record at each address.
164. $z$
   - on `multiplication-algorithm`: $z$ (pointwise product array): An array to which the opposite-sign source transform is applied.
   - on [Tape layout for synthetic transforms](transform-layout.md): $z$ (round input): The array entering a round.
165. $z$
   - on `multiplication-algorithm`: $z$ (pointwise product array): An array to which the opposite-sign source transform is applied.
   - on [Fast address-chunk interchange](address-interchange.md): $z$ (suffix): The part of an address after the second chunk.
166. $z$
   - on `multiplication-algorithm`: $z$ (pointwise product array): An array to which the opposite-sign source transform is applied.
   - on [Simultaneous butterfly layer](simultaneous-layer.md): $z$ (array): The array of records that the operators act on.
167. $z$
   - on `multiplication-algorithm`: $z$ (pointwise product array): An array to which the opposite-sign source transform is applied.
   - on [Retained permutation cancellation](retained-permutations.md): $z$ (vector): A vector of q complex entries being transformed.
168. $w$
   - on `multiplication-algorithm`: $w$ (scaled exact array): The exact array (u*v)/S that the computed array approximates.
   - on [Fast address-chunk interchange](address-interchange.md): $w$ (wire index): The index of an input wire of the network.
169. $w$
   - on `multiplication-algorithm`: $w$ (scaled exact array): The exact array (u*v)/S that the computed array approximates.
   - on [Packed selected-bit addition](packed-bit-addition.md): $w$ (second integer): The integer updated by lines 2, 4, 5 and 7, restored at the end.
170. $u$
   - on `multiplication-algorithm`: $u$ (first source array): In this page, the first source array obtained by applying Phi to the digits, not the integer.
   - on [Error tracking and exact recovery](precision-recovery.md): $u$ (scaled digit array): The array of scaled radix digits of the first input, each stored as its value times $2^{-b-2}$ (not the integer).
171. $u$
   - on `multiplication-algorithm`: $u$ (first source array): In this page, the first source array obtained by applying Phi to the digits, not the integer.
   - on [Discrete Fourier transform](dft.md): $u$ (input sequence): A sequence of q complex numbers to be transformed.
172. $u$
   - on `multiplication-algorithm`: $u$ (first source array): In this page, the first source array obtained by applying Phi to the digits, not the integer.
   - on [Multiplication as radix-digit convolution](radix-digit-reduction.md): $u$ (first input): The first of the two integers being multiplied.
173. $u$
   - on `multiplication-algorithm`: $u$ (first source array): In this page, the first source array obtained by applying Phi to the digits, not the integer.
   - on [Fast address-chunk interchange](address-interchange.md): $u$ (chunk width): The number of bits in each of the two interchanged address chunks.
174. $u$
   - on `multiplication-algorithm`: $u$ (first source array): In this page, the first source array obtained by applying Phi to the digits, not the integer.
   - on [Packed selected-bit addition](packed-bit-addition.md): $u$ (first integer): The integer updated by lines 1, 3, 6 and 8 of the eight additions.
175. $u$
   - on `multiplication-algorithm`: $u$ (first source array): In this page, the first source array obtained by applying Phi to the digits, not the integer.
   - on [Retained permutation cancellation](retained-permutations.md): $u$ (first array): A complex array (not an integer) in the resampling and convolution identities of this page.
176. $V$
   - on `cost-accounting`: $V$ (volume): The number of stored bits of the T coefficients of p bits, V=Tp.
   - on [Elementary stream operations](stream-ops.md): $V$ (array volume): The number of radix-q digits an array stores.
177. $V$
   - on `cost-accounting`: $V$ (volume): The number of stored bits of the T coefficients of p bits, V=Tp.
   - on [Fast address-chunk interchange](address-interchange.md): $V$ (array volume): The number of bits stored in the array.
178. $V$
   - on `cost-accounting`: $V$ (volume): The number of stored bits of the T coefficients of p bits, V=Tp.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $V$ (larger label): A label containing the label $U$ at the other end of an edge.
179. $V$
   - on `cost-accounting`: $V$ (volume): The number of stored bits of the T coefficients of p bits, V=Tp.
   - on [Parameter and prime-length choice](parameter-choice.md): $V$ (bit volume): The number of bits of the logical array the layer acts on.
180. $V$
   - on `cost-accounting`: $V$ (volume): The number of stored bits of the T coefficients of p bits, V=Tp.
   - on [Chinese-remainder address map](crt-map.md): $V$ (stream volume): The volume of the stream being moved, Tp bits.
181. $g_i$
   - on `cost-accounting`: $g_i$ (margin): The margin below one of the i-th dominant power of p, so the power is p^{1-g_i}.
   - on [Packed selected-bit addition](packed-bit-addition.md): $g_i$ (y guard): The guard value of the i-th segment of y, with u_i = 2 g_i + a_i.
182. $A$
   - on `cost-accounting`: $A$ (visit exponent): A fixed exponent such that the recursions make at most p^A visits in total.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $A$ (shear matrix): A rational m by m matrix, taken from a fixed finite set, that the shear applies.
183. $A$
   - on `cost-accounting`: $A$ (visit exponent): A fixed exponent such that the recursions make at most p^A visits in total.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $A$ (exposed factor space): The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
184. $A$
   - on `cost-accounting`: $A$ (visit exponent): A fixed exponent such that the recursions make at most p^A visits in total.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $A$ (ambient space): A finite-dimensional space with a nondegenerate form, containing the subspace P.
185. $A$
   - on `cost-accounting`: $A$ (visit exponent): A fixed exponent such that the recursions make at most p^A visits in total.
   - on [Simultaneous butterfly layer](simultaneous-layer.md): $A$ (chain length bound): A(e) bounds the number of arithmetic operations along a chain from an input to an intermediate coefficient.
186. $C$
   - on `cost-accounting`: $C$ (setup exponent): A fixed exponent such that descriptor setup per visit is at most p^C steps.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $C$ (second ambient space): A finite-dimensional space with a nondegenerate form, containing the subspace Q.
187. $C$
   - on `cost-accounting`: $C$ (setup exponent): A fixed exponent such that descriptor setup per visit is at most p^C steps.
   - on [Two-point kernel C](phase-kernel.md): $C$ (two-point kernel): The 2 by 2 matrix aI+bX.
188. $C$
   - on `cost-accounting`: $C$ (setup exponent): A fixed exponent such that descriptor setup per visit is at most p^C steps.
   - on [Gaussian resampling](gaussian-resampling.md): $C$ (coordinate selection): The map from C^t to C^s that selects coordinate q_j into position j.
189. $c$
   - on `main-result`: $c$ (chunk-width exponent): The fixed exponent giving the chunk width K = floor(d^c); not the machine constant.
   - on [Schönhage–Strassen optimality conjecture](conjecture.md): $c$ (machine constant): A positive constant, depending on the machine, in the lower bound c n log n.
190. $c$
   - on `main-result`: $c$ (chunk-width exponent): The fixed exponent giving the chunk width K = floor(d^c); not the machine constant.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $c$ (scaling integer): A fixed positive integer prime to q by which the target field is multiplied; not the machine constant.
191. $c$
   - on `main-result`: $c$ (chunk-width exponent): The fixed exponent giving the chunk width K = floor(d^c); not the machine constant.
   - on [Packed selected-bit addition](packed-bit-addition.md): $c$ (control bit): A bit, 0 or 1, that gates the eight additions.
192. $c$
   - on `main-result`: $c$ (chunk-width exponent): The fixed exponent giving the chunk width K = floor(d^c); not the machine constant.
   - on [Retained permutation cancellation](retained-permutations.md): $c$ (unit): An integer that is a unit modulo q, used to permute coordinates by z_{cj}.

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

Write the answer to `exegenius/tasks/0216-overloads.answer.json`, then run `exegenius submit 0216-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0216-overloads`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
