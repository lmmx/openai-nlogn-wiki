# exegenius task 0281-overloads

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the page that changes should do: use another letter, or say where the letter is used that it means something else there than on the other page. For the same thing, `note` may be empty.
- `change` is the page that changes. Leave it out for the later page. Give the earlier page's id when its use of the letter is the odd one out, for instance when the sources use the letter as the later page does, and the earlier page binds it on the page, not in a name. A page that other pages take the letter from keeps it and says where its meaning changes.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $T$
   - on `radix-digit-reduction`: $T$ (padded length): A power of two with 4n/b <= T < 8n/b, the padded length from parameter choice.
   - on [Cyclic convolution](convolution.md): $T$ (coefficient count): The total number of complex coefficients in an array.
2. $q$
   - on `radix-digit-reduction`: $q$ (digit count): The number of digits in each input.
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
3. $q$
   - on `stream-ops`: $q$ (radix): The radix: the number of values one digit can take (not a sequence length here).
   - on [Discrete Fourier transform](dft.md): $q$ (sequence length): The number of entries of a sequence.
4. $q$
   - on `stream-ops`: $q$ (radix): The radix: the number of values one digit can take (not a sequence length here).
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
5. $q$
   - on `controlled-shifts`: $q$ (prime radix): The prime radix of the stored digits.
   - on [Elementary stream operations](stream-ops.md): $q$ (radix): The radix: the number of values one digit can take (not a sequence length here).
6. $q$
   - on `controlled-shifts`: $q$ (prime radix): The prime radix of the stored digits.
   - on [Discrete Fourier transform](dft.md): $q$ (sequence length): The number of entries of a sequence.
7. $q$
   - on `controlled-shifts`: $q$ (prime radix): The prime radix of the stored digits.
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
8. $b$
   - on `controlled-shifts`: $b$ (field digit count): The number of base-q digits of a field.
   - on [Butterflies and the fast transform](butterfly.md): $b$ (lowest bit): The lowest bit of the output index m.
9. $B$
   - on `controlled-shifts`: $B$ (suffix digit count): The number of digits that follow the target field.
   - on [Elementary stream operations](stream-ops.md): $B$ (row length): The number of entries per row.
10. $j$
   - on `controlled-shifts`: $j$ (wrap count): The number of times cy wraps past Q.
   - on [Elementary stream operations](stream-ops.md): $j$ (digit value): A value of the chosen digit in the splitting example.
11. $a$
   - on `matrix-shear`: $a$ (rank of A): The rank of the rational matrix A.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $a$ (offset): The offset added to the target field, prepared from the control values.
12. $b$
   - on `matrix-shear`: $b$ (digits per field): The number of base-q digits in each field.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $b$ (field digit count): The number of base-q digits of a field.
13. $b$
   - on `matrix-shear`: $b$ (digits per field): The number of base-q digits in each field.
   - on [Butterflies and the fast transform](butterfly.md): $b$ (lowest bit): The lowest bit of the output index m.
14. $q$
   - on `matrix-shear`: $q$ (fixed odd prime): The fixed odd prime modulus base of the fields.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $q$ (prime radix): The prime radix of the stored digits.
15. $q$
   - on `matrix-shear`: $q$ (fixed odd prime): The fixed odd prime modulus base of the fields.
   - on [Elementary stream operations](stream-ops.md): $q$ (radix): The radix: the number of values one digit can take (not a sequence length here).
16. $q$
   - on `matrix-shear`: $q$ (fixed odd prime): The fixed odd prime modulus base of the fields.
   - on [Discrete Fourier transform](dft.md): $q$ (sequence length): The number of entries of a sequence.
17. $q$
   - on `matrix-shear`: $q$ (fixed odd prime): The fixed odd prime modulus base of the fields.
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
18. $b$
   - on `phase-kernel`: $b$ (kernel coefficient): The complex constant (1-i)/2, a coefficient of the kernel; not a bit index.
   - on [Butterflies and the fast transform](butterfly.md): $b$ (lowest bit): The lowest bit of the output index m.
19. $k$
   - on `crt-map`: $k$ (coefficient index): A single coefficient index, an exponent of x, not an index tuple.
   - on [Multidimensional transforms](multidim-transform.md): $k$ (output index tuple): An output index tuple shaped like j.
20. $T$
   - on `crt-map`: $T$ (padded record count): The number of padded records, the product of the axis lengths t_i.
   - on [Cyclic convolution](convolution.md): $T$ (coefficient count): The total number of complex coefficients in an array.
