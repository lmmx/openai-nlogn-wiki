# exegenius task 0617-overloads

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Check the notation of an explanatory wiki for letters used with two meanings. Each candidate below is a symbol that a page binds, and that a page or concept name it builds on also binds. A reader arriving from the earlier page brings the earlier meaning with them.

- For each candidate, say whether the two bindings denote the same thing (`same: true`), even if worded differently ("number of digits" and "digit count"), or different things (`same: false`, as for a radix and a digit count).
- For different things, say in `note` what the later page should do: use another letter, or say where the letter is used that it means something else here than on the earlier page. For the same thing, `note` may be empty.
- Read the pages in `exegenius/pages/<id>.md` where the bindings alone do not settle it.
- Give a verdict for every candidate.

## Candidates

1. $n$
   - on `convolution`: $n$ (entries per input): The number of entries in each input sequence.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $n$ (input length): The number of bits in each of the two inputs $x$ and $y$.
2. $n$
   - on `convolution`: $n$ (entries per input): The number of entries in each input sequence.
   - on [Running time cost](running-time-cost.md): $n$ (input length): The number of cells that hold the input, which is the argument of the running time cost.
3. $V$
   - on `array`: $V$ (stored bit volume): The number of stored data bits in an array, the volume in which cost bounds are stated.
   - on [Payload](payload.md): $V$ (stream volume): The number of bits stored in the stream, which the time bound counts.
4. $s$
   - on `supremum`: $s$ (positive integer index): A positive integer index, the exponent in each element $1-2^{-s}$ of the example set.
   - on [Array norm](array-norm.md): $s$ (coefficient index): The index of a coefficient of a ring element, running from 0 to r-1.
5. $L$
   - on `supremum`: $L$ (linear map): A linear map, meaning a map that preserves sums and scalar multiples, whose operator norm is taken.
   - on [Payload](payload.md): $L$ (chunk width): The width, in address bits, of an address chunk.
6. $u$
   - on `supremum`: $u$ (input vector): One input vector in the supremum defining the operator norm, a finite list of complex numbers.
   - on [Array norm](array-norm.md): $u$ (entry): An entry of the array X, whose modulus is taken.
7. $s$
   - on `mixed-radix-digits`: $s$ (common length): The common length of every place, which is also the base; it counts the digit values.
   - on [Telescoping identity](telescoping-identity.md): $s$ (first position): The first position of a sum over positions, the lower limit of the sum.
8. $i$
   - on `discrete-fourier-transform`: $i$ (imaginary unit): The imaginary unit, the complex number whose square is $-1$, used in this page in place of the convolution page's input position $i$.
   - on [Linear algebra basics](linear-algebra-basics.md): $i$ (row index): The index of a row of a matrix, running from 1 to m.
9. $i$
   - on `discrete-fourier-transform`: $i$ (imaginary unit): The imaginary unit, the complex number whose square is $-1$, used in this page in place of the convolution page's input position $i$.
   - on [Convolution](convolution.md): $i$ (input position in a): The position of an entry of $a$.
10. $i$
   - on `transform-axis`: $i$ (axis index): An index naming one axis, running from 1 to D.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $i$ (imaginary unit): The imaginary unit, the complex number whose square is $-1$, used in this page in place of the convolution page's input position $i$.
11. $i$
   - on `transform-axis`: $i$ (axis index): An index naming one axis, running from 1 to D.
   - on [Linear algebra basics](linear-algebra-basics.md): $i$ (row index): The index of a row of a matrix, running from 1 to m.
12. $i$
   - on `transform-axis`: $i$ (axis index): An index naming one axis, running from 1 to D.
   - on [Convolution](convolution.md): $i$ (input position in a): The position of an entry of $a$.
13. $s$
   - on `transform-axis`: $s$ (coefficient count): A power of two that is the number of coefficients of the stored polynomial, which is also the length of its axis.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $s$ (input index): An integer index running over $0, 1, \ldots, q-1$ that labels an input coordinate $f_s$.
14. $\rho$
   - on `synthetic-transforms`: $\rho$ (coefficient position): The position of a coefficient in a record, running from 0 to r-1.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\rho$ (exponent): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
15. $\sigma$
   - on `synthetic-transforms`: $\sigma$ (shift count): The number of places a shift moves each coefficient.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
16. $f$
   - on `synthetic-transforms`: $f$ (input list): The list of $N$ records that the transform takes as input.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $f$ (input vector): A vector of $q$ complex numbers, the input to the transform, with coordinates $f_0, \ldots, f_{q-1}$.
17. $j$
   - on `synthetic-transforms`: $j$ (entry index): The index that numbers the entries of a list, running from $0$ to $N-1$.
   - on [Linear algebra basics](linear-algebra-basics.md): $j$ (coordinate index): The index of a coordinate of a vector, running from 1 to m.
18. $j$
   - on `synthetic-transforms`: $j$ (entry index): The index that numbers the entries of a list, running from $0$ to $N-1$.
   - on [Convolution](convolution.md): $j$ (input position in b): The position of an entry of $b$.
19. $\eta$
   - on `synthetic-transforms`: $\eta$ (half-size): The number of positions in each half of a block at a level of the transform.
   - on [Linear algebra basics](linear-algebra-basics.md): $\eta$ (scalar): A scalar in F multiplying a vector.
20. $\gamma$
   - on `synthetic-transforms`: $\gamma$ (block offset): The position within a block at which a butterfly pair starts.
   - on [Linear algebra basics](linear-algebra-basics.md): $\gamma$ (scalar): A scalar in F multiplying a vector.
21. $L$
   - on `linear-contraction`: $L$ (linear map): A linear map from vectors in C^m to vectors in C^{m'} whose contraction property is tested.
   - on [Payload](payload.md): $L$ (chunk width): The width, in address bits, of an address chunk.
22. $\eta$
   - on `linear-contraction`: $\eta$ (carried error): The error vector carried by the computed input, so that the computed input is x + η.
   - on [Linear algebra basics](linear-algebra-basics.md): $\eta$ (scalar): A scalar in F multiplying a vector.
23. $V$
   - on `bilinear-map`: $V$ (second argument space): The vector space that the second argument of the bilinear map ranges over.
   - on [Array](array.md): $V$ (stored bit volume): The number of stored data bits in an array, the volume in which cost bounds are stated.
24. $V$
   - on `bilinear-map`: $V$ (second argument space): The vector space that the second argument of the bilinear map ranges over.
   - on [Payload](payload.md): $V$ (stream volume): The number of bits stored in the stream, which the time bound counts.
25. $V$
   - on `bilinear-map`: $V$ (second argument space): The vector space that the second argument of the bilinear map ranges over.
   - on [Directed graph](directed-graph.md): $V$ (vertex set): The set of vertices of the directed graph, the points that edges join.
26. $\gamma$
   - on `coprime`: $\gamma$ (first integer): One of two integers, not both zero, whose gcd is taken.
   - on [Linear algebra basics](linear-algebra-basics.md): $\gamma$ (scalar): A scalar in F multiplying a vector.
27. $\rho$
   - on `coprime`: $\rho$ (second integer): The other of two integers, not both zero, whose gcd is taken.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\rho$ (exponent): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
28. $\sigma$
   - on `coprime`: $\sigma$ (member index): An index running over 1 to J, numbering the family members.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
29. $G$
   - on `coprime`: $G$ (transform group): The product group Z/f_1 times ... times Z/f_J, with tuples added entrywise.
   - on [Directed graph](directed-graph.md): $G$ (directed graph): The directed graph, written as the pair of its vertex set V and its edge set E.
30. $\rho$
   - on `bezout-identity`: $\rho$ (Bézout coefficient of β): The integer multiplying β in the combination βρ+γσ that equals gcd(β,γ).
   - on [Coprime](coprime.md): $\rho$ (second integer): The other of two integers, not both zero, whose gcd is taken.
31. $\rho$
   - on `bezout-identity`: $\rho$ (Bézout coefficient of β): The integer multiplying β in the combination βρ+γσ that equals gcd(β,γ).
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\rho$ (exponent): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
32. $\sigma$
   - on `bezout-identity`: $\sigma$ (Bézout coefficient of γ): The integer multiplying γ in the combination βρ+γσ that equals gcd(β,γ).
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
33. $\sigma$
   - on `bezout-identity`: $\sigma$ (Bézout coefficient of γ): The integer multiplying γ in the combination βρ+γσ that equals gcd(β,γ).
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
34. $\xi$
   - on `bezout-identity`: $\xi$ (least positive combination): The least positive value of βρ'+γσ' over all integers ρ' and σ'.
   - on [Coprime](coprime.md): $\xi$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the first of the two Bezout coefficients.
35. $f$
   - on `bezout-identity`: $f$ (quotient): The integer quotient in the division of β by ξ.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $f$ (input vector): A vector of $q$ complex numbers, the input to the transform, with coordinates $f_0, \ldots, f_{q-1}$.
36. $t$
   - on `bezout-identity`: $t$ (family parameter): An arbitrary integer labelling one pair of coefficients.
   - on [Convolution](convolution.md): $t$ (output position): The position of an entry of the convolution output.
37. $\rho$
   - on `cyclic-group`: $\rho$ (generator): An element of a group, the base of its powers; when its powers are all the elements, it is the generator.
   - on [Coprime](coprime.md): $\rho$ (second integer): The other of two integers, not both zero, whose gcd is taken.
38. $\rho$
   - on `cyclic-group`: $\rho$ (generator): An element of a group, the base of its powers; when its powers are all the elements, it is the generator.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\rho$ (exponent): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
39. $W$
   - on `cyclic-group`: $W$ (cyclic group order): The number of elements of the cyclic group $C_W$, which counts its distinct powers of the generator.
   - on [Coprime](coprime.md): $W$ (family product): The product f_1 times f_2 up to f_J, which is the least positive integer divisible by every member.
40. $\xi$
   - on `cyclic-group`: $\xi$ (exponent): An integer to which the generator is raised, giving the power $\rho^\xi$.
   - on [Coprime](coprime.md): $\xi$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the first of the two Bezout coefficients.
41. $\sigma$
   - on `cyclic-group`: $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
42. $\sigma$
   - on `cyclic-group`: $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
43. $G$
   - on `order-of-element`: $G$ (group): The group in which the order of sigma is taken, a set with an associative operation, an identity, and inverses.
   - on [Coprime](coprime.md): $G$ (transform group): The product group Z/f_1 times ... times Z/f_J, with tuples added entrywise.
44. $G$
   - on `order-of-element`: $G$ (group): The group in which the order of sigma is taken, a set with an associative operation, an identity, and inverses.
   - on [Directed graph](directed-graph.md): $G$ (directed graph): The directed graph, written as the pair of its vertex set V and its edge set E.
45. $\sigma$
   - on `order-of-element`: $\sigma$ (element): An element of the group G whose powers are taken.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
46. $\sigma$
   - on `order-of-element`: $\sigma$ (element): An element of the group G whose powers are taken.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
47. $\sigma$
   - on `order-of-element`: $\sigma$ (element): An element of the group G whose powers are taken.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
48. $\rho$
   - on `order-of-element`: $\rho$ (order): The least positive integer with sigma to the power rho equal to 1; it counts the distinct powers of sigma.
   - on [Cyclic group](cyclic-group.md): $\rho$ (generator): An element of a group, the base of its powers; when its powers are all the elements, it is the generator.
49. $\rho$
   - on `order-of-element`: $\rho$ (order): The least positive integer with sigma to the power rho equal to 1; it counts the distinct powers of sigma.
   - on [Coprime](coprime.md): $\rho$ (second integer): The other of two integers, not both zero, whose gcd is taken.
50. $\rho$
   - on `order-of-element`: $\rho$ (order): The least positive integer with sigma to the power rho equal to 1; it counts the distinct powers of sigma.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\rho$ (exponent): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
51. $x$
   - on `order-of-element`: $x$ (indeterminate): The indeterminate of the ring C[x] modulo x^S minus 1, whose image the map sends to a product of axis indeterminates.
   - on [Linear algebra basics](linear-algebra-basics.md): $x$ (vector): A vector in a vector space, changed from earlier pages.
52. $x$
   - on `order-of-element`: $x$ (indeterminate): The indeterminate of the ring C[x] modulo x^S minus 1, whose image the map sends to a product of axis indeterminates.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $x$ (first input): The first binary input string, of length $n$.
53. $x_i$
   - on `order-of-element`: $x_i$ (axis indeterminate): The indeterminate of axis i, the variable of the i-th cyclic factor of the target ring.
   - on [Transform axis](transform-axis.md): $x_i$ (axis coordinate): The coordinate of an address along axis i.
54. $\tau$
   - on `diagonal-scaling`: $\tau$ (scalar family): A family of scalars $\tau_\iota$ in $F$, one for each label, which defines a diagonal scaling.
   - on [Payload](payload.md): $\tau$ (fixed exponent): A fixed exponent strictly between 0 and 1 that sets the power of L in the time bound.
55. $f$
   - on `frequency-domain`: $f$ (sequence): A sequence $f=(f_0,\ldots,f_{q-1})$ of $q$ complex numbers, whose frequency domain is taken.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $f$ (input vector): A vector of $q$ complex numbers, the input to the transform, with coordinates $f_0, \ldots, f_{q-1}$.
56. $\sigma$
   - on `frequency-domain`: $\sigma$ (first input position): The position of an entry of the first input sequence $a$ in the convolution sum, running from $0$ to $q-1$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
57. $\rho$
   - on `frequency-domain`: $\rho$ (second input position): The position of an entry of the second input sequence $b$ in the convolution sum, running from $0$ to $q-1$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\rho$ (exponent): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
58. $V$
   - on `projection-along-subspace`: $V$ (larger nested subspace): A nondegenerate subspace containing $U$, the larger of two nested labels.
   - on [Directed graph](directed-graph.md): $V$ (vertex set): The set of vertices of the directed graph, the points that edges join.
59. $V$
   - on `projection-along-subspace`: $V$ (larger nested subspace): A nondegenerate subspace containing $U$, the larger of two nested labels.
   - on [Array](array.md): $V$ (stored bit volume): The number of stored data bits in an array, the volume in which cost bounds are stated.
60. $V$
   - on `projection-along-subspace`: $V$ (larger nested subspace): A nondegenerate subspace containing $U$, the larger of two nested labels.
   - on [Payload](payload.md): $V$ (stream volume): The number of bits stored in the stream, which the time bound counts.
61. $V$
   - on `linear-functional`: $V$ (vector space): The vector space over F whose vectors a linear functional takes as input.
   - on [Directed graph](directed-graph.md): $V$ (vertex set): The set of vertices of the directed graph, the points that edges join.
62. $V$
   - on `linear-functional`: $V$ (vector space): The vector space over F whose vectors a linear functional takes as input.
   - on [Array](array.md): $V$ (stored bit volume): The number of stored data bits in an array, the volume in which cost bounds are stated.
63. $V$
   - on `linear-functional`: $V$ (vector space): The vector space over F whose vectors a linear functional takes as input.
   - on [Payload](payload.md): $V$ (stream volume): The number of bits stored in the stream, which the time bound counts.
64. $\xi$
   - on `bijection`: $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
65. $W$
   - on `permutation`: $W$ (position set): The finite set of positions on which a permutation acts.
   - on [Bijection](bijection.md): $W$ (target set): The set that the map $f$ sends its inputs into, the set of outputs.
66. $\sigma$
   - on `permutation`: $\sigma$ (permutation): The map from W to W that sends each position to its new position.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
67. $\xi$
   - on `permutation`: $\xi$ (address): The position of one entry of an array.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
68. $\xi$
   - on `permutation`: $\xi$ (address): The position of one entry of an array.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
69. $G$
   - on `permutation`: $G$ (array): An array whose entries are stored at addresses.
   - on [Bijection](bijection.md): $G$ (singled-out set): A subset of the source set $U$ singled out by the argument, which is where two bijections may differ: the bad addresses.
70. $\alpha$
   - on `permutation`: $\alpha$ (first entry): The entry of the sequence at position 1.
   - on [Address](address.md): $\alpha$ (address string): A binary string of $d$ bits that labels one entry of the array.
71. $\rho$
   - on `linear-network-frames`: $\rho$ (role permutation): The permutation of roles that sends each input role to an output role.
   - on [Address field](address-field.md): $\rho$ (field width): The number of bits in each of the two fields being interchanged, a count of bit positions.
72. $\sigma$
   - on `linear-network-frames`: $\sigma$ (output role): An output role of the network.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
73. $\sigma$
   - on `linear-network-frames`: $\sigma$ (output role): An output role of the network.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
74. $L$
   - on `linear-network-frames`: $L$ (route length): The number of edges on a route, so that the route has $L+1$ vertices.
   - on [Payload](payload.md): $L$ (chunk width): The width, in address bits, of an address chunk.
75. $G$
   - on `linear-network-frames`: $G$ (pointwise gate): A pointwise linear gate, which combines its inputs the same way at every address.
   - on [Permutation](permutation.md): $G$ (array): An array whose entries are stored at addresses.
76. $G$
   - on `linear-network-frames`: $G$ (pointwise gate): A pointwise linear gate, which combines its inputs the same way at every address.
   - on [Bijection](bijection.md): $G$ (singled-out set): A subset of the source set $U$ singled out by the argument, which is where two bijections may differ: the bad addresses.
77. $G$
   - on `linear-network-frames`: $G$ (pointwise gate): A pointwise linear gate, which combines its inputs the same way at every address.
   - on [Directed graph](directed-graph.md): $G$ (directed graph): The directed graph, written as the pair of its vertex set V and its edge set E.
78. $t$
   - on `linear-network-frames`: $t$ (gate input count): The number of input arrays that the gate $G$ takes.
   - on [Integer](integer.md): $t$ (indeterminate): A formal variable of polynomials, which is not a number.
79. $L$
   - on `logical-array`: $L$ (route length): The number of edges on a route, so the route has $L+1$ vertices.
   - on [Payload](payload.md): $L$ (chunk width): The width, in address bits, of an address chunk.
80. $\sigma$
   - on `cyclic-shift`: $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
81. $\sigma$
   - on `cyclic-shift`: $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
82. $\xi$
   - on `butterfly`: $\xi$ (first input value): The first of the two input values of the butterfly.
   - on [Permutation](permutation.md): $\xi$ (address): The position of one entry of an array.
83. $\xi$
   - on `butterfly`: $\xi$ (first input value): The first of the two input values of the butterfly.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
84. $\xi$
   - on `butterfly`: $\xi$ (first input value): The first of the two input values of the butterfly.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
85. $\zeta$
   - on `butterfly`: $\zeta$ (second input value): The second of the two input values of the butterfly.
   - on [Cyclic shift](cyclic-shift.md): $\zeta$ (position): A position in the block, numbered from 0 to J-1.
86. $\sigma$
   - on `butterfly`: $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
87. $\sigma$
   - on `butterfly`: $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
88. $\sigma$
   - on `butterfly`: $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
89. $\sigma$
   - on `butterfly`: $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
90. $b$
   - on `radix-digit-convolution`: $b$ (digit width): The number of bits in each digit of an input.
   - on [Integer](integer.md): $b$ (base): The base (radix) of a digit representation, an integer at least 2.
91. $b$
   - on `radix-digit-convolution`: $b$ (digit width): The number of bits in each digit of an input.
   - on [Convolution](convolution.md): $b$ (second input sequence): The second of the two input sequences, of length $n$.
92. $J$
   - on `radix-digit-convolution`: $J$ (digit count): The number of digits in each input, that is, the number of blocks of $b$ bits.
   - on [Cyclic shift](cyclic-shift.md): $J$ (block length): The number of positions in the block that the shift rotates, a count of those positions.
93. $\xi$
   - on `radix-digit-convolution`: $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
   - on [Butterfly](butterfly.md): $\xi$ (first input value): The first of the two input values of the butterfly.
94. $\xi$
   - on `radix-digit-convolution`: $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
   - on [Permutation](permutation.md): $\xi$ (address): The position of one entry of an array.
95. $\xi$
   - on `radix-digit-convolution`: $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
96. $\xi$
   - on `radix-digit-convolution`: $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
97. $h$
   - on `ground-set`: $h$ (ground set size): The number of elements of the ground set, the count of its elements.
   - on [Linear networks and frames](linear-network-frames.md): $h$ (route position): The position of a vertex along a route, running from $0$ to $L$.
98. $g_1$
   - on `incidence`: $g_1$ (input array): The logical array on input wire 1 of the gate.
   - on [Gate and terminal of a network](network-gate-terminal.md): $g_1$ (first input array): The logical array on the first input wire of a two-wire gate.
99. $\Gamma$
   - on `incidence`: $\Gamma$ (moving-back operator): The single operator that would move the gate's result back to logical form.
   - on [Bijection](bijection.md): $\Gamma$ (padded address set): A set of integer addresses on which a tape procedure acts, including its padding.
100. $\xi$
   - on `tensor-product`: $\xi$ (row index): A row index of $P$, and in an address the output bit string $\xi$.
   - on [Butterfly](butterfly.md): $\xi$ (first input value): The first of the two input values of the butterfly.
101. $\xi$
   - on `tensor-product`: $\xi$ (row index): A row index of $P$, and in an address the output bit string $\xi$.
   - on [Permutation](permutation.md): $\xi$ (address): The position of one entry of an array.
102. $\xi$
   - on `tensor-product`: $\xi$ (row index): A row index of $P$, and in an address the output bit string $\xi$.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
103. $\xi$
   - on `tensor-product`: $\xi$ (row index): A row index of $P$, and in an address the output bit string $\xi$.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
104. $\sigma$
   - on `tensor-product`: $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
105. $\sigma$
   - on `tensor-product`: $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
106. $\sigma$
   - on `tensor-product`: $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
107. $\sigma$
   - on `tensor-product`: $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
108. $\sigma$
   - on `tensor-product`: $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
109. $\zeta$
   - on `tensor-product`: $\zeta$ (column index of Q): A column index of $Q$.
   - on [Butterfly](butterfly.md): $\zeta$ (second input value): The second of the two input values of the butterfly.
110. $\zeta$
   - on `tensor-product`: $\zeta$ (column index of Q): A column index of $Q$.
   - on [Cyclic shift](cyclic-shift.md): $\zeta$ (position): A position in the block, numbered from 0 to J-1.
111. $J$
   - on `tensor-product`: $J$ (factor count): The number of factors in a tensor power, which is also the number of coordinates it acts on.
   - on [Cyclic shift](cyclic-shift.md): $J$ (block length): The number of positions in the block that the shift rotates, a count of those positions.
112. $l$
   - on `tensor-product`: $l$ (coordinate index): The index of a coordinate, running from $1$ to $J$.
   - on [Linear algebra basics](linear-algebra-basics.md): $l$ (column index): The index of a column of a matrix product.
113. $W$
   - on `tensor-product`: $W$ (row index of P'): A row index of $P'$, summed over as a middle index of $P$ and $P'$.
   - on [Permutation](permutation.md): $W$ (position set): The finite set of positions on which a permutation acts.
114. $W$
   - on `tensor-product`: $W$ (row index of P'): A row index of $P'$, summed over as a middle index of $P$ and $P'$.
   - on [Bijection](bijection.md): $W$ (target set): The set that the map $f$ sends its inputs into, the set of outputs.
115. $t$
   - on `carry-propagation`: $t$ (position index): The position of a coefficient or digit in the list, running over $0, 1, \dots$.
   - on [Integer](integer.md): $t$ (indeterminate): A formal variable of polynomials, which is not a number.
116. $t$
   - on `carry-propagation`: $t$ (position index): The position of a coefficient or digit in the list, running over $0, 1, \dots$.
   - on [Convolution](convolution.md): $t$ (output position): The position of an entry of the convolution output.
117. $B$
   - on `congruence-modulo`: $B$ (modulus): The positive integer modulus by which congruence is taken.
   - on [Linear algebra basics](linear-algebra-basics.md): $B$ (candidate inverse): A matrix that satisfies AB=BA=I.
118. $d$
   - on `congruence-modulo`: $d$ (integer): An integer compared with $e$ modulo $B$.
   - on [Address](address.md): $d$ (address length): The number of bits in each address of the array, the length of every address string.
119. $\xi$
   - on `congruence-modulo`: $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
   - on [Radix-digit convolution](radix-digit-convolution.md): $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
120. $\xi$
   - on `congruence-modulo`: $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
   - on [Butterfly](butterfly.md): $\xi$ (first input value): The first of the two input values of the butterfly.
121. $\xi$
   - on `congruence-modulo`: $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
   - on [Permutation](permutation.md): $\xi$ (address): The position of one entry of an array.
122. $\xi$
   - on `congruence-modulo`: $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
123. $\xi$
   - on `congruence-modulo`: $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
124. $\zeta$
   - on `congruence-modulo`: $\zeta$ (third integer): An integer used in the transitivity argument, with $e \equiv \zeta$.
   - on [Butterfly](butterfly.md): $\zeta$ (second input value): The second of the two input values of the butterfly.
125. $\zeta$
   - on `congruence-modulo`: $\zeta$ (third integer): An integer used in the transitivity argument, with $e \equiv \zeta$.
   - on [Cyclic shift](cyclic-shift.md): $\zeta$ (position): A position in the block, numbered from 0 to J-1.
126. $\sigma$
   - on `congruence-modulo`: $\sigma$ (class member): An integer in the residue class of $d$.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
127. $\sigma$
   - on `congruence-modulo`: $\sigma$ (class member): An integer in the residue class of $d$.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
128. $\sigma$
   - on `congruence-modulo`: $\sigma$ (class member): An integer in the residue class of $d$.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
129. $\sigma$
   - on `congruence-modulo`: $\sigma$ (class member): An integer in the residue class of $d$.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
130. $\sigma$
   - on `congruence-modulo`: $\sigma$ (class member): An integer in the residue class of $d$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
131. $\delta$
   - on `congruence-modulo`: $\delta$ (remainder): The unique integer in $\{0,\dots,B-1\}$ lying in a residue class.
   - on [Permutation](permutation.md): $\delta$ (fourth entry): The entry of the sequence at position 4.
132. $\eta$
   - on `congruence-modulo`: $\eta$ (second multiple): The integer with $e'-e=\eta B$.
   - on [Linear algebra basics](linear-algebra-basics.md): $\eta$ (scalar): A scalar in F multiplying a vector.
133. $\sigma$
   - on `schonhage-strassen`: $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
134. $\sigma$
   - on `schonhage-strassen`: $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
135. $\sigma$
   - on `schonhage-strassen`: $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
136. $\sigma$
   - on `schonhage-strassen`: $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
137. $\sigma$
   - on `schonhage-strassen`: $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
138. $\sigma$
   - on `schonhage-strassen`: $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
139. $\sigma$
   - on `schonhage-strassen`: $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
140. $\sigma$
   - on `schonhage-strassen`: $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
141. $\sigma$
   - on `schonhage-strassen`: $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
142. $\xi$
   - on `schonhage-strassen`: $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
   - on [Congruence](congruence-modulo.md): $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
143. $\xi$
   - on `schonhage-strassen`: $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
   - on [Radix-digit convolution](radix-digit-convolution.md): $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
144. $\xi$
   - on `schonhage-strassen`: $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
   - on [Butterfly](butterfly.md): $\xi$ (first input value): The first of the two input values of the butterfly.
145. $\xi$
   - on `schonhage-strassen`: $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
   - on [Permutation](permutation.md): $\xi$ (address): The position of one entry of an array.
146. $\xi$
   - on `schonhage-strassen`: $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
147. $\xi$
   - on `schonhage-strassen`: $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
148. $\xi$
   - on `schonhage-strassen`: $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
   - on [Cyclic group](cyclic-group.md): $\xi$ (exponent): An integer to which the generator is raised, giving the power $\rho^\xi$.
149. $\xi$
   - on `schonhage-strassen`: $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
   - on [Coprime](coprime.md): $\xi$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the first of the two Bezout coefficients.
150. $\zeta$
   - on `schonhage-strassen`: $\zeta$ (residue): A residue, represented by the integer $\zeta$ with $0\le\zeta<2^\sigma$.
   - on [Congruence](congruence-modulo.md): $\zeta$ (third integer): An integer used in the transitivity argument, with $e \equiv \zeta$.
151. $\zeta$
   - on `schonhage-strassen`: $\zeta$ (residue): A residue, represented by the integer $\zeta$ with $0\le\zeta<2^\sigma$.
   - on [Butterfly](butterfly.md): $\zeta$ (second input value): The second of the two input values of the butterfly.
152. $\zeta$
   - on `schonhage-strassen`: $\zeta$ (residue): A residue, represented by the integer $\zeta$ with $0\le\zeta<2^\sigma$.
   - on [Cyclic shift](cyclic-shift.md): $\zeta$ (position): A position in the block, numbered from 0 to J-1.
153. $\zeta$
   - on `schonhage-strassen`: $\zeta$ (residue): A residue, represented by the integer $\zeta$ with $0\le\zeta<2^\sigma$.
   - on [Coprime](coprime.md): $\zeta$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the second of the two Bezout coefficients.
154. $\zeta_i$
   - on `schonhage-strassen`: $\zeta_i$ (bit of a residue): The bit of $\zeta$ at position $i$, either 0 or 1.
   - on [Cyclic group](cyclic-group.md): $\zeta_i$ (monomial exponent): The exponent of $Y_i$ in a target monomial, an integer from $0$ to $s_i-1$.
155. $i$
   - on `schonhage-strassen`: $i$ (bit position): A bit position of a residue, an integer from 0 to $\sigma-1$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $i$ (imaginary unit): The imaginary unit, the complex number whose square is $-1$, used in this page in place of the convolution page's input position $i$.
156. $i$
   - on `schonhage-strassen`: $i$ (bit position): A bit position of a residue, an integer from 0 to $\sigma-1$.
   - on [Linear algebra basics](linear-algebra-basics.md): $i$ (row index): The index of a row of a matrix, running from 1 to m.
157. $i$
   - on `schonhage-strassen`: $i$ (bit position): A bit position of a residue, an integer from 0 to $\sigma-1$.
   - on [Convolution](convolution.md): $i$ (input position in a): The position of an entry of $a$.
158. $i$
   - on `schonhage-strassen`: $i$ (bit position): A bit position of a residue, an integer from 0 to $\sigma-1$.
   - on [Transform axis](transform-axis.md): $i$ (axis index): An index naming one axis, running from 1 to D.
159. $\xi$
   - on `ring`: $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
160. $\xi$
   - on `ring`: $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Congruence](congruence-modulo.md): $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
161. $\xi$
   - on `ring`: $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Radix-digit convolution](radix-digit-convolution.md): $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
162. $\xi$
   - on `ring`: $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Butterfly](butterfly.md): $\xi$ (first input value): The first of the two input values of the butterfly.
163. $\xi$
   - on `ring`: $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Permutation](permutation.md): $\xi$ (address): The position of one entry of an array.
164. $\xi$
   - on `ring`: $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
165. $\xi$
   - on `ring`: $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
166. $\xi$
   - on `ring`: $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Cyclic group](cyclic-group.md): $\xi$ (exponent): An integer to which the generator is raised, giving the power $\rho^\xi$.
167. $\xi$
   - on `ring`: $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Coprime](coprime.md): $\xi$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the first of the two Bezout coefficients.
168. $\zeta$
   - on `ring`: $\zeta$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\zeta$ (residue): A residue, represented by the integer $\zeta$ with $0\le\zeta<2^\sigma$.
169. $\zeta$
   - on `ring`: $\zeta$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Congruence](congruence-modulo.md): $\zeta$ (third integer): An integer used in the transitivity argument, with $e \equiv \zeta$.
170. $\zeta$
   - on `ring`: $\zeta$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Butterfly](butterfly.md): $\zeta$ (second input value): The second of the two input values of the butterfly.
171. $\zeta$
   - on `ring`: $\zeta$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Cyclic shift](cyclic-shift.md): $\zeta$ (position): A position in the block, numbered from 0 to J-1.
172. $\zeta$
   - on `ring`: $\zeta$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
   - on [Coprime](coprime.md): $\zeta$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the second of the two Bezout coefficients.
173. $y$
   - on `polynomial-ring-mod-yr-plus-1`: $y$ (polynomial variable): The indeterminate of the polynomial ring whose powers act as roots of unity.
   - on [Logarithm](logarithm.md): $y$ (argument): The positive number whose logarithm is taken.
174. $y$
   - on `polynomial-ring-mod-yr-plus-1`: $y$ (polynomial variable): The indeterminate of the polynomial ring whose powers act as roots of unity.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $y$ (second input): The second binary input string, of length $n$.
175. $y$
   - on `polynomial-ring-mod-yr-plus-1`: $y$ (polynomial variable): The indeterminate of the polynomial ring whose powers act as roots of unity.
   - on [Linear algebra basics](linear-algebra-basics.md): $y$ (vector): A vector in a vector space, changed from earlier pages.
176. $\sigma$
   - on `polynomial-ring-mod-yr-plus-1`: $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
177. $\sigma$
   - on `polynomial-ring-mod-yr-plus-1`: $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
178. $\sigma$
   - on `polynomial-ring-mod-yr-plus-1`: $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
179. $\sigma$
   - on `polynomial-ring-mod-yr-plus-1`: $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
180. $\sigma$
   - on `polynomial-ring-mod-yr-plus-1`: $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
181. $\sigma$
   - on `polynomial-ring-mod-yr-plus-1`: $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
182. $\sigma$
   - on `polynomial-ring-mod-yr-plus-1`: $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
183. $\sigma$
   - on `polynomial-ring-mod-yr-plus-1`: $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
184. $\sigma$
   - on `polynomial-ring-mod-yr-plus-1`: $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
185. $\sigma$
   - on `polynomial-ring-mod-yr-plus-1`: $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
186. $\sigma$
   - on `polynomial-ring-mod-yr-plus-1`: $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\sigma$ (shift count): The number of places a shift moves each coefficient.
187. $\xi$
   - on `polynomial-ring-mod-yr-plus-1`: $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
   - on [Ring](ring.md): $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
188. $\xi$
   - on `polynomial-ring-mod-yr-plus-1`: $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
189. $\xi$
   - on `polynomial-ring-mod-yr-plus-1`: $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
   - on [Congruence](congruence-modulo.md): $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
190. $\xi$
   - on `polynomial-ring-mod-yr-plus-1`: $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
   - on [Radix-digit convolution](radix-digit-convolution.md): $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
191. $\xi$
   - on `polynomial-ring-mod-yr-plus-1`: $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
   - on [Butterfly](butterfly.md): $\xi$ (first input value): The first of the two input values of the butterfly.
192. $\xi$
   - on `polynomial-ring-mod-yr-plus-1`: $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
   - on [Permutation](permutation.md): $\xi$ (address): The position of one entry of an array.
193. $\xi$
   - on `polynomial-ring-mod-yr-plus-1`: $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
194. $\xi$
   - on `polynomial-ring-mod-yr-plus-1`: $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
195. $\xi$
   - on `polynomial-ring-mod-yr-plus-1`: $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
   - on [Cyclic group](cyclic-group.md): $\xi$ (exponent): An integer to which the generator is raised, giving the power $\rho^\xi$.
196. $\xi$
   - on `polynomial-ring-mod-yr-plus-1`: $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
   - on [Coprime](coprime.md): $\xi$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the first of the two Bezout coefficients.
197. $\zeta$
   - on `polynomial-ring-mod-yr-plus-1`: $\zeta$ (root of unity): An element of the ring whose positive integer power equals 1.
   - on [Ring](ring.md): $\zeta$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
198. $\zeta$
   - on `polynomial-ring-mod-yr-plus-1`: $\zeta$ (root of unity): An element of the ring whose positive integer power equals 1.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\zeta$ (residue): A residue, represented by the integer $\zeta$ with $0\le\zeta<2^\sigma$.
199. $\zeta$
   - on `polynomial-ring-mod-yr-plus-1`: $\zeta$ (root of unity): An element of the ring whose positive integer power equals 1.
   - on [Congruence](congruence-modulo.md): $\zeta$ (third integer): An integer used in the transitivity argument, with $e \equiv \zeta$.
200. $\zeta$
   - on `polynomial-ring-mod-yr-plus-1`: $\zeta$ (root of unity): An element of the ring whose positive integer power equals 1.
   - on [Butterfly](butterfly.md): $\zeta$ (second input value): The second of the two input values of the butterfly.
201. $\zeta$
   - on `polynomial-ring-mod-yr-plus-1`: $\zeta$ (root of unity): An element of the ring whose positive integer power equals 1.
   - on [Cyclic shift](cyclic-shift.md): $\zeta$ (position): A position in the block, numbered from 0 to J-1.
202. $\zeta$
   - on `polynomial-ring-mod-yr-plus-1`: $\zeta$ (root of unity): An element of the ring whose positive integer power equals 1.
   - on [Coprime](coprime.md): $\zeta$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the second of the two Bezout coefficients.
203. $k$
   - on `limit-inferior`: $k$ (term position): A position in a sequence, the index of a term.
   - on [Integer](integer.md): $k$ (digit count): The number of digits in a digit list.
204. $k$
   - on `limit-inferior`: $k$ (term position): A position in a sequence, the index of a term.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $k$ (padded length): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
205. $k$
   - on `limit-inferior`: $k$ (term position): A position in a sequence, the index of a term.
   - on [Root of unity](root-of-unity.md): $k$ (integer exponent): An integer exponent of $y$ in the power $y^k$ that multiplies the coefficient list.
206. $m$
   - on `limit-inferior`: $m$ (tail start): The position from which a tail of the sequence starts.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
207. $m$
   - on `limit-inferior`: $m$ (tail start): The position from which a tail of the sequence starts.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
208. $m$
   - on `limit-inferior`: $m$ (tail start): The position from which a tail of the sequence starts.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
209. $\delta$
   - on `limit-inferior`: $\delta$ (arbitrary positive real): A real number greater than zero, arbitrary in the negation of the conjecture.
   - on [Extended real numbers](extended-reals.md): $\delta$ (term position): The position of a term in a sequence, a positive integer.
210. $\delta$
   - on `limit-inferior`: $\delta$ (arbitrary positive real): A real number greater than zero, arbitrary in the negation of the conjecture.
   - on [Congruence](congruence-modulo.md): $\delta$ (remainder): The unique integer in $\{0,\dots,B-1\}$ lying in a residue class.
211. $\delta$
   - on `limit-inferior`: $\delta$ (arbitrary positive real): A real number greater than zero, arbitrary in the negation of the conjecture.
   - on [Permutation](permutation.md): $\delta$ (fourth entry): The entry of the sequence at position 4.
212. $\Gamma$
   - on `limit-inferior`: $\Gamma$ (arbitrary threshold): A threshold on input length, arbitrary in the negation of the conjecture.
   - on [Bijection](bijection.md): $\Gamma$ (padded address set): A set of integer addresses on which a tape procedure acts, including its padding.
213. $\Gamma$
   - on `limit-inferior`: $\Gamma$ (arbitrary threshold): A threshold on input length, arbitrary in the negation of the conjecture.
   - on [Cyclic group](cyclic-group.md): $\Gamma$ (target map): The map from polynomials in $\rho$ modulo $\rho^S-1$ to the target monomials, sending $\rho$ to $\prod_i Y_i^{\mu_i}$.
214. $n_0$
   - on `n-log-n-conjecture`: $n_0$ (threshold input length): A threshold on the input length, from which the negated statement asks for some input length with a small running time ratio.
   - on [Big-Theta notation](big-theta-notation.md): $n_0$ (threshold): The input size from which both inequalities hold.
215. $\sigma$
   - on `fixed-tape-model`: $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
   - on [Extended real numbers](extended-reals.md): $\sigma$ (generic real number): A real number used as a generic value in the order, sums and limit conditions.
216. $\sigma$
   - on `fixed-tape-model`: $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
217. $\sigma$
   - on `fixed-tape-model`: $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
218. $\sigma$
   - on `fixed-tape-model`: $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
219. $\sigma$
   - on `fixed-tape-model`: $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
220. $\sigma$
   - on `fixed-tape-model`: $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
221. $\sigma$
   - on `fixed-tape-model`: $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
222. $\sigma$
   - on `fixed-tape-model`: $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
223. $\sigma$
   - on `fixed-tape-model`: $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
224. $\sigma$
   - on `fixed-tape-model`: $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
225. $\sigma$
   - on `fixed-tape-model`: $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
226. $n_0$
   - on `fixed-tape-model`: $n_0$ (threshold input length): The input length from which the lower bound on $T_A(n)$ holds for machine $A$.
   - on [Big-Theta notation](big-theta-notation.md): $n_0$ (threshold): The input size from which both inequalities hold.
227. $\Omega$
   - on `fixed-tape-model`: $\Omega$ (Big-Omega notation): The notation $\Omega(g)$ for the functions that are at least a positive constant times $g$ for all large inputs.
   - on [Big-Omega notation](big-omega-notation.md): $\Omega$ (Big-Omega): The notation $\Omega(h)$ for the set of functions bounded below by a positive constant times $h$ for all large inputs, so that $u(N)=\Omega(h(N))$ says $u$ lies in that set.
228. $\mathbb{F}_2$
   - on `binary-field`: $\mathbb{F}_2$ (binary field): The field with the two elements 0 and 1, in which addition is exclusive or and multiplication is AND.
   - on [Linear algebra basics](linear-algebra-basics.md): $\mathbb{F}_2$ (two-element field): The field of integers modulo 2.
229. $\sigma$
   - on `binary-field`: $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
230. $\sigma$
   - on `binary-field`: $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
231. $\sigma$
   - on `binary-field`: $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
232. $\sigma$
   - on `binary-field`: $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
233. $\sigma$
   - on `binary-field`: $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
234. $\sigma$
   - on `binary-field`: $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
235. $\beta$
   - on `modular-inverse`: $\beta$ (integer to invert): The integer whose inverse modulo M is sought.
   - on [Permutation](permutation.md): $\beta$ (second entry): The entry of the sequence at position 2.
236. $M$
   - on `modular-inverse`: $M$ (modulus): The fixed positive integer modulo which the inverse is taken.
   - on [Running time cost](running-time-cost.md): $M$ (example machine): The example machine that reads cells from the first cell until it finds a $1$ or reaches the last cell.
237. $M$
   - on `modular-inverse`: $M$ (modulus): The fixed positive integer modulo which the inverse is taken.
   - on [Linear algebra basics](linear-algebra-basics.md): $M$ (shear matrix): A matrix over F_2 that determines the shear.
238. $\sigma$
   - on `modular-inverse`: $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
239. $\sigma$
   - on `modular-inverse`: $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
240. $\sigma$
   - on `modular-inverse`: $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
241. $\sigma$
   - on `modular-inverse`: $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
242. $\sigma$
   - on `modular-inverse`: $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
243. $\sigma$
   - on `modular-inverse`: $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
244. $\sigma$
   - on `modular-inverse`: $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
245. $\sigma$
   - on `modular-inverse`: $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
   - on [Bézout's identity](bezout-identity.md): $\sigma$ (Bézout coefficient of γ): The integer multiplying γ in the combination βρ+γσ that equals gcd(β,γ).
246. $\sigma$
   - on `modular-inverse`: $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
247. $i$
   - on `modular-inverse`: $i$ (axis index): The index of an axis, an integer from 1 to d.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $i$ (imaginary unit): The imaginary unit, the complex number whose square is $-1$, used in this page in place of the convolution page's input position $i$.
248. $i$
   - on `modular-inverse`: $i$ (axis index): The index of an axis, an integer from 1 to d.
   - on [Linear algebra basics](linear-algebra-basics.md): $i$ (row index): The index of a row of a matrix, running from 1 to m.
249. $i$
   - on `modular-inverse`: $i$ (axis index): The index of an axis, an integer from 1 to d.
   - on [Convolution](convolution.md): $i$ (input position in a): The position of an entry of $a$.
250. $j$
   - on `modular-inverse`: $j$ (axis index in products): An axis index that runs over the axes before a given axis in a product.
   - on [Integer](integer.md): $j$ (digit position): The position of a digit or bit, counted from the left starting at 1.
251. $j$
   - on `modular-inverse`: $j$ (axis index in products): An axis index that runs over the axes before a given axis in a product.
   - on [Linear algebra basics](linear-algebra-basics.md): $j$ (coordinate index): The index of a coordinate of a vector, running from 1 to m.
252. $j$
   - on `modular-inverse`: $j$ (axis index in products): An axis index that runs over the axes before a given axis in a product.
   - on [Convolution](convolution.md): $j$ (input position in b): The position of an entry of $b$.
253. $j$
   - on `modular-inverse`: $j$ (axis index in products): An axis index that runs over the axes before a given axis in a product.
   - on [Ceiling function](ceiling-function.md): $j$ (integer): Any integer, which is its own ceiling.
254. $\xi$
   - on `modular-inverse`: $\xi$ (group generator): A generator of the cyclic group of order S.
   - on [Radix-digit convolution](radix-digit-convolution.md): $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
255. $\xi$
   - on `modular-inverse`: $\xi$ (group generator): A generator of the cyclic group of order S.
   - on [Butterfly](butterfly.md): $\xi$ (first input value): The first of the two input values of the butterfly.
256. $\xi$
   - on `modular-inverse`: $\xi$ (group generator): A generator of the cyclic group of order S.
   - on [Permutation](permutation.md): $\xi$ (address): The position of one entry of an array.
257. $\xi$
   - on `modular-inverse`: $\xi$ (group generator): A generator of the cyclic group of order S.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
258. $\xi$
   - on `modular-inverse`: $\xi$ (group generator): A generator of the cyclic group of order S.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
259. $\xi$
   - on `modular-inverse`: $\xi$ (group generator): A generator of the cyclic group of order S.
   - on [Cyclic group](cyclic-group.md): $\xi$ (exponent): An integer to which the generator is raised, giving the power $\rho^\xi$.
260. $\xi$
   - on `modular-inverse`: $\xi$ (group generator): A generator of the cyclic group of order S.
   - on [Coprime](coprime.md): $\xi$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the first of the two Bezout coefficients.
261. $\xi$
   - on `modular-inverse`: $\xi$ (group generator): A generator of the cyclic group of order S.
   - on [Bézout's identity](bezout-identity.md): $\xi$ (least positive combination): The least positive value of βρ'+γσ' over all integers ρ' and σ'.
262. $\xi$
   - on `modular-inverse`: $\xi$ (group generator): A generator of the cyclic group of order S.
   - on [Congruence](congruence-modulo.md): $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
263. $\zeta$
   - on `modular-inverse`: $\zeta$ (positive exponent): A positive integer exponent for which the power of the image is 1.
   - on [Butterfly](butterfly.md): $\zeta$ (second input value): The second of the two input values of the butterfly.
264. $\zeta$
   - on `modular-inverse`: $\zeta$ (positive exponent): A positive integer exponent for which the power of the image is 1.
   - on [Cyclic shift](cyclic-shift.md): $\zeta$ (position): A position in the block, numbered from 0 to J-1.
265. $\zeta$
   - on `modular-inverse`: $\zeta$ (positive exponent): A positive integer exponent for which the power of the image is 1.
   - on [Coprime](coprime.md): $\zeta$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the second of the two Bezout coefficients.
266. $\zeta$
   - on `modular-inverse`: $\zeta$ (positive exponent): A positive integer exponent for which the power of the image is 1.
   - on [Congruence](congruence-modulo.md): $\zeta$ (third integer): An integer used in the transitivity argument, with $e \equiv \zeta$.
267. $\sigma$
   - on `binary-change-of-basis`: $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
268. $\sigma$
   - on `binary-change-of-basis`: $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
269. $\sigma$
   - on `binary-change-of-basis`: $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
270. $\sigma$
   - on `binary-change-of-basis`: $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
271. $\sigma$
   - on `binary-change-of-basis`: $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
272. $\sigma$
   - on `binary-change-of-basis`: $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
273. $\sigma$
   - on `binary-change-of-basis`: $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
274. $v$
   - on `binary-change-of-basis`: $v$ (direction vector): A vector of $\mathbb F_2^m$ in a residual basis; $v_j$ is its $j$-th member.
   - on [Linear algebra basics](linear-algebra-basics.md): $v$ (vertex): A vertex of the paper's directed graph.
275. $\rho$
   - on `binary-change-of-basis`: $\rho$ (residual dimension): The number of vectors in a residual basis, which counts the dimension of the edge's residual.
   - on [Address field](address-field.md): $\rho$ (field width): The number of bits in each of the two fields being interchanged, a count of bit positions.
276. $\rho$
   - on `binary-change-of-basis`: $\rho$ (residual dimension): The number of vectors in a residual basis, which counts the dimension of the edge's residual.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\rho$ (exponent): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
277. $\sigma$
   - on `bit-network`: $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
278. $\sigma$
   - on `bit-network`: $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
279. $\sigma$
   - on `bit-network`: $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
280. $\sigma$
   - on `bit-network`: $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
281. $\sigma$
   - on `bit-network`: $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
282. $\sigma$
   - on `bit-network`: $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
283. $\sigma$
   - on `bit-network`: $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
284. $\sigma$
   - on `bit-network`: $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
285. $\sigma$
   - on `bit-network`: $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
286. $W$
   - on `bit-network`: $W$ (source bank): The bank of source bits, holding one bit $W_\sigma$ for each triple $\sigma$.
   - on [Permutation](permutation.md): $W$ (position set): The finite set of positions on which a permutation acts.
287. $W$
   - on `bit-network`: $W$ (source bank): The bank of source bits, holding one bit $W_\sigma$ for each triple $\sigma$.
   - on [Bijection](bijection.md): $W$ (target set): The set that the map $f$ sends its inputs into, the set of outputs.
288. $\zeta$
   - on `phase-factor`: $\zeta$ (phase factor): A complex number of modulus one, the factor multiplied into coefficients.
   - on [Ring](ring.md): $\zeta$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
289. $\zeta$
   - on `phase-factor`: $\zeta$ (phase factor): A complex number of modulus one, the factor multiplied into coefficients.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\zeta$ (residue): A residue, represented by the integer $\zeta$ with $0\le\zeta<2^\sigma$.
290. $\zeta$
   - on `phase-factor`: $\zeta$ (phase factor): A complex number of modulus one, the factor multiplied into coefficients.
   - on [Congruence](congruence-modulo.md): $\zeta$ (third integer): An integer used in the transitivity argument, with $e \equiv \zeta$.
291. $\zeta$
   - on `phase-factor`: $\zeta$ (phase factor): A complex number of modulus one, the factor multiplied into coefficients.
   - on [Butterfly](butterfly.md): $\zeta$ (second input value): The second of the two input values of the butterfly.
292. $\zeta$
   - on `phase-factor`: $\zeta$ (phase factor): A complex number of modulus one, the factor multiplied into coefficients.
   - on [Cyclic shift](cyclic-shift.md): $\zeta$ (position): A position in the block, numbered from 0 to J-1.
293. $\zeta$
   - on `phase-factor`: $\zeta$ (phase factor): A complex number of modulus one, the factor multiplied into coefficients.
   - on [Coprime](coprime.md): $\zeta$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the second of the two Bezout coefficients.
294. $D$
   - on `phase-factor`: $D$ (selected bit count): The number of selected address bits on which a butterfly layer acts.
   - on [Transform axis](transform-axis.md): $D$ (axis count): The number of axes of the array.
295. $x$
   - on `phase-factor`: $x$ (address): An address whose selected bits are $x_1,\dots,x_D$, each 0 or 1.
   - on [Integer](integer.md): $x$ (binary string): A binary string of bits, read as an integer by the paper's rule.
296. $x$
   - on `phase-factor`: $x$ (address): An address whose selected bits are $x_1,\dots,x_D$, each 0 or 1.
   - on [Linear algebra basics](linear-algebra-basics.md): $x$ (vector): A vector in a vector space, changed from earlier pages.
297. $x$
   - on `phase-factor`: $x$ (address): An address whose selected bits are $x_1,\dots,x_D$, each 0 or 1.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $x$ (first input): The first binary input string, of length $n$.
298. $x$
   - on `phase-factor`: $x$ (address): An address whose selected bits are $x_1,\dots,x_D$, each 0 or 1.
   - on [Order of an element](order-of-element.md): $x$ (indeterminate): The indeterminate of the ring C[x] modulo x^S minus 1, whose image the map sends to a product of axis indeterminates.
299. $\sigma$
   - on `gaussian-dyadics`: $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
300. $\sigma$
   - on `gaussian-dyadics`: $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
301. $\sigma$
   - on `gaussian-dyadics`: $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
302. $\sigma$
   - on `gaussian-dyadics`: $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
303. $\sigma$
   - on `gaussian-dyadics`: $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
304. $\sigma$
   - on `gaussian-dyadics`: $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
305. $\sigma$
   - on `gaussian-dyadics`: $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
306. $\sigma$
   - on `gaussian-dyadics`: $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
307. $\sigma$
   - on `gaussian-dyadics`: $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
308. $\sigma$
   - on `gaussian-dyadics`: $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
309. $\sigma$
   - on `gaussian-dyadics`: $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
310. $\Gamma$
   - on `gaussian-dyadics`: $\Gamma$ (denominator exponent): The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
   - on [Bijection](bijection.md): $\Gamma$ (padded address set): A set of integer addresses on which a tape procedure acts, including its padding.
311. $\Gamma$
   - on `gaussian-dyadics`: $\Gamma$ (denominator exponent): The number of factors of two in the denominator of a Gaussian dyadic, a nonnegative integer.
   - on [Cyclic group](cyclic-group.md): $\Gamma$ (target map): The map from polynomials in $\rho$ modulo $\rho^S-1$ to the target monomials, sending $\rho$ to $\prod_i Y_i^{\mu_i}$.
312. $e$
   - on `two-point-kernel`: $e$ (bit position): An index from 0 to d-1 naming the bit along which a kernel acts, counted from the least significant bit.
   - on [Congruence](congruence-modulo.md): $e$ (integer): An integer compared with $d$ modulo $B$.
313. $\delta$
   - on `two-point-kernel`: $\delta$ (identity coefficient): The complex coefficient of the identity matrix in a two-point kernel.
   - on [Permutation](permutation.md): $\delta$ (fourth entry): The entry of the sequence at position 4.
314. $\delta$
   - on `two-point-kernel`: $\delta$ (identity coefficient): The complex coefficient of the identity matrix in a two-point kernel.
   - on [Congruence](congruence-modulo.md): $\delta$ (remainder): The unique integer in $\{0,\dots,B-1\}$ lying in a residue class.
315. $\kappa$
   - on `two-point-kernel`: $\kappa$ (bit-flip coefficient): The complex coefficient of the bit flip in a two-point kernel.
   - on [Base-2 logarithm](base-two-logarithm.md): $\kappa$ (bound constant): The fixed constant $2^{-182}$ in the paper's running-time bound.
316. $\kappa$
   - on `two-point-kernel`: $\kappa$ (bit-flip coefficient): The complex coefficient of the bit flip in a two-point kernel.
   - on [Running time cost](running-time-cost.md): $\kappa$ (exponent constant): The fixed constant $2^{-182}$ in the exponent of the bound $O(n(\lg n)^{1-\kappa})$.
317. $K$
   - on `two-point-kernel`: $K$ (two-point kernel): The 2 by 2 matrix delta I plus kappa X, which is the two-point kernel.
   - on [Linear algebra basics](linear-algebra-basics.md): $K$ (address block): The second bit block of an address.
318. $f$
   - on `polynomial-ring`: $f$ (modulus polynomial): The fixed monic polynomial with complex coefficients by which the ring is reduced.
   - on [Big-Theta notation](big-theta-notation.md): $f$ (bounded function): The function from input sizes to nonnegative reals whose order is compared with that of $h$.
319. $f$
   - on `polynomial-ring`: $f$ (modulus polynomial): The fixed monic polynomial with complex coefficients by which the ring is reduced.
   - on [Bijection](bijection.md): $f$ (map): The map from the source set $U$ to the target set $W$ whose bijectivity is tested.
320. $f$
   - on `polynomial-ring`: $f$ (modulus polynomial): The fixed monic polynomial with complex coefficients by which the ring is reduced.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $f$ (input vector): A vector of $q$ complex numbers, the input to the transform, with coordinates $f_0, \ldots, f_{q-1}$.
321. $m$
   - on `polynomial-ring`: $m$ (coefficient count): The number of coefficients in each representative, which is the degree of f.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
322. $m$
   - on `polynomial-ring`: $m$ (coefficient count): The number of coefficients in each representative, which is the degree of f.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
323. $m$
   - on `polynomial-ring`: $m$ (coefficient count): The number of coefficients in each representative, which is the degree of f.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
324. $R$
   - on `polynomial-ring`: $R$ (polynomial ring): The ring of classes of complex polynomials, where two polynomials are identified when their difference is a multiple of f.
   - on [Ring](ring.md): $R$ (ring): A set with an addition and a multiplication that satisfy the axioms listed on this page.
325. $u$
   - on `polynomial-ring`: $u$ (representative): The unique polynomial of degree less than m in a class, the representative of that class.
   - on [Linear algebra basics](linear-algebra-basics.md): $u$ (vertex): A vertex of the paper's directed graph.
326. $t$
   - on `polynomial-ring`: $t$ (coefficient index): The index of a coefficient of the representative, running from 0 to m-1.
   - on [Integer](integer.md): $t$ (indeterminate): A formal variable of polynomials, which is not a number.
327. $t$
   - on `polynomial-ring`: $t$ (coefficient index): The index of a coefficient of the representative, running from 0 to m-1.
   - on [Carry propagation](carry-propagation.md): $t$ (position index): The position of a coefficient or digit in the list, running over $0, 1, \dots$.
328. $t$
   - on `polynomial-ring`: $t$ (coefficient index): The index of a coefficient of the representative, running from 0 to m-1.
   - on [Convolution](convolution.md): $t$ (output position): The position of an entry of the convolution output.
329. $e$
   - on `polynomial-ring`: $e$ (exponent): The exponent of y in a term of a product, the power of y that reduction tests against m.
   - on [Congruence](congruence-modulo.md): $e$ (integer): An integer compared with $d$ modulo $B$.
330. $s$
   - on `polynomial-ring`: $s$ (shift exponent): The integer exponent of the power of y that multiplies the representative, which the paper writes as a.
   - on [Ceiling function](ceiling-function.md): $s$ (real number): The real number that the ceiling rounds up to an integer.
331. $s$
   - on `polynomial-ring`: $s$ (shift exponent): The integer exponent of the power of y that multiplies the representative, which the paper writes as a.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $s$ (input index): An integer index running over $0, 1, \ldots, q-1$ that labels an input coordinate $f_s$.
332. $s$
   - on `polynomial-ring`: $s$ (shift exponent): The integer exponent of the power of y that multiplies the representative, which the paper writes as a.
   - on [Transform axis](transform-axis.md): $s$ (coefficient count): A power of two that is the number of coefficients of the stored polynomial, which is also the length of its axis.
333. $W$
   - on `grid-numerator`: $W$ (output coefficient): One output coefficient of the paper's polynomial multiplication, a sum of $r$ signed products of input coefficients.
   - on [Permutation](permutation.md): $W$ (position set): The finite set of positions on which a permutation acts.
334. $W$
   - on `grid-numerator`: $W$ (output coefficient): One output coefficient of the paper's polynomial multiplication, a sum of $r$ signed products of input coefficients.
   - on [Bijection](bijection.md): $W$ (target set): The set that the map $f$ sends its inputs into, the set of outputs.
335. $W$
   - on `grid-numerator`: $W$ (output coefficient): One output coefficient of the paper's polynomial multiplication, a sum of $r$ signed products of input coefficients.
   - on [Cyclic group](cyclic-group.md): $W$ (cyclic group order): The number of elements of the cyclic group $C_W$, which counts its distinct powers of the generator.
336. $W$
   - on `grid-numerator`: $W$ (output coefficient): One output coefficient of the paper's polynomial multiplication, a sum of $r$ signed products of input coefficients.
   - on [Coprime](coprime.md): $W$ (family product): The product f_1 times f_2 up to f_J, which is the least positive integer divisible by every member.
337. $J$
   - on `grid-numerator`: $J$ (word width): The number of bits in a signed word that stores one component numerator.
   - on [Radix-digit convolution](radix-digit-convolution.md): $J$ (digit count): The number of digits in each input, that is, the number of blocks of $b$ bits.
338. $J$
   - on `grid-numerator`: $J$ (word width): The number of bits in a signed word that stores one component numerator.
   - on [Cyclic shift](cyclic-shift.md): $J$ (block length): The number of positions in the block that the shift rotates, a count of those positions.
339. $J$
   - on `grid-numerator`: $J$ (word width): The number of bits in a signed word that stores one component numerator.
   - on [Coprime](coprime.md): $J$ (family size): The number of integers in the family f_1 to f_J.
340. $J$
   - on `chinese-remainder-theorem`: $J$ (number of congruences): The number of congruences in the system, a positive integer.
   - on [Coprime](coprime.md): $J$ (family size): The number of integers in the family f_1 to f_J.
341. $J$
   - on `chinese-remainder-theorem`: $J$ (number of congruences): The number of congruences in the system, a positive integer.
   - on [Radix-digit convolution](radix-digit-convolution.md): $J$ (digit count): The number of digits in each input, that is, the number of blocks of $b$ bits.
342. $J$
   - on `chinese-remainder-theorem`: $J$ (number of congruences): The number of congruences in the system, a positive integer.
   - on [Cyclic shift](cyclic-shift.md): $J$ (block length): The number of positions in the block that the shift rotates, a count of those positions.
343. $\sigma$
   - on `chinese-remainder-theorem`: $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
344. $\sigma$
   - on `chinese-remainder-theorem`: $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
345. $\sigma$
   - on `chinese-remainder-theorem`: $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
346. $\sigma$
   - on `chinese-remainder-theorem`: $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
347. $\sigma$
   - on `chinese-remainder-theorem`: $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
348. $\sigma$
   - on `chinese-remainder-theorem`: $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
349. $\sigma$
   - on `chinese-remainder-theorem`: $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
350. $W_\sigma$
   - on `chinese-remainder-theorem`: $W_\sigma$ (modulus): The modulus of the sigma-th congruence, a positive integer.
   - on [Coprime](coprime.md): $W_\sigma$ (prefix product): The product f_1 times ... times f_(sigma-1), with W_1 = 1.
351. $Y$
   - on `chinese-remainder-theorem`: $Y$ (unknown integer): The unknown integer whose congruences are being solved.
   - on [Coprime](coprime.md): $Y$ (common multiple): An integer that both gamma and rho divide, or that every member of the family divides.
352. $\Gamma$
   - on `chinese-remainder-theorem`: $\Gamma$ (product of moduli): The product of all the moduli, a positive integer.
   - on [Bijection](bijection.md): $\Gamma$ (padded address set): A set of integer addresses on which a tape procedure acts, including its padding.
353. $D$
   - on `chinese-remainder-theorem`: $D$ (difference of solutions): The difference Y' minus Y of two solutions.
   - on [Transform axis](transform-axis.md): $D$ (axis count): The number of axes of the array.
354. $f$
   - on `cyclic-convolution`: $f$ (input sequence): The first input sequence, of length n, with entries indexed from 0 to n-1.
   - on [Big-Theta notation](big-theta-notation.md): $f$ (bounded function): The function from input sizes to nonnegative reals whose order is compared with that of $h$.
355. $f$
   - on `cyclic-convolution`: $f$ (input sequence): The first input sequence, of length n, with entries indexed from 0 to n-1.
   - on [Bijection](bijection.md): $f$ (map): The map from the source set $U$ to the target set $W$ whose bijectivity is tested.
356. $f$
   - on `cyclic-convolution`: $f$ (input sequence): The first input sequence, of length n, with entries indexed from 0 to n-1.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $f$ (input vector): A vector of $q$ complex numbers, the input to the transform, with coordinates $f_0, \ldots, f_{q-1}$.
357. $f$
   - on `cyclic-convolution`: $f$ (input sequence): The first input sequence, of length n, with entries indexed from 0 to n-1.
   - on [Bézout's identity](bezout-identity.md): $f$ (quotient): The integer quotient in the division of β by ξ.
358. $g$
   - on `cyclic-convolution`: $g$ (second input sequence): The second input sequence, of length n, with entries indexed from 0 to n-1.
   - on [Linear algebra basics](linear-algebra-basics.md): $g$ (logical array): The array the computation means.
359. $k$
   - on `cyclic-convolution`: $k$ (output position): The position of an entry of the output $f \ast g$, running from 0 to n-1.
   - on [Integer](integer.md): $k$ (digit count): The number of digits in a digit list.
360. $k$
   - on `cyclic-convolution`: $k$ (output position): The position of an entry of the output $f \ast g$, running from 0 to n-1.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $k$ (padded length): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
361. $k$
   - on `cyclic-convolution`: $k$ (output position): The position of an entry of the output $f \ast g$, running from 0 to n-1.
   - on [Root of unity](root-of-unity.md): $k$ (integer exponent): An integer exponent of $y$ in the power $y^k$ that multiplies the coefficient list.
362. $j$
   - on `cyclic-convolution`: $j$ (summand position): The position in $f$ of each summand of an output entry, so it indexes $f$ here.
   - on [Modular inverse](modular-inverse.md): $j$ (axis index in products): An axis index that runs over the axes before a given axis in a product.
363. $j$
   - on `cyclic-convolution`: $j$ (summand position): The position in $f$ of each summand of an output entry, so it indexes $f$ here.
   - on [Integer](integer.md): $j$ (digit position): The position of a digit or bit, counted from the left starting at 1.
364. $j$
   - on `cyclic-convolution`: $j$ (summand position): The position in $f$ of each summand of an output entry, so it indexes $f$ here.
   - on [Linear algebra basics](linear-algebra-basics.md): $j$ (coordinate index): The index of a coordinate of a vector, running from 1 to m.
365. $j$
   - on `cyclic-convolution`: $j$ (summand position): The position in $f$ of each summand of an output entry, so it indexes $f$ here.
   - on [Convolution](convolution.md): $j$ (input position in b): The position of an entry of $b$.
366. $j$
   - on `cyclic-convolution`: $j$ (summand position): The position in $f$ of each summand of an output entry, so it indexes $f$ here.
   - on [Ceiling function](ceiling-function.md): $j$ (integer): Any integer, which is its own ceiling.
367. $d$
   - on `cyclic-convolution`: $d$ (axis count): The number of axes in the split, that is, the number of factors $n_1, \dots, n_d$ of the length n.
   - on [Address](address.md): $d$ (address length): The number of bits in each address of the array, the length of every address string.
368. $d$
   - on `cyclic-convolution`: $d$ (axis count): The number of axes in the split, that is, the number of factors $n_1, \dots, n_d$ of the length n.
   - on [Congruence](congruence-modulo.md): $d$ (integer): An integer compared with $e$ modulo $B$.
369. $\kappa$
   - on `cyclic-convolution`: $\kappa$ (axis index): The index of an axis, running from 1 to d.
   - on [Running time cost](running-time-cost.md): $\kappa$ (exponent constant): The fixed constant $2^{-182}$ in the exponent of the bound $O(n(\lg n)^{1-\kappa})$.
370. $\kappa$
   - on `cyclic-convolution`: $\kappa$ (axis index): The index of an axis, running from 1 to d.
   - on [Base-2 logarithm](base-two-logarithm.md): $\kappa$ (bound constant): The fixed constant $2^{-182}$ in the paper's running-time bound.
371. $t$
   - on `cyclic-convolution`: $t$ (transform length): The even length of the transform, which counts the entries of each sequence it transforms.
   - on [Integer](integer.md): $t$ (indeterminate): A formal variable of polynomials, which is not a number.
372. $t$
   - on `cyclic-convolution`: $t$ (transform length): The even length of the transform, which counts the entries of each sequence it transforms.
   - on [Convolution](convolution.md): $t$ (output position): The position of an entry of the convolution output.
373. $t$
   - on `cyclic-convolution`: $t$ (transform length): The even length of the transform, which counts the entries of each sequence it transforms.
   - on [Bézout's identity](bezout-identity.md): $t$ (family parameter): An arbitrary integer labelling one pair of coefficients.
374. $t$
   - on `cyclic-convolution`: $t$ (transform length): The even length of the transform, which counts the entries of each sequence it transforms.
   - on [Carry propagation](carry-propagation.md): $t$ (position index): The position of a coefficient or digit in the list, running over $0, 1, \dots$.
375. $\omega$
   - on `cyclic-convolution`: $\omega$ (primitive root): The complex number $e^{2\pi i/t}$, whose $t$-th power is 1.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\omega$ (primitive root of unity): The complex number $e^{-2\pi i/q}$, a primitive $q$-th root of unity.
376. $\rho$
   - on `cyclic-convolution`: $\rho$ (phase sequence): The function $\rho(\delta) = e^{-\pi i \delta^2/t}$, read as a sequence of length t modulo t.
   - on [Address field](address-field.md): $\rho$ (field width): The number of bits in each of the two fields being interchanged, a count of bit positions.
377. $\rho$
   - on `cyclic-convolution`: $\rho$ (phase sequence): The function $\rho(\delta) = e^{-\pi i \delta^2/t}$, read as a sequence of length t modulo t.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\rho$ (exponent): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
378. $\rho$
   - on `cyclic-convolution`: $\rho$ (phase sequence): The function $\rho(\delta) = e^{-\pi i \delta^2/t}$, read as a sequence of length t modulo t.
   - on [Cyclic group](cyclic-group.md): $\rho$ (generator): An element of a group, the base of its powers; when its powers are all the elements, it is the generator.
379. $\rho$
   - on `cyclic-convolution`: $\rho$ (phase sequence): The function $\rho(\delta) = e^{-\pi i \delta^2/t}$, read as a sequence of length t modulo t.
   - on [Coprime](coprime.md): $\rho$ (second integer): The other of two integers, not both zero, whose gcd is taken.
380. $\rho$
   - on `cyclic-convolution`: $\rho$ (phase sequence): The function $\rho(\delta) = e^{-\pi i \delta^2/t}$, read as a sequence of length t modulo t.
   - on [Bézout's identity](bezout-identity.md): $\rho$ (Bézout coefficient of β): The integer multiplying β in the combination βρ+γσ that equals gcd(β,γ).
381. $\delta$
   - on `cyclic-convolution`: $\delta$ (integer argument): An integer at which the phase function $\rho$ is evaluated.
   - on [Permutation](permutation.md): $\delta$ (fourth entry): The entry of the sequence at position 4.
382. $\delta$
   - on `cyclic-convolution`: $\delta$ (integer argument): An integer at which the phase function $\rho$ is evaluated.
   - on [Congruence](congruence-modulo.md): $\delta$ (remainder): The unique integer in $\{0,\dots,B-1\}$ lying in a residue class.
383. $\sigma$
   - on `ring-homomorphism`: $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
   - on [Modular inverse](modular-inverse.md): $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
384. $\sigma$
   - on `ring-homomorphism`: $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
385. $\sigma$
   - on `ring-homomorphism`: $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
386. $\sigma$
   - on `ring-homomorphism`: $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
387. $\sigma$
   - on `ring-homomorphism`: $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
388. $\sigma$
   - on `ring-homomorphism`: $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
389. $\sigma$
   - on `ring-homomorphism`: $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
390. $\sigma$
   - on `ring-homomorphism`: $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
391. $\sigma$
   - on `ring-homomorphism`: $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
   - on [Bézout's identity](bezout-identity.md): $\sigma$ (Bézout coefficient of γ): The integer multiplying γ in the combination βρ+γσ that equals gcd(β,γ).
392. $\sigma$
   - on `ring-homomorphism`: $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
393. $\sigma$
   - on `ring-homomorphism`: $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
   - on [Chinese remainder theorem](chinese-remainder-theorem.md): $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
394. $W$
   - on `ring-homomorphism`: $W$ (quotient ring W): The ring of complex polynomials in t in which every multiple of t^2-1 is zero.
   - on [Permutation](permutation.md): $W$ (position set): The finite set of positions on which a permutation acts.
395. $W$
   - on `ring-homomorphism`: $W$ (quotient ring W): The ring of complex polynomials in t in which every multiple of t^2-1 is zero.
   - on [Bijection](bijection.md): $W$ (target set): The set that the map $f$ sends its inputs into, the set of outputs.
396. $W$
   - on `ring-homomorphism`: $W$ (quotient ring W): The ring of complex polynomials in t in which every multiple of t^2-1 is zero.
   - on [Cyclic group](cyclic-group.md): $W$ (cyclic group order): The number of elements of the cyclic group $C_W$, which counts its distinct powers of the generator.
397. $W$
   - on `ring-homomorphism`: $W$ (quotient ring W): The ring of complex polynomials in t in which every multiple of t^2-1 is zero.
   - on [Coprime](coprime.md): $W$ (family product): The product f_1 times f_2 up to f_J, which is the least positive integer divisible by every member.
398. $t$
   - on `ring-homomorphism`: $t$ (indeterminate t): The indeterminate of W; on this page the letter denotes only this.
   - on [Cyclic convolution](cyclic-convolution.md): $t$ (transform length): The even length of the transform, which counts the entries of each sequence it transforms.
399. $t$
   - on `ring-homomorphism`: $t$ (indeterminate t): The indeterminate of W; on this page the letter denotes only this.
   - on [Integer](integer.md): $t$ (indeterminate): A formal variable of polynomials, which is not a number.
400. $t$
   - on `ring-homomorphism`: $t$ (indeterminate t): The indeterminate of W; on this page the letter denotes only this.
   - on [Convolution](convolution.md): $t$ (output position): The position of an entry of the convolution output.
401. $t$
   - on `ring-homomorphism`: $t$ (indeterminate t): The indeterminate of W; on this page the letter denotes only this.
   - on [Bézout's identity](bezout-identity.md): $t$ (family parameter): An arbitrary integer labelling one pair of coefficients.
402. $t$
   - on `ring-homomorphism`: $t$ (indeterminate t): The indeterminate of W; on this page the letter denotes only this.
   - on [Carry propagation](carry-propagation.md): $t$ (position index): The position of a coefficient or digit in the list, running over $0, 1, \dots$.
403. $\alpha$
   - on `ring-homomorphism`: $\alpha$ (constant coefficient): The constant coefficient of an element alpha + beta t of W.
   - on [Address](address.md): $\alpha$ (address string): A binary string of $d$ bits that labels one entry of the array.
404. $\alpha$
   - on `ring-homomorphism`: $\alpha$ (constant coefficient): The constant coefficient of an element alpha + beta t of W.
   - on [Permutation](permutation.md): $\alpha$ (first entry): The entry of the sequence at position 1.
405. $\beta$
   - on `ring-homomorphism`: $\beta$ (linear coefficient): The coefficient of t in an element alpha + beta t of W.
   - on [Modular inverse](modular-inverse.md): $\beta$ (integer to invert): The integer whose inverse modulo M is sought.
406. $\beta$
   - on `ring-homomorphism`: $\beta$ (linear coefficient): The coefficient of t in an element alpha + beta t of W.
   - on [Permutation](permutation.md): $\beta$ (second entry): The entry of the sequence at position 2.
407. $s$
   - on `ring-homomorphism`: $s$ (square-one element): An element of the commutative target ring whose square is 1, the image of t.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $s$ (input index): An integer index running over $0, 1, \ldots, q-1$ that labels an input coordinate $f_s$.
408. $s$
   - on `ring-homomorphism`: $s$ (square-one element): An element of the commutative target ring whose square is 1, the image of t.
   - on [Transform axis](transform-axis.md): $s$ (coefficient count): A power of two that is the number of coefficients of the stored polynomial, which is also the length of its axis.
409. $s$
   - on `ring-homomorphism`: $s$ (square-one element): An element of the commutative target ring whose square is 1, the image of t.
   - on [Ceiling function](ceiling-function.md): $s$ (real number): The real number that the ceiling rounds up to an integer.
410. $\rho$
   - on `ring-homomorphism`: $\rho$ (substitution map): The homomorphism from W to C sending t to 1.
   - on [Cyclic convolution](cyclic-convolution.md): $\rho$ (phase sequence): The function $\rho(\delta) = e^{-\pi i \delta^2/t}$, read as a sequence of length t modulo t.
411. $\rho$
   - on `ring-homomorphism`: $\rho$ (substitution map): The homomorphism from W to C sending t to 1.
   - on [Address field](address-field.md): $\rho$ (field width): The number of bits in each of the two fields being interchanged, a count of bit positions.
412. $\rho$
   - on `ring-homomorphism`: $\rho$ (substitution map): The homomorphism from W to C sending t to 1.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\rho$ (exponent): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
413. $\rho$
   - on `ring-homomorphism`: $\rho$ (substitution map): The homomorphism from W to C sending t to 1.
   - on [Cyclic group](cyclic-group.md): $\rho$ (generator): An element of a group, the base of its powers; when its powers are all the elements, it is the generator.
414. $\rho$
   - on `ring-homomorphism`: $\rho$ (substitution map): The homomorphism from W to C sending t to 1.
   - on [Coprime](coprime.md): $\rho$ (second integer): The other of two integers, not both zero, whose gcd is taken.
415. $\rho$
   - on `ring-homomorphism`: $\rho$ (substitution map): The homomorphism from W to C sending t to 1.
   - on [Bézout's identity](bezout-identity.md): $\rho$ (Bézout coefficient of β): The integer multiplying β in the combination βρ+γσ that equals gcd(β,γ).
416. $x$
   - on `ring-homomorphism`: $x$ (generator): The generator of the cyclic polynomial ring C[x]/(x^S-1).
   - on [Linear algebra basics](linear-algebra-basics.md): $x$ (vector): A vector in a vector space, changed from earlier pages.
417. $x$
   - on `ring-homomorphism`: $x$ (generator): The generator of the cyclic polynomial ring C[x]/(x^S-1).
   - on [Integer](integer.md): $x$ (binary string): A binary string of bits, read as an integer by the paper's rule.
418. $x$
   - on `ring-homomorphism`: $x$ (generator): The generator of the cyclic polynomial ring C[x]/(x^S-1).
   - on [Exact integer multiplication](exact-integer-multiplication.md): $x$ (first input): The first binary input string, of length $n$.
419. $g$
   - on `ring-homomorphism`: $g$ (monomial image of x): The monomial that the map Phi sends x to.
   - on [Linear algebra basics](linear-algebra-basics.md): $g$ (logical array): The array the computation means.
420. $g$
   - on `ring-homomorphism`: $g$ (monomial image of x): The monomial that the map Phi sends x to.
   - on [Cyclic convolution](cyclic-convolution.md): $g$ (second input sequence): The second input sequence, of length n, with entries indexed from 0 to n-1.
421. $D$
   - on `chinese-remainder-map`: $D$ (number of axes): The number of cyclic axes, which is the number of pairwise coprime axis lengths.
   - on [Transform axis](transform-axis.md): $D$ (axis count): The number of axes of the array.
422. $D$
   - on `chinese-remainder-map`: $D$ (number of axes): The number of cyclic axes, which is the number of pairwise coprime axis lengths.
   - on [Chinese remainder theorem](chinese-remainder-theorem.md): $D$ (difference of solutions): The difference Y' minus Y of two solutions.
423. $x$
   - on `chinese-remainder-map`: $x$ (generator indeterminate): A formal symbol, never evaluated, whose powers index the positions of the one-dimensional ring.
   - on [Ring homomorphism and isomorphism](ring-homomorphism.md): $x$ (generator): The generator of the cyclic polynomial ring C[x]/(x^S-1).
424. $x$
   - on `chinese-remainder-map`: $x$ (generator indeterminate): A formal symbol, never evaluated, whose powers index the positions of the one-dimensional ring.
   - on [Linear algebra basics](linear-algebra-basics.md): $x$ (vector): A vector in a vector space, changed from earlier pages.
425. $x$
   - on `chinese-remainder-map`: $x$ (generator indeterminate): A formal symbol, never evaluated, whose powers index the positions of the one-dimensional ring.
   - on [Integer](integer.md): $x$ (binary string): A binary string of bits, read as an integer by the paper's rule.
426. $x$
   - on `chinese-remainder-map`: $x$ (generator indeterminate): A formal symbol, never evaluated, whose powers index the positions of the one-dimensional ring.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $x$ (first input): The first binary input string, of length $n$.
427. $x$
   - on `chinese-remainder-map`: $x$ (generator indeterminate): A formal symbol, never evaluated, whose powers index the positions of the one-dimensional ring.
   - on [Telescoping identity](telescoping-identity.md): $x$ (list of numbers): A list of numbers indexed by position k, whose entry at position k is x_k.
428. $x_i$
   - on `chinese-remainder-map`: $x_i$ (axis indeterminate): The indeterminate of axis $i$ in the multidimensional ring.
   - on [Radix-digit convolution](radix-digit-convolution.md): $x_i$ (input digit): The digit of the first input $x$ at position $i$, a value from $0$ to $2^b-1$.
429. $x_i$
   - on `chinese-remainder-map`: $x_i$ (axis indeterminate): The indeterminate of axis $i$ in the multidimensional ring.
   - on [Transform axis](transform-axis.md): $x_i$ (axis coordinate): The coordinate of an address along axis i.
430. $\nu$
   - on `chinese-remainder-map`: $\nu$ (power exponent): A nonnegative integer exponent of $\Phi(x)$.
   - on [Mixed-radix digits](mixed-radix-digits.md): $\nu$ (integer being written): The integer whose mixed-radix expansion is taken, with 0 <= nu < Lambda.
431. $e$
   - on `chinese-remainder-map`: $e$ (coefficient index): An ordinary coefficient index in $[0,\Lambda)$, the position of a coefficient in the one-dimensional ring.
   - on [Congruence](congruence-modulo.md): $e$ (integer): An integer compared with $d$ modulo $B$.
432. $e$
   - on `chinese-remainder-map`: $e$ (coefficient index): An ordinary coefficient index in $[0,\Lambda)$, the position of a coefficient in the one-dimensional ring.
   - on [Telescoping identity](telescoping-identity.md): $e$ (last position): The last position of a sum over positions, the upper limit of the sum.
433. $a$
   - on `chinese-remainder-map`: $a$ (first exponent): The smaller of two exponents of $\Phi(x)$ compared for equality, an integer with $0\le a<\Lambda$.
   - on [Convolution](convolution.md): $a$ (first input sequence): The first of the two input sequences, of length $n$.
434. $b$
   - on `chinese-remainder-map`: $b$ (second exponent): The larger of two exponents of $\Phi(x)$ compared for equality, an integer with $a<b<\Lambda$.
   - on [Radix-digit convolution](radix-digit-convolution.md): $b$ (digit width): The number of bits in each digit of an input.
435. $b$
   - on `chinese-remainder-map`: $b$ (second exponent): The larger of two exponents of $\Phi(x)$ compared for equality, an integer with $a<b<\Lambda$.
   - on [Integer](integer.md): $b$ (base): The base (radix) of a digit representation, an integer at least 2.
436. $b$
   - on `chinese-remainder-map`: $b$ (second exponent): The larger of two exponents of $\Phi(x)$ compared for equality, an integer with $a<b<\Lambda$.
   - on [Convolution](convolution.md): $b$ (second input sequence): The second of the two input sequences, of length $n$.
437. $b$
   - on `chinese-remainder-map`: $b$ (second exponent): The larger of two exponents of $\Phi(x)$ compared for equality, an integer with $a<b<\Lambda$.
   - on [Logarithm](logarithm.md): $b$ (base): The fixed base of the logarithm, a number greater than 1.
438. $k$
   - on `chinese-remainder-map`: $k$ (exponent): A nonnegative integer exponent of $x_i$, the power to which the indeterminate of axis $i$ is raised.
   - on [Cyclic convolution](cyclic-convolution.md): $k$ (output position): The position of an entry of the output $f \ast g$, running from 0 to n-1.
439. $k$
   - on `chinese-remainder-map`: $k$ (exponent): A nonnegative integer exponent of $x_i$, the power to which the indeterminate of axis $i$ is raised.
   - on [Integer](integer.md): $k$ (digit count): The number of digits in a digit list.
440. $k$
   - on `chinese-remainder-map`: $k$ (exponent): A nonnegative integer exponent of $x_i$, the power to which the indeterminate of axis $i$ is raised.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $k$ (padded length): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
441. $k$
   - on `chinese-remainder-map`: $k$ (exponent): A nonnegative integer exponent of $x_i$, the power to which the indeterminate of axis $i$ is raised.
   - on [Root of unity](root-of-unity.md): $k$ (integer exponent): An integer exponent of $y$ in the power $y^k$ that multiplies the coefficient list.
442. $k$
   - on `chinese-remainder-map`: $k$ (exponent): A nonnegative integer exponent of $x_i$, the power to which the indeterminate of axis $i$ is raised.
   - on [Telescoping identity](telescoping-identity.md): $k$ (term position): The position of a term in the sequence, running from 0 to o.
443. $\sigma$
   - on `chinese-remainder-map`: $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
   - on [Ring homomorphism and isomorphism](ring-homomorphism.md): $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
444. $\sigma$
   - on `chinese-remainder-map`: $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
   - on [Modular inverse](modular-inverse.md): $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
445. $\sigma$
   - on `chinese-remainder-map`: $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
446. $\sigma$
   - on `chinese-remainder-map`: $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
447. $\sigma$
   - on `chinese-remainder-map`: $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
448. $\sigma$
   - on `chinese-remainder-map`: $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
449. $\sigma$
   - on `chinese-remainder-map`: $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
450. $\sigma$
   - on `chinese-remainder-map`: $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
451. $\sigma$
   - on `chinese-remainder-map`: $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
452. $\sigma$
   - on `chinese-remainder-map`: $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
   - on [Bézout's identity](bezout-identity.md): $\sigma$ (Bézout coefficient of γ): The integer multiplying γ in the combination βρ+γσ that equals gcd(β,γ).
453. $\sigma$
   - on `chinese-remainder-map`: $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
454. $\sigma$
   - on `chinese-remainder-map`: $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
   - on [Chinese remainder theorem](chinese-remainder-theorem.md): $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
455. $m$
   - on `opposite-transform`: $m$ (summation index): A dummy summation index running from $0$ to $q-1$ that names an input position of a vector; it counts nothing.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
456. $m$
   - on `opposite-transform`: $m$ (summation index): A dummy summation index running from $0$ to $q-1$ that names an input position of a vector; it counts nothing.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
457. $m$
   - on `opposite-transform`: $m$ (summation index): A dummy summation index running from $0$ to $q-1$ that names an input position of a vector; it counts nothing.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
458. $n$
   - on `opposite-transform`: $n$ (second summation index): A second dummy summation index running from $0$ to $q-1$ that names an input position of a second vector.
   - on [Logarithm](logarithm.md): $n$ (input integer): The positive integer whose base-2 logarithm is taken.
459. $n$
   - on `opposite-transform`: $n$ (second summation index): A second dummy summation index running from $0$ to $q-1$ that names an input position of a second vector.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $n$ (input length): The number of bits in each of the two inputs $x$ and $y$.
460. $n$
   - on `opposite-transform`: $n$ (second summation index): A second dummy summation index running from $0$ to $q-1$ that names an input position of a second vector.
   - on [Running time cost](running-time-cost.md): $n$ (input length): The number of cells that hold the input, which is the argument of the running time cost.
461. $n$
   - on `opposite-transform`: $n$ (second summation index): A second dummy summation index running from $0$ to $q-1$ that names an input position of a second vector.
   - on [Convolution](convolution.md): $n$ (entries per input): The number of entries in each input sequence.
462. $M$
   - on `opposite-transform`: $M$ (cyclic address count): The number of cyclic addresses of each array, which counts the entries along the cyclic axes.
   - on [Running time cost](running-time-cost.md): $M$ (example machine): The example machine that reads cells from the first cell until it finds a $1$ or reaches the last cell.
463. $M$
   - on `opposite-transform`: $M$ (cyclic address count): The number of cyclic addresses of each array, which counts the entries along the cyclic axes.
   - on [Linear algebra basics](linear-algebra-basics.md): $M$ (shear matrix): A matrix over F_2 that determines the shear.
464. $f$
   - on `opposite-transform`: $f$ (first input array): The first of the two disk-grid ring arrays whose convolution is taken.
   - on [Big-Theta notation](big-theta-notation.md): $f$ (bounded function): The function from input sizes to nonnegative reals whose order is compared with that of $h$.
465. $f$
   - on `opposite-transform`: $f$ (first input array): The first of the two disk-grid ring arrays whose convolution is taken.
   - on [Bijection](bijection.md): $f$ (map): The map from the source set $U$ to the target set $W$ whose bijectivity is tested.
466. $f$
   - on `opposite-transform`: $f$ (first input array): The first of the two disk-grid ring arrays whose convolution is taken.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $f$ (input vector): A vector of $q$ complex numbers, the input to the transform, with coordinates $f_0, \ldots, f_{q-1}$.
467. $f$
   - on `opposite-transform`: $f$ (first input array): The first of the two disk-grid ring arrays whose convolution is taken.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $f$ (input list): The list of $N$ records that the transform takes as input.
468. $f$
   - on `opposite-transform`: $f$ (first input array): The first of the two disk-grid ring arrays whose convolution is taken.
   - on [Frequency domain](frequency-domain.md): $f$ (sequence): A sequence $f=(f_0,\ldots,f_{q-1})$ of $q$ complex numbers, whose frequency domain is taken.
469. $g$
   - on `opposite-transform`: $g$ (second input array): The second of the two disk-grid ring arrays whose convolution is taken.
   - on [Linear algebra basics](linear-algebra-basics.md): $g$ (logical array): The array the computation means.
470. $c$
   - on `near-linear-time`: $c$ (log exponent): A fixed real number, the power to which the logarithm factor of a near-linear bound is raised.
   - on [Integer](integer.md): $c$ (digit): A digit of a digit list, an integer between 0 and the base minus one.
471. $\sigma$
   - on `negacyclic-convolution`: $\sigma$ (negacyclic convolution): The sequence of n complex numbers that is the negacyclic convolution of a and b.
   - on [Modular inverse](modular-inverse.md): $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
472. $\sigma$
   - on `negacyclic-convolution`: $\sigma$ (negacyclic convolution): The sequence of n complex numbers that is the negacyclic convolution of a and b.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
473. $\sigma$
   - on `negacyclic-convolution`: $\sigma$ (negacyclic convolution): The sequence of n complex numbers that is the negacyclic convolution of a and b.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
474. $\sigma$
   - on `negacyclic-convolution`: $\sigma$ (negacyclic convolution): The sequence of n complex numbers that is the negacyclic convolution of a and b.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
475. $\sigma$
   - on `negacyclic-convolution`: $\sigma$ (negacyclic convolution): The sequence of n complex numbers that is the negacyclic convolution of a and b.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
476. $\sigma$
   - on `negacyclic-convolution`: $\sigma$ (negacyclic convolution): The sequence of n complex numbers that is the negacyclic convolution of a and b.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
477. $\sigma$
   - on `negacyclic-convolution`: $\sigma$ (negacyclic convolution): The sequence of n complex numbers that is the negacyclic convolution of a and b.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
478. $\sigma$
   - on `negacyclic-convolution`: $\sigma$ (negacyclic convolution): The sequence of n complex numbers that is the negacyclic convolution of a and b.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
479. $\sigma$
   - on `negacyclic-convolution`: $\sigma$ (negacyclic convolution): The sequence of n complex numbers that is the negacyclic convolution of a and b.
   - on [Bézout's identity](bezout-identity.md): $\sigma$ (Bézout coefficient of γ): The integer multiplying γ in the combination βρ+γσ that equals gcd(β,γ).
480. $\sigma$
   - on `negacyclic-convolution`: $\sigma$ (negacyclic convolution): The sequence of n complex numbers that is the negacyclic convolution of a and b.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
481. $\sigma$
   - on `negacyclic-convolution`: $\sigma$ (negacyclic convolution): The sequence of n complex numbers that is the negacyclic convolution of a and b.
   - on [Chinese remainder theorem](chinese-remainder-theorem.md): $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
482. $\alpha$
   - on `neumann-series`: $\alpha$ (construction parameter): A parameter of the paper's construction, not the address letter of earlier pages.
   - on [Address](address.md): $\alpha$ (address string): A binary string of $d$ bits that labels one entry of the array.
483. $N$
   - on `neumann-series`: $N$ (paper's operator): The operator $I+J$ of the paper, with $J=N-I$; the letter changes meaning from earlier pages.
   - on [Address](address.md): $N$ (entry count): The number of entries in the array, counting each stored entry once; it counts the positions $0$ through $N-1$.
484. $\Pr$
   - on `independence`: $\Pr$ (probability function): The function that assigns each event a number between 0 and 1.
   - on [Probability](probability.md): $\Pr$ (probability): The function giving the probability $\Pr(\mathcal{A})$ of an event $\mathcal{A}$, a real number between 0 and 1.
485. $\sigma$
   - on `radix-two-factorization`: $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
486. $\sigma$
   - on `radix-two-factorization`: $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
487. $\sigma$
   - on `radix-two-factorization`: $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
488. $\sigma$
   - on `radix-two-factorization`: $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
489. $\sigma$
   - on `radix-two-factorization`: $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
490. $\sigma$
   - on `multidimensional-transform`: $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\sigma$ (shift count): The number of places a shift moves each coefficient.
491. $\sigma$
   - on `multidimensional-transform`: $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
492. $\sigma$
   - on `multidimensional-transform`: $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
   - on [Radix-two factorization](radix-two-factorization.md): $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
493. $\sigma$
   - on `multidimensional-transform`: $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
494. $\sigma$
   - on `multidimensional-transform`: $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
495. $\sigma$
   - on `multidimensional-transform`: $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
496. $\sigma$
   - on `multidimensional-transform`: $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
497. $k$
   - on `multidimensional-transform`: $k$ (radix-two exponent): The exponent with t_sigma equal to 2^k, which counts the radix-two levels of the axis transform.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $k$ (padded length): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
498. $k$
   - on `multidimensional-transform`: $k$ (radix-two exponent): The exponent with t_sigma equal to 2^k, which counts the radix-two levels of the axis transform.
   - on [Integer](integer.md): $k$ (digit count): The number of digits in a digit list.
499. $k$
   - on `multidimensional-transform`: $k$ (radix-two exponent): The exponent with t_sigma equal to 2^k, which counts the radix-two levels of the axis transform.
   - on [Root of unity](root-of-unity.md): $k$ (integer exponent): An integer exponent of $y$ in the power $y^k$ that multiplies the coefficient list.
500. $W$
   - on `gaussian-resampling`: $W$ (target length): The number of entries of the resampled vector, a power of two greater than $q$.
   - on [Coprime](coprime.md): $W$ (family product): The product f_1 times f_2 up to f_J, which is the least positive integer divisible by every member.
501. $W$
   - on `gaussian-resampling`: $W$ (target length): The number of entries of the resampled vector, a power of two greater than $q$.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $W$ (second butterfly entry): The entry of a butterfly pair at position $\gamma+\eta$ of the block.
502. $W$
   - on `gaussian-resampling`: $W$ (target length): The number of entries of the resampled vector, a power of two greater than $q$.
   - on [Permutation](permutation.md): $W$ (position set): The finite set of positions on which a permutation acts.
503. $W$
   - on `gaussian-resampling`: $W$ (target length): The number of entries of the resampled vector, a power of two greater than $q$.
   - on [Bijection](bijection.md): $W$ (target set): The set that the map $f$ sends its inputs into, the set of outputs.
504. $\sigma$
   - on `gaussian-resampling`: $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
505. $\sigma$
   - on `gaussian-resampling`: $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
506. $\sigma$
   - on `gaussian-resampling`: $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
   - on [Multidimensional transform](multidimensional-transform.md): $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
507. $\sigma$
   - on `gaussian-resampling`: $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\sigma$ (shift count): The number of places a shift moves each coefficient.
508. $\sigma$
   - on `gaussian-resampling`: $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
   - on [Radix-two factorization](radix-two-factorization.md): $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
509. $\sigma$
   - on `gaussian-resampling`: $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
510. $\sigma$
   - on `gaussian-resampling`: $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
511. $\sigma$
   - on `gaussian-resampling`: $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
512. $\sigma$
   - on `gaussian-resampling`: $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
513. $k$
   - on `gaussian-resampling`: $k$ (output index): The index of an entry of a length-$W$ output vector, running from $0$ to $W-1$.
   - on [Root of unity](root-of-unity.md): $k$ (integer exponent): An integer exponent of $y$ in the power $y^k$ that multiplies the coefficient list.
514. $k$
   - on `gaussian-resampling`: $k$ (output index): The index of an entry of a length-$W$ output vector, running from $0$ to $W-1$.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $k$ (padded length): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
515. $k$
   - on `gaussian-resampling`: $k$ (output index): The index of an entry of a length-$W$ output vector, running from $0$ to $W-1$.
   - on [Multidimensional transform](multidimensional-transform.md): $k$ (radix-two exponent): The exponent with t_sigma equal to 2^k, which counts the radix-two levels of the axis transform.
516. $k$
   - on `gaussian-resampling`: $k$ (output index): The index of an entry of a length-$W$ output vector, running from $0$ to $W-1$.
   - on [Integer](integer.md): $k$ (digit count): The number of digits in a digit list.
517. $\gamma$
   - on `matrix-rank`: $\gamma$ (first field value): The value of the field $H_i$ before one update.
   - on [Linear algebra basics](linear-algebra-basics.md): $\gamma$ (scalar): A scalar in F multiplying a vector.
518. $\gamma$
   - on `matrix-rank`: $\gamma$ (first field value): The value of the field $H_i$ before one update.
   - on [Permutation](permutation.md): $\gamma$ (third entry): The entry of the sequence at position 3.
519. $\delta$
   - on `matrix-rank`: $\delta$ (second field value): The value of the field $J_j$ before one update.
   - on [Permutation](permutation.md): $\delta$ (fourth entry): The entry of the sequence at position 4.
520. $W$
   - on `matrix-rank`: $W$ (wire count): The number of wires of the paper's circuit, including its scratch wires.
   - on [Permutation](permutation.md): $W$ (position set): The finite set of positions on which a permutation acts.
521. $W$
   - on `matrix-rank`: $W$ (wire count): The number of wires of the paper's circuit, including its scratch wires.
   - on [Bijection](bijection.md): $W$ (target set): The set that the map $f$ sends its inputs into, the set of outputs.
522. $S$
   - on `symmetric-matrix`: $S$ (three-element subset): A three-element subset of a finite set, one of the two triples compared for neighbourhood.
   - on [Linear algebra basics](linear-algebra-basics.md): $S$ (inverse map): A linear map that inverts an invertible operator T.
523. $T$
   - on `symmetric-matrix`: $T$ (three-element subset): A three-element subset of a finite set, the second triple compared with $S$.
   - on [Linear algebra basics](linear-algebra-basics.md): $T$ (linear map): A linear map between vector spaces over F.
524. $V$
   - on `eigenvalue`: $V$ (vector space): The vector space on which the linear operator T acts, over the field F.
   - on [Directed graph](directed-graph.md): $V$ (vertex set): The set of vertices of the directed graph, the points that edges join.
525. $V$
   - on `eigenvalue`: $V$ (vector space): The vector space on which the linear operator T acts, over the field F.
   - on [Array](array.md): $V$ (stored bit volume): The number of stored data bits in an array, the volume in which cost bounds are stated.
526. $V$
   - on `eigenvalue`: $V$ (vector space): The vector space on which the linear operator T acts, over the field F.
   - on [Payload](payload.md): $V$ (stream volume): The number of bits stored in the stream, which the time bound counts.
527. $\langle x,y\rangle$
   - on `bilinear-form`: $\langle x,y\rangle$ (bilinear form): The scalar in F that the form assigns to the vectors x and y of E.
   - on [Eigenvalue](eigenvalue.md): $\langle x,y\rangle$ (bilinear value): The number that the bilinear form assigns to the pair of vectors x and y.
528. $U$
   - on `bilinear-form`: $U$ (subspace): A subspace of E whose orthogonal complement is taken.
   - on [Bijection](bijection.md): $U$ (source set): The set of inputs of the map $f$, each of which $f$ sends to an element of $W$.
529. $U$
   - on `bilinear-form`: $U$ (subspace): A subspace of E whose orthogonal complement is taken.
   - on [Bilinear map](bilinear-map.md): $U$ (first argument space): The vector space that the first argument of the bilinear map ranges over.
530. $x_i$
   - on `bilinear-form`: $x_i$ (coordinate): The i-th coordinate of the vector x in the basis e_1 through e_m.
   - on [Radix-digit convolution](radix-digit-convolution.md): $x_i$ (input digit): The digit of the first input $x$ at position $i$, a value from $0$ to $2^b-1$.
531. $y_j$
   - on `bilinear-form`: $y_j$ (coordinate of y): The j-th coordinate of the vector y in the basis e_1 through e_m.
   - on [Radix-digit convolution](radix-digit-convolution.md): $y_j$ (input digit of y): The digit of the second input $y$ at position $j$, defined as the digits of $x$ are.
532. $T$
   - on `bilinear-form`: $T$ (triple): A three-element subset of [h], one of the triples whose indicator vectors are used.
   - on [Linear algebra basics](linear-algebra-basics.md): $T$ (linear map): A linear map between vector spaces over F.
533. $T$
   - on `bilinear-form`: $T$ (triple): A three-element subset of [h], one of the triples whose indicator vectors are used.
   - on [Symmetric matrix](symmetric-matrix.md): $T$ (three-element subset): A three-element subset of a finite set, the second triple compared with $S$.
534. $S$
   - on `bilinear-form`: $S$ (second triple): A second three-element subset of [h], whose indicator vector is t_S.
   - on [Linear algebra basics](linear-algebra-basics.md): $S$ (inverse map): A linear map that inverts an invertible operator T.
535. $S$
   - on `bilinear-form`: $S$ (second triple): A second three-element subset of [h], whose indicator vector is t_S.
   - on [Symmetric matrix](symmetric-matrix.md): $S$ (three-element subset): A three-element subset of a finite set, one of the two triples compared for neighbourhood.
536. $X$
   - on `orthogonal-complement`: $X$ (vector space): A vector space over $F$ on which the bilinear form is defined.
   - on [Array norm](array-norm.md): $X$ (array): A finite array of complex values, whose norm is taken.
537. $W$
   - on `orthogonal-complement`: $W$ (larger label): The larger of the two labels on an edge, which contains the smaller label $U$.
   - on [Bit network](bit-network.md): $W$ (source bank): The bank of source bits, holding one bit $W_\sigma$ for each triple $\sigma$.
538. $W$
   - on `orthogonal-complement`: $W$ (larger label): The larger of the two labels on an edge, which contains the smaller label $U$.
   - on [Permutation](permutation.md): $W$ (position set): The finite set of positions on which a permutation acts.
539. $W$
   - on `orthogonal-complement`: $W$ (larger label): The larger of the two labels on an edge, which contains the smaller label $U$.
   - on [Bijection](bijection.md): $W$ (target set): The set that the map $f$ sends its inputs into, the set of outputs.
540. $W$
   - on `orthogonal-complement`: $W$ (larger label): The larger of the two labels on an edge, which contains the smaller label $U$.
   - on [Bilinear map](bilinear-map.md): $W$ (output space): The vector space that the bilinear map returns its values in.
541. $S$
   - on `indicator-vector`: $S$ (triple): A single three-element subset of [h], one of the two triples in a neighbor pair.
   - on [Bilinear form](bilinear-form.md): $S$ (second triple): A second three-element subset of [h], whose indicator vector is t_S.
542. $S$
   - on `indicator-vector`: $S$ (triple): A single three-element subset of [h], one of the two triples in a neighbor pair.
   - on [Linear algebra basics](linear-algebra-basics.md): $S$ (inverse map): A linear map that inverts an invertible operator T.
543. $S$
   - on `indicator-vector`: $S$ (triple): A single three-element subset of [h], one of the two triples in a neighbor pair.
   - on [Symmetric matrix](symmetric-matrix.md): $S$ (three-element subset): A three-element subset of a finite set, one of the two triples compared for neighbourhood.
544. $T$
   - on `indicator-vector`: $T$ (triple): A single three-element subset of [h]; on the ground-set page T names all triples.
   - on [Linear algebra basics](linear-algebra-basics.md): $T$ (linear map): A linear map between vector spaces over F.
545. $T$
   - on `indicator-vector`: $T$ (triple): A single three-element subset of [h]; on the ground-set page T names all triples.
   - on [Symmetric matrix](symmetric-matrix.md): $T$ (three-element subset): A three-element subset of a finite set, the second triple compared with $S$.
546. $e$
   - on `indicator-vector`: $e$ (position): An element of the ground set [h], a position of the indicator vector.
   - on [Congruence](congruence-modulo.md): $e$ (integer): An integer compared with $d$ modulo $B$.
547. $e$
   - on `indicator-vector`: $e$ (position): An element of the ground set [h], a position of the indicator vector.
   - on [Eigenvalue](eigenvalue.md): $e$ (eigenvector): A nonzero vector of V that T maps to a multiple of itself.
548. $J$
   - on `indicator-vector`: $J$ (all-ones matrix): The h by h matrix whose entries are all 1.
   - on [Radix-digit convolution](radix-digit-convolution.md): $J$ (digit count): The number of digits in each input, that is, the number of blocks of $b$ bits.
549. $J$
   - on `indicator-vector`: $J$ (all-ones matrix): The h by h matrix whose entries are all 1.
   - on [Cyclic shift](cyclic-shift.md): $J$ (block length): The number of positions in the block that the shift rotates, a count of those positions.
550. $J$
   - on `indicator-vector`: $J$ (all-ones matrix): The h by h matrix whose entries are all 1.
   - on [Eigenvalue](eigenvalue.md): $J$ (all-one matrix): The h by h matrix with every entry equal to 1.
551. $\sigma$
   - on `line-spanned-by-vector`: $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
552. $\sigma$
   - on `line-spanned-by-vector`: $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
553. $\sigma$
   - on `line-spanned-by-vector`: $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
554. $\sigma$
   - on `line-spanned-by-vector`: $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
   - on [Bit network](bit-network.md): $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
555. $\sigma$
   - on `line-spanned-by-vector`: $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
556. $\sigma$
   - on `line-spanned-by-vector`: $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
557. $\sigma$
   - on `line-spanned-by-vector`: $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
558. $\sigma$
   - on `line-spanned-by-vector`: $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
559. $\sigma$
   - on `line-spanned-by-vector`: $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
560. $\sigma$
   - on `line-spanned-by-vector`: $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
561. $\sigma$
   - on `line-spanned-by-vector`: $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
   - on [Tensor product](tensor-product.md): $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
562. $U$
   - on `subspace-labels`: $U$ (label): A label of a wire, a nondegenerate subspace of the fixed space E.
   - on [Bijection](bijection.md): $U$ (source set): The set of inputs of the map $f$, each of which $f$ sends to an element of $W$.
563. $U$
   - on `subspace-labels`: $U$ (label): A label of a wire, a nondegenerate subspace of the fixed space E.
   - on [Projection along a subspace](projection-along-subspace.md): $U$ (subspace): A subspace of $W$ onto which a vector is projected.
564. $U$
   - on `subspace-labels`: $U$ (label): A label of a wire, a nondegenerate subspace of the fixed space E.
   - on [Bilinear form](bilinear-form.md): $U$ (subspace): A subspace of E whose orthogonal complement is taken.
565. $U$
   - on `subspace-labels`: $U$ (label): A label of a wire, a nondegenerate subspace of the fixed space E.
   - on [Bilinear map](bilinear-map.md): $U$ (first argument space): The vector space that the first argument of the bilinear map ranges over.
566. $s$
   - on `subspace-labels`: $s$ (basis index): An index numbering the basis vectors of an edge residual.
   - on [Ceiling function](ceiling-function.md): $s$ (real number): The real number that the ceiling rounds up to an integer.
567. $s$
   - on `subspace-labels`: $s$ (basis index): An index numbering the basis vectors of an edge residual.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $s$ (input index): An integer index running over $0, 1, \ldots, q-1$ that labels an input coordinate $f_s$.
568. $s$
   - on `subspace-labels`: $s$ (basis index): An index numbering the basis vectors of an edge residual.
   - on [Array norm](array-norm.md): $s$ (coefficient index): The index of a coefficient of a ring element, running from 0 to r-1.
569. $s$
   - on `subspace-labels`: $s$ (basis index): An index numbering the basis vectors of an edge residual.
   - on [Transform axis](transform-axis.md): $s$ (coefficient count): A power of two that is the number of coefficients of the stored polynomial, which is also the length of its axis.
570. $\mathcal T$
   - on `subset-intersection-network`: $\mathcal T$ (triple set): The set of all three-element subsets of the ground set $[h]$, whose members are the triples.
   - on [Ground set](ground-set.md): $\mathcal T$ (three-element subsets): The set of all three-element subsets of $[h]$.
571. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Dual space](dual-space.md): $\sigma$ (example functional): The linear functional on R^2 sending x to 3x_1 - x_2.
572. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Bit network](bit-network.md): $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
573. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
574. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
575. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
576. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
577. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
578. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
579. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
580. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
581. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
582. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Line spanned by a vector](line-spanned-by-vector.md): $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
583. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Tensor product](tensor-product.md): $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
584. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
585. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
586. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
587. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
588. $\sigma$
   - on `subset-intersection-network`: $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
589. $\xi$
   - on `subset-intersection-network`: $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
   - on [Permutation](permutation.md): $\xi$ (address): The position of one entry of an array.
590. $\xi$
   - on `subset-intersection-network`: $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
591. $\xi$
   - on `subset-intersection-network`: $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
592. $\xi$
   - on `subset-intersection-network`: $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
   - on [Congruence](congruence-modulo.md): $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
593. $\xi$
   - on `subset-intersection-network`: $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
   - on [Radix-digit convolution](radix-digit-convolution.md): $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
594. $\xi$
   - on `subset-intersection-network`: $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
   - on [Butterfly](butterfly.md): $\xi$ (first input value): The first of the two input values of the butterfly.
595. $\xi$
   - on `subset-intersection-network`: $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
   - on [Bilinear map](bilinear-map.md): $\xi$ (first argument): An arbitrary element of the first argument space $U$.
596. $\xi$
   - on `subset-intersection-network`: $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
   - on [Tensor product](tensor-product.md): $\xi$ (row index): A row index of $P$, and in an address the output bit string $\xi$.
597. $\xi$
   - on `subset-intersection-network`: $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
   - on [Ring](ring.md): $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
598. $\xi$
   - on `subset-intersection-network`: $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
599. $\xi$
   - on `subset-intersection-network`: $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
   - on [Cyclic group](cyclic-group.md): $\xi$ (exponent): An integer to which the generator is raised, giving the power $\rho^\xi$.
600. $\xi$
   - on `subset-intersection-network`: $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
   - on [Coprime](coprime.md): $\xi$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the first of the two Bezout coefficients.
601. $\eta$
   - on `subset-intersection-network`: $\eta$ (target vector): The vector, indexed by triples, of the entries of the target bank along the varying coordinate.
   - on [Linear algebra basics](linear-algebra-basics.md): $\eta$ (scalar): A scalar in F multiplying a vector.
602. $\eta$
   - on `subset-intersection-network`: $\eta$ (target vector): The vector, indexed by triples, of the entries of the target bank along the varying coordinate.
   - on [Congruence](congruence-modulo.md): $\eta$ (second multiple): The integer with $e'-e=\eta B$.
603. $\ell$
   - on `subset-intersection-network`: $\ell$ (ground element): An element of the ground set $[h]$, which names one central wire.
   - on [Linear networks and frames](linear-network-frames.md): $\ell$ (input wire): An input wire of the network, whose supplied array and source vertex are named.
604. $\ell$
   - on `subset-intersection-network`: $\ell$ (ground element): An element of the ground set $[h]$, which names one central wire.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\ell$ (output index): An integer index running over $0, 1, \ldots, q-1$ that labels an output coordinate $(F_q f)_\ell$.
605. $x$
   - on `scratch-storage`: $x$ (control vector): The control vector, whose entry at triple $T$ is $x_T$.
   - on [Linear algebra basics](linear-algebra-basics.md): $x$ (vector): A vector in a vector space, changed from earlier pages.
606. $x$
   - on `scratch-storage`: $x$ (control vector): The control vector, whose entry at triple $T$ is $x_T$.
   - on [Integer](integer.md): $x$ (binary string): A binary string of bits, read as an integer by the paper's rule.
607. $x$
   - on `scratch-storage`: $x$ (control vector): The control vector, whose entry at triple $T$ is $x_T$.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $x$ (first input): The first binary input string, of length $n$.
608. $x$
   - on `scratch-storage`: $x$ (control vector): The control vector, whose entry at triple $T$ is $x_T$.
   - on [Phase factor](phase-factor.md): $x$ (address): An address whose selected bits are $x_1,\dots,x_D$, each 0 or 1.
609. $x$
   - on `scratch-storage`: $x$ (control vector): The control vector, whose entry at triple $T$ is $x_T$.
   - on [Order of an element](order-of-element.md): $x$ (indeterminate): The indeterminate of the ring C[x] modulo x^S minus 1, whose image the map sends to a product of axis indeterminates.
610. $y$
   - on `scratch-storage`: $y$ (target vector): The target vector, whose entry at triple $S$ is $y_S$.
   - on [Linear algebra basics](linear-algebra-basics.md): $y$ (vector): A vector in a vector space, changed from earlier pages.
611. $y$
   - on `scratch-storage`: $y$ (target vector): The target vector, whose entry at triple $S$ is $y_S$.
   - on [Logarithm](logarithm.md): $y$ (argument): The positive number whose logarithm is taken.
612. $y$
   - on `scratch-storage`: $y$ (target vector): The target vector, whose entry at triple $S$ is $y_S$.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $y$ (second input): The second binary input string, of length $n$.
613. $y$
   - on `scratch-storage`: $y$ (target vector): The target vector, whose entry at triple $S$ is $y_S$.
   - on [Root of unity](root-of-unity.md): $y$ (polynomial variable): The variable of the polynomial ring $\mathbb{C}[y]/(y^4+1)$, in which $y^4 = -1$; this replaces the logarithm page's meaning of $y$ on this page.
614. $a$
   - on `scratch-storage`: $a$ (starting side values): The vector of starting values of the side wires.
   - on [Convolution](convolution.md): $a$ (first input sequence): The first of the two input sequences, of length $n$.
615. $c$
   - on `scratch-storage`: $c$ (starting central values): The vector of starting values of the central wires.
   - on [Eigenvalue](eigenvalue.md): $c$ (average entry): The average of the entries of x, which is the coefficient of the all-ones vector in its split.
616. $c$
   - on `scratch-storage`: $c$ (starting central values): The vector of starting values of the central wires.
   - on [Integer](integer.md): $c$ (digit): A digit of a digit list, an integer between 0 and the base minus one.
617. $c$
   - on `scratch-storage`: $c$ (starting central values): The vector of starting values of the central wires.
   - on [Convolution](convolution.md): $c$ (convolution): The convolution of $a$ and $b$, a sequence of length $2n-1$.
618. $V$
   - on `scratch-storage`: $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
   - on [Linear functional](linear-functional.md): $V$ (vector space): The vector space over F whose vectors a linear functional takes as input.
619. $V$
   - on `scratch-storage`: $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
   - on [Directed graph](directed-graph.md): $V$ (vertex set): The set of vertices of the directed graph, the points that edges join.
620. $V$
   - on `scratch-storage`: $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
   - on [Array](array.md): $V$ (stored bit volume): The number of stored data bits in an array, the volume in which cost bounds are stated.
621. $V$
   - on `scratch-storage`: $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
   - on [Payload](payload.md): $V$ (stream volume): The number of bits stored in the stream, which the time bound counts.
622. $V$
   - on `scratch-storage`: $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
   - on [Eigenvalue](eigenvalue.md): $V$ (vector space): The vector space on which the linear operator T acts, over the field F.
623. $V$
   - on `scratch-storage`: $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
   - on [Big-Theta notation](big-theta-notation.md): $V$ (stored bit volume): The number of stored bits, which is of order $n$.
624. $V$
   - on `scratch-storage`: $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
   - on [Cyclic shift](cyclic-shift.md): $V$ (stored bit volume): The number of stored bits in the array, a count of its data bits.
625. $V$
   - on `scratch-storage`: $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
   - on [Bilinear map](bilinear-map.md): $V$ (second argument space): The vector space that the second argument of the bilinear map ranges over.
626. $V$
   - on `scratch-storage`: $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
   - on [Projection along a subspace](projection-along-subspace.md): $V$ (larger nested subspace): A nondegenerate subspace containing $U$, the larger of two nested labels.
627. $J$
   - on `scratch-storage`: $J$ (side injection): The operation that adds to $y_S$ the side wires over the neighbours of $S$.
   - on [Eigenvalue](eigenvalue.md): $J$ (all-one matrix): The h by h matrix with every entry equal to 1.
628. $J$
   - on `scratch-storage`: $J$ (side injection): The operation that adds to $y_S$ the side wires over the neighbours of $S$.
   - on [Radix-digit convolution](radix-digit-convolution.md): $J$ (digit count): The number of digits in each input, that is, the number of blocks of $b$ bits.
629. $J$
   - on `scratch-storage`: $J$ (side injection): The operation that adds to $y_S$ the side wires over the neighbours of $S$.
   - on [Cyclic shift](cyclic-shift.md): $J$ (block length): The number of positions in the block that the shift rotates, a count of those positions.
630. $J$
   - on `scratch-storage`: $J$ (side injection): The operation that adds to $y_S$ the side wires over the neighbours of $S$.
   - on [Tensor product](tensor-product.md): $J$ (factor count): The number of factors in a tensor power, which is also the number of coordinates it acts on.
631. $J$
   - on `scratch-storage`: $J$ (side injection): The operation that adds to $y_S$ the side wires over the neighbours of $S$.
   - on [Indicator vector](indicator-vector.md): $J$ (all-ones matrix): The h by h matrix whose entries are all 1.
632. $J$
   - on `scratch-storage`: $J$ (side injection): The operation that adds to $y_S$ the side wires over the neighbours of $S$.
   - on [Coprime](coprime.md): $J$ (family size): The number of integers in the family f_1 to f_J.
633. $G$
   - on `scratch-storage`: $G$ (gather): The operation that adds $x_T$ to each central wire $C_\ell$ with $\ell\in T$.
   - on [Directed graph](directed-graph.md): $G$ (directed graph): The directed graph, written as the pair of its vertex set V and its edge set E.
634. $G$
   - on `scratch-storage`: $G$ (gather): The operation that adds $x_T$ to each central wire $C_\ell$ with $\ell\in T$.
   - on [Linear networks and frames](linear-network-frames.md): $G$ (pointwise gate): A pointwise linear gate, which combines its inputs the same way at every address.
635. $G$
   - on `scratch-storage`: $G$ (gather): The operation that adds $x_T$ to each central wire $C_\ell$ with $\ell\in T$.
   - on [Permutation](permutation.md): $G$ (array): An array whose entries are stored at addresses.
636. $G$
   - on `scratch-storage`: $G$ (gather): The operation that adds $x_T$ to each central wire $C_\ell$ with $\ell\in T$.
   - on [Bijection](bijection.md): $G$ (singled-out set): A subset of the source set $U$ singled out by the argument, which is where two bijections may differ: the bad addresses.
637. $G$
   - on `scratch-storage`: $G$ (gather): The operation that adds $x_T$ to each central wire $C_\ell$ with $\ell\in T$.
   - on [Order of an element](order-of-element.md): $G$ (group): The group in which the order of sigma is taken, a set with an associative operation, an identity, and inverses.
638. $G$
   - on `scratch-storage`: $G$ (gather): The operation that adds $x_T$ to each central wire $C_\ell$ with $\ell\in T$.
   - on [Coprime](coprime.md): $G$ (transform group): The product group Z/f_1 times ... times Z/f_J, with tuples added entrywise.
639. $R$
   - on `scratch-storage`: $R$ (scatter): The operation that adds to $y_S$ the central wires $C_\ell$ with $\ell\in S$.
   - on [Ring](ring.md): $R$ (ring): A set with an addition and a multiplication that satisfy the axioms listed on this page.
640. $\tau$
   - on `address-interchange`: $\tau$ (fixed exponent): A fixed number below 1, the exponent in the cost bound $O(Vu^{\tau})$.
   - on [Extended real numbers](extended-reals.md): $\tau$ (sequence term): The term of a sequence at position $\delta$.
641. $x$
   - on `address-interchange`: $x$ (first field block): The bits of the first of the two address fields, read as a block at matching positions.
   - on [Scratch storage](scratch-storage.md): $x$ (control vector): The control vector, whose entry at triple $T$ is $x_T$.
642. $x$
   - on `address-interchange`: $x$ (first field block): The bits of the first of the two address fields, read as a block at matching positions.
   - on [Linear algebra basics](linear-algebra-basics.md): $x$ (vector): A vector in a vector space, changed from earlier pages.
643. $x$
   - on `address-interchange`: $x$ (first field block): The bits of the first of the two address fields, read as a block at matching positions.
   - on [Integer](integer.md): $x$ (binary string): A binary string of bits, read as an integer by the paper's rule.
644. $x$
   - on `address-interchange`: $x$ (first field block): The bits of the first of the two address fields, read as a block at matching positions.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $x$ (first input): The first binary input string, of length $n$.
645. $x$
   - on `address-interchange`: $x$ (first field block): The bits of the first of the two address fields, read as a block at matching positions.
   - on [Phase factor](phase-factor.md): $x$ (address): An address whose selected bits are $x_1,\dots,x_D$, each 0 or 1.
646. $x$
   - on `address-interchange`: $x$ (first field block): The bits of the first of the two address fields, read as a block at matching positions.
   - on [Order of an element](order-of-element.md): $x$ (indeterminate): The indeterminate of the ring C[x] modulo x^S minus 1, whose image the map sends to a product of axis indeterminates.
647. $y$
   - on `address-interchange`: $y$ (second field block): The bits of the second of the two address fields, read as a block at matching positions.
   - on [Scratch storage](scratch-storage.md): $y$ (target vector): The target vector, whose entry at triple $S$ is $y_S$.
648. $y$
   - on `address-interchange`: $y$ (second field block): The bits of the second of the two address fields, read as a block at matching positions.
   - on [Linear algebra basics](linear-algebra-basics.md): $y$ (vector): A vector in a vector space, changed from earlier pages.
649. $y$
   - on `address-interchange`: $y$ (second field block): The bits of the second of the two address fields, read as a block at matching positions.
   - on [Logarithm](logarithm.md): $y$ (argument): The positive number whose logarithm is taken.
650. $y$
   - on `address-interchange`: $y$ (second field block): The bits of the second of the two address fields, read as a block at matching positions.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $y$ (second input): The second binary input string, of length $n$.
651. $y$
   - on `address-interchange`: $y$ (second field block): The bits of the second of the two address fields, read as a block at matching positions.
   - on [Root of unity](root-of-unity.md): $y$ (polynomial variable): The variable of the polynomial ring $\mathbb{C}[y]/(y^4+1)$, in which $y^4 = -1$; this replaces the logarithm page's meaning of $y$ on this page.
652. $m$
   - on `address-interchange`: $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
653. $m$
   - on `address-interchange`: $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
654. $m$
   - on `address-interchange`: $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
655. $m$
   - on `address-interchange`: $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
   - on [Limit inferior](limit-inferior.md): $m$ (tail start): The position from which a tail of the sequence starts.
656. $k$
   - on `address-interchange`: $k$ (level count): The number of levels of the recursion, the logarithm to base m of the field width u.
   - on [Integer](integer.md): $k$ (digit count): The number of digits in a digit list.
657. $k$
   - on `address-interchange`: $k$ (level count): The number of levels of the recursion, the logarithm to base m of the field width u.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $k$ (padded length): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
658. $k$
   - on `address-interchange`: $k$ (level count): The number of levels of the recursion, the logarithm to base m of the field width u.
   - on [Root of unity](root-of-unity.md): $k$ (integer exponent): An integer exponent of $y$ in the power $y^k$ that multiplies the coefficient list.
659. $k$
   - on `address-interchange`: $k$ (level count): The number of levels of the recursion, the logarithm to base m of the field width u.
   - on [Limit inferior](limit-inferior.md): $k$ (term position): A position in a sequence, the index of a term.
660. $s$
   - on `address-interchange`: $s$ (smaller calls): The number of smaller calls one call makes, equal to the sum of the edge ranks.
   - on [Ceiling function](ceiling-function.md): $s$ (real number): The real number that the ceiling rounds up to an integer.
661. $s$
   - on `address-interchange`: $s$ (smaller calls): The number of smaller calls one call makes, equal to the sum of the edge ranks.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $s$ (input index): An integer index running over $0, 1, \ldots, q-1$ that labels an input coordinate $f_s$.
662. $s$
   - on `address-interchange`: $s$ (smaller calls): The number of smaller calls one call makes, equal to the sum of the edge ranks.
   - on [Array norm](array-norm.md): $s$ (coefficient index): The index of a coefficient of a ring element, running from 0 to r-1.
663. $s$
   - on `address-interchange`: $s$ (smaller calls): The number of smaller calls one call makes, equal to the sum of the edge ranks.
   - on [Subspace labels](subspace-labels.md): $s$ (basis index): An index numbering the basis vectors of an edge residual.
664. $s$
   - on `address-interchange`: $s$ (smaller calls): The number of smaller calls one call makes, equal to the sum of the edge ranks.
   - on [Transform axis](transform-axis.md): $s$ (coefficient count): A power of two that is the number of coefficients of the stored polynomial, which is also the length of its axis.
665. $j$
   - on `address-interchange`: $j$ (level index): The level of a call, so a call on width $m^j$ sits at level $j$.
   - on [Linear algebra basics](linear-algebra-basics.md): $j$ (coordinate index): The index of a coordinate of a vector, running from 1 to m.
666. $j$
   - on `address-interchange`: $j$ (level index): The level of a call, so a call on width $m^j$ sits at level $j$.
   - on [Integer](integer.md): $j$ (digit position): The position of a digit or bit, counted from the left starting at 1.
667. $j$
   - on `address-interchange`: $j$ (level index): The level of a call, so a call on width $m^j$ sits at level $j$.
   - on [Ceiling function](ceiling-function.md): $j$ (integer): Any integer, which is its own ceiling.
668. $j$
   - on `address-interchange`: $j$ (level index): The level of a call, so a call on width $m^j$ sits at level $j$.
   - on [Convolution](convolution.md): $j$ (input position in b): The position of an entry of $b$.
669. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
670. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
671. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
672. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Bit network](bit-network.md): $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
673. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
674. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
675. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
676. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
677. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
678. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
679. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Subset-intersection network](subset-intersection-network.md): $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
680. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Dual space](dual-space.md): $\sigma$ (example functional): The linear functional on R^2 sending x to 3x_1 - x_2.
681. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Line spanned by a vector](line-spanned-by-vector.md): $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
682. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Tensor product](tensor-product.md): $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
683. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
684. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
685. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
686. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
687. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
688. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Fixed-tape machine model](fixed-tape-model.md): $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
689. $\sigma$
   - on `xor`: $\sigma$ (first bit): A bit, a value 0 or 1, the first operand of the exclusive or.
   - on [Extended real numbers](extended-reals.md): $\sigma$ (generic real number): A real number used as a generic value in the order, sums and limit conditions.
690. $\sigma'$
   - on `xor`: $\sigma'$ (second bit): A bit, a value 0 or 1, the second operand of the exclusive or.
   - on [Binary field](binary-field.md): $\sigma'$ (second three-element subset): A second three-element subset of the ground set, the output side of the coefficient.
691. $\sigma'$
   - on `xor`: $\sigma'$ (second bit): A bit, a value 0 or 1, the second operand of the exclusive or.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\sigma'$ (second numerator): The Gaussian integer numerator of a second Gaussian dyadic $\sigma'/2^{\Gamma'}$.
692. $\sigma$
   - on `gram-matrix`: $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
   - on [Bit network](bit-network.md): $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
693. $\sigma$
   - on `gram-matrix`: $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
694. $\sigma$
   - on `gram-matrix`: $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
695. $\sigma$
   - on `gram-matrix`: $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
696. $\sigma$
   - on `gram-matrix`: $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
697. $\sigma$
   - on `gram-matrix`: $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
698. $\sigma$
   - on `gram-matrix`: $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
699. $\sigma$
   - on `gram-matrix`: $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
700. $\sigma$
   - on `gram-matrix`: $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
701. $\sigma$
   - on `gram-matrix`: $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
702. $H$
   - on `complex-phase-network`: $H$ (normalized Hadamard matrix): The 2 by 2 matrix whose tensor powers give the frames of the phase network.
   - on [Linear algebra basics](linear-algebra-basics.md): $H$ (address block): The first bit block of an address.
703. $C_U$
   - on `complex-phase-network`: $C_U$ (phase frame): The frame of a vertex with label U, an operator on arrays of addresses.
   - on [Subspace labels](subspace-labels.md): $C_U$ (label frame): The invertible operator on arrays carried by a vertex with label U.
704. $U$
   - on `complex-phase-network`: $U$ (tail label): The label at the tail of an edge.
   - on [Bilinear form](bilinear-form.md): $U$ (subspace): A subspace of E whose orthogonal complement is taken.
705. $U$
   - on `complex-phase-network`: $U$ (tail label): The label at the tail of an edge.
   - on [Bijection](bijection.md): $U$ (source set): The set of inputs of the map $f$, each of which $f$ sends to an element of $W$.
706. $U$
   - on `complex-phase-network`: $U$ (tail label): The label at the tail of an edge.
   - on [Bilinear map](bilinear-map.md): $U$ (first argument space): The vector space that the first argument of the bilinear map ranges over.
707. $U$
   - on `complex-phase-network`: $U$ (tail label): The label at the tail of an edge.
   - on [Subspace labels](subspace-labels.md): $U$ (label): A label of a wire, a nondegenerate subspace of the fixed space E.
708. $U$
   - on `complex-phase-network`: $U$ (tail label): The label at the tail of an edge.
   - on [Projection along a subspace](projection-along-subspace.md): $U$ (subspace): A subspace of $W$ onto which a vector is projected.
709. $U$
   - on `complex-phase-network`: $U$ (tail label): The label at the tail of an edge.
   - on [Dual space](dual-space.md): $U$ (vector space): A vector space over the field F, whose linear functionals form the dual space.
710. $V$
   - on `complex-phase-network`: $V$ (head label): The label at the head of an edge.
   - on [Directed graph](directed-graph.md): $V$ (vertex set): The set of vertices of the directed graph, the points that edges join.
711. $V$
   - on `complex-phase-network`: $V$ (head label): The label at the head of an edge.
   - on [Array](array.md): $V$ (stored bit volume): The number of stored data bits in an array, the volume in which cost bounds are stated.
712. $V$
   - on `complex-phase-network`: $V$ (head label): The label at the head of an edge.
   - on [Payload](payload.md): $V$ (stream volume): The number of bits stored in the stream, which the time bound counts.
713. $V$
   - on `complex-phase-network`: $V$ (head label): The label at the head of an edge.
   - on [Big-Theta notation](big-theta-notation.md): $V$ (stored bit volume): The number of stored bits, which is of order $n$.
714. $V$
   - on `complex-phase-network`: $V$ (head label): The label at the head of an edge.
   - on [Cyclic shift](cyclic-shift.md): $V$ (stored bit volume): The number of stored bits in the array, a count of its data bits.
715. $V$
   - on `complex-phase-network`: $V$ (head label): The label at the head of an edge.
   - on [Eigenvalue](eigenvalue.md): $V$ (vector space): The vector space on which the linear operator T acts, over the field F.
716. $V$
   - on `complex-phase-network`: $V$ (head label): The label at the head of an edge.
   - on [Bilinear map](bilinear-map.md): $V$ (second argument space): The vector space that the second argument of the bilinear map ranges over.
717. $V$
   - on `complex-phase-network`: $V$ (head label): The label at the head of an edge.
   - on [Linear functional](linear-functional.md): $V$ (vector space): The vector space over F whose vectors a linear functional takes as input.
718. $V$
   - on `complex-phase-network`: $V$ (head label): The label at the head of an edge.
   - on [Projection along a subspace](projection-along-subspace.md): $V$ (larger nested subspace): A nondegenerate subspace containing $U$, the larger of two nested labels.
719. $X_v$
   - on `complex-phase-network`: $X_v$ (translation by v): The operator sending a function f to (X_v f)(x) = f(x+v) on addresses.
   - on [Subspace labels](subspace-labels.md): $X_v$ (translation): The operator that shifts a function of addresses by the binary vector v.
720. $D$
   - on `simultaneous-butterfly-layer`: $D$ (number of axes): The number of transform axes that the layer acts on, one selected bit on each.
   - on [Phase factor](phase-factor.md): $D$ (selected bit count): The number of selected address bits on which a butterfly layer acts.
721. $D$
   - on `simultaneous-butterfly-layer`: $D$ (number of axes): The number of transform axes that the layer acts on, one selected bit on each.
   - on [Transform axis](transform-axis.md): $D$ (axis count): The number of axes of the array.
722. $\delta$
   - on `simultaneous-butterfly-layer`: $\delta$ (chunk width): The number of consecutive address bits in each transform axis (chunk).
   - on [Two-point kernel](two-point-kernel.md): $\delta$ (identity coefficient): The complex coefficient of the identity matrix in a two-point kernel.
723. $\delta$
   - on `simultaneous-butterfly-layer`: $\delta$ (chunk width): The number of consecutive address bits in each transform axis (chunk).
   - on [Permutation](permutation.md): $\delta$ (fourth entry): The entry of the sequence at position 4.
724. $\delta$
   - on `simultaneous-butterfly-layer`: $\delta$ (chunk width): The number of consecutive address bits in each transform axis (chunk).
   - on [Congruence](congruence-modulo.md): $\delta$ (remainder): The unique integer in $\{0,\dots,B-1\}$ lying in a residue class.
725. $\delta$
   - on `simultaneous-butterfly-layer`: $\delta$ (chunk width): The number of consecutive address bits in each transform axis (chunk).
   - on [Limit inferior](limit-inferior.md): $\delta$ (arbitrary positive real): A real number greater than zero, arbitrary in the negation of the conjecture.
726. $\delta$
   - on `simultaneous-butterfly-layer`: $\delta$ (chunk width): The number of consecutive address bits in each transform axis (chunk).
   - on [Extended real numbers](extended-reals.md): $\delta$ (term position): The position of a term in a sequence, a positive integer.
727. $H_0$
   - on `simultaneous-butterfly-layer`: $H_0$ (two-point map): The two-point map $H_0(u,v)=((u+v)/2,(u-v)/2)$, as a $2\times2$ matrix.
   - on [Butterfly](butterfly.md): $H_0$ (butterfly map): The two-point map sending a pair of values to its half-sum and half-difference.
728. $F_q$
   - on `simultaneous-butterfly-layer`: $F_q$ (length-q transform): The discrete Fourier transform on $q$ values, normalized by $1/q$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $F_q$ (Fourier transform): The discrete Fourier transform of length $q$, the map sending $f$ to the vector $F_q f$ with the coordinates given above.
729. $q$
   - on `simultaneous-butterfly-layer`: $q$ (number of values): The number of values that the transform $F_q$ acts on.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $q$ (transform length): The number of coordinates of each vector the transform acts on, a positive integer.
730. $j$
   - on `simultaneous-butterfly-layer`: $j$ (input index): The index of an input value in the transform $F_q$.
   - on [Integer](integer.md): $j$ (digit position): The position of a digit or bit, counted from the left starting at 1.
731. $j$
   - on `simultaneous-butterfly-layer`: $j$ (input index): The index of an input value in the transform $F_q$.
   - on [Linear algebra basics](linear-algebra-basics.md): $j$ (coordinate index): The index of a coordinate of a vector, running from 1 to m.
732. $j$
   - on `simultaneous-butterfly-layer`: $j$ (input index): The index of an input value in the transform $F_q$.
   - on [Ceiling function](ceiling-function.md): $j$ (integer): Any integer, which is its own ceiling.
733. $j$
   - on `simultaneous-butterfly-layer`: $j$ (input index): The index of an input value in the transform $F_q$.
   - on [Convolution](convolution.md): $j$ (input position in b): The position of an entry of $b$.
734. $j$
   - on `simultaneous-butterfly-layer`: $j$ (input index): The index of an input value in the transform $F_q$.
   - on [Address-field interchange](address-interchange.md): $j$ (level index): The level of a call, so a call on width $m^j$ sits at level $j$.
735. $k$
   - on `simultaneous-butterfly-layer`: $k$ (output index): The index of an output coordinate of the transform $F_q$.
   - on [Integer](integer.md): $k$ (digit count): The number of digits in a digit list.
736. $k$
   - on `simultaneous-butterfly-layer`: $k$ (output index): The index of an output coordinate of the transform $F_q$.
   - on [Root of unity](root-of-unity.md): $k$ (integer exponent): An integer exponent of $y$ in the power $y^k$ that multiplies the coefficient list.
737. $k$
   - on `simultaneous-butterfly-layer`: $k$ (output index): The index of an output coordinate of the transform $F_q$.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $k$ (padded length): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
738. $k$
   - on `simultaneous-butterfly-layer`: $k$ (output index): The index of an output coordinate of the transform $F_q$.
   - on [Address-field interchange](address-interchange.md): $k$ (level count): The number of levels of the recursion, the logarithm to base m of the field width u.
739. $k$
   - on `simultaneous-butterfly-layer`: $k$ (output index): The index of an output coordinate of the transform $F_q$.
   - on [Limit inferior](limit-inferior.md): $k$ (term position): A position in a sequence, the index of a term.
740. $\Delta$
   - on `simultaneous-butterfly-layer`: $\Delta$ (diagonal phase matrix): The diagonal matrix $\mathrm{diag}(1,i)$.
   - on [Complex phase network](complex-phase-network.md): $\Delta$ (orthogonal residual): The orthogonal complement of the smaller label of an edge inside the larger one.
741. $X$
   - on `simultaneous-butterfly-layer`: $X$ (bit-flip matrix): The $2\times2$ matrix that swaps the two basis states of one bit.
   - on [Two-point kernel](two-point-kernel.md): $X$ (bit flip): The 2 by 2 matrix that interchanges the two entries of a pair.
742. $X$
   - on `simultaneous-butterfly-layer`: $X$ (bit-flip matrix): The $2\times2$ matrix that swaps the two basis states of one bit.
   - on [Array norm](array-norm.md): $X$ (array): A finite array of complex values, whose norm is taken.
743. $X$
   - on `simultaneous-butterfly-layer`: $X$ (bit-flip matrix): The $2\times2$ matrix that swaps the two basis states of one bit.
   - on [Orthogonal complement](orthogonal-complement.md): $X$ (vector space): A vector space over $F$ on which the bilinear form is defined.
744. $C$
   - on `simultaneous-butterfly-layer`: $C$ (two-point kernel): The two-by-two operator $\mathcal H\Delta\mathcal H$, equal to $\lambda I+\mu X$.
   - on [Phase factor](phase-factor.md): $C$ (forward kernel): The 2 by 2 matrix with entries (1+i)/2 and (1-i)/2 that is the forward kernel.
745. $p$
   - on `simultaneous-butterfly-layer`: $p$ (working precision): The working precision in bits: the inputs lie on the grid $2^{-p}\mathbb Z[i]$.
   - on [Truncation](truncation.md): $p$ (precision): The number of fractional binary places kept, which counts the binary digits after the point.
746. $s$
   - on `simultaneous-butterfly-layer`: $s$ (number of H_0 factors): The number of individual factors $H_0$ applied, which refines the grid to $2^{-(p+s)}$.
   - on [Ceiling function](ceiling-function.md): $s$ (real number): The real number that the ceiling rounds up to an integer.
747. $s$
   - on `simultaneous-butterfly-layer`: $s$ (number of H_0 factors): The number of individual factors $H_0$ applied, which refines the grid to $2^{-(p+s)}$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $s$ (input index): An integer index running over $0, 1, \ldots, q-1$ that labels an input coordinate $f_s$.
748. $s$
   - on `simultaneous-butterfly-layer`: $s$ (number of H_0 factors): The number of individual factors $H_0$ applied, which refines the grid to $2^{-(p+s)}$.
   - on [Transform axis](transform-axis.md): $s$ (coefficient count): A power of two that is the number of coefficients of the stored polynomial, which is also the length of its axis.
749. $s$
   - on `simultaneous-butterfly-layer`: $s$ (number of H_0 factors): The number of individual factors $H_0$ applied, which refines the grid to $2^{-(p+s)}$.
   - on [Truncation](truncation.md): $s$ (first pair value): The first of the two values in a pair that a layer combines.
750. $s$
   - on `simultaneous-butterfly-layer`: $s$ (number of H_0 factors): The number of individual factors $H_0$ applied, which refines the grid to $2^{-(p+s)}$.
   - on [Address-field interchange](address-interchange.md): $s$ (smaller calls): The number of smaller calls one call makes, equal to the sum of the edge ranks.
751. $s$
   - on `simultaneous-butterfly-layer`: $s$ (number of H_0 factors): The number of individual factors $H_0$ applied, which refines the grid to $2^{-(p+s)}$.
   - on [Array norm](array-norm.md): $s$ (coefficient index): The index of a coefficient of a ring element, running from 0 to r-1.
752. $s$
   - on `simultaneous-butterfly-layer`: $s$ (number of H_0 factors): The number of individual factors $H_0$ applied, which refines the grid to $2^{-(p+s)}$.
   - on [Subspace labels](subspace-labels.md): $s$ (basis index): An index numbering the basis vectors of an edge residual.
753. $\Delta$
   - on `guard-width-bound`: $\Delta$ (guard width): The number of extra fractional and integer bits reserved per real component, which bounds the depth of every value.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $\Delta$ (diagonal phase matrix): The diagonal matrix $\mathrm{diag}(1,i)$.
754. $\Delta$
   - on `guard-width-bound`: $\Delta$ (guard width): The number of extra fractional and integer bits reserved per real component, which bounds the depth of every value.
   - on [Complex phase network](complex-phase-network.md): $\Delta$ (orthogonal residual): The orthogonal complement of the smaller label of an edge inside the larger one.
755. $u$
   - on `guard-width-bound`: $u$ (first input value): The first of the two values that the two-point map combines.
   - on [Linear algebra basics](linear-algebra-basics.md): $u$ (vertex): A vertex of the paper's directed graph.
756. $u$
   - on `guard-width-bound`: $u$ (first input value): The first of the two values that the two-point map combines.
   - on [Supremum](supremum.md): $u$ (input vector): One input vector in the supremum defining the operator norm, a finite list of complex numbers.
757. $u$
   - on `guard-width-bound`: $u$ (first input value): The first of the two values that the two-point map combines.
   - on [Array norm](array-norm.md): $u$ (entry): An entry of the array X, whose modulus is taken.
758. $v$
   - on `guard-width-bound`: $v$ (second input value): The second of the two values that the two-point map combines.
   - on [Linear algebra basics](linear-algebra-basics.md): $v$ (vertex): A vertex of the paper's directed graph.
759. $v$
   - on `guard-width-bound`: $v$ (second input value): The second of the two values that the two-point map combines.
   - on [Binary change of basis](binary-change-of-basis.md): $v$ (direction vector): A vector of $\mathbb F_2^m$ in a residual basis; $v_j$ is its $j$-th member.
760. $d$
   - on `guard-width-bound`: $d$ (axis bound): A bound on the number D of selected bits in a layer, so that D is at most d.
   - on [Address](address.md): $d$ (address length): The number of bits in each address of the array, the length of every address string.
761. $d$
   - on `guard-width-bound`: $d$ (axis bound): A bound on the number D of selected bits in a layer, so that D is at most d.
   - on [Congruence](congruence-modulo.md): $d$ (integer): An integer compared with $e$ modulo $B$.
762. $\ell$
   - on `guard-width-bound`: $\ell$ (depth): The number of operations on a chain that follows an operand from an input into a value.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\ell$ (output index): An integer index running over $0, 1, \ldots, q-1$ that labels an output coordinate $(F_q f)_\ell$.
763. $\ell$
   - on `guard-width-bound`: $\ell$ (depth): The number of operations on a chain that follows an operand from an input into a value.
   - on [Linear networks and frames](linear-network-frames.md): $\ell$ (input wire): An input wire of the network, whose supplied array and source vertex are named.
764. $\ell$
   - on `guard-width-bound`: $\ell$ (depth): The number of operations on a chain that follows an operand from an input into a value.
   - on [Subset-intersection network](subset-intersection-network.md): $\ell$ (ground element): An element of the ground set $[h]$, which names one central wire.
765. $m$
   - on `guard-width-bound`: $m$ (splitting factor): The factor by which a call divides the axis count.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
766. $m$
   - on `guard-width-bound`: $m$ (splitting factor): The factor by which a call divides the axis count.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
767. $m$
   - on `guard-width-bound`: $m$ (splitting factor): The factor by which a call divides the axis count.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
768. $m$
   - on `guard-width-bound`: $m$ (splitting factor): The factor by which a call divides the axis count.
   - on [Address-field interchange](address-interchange.md): $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
769. $m$
   - on `guard-width-bound`: $m$ (splitting factor): The factor by which a call divides the axis count.
   - on [Limit inferior](limit-inferior.md): $m$ (tail start): The position from which a tail of the sequence starts.
770. $e$
   - on `guard-width-bound`: $e$ (group size): The number of selected axes in a group that the recursion splits.
   - on [Congruence](congruence-modulo.md): $e$ (integer): An integer compared with $d$ modulo $B$.
771. $e$
   - on `guard-width-bound`: $e$ (group size): The number of selected axes in a group that the recursion splits.
   - on [Two-point kernel](two-point-kernel.md): $e$ (bit position): An index from 0 to d-1 naming the bit along which a kernel acts, counted from the least significant bit.
772. $e$
   - on `guard-width-bound`: $e$ (group size): The number of selected axes in a group that the recursion splits.
   - on [Eigenvalue](eigenvalue.md): $e$ (eigenvector): A nonzero vector of V that T maps to a multiple of itself.
773. $e$
   - on `guard-width-bound`: $e$ (group size): The number of selected axes in a group that the recursion splits.
   - on [Indicator vector](indicator-vector.md): $e$ (position): An element of the ground set [h], a position of the indicator vector.
774. $A$
   - on `guard-width-bound`: $A$ (depth bound): The bound on the number of operations on any chain within a group, as a function of its size.
   - on [Running time cost](running-time-cost.md): $A$ (machine): A machine whose running time cost is being measured.
775. $A$
   - on `guard-width-bound`: $A$ (depth bound): The bound on the number of operations on any chain within a group, as a function of its size.
   - on [Linear algebra basics](linear-algebra-basics.md): $A$ (matrix): An m by m matrix with entries in F.
776. $E$
   - on `guard-width-bound`: $E$ (gate budget): The most gate operations charged at a node of the recursion.
   - on [Exceptional set](exceptional-set.md): $E$ (exceptional set): The set of addresses at which the special rule gives a value different from the generic formula F.
777. $E$
   - on `guard-width-bound`: $E$ (gate budget): The most gate operations charged at a node of the recursion.
   - on [Directed graph](directed-graph.md): $E$ (edge set): The set of directed edges of the directed graph, each an ordered pair of vertices.
778. $k$
   - on `guard-width-bound`: $k$ (internal levels): The number of internal levels of the recursion.
   - on [Integer](integer.md): $k$ (digit count): The number of digits in a digit list.
779. $k$
   - on `guard-width-bound`: $k$ (internal levels): The number of internal levels of the recursion.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $k$ (padded length): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
780. $k$
   - on `guard-width-bound`: $k$ (internal levels): The number of internal levels of the recursion.
   - on [Root of unity](root-of-unity.md): $k$ (integer exponent): An integer exponent of $y$ in the power $y^k$ that multiplies the coefficient list.
781. $k$
   - on `guard-width-bound`: $k$ (internal levels): The number of internal levels of the recursion.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $k$ (output index): The index of an output coordinate of the transform $F_q$.
782. $k$
   - on `guard-width-bound`: $k$ (internal levels): The number of internal levels of the recursion.
   - on [Address-field interchange](address-interchange.md): $k$ (level count): The number of levels of the recursion, the logarithm to base m of the field width u.
783. $k$
   - on `guard-width-bound`: $k$ (internal levels): The number of internal levels of the recursion.
   - on [Limit inferior](limit-inferior.md): $k$ (term position): A position in a sequence, the index of a term.
784. $B$
   - on `guard-width-bound`: $B$ (level factor): The growth factor $s+E$ that each recursion level multiplies a bound by.
   - on [Linear algebra basics](linear-algebra-basics.md): $B$ (candidate inverse): A matrix that satisfies AB=BA=I.
785. $B$
   - on `guard-width-bound`: $B$ (level factor): The growth factor $s+E$ that each recursion level multiplies a bound by.
   - on [Congruence](congruence-modulo.md): $B$ (modulus): The positive integer modulus by which congruence is taken.
786. $x$
   - on `guard-width-bound`: $x$ (real bound): A real number at least one, used as a generic bound in the level inequality.
   - on [Integer](integer.md): $x$ (binary string): A binary string of bits, read as an integer by the paper's rule.
787. $x$
   - on `guard-width-bound`: $x$ (real bound): A real number at least one, used as a generic bound in the level inequality.
   - on [Linear algebra basics](linear-algebra-basics.md): $x$ (vector): A vector in a vector space, changed from earlier pages.
788. $x$
   - on `guard-width-bound`: $x$ (real bound): A real number at least one, used as a generic bound in the level inequality.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $x$ (first input): The first binary input string, of length $n$.
789. $x$
   - on `guard-width-bound`: $x$ (real bound): A real number at least one, used as a generic bound in the level inequality.
   - on [Phase factor](phase-factor.md): $x$ (address): An address whose selected bits are $x_1,\dots,x_D$, each 0 or 1.
790. $x$
   - on `guard-width-bound`: $x$ (real bound): A real number at least one, used as a generic bound in the level inequality.
   - on [Order of an element](order-of-element.md): $x$ (indeterminate): The indeterminate of the ring C[x] modulo x^S minus 1, whose image the map sends to a product of axis indeterminates.
791. $x$
   - on `guard-width-bound`: $x$ (real bound): A real number at least one, used as a generic bound in the level inequality.
   - on [Address-field interchange](address-interchange.md): $x$ (first field block): The bits of the first of the two address fields, read as a block at matching positions.
792. $x$
   - on `guard-width-bound`: $x$ (real bound): A real number at least one, used as a generic bound in the level inequality.
   - on [Scratch storage](scratch-storage.md): $x$ (control vector): The control vector, whose entry at triple $T$ is $x_T$.
793. $\nu$
   - on `guard-width-bound`: $\nu$ (exponent): The least positive integer $j$ with $m^j\ge B$.
   - on [Two-point kernel](two-point-kernel.md): $\nu$ (address): An integer from 0 to 2^d-1 labeling one entry of an array, whose binary form has d bits.
794. $t$
   - on `guard-width-bound`: $t$ (shift count): The number of places a shift moves, equal to $\lfloor D/2\rfloor$.
   - on [Integer](integer.md): $t$ (indeterminate): A formal variable of polynomials, which is not a number.
795. $t$
   - on `guard-width-bound`: $t$ (shift count): The number of places a shift moves, equal to $\lfloor D/2\rfloor$.
   - on [Convolution](convolution.md): $t$ (output position): The position of an entry of the convolution output.
796. $t$
   - on `guard-width-bound`: $t$ (shift count): The number of places a shift moves, equal to $\lfloor D/2\rfloor$.
   - on [Linear networks and frames](linear-network-frames.md): $t$ (gate input count): The number of input arrays that the gate $G$ takes.
797. $t$
   - on `guard-width-bound`: $t$ (shift count): The number of places a shift moves, equal to $\lfloor D/2\rfloor$.
   - on [Carry propagation](carry-propagation.md): $t$ (position index): The position of a coefficient or digit in the list, running over $0, 1, \dots$.
798. $\varepsilon$
   - on `guard-width-bound`: $\varepsilon$ (growth exponent): The exponent in $d=\Theta(p^{arepsilon})$, chosen so that $arepsilon C_1<1$.
   - on [Supremum](supremum.md): $\varepsilon$ (positive gap): The positive number $1-\Omega$, the distance from $\Omega$ up to $1$.
799. $\varepsilon$
   - on `guard-width-bound`: $\varepsilon$ (growth exponent): The exponent in $d=\Theta(p^{arepsilon})$, chosen so that $arepsilon C_1<1$.
   - on [Limit inferior](limit-inferior.md): $\varepsilon$ (tolerance): A positive real number against which the terms of the sequence are compared.
800. $d$
   - on `numerical-layer`: $d$ (selected-bit bound): An upper bound on the number $D$ of selected bits, so that $D \le d$.
   - on [Address](address.md): $d$ (address length): The number of bits in each address of the array, the length of every address string.
801. $d$
   - on `numerical-layer`: $d$ (selected-bit bound): An upper bound on the number $D$ of selected bits, so that $D \le d$.
   - on [Congruence](congruence-modulo.md): $d$ (integer): An integer compared with $e$ modulo $B$.
802. $e$
   - on `numerical-layer`: $e$ (selected axis count): The number of selected axes that a call acts on.
   - on [Two-point kernel](two-point-kernel.md): $e$ (bit position): An index from 0 to d-1 naming the bit along which a kernel acts, counted from the least significant bit.
803. $e$
   - on `numerical-layer`: $e$ (selected axis count): The number of selected axes that a call acts on.
   - on [Congruence](congruence-modulo.md): $e$ (integer): An integer compared with $d$ modulo $B$.
804. $e$
   - on `numerical-layer`: $e$ (selected axis count): The number of selected axes that a call acts on.
   - on [Eigenvalue](eigenvalue.md): $e$ (eigenvector): A nonzero vector of V that T maps to a multiple of itself.
805. $e$
   - on `numerical-layer`: $e$ (selected axis count): The number of selected axes that a call acts on.
   - on [Indicator vector](indicator-vector.md): $e$ (position): An element of the ground set [h], a position of the indicator vector.
806. $m$
   - on `numerical-layer`: $m$ (division factor): The fixed integer by which a call divides its number of selected axes.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
807. $m$
   - on `numerical-layer`: $m$ (division factor): The fixed integer by which a call divides its number of selected axes.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
808. $m$
   - on `numerical-layer`: $m$ (division factor): The fixed integer by which a call divides its number of selected axes.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
809. $m$
   - on `numerical-layer`: $m$ (division factor): The fixed integer by which a call divides its number of selected axes.
   - on [Address-field interchange](address-interchange.md): $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
810. $m$
   - on `numerical-layer`: $m$ (division factor): The fixed integer by which a call divides its number of selected axes.
   - on [Limit inferior](limit-inferior.md): $m$ (tail start): The position from which a tail of the sequence starts.
811. $s$
   - on `numerical-layer`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $s$ (number of H_0 factors): The number of individual factors $H_0$ applied, which refines the grid to $2^{-(p+s)}$.
812. $s$
   - on `numerical-layer`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Ceiling function](ceiling-function.md): $s$ (real number): The real number that the ceiling rounds up to an integer.
813. $s$
   - on `numerical-layer`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $s$ (input index): An integer index running over $0, 1, \ldots, q-1$ that labels an input coordinate $f_s$.
814. $s$
   - on `numerical-layer`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Transform axis](transform-axis.md): $s$ (coefficient count): A power of two that is the number of coefficients of the stored polynomial, which is also the length of its axis.
815. $s$
   - on `numerical-layer`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Truncation](truncation.md): $s$ (first pair value): The first of the two values in a pair that a layer combines.
816. $s$
   - on `numerical-layer`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Address-field interchange](address-interchange.md): $s$ (smaller calls): The number of smaller calls one call makes, equal to the sum of the edge ranks.
817. $s$
   - on `numerical-layer`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Array norm](array-norm.md): $s$ (coefficient index): The index of a coefficient of a ring element, running from 0 to r-1.
818. $s$
   - on `numerical-layer`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Subspace labels](subspace-labels.md): $s$ (basis index): An index numbering the basis vectors of an edge residual.
819. $\omega$
   - on `union-bound`: $\omega$ (outcome): An element of the outcome set Ω, one possible outcome.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\omega$ (primitive root of unity): The complex number $e^{-2\pi i/q}$, a primitive $q$-th root of unity.
820. $m$
   - on `union-bound`: $m$ (event count): The number of events E_1 through E_m.
   - on [Guard-width bound](guard-width-bound.md): $m$ (splitting factor): The factor by which a call divides the axis count.
821. $m$
   - on `union-bound`: $m$ (event count): The number of events E_1 through E_m.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
822. $m$
   - on `union-bound`: $m$ (event count): The number of events E_1 through E_m.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
823. $m$
   - on `union-bound`: $m$ (event count): The number of events E_1 through E_m.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
824. $m$
   - on `union-bound`: $m$ (event count): The number of events E_1 through E_m.
   - on [Address-field interchange](address-interchange.md): $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
825. $m$
   - on `union-bound`: $m$ (event count): The number of events E_1 through E_m.
   - on [Limit inferior](limit-inferior.md): $m$ (tail start): The position from which a tail of the sequence starts.
826. $i$
   - on `union-bound`: $i$ (event index): An index numbering the events, running from 1 to m.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $i$ (imaginary unit): The imaginary unit, the complex number whose square is $-1$, used in this page in place of the convolution page's input position $i$.
827. $i$
   - on `union-bound`: $i$ (event index): An index numbering the events, running from 1 to m.
   - on [Linear algebra basics](linear-algebra-basics.md): $i$ (row index): The index of a row of a matrix, running from 1 to m.
828. $i$
   - on `union-bound`: $i$ (event index): An index numbering the events, running from 1 to m.
   - on [Convolution](convolution.md): $i$ (input position in a): The position of an entry of $a$.
829. $i$
   - on `union-bound`: $i$ (event index): An index numbering the events, running from 1 to m.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $i$ (bit position): A bit position of a residue, an integer from 0 to $\sigma-1$.
830. $i$
   - on `union-bound`: $i$ (event index): An index numbering the events, running from 1 to m.
   - on [Transform axis](transform-axis.md): $i$ (axis index): An index naming one axis, running from 1 to D.
831. $f$
   - on `union-bound`: $f$ (selected bit count): The number of selected bit positions of the addition.
   - on [Big-Theta notation](big-theta-notation.md): $f$ (bounded function): The function from input sizes to nonnegative reals whose order is compared with that of $h$.
832. $f$
   - on `union-bound`: $f$ (selected bit count): The number of selected bit positions of the addition.
   - on [Bijection](bijection.md): $f$ (map): The map from the source set $U$ to the target set $W$ whose bijectivity is tested.
833. $f$
   - on `union-bound`: $f$ (selected bit count): The number of selected bit positions of the addition.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $f$ (input vector): A vector of $q$ complex numbers, the input to the transform, with coordinates $f_0, \ldots, f_{q-1}$.
834. $f$
   - on `union-bound`: $f$ (selected bit count): The number of selected bit positions of the addition.
   - on [Dual space](dual-space.md): $f$ (linear functional): A generic element of the dual space U^*, which is a linear map from U to F.
835. $f$
   - on `union-bound`: $f$ (selected bit count): The number of selected bit positions of the addition.
   - on [Linear functional](linear-functional.md): $f$ (linear functional): The map from V to F under study, which sends each vector to one scalar and respects addition and scalar multiplication.
836. $K$
   - on `union-bound`: $K$ (segment width): The number of consecutive bits in each segment.
   - on [Linear algebra basics](linear-algebra-basics.md): $K$ (address block): The second bit block of an address.
837. $K$
   - on `union-bound`: $K$ (segment width): The number of consecutive bits in each segment.
   - on [Two-point kernel](two-point-kernel.md): $K$ (two-point kernel): The 2 by 2 matrix delta I plus kappa X, which is the two-point kernel.
838. $y$
   - on `union-bound`: $y$ (address chunk y): One of the two chunks of each address, a block of its coordinates.
   - on [Linear algebra basics](linear-algebra-basics.md): $y$ (vector): A vector in a vector space, changed from earlier pages.
839. $y$
   - on `union-bound`: $y$ (address chunk y): One of the two chunks of each address, a block of its coordinates.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $y$ (second input): The second binary input string, of length $n$.
840. $y$
   - on `union-bound`: $y$ (address chunk y): One of the two chunks of each address, a block of its coordinates.
   - on [Root of unity](root-of-unity.md): $y$ (polynomial variable): The variable of the polynomial ring $\mathbb{C}[y]/(y^4+1)$, in which $y^4 = -1$; this replaces the logarithm page's meaning of $y$ on this page.
841. $y$
   - on `union-bound`: $y$ (address chunk y): One of the two chunks of each address, a block of its coordinates.
   - on [Logarithm](logarithm.md): $y$ (argument): The positive number whose logarithm is taken.
842. $y$
   - on `union-bound`: $y$ (address chunk y): One of the two chunks of each address, a block of its coordinates.
   - on [Address-field interchange](address-interchange.md): $y$ (second field block): The bits of the second of the two address fields, read as a block at matching positions.
843. $y$
   - on `union-bound`: $y$ (address chunk y): One of the two chunks of each address, a block of its coordinates.
   - on [Scratch storage](scratch-storage.md): $y$ (target vector): The target vector, whose entry at triple $S$ is $y_S$.
844. $z$
   - on `union-bound`: $z$ (address chunk z): The other of the two chunks of each address.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $z$ (padded integer): A nonnegative integer with $z < 2^k$ that is written in binary.
845. $z$
   - on `union-bound`: $z$ (address chunk z): The other of the two chunks of each address.
   - on [Root of unity](root-of-unity.md): $z$ (complex number): A complex number whose powers are taken; a root of unity is such a number.
846. $D$
   - on `transform-round`: $D$ (participating axis count): The number of participating axes, the axes that take a butterfly step in the round.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $D$ (number of axes): The number of transform axes that the layer acts on, one selected bit on each.
847. $D$
   - on `transform-round`: $D$ (participating axis count): The number of participating axes, the axes that take a butterfly step in the round.
   - on [Phase factor](phase-factor.md): $D$ (selected bit count): The number of selected address bits on which a butterfly layer acts.
848. $D$
   - on `transform-round`: $D$ (participating axis count): The number of participating axes, the axes that take a butterfly step in the round.
   - on [Transform axis](transform-axis.md): $D$ (axis count): The number of axes of the array.
849. $i$
   - on `transform-round`: $i$ (axis index): An index naming one of the participating axes.
   - on [Linear algebra basics](linear-algebra-basics.md): $i$ (row index): The index of a row of a matrix, running from 1 to m.
850. $i$
   - on `transform-round`: $i$ (axis index): An index naming one of the participating axes.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $i$ (bit position): A bit position of a residue, an integer from 0 to $\sigma-1$.
851. $i$
   - on `transform-round`: $i$ (axis index): An index naming one of the participating axes.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $i$ (imaginary unit): The imaginary unit, the complex number whose square is $-1$, used in this page in place of the convolution page's input position $i$.
852. $i$
   - on `transform-round`: $i$ (axis index): An index naming one of the participating axes.
   - on [Convolution](convolution.md): $i$ (input position in a): The position of an entry of $a$.
853. $h$
   - on `transform-round`: $h$ (highest unprocessed bit): The position of the highest unprocessed address bit on axis i, which receives the branch bit.
   - on [Linear networks and frames](linear-network-frames.md): $h$ (route position): The position of a vertex along a route, running from $0$ to $L$.
854. $h$
   - on `transform-round`: $h$ (highest unprocessed bit): The position of the highest unprocessed address bit on axis i, which receives the branch bit.
   - on [Big-Theta notation](big-theta-notation.md): $h$ (comparison function): The function from input sizes to nonnegative reals against which $f$ is compared.
855. $h$
   - on `transform-round`: $h$ (highest unprocessed bit): The position of the highest unprocessed address bit on axis i, which receives the branch bit.
   - on [Eigenvalue](eigenvalue.md): $h$ (coordinate count): The number of coordinates of each vector in Q^h, at least 2.
856. $h$
   - on `transform-round`: $h$ (highest unprocessed bit): The position of the highest unprocessed address bit on axis i, which receives the branch bit.
   - on [Array norm](array-norm.md): $h$ (ring element): An element of the ring modulo y^r+1, written as a polynomial in y.
857. $h$
   - on `transform-round`: $h$ (highest unprocessed bit): The position of the highest unprocessed address bit on axis i, which receives the branch bit.
   - on [Ground set](ground-set.md): $h$ (ground set size): The number of elements of the ground set, the count of its elements.
858. $\eta$
   - on `transform-round`: $\eta$ (twiddle exponent): The exponent of y at an address, so that the round multiplies each record by y to the power eta.
   - on [Linear algebra basics](linear-algebra-basics.md): $\eta$ (scalar): A scalar in F multiplying a vector.
859. $\eta$
   - on `transform-round`: $\eta$ (twiddle exponent): The exponent of y at an address, so that the round multiplies each record by y to the power eta.
   - on [Congruence](congruence-modulo.md): $\eta$ (second multiple): The integer with $e'-e=\eta B$.
860. $\eta$
   - on `transform-round`: $\eta$ (twiddle exponent): The exponent of y at an address, so that the round multiplies each record by y to the power eta.
   - on [Subset-intersection network](subset-intersection-network.md): $\eta$ (target vector): The vector, indexed by triples, of the entries of the target bank along the varying coordinate.
861. $\eta$
   - on `transform-round`: $\eta$ (twiddle exponent): The exponent of y at an address, so that the round multiplies each record by y to the power eta.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\eta$ (half-size): The number of positions in each half of a block at a level of the transform.
862. $e$
   - on `transform-round`: $e$ (quotient): The integer quotient of eta by r: the number of whole multiples of r in eta.
   - on [Two-point kernel](two-point-kernel.md): $e$ (bit position): An index from 0 to d-1 naming the bit along which a kernel acts, counted from the least significant bit.
863. $e$
   - on `transform-round`: $e$ (quotient): The integer quotient of eta by r: the number of whole multiples of r in eta.
   - on [Congruence](congruence-modulo.md): $e$ (integer): An integer compared with $d$ modulo $B$.
864. $e$
   - on `transform-round`: $e$ (quotient): The integer quotient of eta by r: the number of whole multiples of r in eta.
   - on [Eigenvalue](eigenvalue.md): $e$ (eigenvector): A nonzero vector of V that T maps to a multiple of itself.
865. $e$
   - on `transform-round`: $e$ (quotient): The integer quotient of eta by r: the number of whole multiples of r in eta.
   - on [Indicator vector](indicator-vector.md): $e$ (position): An element of the ground set [h], a position of the indicator vector.
866. $\delta$
   - on `transform-round`: $\delta$ (remainder): The remainder of eta on division by r, from 0 to r minus 1.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $\delta$ (chunk width): The number of consecutive address bits in each transform axis (chunk).
867. $\delta$
   - on `transform-round`: $\delta$ (remainder): The remainder of eta on division by r, from 0 to r minus 1.
   - on [Two-point kernel](two-point-kernel.md): $\delta$ (identity coefficient): The complex coefficient of the identity matrix in a two-point kernel.
868. $\delta$
   - on `transform-round`: $\delta$ (remainder): The remainder of eta on division by r, from 0 to r minus 1.
   - on [Permutation](permutation.md): $\delta$ (fourth entry): The entry of the sequence at position 4.
869. $\delta$
   - on `transform-round`: $\delta$ (remainder): The remainder of eta on division by r, from 0 to r minus 1.
   - on [Limit inferior](limit-inferior.md): $\delta$ (arbitrary positive real): A real number greater than zero, arbitrary in the negation of the conjecture.
870. $\delta$
   - on `transform-round`: $\delta$ (remainder): The remainder of eta on division by r, from 0 to r minus 1.
   - on [Extended real numbers](extended-reals.md): $\delta$ (term position): The position of a term in a sequence, a positive integer.
871. $d$
   - on `tape-procedure`: $d$ (chunk count bound): An upper bound on the number of equal-width address chunks whose selected bits one pass handles.
   - on [Address](address.md): $d$ (address length): The number of bits in each address of the array, the length of every address string.
872. $d$
   - on `tape-procedure`: $d$ (chunk count bound): An upper bound on the number of equal-width address chunks whose selected bits one pass handles.
   - on [Congruence](congruence-modulo.md): $d$ (integer): An integer compared with $e$ modulo $B$.
873. $\theta$
   - on `bit-procedure`: $\theta$ (capped log exponent): The capped logarithm max(0, log_m(s/W)) of s/W, which is below tau.
   - on [Eigenvalue](eigenvalue.md): $\theta$ (eigenvalue): A scalar for which T maps some nonzero vector e to the multiple theta e.
874. $\theta$
   - on `bit-procedure`: $\theta$ (capped log exponent): The capped logarithm max(0, log_m(s/W)) of s/W, which is below tau.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\theta$ (twiddle): The power of $\omega_N$ by which a butterfly multiplies its second entry.
875. $q$
   - on `address-shear`: $q$ (radix): A fixed odd prime, the radix in which each digit of a field is written.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $q$ (transform length): The number of coordinates of each vector the transform acts on, a positive integer.
876. $q$
   - on `address-shear`: $q$ (radix): A fixed odd prime, the radix in which each digit of a field is written.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $q$ (number of values): The number of values that the transform $F_q$ acts on.
877. $b$
   - on `address-shear`: $b$ (digits per field): The number of radix-$q$ digits in each field, so it counts digits.
   - on [Integer](integer.md): $b$ (base): The base (radix) of a digit representation, an integer at least 2.
878. $b$
   - on `address-shear`: $b$ (digits per field): The number of radix-$q$ digits in each field, so it counts digits.
   - on [Logarithm](logarithm.md): $b$ (base): The fixed base of the logarithm, a number greater than 1.
879. $b$
   - on `address-shear`: $b$ (digits per field): The number of radix-$q$ digits in each field, so it counts digits.
   - on [Radix-digit convolution](radix-digit-convolution.md): $b$ (digit width): The number of bits in each digit of an input.
880. $b$
   - on `address-shear`: $b$ (digits per field): The number of radix-$q$ digits in each field, so it counts digits.
   - on [Convolution](convolution.md): $b$ (second input sequence): The second of the two input sequences, of length $n$.
881. $b$
   - on `address-shear`: $b$ (digits per field): The number of radix-$q$ digits in each field, so it counts digits.
   - on [Extended real numbers](extended-reals.md): $b$ (least real bound): The least real upper bound of $R$, which is the supremum of $S$ in that case.
882. $e$
   - on `address-shear`: $e$ (chunk digit count): The number of digits in a chunk at recursion depth $k$, equal to $m^k$.
   - on [Eigenvalue](eigenvalue.md): $e$ (eigenvector): A nonzero vector of V that T maps to a multiple of itself.
883. $e$
   - on `address-shear`: $e$ (chunk digit count): The number of digits in a chunk at recursion depth $k$, equal to $m^k$.
   - on [Congruence](congruence-modulo.md): $e$ (integer): An integer compared with $d$ modulo $B$.
884. $e$
   - on `address-shear`: $e$ (chunk digit count): The number of digits in a chunk at recursion depth $k$, equal to $m^k$.
   - on [Indicator vector](indicator-vector.md): $e$ (position): An element of the ground set [h], a position of the indicator vector.
885. $e$
   - on `address-shear`: $e$ (chunk digit count): The number of digits in a chunk at recursion depth $k$, equal to $m^k$.
   - on [Two-point kernel](two-point-kernel.md): $e$ (bit position): An index from 0 to d-1 naming the bit along which a kernel acts, counted from the least significant bit.
886. $e$
   - on `address-shear`: $e$ (chunk digit count): The number of digits in a chunk at recursion depth $k$, equal to $m^k$.
   - on [Transform round](transform-round.md): $e$ (quotient): The integer quotient of eta by r: the number of whole multiples of r in eta.
887. $M$
   - on `stable-radix-sort`: $M$ (record count): The number of records in the full stream, a count of records, so every rank is an integer from 0 to M-1.
   - on [Linear algebra basics](linear-algebra-basics.md): $M$ (shear matrix): A matrix over F_2 that determines the shear.
888. $M$
   - on `stable-radix-sort`: $M$ (record count): The number of records in the full stream, a count of records, so every rank is an integer from 0 to M-1.
   - on [Running time cost](running-time-cost.md): $M$ (example machine): The example machine that reads cells from the first cell until it finds a $1$ or reaches the last cell.
889. $w$
   - on `stable-radix-sort`: $w$ (key width): The number of bits in each key, a count of bits, which is also the number of passes.
   - on [Truncation](truncation.md): $w$ (coefficient list): A finite list of complex numbers, called coefficients.
890. $q$
   - on `stable-radix-sort`: $q$ (record key): The key of a record, a string of w bits written as q_{w-1} through q_0.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $q$ (number of values): The number of values that the transform $F_q$ acts on.
891. $q$
   - on `stable-radix-sort`: $q$ (record key): The key of a record, a string of w bits written as q_{w-1} through q_0.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $q$ (transform length): The number of coordinates of each vector the transform acts on, a positive integer.
892. $q$
   - on `stable-radix-sort`: $q$ (record key): The key of a record, a string of w bits written as q_{w-1} through q_0.
   - on [Mathematical induction](mathematical-induction.md): $q$ (level ratio): The fixed positive real number by which one recursion level may multiply a bound.
893. $t$
   - on `stable-radix-sort`: $t$ (bit position): A bit position of the key, counted from 0 at the least significant bit, which also indexes the pass that sorts by that bit.
   - on [Integer](integer.md): $t$ (indeterminate): A formal variable of polynomials, which is not a number.
894. $t$
   - on `stable-radix-sort`: $t$ (bit position): A bit position of the key, counted from 0 at the least significant bit, which also indexes the pass that sorts by that bit.
   - on [Linear networks and frames](linear-network-frames.md): $t$ (gate input count): The number of input arrays that the gate $G$ takes.
895. $t$
   - on `stable-radix-sort`: $t$ (bit position): A bit position of the key, counted from 0 at the least significant bit, which also indexes the pass that sorts by that bit.
   - on [Carry propagation](carry-propagation.md): $t$ (position index): The position of a coefficient or digit in the list, running over $0, 1, \dots$.
896. $t$
   - on `stable-radix-sort`: $t$ (bit position): A bit position of the key, counted from 0 at the least significant bit, which also indexes the pass that sorts by that bit.
   - on [Convolution](convolution.md): $t$ (output position): The position of an entry of the convolution output.
897. $t$
   - on `stable-radix-sort`: $t$ (bit position): A bit position of the key, counted from 0 at the least significant bit, which also indexes the pass that sorts by that bit.
   - on [Mathematical induction](mathematical-induction.md): $t$ (step index): The number of recursion levels passed, a nonnegative integer.
898. $\Psi$
   - on `destination-rank`: $\Psi$ (address): The address of a record, given by its three chunk values $\Psi_1$, $\Psi_2$, $\Psi_3$.
   - on [Tensor product](tensor-product.md): $\Psi$ (function on addresses): A complex-valued function on addresses of $J$ bits, which $P^{\otimes J}$ transforms.
899. $\Psi$
   - on `destination-rank`: $\Psi$ (address): The address of a record, given by its three chunk values $\Psi_1$, $\Psi_2$, $\Psi_3$.
   - on [Bilinear form](bilinear-form.md): $\Psi$ (form matrix): The m by m matrix whose entry in row i and column j is the form value of e_i and e_j.
900. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
901. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
902. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
903. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
904. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
905. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
906. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
907. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
908. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
909. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
910. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
911. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
912. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
913. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
914. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Tensor product](tensor-product.md): $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
915. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Subset-intersection network](subset-intersection-network.md): $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
916. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Dual space](dual-space.md): $\sigma$ (example functional): The linear functional on R^2 sending x to 3x_1 - x_2.
917. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Bit network](bit-network.md): $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
918. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Line spanned by a vector](line-spanned-by-vector.md): $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
919. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Fixed-tape machine model](fixed-tape-model.md): $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
920. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Extended real numbers](extended-reals.md): $\sigma$ (generic real number): A real number used as a generic value in the order, sums and limit conditions.
921. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Gram matrix](gram-matrix.md): $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
922. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Multidimensional transform](multidimensional-transform.md): $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
923. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\sigma$ (shift count): The number of places a shift moves each coefficient.
924. $\sigma$
   - on `destination-rank`: $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
   - on [Radix-two factorization](radix-two-factorization.md): $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
925. $T_0$
   - on `destination-rank`: $T_0$ (ideal permutation): The permutation of addresses that the packed addition should perform.
   - on [Bijection](bijection.md): $T_0$ (ideal bijection): The ideal bijection of the rectangle that performs the required XORs and fixes the other coordinates.
926. $S_0$
   - on `destination-rank`: $S_0$ (packed approximation): The packed addition that agrees with the ideal permutation $T_0$ off the exceptional addresses.
   - on [Bijection](bijection.md): $S_0$ (composed bijection): The bijection of the rectangle that the update lines of the interchange compose to.
927. $R$
   - on `destination-rank`: $R$ (payload bits): The number of payload bits in each record.
   - on [Ring](ring.md): $R$ (ring): A set with an addition and a multiplication that satisfy the axioms listed on this page.
928. $R$
   - on `destination-rank`: $R$ (payload bits): The number of payload bits in each record.
   - on [Scratch storage](scratch-storage.md): $R$ (scatter): The operation that adds to $y_S$ the central wires $C_\ell$ with $\ell\in S$.
929. $V$
   - on `destination-rank`: $V$ (stream bit count): The number of bits in the stream, $MR$.
   - on [Directed graph](directed-graph.md): $V$ (vertex set): The set of vertices of the directed graph, the points that edges join.
930. $V$
   - on `destination-rank`: $V$ (stream bit count): The number of bits in the stream, $MR$.
   - on [Array](array.md): $V$ (stored bit volume): The number of stored data bits in an array, the volume in which cost bounds are stated.
931. $V$
   - on `destination-rank`: $V$ (stream bit count): The number of bits in the stream, $MR$.
   - on [Payload](payload.md): $V$ (stream volume): The number of bits stored in the stream, which the time bound counts.
932. $V$
   - on `destination-rank`: $V$ (stream bit count): The number of bits in the stream, $MR$.
   - on [Big-Theta notation](big-theta-notation.md): $V$ (stored bit volume): The number of stored bits, which is of order $n$.
933. $V$
   - on `destination-rank`: $V$ (stream bit count): The number of bits in the stream, $MR$.
   - on [Cyclic shift](cyclic-shift.md): $V$ (stored bit volume): The number of stored bits in the array, a count of its data bits.
934. $V$
   - on `destination-rank`: $V$ (stream bit count): The number of bits in the stream, $MR$.
   - on [Scratch storage](scratch-storage.md): $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
935. $V$
   - on `destination-rank`: $V$ (stream bit count): The number of bits in the stream, $MR$.
   - on [Linear functional](linear-functional.md): $V$ (vector space): The vector space over F whose vectors a linear functional takes as input.
936. $V$
   - on `destination-rank`: $V$ (stream bit count): The number of bits in the stream, $MR$.
   - on [Eigenvalue](eigenvalue.md): $V$ (vector space): The vector space on which the linear operator T acts, over the field F.
937. $V$
   - on `destination-rank`: $V$ (stream bit count): The number of bits in the stream, $MR$.
   - on [Bilinear map](bilinear-map.md): $V$ (second argument space): The vector space that the second argument of the bilinear map ranges over.
938. $V$
   - on `destination-rank`: $V$ (stream bit count): The number of bits in the stream, $MR$.
   - on [Projection along a subspace](projection-along-subspace.md): $V$ (larger nested subspace): A nondegenerate subspace containing $U$, the larger of two nested labels.
939. $V$
   - on `destination-rank`: $V$ (stream bit count): The number of bits in the stream, $MR$.
   - on [Complex phase network](complex-phase-network.md): $V$ (head label): The label at the head of an edge.
940. $\Pi$
   - on `transform-identity`: $\Pi$ (coordinate permutation): A permutation that rearranges the entries of a vector by their positions.
   - on [Frequency domain](frequency-domain.md): $\Pi$ (record permutation): The permutation of storage slots that moves the entry of frequency $\ell$ to slot $\mathrm{rev}(\ell)$.
941. $c$
   - on `transform-identity`: $c$ (unit multiplier): A unit modulo $s$ that defines the retained permutation $\Pi_c$.
   - on [Integer](integer.md): $c$ (digit): A digit of a digit list, an integer between 0 and the base minus one.
942. $c$
   - on `transform-identity`: $c$ (unit multiplier): A unit modulo $s$ that defines the retained permutation $\Pi_c$.
   - on [Convolution](convolution.md): $c$ (convolution): The convolution of $a$ and $b$, a sequence of length $2n-1$.
943. $c$
   - on `transform-identity`: $c$ (unit multiplier): A unit modulo $s$ that defines the retained permutation $\Pi_c$.
   - on [Scratch storage](scratch-storage.md): $c$ (starting central values): The vector of starting values of the central wires.
944. $c$
   - on `transform-identity`: $c$ (unit multiplier): A unit modulo $s$ that defines the retained permutation $\Pi_c$.
   - on [Eigenvalue](eigenvalue.md): $c$ (average entry): The average of the entries of x, which is the coefficient of the all-ones vector in its split.
945. $c$
   - on `transform-identity`: $c$ (unit multiplier): A unit modulo $s$ that defines the retained permutation $\Pi_c$.
   - on [Near-linear time](near-linear-time.md): $c$ (log exponent): A fixed real number, the power to which the logarithm factor of a near-linear bound is raised.
946. $\chi$
   - on `transform-identity`: $\chi$ (inverse of t): An integer with $\chi t\equiv 1 \pmod s$, so it inverts $t$ modulo $s$.
   - on [Two-point kernel](two-point-kernel.md): $\chi$ (array of values): An array of complex values with one entry for each address.
947. $\chi$
   - on `transform-identity`: $\chi$ (inverse of t): An integer with $\chi t\equiv 1 \pmod s$, so it inverts $t$ modulo $s$.
   - on [Limit inferior](limit-inferior.md): $\chi$ (sequence): A sequence of real numbers; $\chi_k$ is its $k$-th term.
948. $A$
   - on `transform-identity`: $A$ (linear contraction): A linear map from $\mathbb{C}^s$ to $\mathbb{C}^t$ in the lemma.
   - on [Linear algebra basics](linear-algebra-basics.md): $A$ (matrix): An m by m matrix with entries in F.
949. $A$
   - on `transform-identity`: $A$ (linear contraction): A linear map from $\mathbb{C}^s$ to $\mathbb{C}^t$ in the lemma.
   - on [Running time cost](running-time-cost.md): $A$ (machine): A machine whose running time cost is being measured.
950. $\Psi$
   - on `transform-identity`: $\Psi$ (generic linear map): A generic linear map, used to define contractions.
   - on [Neumann series](neumann-series.md): $\Psi$ (partial sum): An arbitrary partial sum of the series with $\Xi$ terms, used in the error identity.
951. $\Psi$
   - on `transform-identity`: $\Psi$ (generic linear map): A generic linear map, used to define contractions.
   - on [Tensor product](tensor-product.md): $\Psi$ (function on addresses): A complex-valued function on addresses of $J$ bits, which $P^{\otimes J}$ transforms.
952. $\Psi$
   - on `transform-identity`: $\Psi$ (generic linear map): A generic linear map, used to define contractions.
   - on [Bilinear form](bilinear-form.md): $\Psi$ (form matrix): The m by m matrix whose entry in row i and column j is the form value of e_i and e_j.
953. $\Psi$
   - on `transform-identity`: $\Psi$ (generic linear map): A generic linear map, used to define contractions.
   - on [Gaussian resampling](gaussian-resampling.md): $\Psi$ (first Gaussian map): The map sending a length-$q$ vector to a length-$W$ vector by Gaussian-weighted sums with weight $\exp(-\pi\sigma^{-2}(j-qk/W)^2)$.
954. $\theta$
   - on `transform-identity`: $\theta$ (relative gap): The ratio $t/s$ minus one, which the lemma requires to exceed $p/\alpha^4$.
   - on [Neumann series](neumann-series.md): $\theta$ (construction parameter): A parameter of the paper's construction, entering the exponent $\sigma=\alpha^2\theta$.
955. $\theta$
   - on `transform-identity`: $\theta$ (relative gap): The ratio $t/s$ minus one, which the lemma requires to exceed $p/\alpha^4$.
   - on [Eigenvalue](eigenvalue.md): $\theta$ (eigenvalue): A scalar for which T maps some nonzero vector e to the multiple theta e.
956. $\theta$
   - on `transform-identity`: $\theta$ (relative gap): The ratio $t/s$ minus one, which the lemma requires to exceed $p/\alpha^4$.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\theta$ (twiddle): The power of $\omega_N$ by which a butterfly multiplies its second entry.
957. $\Upsilon$
   - on `transform-identity`: $\Upsilon$ (left inverse of Gamma): A linear map with $\Upsilon\Gamma=I$, built from $N^{-1}$ and a diagonal scaling.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\Upsilon$ (common exponent): The larger of the two exponents $\Gamma$ and $\Gamma'$, the number of factors of two in the common denominator of a sum.
958. $\Upsilon$
   - on `transform-identity`: $\Upsilon$ (left inverse of Gamma): A linear map with $\Upsilon\Gamma=I$, built from $N^{-1}$ and a diagonal scaling.
   - on [Gaussian resampling](gaussian-resampling.md): $\Upsilon$ (diagonal correction): The diagonal map multiplying entry $j$ by the factor that cancels the weight of $\Xi$ at position $j$.
959. $D$
   - on `transform-layout`: $D$ (participating axis count): The number of participating axes of a round, which is the number of chunks that share one offset.
   - on [Transform axis](transform-axis.md): $D$ (axis count): The number of axes of the array.
960. $D$
   - on `transform-layout`: $D$ (participating axis count): The number of participating axes of a round, which is the number of chunks that share one offset.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $D$ (number of axes): The number of transform axes that the layer acts on, one selected bit on each.
961. $D$
   - on `transform-layout`: $D$ (participating axis count): The number of participating axes of a round, which is the number of chunks that share one offset.
   - on [Phase factor](phase-factor.md): $D$ (selected bit count): The number of selected address bits on which a butterfly layer acts.
962. $K$
   - on `transform-layout`: $K$ (chunk width): The number of consecutive address bits in each chunk.
   - on [Linear algebra basics](linear-algebra-basics.md): $K$ (address block): The second bit block of an address.
963. $K$
   - on `transform-layout`: $K$ (chunk width): The number of consecutive address bits in each chunk.
   - on [Two-point kernel](two-point-kernel.md): $K$ (two-point kernel): The 2 by 2 matrix delta I plus kappa X, which is the two-point kernel.
964. $\upsilon$
   - on `transform-layout`: $\upsilon$ (chunk offset): The position of the selected bit within its chunk, counted from the least significant end.
   - on [Tensor product](tensor-product.md): $\upsilon$ (row index of Q): A row index of $Q$.
965. $\upsilon$
   - on `transform-layout`: $\upsilon$ (chunk offset): The position of the selected bit within its chunk, counted from the least significant end.
   - on [Bit network](bit-network.md): $\upsilon$ (ground element): An element of the ground set $[h]$, indexing a central wire.
966. $\varsigma$
   - on `transform-layout`: $\varsigma$ (round bit position): The position, counted from the least significant end, of the bit on which a round acts.
   - on [Subspace labels](subspace-labels.md): $\varsigma$ (translation coefficient): The coefficient of the translation in a translation kernel.
967. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
968. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
969. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
970. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
971. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
972. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Neumann series](neumann-series.md): $\sigma$ (norm exponent): The exponent $\alpha^2\theta$ in the bound $\|J\|<2^{-\sigma}$.
973. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
974. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
975. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
976. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
977. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
978. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
979. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
980. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
981. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
982. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Tensor product](tensor-product.md): $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
983. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Subset-intersection network](subset-intersection-network.md): $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
984. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Dual space](dual-space.md): $\sigma$ (example functional): The linear functional on R^2 sending x to 3x_1 - x_2.
985. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Bit network](bit-network.md): $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
986. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Line spanned by a vector](line-spanned-by-vector.md): $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
987. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Fixed-tape machine model](fixed-tape-model.md): $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
988. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Extended real numbers](extended-reals.md): $\sigma$ (generic real number): A real number used as a generic value in the order, sums and limit conditions.
989. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Gram matrix](gram-matrix.md): $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
990. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Multidimensional transform](multidimensional-transform.md): $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
991. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\sigma$ (shift count): The number of places a shift moves each coefficient.
992. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Radix-two factorization](radix-two-factorization.md): $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
993. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Diagonal scaling](diagonal-scaling.md): $\sigma$ (second scalar family): A second family of scalars, one for each label, used to compose diagonal scalings.
994. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
995. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Frequency domain](frequency-domain.md): $\sigma$ (first input position): The position of an entry of the first input sequence $a$ in the convolution sum, running from $0$ to $q-1$.
996. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Gaussian resampling](gaussian-resampling.md): $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
997. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Modular inverse](modular-inverse.md): $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
998. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Bézout's identity](bezout-identity.md): $\sigma$ (Bézout coefficient of γ): The integer multiplying γ in the combination βρ+γσ that equals gcd(β,γ).
999. $\sigma$
   - on `cyclic-coordinate`: $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
   - on [Chinese remainder theorem](chinese-remainder-theorem.md): $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
1000. $T$
   - on `cyclic-coordinate`: $T$ (box size): The number of entries of the padded box, a power of two; on this page only, not the three-element subsets of other pages.
   - on [Linear algebra basics](linear-algebra-basics.md): $T$ (linear map): A linear map between vector spaces over F.
1001. $T$
   - on `cyclic-coordinate`: $T$ (box size): The number of entries of the padded box, a power of two; on this page only, not the three-element subsets of other pages.
   - on [Symmetric matrix](symmetric-matrix.md): $T$ (three-element subset): A three-element subset of a finite set, the second triple compared with $S$.
1002. $T$
   - on `cyclic-coordinate`: $T$ (box size): The number of entries of the padded box, a power of two; on this page only, not the three-element subsets of other pages.
   - on [Bilinear form](bilinear-form.md): $T$ (triple): A three-element subset of [h], one of the triples whose indicator vectors are used.
1003. $T$
   - on `cyclic-coordinate`: $T$ (box size): The number of entries of the padded box, a power of two; on this page only, not the three-element subsets of other pages.
   - on [Indicator vector](indicator-vector.md): $T$ (triple): A single three-element subset of [h]; on the ground-set page T names all triples.
1004. $\upsilon$
   - on `cyclic-coordinate`: $\upsilon$ (twist position): An integer position from 0 to r-1 on the last coordinate, at which the phase twist acts.
   - on [Tensor product](tensor-product.md): $\upsilon$ (row index of Q): A row index of $Q$.
1005. $\upsilon$
   - on `cyclic-coordinate`: $\upsilon$ (twist position): An integer position from 0 to r-1 on the last coordinate, at which the phase twist acts.
   - on [Bit network](bit-network.md): $\upsilon$ (ground element): An element of the ground set $[h]$, indexing a central wire.
1006. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\rho$ (exponent): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
1007. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Address field](address-field.md): $\rho$ (field width): The number of bits in each of the two fields being interchanged, a count of bit positions.
1008. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Linear networks and frames](linear-network-frames.md): $\rho$ (role permutation): The permutation of roles that sends each input role to an output role.
1009. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Order of an element](order-of-element.md): $\rho$ (order): The least positive integer with sigma to the power rho equal to 1; it counts the distinct powers of sigma.
1010. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Cyclic group](cyclic-group.md): $\rho$ (generator): An element of a group, the base of its powers; when its powers are all the elements, it is the generator.
1011. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Coprime](coprime.md): $\rho$ (second integer): The other of two integers, not both zero, whose gcd is taken.
1012. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Binary change of basis](binary-change-of-basis.md): $\rho$ (residual dimension): The number of vectors in a residual basis, which counts the dimension of the edge's residual.
1013. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Dual space](dual-space.md): $\rho$ (second example functional): The linear functional on R^2 sending x to x_1.
1014. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\rho$ (coefficient position): The position of a coefficient in a record, running from 0 to r-1.
1015. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Frequency domain](frequency-domain.md): $\rho$ (second input position): The position of an entry of the second input sequence $b$ in the convolution sum, running from $0$ to $q-1$.
1016. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Cyclic convolution](cyclic-convolution.md): $\rho$ (phase sequence): The function $\rho(\delta) = e^{-\pi i \delta^2/t}$, read as a sequence of length t modulo t.
1017. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Bézout's identity](bezout-identity.md): $\rho$ (Bézout coefficient of β): The integer multiplying β in the combination βρ+γσ that equals gcd(β,γ).
1018. $\rho$
   - on `prime-number`: $\rho$ (prime): A prime number, the integer whose divisors are classified.
   - on [Ring homomorphism and isomorphism](ring-homomorphism.md): $\rho$ (substitution map): The homomorphism from W to C sending t to 1.
1019. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Cyclic coordinate](cyclic-coordinate.md): $\sigma$ (coordinate index): An integer from 1 to d that names one coordinate of the array.
1020. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
1021. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
1022. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
1023. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
1024. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
1025. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Neumann series](neumann-series.md): $\sigma$ (norm exponent): The exponent $\alpha^2\theta$ in the bound $\|J\|<2^{-\sigma}$.
1026. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
1027. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
1028. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
1029. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
1030. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
1031. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
1032. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
1033. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
1034. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
1035. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Tensor product](tensor-product.md): $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
1036. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Subset-intersection network](subset-intersection-network.md): $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
1037. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Dual space](dual-space.md): $\sigma$ (example functional): The linear functional on R^2 sending x to 3x_1 - x_2.
1038. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Bit network](bit-network.md): $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
1039. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Line spanned by a vector](line-spanned-by-vector.md): $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
1040. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Fixed-tape machine model](fixed-tape-model.md): $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
1041. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Extended real numbers](extended-reals.md): $\sigma$ (generic real number): A real number used as a generic value in the order, sums and limit conditions.
1042. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Gram matrix](gram-matrix.md): $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
1043. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Multidimensional transform](multidimensional-transform.md): $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
1044. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\sigma$ (shift count): The number of places a shift moves each coefficient.
1045. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Radix-two factorization](radix-two-factorization.md): $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
1046. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Diagonal scaling](diagonal-scaling.md): $\sigma$ (second scalar family): A second family of scalars, one for each label, used to compose diagonal scalings.
1047. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
1048. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Frequency domain](frequency-domain.md): $\sigma$ (first input position): The position of an entry of the first input sequence $a$ in the convolution sum, running from $0$ to $q-1$.
1049. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Gaussian resampling](gaussian-resampling.md): $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
1050. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Modular inverse](modular-inverse.md): $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
1051. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Bézout's identity](bezout-identity.md): $\sigma$ (Bézout coefficient of γ): The integer multiplying γ in the combination βρ+γσ that equals gcd(β,γ).
1052. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Chinese remainder theorem](chinese-remainder-theorem.md): $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
1053. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Chinese-remainder map](chinese-remainder-map.md): $\sigma$ (row index): The row index of the transform matrix $A_i$, running from $0$ to $\lambda_i-1$.
1054. $\sigma$
   - on `prime-number`: $\sigma$ (second prime): A second prime number, distinct from rho.
   - on [Ring homomorphism and isomorphism](ring-homomorphism.md): $\sigma$ (ring homomorphism): A map between rings that preserves sums, products and 1.
1055. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Radix-digit convolution](radix-digit-convolution.md): $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
1056. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Butterfly](butterfly.md): $\xi$ (first input value): The first of the two input values of the butterfly.
1057. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Permutation](permutation.md): $\xi$ (address): The position of one entry of an array.
1058. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
1059. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
1060. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Neumann series](neumann-series.md): $\xi$ (term index): The index numbering the terms of the series, a nonnegative integer.
1061. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Ring](ring.md): $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
1062. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
1063. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Congruence](congruence-modulo.md): $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
1064. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Cyclic group](cyclic-group.md): $\xi$ (exponent): An integer to which the generator is raised, giving the power $\rho^\xi$.
1065. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Coprime](coprime.md): $\xi$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the first of the two Bezout coefficients.
1066. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Tensor product](tensor-product.md): $\xi$ (row index): A row index of $P$, and in an address the output bit string $\xi$.
1067. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Subset-intersection network](subset-intersection-network.md): $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
1068. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Bilinear map](bilinear-map.md): $\xi$ (first argument): An arbitrary element of the first argument space $U$.
1069. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
1070. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Frequency domain](frequency-domain.md): $\xi$ (binary digit count): The number of binary digits of an index, so that the transform length is $q=2^{\xi}$; it counts digits.
1071. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Modular inverse](modular-inverse.md): $\xi$ (group generator): A generator of the cyclic group of order S.
1072. $\xi$
   - on `prime-number`: $\xi$ (divisor): A positive integer that divides another integer.
   - on [Bézout's identity](bezout-identity.md): $\xi$ (least positive combination): The least positive value of βρ'+γσ' over all integers ρ' and σ'.
1073. $\eta$
   - on `prime-number`: $\eta$ (cofactor): The integer that multiplies the divisor to give the integer being divided.
   - on [Linear algebra basics](linear-algebra-basics.md): $\eta$ (scalar): A scalar in F multiplying a vector.
1074. $\eta$
   - on `prime-number`: $\eta$ (cofactor): The integer that multiplies the divisor to give the integer being divided.
   - on [Transform round](transform-round.md): $\eta$ (twiddle exponent): The exponent of y at an address, so that the round multiplies each record by y to the power eta.
1075. $\eta$
   - on `prime-number`: $\eta$ (cofactor): The integer that multiplies the divisor to give the integer being divided.
   - on [Congruence](congruence-modulo.md): $\eta$ (second multiple): The integer with $e'-e=\eta B$.
1076. $\eta$
   - on `prime-number`: $\eta$ (cofactor): The integer that multiplies the divisor to give the integer being divided.
   - on [Subset-intersection network](subset-intersection-network.md): $\eta$ (target vector): The vector, indexed by triples, of the entries of the target bank along the varying coordinate.
1077. $\eta$
   - on `prime-number`: $\eta$ (cofactor): The integer that multiplies the divisor to give the integer being divided.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\eta$ (half-size): The number of positions in each half of a block at a level of the transform.
1078. $\Upsilon$
   - on `logical-bit-volume`: $\Upsilon$ (logical bit volume): The number of bits in a padded transform box, counting every entry at its record width.
   - on [Transform identity with retained permutations](transform-identity.md): $\Upsilon$ (left inverse of Gamma): A linear map with $\Upsilon\Gamma=I$, built from $N^{-1}$ and a diagonal scaling.
1079. $\Upsilon$
   - on `logical-bit-volume`: $\Upsilon$ (logical bit volume): The number of bits in a padded transform box, counting every entry at its record width.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\Upsilon$ (common exponent): The larger of the two exponents $\Gamma$ and $\Gamma'$, the number of factors of two in the common denominator of a sum.
1080. $\Upsilon$
   - on `logical-bit-volume`: $\Upsilon$ (logical bit volume): The number of bits in a padded transform box, counting every entry at its record width.
   - on [Gaussian resampling](gaussian-resampling.md): $\Upsilon$ (diagonal correction): The diagonal map multiplying entry $j$ by the factor that cancels the weight of $\Xi$ at position $j$.
1081. $Q$
   - on `logical-bit-volume`: $Q$ (entry count): The number of entries in the padded transform box.
   - on [Tensor product](tensor-product.md): $Q$ (matrix Q): A second matrix, the second factor of a tensor product.
1082. $\chi$
   - on `logical-bit-volume`: $\chi$ (record width): The number of bits in one record of the padded transform box.
   - on [Transform identity with retained permutations](transform-identity.md): $\chi$ (inverse of t): An integer with $\chi t\equiv 1 \pmod s$, so it inverts $t$ modulo $s$.
1083. $\chi$
   - on `logical-bit-volume`: $\chi$ (record width): The number of bits in one record of the padded transform box.
   - on [Two-point kernel](two-point-kernel.md): $\chi$ (array of values): An array of complex values with one entry for each address.
1084. $\chi$
   - on `logical-bit-volume`: $\chi$ (record width): The number of bits in one record of the padded transform box.
   - on [Limit inferior](limit-inferior.md): $\chi$ (sequence): A sequence of real numbers; $\chi_k$ is its $k$-th term.
1085. $V$
   - on `logical-bit-volume`: $V$ (paper's bit volume): The paper's name for the same count of bits as the logical bit volume.
   - on [Directed graph](directed-graph.md): $V$ (vertex set): The set of vertices of the directed graph, the points that edges join.
1086. $V$
   - on `logical-bit-volume`: $V$ (paper's bit volume): The paper's name for the same count of bits as the logical bit volume.
   - on [Array](array.md): $V$ (stored bit volume): The number of stored data bits in an array, the volume in which cost bounds are stated.
1087. $V$
   - on `logical-bit-volume`: $V$ (paper's bit volume): The paper's name for the same count of bits as the logical bit volume.
   - on [Payload](payload.md): $V$ (stream volume): The number of bits stored in the stream, which the time bound counts.
1088. $V$
   - on `logical-bit-volume`: $V$ (paper's bit volume): The paper's name for the same count of bits as the logical bit volume.
   - on [Big-Theta notation](big-theta-notation.md): $V$ (stored bit volume): The number of stored bits, which is of order $n$.
1089. $V$
   - on `logical-bit-volume`: $V$ (paper's bit volume): The paper's name for the same count of bits as the logical bit volume.
   - on [Cyclic shift](cyclic-shift.md): $V$ (stored bit volume): The number of stored bits in the array, a count of its data bits.
1090. $V$
   - on `logical-bit-volume`: $V$ (paper's bit volume): The paper's name for the same count of bits as the logical bit volume.
   - on [Scratch storage](scratch-storage.md): $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
1091. $V$
   - on `logical-bit-volume`: $V$ (paper's bit volume): The paper's name for the same count of bits as the logical bit volume.
   - on [Linear functional](linear-functional.md): $V$ (vector space): The vector space over F whose vectors a linear functional takes as input.
1092. $V$
   - on `logical-bit-volume`: $V$ (paper's bit volume): The paper's name for the same count of bits as the logical bit volume.
   - on [Eigenvalue](eigenvalue.md): $V$ (vector space): The vector space on which the linear operator T acts, over the field F.
1093. $V$
   - on `logical-bit-volume`: $V$ (paper's bit volume): The paper's name for the same count of bits as the logical bit volume.
   - on [Bilinear map](bilinear-map.md): $V$ (second argument space): The vector space that the second argument of the bilinear map ranges over.
1094. $V$
   - on `logical-bit-volume`: $V$ (paper's bit volume): The paper's name for the same count of bits as the logical bit volume.
   - on [Projection along a subspace](projection-along-subspace.md): $V$ (larger nested subspace): A nondegenerate subspace containing $U$, the larger of two nested labels.
1095. $V$
   - on `logical-bit-volume`: $V$ (paper's bit volume): The paper's name for the same count of bits as the logical bit volume.
   - on [Complex phase network](complex-phase-network.md): $V$ (head label): The label at the head of an edge.
1096. $b$
   - on `cost-table`: $b$ (bit length): The rounded-up base-2 logarithm of $n$, which counts the bits of $n$.
   - on [Convolution](convolution.md): $b$ (second input sequence): The second of the two input sequences, of length $n$.
1097. $b$
   - on `cost-table`: $b$ (bit length): The rounded-up base-2 logarithm of $n$, which counts the bits of $n$.
   - on [Radix-digit convolution](radix-digit-convolution.md): $b$ (digit width): The number of bits in each digit of an input.
1098. $b$
   - on `cost-table`: $b$ (bit length): The rounded-up base-2 logarithm of $n$, which counts the bits of $n$.
   - on [Integer](integer.md): $b$ (base): The base (radix) of a digit representation, an integer at least 2.
1099. $b$
   - on `cost-table`: $b$ (bit length): The rounded-up base-2 logarithm of $n$, which counts the bits of $n$.
   - on [Logarithm](logarithm.md): $b$ (base): The fixed base of the logarithm, a number greater than 1.
1100. $b$
   - on `cost-table`: $b$ (bit length): The rounded-up base-2 logarithm of $n$, which counts the bits of $n$.
   - on [Extended real numbers](extended-reals.md): $b$ (least real bound): The least real upper bound of $R$, which is the supremum of $S$ in that case.
1101. $T$
   - on `cost-table`: $T$ (padded cell count): The number of cells of the padded box, a power of two in $[4n/b, 8n/b)$.
   - on [Linear algebra basics](linear-algebra-basics.md): $T$ (linear map): A linear map between vector spaces over F.
1102. $T$
   - on `cost-table`: $T$ (padded cell count): The number of cells of the padded box, a power of two in $[4n/b, 8n/b)$.
   - on [Symmetric matrix](symmetric-matrix.md): $T$ (three-element subset): A three-element subset of a finite set, the second triple compared with $S$.
1103. $T$
   - on `cost-table`: $T$ (padded cell count): The number of cells of the padded box, a power of two in $[4n/b, 8n/b)$.
   - on [Bilinear form](bilinear-form.md): $T$ (triple): A three-element subset of [h], one of the triples whose indicator vectors are used.
1104. $T$
   - on `cost-table`: $T$ (padded cell count): The number of cells of the padded box, a power of two in $[4n/b, 8n/b)$.
   - on [Indicator vector](indicator-vector.md): $T$ (triple): A single three-element subset of [h]; on the ground-set page T names all triples.
1105. $d$
   - on `cost-table`: $d$ (axis count): The number of axes of the padded box.
   - on [Address](address.md): $d$ (address length): The number of bits in each address of the array, the length of every address string.
1106. $d$
   - on `cost-table`: $d$ (axis count): The number of axes of the padded box.
   - on [Tape procedure](tape-procedure.md): $d$ (chunk count bound): An upper bound on the number of equal-width address chunks whose selected bits one pass handles.
1107. $d$
   - on `cost-table`: $d$ (axis count): The number of axes of the padded box.
   - on [Congruence](congruence-modulo.md): $d$ (integer): An integer compared with $e$ modulo $B$.
1108. $K$
   - on `cost-table`: $K$ (chunk width): The number of bits in each address chunk.
   - on [Linear algebra basics](linear-algebra-basics.md): $K$ (address block): The second bit block of an address.
1109. $K$
   - on `cost-table`: $K$ (chunk width): The number of bits in each address chunk.
   - on [Two-point kernel](two-point-kernel.md): $K$ (two-point kernel): The 2 by 2 matrix delta I plus kappa X, which is the two-point kernel.
1110. $\ell$
   - on `cost-table`: $\ell$ (axis exponent): The exponent with $r = 2^{\ell}$, which counts the factors of two in $r$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\ell$ (output index): An integer index running over $0, 1, \ldots, q-1$ that labels an output coordinate $(F_q f)_\ell$.
1111. $\ell$
   - on `cost-table`: $\ell$ (axis exponent): The exponent with $r = 2^{\ell}$, which counts the factors of two in $r$.
   - on [Linear networks and frames](linear-network-frames.md): $\ell$ (input wire): An input wire of the network, whose supplied array and source vertex are named.
1112. $\ell$
   - on `cost-table`: $\ell$ (axis exponent): The exponent with $r = 2^{\ell}$, which counts the factors of two in $r$.
   - on [Subset-intersection network](subset-intersection-network.md): $\ell$ (ground element): An element of the ground set $[h]$, which names one central wire.
1113. $c$
   - on `cost-table`: $c$ (chunk exponent): A fixed positive exponent, equal to $2^{-56}$.
   - on [Convolution](convolution.md): $c$ (convolution): The convolution of $a$ and $b$, a sequence of length $2n-1$.
1114. $c$
   - on `cost-table`: $c$ (chunk exponent): A fixed positive exponent, equal to $2^{-56}$.
   - on [Integer](integer.md): $c$ (digit): A digit of a digit list, an integer between 0 and the base minus one.
1115. $c$
   - on `cost-table`: $c$ (chunk exponent): A fixed positive exponent, equal to $2^{-56}$.
   - on [Transform identity with retained permutations](transform-identity.md): $c$ (unit multiplier): A unit modulo $s$ that defines the retained permutation $\Pi_c$.
1116. $c$
   - on `cost-table`: $c$ (chunk exponent): A fixed positive exponent, equal to $2^{-56}$.
   - on [Scratch storage](scratch-storage.md): $c$ (starting central values): The vector of starting values of the central wires.
1117. $c$
   - on `cost-table`: $c$ (chunk exponent): A fixed positive exponent, equal to $2^{-56}$.
   - on [Eigenvalue](eigenvalue.md): $c$ (average entry): The average of the entries of x, which is the coefficient of the all-ones vector in its split.
1118. $c$
   - on `cost-table`: $c$ (chunk exponent): A fixed positive exponent, equal to $2^{-56}$.
   - on [Near-linear time](near-linear-time.md): $c$ (log exponent): A fixed real number, the power to which the logarithm factor of a near-linear bound is raised.
1119. $\tau$
   - on `cost-table`: $\tau$ (exchange exponent): The exponent $1-2^{-50}$ in the cost of a chunk exchange.
   - on [Payload](payload.md): $\tau$ (fixed exponent): A fixed exponent strictly between 0 and 1 that sets the power of L in the time bound.
1120. $\tau$
   - on `cost-table`: $\tau$ (exchange exponent): The exponent $1-2^{-50}$ in the cost of a chunk exchange.
   - on [Address-field interchange](address-interchange.md): $\tau$ (fixed exponent): A fixed number below 1, the exponent in the cost bound $O(Vu^{\tau})$.
1121. $\tau$
   - on `cost-table`: $\tau$ (exchange exponent): The exponent $1-2^{-50}$ in the cost of a chunk exchange.
   - on [Extended real numbers](extended-reals.md): $\tau$ (sequence term): The term of a sequence at position $\delta$.
1122. $\tau$
   - on `cost-table`: $\tau$ (exchange exponent): The exponent $1-2^{-50}$ in the cost of a chunk exchange.
   - on [Diagonal scaling](diagonal-scaling.md): $\tau$ (scalar family): A family of scalars $\tau_\iota$ in $F$, one for each label, which defines a diagonal scaling.
1123. $\delta$
   - on `cost-table`: $\delta$ (small exponent): A fixed small exponent, equal to $1/16$.
   - on [Permutation](permutation.md): $\delta$ (fourth entry): The entry of the sequence at position 4.
1124. $\delta$
   - on `cost-table`: $\delta$ (small exponent): A fixed small exponent, equal to $1/16$.
   - on [Transform round](transform-round.md): $\delta$ (remainder): The remainder of eta on division by r, from 0 to r minus 1.
1125. $\delta$
   - on `cost-table`: $\delta$ (small exponent): A fixed small exponent, equal to $1/16$.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $\delta$ (chunk width): The number of consecutive address bits in each transform axis (chunk).
1126. $\delta$
   - on `cost-table`: $\delta$ (small exponent): A fixed small exponent, equal to $1/16$.
   - on [Two-point kernel](two-point-kernel.md): $\delta$ (identity coefficient): The complex coefficient of the identity matrix in a two-point kernel.
1127. $\delta$
   - on `cost-table`: $\delta$ (small exponent): A fixed small exponent, equal to $1/16$.
   - on [Congruence](congruence-modulo.md): $\delta$ (remainder): The unique integer in $\{0,\dots,B-1\}$ lying in a residue class.
1128. $\delta$
   - on `cost-table`: $\delta$ (small exponent): A fixed small exponent, equal to $1/16$.
   - on [Limit inferior](limit-inferior.md): $\delta$ (arbitrary positive real): A real number greater than zero, arbitrary in the negation of the conjecture.
1129. $\delta$
   - on `cost-table`: $\delta$ (small exponent): A fixed small exponent, equal to $1/16$.
   - on [Extended real numbers](extended-reals.md): $\delta$ (term position): The position of a term in a sequence, a positive integer.
1130. $\alpha$
   - on `cost-table`: $\alpha$ (line-map factor): The factor that scales the cost of the line maps.
   - on [Address](address.md): $\alpha$ (address string): A binary string of $d$ bits that labels one entry of the array.
1131. $\alpha$
   - on `cost-table`: $\alpha$ (line-map factor): The factor that scales the cost of the line maps.
   - on [Permutation](permutation.md): $\alpha$ (first entry): The entry of the sequence at position 1.
1132. $\alpha$
   - on `cost-table`: $\alpha$ (line-map factor): The factor that scales the cost of the line maps.
   - on [Neumann series](neumann-series.md): $\alpha$ (construction parameter): A parameter of the paper's construction, not the address letter of earlier pages.
1133. $N$
   - on `established-multiplier`: $N$ (input bit length): The number of bits in each input of the multiplier, the count of input bits.
   - on [Address](address.md): $N$ (entry count): The number of entries in the array, counting each stored entry once; it counts the positions $0$ through $N-1$.
1134. $N$
   - on `established-multiplier`: $N$ (input bit length): The number of bits in each input of the multiplier, the count of input bits.
   - on [Neumann series](neumann-series.md): $N$ (paper's operator): The operator $I+J$ of the paper, with $J=N-I$; the letter changes meaning from earlier pages.
1135. $f$
   - on `signed-packing`: $f$ (integer polynomial): The first factor, an integer polynomial in $y$ with $r$ coefficients.
   - on [Big-Theta notation](big-theta-notation.md): $f$ (bounded function): The function from input sizes to nonnegative reals whose order is compared with that of $h$.
1136. $f$
   - on `signed-packing`: $f$ (integer polynomial): The first factor, an integer polynomial in $y$ with $r$ coefficients.
   - on [Bijection](bijection.md): $f$ (map): The map from the source set $U$ to the target set $W$ whose bijectivity is tested.
1137. $f$
   - on `signed-packing`: $f$ (integer polynomial): The first factor, an integer polynomial in $y$ with $r$ coefficients.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $f$ (input vector): A vector of $q$ complex numbers, the input to the transform, with coordinates $f_0, \ldots, f_{q-1}$.
1138. $f$
   - on `signed-packing`: $f$ (integer polynomial): The first factor, an integer polynomial in $y$ with $r$ coefficients.
   - on [Polynomial ring](polynomial-ring.md): $f$ (modulus polynomial): The fixed monic polynomial with complex coefficients by which the ring is reduced.
1139. $f$
   - on `signed-packing`: $f$ (integer polynomial): The first factor, an integer polynomial in $y$ with $r$ coefficients.
   - on [Dual space](dual-space.md): $f$ (linear functional): A generic element of the dual space U^*, which is a linear map from U to F.
1140. $f$
   - on `signed-packing`: $f$ (integer polynomial): The first factor, an integer polynomial in $y$ with $r$ coefficients.
   - on [Linear functional](linear-functional.md): $f$ (linear functional): The map from V to F under study, which sends each vector to one scalar and respects addition and scalar multiplication.
1141. $f$
   - on `signed-packing`: $f$ (integer polynomial): The first factor, an integer polynomial in $y$ with $r$ coefficients.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $f$ (input list): The list of $N$ records that the transform takes as input.
1142. $f$
   - on `signed-packing`: $f$ (integer polynomial): The first factor, an integer polynomial in $y$ with $r$ coefficients.
   - on [Opposite transform](opposite-transform.md): $f$ (first input array): The first of the two disk-grid ring arrays whose convolution is taken.
1143. $f$
   - on `signed-packing`: $f$ (integer polynomial): The first factor, an integer polynomial in $y$ with $r$ coefficients.
   - on [Frequency domain](frequency-domain.md): $f$ (sequence): A sequence $f=(f_0,\ldots,f_{q-1})$ of $q$ complex numbers, whose frequency domain is taken.
1144. $g$
   - on `signed-packing`: $g$ (integer polynomial): The second factor, an integer polynomial in $y$ with $r$ coefficients.
   - on [Linear algebra basics](linear-algebra-basics.md): $g$ (logical array): The array the computation means.
1145. $g$
   - on `signed-packing`: $g$ (integer polynomial): The second factor, an integer polynomial in $y$ with $r$ coefficients.
   - on [Opposite transform](opposite-transform.md): $g$ (second input array): The second of the two disk-grid ring arrays whose convolution is taken.
1146. $p$
   - on `signed-packing`: $p$ (coefficient bit bound): The number of bits in a bound on the coefficient magnitudes, so that each coefficient has absolute value at most $2^p$.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $p$ (working precision): The working precision in bits: the inputs lie on the grid $2^{-p}\mathbb Z[i]$.
1147. $p$
   - on `signed-packing`: $p$ (coefficient bit bound): The number of bits in a bound on the coefficient magnitudes, so that each coefficient has absolute value at most $2^p$.
   - on [Truncation](truncation.md): $p$ (precision): The number of fractional binary places kept, which counts the binary digits after the point.
1148. $h$
   - on `signed-packing`: $h$ (ordinary product): The ordinary product $fg$ of the two integer polynomials.
   - on [Big-Theta notation](big-theta-notation.md): $h$ (comparison function): The function from input sizes to nonnegative reals against which $f$ is compared.
1149. $h$
   - on `signed-packing`: $h$ (ordinary product): The ordinary product $fg$ of the two integer polynomials.
   - on [Array norm](array-norm.md): $h$ (ring element): An element of the ring modulo y^r+1, written as a polynomial in y.
1150. $h$
   - on `signed-packing`: $h$ (ordinary product): The ordinary product $fg$ of the two integer polynomials.
   - on [Linear networks and frames](linear-network-frames.md): $h$ (route position): The position of a vertex along a route, running from $0$ to $L$.
1151. $h$
   - on `signed-packing`: $h$ (ordinary product): The ordinary product $fg$ of the two integer polynomials.
   - on [Transform round](transform-round.md): $h$ (highest unprocessed bit): The position of the highest unprocessed address bit on axis i, which receives the branch bit.
1152. $h$
   - on `signed-packing`: $h$ (ordinary product): The ordinary product $fg$ of the two integer polynomials.
   - on [Eigenvalue](eigenvalue.md): $h$ (coordinate count): The number of coordinates of each vector in Q^h, at least 2.
1153. $h$
   - on `signed-packing`: $h$ (ordinary product): The ordinary product $fg$ of the two integer polynomials.
   - on [Ground set](ground-set.md): $h$ (ground set size): The number of elements of the ground set, the count of its elements.
1154. $B$
   - on `signed-packing`: $B$ (block base): The block base $2^{4p}$, the value substituted for $y$ and the modulus of the congruence used for recovery.
   - on [Congruence](congruence-modulo.md): $B$ (modulus): The positive integer modulus by which congruence is taken.
1155. $B$
   - on `signed-packing`: $B$ (block base): The block base $2^{4p}$, the value substituted for $y$ and the modulus of the congruence used for recovery.
   - on [Linear algebra basics](linear-algebra-basics.md): $B$ (candidate inverse): A matrix that satisfies AB=BA=I.
1156. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
1157. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
1158. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
1159. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
1160. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
1161. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
1162. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
1163. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
1164. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
1165. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
1166. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Neumann series](neumann-series.md): $\sigma$ (norm exponent): The exponent $\alpha^2\theta$ in the bound $\|J\|<2^{-\sigma}$.
1167. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
1168. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
1169. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
1170. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
1171. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Tensor product](tensor-product.md): $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
1172. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Subset-intersection network](subset-intersection-network.md): $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
1173. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Dual space](dual-space.md): $\sigma$ (example functional): The linear functional on R^2 sending x to 3x_1 - x_2.
1174. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Bit network](bit-network.md): $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
1175. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Line spanned by a vector](line-spanned-by-vector.md): $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
1176. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Fixed-tape machine model](fixed-tape-model.md): $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
1177. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Extended real numbers](extended-reals.md): $\sigma$ (generic real number): A real number used as a generic value in the order, sums and limit conditions.
1178. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Gram matrix](gram-matrix.md): $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
1179. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Multidimensional transform](multidimensional-transform.md): $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
1180. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\sigma$ (shift count): The number of places a shift moves each coefficient.
1181. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Radix-two factorization](radix-two-factorization.md): $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
1182. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Diagonal scaling](diagonal-scaling.md): $\sigma$ (second scalar family): A second family of scalars, one for each label, used to compose diagonal scalings.
1183. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
1184. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Frequency domain](frequency-domain.md): $\sigma$ (first input position): The position of an entry of the first input sequence $a$ in the convolution sum, running from $0$ to $q-1$.
1185. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Gaussian resampling](gaussian-resampling.md): $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
1186. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Chinese remainder theorem](chinese-remainder-theorem.md): $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
1187. $\sigma$
   - on `signed-packing`: $\sigma$ (centered residue): The unique integer in $[-B/2, B/2)$ congruent to $f(B)\,g(B)$ modulo $B$.
   - on [Destination rank](destination-rank.md): $\sigma$ (chunk stride): The amount the rank changes when a chunk rises by one with the other two fixed; $\sigma_1$, $\sigma_2$, $\sigma_3$ are the strides of chunks 1, 2 and 3.
1188. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
1189. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
1190. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
1191. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
1192. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
1193. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Neumann series](neumann-series.md): $\sigma$ (norm exponent): The exponent $\alpha^2\theta$ in the bound $\|J\|<2^{-\sigma}$.
1194. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
1195. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
1196. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
1197. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
1198. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
1199. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
1200. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
1201. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
1202. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
1203. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Tensor product](tensor-product.md): $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
1204. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Subset-intersection network](subset-intersection-network.md): $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
1205. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Dual space](dual-space.md): $\sigma$ (example functional): The linear functional on R^2 sending x to 3x_1 - x_2.
1206. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Bit network](bit-network.md): $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
1207. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Line spanned by a vector](line-spanned-by-vector.md): $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
1208. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Fixed-tape machine model](fixed-tape-model.md): $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
1209. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Extended real numbers](extended-reals.md): $\sigma$ (generic real number): A real number used as a generic value in the order, sums and limit conditions.
1210. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Gram matrix](gram-matrix.md): $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
1211. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Multidimensional transform](multidimensional-transform.md): $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
1212. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\sigma$ (shift count): The number of places a shift moves each coefficient.
1213. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Radix-two factorization](radix-two-factorization.md): $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
1214. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Diagonal scaling](diagonal-scaling.md): $\sigma$ (second scalar family): A second family of scalars, one for each label, used to compose diagonal scalings.
1215. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
1216. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Frequency domain](frequency-domain.md): $\sigma$ (first input position): The position of an entry of the first input sequence $a$ in the convolution sum, running from $0$ to $q-1$.
1217. $\sigma$
   - on `schoolbook-multiplication`: $\sigma$ (bit position): An integer from 0 to n-1 giving the position of a bit of y, counted from the least significant end.
   - on [Gaussian resampling](gaussian-resampling.md): $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
1218. $a$
   - on `polynomial-ring-convolution`: $a$ (record address): An address of the first input array, which indexes its records.
   - on [Convolution](convolution.md): $a$ (first input sequence): The first of the two input sequences, of length $n$.
1219. $a$
   - on `polynomial-ring-convolution`: $a$ (record address): An address of the first input array, which indexes its records.
   - on [Scratch storage](scratch-storage.md): $a$ (starting side values): The vector of starting values of the side wires.
1220. $b$
   - on `polynomial-ring-convolution`: $b$ (record address): An address of the second input array, which indexes its records.
   - on [Convolution](convolution.md): $b$ (second input sequence): The second of the two input sequences, of length $n$.
1221. $b$
   - on `polynomial-ring-convolution`: $b$ (record address): An address of the second input array, which indexes its records.
   - on [Logarithm](logarithm.md): $b$ (base): The fixed base of the logarithm, a number greater than 1.
1222. $b$
   - on `polynomial-ring-convolution`: $b$ (record address): An address of the second input array, which indexes its records.
   - on [Integer](integer.md): $b$ (base): The base (radix) of a digit representation, an integer at least 2.
1223. $b$
   - on `polynomial-ring-convolution`: $b$ (record address): An address of the second input array, which indexes its records.
   - on [Radix-digit convolution](radix-digit-convolution.md): $b$ (digit width): The number of bits in each digit of an input.
1224. $b$
   - on `polynomial-ring-convolution`: $b$ (record address): An address of the second input array, which indexes its records.
   - on [Cost table](cost-table.md): $b$ (bit length): The rounded-up base-2 logarithm of $n$, which counts the bits of $n$.
1225. $b$
   - on `polynomial-ring-convolution`: $b$ (record address): An address of the second input array, which indexes its records.
   - on [Extended real numbers](extended-reals.md): $b$ (least real bound): The least real upper bound of $R$, which is the supremum of $S$ in that case.
1226. $\mu$
   - on `polynomial-ring-convolution`: $\mu$ (record count): The number of records in an array, the product of the axis lengths.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $\mu$ (bit-flip coefficient): The coefficient of $X$ in $C$, equal to $(1-i)/2$.
1227. $j$
   - on `polynomial-ring-convolution`: $j$ (frequency address): An integer index of a transform entry, one entry per axis.
   - on [Mixed-radix digits](mixed-radix-digits.md): $j$ (place index): A place, numbered from 1 to beta.
1228. $j$
   - on `polynomial-ring-convolution`: $j$ (frequency address): An integer index of a transform entry, one entry per axis.
   - on [Linear algebra basics](linear-algebra-basics.md): $j$ (coordinate index): The index of a coordinate of a vector, running from 1 to m.
1229. $j$
   - on `polynomial-ring-convolution`: $j$ (frequency address): An integer index of a transform entry, one entry per axis.
   - on [Convolution](convolution.md): $j$ (input position in b): The position of an entry of $b$.
1230. $j$
   - on `polynomial-ring-convolution`: $j$ (frequency address): An integer index of a transform entry, one entry per axis.
   - on [Integer](integer.md): $j$ (digit position): The position of a digit or bit, counted from the left starting at 1.
1231. $j$
   - on `polynomial-ring-convolution`: $j$ (frequency address): An integer index of a transform entry, one entry per axis.
   - on [Ceiling function](ceiling-function.md): $j$ (integer): Any integer, which is its own ceiling.
1232. $j$
   - on `polynomial-ring-convolution`: $j$ (frequency address): An integer index of a transform entry, one entry per axis.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $j$ (input index): The index of an input value in the transform $F_q$.
1233. $j$
   - on `polynomial-ring-convolution`: $j$ (frequency address): An integer index of a transform entry, one entry per axis.
   - on [Address-field interchange](address-interchange.md): $j$ (level index): The level of a call, so a call on width $m^j$ sits at level $j$.
1234. $j$
   - on `polynomial-ring-convolution`: $j$ (frequency address): An integer index of a transform entry, one entry per axis.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $j$ (entry index): The index that numbers the entries of a list, running from $0$ to $N-1$.
1235. $k$
   - on `polynomial-ring-convolution`: $k$ (summation index): The index of the sum on an axis, running over the $t$ positions of that axis.
   - on [Telescoping identity](telescoping-identity.md): $k$ (term position): The position of a term in the sequence, running from 0 to o.
1236. $k$
   - on `polynomial-ring-convolution`: $k$ (summation index): The index of the sum on an axis, running over the $t$ positions of that axis.
   - on [Root of unity](root-of-unity.md): $k$ (integer exponent): An integer exponent of $y$ in the power $y^k$ that multiplies the coefficient list.
1237. $k$
   - on `polynomial-ring-convolution`: $k$ (summation index): The index of the sum on an axis, running over the $t$ positions of that axis.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $k$ (padded length): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
1238. $k$
   - on `polynomial-ring-convolution`: $k$ (summation index): The index of the sum on an axis, running over the $t$ positions of that axis.
   - on [Integer](integer.md): $k$ (digit count): The number of digits in a digit list.
1239. $k$
   - on `polynomial-ring-convolution`: $k$ (summation index): The index of the sum on an axis, running over the $t$ positions of that axis.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $k$ (output index): The index of an output coordinate of the transform $F_q$.
1240. $k$
   - on `polynomial-ring-convolution`: $k$ (summation index): The index of the sum on an axis, running over the $t$ positions of that axis.
   - on [Address-field interchange](address-interchange.md): $k$ (level count): The number of levels of the recursion, the logarithm to base m of the field width u.
1241. $k$
   - on `polynomial-ring-convolution`: $k$ (summation index): The index of the sum on an axis, running over the $t$ positions of that axis.
   - on [Limit inferior](limit-inferior.md): $k$ (term position): A position in a sequence, the index of a term.
1242. $k$
   - on `polynomial-ring-convolution`: $k$ (summation index): The index of the sum on an axis, running over the $t$ positions of that axis.
   - on [Multidimensional transform](multidimensional-transform.md): $k$ (radix-two exponent): The exponent with t_sigma equal to 2^k, which counts the radix-two levels of the axis transform.
1243. $k$
   - on `polynomial-ring-convolution`: $k$ (summation index): The index of the sum on an axis, running over the $t$ positions of that axis.
   - on [Gaussian resampling](gaussian-resampling.md): $k$ (output index): The index of an entry of a length-$W$ output vector, running from $0$ to $W-1$.
1244. $\odot$
   - on `polynomial-ring-convolution`: $\odot$ (entrywise product): The product of two arrays entry by entry, divided by the record length $r$.
   - on [Pointwise product](pointwise-product.md): $\odot$ (pointwise product): The operation giving $a\odot b$, the sequence whose entry at each position is the product of the two entries at that position.
1245. $\ell$
   - on `polynomial-ring-convolution`: $\ell$ (record length exponent): The integer exponent with $r=2^\ell$, the base-two logarithm of the record length.
   - on [Fixed-width digit blocks](fixed-width-digit-blocks.md): $\ell$ (place index): The position of a digit in a block, running from 0 to L-1, with 0 the least significant place.
1246. $\ell$
   - on `polynomial-ring-convolution`: $\ell$ (record length exponent): The integer exponent with $r=2^\ell$, the base-two logarithm of the record length.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\ell$ (output index): An integer index running over $0, 1, \ldots, q-1$ that labels an output coordinate $(F_q f)_\ell$.
1247. $\ell$
   - on `polynomial-ring-convolution`: $\ell$ (record length exponent): The integer exponent with $r=2^\ell$, the base-two logarithm of the record length.
   - on [Cost table](cost-table.md): $\ell$ (axis exponent): The exponent with $r = 2^{\ell}$, which counts the factors of two in $r$.
1248. $\ell$
   - on `polynomial-ring-convolution`: $\ell$ (record length exponent): The integer exponent with $r=2^\ell$, the base-two logarithm of the record length.
   - on [Linear networks and frames](linear-network-frames.md): $\ell$ (input wire): An input wire of the network, whose supplied array and source vertex are named.
1249. $\ell$
   - on `polynomial-ring-convolution`: $\ell$ (record length exponent): The integer exponent with $r=2^\ell$, the base-two logarithm of the record length.
   - on [Subset-intersection network](subset-intersection-network.md): $\ell$ (ground element): An element of the ground set $[h]$, which names one central wire.
1250. $j'$
   - on `normalized-cyclic-convolution`: $j'$ (second input index): The position of an entry of $g$ paired with the position $j$ of $f$ in the sum for a transform entry.
   - on [Transform identity with retained permutations](transform-identity.md): $j'$ (second position): A second position in $\{0,\dots,s-1\}$, compared with $j$.
1251. $m$
   - on `normalized-cyclic-convolution`: $m$ (chirp argument): A free integer at which the chirp phase $\chi_m$ is evaluated; this letter changes meaning here and is not the order of a root.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
1252. $m$
   - on `normalized-cyclic-convolution`: $m$ (chirp argument): A free integer at which the chirp phase $\chi_m$ is evaluated; this letter changes meaning here and is not the order of a root.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
1253. $m$
   - on `normalized-cyclic-convolution`: $m$ (chirp argument): A free integer at which the chirp phase $\chi_m$ is evaluated; this letter changes meaning here and is not the order of a root.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
1254. $m$
   - on `normalized-cyclic-convolution`: $m$ (chirp argument): A free integer at which the chirp phase $\chi_m$ is evaluated; this letter changes meaning here and is not the order of a root.
   - on [Address-field interchange](address-interchange.md): $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
1255. $m$
   - on `normalized-cyclic-convolution`: $m$ (chirp argument): A free integer at which the chirp phase $\chi_m$ is evaluated; this letter changes meaning here and is not the order of a root.
   - on [Limit inferior](limit-inferior.md): $m$ (tail start): The position from which a tail of the sequence starts.
1256. $m$
   - on `normalized-cyclic-convolution`: $m$ (chirp argument): A free integer at which the chirp phase $\chi_m$ is evaluated; this letter changes meaning here and is not the order of a root.
   - on [Opposite transform](opposite-transform.md): $m$ (summation index): A dummy summation index running from $0$ to $q-1$ that names an input position of a vector; it counts nothing.
1257. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Negacyclic convolution](negacyclic-convolution.md): $\sigma$ (negacyclic convolution): The sequence of n complex numbers that is the negacyclic convolution of a and b.
1258. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Modular inverse](modular-inverse.md): $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
1259. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
1260. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
1261. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
1262. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
1263. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
1264. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
1265. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
1266. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Bézout's identity](bezout-identity.md): $\sigma$ (Bézout coefficient of γ): The integer multiplying γ in the combination βρ+γσ that equals gcd(β,γ).
1267. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
1268. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Chinese remainder theorem](chinese-remainder-theorem.md): $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
1269. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Gaussian resampling](gaussian-resampling.md): $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
1270. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Multidimensional transform](multidimensional-transform.md): $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
1271. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\sigma$ (shift count): The number of places a shift moves each coefficient.
1272. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Radix-two factorization](radix-two-factorization.md): $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
1273. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Neumann series](neumann-series.md): $\sigma$ (norm exponent): The exponent $\alpha^2\theta$ in the bound $\|J\|<2^{-\sigma}$.
1274. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
1275. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
1276. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
1277. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
1278. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
1279. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
1280. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Tensor product](tensor-product.md): $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
1281. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Subset-intersection network](subset-intersection-network.md): $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
1282. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Dual space](dual-space.md): $\sigma$ (example functional): The linear functional on R^2 sending x to 3x_1 - x_2.
1283. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Bit network](bit-network.md): $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
1284. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Line spanned by a vector](line-spanned-by-vector.md): $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
1285. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Fixed-tape machine model](fixed-tape-model.md): $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
1286. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Extended real numbers](extended-reals.md): $\sigma$ (generic real number): A real number used as a generic value in the order, sums and limit conditions.
1287. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Gram matrix](gram-matrix.md): $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
1288. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Diagonal scaling](diagonal-scaling.md): $\sigma$ (second scalar family): A second family of scalars, one for each label, used to compose diagonal scalings.
1289. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
1290. $\sigma$
   - on `bluestein-chirp-identity`: $\sigma$ (chirp position): An integer position at which the chirp is evaluated, which may be negative or at least $q$.
   - on [Frequency domain](frequency-domain.md): $\sigma$ (first input position): The position of an entry of the first input sequence $a$ in the convolution sum, running from $0$ to $q-1$.
1291. $\cdot$
   - on `bluestein-chirp-identity`: $\cdot$ (coordinatewise product): The product of two vectors taken entry by entry.
   - on [Normalized cyclic convolution](normalized-cyclic-convolution.md): $\cdot$ (entrywise product): The product of two vectors taken position by position.
1292. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Gaussian resampling](gaussian-resampling.md): $\sigma$ (Gaussian width): The width of the Gaussian weights, an integer at least 2 with $\sigma^2<p$.
1293. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
1294. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
1295. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Multidimensional transform](multidimensional-transform.md): $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
1296. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\sigma$ (shift count): The number of places a shift moves each coefficient.
1297. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Radix-two factorization](radix-two-factorization.md): $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
1298. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
1299. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
1300. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
1301. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
1302. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Neumann series](neumann-series.md): $\sigma$ (norm exponent): The exponent $\alpha^2\theta$ in the bound $\|J\|<2^{-\sigma}$.
1303. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
1304. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
1305. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
1306. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
1307. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
1308. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
1309. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
1310. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
1311. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Tensor product](tensor-product.md): $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
1312. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Subset-intersection network](subset-intersection-network.md): $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
1313. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Dual space](dual-space.md): $\sigma$ (example functional): The linear functional on R^2 sending x to 3x_1 - x_2.
1314. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Bit network](bit-network.md): $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
1315. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Line spanned by a vector](line-spanned-by-vector.md): $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
1316. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Fixed-tape machine model](fixed-tape-model.md): $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
1317. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Extended real numbers](extended-reals.md): $\sigma$ (generic real number): A real number used as a generic value in the order, sums and limit conditions.
1318. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Gram matrix](gram-matrix.md): $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
1319. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Diagonal scaling](diagonal-scaling.md): $\sigma$ (second scalar family): A second family of scalars, one for each label, used to compose diagonal scalings.
1320. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $\sigma$ (exponent of y): An integer exponent of $y$, the power being reduced or the order being tested.
1321. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Frequency domain](frequency-domain.md): $\sigma$ (first input position): The position of an entry of the first input sequence $a$ in the convolution sum, running from $0$ to $q-1$.
1322. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Modular inverse](modular-inverse.md): $\sigma$ (integer quotient): The integer quotient of beta times mu minus 1 divided by M.
1323. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Bézout's identity](bezout-identity.md): $\sigma$ (Bézout coefficient of γ): The integer multiplying γ in the combination βρ+γσ that equals gcd(β,γ).
1324. $\sigma$
   - on `normalization-scales`: $\sigma$ (digit scale): The factor $2^{-b-2}$ by which each digit is scaled, so that a stored value is $\sigma$ times its digit.
   - on [Chinese remainder theorem](chinese-remainder-theorem.md): $\sigma$ (congruence index): An integer index numbering the congruences, running from 1 to J.
1325. $m$
   - on `normalization-scales`: $m$ (digit count): The number of digits of each input, which is also the number of entries of each digit array.
   - on [Normalized cyclic convolution](normalized-cyclic-convolution.md): $m$ (chirp argument): A free integer at which the chirp phase $\chi_m$ is evaluated; this letter changes meaning here and is not the order of a root.
1326. $m$
   - on `normalization-scales`: $m$ (digit count): The number of digits of each input, which is also the number of entries of each digit array.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
1327. $m$
   - on `normalization-scales`: $m$ (digit count): The number of digits of each input, which is also the number of entries of each digit array.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
1328. $m$
   - on `normalization-scales`: $m$ (digit count): The number of digits of each input, which is also the number of entries of each digit array.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
1329. $m$
   - on `normalization-scales`: $m$ (digit count): The number of digits of each input, which is also the number of entries of each digit array.
   - on [Address-field interchange](address-interchange.md): $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
1330. $m$
   - on `normalization-scales`: $m$ (digit count): The number of digits of each input, which is also the number of entries of each digit array.
   - on [Limit inferior](limit-inferior.md): $m$ (tail start): The position from which a tail of the sequence starts.
1331. $m$
   - on `normalization-scales`: $m$ (digit count): The number of digits of each input, which is also the number of entries of each digit array.
   - on [Opposite transform](opposite-transform.md): $m$ (summation index): A dummy summation index running from $0$ to $q-1$ that names an input position of a vector; it counts nothing.
1332. $\varsigma$
   - on `middle-transform`: $\varsigma$ (chirp factor): The unit complex number $\varsigma_j=\exp(-\pi i s j^2/t)$ attached to each integer $j$.
   - on [Subspace labels](subspace-labels.md): $\varsigma$ (translation coefficient): The coefficient of the translation in a translation kernel.
1333. $\zeta$
   - on `phase-twist`: $\zeta$ (twist root): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
   - on [Modular inverse](modular-inverse.md): $\zeta$ (positive exponent): A positive integer exponent for which the power of the image is 1.
1334. $\zeta$
   - on `phase-twist`: $\zeta$ (twist root): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
   - on [Butterfly](butterfly.md): $\zeta$ (second input value): The second of the two input values of the butterfly.
1335. $\zeta$
   - on `phase-twist`: $\zeta$ (twist root): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
   - on [Cyclic shift](cyclic-shift.md): $\zeta$ (position): A position in the block, numbered from 0 to J-1.
1336. $\zeta$
   - on `phase-twist`: $\zeta$ (twist root): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
   - on [Coprime](coprime.md): $\zeta$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the second of the two Bezout coefficients.
1337. $\zeta$
   - on `phase-twist`: $\zeta$ (twist root): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
   - on [Congruence](congruence-modulo.md): $\zeta$ (third integer): An integer used in the transitivity argument, with $e \equiv \zeta$.
1338. $\zeta$
   - on `phase-twist`: $\zeta$ (twist root): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
   - on [Phase factor](phase-factor.md): $\zeta$ (phase factor): A complex number of modulus one, the factor multiplied into coefficients.
1339. $\zeta$
   - on `phase-twist`: $\zeta$ (twist root): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
   - on [Ring](ring.md): $\zeta$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
1340. $\zeta$
   - on `phase-twist`: $\zeta$ (twist root): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\zeta$ (residue): A residue, represented by the integer $\zeta$ with $0\le\zeta<2^\sigma$.
1341. $\zeta$
   - on `phase-twist`: $\zeta$ (twist root): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
   - on [Tensor product](tensor-product.md): $\zeta$ (column index of Q): A column index of $Q$.
1342. $\zeta$
   - on `phase-twist`: $\zeta$ (twist root): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
   - on [Bilinear map](bilinear-map.md): $\zeta$ (second argument): An arbitrary element of the second argument space $V$.
1343. $\zeta$
   - on `phase-twist`: $\zeta$ (twist root): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $\zeta$ (root of unity): An element of the ring whose positive integer power equals 1.
1344. $\zeta$
   - on `phase-twist`: $\zeta$ (twist root): The root of unity $e^{\pi i/r}$ of order $2r$, whose powers multiply the coefficients in the twist.
   - on [Frequency domain](frequency-domain.md): $\zeta$ (frequency summation index): An index running over the frequencies $0,\ldots,q-1$, summed over in the inversion identity.
1345. $e$
   - on `phase-twist`: $e$ (Euler's number): The base of the natural exponential, so that $e^{i\theta} = \cos\theta + i\sin\theta$.
   - on [Congruence](congruence-modulo.md): $e$ (integer): An integer compared with $d$ modulo $B$.
1346. $e$
   - on `phase-twist`: $e$ (Euler's number): The base of the natural exponential, so that $e^{i\theta} = \cos\theta + i\sin\theta$.
   - on [Telescoping identity](telescoping-identity.md): $e$ (last position): The last position of a sum over positions, the upper limit of the sum.
1347. $e$
   - on `phase-twist`: $e$ (Euler's number): The base of the natural exponential, so that $e^{i\theta} = \cos\theta + i\sin\theta$.
   - on [Transform round](transform-round.md): $e$ (quotient): The integer quotient of eta by r: the number of whole multiples of r in eta.
1348. $e$
   - on `phase-twist`: $e$ (Euler's number): The base of the natural exponential, so that $e^{i\theta} = \cos\theta + i\sin\theta$.
   - on [Two-point kernel](two-point-kernel.md): $e$ (bit position): An index from 0 to d-1 naming the bit along which a kernel acts, counted from the least significant bit.
1349. $e$
   - on `phase-twist`: $e$ (Euler's number): The base of the natural exponential, so that $e^{i\theta} = \cos\theta + i\sin\theta$.
   - on [Eigenvalue](eigenvalue.md): $e$ (eigenvector): A nonzero vector of V that T maps to a multiple of itself.
1350. $e$
   - on `phase-twist`: $e$ (Euler's number): The base of the natural exponential, so that $e^{i\theta} = \cos\theta + i\sin\theta$.
   - on [Indicator vector](indicator-vector.md): $e$ (position): An element of the ground set [h], a position of the indicator vector.
1351. $j$
   - on `phase-twist`: $j$ (record position): The position of a coefficient in a record, counted from 0 to r-1; on this page it replaces the convolution's input index.
   - on [Cyclic convolution](cyclic-convolution.md): $j$ (summand position): The position in $f$ of each summand of an output entry, so it indexes $f$ here.
1352. $j$
   - on `phase-twist`: $j$ (record position): The position of a coefficient in a record, counted from 0 to r-1; on this page it replaces the convolution's input index.
   - on [Modular inverse](modular-inverse.md): $j$ (axis index in products): An axis index that runs over the axes before a given axis in a product.
1353. $j$
   - on `phase-twist`: $j$ (record position): The position of a coefficient in a record, counted from 0 to r-1; on this page it replaces the convolution's input index.
   - on [Integer](integer.md): $j$ (digit position): The position of a digit or bit, counted from the left starting at 1.
1354. $j$
   - on `phase-twist`: $j$ (record position): The position of a coefficient in a record, counted from 0 to r-1; on this page it replaces the convolution's input index.
   - on [Linear algebra basics](linear-algebra-basics.md): $j$ (coordinate index): The index of a coordinate of a vector, running from 1 to m.
1355. $j$
   - on `phase-twist`: $j$ (record position): The position of a coefficient in a record, counted from 0 to r-1; on this page it replaces the convolution's input index.
   - on [Convolution](convolution.md): $j$ (input position in b): The position of an entry of $b$.
1356. $j$
   - on `phase-twist`: $j$ (record position): The position of a coefficient in a record, counted from 0 to r-1; on this page it replaces the convolution's input index.
   - on [Ceiling function](ceiling-function.md): $j$ (integer): Any integer, which is its own ceiling.
1357. $j$
   - on `phase-twist`: $j$ (record position): The position of a coefficient in a record, counted from 0 to r-1; on this page it replaces the convolution's input index.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $j$ (entry index): The index that numbers the entries of a list, running from $0$ to $N-1$.
1358. $j$
   - on `phase-twist`: $j$ (record position): The position of a coefficient in a record, counted from 0 to r-1; on this page it replaces the convolution's input index.
   - on [Mixed-radix digits](mixed-radix-digits.md): $j$ (place index): A place, numbered from 1 to beta.
1359. $j$
   - on `phase-twist`: $j$ (record position): The position of a coefficient in a record, counted from 0 to r-1; on this page it replaces the convolution's input index.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $j$ (input index): The index of an input value in the transform $F_q$.
1360. $j$
   - on `phase-twist`: $j$ (record position): The position of a coefficient in a record, counted from 0 to r-1; on this page it replaces the convolution's input index.
   - on [Address-field interchange](address-interchange.md): $j$ (level index): The level of a call, so a call on width $m^j$ sits at level $j$.
1361. $b$
   - on `prime-source-lengths`: $b$ (bit length): The number of binary digits of $n$, $b=\lceil\log_2 n\rceil$.
   - on [Convolution](convolution.md): $b$ (second input sequence): The second of the two input sequences, of length $n$.
1362. $b$
   - on `prime-source-lengths`: $b$ (bit length): The number of binary digits of $n$, $b=\lceil\log_2 n\rceil$.
   - on [Radix-digit convolution](radix-digit-convolution.md): $b$ (digit width): The number of bits in each digit of an input.
1363. $b$
   - on `prime-source-lengths`: $b$ (bit length): The number of binary digits of $n$, $b=\lceil\log_2 n\rceil$.
   - on [Integer](integer.md): $b$ (base): The base (radix) of a digit representation, an integer at least 2.
1364. $b$
   - on `prime-source-lengths`: $b$ (bit length): The number of binary digits of $n$, $b=\lceil\log_2 n\rceil$.
   - on [Logarithm](logarithm.md): $b$ (base): The fixed base of the logarithm, a number greater than 1.
1365. $b$
   - on `prime-source-lengths`: $b$ (bit length): The number of binary digits of $n$, $b=\lceil\log_2 n\rceil$.
   - on [Extended real numbers](extended-reals.md): $b$ (least real bound): The least real upper bound of $R$, which is the supremum of $S$ in that case.
1366. $b$
   - on `prime-source-lengths`: $b$ (bit length): The number of binary digits of $n$, $b=\lceil\log_2 n\rceil$.
   - on [Chinese-remainder map](chinese-remainder-map.md): $b$ (second exponent): The larger of two exponents of $\Phi(x)$ compared for equality, an integer with $a<b<\Lambda$.
1367. $T$
   - on `prime-source-lengths`: $T$ (padded box size): The number of cells of the padded box, the product of the axis lengths.
   - on [Cyclic coordinate](cyclic-coordinate.md): $T$ (box size): The number of entries of the padded box, a power of two; on this page only, not the three-element subsets of other pages.
1368. $T$
   - on `prime-source-lengths`: $T$ (padded box size): The number of cells of the padded box, the product of the axis lengths.
   - on [Linear algebra basics](linear-algebra-basics.md): $T$ (linear map): A linear map between vector spaces over F.
1369. $T$
   - on `prime-source-lengths`: $T$ (padded box size): The number of cells of the padded box, the product of the axis lengths.
   - on [Symmetric matrix](symmetric-matrix.md): $T$ (three-element subset): A three-element subset of a finite set, the second triple compared with $S$.
1370. $T$
   - on `prime-source-lengths`: $T$ (padded box size): The number of cells of the padded box, the product of the axis lengths.
   - on [Bilinear form](bilinear-form.md): $T$ (triple): A three-element subset of [h], one of the triples whose indicator vectors are used.
1371. $T$
   - on `prime-source-lengths`: $T$ (padded box size): The number of cells of the padded box, the product of the axis lengths.
   - on [Indicator vector](indicator-vector.md): $T$ (triple): A single three-element subset of [h]; on the ground-set page T names all triples.
1372. $i$
   - on `prime-source-lengths`: $i$ (axis index): The index of an axis, running from 1 to $d$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $i$ (imaginary unit): The imaginary unit, the complex number whose square is $-1$, used in this page in place of the convolution page's input position $i$.
1373. $i$
   - on `prime-source-lengths`: $i$ (axis index): The index of an axis, running from 1 to $d$.
   - on [Linear algebra basics](linear-algebra-basics.md): $i$ (row index): The index of a row of a matrix, running from 1 to m.
1374. $i$
   - on `prime-source-lengths`: $i$ (axis index): The index of an axis, running from 1 to $d$.
   - on [Convolution](convolution.md): $i$ (input position in a): The position of an entry of $a$.
1375. $i$
   - on `prime-source-lengths`: $i$ (axis index): The index of an axis, running from 1 to $d$.
   - on [Mixed-radix digits](mixed-radix-digits.md): $i$ (lower place index): A place index that runs over the places below j in the sums of the proof.
1376. $i$
   - on `prime-source-lengths`: $i$ (axis index): The index of an axis, running from 1 to $d$.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $i$ (bit position): A bit position of a residue, an integer from 0 to $\sigma-1$.
1377. $u$
   - on `prime-source-lengths`: $u$ (longest axis length): The common length of the longest axes, a power of two, $u=2^\ell$.
   - on [Linear algebra basics](linear-algebra-basics.md): $u$ (vertex): A vertex of the paper's directed graph.
1378. $u$
   - on `prime-source-lengths`: $u$ (longest axis length): The common length of the longest axes, a power of two, $u=2^\ell$.
   - on [Array norm](array-norm.md): $u$ (entry): An entry of the array X, whose modulus is taken.
1379. $w$
   - on `prime-source-lengths`: $w$ (short axis count): The number of axes whose length is $u/2$.
   - on [Stable radix sort](stable-radix-sort.md): $w$ (key width): The number of bits in each key, a count of bits, which is also the number of passes.
1380. $w$
   - on `prime-source-lengths`: $w$ (short axis count): The number of axes whose length is $u/2$.
   - on [Truncation](truncation.md): $w$ (coefficient list): A finite list of complex numbers, called coefficients.
1381. $w$
   - on `prime-source-lengths`: $w$ (short axis count): The number of axes whose length is $u/2$.
   - on [Diagonal scaling](diagonal-scaling.md): $w$ (selected bit count): The number of selected bits of an address, the count of bits that the layer acts on.
1382. $w$
   - on `prime-source-lengths`: $w$ (short axis count): The number of axes whose length is $u/2$.
   - on [Cyclic convolution](cyclic-convolution.md): $w$ (formal variable): The formal variable in which the sequence $f$ is written as a polynomial.
1383. $p$
   - on `prime-source-lengths`: $p$ (working precision): The working precision in bits, $p=6b$.
   - on [Truncation](truncation.md): $p$ (precision): The number of fractional binary places kept, which counts the binary digits after the point.
1384. $\eta$
   - on `prime-source-lengths`: $\eta$ (slack fraction): The slack fraction of the prime-interval bound, $\eta=1/(4d)$ on this page.
   - on [Prime number](prime-number.md): $\eta$ (cofactor): The integer that multiplies the divisor to give the integer being divided.
1385. $\eta$
   - on `prime-source-lengths`: $\eta$ (slack fraction): The slack fraction of the prime-interval bound, $\eta=1/(4d)$ on this page.
   - on [Linear algebra basics](linear-algebra-basics.md): $\eta$ (scalar): A scalar in F multiplying a vector.
1386. $\eta$
   - on `prime-source-lengths`: $\eta$ (slack fraction): The slack fraction of the prime-interval bound, $\eta=1/(4d)$ on this page.
   - on [Transform round](transform-round.md): $\eta$ (twiddle exponent): The exponent of y at an address, so that the round multiplies each record by y to the power eta.
1387. $\eta$
   - on `prime-source-lengths`: $\eta$ (slack fraction): The slack fraction of the prime-interval bound, $\eta=1/(4d)$ on this page.
   - on [Congruence](congruence-modulo.md): $\eta$ (second multiple): The integer with $e'-e=\eta B$.
1388. $\eta$
   - on `prime-source-lengths`: $\eta$ (slack fraction): The slack fraction of the prime-interval bound, $\eta=1/(4d)$ on this page.
   - on [Subset-intersection network](subset-intersection-network.md): $\eta$ (target vector): The vector, indexed by triples, of the entries of the target bank along the varying coordinate.
1389. $\eta$
   - on `prime-source-lengths`: $\eta$ (slack fraction): The slack fraction of the prime-interval bound, $\eta=1/(4d)$ on this page.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\eta$ (half-size): The number of positions in each half of a block at a level of the transform.
1390. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Prime number](prime-number.md): $\xi$ (divisor): A positive integer that divides another integer.
1391. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Radix-digit convolution](radix-digit-convolution.md): $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
1392. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Butterfly](butterfly.md): $\xi$ (first input value): The first of the two input values of the butterfly.
1393. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Permutation](permutation.md): $\xi$ (address): The position of one entry of an array.
1394. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
1395. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
1396. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Neumann series](neumann-series.md): $\xi$ (term index): The index numbering the terms of the series, a nonnegative integer.
1397. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Ring](ring.md): $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
1398. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
1399. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Congruence](congruence-modulo.md): $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
1400. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Cyclic group](cyclic-group.md): $\xi$ (exponent): An integer to which the generator is raised, giving the power $\rho^\xi$.
1401. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Coprime](coprime.md): $\xi$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the first of the two Bezout coefficients.
1402. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Tensor product](tensor-product.md): $\xi$ (row index): A row index of $P$, and in an address the output bit string $\xi$.
1403. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Subset-intersection network](subset-intersection-network.md): $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
1404. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Bilinear map](bilinear-map.md): $\xi$ (first argument): An arbitrary element of the first argument space $U$.
1405. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
1406. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Frequency domain](frequency-domain.md): $\xi$ (binary digit count): The number of binary digits of an index, so that the transform length is $q=2^{\xi}$; it counts digits.
1407. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Modular inverse](modular-inverse.md): $\xi$ (group generator): A generator of the cyclic group of order S.
1408. $\xi$
   - on `prime-source-lengths`: $\xi$ (real scale): The real point at which the prime-interval bound is applied.
   - on [Bézout's identity](bezout-identity.md): $\xi$ (least positive combination): The least positive value of βρ'+γσ' over all integers ρ' and σ'.
1409. $m$
   - on `recovery-and-error`: $m$ (nearest integer): The integer nearest to a computed value that lies within $1/2$ of it.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
1410. $m$
   - on `recovery-and-error`: $m$ (nearest integer): The integer nearest to a computed value that lies within $1/2$ of it.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
1411. $m$
   - on `recovery-and-error`: $m$ (nearest integer): The integer nearest to a computed value that lies within $1/2$ of it.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
1412. $m$
   - on `recovery-and-error`: $m$ (nearest integer): The integer nearest to a computed value that lies within $1/2$ of it.
   - on [Normalization scales](normalization-scales.md): $m$ (digit count): The number of digits of each input, which is also the number of entries of each digit array.
1413. $m$
   - on `recovery-and-error`: $m$ (nearest integer): The integer nearest to a computed value that lies within $1/2$ of it.
   - on [Normalized cyclic convolution](normalized-cyclic-convolution.md): $m$ (chirp argument): A free integer at which the chirp phase $\chi_m$ is evaluated; this letter changes meaning here and is not the order of a root.
1414. $m$
   - on `recovery-and-error`: $m$ (nearest integer): The integer nearest to a computed value that lies within $1/2$ of it.
   - on [Address-field interchange](address-interchange.md): $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
1415. $m$
   - on `recovery-and-error`: $m$ (nearest integer): The integer nearest to a computed value that lies within $1/2$ of it.
   - on [Limit inferior](limit-inferior.md): $m$ (tail start): The position from which a tail of the sequence starts.
1416. $m$
   - on `recovery-and-error`: $m$ (nearest integer): The integer nearest to a computed value that lies within $1/2$ of it.
   - on [Opposite transform](opposite-transform.md): $m$ (summation index): A dummy summation index running from $0$ to $q-1$ that names an input position of a vector; it counts nothing.
1417. $m$
   - on `recovery-and-error`: $m$ (nearest integer): The integer nearest to a computed value that lies within $1/2$ of it.
   - on [Guard-width bound](guard-width-bound.md): $m$ (splitting factor): The factor by which a call divides the axis count.
1418. $m$
   - on `recovery-and-error`: $m$ (nearest integer): The integer nearest to a computed value that lies within $1/2$ of it.
   - on [Polynomial ring](polynomial-ring.md): $m$ (coefficient count): The number of coefficients in each representative, which is the degree of f.
1419. $\mathcal{B}$
   - on `recovery-and-error`: $\mathcal{B}$ (bilinear map): The bilinear map whose approximate products are bounded.
   - on [Transform round](transform-round.md): $\mathcal{B}$ (parallel butterfly): The operator that applies H_0 on every participating axis.
1420. $\gamma$
   - on `recovery-and-error`: $\gamma$ (construction constant): The construction constant of the source, $2d\alpha^2$.
   - on [Permutation](permutation.md): $\gamma$ (third entry): The entry of the sequence at position 3.
1421. $\gamma$
   - on `recovery-and-error`: $\gamma$ (construction constant): The construction constant of the source, $2d\alpha^2$.
   - on [Linear algebra basics](linear-algebra-basics.md): $\gamma$ (scalar): A scalar in F multiplying a vector.
1422. $\gamma$
   - on `recovery-and-error`: $\gamma$ (construction constant): The construction constant of the source, $2d\alpha^2$.
   - on [Coprime](coprime.md): $\gamma$ (first integer): One of two integers, not both zero, whose gcd is taken.
1423. $\gamma$
   - on `recovery-and-error`: $\gamma$ (construction constant): The construction constant of the source, $2d\alpha^2$.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\gamma$ (block offset): The position within a block at which a butterfly pair starts.
1424. $d$
   - on `recovery-and-error`: $d$ (number of axes): The number of axes of the padded box, equal to $\lfloor b^{\epsilon}\rfloor$.
   - on [Address](address.md): $d$ (address length): The number of bits in each address of the array, the length of every address string.
1425. $d$
   - on `recovery-and-error`: $d$ (number of axes): The number of axes of the padded box, equal to $\lfloor b^{\epsilon}\rfloor$.
   - on [Congruence](congruence-modulo.md): $d$ (integer): An integer compared with $e$ modulo $B$.
1426. $d$
   - on `recovery-and-error`: $d$ (number of axes): The number of axes of the padded box, equal to $\lfloor b^{\epsilon}\rfloor$.
   - on [Tape procedure](tape-procedure.md): $d$ (chunk count bound): An upper bound on the number of equal-width address chunks whose selected bits one pass handles.
1427. $d$
   - on `recovery-and-error`: $d$ (number of axes): The number of axes of the padded box, equal to $\lfloor b^{\epsilon}\rfloor$.
   - on [Cyclic convolution](cyclic-convolution.md): $d$ (axis count): The number of axes in the split, that is, the number of factors $n_1, \dots, n_d$ of the length n.
1428. $d$
   - on `recovery-and-error`: $d$ (number of axes): The number of axes of the padded box, equal to $\lfloor b^{\epsilon}\rfloor$.
   - on [Guard-width bound](guard-width-bound.md): $d$ (axis bound): A bound on the number D of selected bits in a layer, so that D is at most d.
1429. $d$
   - on `recovery-and-error`: $d$ (number of axes): The number of axes of the padded box, equal to $\lfloor b^{\epsilon}\rfloor$.
   - on [Cost table](cost-table.md): $d$ (axis count): The number of axes of the padded box.
1430. $\alpha$
   - on `recovery-and-error`: $\alpha$ (construction factor): The ceiling of $(12d^2b)^{1/4}$, the parameter $\alpha$ in the constant $\gamma$.
   - on [Permutation](permutation.md): $\alpha$ (first entry): The entry of the sequence at position 1.
1431. $\alpha$
   - on `recovery-and-error`: $\alpha$ (construction factor): The ceiling of $(12d^2b)^{1/4}$, the parameter $\alpha$ in the constant $\gamma$.
   - on [Address](address.md): $\alpha$ (address string): A binary string of $d$ bits that labels one entry of the array.
1432. $\alpha$
   - on `recovery-and-error`: $\alpha$ (construction factor): The ceiling of $(12d^2b)^{1/4}$, the parameter $\alpha$ in the constant $\gamma$.
   - on [Neumann series](neumann-series.md): $\alpha$ (construction parameter): A parameter of the paper's construction, not the address letter of earlier pages.
1433. $\alpha$
   - on `recovery-and-error`: $\alpha$ (construction factor): The ceiling of $(12d^2b)^{1/4}$, the parameter $\alpha$ in the constant $\gamma$.
   - on [Ring homomorphism and isomorphism](ring-homomorphism.md): $\alpha$ (constant coefficient): The constant coefficient of an element alpha + beta t of W.
1434. $\alpha$
   - on `recovery-and-error`: $\alpha$ (construction factor): The ceiling of $(12d^2b)^{1/4}$, the parameter $\alpha$ in the constant $\gamma$.
   - on [Cost table](cost-table.md): $\alpha$ (line-map factor): The factor that scales the cost of the line maps.
1435. $\varpi$
   - on `recovery-and-error`: $\varpi$ (normalized digit convolution): The convolution of the two scaled digit arrays divided by $S$.
   - on [Multidimensional transform](multidimensional-transform.md): $\varpi$ (output position): A tuple of D coordinates labelling one position in the output array Y.
1436. $\varpi$
   - on `recovery-and-error`: $\varpi$ (normalized digit convolution): The convolution of the two scaled digit arrays divided by $S$.
   - on [Subspace labels](subspace-labels.md): $\varpi$ (identity coefficient): The coefficient of the identity in a translation kernel.
1437. $w$
   - on `recovery-and-error`: $w$ (paper's digit convolution): The paper's name for the normalized digit convolution $\varpi$.
   - on [Stable radix sort](stable-radix-sort.md): $w$ (key width): The number of bits in each key, a count of bits, which is also the number of passes.
1438. $w$
   - on `recovery-and-error`: $w$ (paper's digit convolution): The paper's name for the normalized digit convolution $\varpi$.
   - on [Truncation](truncation.md): $w$ (coefficient list): A finite list of complex numbers, called coefficients.
1439. $w$
   - on `recovery-and-error`: $w$ (paper's digit convolution): The paper's name for the normalized digit convolution $\varpi$.
   - on [Diagonal scaling](diagonal-scaling.md): $w$ (selected bit count): The number of selected bits of an address, the count of bits that the layer acts on.
1440. $w$
   - on `recovery-and-error`: $w$ (paper's digit convolution): The paper's name for the normalized digit convolution $\varpi$.
   - on [Cyclic convolution](cyclic-convolution.md): $w$ (formal variable): The formal variable in which the sequence $f$ is written as a polynomial.
1441. $w$
   - on `recovery-and-error`: $w$ (paper's digit convolution): The paper's name for the normalized digit convolution $\varpi$.
   - on [Prime source lengths](prime-source-lengths.md): $w$ (short axis count): The number of axes whose length is $u/2$.
1442. $h$
   - on `bit-construction`: $h$ (ground set size): The number of elements in the ground set $[h]$, which is 100 here.
   - on [Transform round](transform-round.md): $h$ (highest unprocessed bit): The position of the highest unprocessed address bit on axis i, which receives the branch bit.
1443. $h$
   - on `bit-construction`: $h$ (ground set size): The number of elements in the ground set $[h]$, which is 100 here.
   - on [Linear networks and frames](linear-network-frames.md): $h$ (route position): The position of a vertex along a route, running from $0$ to $L$.
1444. $h$
   - on `bit-construction`: $h$ (ground set size): The number of elements in the ground set $[h]$, which is 100 here.
   - on [Big-Theta notation](big-theta-notation.md): $h$ (comparison function): The function from input sizes to nonnegative reals against which $f$ is compared.
1445. $h$
   - on `bit-construction`: $h$ (ground set size): The number of elements in the ground set $[h]$, which is 100 here.
   - on [Eigenvalue](eigenvalue.md): $h$ (coordinate count): The number of coordinates of each vector in Q^h, at least 2.
1446. $h$
   - on `bit-construction`: $h$ (ground set size): The number of elements in the ground set $[h]$, which is 100 here.
   - on [Array norm](array-norm.md): $h$ (ring element): An element of the ring modulo y^r+1, written as a polynomial in y.
1447. $S$
   - on `bit-construction`: $S$ (triple): A member of $\mathcal K$, that is, a three-element subset of $[h]$.
   - on [Linear algebra basics](linear-algebra-basics.md): $S$ (inverse map): A linear map that inverts an invertible operator T.
1448. $S$
   - on `bit-construction`: $S$ (triple): A member of $\mathcal K$, that is, a three-element subset of $[h]$.
   - on [Symmetric matrix](symmetric-matrix.md): $S$ (three-element subset): A three-element subset of a finite set, one of the two triples compared for neighbourhood.
1449. $S$
   - on `bit-construction`: $S$ (triple): A member of $\mathcal K$, that is, a three-element subset of $[h]$.
   - on [Bilinear form](bilinear-form.md): $S$ (second triple): A second three-element subset of [h], whose indicator vector is t_S.
1450. $S$
   - on `bit-construction`: $S$ (triple): A member of $\mathcal K$, that is, a three-element subset of $[h]$.
   - on [Extended real numbers](extended-reals.md): $S$ (set of extended reals): Any set of extended real numbers, whose infimum and supremum are taken.
1451. $T$
   - on `bit-construction`: $T$ (triple): A member of $\mathcal K$, that is, a three-element subset of $[h]$.
   - on [Linear algebra basics](linear-algebra-basics.md): $T$ (linear map): A linear map between vector spaces over F.
1452. $T$
   - on `bit-construction`: $T$ (triple): A member of $\mathcal K$, that is, a three-element subset of $[h]$.
   - on [Symmetric matrix](symmetric-matrix.md): $T$ (three-element subset): A three-element subset of a finite set, the second triple compared with $S$.
1453. $X$
   - on `bit-construction`: $X$ (source bank): The bank of scalars with one entry $\xi_T$ per triple, which the invocation reads.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $X$ (bit-flip matrix): The $2\times2$ matrix that swaps the two basis states of one bit.
1454. $X$
   - on `bit-construction`: $X$ (source bank): The bank of scalars with one entry $\xi_T$ per triple, which the invocation reads.
   - on [Two-point kernel](two-point-kernel.md): $X$ (bit flip): The 2 by 2 matrix that interchanges the two entries of a pair.
1455. $X$
   - on `bit-construction`: $X$ (source bank): The bank of scalars with one entry $\xi_T$ per triple, which the invocation reads.
   - on [Array norm](array-norm.md): $X$ (array): A finite array of complex values, whose norm is taken.
1456. $X$
   - on `bit-construction`: $X$ (source bank): The bank of scalars with one entry $\xi_T$ per triple, which the invocation reads.
   - on [Orthogonal complement](orthogonal-complement.md): $X$ (vector space): A vector space over $F$ on which the bilinear form is defined.
1457. $Y$
   - on `bit-construction`: $Y$ (target bank): The bank of scalars with one entry $\eta_S$ per triple, which the invocation updates.
   - on [Coprime](coprime.md): $Y$ (common multiple): An integer that both gamma and rho divide, or that every member of the family divides.
1458. $Y$
   - on `bit-construction`: $Y$ (target bank): The bank of scalars with one entry $\eta_S$ per triple, which the invocation updates.
   - on [Tensor product](tensor-product.md): $Y$ (row index of Q'): A row index of $Q'$, summed over as a middle index of $Q$ and $Q'$.
1459. $Y$
   - on `bit-construction`: $Y$ (target bank): The bank of scalars with one entry $\eta_S$ per triple, which the invocation updates.
   - on [Projection along a subspace](projection-along-subspace.md): $Y$ (complementary subspace): A subspace of $W$ meeting $U$ only in $0$ and with $U$ spanning $W$ together with it.
1460. $Y$
   - on `bit-construction`: $Y$ (target bank): The bank of scalars with one entry $\eta_S$ per triple, which the invocation updates.
   - on [Multidimensional transform](multidimensional-transform.md): $Y$ (output array): The array of values that the multidimensional transform produces from X.
1461. $N$
   - on `complex-construction`: $N$ (bank entry count): The number of entries in each data bank, v^3.
   - on [Address](address.md): $N$ (entry count): The number of entries in the array, counting each stored entry once; it counts the positions $0$ through $N-1$.
1462. $I$
   - on `complex-construction`: $I$ (invocation count): The number of invocations, 3v^2.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $I$ (identity matrix): The $2\times2$ identity matrix.
1463. $I$
   - on `complex-construction`: $I$ (invocation count): The number of invocations, 3v^2.
   - on [Linear algebra basics](linear-algebra-basics.md): $I$ (identity matrix): The square matrix with ones on the diagonal and zeros elsewhere.
1464. $v$
   - on `complex-construction`: $v$ (triple count): The number of triples, the binomial coefficient of h choose 3.
   - on [Linear algebra basics](linear-algebra-basics.md): $v$ (vertex): A vertex of the paper's directed graph.
1465. $v$
   - on `complex-construction`: $v$ (triple count): The number of triples, the binomial coefficient of h choose 3.
   - on [Binary change of basis](binary-change-of-basis.md): $v$ (direction vector): A vector of $\mathbb F_2^m$ in a residual basis; $v_j$ is its $j$-th member.
1466. $m$
   - on `complex-construction`: $m$ (label dimension): The dimension of the label space, h^3.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
1467. $m$
   - on `complex-construction`: $m$ (label dimension): The dimension of the label space, h^3.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
1468. $m$
   - on `complex-construction`: $m$ (label dimension): The dimension of the label space, h^3.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
1469. $m$
   - on `complex-construction`: $m$ (label dimension): The dimension of the label space, h^3.
   - on [Address-field interchange](address-interchange.md): $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
1470. $m$
   - on `complex-construction`: $m$ (label dimension): The dimension of the label space, h^3.
   - on [Limit inferior](limit-inferior.md): $m$ (tail start): The position from which a tail of the sequence starts.
1471. $s$
   - on `rank-saving-recursion`: $s$ (smaller-call count): The total number of smaller calls that one call makes.
   - on [Ceiling function](ceiling-function.md): $s$ (real number): The real number that the ceiling rounds up to an integer.
1472. $s$
   - on `rank-saving-recursion`: $s$ (smaller-call count): The total number of smaller calls that one call makes.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $s$ (input index): An integer index running over $0, 1, \ldots, q-1$ that labels an input coordinate $f_s$.
1473. $s$
   - on `rank-saving-recursion`: $s$ (smaller-call count): The total number of smaller calls that one call makes.
   - on [Array norm](array-norm.md): $s$ (coefficient index): The index of a coefficient of a ring element, running from 0 to r-1.
1474. $s$
   - on `rank-saving-recursion`: $s$ (smaller-call count): The total number of smaller calls that one call makes.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $s$ (number of H_0 factors): The number of individual factors $H_0$ applied, which refines the grid to $2^{-(p+s)}$.
1475. $s$
   - on `rank-saving-recursion`: $s$ (smaller-call count): The total number of smaller calls that one call makes.
   - on [Transform axis](transform-axis.md): $s$ (coefficient count): A power of two that is the number of coefficients of the stored polynomial, which is also the length of its axis.
1476. $s$
   - on `rank-saving-recursion`: $s$ (smaller-call count): The total number of smaller calls that one call makes.
   - on [Truncation](truncation.md): $s$ (first pair value): The first of the two values in a pair that a layer combines.
1477. $s$
   - on `rank-saving-recursion`: $s$ (smaller-call count): The total number of smaller calls that one call makes.
   - on [Address-field interchange](address-interchange.md): $s$ (smaller calls): The number of smaller calls one call makes, equal to the sum of the edge ranks.
1478. $s$
   - on `rank-saving-recursion`: $s$ (smaller-call count): The total number of smaller calls that one call makes.
   - on [Subspace labels](subspace-labels.md): $s$ (basis index): An index numbering the basis vectors of an edge residual.
1479. $s$
   - on `rank-saving-recursion`: $s$ (smaller-call count): The total number of smaller calls that one call makes.
   - on [Mixed-radix digits](mixed-radix-digits.md): $s$ (common length): The common length of every place, which is also the base; it counts the digit values.
1480. $s$
   - on `rank-saving-recursion`: $s$ (smaller-call count): The total number of smaller calls that one call makes.
   - on [Telescoping identity](telescoping-identity.md): $s$ (first position): The first position of a sum over positions, the lower limit of the sum.
1481. $W$
   - on `rank-saving-recursion`: $W$ (wire count): The number of wires of the network, which is also the number of roles.
   - on [Bit network](bit-network.md): $W$ (source bank): The bank of source bits, holding one bit $W_\sigma$ for each triple $\sigma$.
1482. $W$
   - on `rank-saving-recursion`: $W$ (wire count): The number of wires of the network, which is also the number of roles.
   - on [Permutation](permutation.md): $W$ (position set): The finite set of positions on which a permutation acts.
1483. $W$
   - on `rank-saving-recursion`: $W$ (wire count): The number of wires of the network, which is also the number of roles.
   - on [Bijection](bijection.md): $W$ (target set): The set that the map $f$ sends its inputs into, the set of outputs.
1484. $W$
   - on `rank-saving-recursion`: $W$ (wire count): The number of wires of the network, which is also the number of roles.
   - on [Bilinear map](bilinear-map.md): $W$ (output space): The vector space that the bilinear map returns its values in.
1485. $W$
   - on `rank-saving-recursion`: $W$ (wire count): The number of wires of the network, which is also the number of roles.
   - on [Cyclic group](cyclic-group.md): $W$ (cyclic group order): The number of elements of the cyclic group $C_W$, which counts its distinct powers of the generator.
1486. $W$
   - on `rank-saving-recursion`: $W$ (wire count): The number of wires of the network, which is also the number of roles.
   - on [Coprime](coprime.md): $W$ (family product): The product f_1 times f_2 up to f_J, which is the least positive integer divisible by every member.
1487. $W$
   - on `rank-saving-recursion`: $W$ (wire count): The number of wires of the network, which is also the number of roles.
   - on [Tensor product](tensor-product.md): $W$ (row index of P'): A row index of $P'$, summed over as a middle index of $P$ and $P'$.
1488. $W$
   - on `rank-saving-recursion`: $W$ (wire count): The number of wires of the network, which is also the number of roles.
   - on [Projection along a subspace](projection-along-subspace.md): $W$ (ambient space): The finite-dimensional vector space over $F$ on which every projection acts.
1489. $W$
   - on `rank-saving-recursion`: $W$ (wire count): The number of wires of the network, which is also the number of roles.
   - on [Orthogonal complement](orthogonal-complement.md): $W$ (larger label): The larger of the two labels on an edge, which contains the smaller label $U$.
1490. $W$
   - on `rank-saving-recursion`: $W$ (wire count): The number of wires of the network, which is also the number of roles.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $W$ (second butterfly entry): The entry of a butterfly pair at position $\gamma+\eta$ of the block.
1491. $m$
   - on `rank-saving-recursion`: $m$ (label dimension): The dimension of the fixed nondegenerate space $F$ that contains every label.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
1492. $m$
   - on `rank-saving-recursion`: $m$ (label dimension): The dimension of the fixed nondegenerate space $F$ that contains every label.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
1493. $m$
   - on `rank-saving-recursion`: $m$ (label dimension): The dimension of the fixed nondegenerate space $F$ that contains every label.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
1494. $m$
   - on `rank-saving-recursion`: $m$ (label dimension): The dimension of the fixed nondegenerate space $F$ that contains every label.
   - on [Address-field interchange](address-interchange.md): $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
1495. $m$
   - on `rank-saving-recursion`: $m$ (label dimension): The dimension of the fixed nondegenerate space $F$ that contains every label.
   - on [Limit inferior](limit-inferior.md): $m$ (tail start): The position from which a tail of the sequence starts.
1496. $m$
   - on `rank-saving-recursion`: $m$ (label dimension): The dimension of the fixed nondegenerate space $F$ that contains every label.
   - on [Numerical layer](numerical-layer.md): $m$ (division factor): The fixed integer by which a call divides its number of selected axes.
1497. $F$
   - on `rank-saving-recursion`: $F$ (nondegenerate space): The fixed space that holds all labels, with no nonzero vector orthogonal to all of it.
   - on [Exceptional set](exceptional-set.md): $F$ (generic formula): The rule that gives a value F(\alpha) for each address \alpha, and is correct outside the exceptional set.
1498. $F$
   - on `rank-saving-recursion`: $F$ (nondegenerate space): The fixed space that holds all labels, with no nonzero vector orthogonal to all of it.
   - on [Linear algebra basics](linear-algebra-basics.md): $F$ (field): The field of scalars over which the vector spaces are taken.
1499. $F$
   - on `rank-saving-recursion`: $F$ (nondegenerate space): The fixed space that holds all labels, with no nonzero vector orthogonal to all of it.
   - on [Extended real numbers](extended-reals.md): $F$ (real elements): The set of real elements of $S$, used to find the supremum of $S$.
1500. $U$
   - on `rank-saving-recursion`: $U$ (label): A nondegenerate subspace of $F$ attached to a vertex.
   - on [Bilinear form](bilinear-form.md): $U$ (subspace): A subspace of E whose orthogonal complement is taken.
1501. $U$
   - on `rank-saving-recursion`: $U$ (label): A nondegenerate subspace of $F$ attached to a vertex.
   - on [Bijection](bijection.md): $U$ (source set): The set of inputs of the map $f$, each of which $f$ sends to an element of $W$.
1502. $U$
   - on `rank-saving-recursion`: $U$ (label): A nondegenerate subspace of $F$ attached to a vertex.
   - on [Bilinear map](bilinear-map.md): $U$ (first argument space): The vector space that the first argument of the bilinear map ranges over.
1503. $U$
   - on `rank-saving-recursion`: $U$ (label): A nondegenerate subspace of $F$ attached to a vertex.
   - on [Dual space](dual-space.md): $U$ (vector space): A vector space over the field F, whose linear functionals form the dual space.
1504. $U$
   - on `rank-saving-recursion`: $U$ (label): A nondegenerate subspace of $F$ attached to a vertex.
   - on [Projection along a subspace](projection-along-subspace.md): $U$ (subspace): A subspace of $W$ onto which a vector is projected.
1505. $U$
   - on `rank-saving-recursion`: $U$ (label): A nondegenerate subspace of $F$ attached to a vertex.
   - on [Complex phase network](complex-phase-network.md): $U$ (tail label): The label at the tail of an edge.
1506. $U$
   - on `rank-saving-recursion`: $U$ (label): A nondegenerate subspace of $F$ attached to a vertex.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $U$ (first butterfly entry): The entry of a butterfly pair at position $\gamma$ of the block.
1507. $V$
   - on `rank-saving-recursion`: $V$ (padded volume): The stored volume of the array after padding, in bits.
   - on [Directed graph](directed-graph.md): $V$ (vertex set): The set of vertices of the directed graph, the points that edges join.
1508. $V$
   - on `rank-saving-recursion`: $V$ (padded volume): The stored volume of the array after padding, in bits.
   - on [Array](array.md): $V$ (stored bit volume): The number of stored data bits in an array, the volume in which cost bounds are stated.
1509. $V$
   - on `rank-saving-recursion`: $V$ (padded volume): The stored volume of the array after padding, in bits.
   - on [Payload](payload.md): $V$ (stream volume): The number of bits stored in the stream, which the time bound counts.
1510. $V$
   - on `rank-saving-recursion`: $V$ (padded volume): The stored volume of the array after padding, in bits.
   - on [Big-Theta notation](big-theta-notation.md): $V$ (stored bit volume): The number of stored bits, which is of order $n$.
1511. $V$
   - on `rank-saving-recursion`: $V$ (padded volume): The stored volume of the array after padding, in bits.
   - on [Cyclic shift](cyclic-shift.md): $V$ (stored bit volume): The number of stored bits in the array, a count of its data bits.
1512. $V$
   - on `rank-saving-recursion`: $V$ (padded volume): The stored volume of the array after padding, in bits.
   - on [Eigenvalue](eigenvalue.md): $V$ (vector space): The vector space on which the linear operator T acts, over the field F.
1513. $V$
   - on `rank-saving-recursion`: $V$ (padded volume): The stored volume of the array after padding, in bits.
   - on [Bilinear map](bilinear-map.md): $V$ (second argument space): The vector space that the second argument of the bilinear map ranges over.
1514. $V$
   - on `rank-saving-recursion`: $V$ (padded volume): The stored volume of the array after padding, in bits.
   - on [Scratch storage](scratch-storage.md): $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
1515. $V$
   - on `rank-saving-recursion`: $V$ (padded volume): The stored volume of the array after padding, in bits.
   - on [Linear functional](linear-functional.md): $V$ (vector space): The vector space over F whose vectors a linear functional takes as input.
1516. $V$
   - on `rank-saving-recursion`: $V$ (padded volume): The stored volume of the array after padding, in bits.
   - on [Projection along a subspace](projection-along-subspace.md): $V$ (larger nested subspace): A nondegenerate subspace containing $U$, the larger of two nested labels.
1517. $V$
   - on `rank-saving-recursion`: $V$ (padded volume): The stored volume of the array after padding, in bits.
   - on [Complex phase network](complex-phase-network.md): $V$ (head label): The label at the head of an edge.
1518. $\mu$
   - on `rank-saving-recursion`: $\mu$ (source dimension sum): The sum of the dimensions of the source labels.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $\mu$ (bit-flip coefficient): The coefficient of $X$ in $C$, equal to $(1-i)/2$.
1519. $e$
   - on `rank-saving-recursion`: $e$ (chunk digit count): The number of digits in each chunk being interchanged.
   - on [Congruence](congruence-modulo.md): $e$ (integer): An integer compared with $d$ modulo $B$.
1520. $e$
   - on `rank-saving-recursion`: $e$ (chunk digit count): The number of digits in each chunk being interchanged.
   - on [Eigenvalue](eigenvalue.md): $e$ (eigenvector): A nonzero vector of V that T maps to a multiple of itself.
1521. $e$
   - on `rank-saving-recursion`: $e$ (chunk digit count): The number of digits in each chunk being interchanged.
   - on [Transform round](transform-round.md): $e$ (quotient): The integer quotient of eta by r: the number of whole multiples of r in eta.
1522. $e$
   - on `rank-saving-recursion`: $e$ (chunk digit count): The number of digits in each chunk being interchanged.
   - on [Two-point kernel](two-point-kernel.md): $e$ (bit position): An index from 0 to d-1 naming the bit along which a kernel acts, counted from the least significant bit.
1523. $e$
   - on `rank-saving-recursion`: $e$ (chunk digit count): The number of digits in each chunk being interchanged.
   - on [Indicator vector](indicator-vector.md): $e$ (position): An element of the ground set [h], a position of the indicator vector.
1524. $e$
   - on `rank-saving-recursion`: $e$ (chunk digit count): The number of digits in each chunk being interchanged.
   - on [Telescoping identity](telescoping-identity.md): $e$ (last position): The last position of a sum over positions, the upper limit of the sum.
1525. $e$
   - on `rank-saving-recursion`: $e$ (chunk digit count): The number of digits in each chunk being interchanged.
   - on [Numerical layer](numerical-layer.md): $e$ (selected axis count): The number of selected axes that a call acts on.
1526. $q$
   - on `rank-saving-recursion`: $q$ (radix): The fixed radix in which the digits are written.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $q$ (transform length): The number of coordinates of each vector the transform acts on, a positive integer.
1527. $q$
   - on `rank-saving-recursion`: $q$ (radix): The fixed radix in which the digits are written.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $q$ (number of values): The number of values that the transform $F_q$ acts on.
1528. $\gamma$
   - on `rank-saving-recursion`: $\gamma$ (linear-work constant): The constant multiplying the stored volume in the linear work of one call.
   - on [Permutation](permutation.md): $\gamma$ (third entry): The entry of the sequence at position 3.
1529. $\gamma$
   - on `rank-saving-recursion`: $\gamma$ (linear-work constant): The constant multiplying the stored volume in the linear work of one call.
   - on [Linear algebra basics](linear-algebra-basics.md): $\gamma$ (scalar): A scalar in F multiplying a vector.
1530. $\gamma$
   - on `rank-saving-recursion`: $\gamma$ (linear-work constant): The constant multiplying the stored volume in the linear work of one call.
   - on [Coprime](coprime.md): $\gamma$ (first integer): One of two integers, not both zero, whose gcd is taken.
1531. $\gamma$
   - on `rank-saving-recursion`: $\gamma$ (linear-work constant): The constant multiplying the stored volume in the linear work of one call.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\gamma$ (block offset): The position within a block at which a butterfly pair starts.
1532. $\tau$
   - on `rank-saving-recursion`: $\tau$ (power-saving exponent): A fixed number in $(0,1)$ that is the exponent of the bound $O(Ve^\tau)$.
   - on [Payload](payload.md): $\tau$ (fixed exponent): A fixed exponent strictly between 0 and 1 that sets the power of L in the time bound.
1533. $\tau$
   - on `rank-saving-recursion`: $\tau$ (power-saving exponent): A fixed number in $(0,1)$ that is the exponent of the bound $O(Ve^\tau)$.
   - on [Address-field interchange](address-interchange.md): $\tau$ (fixed exponent): A fixed number below 1, the exponent in the cost bound $O(Vu^{\tau})$.
1534. $\tau$
   - on `rank-saving-recursion`: $\tau$ (power-saving exponent): A fixed number in $(0,1)$ that is the exponent of the bound $O(Ve^\tau)$.
   - on [Extended real numbers](extended-reals.md): $\tau$ (sequence term): The term of a sequence at position $\delta$.
1535. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Bit network](bit-network.md): $\sigma$ (triple): An element of $T$, a three-element subset of $[h]$.
1536. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Linear networks and frames](linear-network-frames.md): $\sigma$ (output role): An output role of the network.
1537. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Permutation](permutation.md): $\sigma$ (permutation): The map from W to W that sends each position to its new position.
1538. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Bijection](bijection.md): $\sigma$ (source element): An element of the source set $U$, the input of the map $f$.
1539. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Binary change of basis](binary-change-of-basis.md): $\sigma$ (selected bit values): The column $(\sigma_1,\dots,\sigma_m)$ of the values of the $m$ selected bits, each in $\mathbb F_2$.
1540. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Binary field](binary-field.md): $\sigma$ (three-element subset): A three-element subset of the ground set, one of the two whose shared elements give a coefficient.
1541. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Congruence](congruence-modulo.md): $\sigma$ (class member): An integer in the residue class of $d$.
1542. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Butterfly](butterfly.md): $\sigma$ (index bit): The index of one bit of a position, counted from 0 at the least significant end, so a level acts on the pairs that differ in this bit.
1543. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Cyclic shift](cyclic-shift.md): $\sigma$ (offset): The amount of rotation, an integer taken modulo J.
1544. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\sigma$ (dummy index): A second index running over $0, 1, \ldots, q-1$, introduced so that the substituted sum does not reuse $s$.
1545. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\sigma$ (residue bit count): The number of bits in a residue, which sets the modulus $2^\sigma+1$.
1546. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Order of an element](order-of-element.md): $\sigma$ (element): An element of the group G whose powers are taken.
1547. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Cyclic group](cyclic-group.md): $\sigma$ (order of an element): The least positive integer with $\rho^\sigma=1$, which is the order of $\rho$ as a group element.
1548. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Coprime](coprime.md): $\sigma$ (member index): An index running over 1 to J, numbering the family members.
1549. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Gaussian dyadics](gaussian-dyadics.md): $\sigma$ (numerator): The Gaussian integer numerator of a Gaussian dyadic $\sigma/2^{\Gamma}$.
1550. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Tensor product](tensor-product.md): $\sigma$ (column index): A column index of $P$, and in an address the input bit string $\sigma$.
1551. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Subset-intersection network](subset-intersection-network.md): $\sigma$ (triple of triples): A tuple of three triples, which indexes the entries of a bank.
1552. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Dual space](dual-space.md): $\sigma$ (example functional): The linear functional on R^2 sending x to 3x_1 - x_2.
1553. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Line spanned by a vector](line-spanned-by-vector.md): $\sigma$ (triple choice): An ordered choice of three triples, which indexes one label, its vector and its data banks.
1554. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Fixed-tape machine model](fixed-tape-model.md): $\sigma$ (positive constant): A positive constant multiplying $n\log n$ in the lower bound $T_A(n) \geq \sigma\, n\log n$ for machine $A$.
1555. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Extended real numbers](extended-reals.md): $\sigma$ (generic real number): A real number used as a generic value in the order, sums and limit conditions.
1556. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Gram matrix](gram-matrix.md): $\sigma$ (list length): The number of vectors in the list, which is the number of rows and columns of the Gram matrix.
1557. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Multidimensional transform](multidimensional-transform.md): $\sigma$ (axis index): The index of one transform axis, an integer from 1 to D.
1558. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\sigma$ (shift count): The number of places a shift moves each coefficient.
1559. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Radix-two factorization](radix-two-factorization.md): $\sigma$ (half-length output index): The output index of a half-length transform, with $0 \le \sigma < q/2$, so that the full output index is $\ell = 2\sigma + b$.
1560. $\sigma$
   - on `rank-saving-recursion`: $\sigma$ (saving ratio): The ratio $(s/W)m^{-\tau}$, which is below one.
   - on [Iverson bracket](iverson-bracket.md): $\sigma$ (condition): A statement that is either true or false, and whose truth decides whether its bracket is 1 or 0.
1561. $\beta$
   - on `rank-saving-recursion`: $\beta$ (one-digit cost constant): A constant such that one digit's interchange costs at most $\beta V$.
   - on [Permutation](permutation.md): $\beta$ (second entry): The entry of the sequence at position 2.
1562. $\beta$
   - on `rank-saving-recursion`: $\beta$ (one-digit cost constant): A constant such that one digit's interchange costs at most $\beta V$.
   - on [Mixed-radix digits](mixed-radix-digits.md): $\beta$ (place count): The number of places, a positive integer; the places are numbered 1 to beta.
1563. $\theta$
   - on `family-parameter`: $\theta$ (family parameter): A nonnegative integer that indexes the members of the family.
   - on [Eigenvalue](eigenvalue.md): $\theta$ (eigenvalue): A scalar for which T maps some nonzero vector e to the multiple theta e.
1564. $\theta$
   - on `family-parameter`: $\theta$ (family parameter): A nonnegative integer that indexes the members of the family.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\theta$ (twiddle): The power of $\omega_N$ by which a butterfly multiplies its second entry.
1565. $\mathcal{X}$
   - on `packed-bit-addition`: $\mathcal{X}$ (source field): The field whose selected bits are XORed into the target field.
   - on [Union bound](union-bound.md): $\mathcal{X}$ (finite set): A generic finite set, whose elements are counted by |X|.
1566. $\mathcal{X}$
   - on `packed-bit-addition`: $\mathcal{X}$ (source field): The field whose selected bits are XORed into the target field.
   - on [Gaussian resampling](gaussian-resampling.md): $\mathcal{X}$ (deviation from identity): The difference $I-\mathcal N$, whose norm is below one half.
1567. $\mathcal{W}$
   - on `packed-bit-addition`: $\mathcal{W}$ (target field): The field that receives the XOR of the selected bits of the source.
   - on [Subspace labels](subspace-labels.md): $\mathcal{W}$ (Hadamard matrix): The Hadamard matrix of order 2, which satisfies W^2 = I.
1568. $\mathcal{W}$
   - on `packed-bit-addition`: $\mathcal{W}$ (target field): The field that receives the XOR of the selected bits of the source.
   - on [Independence of events](independence.md): $\mathcal{W}$ (sample space): The finite set of possible outcomes of an experiment.
1569. $L$
   - on `packed-bit-addition`: $L$ (field width): The number of address bits in each field, $fK$.
   - on [Linear networks and frames](linear-network-frames.md): $L$ (route length): The number of edges on a route, so that the route has $L+1$ vertices.
1570. $L$
   - on `packed-bit-addition`: $L$ (field width): The number of address bits in each field, $fK$.
   - on [Payload](payload.md): $L$ (chunk width): The width, in address bits, of an address chunk.
1571. $L$
   - on `packed-bit-addition`: $L$ (field width): The number of address bits in each field, $fK$.
   - on [Extended real numbers](extended-reals.md): $L$ (candidate limit): A point of $\overline{\mathbb{R}}$ that a sequence may have as its limit.
1572. $L$
   - on `packed-bit-addition`: $L$ (field width): The number of address bits in each field, $fK$.
   - on [Linear contraction](linear-contraction.md): $L$ (linear map): A linear map from vectors in C^m to vectors in C^{m'} whose contraction property is tested.
1573. $L$
   - on `packed-bit-addition`: $L$ (field width): The number of address bits in each field, $fK$.
   - on [Supremum](supremum.md): $L$ (linear map): A linear map, meaning a map that preserves sums and scalar multiples, whose operator norm is taken.
1574. $L$
   - on `packed-bit-addition`: $L$ (field width): The number of address bits in each field, $fK$.
   - on [Logical array](logical-array.md): $L$ (route length): The number of edges on a route, so the route has $L+1$ vertices.
1575. $\rho$
   - on `packed-bit-addition`: $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
   - on [Linear networks and frames](linear-network-frames.md): $\rho$ (role permutation): The permutation of roles that sends each input role to an output role.
1576. $\rho$
   - on `packed-bit-addition`: $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
   - on [Address field](address-field.md): $\rho$ (field width): The number of bits in each of the two fields being interchanged, a count of bit positions.
1577. $\rho$
   - on `packed-bit-addition`: $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
   - on [Binary change of basis](binary-change-of-basis.md): $\rho$ (residual dimension): The number of vectors in a residual basis, which counts the dimension of the edge's residual.
1578. $\rho$
   - on `packed-bit-addition`: $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\rho$ (exponent): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
1579. $\rho$
   - on `packed-bit-addition`: $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
   - on [Order of an element](order-of-element.md): $\rho$ (order): The least positive integer with sigma to the power rho equal to 1; it counts the distinct powers of sigma.
1580. $\rho$
   - on `packed-bit-addition`: $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
   - on [Cyclic group](cyclic-group.md): $\rho$ (generator): An element of a group, the base of its powers; when its powers are all the elements, it is the generator.
1581. $\rho$
   - on `packed-bit-addition`: $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
   - on [Coprime](coprime.md): $\rho$ (second integer): The other of two integers, not both zero, whose gcd is taken.
1582. $\rho$
   - on `packed-bit-addition`: $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
   - on [Dual space](dual-space.md): $\rho$ (second example functional): The linear functional on R^2 sending x to x_1.
1583. $\rho$
   - on `packed-bit-addition`: $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\rho$ (coefficient position): The position of a coefficient in a record, running from 0 to r-1.
1584. $\rho$
   - on `packed-bit-addition`: $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
   - on [Linear contraction](linear-contraction.md): $\rho$ (rounding error): The rounding error introduced at one step of a computation, added to that step's output.
1585. $\rho$
   - on `packed-bit-addition`: $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
   - on [Frequency domain](frequency-domain.md): $\rho$ (second input position): The position of an entry of the second input sequence $b$ in the convolution sum, running from $0$ to $q-1$.
1586. $\rho$
   - on `packed-bit-addition`: $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
   - on [Bézout's identity](bezout-identity.md): $\rho$ (Bézout coefficient of β): The integer multiplying β in the combination βρ+γσ that equals gcd(β,γ).
1587. $i$
   - on `packed-bit-addition`: $i$ (segment index): The number of a segment, running from $0$ to $f-2$.
   - on [Linear algebra basics](linear-algebra-basics.md): $i$ (row index): The index of a row of a matrix, running from 1 to m.
1588. $i$
   - on `packed-bit-addition`: $i$ (segment index): The number of a segment, running from $0$ to $f-2$.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $i$ (imaginary unit): The imaginary unit, the complex number whose square is $-1$, used in this page in place of the convolution page's input position $i$.
1589. $i$
   - on `packed-bit-addition`: $i$ (segment index): The number of a segment, running from $0$ to $f-2$.
   - on [Convolution](convolution.md): $i$ (input position in a): The position of an entry of $a$.
1590. $i$
   - on `packed-bit-addition`: $i$ (segment index): The number of a segment, running from $0$ to $f-2$.
   - on [Transform round](transform-round.md): $i$ (axis index): An index naming one of the participating axes.
1591. $i$
   - on `packed-bit-addition`: $i$ (segment index): The number of a segment, running from $0$ to $f-2$.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $i$ (bit position): A bit position of a residue, an integer from 0 to $\sigma-1$.
1592. $i$
   - on `packed-bit-addition`: $i$ (segment index): The number of a segment, running from $0$ to $f-2$.
   - on [Transform axis](transform-axis.md): $i$ (axis index): An index naming one axis, running from 1 to D.
1593. $i$
   - on `packed-bit-addition`: $i$ (segment index): The number of a segment, running from $0$ to $f-2$.
   - on [Mixed-radix digits](mixed-radix-digits.md): $i$ (lower place index): A place index that runs over the places below j in the sums of the proof.
1594. $i$
   - on `packed-bit-addition`: $i$ (segment index): The number of a segment, running from $0$ to $f-2$.
   - on [Union bound](union-bound.md): $i$ (event index): An index numbering the events, running from 1 to m.
1595. $i$
   - on `packed-bit-addition`: $i$ (segment index): The number of a segment, running from $0$ to $f-2$.
   - on [Modular inverse](modular-inverse.md): $i$ (axis index): The index of an axis, an integer from 1 to d.
1596. $a$
   - on `packed-bit-addition`: $a$ (selected bit): The lowest bit of a segment, which is 0 or 1.
   - on [Convolution](convolution.md): $a$ (first input sequence): The first of the two input sequences, of length $n$.
1597. $a$
   - on `packed-bit-addition`: $a$ (selected bit): The lowest bit of a segment, which is 0 or 1.
   - on [Scratch storage](scratch-storage.md): $a$ (starting side values): The vector of starting values of the side wires.
1598. $a$
   - on `packed-bit-addition`: $a$ (selected bit): The lowest bit of a segment, which is 0 or 1.
   - on [Matrix rank](matrix-rank.md): $a$ (matrix rank): The rank of $A$ over the rationals, the number of linearly independent rows of $A$.
1599. $\gamma$
   - on `packed-bit-addition`: $\gamma$ (guard value): The integer formed by the other $K-1$ bits of a segment.
   - on [Rank-saving recursion](rank-saving-recursion.md): $\gamma$ (linear-work constant): The constant multiplying the stored volume in the linear work of one call.
1600. $\gamma$
   - on `packed-bit-addition`: $\gamma$ (guard value): The integer formed by the other $K-1$ bits of a segment.
   - on [Permutation](permutation.md): $\gamma$ (third entry): The entry of the sequence at position 3.
1601. $\gamma$
   - on `packed-bit-addition`: $\gamma$ (guard value): The integer formed by the other $K-1$ bits of a segment.
   - on [Linear algebra basics](linear-algebra-basics.md): $\gamma$ (scalar): A scalar in F multiplying a vector.
1602. $\gamma$
   - on `packed-bit-addition`: $\gamma$ (guard value): The integer formed by the other $K-1$ bits of a segment.
   - on [Coprime](coprime.md): $\gamma$ (first integer): One of two integers, not both zero, whose gcd is taken.
1603. $\gamma$
   - on `packed-bit-addition`: $\gamma$ (guard value): The integer formed by the other $K-1$ bits of a segment.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\gamma$ (block offset): The position within a block at which a butterfly pair starts.
1604. $\gamma$
   - on `packed-bit-addition`: $\gamma$ (guard value): The integer formed by the other $K-1$ bits of a segment.
   - on [Matrix rank](matrix-rank.md): $\gamma$ (first field value): The value of the field $H_i$ before one update.
1605. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Permutation](permutation.md): $\xi$ (address): The position of one entry of an array.
1606. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Bijection](bijection.md): $\xi$ (target element): An element of the target set $W$, the output that a bijection must hit exactly once.
1607. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Floor function](floor-function.md): $\xi$ (real argument): The real number whose floor is taken.
1608. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Congruence](congruence-modulo.md): $\xi$ (multiple of B): The integer with $d-e=\xi B$, so $\xi B$ is the difference of two congruent integers.
1609. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Radix-digit convolution](radix-digit-convolution.md): $\xi$ (formal variable): A symbol, not a number, that the digit polynomials are written in.
1610. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Butterfly](butterfly.md): $\xi$ (first input value): The first of the two input values of the butterfly.
1611. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Bilinear map](bilinear-map.md): $\xi$ (first argument): An arbitrary element of the first argument space $U$.
1612. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Ring](ring.md): $\xi$ (ring element): An element of the ring $R$, one of the arguments of its addition and multiplication.
1613. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Schönhage–Strassen multiplication](schonhage-strassen.md): $\xi$ (shift count): The number of places a multiplication shifts, with $0\le\xi<\sigma$.
1614. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Cyclic group](cyclic-group.md): $\xi$ (exponent): An integer to which the generator is raised, giving the power $\rho^\xi$.
1615. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Coprime](coprime.md): $\xi$ (Bezout coefficient): An integer with $\gamma\xi+\rho\zeta=1$, the first of the two Bezout coefficients.
1616. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Tensor product](tensor-product.md): $\xi$ (row index): A row index of $P$, and in an address the output bit string $\xi$.
1617. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Subset-intersection network](subset-intersection-network.md): $\xi$ (source vector): The vector, indexed by triples, of the entries of the source bank along the varying coordinate.
1618. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Neumann series](neumann-series.md): $\xi$ (term index): The index numbering the terms of the series, a nonnegative integer.
1619. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $\xi$ (quotient polynomial): The polynomial whose product with $y^r+1$ is the difference of two representatives.
1620. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Frequency domain](frequency-domain.md): $\xi$ (binary digit count): The number of binary digits of an index, so that the transform length is $q=2^{\xi}$; it counts digits.
1621. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Modular inverse](modular-inverse.md): $\xi$ (group generator): A generator of the cyclic group of order S.
1622. $\xi$
   - on `packed-bit-addition`: $\xi$ (target segment value): The integer value of a segment of the target field.
   - on [Bézout's identity](bezout-identity.md): $\xi$ (least positive combination): The least positive value of βρ'+γσ' over all integers ρ' and σ'.
1623. $\eta$
   - on `packed-bit-addition`: $\eta$ (scratch segment value): The integer value of the matching segment of the scratch field.
   - on [Linear algebra basics](linear-algebra-basics.md): $\eta$ (scalar): A scalar in F multiplying a vector.
1624. $\eta$
   - on `packed-bit-addition`: $\eta$ (scratch segment value): The integer value of the matching segment of the scratch field.
   - on [Congruence](congruence-modulo.md): $\eta$ (second multiple): The integer with $e'-e=\eta B$.
1625. $\eta$
   - on `packed-bit-addition`: $\eta$ (scratch segment value): The integer value of the matching segment of the scratch field.
   - on [Transform round](transform-round.md): $\eta$ (twiddle exponent): The exponent of y at an address, so that the round multiplies each record by y to the power eta.
1626. $\eta$
   - on `packed-bit-addition`: $\eta$ (scratch segment value): The integer value of the matching segment of the scratch field.
   - on [Subset-intersection network](subset-intersection-network.md): $\eta$ (target vector): The vector, indexed by triples, of the entries of the target bank along the varying coordinate.
1627. $\eta$
   - on `packed-bit-addition`: $\eta$ (scratch segment value): The integer value of the matching segment of the scratch field.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\eta$ (half-size): The number of positions in each half of a block at a level of the transform.
1628. $\eta$
   - on `packed-bit-addition`: $\eta$ (scratch segment value): The integer value of the matching segment of the scratch field.
   - on [Linear contraction](linear-contraction.md): $\eta$ (carried error): The error vector carried by the computed input, so that the computed input is x + η.
1629. $\beta$
   - on `packed-bit-addition`: $\beta$ (control bit): The selected bit of the source in a segment, which controls its updates.
   - on [Rank-saving recursion](rank-saving-recursion.md): $\beta$ (one-digit cost constant): A constant such that one digit's interchange costs at most $\beta V$.
1630. $\beta$
   - on `packed-bit-addition`: $\beta$ (control bit): The selected bit of the source in a segment, which controls its updates.
   - on [Permutation](permutation.md): $\beta$ (second entry): The entry of the sequence at position 2.
1631. $\beta$
   - on `packed-bit-addition`: $\beta$ (control bit): The selected bit of the source in a segment, which controls its updates.
   - on [Mixed-radix digits](mixed-radix-digits.md): $\beta$ (place count): The number of places, a positive integer; the places are numbered 1 to beta.
1632. $\beta$
   - on `packed-bit-addition`: $\beta$ (control bit): The selected bit of the source in a segment, which controls its updates.
   - on [Modular inverse](modular-inverse.md): $\beta$ (integer to invert): The integer whose inverse modulo M is sought.
1633. $\mathcal{E}$
   - on `packed-bit-addition`: $\mathcal{E}$ (exceptional set): The set of addresses at which some guard lies outside the safe range.
   - on [Destination rank](destination-rank.md): $\mathcal{E}$ (exceptional addresses): The set of addresses whose records the correction moves.
1634. $\mathcal{E}$
   - on `packed-bit-addition`: $\mathcal{E}$ (exceptional set): The set of addresses at which some guard lies outside the safe range.
   - on [Gaussian resampling](gaussian-resampling.md): $\mathcal{E}$ (first contraction): The map $\Psi/2$ from length $q$ to length $W$, which is a contraction.
1635. $\delta$
   - on `packed-bit-addition`: $\delta$ (bad fraction bound): The bound on the fraction of exceptional addresses, capped at one.
   - on [Permutation](permutation.md): $\delta$ (fourth entry): The entry of the sequence at position 4.
1636. $\delta$
   - on `packed-bit-addition`: $\delta$ (bad fraction bound): The bound on the fraction of exceptional addresses, capped at one.
   - on [Congruence](congruence-modulo.md): $\delta$ (remainder): The unique integer in $\{0,\dots,B-1\}$ lying in a residue class.
1637. $\delta$
   - on `packed-bit-addition`: $\delta$ (bad fraction bound): The bound on the fraction of exceptional addresses, capped at one.
   - on [Transform round](transform-round.md): $\delta$ (remainder): The remainder of eta on division by r, from 0 to r minus 1.
1638. $\delta$
   - on `packed-bit-addition`: $\delta$ (bad fraction bound): The bound on the fraction of exceptional addresses, capped at one.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $\delta$ (chunk width): The number of consecutive address bits in each transform axis (chunk).
1639. $\delta$
   - on `packed-bit-addition`: $\delta$ (bad fraction bound): The bound on the fraction of exceptional addresses, capped at one.
   - on [Two-point kernel](two-point-kernel.md): $\delta$ (identity coefficient): The complex coefficient of the identity matrix in a two-point kernel.
1640. $\delta$
   - on `packed-bit-addition`: $\delta$ (bad fraction bound): The bound on the fraction of exceptional addresses, capped at one.
   - on [Limit inferior](limit-inferior.md): $\delta$ (arbitrary positive real): A real number greater than zero, arbitrary in the negation of the conjecture.
1641. $\delta$
   - on `packed-bit-addition`: $\delta$ (bad fraction bound): The bound on the fraction of exceptional addresses, capped at one.
   - on [Extended real numbers](extended-reals.md): $\delta$ (term position): The position of a term in a sequence, a positive integer.
1642. $\delta$
   - on `packed-bit-addition`: $\delta$ (bad fraction bound): The bound on the fraction of exceptional addresses, capped at one.
   - on [Cost table](cost-table.md): $\delta$ (small exponent): A fixed small exponent, equal to $1/16$.
1643. $\delta$
   - on `packed-bit-addition`: $\delta$ (bad fraction bound): The bound on the fraction of exceptional addresses, capped at one.
   - on [Matrix rank](matrix-rank.md): $\delta$ (second field value): The value of the field $J_j$ before one update.
1644. $\pi$
   - on `packed-bit-addition`: $\pi$ (address permutation): The permutation of addresses that the correction must realize.
   - on [Bilinear map](bilinear-map.md): $\pi$ (bilinear map): The map sending each pair of arguments to a vector of the output space, linear in each argument.
1645. $\operatorname{rank}$
   - on `packed-bit-addition`: $\operatorname{rank}$ (stream rank): The number of addresses that come before a given address in stream order.
   - on [Destination rank](destination-rank.md): $\operatorname{rank}$ (rank): The position of the record at an address among the records in stream order, counted from 0.
1646. $p$
   - on `packed-bit-addition`: $p$ (family index): The index of the family of parameters, which tends to infinity.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $p$ (working precision): The working precision in bits: the inputs lie on the grid $2^{-p}\mathbb Z[i]$.
1647. $p$
   - on `packed-bit-addition`: $p$ (family index): The index of the family of parameters, which tends to infinity.
   - on [Truncation](truncation.md): $p$ (precision): The number of fractional binary places kept, which counts the binary digits after the point.
1648. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Integer](integer.md): $m$ (bit count): The number of bits in a binary string.
1649. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Root of unity](root-of-unity.md): $m$ (order): The least positive integer with $z^m = 1$, which is also the number of distinct powers of $z$.
1650. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Linear algebra basics](linear-algebra-basics.md): $m$ (coordinate count): The number of coordinates in each vector of F^m.
1651. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Address-field interchange](address-interchange.md): $m$ (pieces per level): A fixed integer at least 2, the number of pieces each field is cut into at each level.
1652. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Limit inferior](limit-inferior.md): $m$ (tail start): The position from which a tail of the sequence starts.
1653. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Opposite transform](opposite-transform.md): $m$ (summation index): A dummy summation index running from $0$ to $q-1$ that names an input position of a vector; it counts nothing.
1654. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Exact coefficient recovery](recovery-and-error.md): $m$ (nearest integer): The integer nearest to a computed value that lies within $1/2$ of it.
1655. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Normalization scales](normalization-scales.md): $m$ (digit count): The number of digits of each input, which is also the number of entries of each digit array.
1656. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Normalized cyclic convolution](normalized-cyclic-convolution.md): $m$ (chirp argument): A free integer at which the chirp phase $\chi_m$ is evaluated; this letter changes meaning here and is not the order of a root.
1657. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Guard-width bound](guard-width-bound.md): $m$ (splitting factor): The factor by which a call divides the axis count.
1658. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Polynomial ring](polynomial-ring.md): $m$ (coefficient count): The number of coefficients in each representative, which is the degree of f.
1659. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Rank-saving recursion](rank-saving-recursion.md): $m$ (label dimension): The dimension of the fixed nondegenerate space $F$ that contains every label.
1660. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Complex construction](complex-construction.md): $m$ (label dimension): The dimension of the label space, h^3.
1661. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Numerical layer](numerical-layer.md): $m$ (division factor): The fixed integer by which a call divides its number of selected axes.
1662. $m$
   - on `main-theorem`: $m$ (growth factor): The factor by which one recursion level multiplies the call parameter.
   - on [Union bound](union-bound.md): $m$ (event count): The number of events E_1 through E_m.
1663. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Permutation](permutation.md): $W$ (position set): The finite set of positions on which a permutation acts.
1664. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Bijection](bijection.md): $W$ (target set): The set that the map $f$ sends its inputs into, the set of outputs.
1665. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Neumann series](neumann-series.md): $W$ (limit operator): The limit of the partial sums, which is the inverse $(I+J)^{-1}$.
1666. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Cyclic group](cyclic-group.md): $W$ (cyclic group order): The number of elements of the cyclic group $C_W$, which counts its distinct powers of the generator.
1667. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Coprime](coprime.md): $W$ (family product): The product f_1 times f_2 up to f_J, which is the least positive integer divisible by every member.
1668. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Tensor product](tensor-product.md): $W$ (row index of P'): A row index of $P'$, summed over as a middle index of $P$ and $P'$.
1669. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Bit network](bit-network.md): $W$ (source bank): The bank of source bits, holding one bit $W_\sigma$ for each triple $\sigma$.
1670. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Bilinear map](bilinear-map.md): $W$ (output space): The vector space that the bilinear map returns its values in.
1671. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Projection along a subspace](projection-along-subspace.md): $W$ (ambient space): The finite-dimensional vector space over $F$ on which every projection acts.
1672. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Orthogonal complement](orthogonal-complement.md): $W$ (larger label): The larger of the two labels on an edge, which contains the smaller label $U$.
1673. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $W$ (second butterfly entry): The entry of a butterfly pair at position $\gamma+\eta$ of the block.
1674. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Gaussian resampling](gaussian-resampling.md): $W$ (target length): The number of entries of the resampled vector, a power of two greater than $q$.
1675. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Grid numerator](grid-numerator.md): $W$ (output coefficient): One output coefficient of the paper's polynomial multiplication, a sum of $r$ signed products of input coefficients.
1676. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Ring homomorphism and isomorphism](ring-homomorphism.md): $W$ (quotient ring W): The ring of complex polynomials in t in which every multiple of t^2-1 is zero.
1677. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Rank-saving recursion](rank-saving-recursion.md): $W$ (wire count): The number of wires of the network, which is also the number of roles.
1678. $W$
   - on `main-theorem`: $W$ (number of pieces): The number of pieces into which a call divides its volume, counting the pieces.
   - on [Matrix rank](matrix-rank.md): $W$ (wire count): The number of wires of the paper's circuit, including its scratch wires.
1679. $V$
   - on `main-theorem`: $V$ (stored bit volume): The number of stored bits a call works on, counting the bits.
   - on [Logical bit volume](logical-bit-volume.md): $V$ (paper's bit volume): The paper's name for the same count of bits as the logical bit volume.
1680. $V$
   - on `main-theorem`: $V$ (stored bit volume): The number of stored bits a call works on, counting the bits.
   - on [Directed graph](directed-graph.md): $V$ (vertex set): The set of vertices of the directed graph, the points that edges join.
1681. $V$
   - on `main-theorem`: $V$ (stored bit volume): The number of stored bits a call works on, counting the bits.
   - on [Payload](payload.md): $V$ (stream volume): The number of bits stored in the stream, which the time bound counts.
1682. $V$
   - on `main-theorem`: $V$ (stored bit volume): The number of stored bits a call works on, counting the bits.
   - on [Scratch storage](scratch-storage.md): $V$ (copy): The operation that adds $x_T$ to $W_{ST}$ for each neighbouring pair.
1683. $V$
   - on `main-theorem`: $V$ (stored bit volume): The number of stored bits a call works on, counting the bits.
   - on [Linear functional](linear-functional.md): $V$ (vector space): The vector space over F whose vectors a linear functional takes as input.
1684. $V$
   - on `main-theorem`: $V$ (stored bit volume): The number of stored bits a call works on, counting the bits.
   - on [Eigenvalue](eigenvalue.md): $V$ (vector space): The vector space on which the linear operator T acts, over the field F.
1685. $V$
   - on `main-theorem`: $V$ (stored bit volume): The number of stored bits a call works on, counting the bits.
   - on [Bilinear map](bilinear-map.md): $V$ (second argument space): The vector space that the second argument of the bilinear map ranges over.
1686. $V$
   - on `main-theorem`: $V$ (stored bit volume): The number of stored bits a call works on, counting the bits.
   - on [Projection along a subspace](projection-along-subspace.md): $V$ (larger nested subspace): A nondegenerate subspace containing $U$, the larger of two nested labels.
1687. $V$
   - on `main-theorem`: $V$ (stored bit volume): The number of stored bits a call works on, counting the bits.
   - on [Complex phase network](complex-phase-network.md): $V$ (head label): The label at the head of an edge.
1688. $V$
   - on `main-theorem`: $V$ (stored bit volume): The number of stored bits a call works on, counting the bits.
   - on [Destination rank](destination-rank.md): $V$ (stream bit count): The number of bits in the stream, $MR$.
1689. $V$
   - on `main-theorem`: $V$ (stored bit volume): The number of stored bits a call works on, counting the bits.
   - on [Rank-saving recursion](rank-saving-recursion.md): $V$ (padded volume): The stored volume of the array after padding, in bits.
1690. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Telescoping identity](telescoping-identity.md): $e$ (last position): The last position of a sum over positions, the upper limit of the sum.
1691. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Transform round](transform-round.md): $e$ (quotient): The integer quotient of eta by r: the number of whole multiples of r in eta.
1692. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Two-point kernel](two-point-kernel.md): $e$ (bit position): An index from 0 to d-1 naming the bit along which a kernel acts, counted from the least significant bit.
1693. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Congruence](congruence-modulo.md): $e$ (integer): An integer compared with $d$ modulo $B$.
1694. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Eigenvalue](eigenvalue.md): $e$ (eigenvector): A nonzero vector of V that T maps to a multiple of itself.
1695. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Indicator vector](indicator-vector.md): $e$ (position): An element of the ground set [h], a position of the indicator vector.
1696. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Chinese-remainder map](chinese-remainder-map.md): $e$ (coefficient index): An ordinary coefficient index in $[0,\Lambda)$, the position of a coefficient in the one-dimensional ring.
1697. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Phase twist](phase-twist.md): $e$ (Euler's number): The base of the natural exponential, so that $e^{i\theta} = \cos\theta + i\sin\theta$.
1698. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Guard-width bound](guard-width-bound.md): $e$ (group size): The number of selected axes in a group that the recursion splits.
1699. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Polynomial ring](polynomial-ring.md): $e$ (exponent): The exponent of y in a term of a product, the power of y that reduction tests against m.
1700. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Rank-saving recursion](rank-saving-recursion.md): $e$ (chunk digit count): The number of digits in each chunk being interchanged.
1701. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Numerical layer](numerical-layer.md): $e$ (selected axis count): The number of selected axes that a call acts on.
1702. $e$
   - on `main-theorem`: $e$ (call parameter): The parameter of a call, which counts its field digits or selected axes.
   - on [Address shear](address-shear.md): $e$ (chunk digit count): The number of digits in a chunk at recursion depth $k$, equal to $m^k$.
1703. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Transform axis](transform-axis.md): $s$ (coefficient count): A power of two that is the number of coefficients of the stored polynomial, which is also the length of its axis.
1704. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $s$ (input index): An integer index running over $0, 1, \ldots, q-1$ that labels an input coordinate $f_s$.
1705. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Array norm](array-norm.md): $s$ (coefficient index): The index of a coefficient of a ring element, running from 0 to r-1.
1706. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Mixed-radix digits](mixed-radix-digits.md): $s$ (common length): The common length of every place, which is also the base; it counts the digit values.
1707. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Telescoping identity](telescoping-identity.md): $s$ (first position): The first position of a sum over positions, the lower limit of the sum.
1708. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $s$ (number of H_0 factors): The number of individual factors $H_0$ applied, which refines the grid to $2^{-(p+s)}$.
1709. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Ceiling function](ceiling-function.md): $s$ (real number): The real number that the ceiling rounds up to an integer.
1710. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Truncation](truncation.md): $s$ (first pair value): The first of the two values in a pair that a layer combines.
1711. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Address-field interchange](address-interchange.md): $s$ (smaller calls): The number of smaller calls one call makes, equal to the sum of the edge ranks.
1712. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Subspace labels](subspace-labels.md): $s$ (basis index): An index numbering the basis vectors of an edge residual.
1713. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Ring homomorphism and isomorphism](ring-homomorphism.md): $s$ (square-one element): An element of the commutative target ring whose square is 1, the image of t.
1714. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Supremum](supremum.md): $s$ (positive integer index): A positive integer index, the exponent in each element $1-2^{-s}$ of the example set.
1715. $s$
   - on `main-theorem`: $s$ (smaller-call count): The number of smaller calls that one call makes.
   - on [Polynomial ring](polynomial-ring.md): $s$ (shift exponent): The integer exponent of the power of y that multiplies the representative, which the paper writes as a.
1716. $F_k$
   - on `main-theorem`: $F_k$ (cost per unit volume): The time per unit volume of a call at parameter m^k.
   - on [Address shear](address-shear.md): $F_k$ (time per unit volume): The time per unit volume at recursion depth $k$.
1717. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Integer](integer.md): $k$ (digit count): The number of digits in a digit list.
1718. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Root of unity](root-of-unity.md): $k$ (integer exponent): An integer exponent of $y$ in the power $y^k$ that multiplies the coefficient list.
1719. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $k$ (padded length): The number of bits in a padded binary string, that is, the length to which $\mathrm{bin}_k$ pads.
1720. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Telescoping identity](telescoping-identity.md): $k$ (term position): The position of a term in the sequence, running from 0 to o.
1721. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $k$ (output index): The index of an output coordinate of the transform $F_q$.
1722. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Address-field interchange](address-interchange.md): $k$ (level count): The number of levels of the recursion, the logarithm to base m of the field width u.
1723. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Limit inferior](limit-inferior.md): $k$ (term position): A position in a sequence, the index of a term.
1724. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Multidimensional transform](multidimensional-transform.md): $k$ (radix-two exponent): The exponent with t_sigma equal to 2^k, which counts the radix-two levels of the axis transform.
1725. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Gaussian resampling](gaussian-resampling.md): $k$ (output index): The index of an entry of a length-$W$ output vector, running from $0$ to $W-1$.
1726. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Cyclic convolution](cyclic-convolution.md): $k$ (output position): The position of an entry of the output $f \ast g$, running from 0 to n-1.
1727. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Chinese-remainder map](chinese-remainder-map.md): $k$ (exponent): A nonnegative integer exponent of $x_i$, the power to which the indeterminate of axis $i$ is raised.
1728. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Guard-width bound](guard-width-bound.md): $k$ (internal levels): The number of internal levels of the recursion.
1729. $k$
   - on `main-theorem`: $k$ (recursion levels): The number of levels of recursion beneath a call, counting them.
   - on [Convolution over the polynomial ring](polynomial-ring-convolution.md): $k$ (summation index): The index of the sum on an axis, running over the $t$ positions of that axis.
1730. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Discrete Fourier transform](discrete-fourier-transform.md): $\rho$ (exponent): An integer exponent of $\omega$; in the inner sum it is the difference $\sigma - \ell$, with $-q < \rho < q$.
1731. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Address field](address-field.md): $\rho$ (field width): The number of bits in each of the two fields being interchanged, a count of bit positions.
1732. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Linear networks and frames](linear-network-frames.md): $\rho$ (role permutation): The permutation of roles that sends each input role to an output role.
1733. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Order of an element](order-of-element.md): $\rho$ (order): The least positive integer with sigma to the power rho equal to 1; it counts the distinct powers of sigma.
1734. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Cyclic group](cyclic-group.md): $\rho$ (generator): An element of a group, the base of its powers; when its powers are all the elements, it is the generator.
1735. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Coprime](coprime.md): $\rho$ (second integer): The other of two integers, not both zero, whose gcd is taken.
1736. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Binary change of basis](binary-change-of-basis.md): $\rho$ (residual dimension): The number of vectors in a residual basis, which counts the dimension of the edge's residual.
1737. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Dual space](dual-space.md): $\rho$ (second example functional): The linear functional on R^2 sending x to x_1.
1738. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Synthetic polynomial transforms](synthetic-transforms.md): $\rho$ (coefficient position): The position of a coefficient in a record, running from 0 to r-1.
1739. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Frequency domain](frequency-domain.md): $\rho$ (second input position): The position of an entry of the second input sequence $b$ in the convolution sum, running from $0$ to $q-1$.
1740. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Closed disk in the complex plane](complex-disk.md): $\rho$ (disk radius): The fixed nonnegative real radius, the largest allowed distance from the center.
1741. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Cyclic convolution](cyclic-convolution.md): $\rho$ (phase sequence): The function $\rho(\delta) = e^{-\pi i \delta^2/t}$, read as a sequence of length t modulo t.
1742. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Bézout's identity](bezout-identity.md): $\rho$ (Bézout coefficient of β): The integer multiplying β in the combination βρ+γσ that equals gcd(β,γ).
1743. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Prime number](prime-number.md): $\rho$ (prime): A prime number, the integer whose divisors are classified.
1744. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Ring homomorphism and isomorphism](ring-homomorphism.md): $\rho$ (substitution map): The homomorphism from W to C sending t to 1.
1745. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Linear contraction](linear-contraction.md): $\rho$ (rounding error): The rounding error introduced at one step of a computation, added to that step's output.
1746. $\rho$
   - on `main-theorem`: $\rho$ (call ratio): The ratio s/W of child calls to pieces.
   - on [Packed selected-bit addition](packed-bit-addition.md): $\rho$ (first selected position): The position of the first selected bit, counted from the least significant end.
1747. $\log_m$
   - on `main-theorem`: $\log_m$ (logarithm base m): The function sending x to the exponent t with m^t = x.
   - on [Numerical layer](numerical-layer.md): $\log_m$ (base-m logarithm): The exponent to which $m$ must be raised to give $x$.
1748. $\tau$
   - on `main-theorem`: $\tau$ (saving exponent): The exponent below one with a < m^tau, which sets the cost per unit volume.
   - on [Payload](payload.md): $\tau$ (fixed exponent): A fixed exponent strictly between 0 and 1 that sets the power of L in the time bound.
1749. $\tau$
   - on `main-theorem`: $\tau$ (saving exponent): The exponent below one with a < m^tau, which sets the cost per unit volume.
   - on [Address-field interchange](address-interchange.md): $\tau$ (fixed exponent): A fixed number below 1, the exponent in the cost bound $O(Vu^{\tau})$.
1750. $\tau$
   - on `main-theorem`: $\tau$ (saving exponent): The exponent below one with a < m^tau, which sets the cost per unit volume.
   - on [Extended real numbers](extended-reals.md): $\tau$ (sequence term): The term of a sequence at position $\delta$.
1751. $\tau$
   - on `main-theorem`: $\tau$ (saving exponent): The exponent below one with a < m^tau, which sets the cost per unit volume.
   - on [Diagonal scaling](diagonal-scaling.md): $\tau$ (scalar family): A family of scalars $\tau_\iota$ in $F$, one for each label, which defines a diagonal scaling.
1752. $\tau$
   - on `main-theorem`: $\tau$ (saving exponent): The exponent below one with a < m^tau, which sets the cost per unit volume.
   - on [Cost table](cost-table.md): $\tau$ (exchange exponent): The exponent $1-2^{-50}$ in the cost of a chunk exchange.
1753. $\tau$
   - on `main-theorem`: $\tau$ (saving exponent): The exponent below one with a < m^tau, which sets the cost per unit volume.
   - on [Rank-saving recursion](rank-saving-recursion.md): $\tau$ (power-saving exponent): A fixed number in $(0,1)$ that is the exponent of the bound $O(Ve^\tau)$.
1754. $b$
   - on `main-theorem`: $b$ (bit length of n): The number of bits of n, the ceiling of log2 n, counting them.
   - on [Logarithm](logarithm.md): $b$ (base): The fixed base of the logarithm, a number greater than 1.
1755. $b$
   - on `main-theorem`: $b$ (bit length of n): The number of bits of n, the ceiling of log2 n, counting them.
   - on [Integer](integer.md): $b$ (base): The base (radix) of a digit representation, an integer at least 2.
1756. $b$
   - on `main-theorem`: $b$ (bit length of n): The number of bits of n, the ceiling of log2 n, counting them.
   - on [Convolution](convolution.md): $b$ (second input sequence): The second of the two input sequences, of length $n$.
1757. $b$
   - on `main-theorem`: $b$ (bit length of n): The number of bits of n, the ceiling of log2 n, counting them.
   - on [Radix-digit convolution](radix-digit-convolution.md): $b$ (digit width): The number of bits in each digit of an input.
1758. $b$
   - on `main-theorem`: $b$ (bit length of n): The number of bits of n, the ceiling of log2 n, counting them.
   - on [Extended real numbers](extended-reals.md): $b$ (least real bound): The least real upper bound of $R$, which is the supremum of $S$ in that case.
1759. $b$
   - on `main-theorem`: $b$ (bit length of n): The number of bits of n, the ceiling of log2 n, counting them.
   - on [Prime source lengths](prime-source-lengths.md): $b$ (bit length): The number of binary digits of $n$, $b=\lceil\log_2 n\rceil$.
1760. $b$
   - on `main-theorem`: $b$ (bit length of n): The number of bits of n, the ceiling of log2 n, counting them.
   - on [Chinese-remainder map](chinese-remainder-map.md): $b$ (second exponent): The larger of two exponents of $\Phi(x)$ compared for equality, an integer with $a<b<\Lambda$.
1761. $b$
   - on `main-theorem`: $b$ (bit length of n): The number of bits of n, the ceiling of log2 n, counting them.
   - on [Convolution over the polynomial ring](polynomial-ring-convolution.md): $b$ (record address): An address of the second input array, which indexes its records.
1762. $b$
   - on `main-theorem`: $b$ (bit length of n): The number of bits of n, the ceiling of log2 n, counting them.
   - on [Cost table](cost-table.md): $b$ (bit length): The rounded-up base-2 logarithm of $n$, which counts the bits of $n$.
1763. $b$
   - on `main-theorem`: $b$ (bit length of n): The number of bits of n, the ceiling of log2 n, counting them.
   - on [Address shear](address-shear.md): $b$ (digits per field): The number of radix-$q$ digits in each field, so it counts digits.
1764. $p$
   - on `main-theorem`: $p$ (working precision): The working precision in bits, equal to 6b.
   - on [Truncation](truncation.md): $p$ (precision): The number of fractional binary places kept, which counts the binary digits after the point.
1765. $p$
   - on `main-theorem`: $p$ (working precision): The working precision in bits, equal to 6b.
   - on [Signed coefficient packing](signed-packing.md): $p$ (coefficient bit bound): The number of bits in a bound on the coefficient magnitudes, so that each coefficient has absolute value at most $2^p$.
1766. $p$
   - on `main-theorem`: $p$ (working precision): The working precision in bits, equal to 6b.
   - on [Packed selected-bit addition](packed-bit-addition.md): $p$ (family index): The index of the family of parameters, which tends to infinity.
1767. $d$
   - on `main-theorem`: $d$ (axis bound): An upper bound on the number of selected axes of the numerical layer, counting axes.
   - on [Address](address.md): $d$ (address length): The number of bits in each address of the array, the length of every address string.
1768. $d$
   - on `main-theorem`: $d$ (axis bound): An upper bound on the number of selected axes of the numerical layer, counting axes.
   - on [Tape procedure](tape-procedure.md): $d$ (chunk count bound): An upper bound on the number of equal-width address chunks whose selected bits one pass handles.
1769. $d$
   - on `main-theorem`: $d$ (axis bound): An upper bound on the number of selected axes of the numerical layer, counting axes.
   - on [Congruence](congruence-modulo.md): $d$ (integer): An integer compared with $e$ modulo $B$.
1770. $d$
   - on `main-theorem`: $d$ (axis bound): An upper bound on the number of selected axes of the numerical layer, counting axes.
   - on [Exact coefficient recovery](recovery-and-error.md): $d$ (number of axes): The number of axes of the padded box, equal to $\lfloor b^{\epsilon}\rfloor$.
1771. $d$
   - on `main-theorem`: $d$ (axis bound): An upper bound on the number of selected axes of the numerical layer, counting axes.
   - on [Cyclic convolution](cyclic-convolution.md): $d$ (axis count): The number of axes in the split, that is, the number of factors $n_1, \dots, n_d$ of the length n.
1772. $d$
   - on `main-theorem`: $d$ (axis bound): An upper bound on the number of selected axes of the numerical layer, counting axes.
   - on [Cost table](cost-table.md): $d$ (axis count): The number of axes of the padded box.
1773. $d$
   - on `main-theorem`: $d$ (axis bound): An upper bound on the number of selected axes of the numerical layer, counting axes.
   - on [Numerical layer](numerical-layer.md): $d$ (selected-bit bound): An upper bound on the number $D$ of selected bits, so that $D \le d$.
1774. $\epsilon$
   - on `main-theorem`: $\epsilon$ (size exponent): The fixed exponent in d = Theta(p^epsilon), with 0 < epsilon < 1.
   - on [Cost table](cost-table.md): $\epsilon$ (dimension exponent): A fixed positive exponent, equal to $2^{-75}$.
1775. $C$
   - on `main-theorem`: $C$ (padded box cell count): The number of cells of the padded box, the array the transforms act on.
   - on [Simultaneous butterfly layer](simultaneous-butterfly-layer.md): $C$ (two-point kernel): The two-by-two operator $\mathcal H\Delta\mathcal H$, equal to $\lambda I+\mu X$.
1776. $C$
   - on `main-theorem`: $C$ (padded box cell count): The number of cells of the padded box, the array the transforms act on.
   - on [Phase factor](phase-factor.md): $C$ (forward kernel): The 2 by 2 matrix with entries (1+i)/2 and (1-i)/2 that is the forward kernel.
1777. $C$
   - on `main-theorem`: $C$ (padded box cell count): The number of cells of the padded box, the array the transforms act on.
   - on [Little-o notation](little-o-notation.md): $C$ (big-O constant): A constant such that the running time is at most C times n(lg n) to the power 1 minus kappa for all sufficiently large n.
1778. $z$
   - on `main-theorem`: $z$ (polynomial variable): The variable of the polynomial ring modulo z^r+1, which the source writes as y.
   - on [Root of unity](root-of-unity.md): $z$ (complex number): A complex number whose powers are taken; a root of unity is such a number.
1779. $z$
   - on `main-theorem`: $z$ (polynomial variable): The variable of the polynomial ring modulo z^r+1, which the source writes as y.
   - on [Exact integer multiplication](exact-integer-multiplication.md): $z$ (padded integer): A nonnegative integer with $z < 2^k$ that is written in binary.
1780. $z$
   - on `main-theorem`: $z$ (polynomial variable): The variable of the polynomial ring modulo z^r+1, which the source writes as y.
   - on [Union bound](union-bound.md): $z$ (address chunk z): The other of the two chunks of each address.
1781. $r$
   - on `main-theorem`: $r$ (coefficient count): The number of coefficients in a record, a power of two.
   - on [Truncation](truncation.md): $r$ (second pair value): The second of the two values in a pair that a layer combines.
1782. $r$
   - on `main-theorem`: $r$ (coefficient count): The number of coefficients in a record, a power of two.
   - in the name of Polynomial ring modulo y^r + 1: $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
1783. $r$
   - on `main-theorem`: $r$ (coefficient count): The number of coefficients in a record, a power of two.
   - on [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md): $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.

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

Write the answer to `exegenius/tasks/0617-overloads.answer.json`, then run `exegenius submit 0617-overloads` in the project directory. If submit rejects the answer, fix the answer and submit again.
