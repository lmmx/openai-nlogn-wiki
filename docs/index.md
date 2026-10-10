# Integer multiplication below n log n

This wiki explains [Deterministic O(n (lg n)^(1-kappa)) multiplication](main-theorem.md). There is one deterministic fixed-tape Turing machine computing the exact product of n-bit integers in O(n (lg n)^(1-kappa)) worst-case time, with kappa = 2^(-182), which refutes the n log n optimality conjecture in this model.

It is written for a reader who knows: Undergraduate computer science: big-O notation, polynomials, complex numbers

## Reading order

1. [Exact integer multiplication](exact-integer-multiplication.md) — Computing the exact binary representation of the product of two n-bit integers, with no rounding.
2. [Schönhage–Strassen n log n conjecture](n-log-n-conjecture.md) — The conjecture that n log n is the optimal order of growth for multiplying n-bit integers on a multitape Turing machine.
3. [Discrete Fourier transform](discrete-fourier-transform.md) — A linear map that evaluates a sequence at powers of a root of unity, computing convolutions pointwise after transformation.
4. [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md) — The ring of polynomials in y with coefficients in C, reduced modulo y^r + 1 for a power of two r, in which y^r = -1.
5. [Synthetic polynomial transform](synthetic-transform.md) — A transform over a polynomial ring modulo y^r + 1 whose roots of unity are powers of y, so that multiplying by a root is a signed cyclic shift of coefficients.
6. [Record](record.md) — A fixed-width block of stored data, such as one polynomial with complex coefficients, that is handled as a single unit by the procedures.
7. [Gaussian dyadic numbers](gaussian-dyadic.md) — Complex numbers whose real and imaginary parts are dyadic rationals, that is, have denominators that are powers of two.
8. [Row of an array](row-of-array.md) — The block of consecutive entries that share a fixed prefix and row index, containing all address fields after the row field.
9. [Established O(n log n) multiplier](established-multiplier.md) — The known deterministic O(n log n) multitape multiplication, used as an ordinary subroutine on short records.
10. [Signed coefficient packing](signed-packing.md) — Encoding polynomial coefficients as signed integers at a fixed bit spacing so that one integer multiplication computes a polynomial product in the ring modulo y^r + 1.
11. [Complementary intersection graphs](complementary-intersection-graph.md) — A pair of graphs on the same family of sets, one joining two sets when their intersection size lies in a prescribed set of values and the other joining the remaining pairs, so that each is the complement of the other.
12. [Rational bilinear form](rational-bilinear-form.md) — A function of two vectors that is linear in each argument separately and whose coefficients are rational numbers.
13. [Frankl–Wilson construction](frankl-wilson-construction.md) — A construction of set systems with restricted intersection sizes, which gives low-degree polynomial representations of intersection graphs over fields.
14. [Multitape Turing machine](turing-machine-model.md) — A Turing machine with a fixed finite alphabet and a fixed finite number of one-dimensional tapes, where each step moves each head by at most one cell.
15. [Bit complexity](bit-complexity.md) — The running time of an algorithm measured as the number of elementary bit-level steps on a fixed machine model, as opposed to arithmetic operations on words.
16. [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) — A tape procedure that applies the two-point map H0(u, v) = ((u + v)/2, (u − v)/2) to selected coordinate bits of all records at once, in O(V d^lambda') time.
17. [Linear networks with frames](linear-network-frames.md) — A fixed linear network that exchanges banks of values with prescribed signs and restores auxiliary values, where each node carries an invertible frame operator so that intermediate frames cancel along a route.
18. [Array with a complete Cartesian address set](cartesian-address-array.md) — An array whose addresses are all tuples in a product of ranges, stored in lexicographic order with the first coordinate most significant.
19. [Address-field interchange](address-interchange.md) — A tape procedure that swaps two disjoint contiguous address fields of u bits in O(V u^tau) time for a fixed tau < 1, with intermediate XOR combinations but an exact final permutation.
20. [Side wire](side-wire.md) — A wire of a linear network that joins two neighbouring triples of the construction, carrying values between them in addition to the central wires and the data wires.
21. [Linear index-code decoding](linear-index-coding-decoding.md) — Recovering a wanted coordinate from a low-rank linear summary of several coordinates by subtracting the contributions of neighbouring coordinates that are already known.
22. [Gather and scatter operations](gather-scatter.md) — Operations that collect the entries of a network's wires over a three-element subset and redistribute them, producing coefficients that depend only on the size of the intersection of two subsets.
23. [Linear contraction](linear-contraction.md) — A linear map that does not increase the size of its inputs, so that its output has norm at most that of the input.
24. [Cyclic convolution](cyclic-convolution.md) — Multiplication of two coefficient sequences as polynomials modulo x^S - 1, so that exponents wrap around modulo S.
25. [Gaussian resampling](gaussian-resampling.md) — A reduction that replaces a Fourier transform of arbitrary length by a multidimensional transform whose axis lengths are powers of two, using Gaussian-weighted resampling.
26. [Transform identity](transform-identity.md) — The identity that expresses each source Fourier transform, after Gaussian resampling, through a power-of-two tensor transform together with source and target coordinate permutations.
27. [Source and target permutations](target-permutation.md) — The reorderings of the coordinates of a transform's input and output that the transform identity keeps symbolically instead of executing as separate sorts.
28. [Chinese-remainder address map](chinese-remainder-map.md) — A relabelling of a cyclic convolution of length S as a multidimensional cyclic convolution over pairwise coprime lengths, via the Chinese remainder theorem.
29. [Sup norm](sup-norm.md) — The maximum absolute value of the coefficients of a polynomial or array.
30. [Middle transform](middle-transform.md) — The central factor in the splitting of a source Fourier transform into Gaussian resampling, a chirp, and this middle transform, which the chirp identity then converts into a convolution.
31. [Bluestein chirp identity](bluestein-chirp-identity.md) — An identity that rewrites a discrete Fourier transform, including its target permutation, as a normalized cyclic convolution with a quadratic-phase chirp.
32. [Coefficient phase twist](phase-twist.md) — A multiplication of coefficients by powers of a root zeta = e^(pi i / r) that converts cyclic wraparound in the last coordinate into negacyclic wraparound modulo y^r + 1, and back.
33. [Complex modulus (norm of a coefficient)](complex-modulus.md) — For a complex number x + iy, its modulus sqrt(x^2 + y^2), the length of the number viewed as a vector in the plane, which is the norm used to bound each coefficient.
34. [Disk-grid values](disk-grid-values.md) — Complex numbers stored exactly with p fractional bits in each real and imaginary part, with norm bounded by a fixed constant.
35. [Normalized cost](normalized-cost.md) — The running time of an operation divided by the stored volume V, so that costs of different operations on arrays of different sizes can be compared as powers of p.
36. [Linear convolution](linear-convolution.md) — The coefficient list of the ordinary product of two polynomials, with no reduction modulo any polynomial, so its length is the sum of the input lengths minus one.
37. [Radix-digit convolution](radix-digit-convolution.md) — Reduction of integer multiplication to a convolution of coefficient lists obtained by splitting each input into radix digits and propagating carries.
38. [Precision and exact recovery](precision-and-rounding.md) — The bookkeeping showing that fixed-precision approximations of the transforms recover each integer coefficient exactly after rounding, so that carry propagation yields the exact product.
39. [Parameter choice](parameter-choice.md) — The fixed rational exponents and the sizes b, p, d, T and r chosen so that the cost terms all fit the target bound.
40. [Multiplication algorithm](multiplication-algorithm.md) — The six-step algorithm that forms three source transforms, multiplies them pointwise, scales and rounds the result, and propagates carries to output the exact 2n-bit product.
41. [Indicator vector](indicator-vector.md) — A vector indexed by a ground set whose entry is 1 at the elements of a given subset and 0 elsewhere.
42. [Subset-intersection subspace construction](subspace-intersection-network.md) — A construction that attaches nested subspaces of a fixed space to the gates of a linear network, using three-element subsets and intersection-size parity, so that the subspace dimensions drop along each edge.
43. [Recursive rank saving](rank-saving-recursion.md) — The recursion in which a call at parameter m uses s smaller calls with s < W m, so the cost per unit of volume is multiplied by a factor below m at each level and gives a power saving.
44. [Cost accounting](cost-accounting.md) — The normalized cost table showing each operation costs O(T p) times a power of p, and that every exponent falls below one by a margin of at least 2^(-181) = 2 kappa.
45. [Deterministic O(n (lg n)^(1-kappa)) multiplication](main-theorem.md) — There is one deterministic fixed-tape Turing machine computing the exact product of n-bit integers in O(n (lg n)^(1-kappa)) worst-case time, with kappa = 2^(-182), which refutes the n log n optimality conjecture in this model.

## Assumed known

- Big-O notation — Asymptotic upper-bound notation for growth rates of running time.
- Polynomials — Formal sums of powers of an indeterminate with coefficients in a ring or field.
- Complex numbers — Numbers a + bi with real a, b and i squared equal to -1.

## Sources

- Integer multiplication below n log n (OpenAI, 2026)