21. $t_i$
   - on `crt-map`: $t_i$ (padded axis length): The length of axis i after zero padding, either r/2 or r.
   - on [Cyclic convolution](convolution.md): $t_i$ (axis length): The length of cyclic axis i.
22. $k$
   - on `gaussian-resampling`: $k$ (coordinate index): A single coordinate index of a vector, not an index tuple.
   - on [Multidimensional transforms](multidim-transform.md): $k$ (output index tuple): An output index tuple shaped like j.
23. $j$
   - on `gaussian-resampling`: $j$ (coordinate index): A single coordinate index of a vector, not an index tuple.
   - on [Multidimensional transforms](multidim-transform.md): $j$ (index tuple): The tuple of coordinates (j_1,...,j_d) of an entry of the array.
24. $\alpha$
   - on `gaussian-resampling`: $\alpha$ (width parameter): An integer with 2<=alpha<sqrt p setting the width of the Gaussian weights.
   - on [Multidimensional transforms](multidim-transform.md): $\alpha$ (resampling parameter): An integer resampling parameter with 2<=alpha<sqrt p.
25. $t$
   - on `gaussian-resampling`: $t$ (padded length): The nearby larger transform length, a power of two, into which the length-s transform is resampled.
   - on [Butterflies and the fast transform](butterfly.md): $t$ (transform length): The number of positions in the sequence being transformed, a power of two.
26. $u$
   - on `retained-permutations`: $u$ (first array): A complex array, not an integer, transformed along the axes.
   - on [Discrete Fourier transform](dft.md): $u$ (input sequence): A sequence of q complex numbers to be transformed.
27. $L$
   - on `precision-recovery`: $L$ (log of padded length): The base-2 logarithm of the padded length $T$; not the linear map $L$ of the contractions page.
   - on [Contractions and bilinear contractions](contraction-maps.md): $L$ (linear map): A linear map whose norm bound is being defined.
28. $a$
   - on `precision-recovery`: $a$ (error size): The size of an error, counted in grid spacings $h_p$.
   - on [Bluestein chirp identity](chirp.md): $a$ (chirp): The chirp, a phase quadratic in the index.
29. $x$
   - on `precision-recovery`: $x$ (disk operand): An array in the unit disk to which a phase or chirp transform is applied; not the digit-polynomial variable.
   - on [Multiplication as radix-digit convolution](radix-digit-reduction.md): $x$ (polynomial variable): The indeterminate of the digit polynomials.
30. $u$
   - on `precision-recovery`: $u$ (scaled digit array): The array of scaled radix digits of the first input, each digit stored as its value times $2^{-b-2}$; not the integer.
   - on [Discrete Fourier transform](dft.md): $u$ (input sequence): A sequence of q complex numbers to be transformed.
31. $u$
   - on `precision-recovery`: $u$ (scaled digit array): The array of scaled radix digits of the first input, each digit stored as its value times $2^{-b-2}$; not the integer.
   - on [Multiplication as radix-digit convolution](radix-digit-reduction.md): $u$ (first input): The first of the two integers being multiplied.
32. $v$
   - on `precision-recovery`: $v$ (scaled digit array): The array of scaled radix digits of the second input, each digit stored as its value times $2^{-b-2}$; not the integer.
   - on [Multiplication as radix-digit convolution](radix-digit-reduction.md): $v$ (second input): The second of the two integers being multiplied.
33. $\tau$
   - on `parameter-choice`: $\tau$ (chunk-interchange exponent): The exponent in the cost of a chunk interchange.
   - on [Chinese-remainder address map](crt-map.md): $\tau$ (interchange exponent): A fixed exponent below 1 in the chunk-interchange time bound.
34. $V$
   - on `parameter-choice`: $V$ (bit volume): The bit volume on which the layer cost is measured.
   - on [Elementary stream operations](stream-ops.md): $V$ (array volume): The number of digits stored in the array.
35. $c$
   - on `parameter-choice`: $c$ (chunk-width exponent): The exponent of the address-chunk width (a new meaning of c).
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $c$ (scaling integer): A fixed positive integer prime to q, by which the field is multiplied.
36. $\delta$
   - on `parameter-choice`: $\delta$ (resampling slack): The slack in the resampling cost exponent.
   - on [Multidimensional transforms](multidim-transform.md): $\delta$ (time-bound slack): A fixed constant with 0<delta<1/8 that sets the slack in the exponent 3/2+delta of p in the time bound.
37. $q$
   - on `parameter-choice`: $q$ (interval integer): An integer in the interval (1-2eta)x < q <= (1-eta)x.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $q$ (prime radix): The prime radix of the stored digits.
38. $q$
   - on `parameter-choice`: $q$ (interval integer): An integer in the interval (1-2eta)x < q <= (1-eta)x.
   - on [Elementary stream operations](stream-ops.md): $q$ (radix): The radix: the number of values one digit can take (not a sequence length here).
39. $q$
   - on `parameter-choice`: $q$ (interval integer): An integer in the interval (1-2eta)x < q <= (1-eta)x.
   - on [Discrete Fourier transform](dft.md): $q$ (sequence length): The number of entries of a sequence.
40. $q$
   - on `parameter-choice`: $q$ (interval integer): An integer in the interval (1-2eta)x < q <= (1-eta)x.
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
41. $X$
   - on `subspace-labels`: $X$ (X bank): The bank of data wires $X_a$.
   - on [Linear exchange network with restored scratch wires](exchange-network.md): $X$ (first data bank): One of the two data banks, with entries X_a.
42. $Y$
   - on `subspace-labels`: $Y$ (Y bank): The bank of data wires $Y_a$.
   - on [Linear exchange network with restored scratch wires](exchange-network.md): $Y$ (second data bank): The other data bank, with entries Y_a.
43. $F$
   - on `rank-recurrence`: $F$ (time per unit volume): The running time of a call at a given parameter, divided by the volume of its stream.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $F$ (one-factor label space): The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
44. $F$
   - on `rank-recurrence`: $F$ (time per unit volume): The running time of a call at a given parameter, divided by the volume of its stream.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $F$ (base space): A space of dimension h with a nondegenerate form, whose triple power is the label space.
45. $j$
   - on `rank-recurrence`: $j$ (recursion depth): The number of recursion levels below the top call, indexing the terms of the unrolled sum.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $j$ (stage number): The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
46. $u$
   - on `address-interchange`: $u$ (chunk width): The number of bits in each of the two chunks.
   - on [Discrete Fourier transform](dft.md): $u$ (input sequence): A sequence of q complex numbers to be transformed.
47. $p$
   - on `address-interchange`: $p$ (address prefix): The prefix part of an address, before the first chunk.
   - on [Fixed-point Gaussian dyadic records](fixed-point.md): $p$ (fractional bits): The number of fractional bits of the grid on which stored values lie.
48. $h$
   - on `address-interchange`: $h$ (first chunk): The first of the two address chunks to be interchanged.
   - on [Butterflies and the fast transform](butterfly.md): $h$ (remaining index): The output index m with its lowest bit removed.
49. $h$
   - on `address-interchange`: $h$ (first chunk): The first of the two address chunks to be interchanged.
   - on [Linear exchange network with restored scratch wires](exchange-network.md): $h$ (ground-set size): The size of the ground set [h] whose three-element subsets index the banks.
50. $d$
   - on `address-interchange`: $d$ (second chunk): The second of the two address chunks to be interchanged.
   - on [Cyclic convolution](convolution.md): $d$ (axis count): The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
51. $q$
   - on `address-interchange`: $q$ (digit radix): The fixed prime radix of the digits.
   - on [Elementary stream operations](stream-ops.md): $q$ (radix): The radix: the number of values one digit can take (not a sequence length here).
52. $q$
   - on `address-interchange`: $q$ (digit radix): The fixed prime radix of the digits.
   - on [Discrete Fourier transform](dft.md): $q$ (sequence length): The number of entries of a sequence.
53. $q$
   - on `address-interchange`: $q$ (digit radix): The fixed prime radix of the digits.
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
54. $q$
   - on `address-interchange`: $q$ (digit radix): The fixed prime radix of the digits.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $q$ (fixed odd prime): The fixed odd prime modulus base of the fields.
55. $q$
   - on `address-interchange`: $q$ (digit radix): The fixed prime radix of the digits.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $q$ (prime radix): The prime radix of the stored digits.
56. $H$
   - on `address-interchange`: $H$ (first chunk value): The value of the first chunk, the target of the shear.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $H$ (target group): The first group of m fields, which receives AD.
57. $D$
   - on `address-interchange`: $D$ (second chunk value): The value of the second chunk, the source of the shear.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $D$ (source group): The second group of m fields, which is left unchanged.
58. $M$
   - on `address-interchange`: $M$ (vertex matrix): The rational m by m matrix carried by a vertex of the network.
   - on [Cyclic convolution](convolution.md): $M$ (address count): The number of cyclic addresses of an array, the product of the axis lengths.
59. $x$
   - on `address-interchange`: $x$ (stream row number): The row number within a role stream.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $x$ (vector of F): A vector of $F$, the first argument of the bilinear form.
60. $j$
   - on `address-interchange`: $j$ (level index): An index of recursion levels in the unrolled sum.
   - on [Elementary stream operations](stream-ops.md): $j$ (digit value): A value of the chosen digit in the splitting example.
61. $j$
   - on `address-interchange`: $j$ (level index): An index of recursion levels in the unrolled sum.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $j$ (wrap count): The number of times cy wraps past Q.
62. $j$
   - on `address-interchange`: $j$ (level index): An index of recursion levels in the unrolled sum.
   - on [Recursive power saving](rank-recurrence.md): $j$ (recursion depth): The number of recursion levels below the top call, indexing the terms of the unrolled sum.
63. $j$
   - on `address-interchange`: $j$ (level index): An index of recursion levels in the unrolled sum.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $j$ (stage number): The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
64. $v$
   - on `phase-frames`: $v$ (binary vector): A binary vector in F_2^m; on this page v is not a number of triples.
   - on [Linear exchange network with restored scratch wires](exchange-network.md): $v$ (number of triples): The number of three-element subsets of [h].
65. $E$
   - on `phase-frames`: $E$ (edge residual): The orthogonal complement of the tail label inside the head label of an edge; not a tensor factor.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $E$ (first space): The first of the two finite-dimensional vector spaces being tensored.
66. $k$
   - on `phase-frames`: $k$ (column count): The number of columns of data, tensored together; not a depth.
   - on [Fixed-point Gaussian dyadic records](fixed-point.md): $k$ (depth): The number of operations in sequence since the layer began that produced a value.
67. $u$
   - on `phase-frames`: $u$ (binary vector): A binary vector in F_2^m.
   - on [Discrete Fourier transform](dft.md): $u$ (input sequence): A sequence of q complex numbers to be transformed.
68. $D$
   - on `simultaneous-layer`: $D$ (selected chunk count): The number of selected address chunks, at most d.
   - on [Fast address-chunk interchange](address-interchange.md): $D$ (second chunk value): The value of the second chunk, the source of the shear.
69. $D$
   - on `simultaneous-layer`: $D$ (selected chunk count): The number of selected address chunks, at most d.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $D$ (source group): The second group of m fields, which is left unchanged.
70. $e$
   - on `simultaneous-layer`: $e$ (selected axis count): The number of selected axes in a group, e = mf.
   - on [Fast address-chunk interchange](address-interchange.md): $e$ (chunk digit count): The number of digits in each chunk.
71. $z$
   - on `simultaneous-layer`: $z$ (array): An array on which the diagonal operator acts.
   - on [Fast address-chunk interchange](address-interchange.md): $z$ (suffix): The part of the address after the second chunk.
72. $z$
   - on `simultaneous-layer`: $z$ (array): An array on which the diagonal operator acts.
   - on [Binary phase frames](phase-frames.md): $z$ (binary vector): A vector of F_2^m.
73. $E$
   - on `simultaneous-layer`: $E$ (invocation operation bound): A bound on the operations in one invocation of the network.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $E$ (first space): The first of the two finite-dimensional vector spaces being tensored.
74. $E$
   - on `simultaneous-layer`: $E$ (invocation operation bound): A bound on the operations in one invocation of the network.
   - on [Binary phase frames](phase-frames.md): $E$ (edge residual): The orthogonal complement of the tail label inside the head label of an edge; not a tensor factor.
75. $D$
   - on `transform-layout`: $D$ (transformed axes): The number of transformed axes, d-1.
   - on [Fast address-chunk interchange](address-interchange.md): $D$ (second chunk value): The value of the second chunk, the source of the shear.
76. $D$
   - on `transform-layout`: $D$ (transformed axes): The number of transformed axes, d-1.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $D$ (source group): The second group of m fields, which is left unchanged.
77. $D$
   - on `transform-layout`: $D$ (transformed axes): The number of transformed axes, d-1.
   - on [Simultaneous butterfly layer](simultaneous-layer.md): $D$ (selected chunk count): The number of selected address chunks, at most d.
78. $\tau$
   - on `transform-layout`: $\tau$ (interchange exponent): The exponent below 1 in the cost O(V u^tau) of a chunk interchange.
   - on [Fast address-chunk interchange](address-interchange.md): $\tau$ (saving exponent): The fixed exponent below 1 in the cost of the interchange.
79. $B$
   - on `transform-layout`: $B$ (bit reversal): The bit-reversal permutation applied along every axis.
   - on [Elementary stream operations](stream-ops.md): $B$ (row length): The number of entries per row.
80. $B$
   - on `transform-layout`: $B$ (bit reversal): The bit-reversal permutation applied along every axis.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $B$ (suffix digit count): The number of digits that follow the target field.
81. $b$
   - on `transform-layout`: $b$ (leftover low bits): The number of leftover low bits of an axis after whole chunks.
   - on [Butterflies and the fast transform](butterfly.md): $b$ (lowest bit): The lowest bit of the output index m.
82. $b$
   - on `transform-layout`: $b$ (leftover low bits): The number of leftover low bits of an axis after whole chunks.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $b$ (digits per field): The number of base-q digits in each field.
83. $b$
   - on `transform-layout`: $b$ (leftover low bits): The number of leftover low bits of an axis after whole chunks.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $b$ (field digit count): The number of base-q digits of a field.
84. $b$
   - on `transform-layout`: $b$ (leftover low bits): The number of leftover low bits of an axis after whole chunks.
   - on [Two-point kernel C](phase-kernel.md): $b$ (kernel coefficient): The complex constant (1-i)/2, a coefficient of the kernel; not a bit index.
85. $q$
   - on `transform-layout`: $q$ (whole chunks): The number of whole K-bit chunks of an axis.
   - on [Discrete Fourier transform](dft.md): $q$ (sequence length): The number of entries of a sequence.
86. $q$
   - on `transform-layout`: $q$ (whole chunks): The number of whole K-bit chunks of an axis.
   - on [Cyclic convolution](convolution.md): $q$ (sequence length): The number of entries in each of the two sequences being convolved.
87. $q$
   - on `transform-layout`: $q$ (whole chunks): The number of whole K-bit chunks of an axis.
   - on [Fast address-chunk interchange](address-interchange.md): $q$ (digit radix): The fixed prime radix of the digits.
88. $q$
   - on `transform-layout`: $q$ (whole chunks): The number of whole K-bit chunks of an axis.
   - on [Elementary stream operations](stream-ops.md): $q$ (radix): The radix: the number of values one digit can take (not a sequence length here).
89. $q$
   - on `transform-layout`: $q$ (whole chunks): The number of whole K-bit chunks of an axis.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $q$ (fixed odd prime): The fixed odd prime modulus base of the fields.
90. $q$
   - on `transform-layout`: $q$ (whole chunks): The number of whole K-bit chunks of an axis.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $q$ (prime radix): The prime radix of the stored digits.
91. $L$
   - on `transform-layout`: $L$ (layout permutation): The record permutation defined by the prefix moves and chunk exchanges.
   - on [Contractions and bilinear contractions](contraction-maps.md): $L$ (linear map): A linear map whose norm bound is being defined.
92. $L$
   - on `transform-layout`: $L$ (layout permutation): The record permutation defined by the prefix moves and chunk exchanges.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $L$ (total dimension loss): The total number of dimensions lost on decreasing edges.
93. $z$
   - on `transform-layout`: $z$ (round input): The array entering a round.
   - on [Fast address-chunk interchange](address-interchange.md): $z$ (suffix): The part of the address after the second chunk.
94. $z$
   - on `transform-layout`: $z$ (round input): The array entering a round.
   - on [Simultaneous butterfly layer](simultaneous-layer.md): $z$ (array): An array on which the diagonal operator acts.
95. $z$
   - on `transform-layout`: $z$ (round input): The array entering a round.
   - on [Binary phase frames](phase-frames.md): $z$ (binary vector): A vector of F_2^m.
96. $P$
   - on `ring-convolution`: $P$ (pointwise product): The pointwise product $uv/r$ of two arrays of ring elements, not a prefix count or a subspace.
   - on [Elementary stream operations](stream-ops.md): $P$ (prefix count): The number of prefix values in the array indexed by [P]x[R]x[B].
97. $P$
   - on `ring-convolution`: $P$ (pointwise product): The pointwise product $uv/r$ of two arrays of ring elements, not a prefix count or a subspace.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $P$ (earlier tensor line): The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
98. $P$
   - on `ring-convolution`: $P$ (pointwise product): The pointwise product $uv/r$ of two arrays of ring elements, not a prefix count or a subspace.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $P$ (subspace of A): A subspace of A, later taken nondegenerate.
99. $L$
   - on `ring-convolution`: $L$ (layout permutation): The permutation of records made by the tape layout, not a linear map, a loss or a chunk length.
   - on [Contractions and bilinear contractions](contraction-maps.md): $L$ (linear map): A linear map whose norm bound is being defined.
100. $L$
   - on `ring-convolution`: $L$ (layout permutation): The permutation of records made by the tape layout, not a linear map, a loss or a chunk length.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $L$ (total dimension loss): The total number of dimensions lost on decreasing edges.
101. $B$
   - on `ring-convolution`: $B$ (bit-reversal order): The bit-reversal order of records, not a complement, a level factor or a row length.
   - on [Tape layout for synthetic transforms](transform-layout.md): $B$ (bit reversal): The bit-reversal permutation applied along every axis.
102. $B$
   - on `ring-convolution`: $B$ (bit-reversal order): The bit-reversal order of records, not a complement, a level factor or a row length.
   - on [Elementary stream operations](stream-ops.md): $B$ (row length): The number of entries per row.
103. $B$
   - on `ring-convolution`: $B$ (bit-reversal order): The bit-reversal order of records, not a complement, a level factor or a row length.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $B$ (suffix digit count): The number of digits that follow the target field.
104. $B$
   - on `ring-convolution`: $B$ (bit-reversal order): The bit-reversal order of records, not a complement, a level factor or a row length.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $B$ (complement of P): The orthogonal complement of $P$ inside $A$.
105. $B$
   - on `ring-convolution`: $B$ (bit-reversal order): The bit-reversal order of records, not a complement, a level factor or a row length.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $B$ (orthogonal complement): The orthogonal complement of P in A.
106. $\eta$
   - on `ring-convolution`: $\eta$ (truncation error bound): The bound $\sqrt2\,2^{-p}$ on the change made by one truncation; not a relative deficit.
   - on [Recursive power saving](rank-recurrence.md): $\eta$ (relative rank deficit): The relative deficit (Wm-s)/(Wm) by which the number of smaller calls falls short of Wm.
107. $K$
   - on `ring-convolution`: $K$ (layout chunk width): The width in bits of an address chunk in the tape layout; not a tensor line or a segment spacing.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $K$ (later tensor line): The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
108. $b$
   - on `multiplication-algorithm`: $b$ (digit width): The number of bits in one radix digit, not a lowest bit or kernel coefficient.
   - on [Multiplication as radix-digit convolution](radix-digit-reduction.md): $b$ (digit bits): The number of bits in one radix-2^b digit.
109. $b$
   - on `multiplication-algorithm`: $b$ (digit width): The number of bits in one radix digit, not a lowest bit or kernel coefficient.
   - on [Controlled shifts and rational scalings](controlled-shifts.md): $b$ (field digit count): The number of base-q digits of a field.
110. $b$
   - on `multiplication-algorithm`: $b$ (digit width): The number of bits in one radix digit, not a lowest bit or kernel coefficient.
   - on [Butterflies and the fast transform](butterfly.md): $b$ (lowest bit): The lowest bit of the output index m.
111. $b$
   - on `multiplication-algorithm`: $b$ (digit width): The number of bits in one radix digit, not a lowest bit or kernel coefficient.
   - on [Tape layout for synthetic transforms](transform-layout.md): $b$ (leftover low bits): The number of leftover low bits of an axis after whole chunks.
112. $b$
   - on `multiplication-algorithm`: $b$ (digit width): The number of bits in one radix digit, not a lowest bit or kernel coefficient.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $b$ (digits per field): The number of base-q digits in each field.
113. $b$
   - on `multiplication-algorithm`: $b$ (digit width): The number of bits in one radix digit, not a lowest bit or kernel coefficient.
   - on [Two-point kernel C](phase-kernel.md): $b$ (kernel coefficient): The complex constant (1-i)/2, a coefficient of the kernel; not a bit index.
114. $u$
   - on `multiplication-algorithm`: $u$ (first source array): The array obtained by applying Phi to the scaled digits of the first input; not an integer.
   - on [Error tracking and exact recovery](precision-recovery.md): $u$ (scaled digit array): The array of scaled radix digits of the first input, each digit stored as its value times $2^{-b-2}$; not the integer.
115. $u$
   - on `multiplication-algorithm`: $u$ (first source array): The array obtained by applying Phi to the scaled digits of the first input; not an integer.
   - on [Discrete Fourier transform](dft.md): $u$ (input sequence): A sequence of q complex numbers to be transformed.
116. $u$
   - on `multiplication-algorithm`: $u$ (first source array): The array obtained by applying Phi to the scaled digits of the first input; not an integer.
   - on [Multiplication as radix-digit convolution](radix-digit-reduction.md): $u$ (first input): The first of the two integers being multiplied.
117. $u$
   - on `multiplication-algorithm`: $u$ (first source array): The array obtained by applying Phi to the scaled digits of the first input; not an integer.
   - on [Fast address-chunk interchange](address-interchange.md): $u$ (chunk width): The number of bits in each of the two chunks.
118. $u$
   - on `multiplication-algorithm`: $u$ (first source array): The array obtained by applying Phi to the scaled digits of the first input; not an integer.
   - on [Binary phase frames](phase-frames.md): $u$ (binary vector): A binary vector in F_2^m.
119. $u$
   - on `multiplication-algorithm`: $u$ (first source array): The array obtained by applying Phi to the scaled digits of the first input; not an integer.
   - on [Retained permutation cancellation](retained-permutations.md): $u$ (first array): A complex array, not an integer, transformed along the axes.
120. $v$
   - on `multiplication-algorithm`: $v$ (second source array): The array obtained by applying Phi to the scaled digits of the second input; not an integer.
   - on [Error tracking and exact recovery](precision-recovery.md): $v$ (scaled digit array): The array of scaled radix digits of the second input, each digit stored as its value times $2^{-b-2}$; not the integer.
121. $v$
   - on `multiplication-algorithm`: $v$ (second source array): The array obtained by applying Phi to the scaled digits of the second input; not an integer.
   - on [Multiplication as radix-digit convolution](radix-digit-reduction.md): $v$ (second input): The second of the two integers being multiplied.
122. $v$
   - on `multiplication-algorithm`: $v$ (second source array): The array obtained by applying Phi to the scaled digits of the second input; not an integer.
   - on [Linear exchange network with restored scratch wires](exchange-network.md): $v$ (number of triples): The number of three-element subsets of [h].
123. $v$
   - on `multiplication-algorithm`: $v$ (second source array): The array obtained by applying Phi to the scaled digits of the second input; not an integer.
   - on [Binary phase frames](phase-frames.md): $v$ (binary vector): A binary vector in F_2^m; on this page v is not a number of triples.
124. $v$
   - on `multiplication-algorithm`: $v$ (second source array): The array obtained by applying Phi to the scaled digits of the second input; not an integer.
   - on [Retained permutation cancellation](retained-permutations.md): $v$ (second array): A complex array, not an integer, transformed along the axes.
125. $z$
   - on `multiplication-algorithm`: $z$ (pointwise product array): An array of complex numbers fed to the opposite-sign procedure; in step 3 the truncated pointwise product of the two transforms.
   - on [Error tracking and exact recovery](precision-recovery.md): $z$ (truncated product): The truncated pointwise product of the two computed source transforms.
126. $z$
   - on `multiplication-algorithm`: $z$ (pointwise product array): An array of complex numbers fed to the opposite-sign procedure; in step 3 the truncated pointwise product of the two transforms.
   - on [Tape layout for synthetic transforms](transform-layout.md): $z$ (round input): The array entering a round.
127. $z$
   - on `multiplication-algorithm`: $z$ (pointwise product array): An array of complex numbers fed to the opposite-sign procedure; in step 3 the truncated pointwise product of the two transforms.
   - on [Fast address-chunk interchange](address-interchange.md): $z$ (suffix): The part of the address after the second chunk.
128. $z$
   - on `multiplication-algorithm`: $z$ (pointwise product array): An array of complex numbers fed to the opposite-sign procedure; in step 3 the truncated pointwise product of the two transforms.
   - on [Simultaneous butterfly layer](simultaneous-layer.md): $z$ (array): An array on which the diagonal operator acts.
129. $z$
   - on `multiplication-algorithm`: $z$ (pointwise product array): An array of complex numbers fed to the opposite-sign procedure; in step 3 the truncated pointwise product of the two transforms.
   - on [Binary phase frames](phase-frames.md): $z$ (binary vector): A vector of F_2^m.
130. $z$
   - on `multiplication-algorithm`: $z$ (pointwise product array): An array of complex numbers fed to the opposite-sign procedure; in step 3 the truncated pointwise product of the two transforms.
   - on [Retained permutation cancellation](retained-permutations.md): $z$ (input vector): A vector of q complex entries to which the transform is applied.
131. $w$
   - on `multiplication-algorithm`: $w$ (scaled exact array): The exact array (u*v)/S that the computed array after step 4 approximates.
   - on [Error tracking and exact recovery](precision-recovery.md): $w$ (first scaled result): The convolution $(u*v)/S$ of the digit arrays divided by $S$, whose scaling by $2^{2b+4}S$ gives the integer coefficients.
132. $w$
   - on `multiplication-algorithm`: $w$ (scaled exact array): The exact array (u*v)/S that the computed array after step 4 approximates.
   - on [Fast address-chunk interchange](address-interchange.md): $w$ (wire index): The index of an input wire of the network.
133. $w$
   - on `multiplication-algorithm`: $w$ (scaled exact array): The exact array (u*v)/S that the computed array after step 4 approximates.
   - on [Binary phase frames](phase-frames.md): $w$ (binary vector): A vector of F_2^m.
134. $w$
   - on `multiplication-algorithm`: $w$ (scaled exact array): The exact array (u*v)/S that the computed array after step 4 approximates.
   - on [Retained permutation cancellation](retained-permutations.md): $w$ (summation index): The summation index in the Fourier sum.
135. $R$
   - on `multiplication-algorithm`: $R$ (retained permutation): The permutation of coordinates retained inside the exact source transform.
   - on [Elementary stream operations](stream-ops.md): $R$ (row count): The number of rows in each prefix (not the scalar ring).
136. $R$
   - on `multiplication-algorithm`: $R$ (retained permutation): The permutation of coordinates retained inside the exact source transform.
   - on [Multidimensional transforms](multidim-transform.md): $R$ (source permutation): The tensor product of the source index permutations P_{s_i}; here not the scalar ring.
137. $R$
   - on `multiplication-algorithm`: $R$ (retained permutation): The permutation of coordinates retained inside the exact source transform.
   - on [Frames on wire arrays](array-frames.md): $R$ (scalar ring): The ring of scalars carried by the wires.
138. $\gamma$
   - on `multiplication-algorithm`: $\gamma$ (scale exponent): The exponent of the power-of-two scale that resampling introduces.
   - on [Multidimensional transforms](multidim-transform.md): $\gamma$ (scalar exponent): The total exponent 2d alpha^2 of the power of two multiplying the tensored identity.
139. $V$
   - on `cost-accounting`: $V$ (volume): The number of stored bits of T coefficients of p bits each, Theta(n).
   - on [Elementary stream operations](stream-ops.md): $V$ (array volume): The number of digits stored in the array.
140. $V$
   - on `cost-accounting`: $V$ (volume): The number of stored bits of T coefficients of p bits each, Theta(n).
   - on [Fast address-chunk interchange](address-interchange.md): $V$ (array volume): The number of bits stored in the array.
141. $V$
   - on `cost-accounting`: $V$ (volume): The number of stored bits of T coefficients of p bits each, Theta(n).
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $V$ (larger label): A label containing the label $U$ at the other end of an edge.
142. $V$
   - on `cost-accounting`: $V$ (volume): The number of stored bits of T coefficients of p bits each, Theta(n).
   - on [Parameter and prime-length choice](parameter-choice.md): $V$ (bit volume): The bit volume on which the layer cost is measured.
143. $A$
   - on `cost-accounting`: $A$ (visit exponent): A fixed exponent such that the total number of visits is at most p^A.
   - on [Matrix shear by triangular factorization](matrix-shear.md): $A$ (shear matrix): The rational m by m matrix whose shear is performed.
144. $A$
   - on `cost-accounting`: $A$ (visit exponent): A fixed exponent such that the total number of visits is at most p^A.
   - on [Nested subspace labels and rank deficit](subspace-labels.md): $A$ (exposed factor space): The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
145. $A$
   - on `cost-accounting`: $A$ (visit exponent): A fixed exponent such that the total number of visits is at most p^A.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $A$ (ambient space): A finite-dimensional space with a nondegenerate form, containing the subspace P.
146. $C$
   - on `cost-accounting`: $C$ (setup exponent): A fixed exponent such that descriptor setup per visit takes at most p^C steps.
   - on [Tensor products of subspaces](tensor-product-of-spaces.md): $C$ (second ambient space): A finite-dimensional space with a nondegenerate form, containing the subspace Q.
147. $C$
   - on `cost-accounting`: $C$ (setup exponent): A fixed exponent such that descriptor setup per visit takes at most p^C steps.
   - on [Two-point kernel C](phase-kernel.md): $C$ (two-point kernel): The two-point kernel aI + bX.
148. $C$
   - on `cost-accounting`: $C$ (setup exponent): A fixed exponent such that descriptor setup per visit takes at most p^C steps.
   - on [Gaussian resampling](gaussian-resampling.md): $C$ (selection map): The map from length-t to length-s vectors that picks coordinate q_j for each j.

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

Write the answer to `exegenius/tasks/0281-overloads.answer.json`, then run `exegenius submit 0281-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0281-overloads`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
