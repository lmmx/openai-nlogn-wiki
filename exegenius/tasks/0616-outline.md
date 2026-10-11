# exegenius task 0616-outline

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Organise the finished pages of an explanatory wiki into parts, and write its front page. The wiki explains a target result to a specific reader, one concept per page.

- Group the pages into parts that the reader works through in order, each a coherent stage of the explanation (for example: background, the main construction, the analysis). Aim for 3 to 8 parts; a small wiki may need fewer.
- Put every page in exactly one part, or in the glossary. Each page's prerequisites (listed below) must be in the glossary, the same part or an earlier one; submit rejects an outline that breaks this. Pages within a part are shown in reading order automatically, so their order in your list does not matter.
- Glossary: minor pages that define a term in a few sentences rather than explain an idea, such as a short page on a piece of terminology that one or two other pages use. They move to a glossary page, out of the reading order; links to them still work. Keep every page that explains a method, construction, result or argument in a part. Never put the target in the glossary. The word count and the number of pages using each page are listed to help.
- If the argument's main steps are listed below, base the parts on them where the prerequisites allow: a part per main step, with the pages that present its sub-steps, and background parts for the concepts the steps rely on.
- Part titles: 2 to 5 words, plain text, no numbering.
- Part intros: 2 to 4 sentences on what the part covers and why the reader needs it for what comes next. Link pages as `[Name](id.md)`.
- Overview: the front page, 150 to 350 words, for the reader described below. Say what the target result is and why it matters, then the route the wiki takes to it, part by part, naming the key ideas and linking their pages as `[Name](id.md)`. No headings.
- Write for this reader: concrete and specific, with no filler and no rhetorical flourishes. Mathematics in LaTeX ($...$). Links to anything other than the pages listed are rejected; external URLs are allowed.

## Target

Integer multiplication below n log n: A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model.

## Reader

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Pages, in reading order

- `integer`: [Integer](integer.md) — A whole number, positive, negative or zero. (670 words, used by 4)
- `logarithm`: [Logarithm](logarithm.md) — The exponent to which a fixed base must be raised to give a positive number; lg n is the logarithm to base 2. Needs: integer. (316 words, used by 4)
- `base-two-logarithm`: [Base-2 logarithm](base-two-logarithm.md) — The logarithm to base 2, written lg n or log₂ n. Needs: logarithm. (256 words, used by 2)
- `root-of-unity`: [Root of unity](root-of-unity.md) — A complex number z for which some positive power of z equals one. (389 words, used by 3)
- `running-time-cost`: [Running time cost](running-time-cost.md) — The number of machine steps an algorithm takes, as a worst-case function of the input length, on a machine with a fixed alphabet and fixed number of tapes. (452 words, used by 5)
- `exact-integer-multiplication`: [Exact integer multiplication](exact-integer-multiplication.md) — Given binary strings x and y of length n, output the 2n-bit binary representation of their product. Needs: running-time-cost. (356 words, used by 7)
- `convolution`: [Convolution](convolution.md) — The product of two sequences in which each output index sums the products of pairs of input indices that combine to it. Needs: exact-integer-multiplication. (241 words, used by 2)
- `payload`: [Payload](payload.md) — The record data carried at each address of an array, as distinct from the address that locates it. (316 words, used by 3)
- `mathematical-induction`: [Mathematical induction](mathematical-induction.md) — A proof method that establishes a statement for all integers by proving a base case and that each case implies the next. (290 words, used by 1)
- `little-o-notation`: [Little-o notation](little-o-notation.md) — A function f is o(g) when the ratio f/g tends to zero, a stronger statement than being O(g). (470 words, used by 2)
- `address`: [Address](address.md) — A label that locates one entry of an array, written as a string of address bits. (290 words, used by 7)
- `truncation`: [Truncation](truncation.md) — Discarding the fractional digits of a value beyond a fixed precision, here toward zero, so that the value stays on a fixed grid. Needs: address. (540 words, used by 1)
- `array`: [Array](array.md) — A finite collection of entries, each stored at an address and carrying a payload. Needs: address, payload. (289 words, used by 6)
- `array-norm`: [Array norm](array-norm.md) — The maximum modulus over all entries of an array of complex values; an array has norm at most one exactly when every entry has modulus at most one. Needs: array. (271 words, used by 5)
- `ceiling-function`: [Ceiling function](ceiling-function.md) — The least integer that is not less than a given real number, written with brackets ⌈x⌉. Needs: exact-integer-multiplication. (197 words, used by 1)
- `big-theta-notation`: [Big-Theta notation](big-theta-notation.md) — A function f is Θ(g) when f is both O(g) and bounded below by a constant multiple of g for large inputs. (547 words, used by 2)
- `extended-reals`: [Extended real numbers](extended-reals.md) — The real numbers together with two added values, positive infinity and negative infinity. (472 words, used by 1)
- `supremum`: [Supremum](supremum.md) — The least upper bound of a set of real numbers. Needs: array-norm. (339 words, used by 1)
- `telescoping-identity`: [Telescoping identity](telescoping-identity.md) — A sum of differences of consecutive terms equals the difference of its first and last terms. (354 words, used by 1)
- `mixed-radix-digits`: [Mixed-radix digits](mixed-radix-digits.md) — The digits of an integer written in a positional system whose place values use a separate length for each place, so that the digit at each place ranges over its own length. Needs: telescoping-identity. (619 words, used by 4)
- `fixed-width-digit-blocks`: [Fixed-width digit blocks](fixed-width-digit-blocks.md) — A coefficient stored as a block of a fixed number of digits in a positional system with base B, padded with leading zeros. Needs: mixed-radix-digits. (484 words, used by 1)
- `exceptional-set`: [Exceptional set](exceptional-set.md) — The set of addresses at which a generic formula must be replaced by a special rule; the generic formula is correct everywhere outside it. Needs: address. (369 words, used by 2)
- `big-omega-notation`: [Big-Omega notation](big-omega-notation.md) — A function f is Ω(g) when f is bounded below by a positive constant times g for all sufficiently large inputs. (459 words, used by 1)
- `bit-reversed-order`: [Bit-reversed index order](bit-reversed-order.md) — The order of array positions obtained by reversing the binary digits of each index. Needs: address. (219 words, used by 1)
- `directed-graph`: [Directed graph](directed-graph.md) — A set of vertices together with a set of ordered pairs of vertices, called directed edges. (244 words, used by 1)
- `linear-algebra-basics`: [Linear algebra basics](linear-algebra-basics.md) — Vector spaces over a field, linear maps and matrices, and the inverse of an invertible linear operator. Needs: array, directed-graph. (635 words, used by 22)
- `discrete-fourier-transform`: [Discrete Fourier transform](discrete-fourier-transform.md) — The map sending a vector of q values to its q values weighted by powers of a q-th root of unity, normalized by 1/q. Needs: convolution, linear-algebra-basics. (633 words, used by 14)
- `transform-axis`: [Transform axis](transform-axis.md) — One coordinate direction of a multidimensional array or transform, with its own length. Needs: discrete-fourier-transform, root-of-unity. (364 words, used by 6)
- `synthetic-transforms`: [Synthetic polynomial transforms](synthetic-transforms.md) — Fourier-type transforms whose roots of unity are powers of y in a polynomial ring, so that multiplying by a root is a signed shift of coefficients. Needs: discrete-fourier-transform, bit-reversed-order. (1007 words, used by 5)
- `linear-contraction`: [Linear contraction](linear-contraction.md) — A linear map that does not increase the maximum modulus of any vector, so that errors pass through it without growing. Needs: linear-algebra-basics, supremum. (336 words, used by 1)
- `bilinear-map`: [Bilinear map](bilinear-map.md) — A map that is linear in each of two vector arguments separately, such as the product of two polynomials. Needs: linear-algebra-basics, array, array-norm. (436 words, used by 2)
- `coprime`: [Coprime](coprime.md) — Two integers are coprime when their greatest common divisor is 1; a set of integers is pairwise coprime when every two of them are coprime. Needs: transform-axis. (423 words, used by 7)
- `bezout-identity`: [Bézout's identity](bezout-identity.md) — For integers a and b with greatest common divisor d, there are integers x and y with ax + by = d. Needs: coprime. (341 words, used by 1)
- `cyclic-group`: [Cyclic group](cyclic-group.md) — A group whose elements are all powers of one fixed element, called a generator. Needs: coprime. (459 words, used by 2)
- `order-of-element`: [Order of an element](order-of-element.md) — The least positive integer k for which the k-th power of an element of a group is the identity. Needs: cyclic-group. (590 words, used by 1)
- `diagonal-scaling`: [Diagonal scaling](diagonal-scaling.md) — A linear operator that multiplies each coordinate by its own fixed scalar. Needs: linear-algebra-basics. (477 words, used by 1)
- `frequency-domain`: [Frequency domain](frequency-domain.md) — The representation of a sequence by the values of its discrete Fourier transform. Needs: discrete-fourier-transform. (717 words, used by 1)
- `projection-along-subspace`: [Projection along a subspace](projection-along-subspace.md) — A linear map that keeps the component of a vector in one subspace and removes its component in a complementary subspace. Needs: linear-algebra-basics. (665 words, used by 1)
- `complex-disk`: [Closed disk in the complex plane](complex-disk.md) — The set of complex numbers whose distance from a fixed center is at most a fixed radius. (367 words, used by 1)
- `linear-functional`: [Linear functional](linear-functional.md) — A linear map from a vector space to its field of scalars. Needs: linear-algebra-basics. (388 words, used by 2)
- `dual-space`: [Dual space](dual-space.md) — The vector space of all linear functionals on a given vector space. Needs: linear-algebra-basics, linear-functional. (219 words, used by 1)
- `floor-function`: [Floor function](floor-function.md) — The greatest integer that is not greater than a given real number. Needs: integer. (375 words, used by 1)
- `bijection`: [Bijection](bijection.md) — A map that is one-to-one and onto, so that every element of the target is hit by exactly one element of the source. Needs: floor-function, exceptional-set. (535 words, used by 2)
- `permutation`: [Permutation](permutation.md) — A bijection of a finite set onto itself, which rearranges the positions of a sequence. Needs: bijection. (471 words, used by 3)
- `address-field`: [Address field](address-field.md) — A contiguous block of address bits of an array, which an address interchange exchanges with another block of the same width. Needs: address, permutation. (496 words, used by 5)
- `linear-network-frames`: [Linear networks and frames](linear-network-frames.md) — A fixed linear network that exchanges two banks of values while restoring scratch values, in which each vertex carries an invertible operator called its frame. Needs: linear-algebra-basics, address-field. (671 words, used by 12)
- `logical-array`: [Logical array](logical-array.md) — The array of values that a role presents to the network, which may differ from the stored array by a frame. Needs: array, linear-network-frames. (428 words, used by 1)
- `cyclic-shift`: [Cyclic shift](cyclic-shift.md) — A rotation of the values of a block of positions by an offset taken modulo the block length, where the offset may be set by control bits. Needs: address-field, running-time-cost. (342 words, used by 3)
- `butterfly`: [Butterfly](butterfly.md) — The two-point map H0(u, v) = ((u + v)/2, (u − v)/2) applied to a pair of values, the elementary step of a Fourier-type transform. Needs: discrete-fourier-transform, cyclic-shift. (274 words, used by 5)
- `radix-digit-convolution`: [Radix-digit convolution](radix-digit-convolution.md) — Writing both integers as polynomials in a power of two whose coefficients are their digits, so that their product is a polynomial convolution of short coefficients. Needs: exact-integer-multiplication, discrete-fourier-transform, butterfly, big-theta-notation. (859 words, used by 7)
- `ground-set`: [Ground set](ground-set.md) — A finite set from which the subsets under consideration are chosen. Needs: linear-network-frames. (187 words, used by 2)
- `network-gate-terminal`: [Gate and terminal of a network](network-gate-terminal.md) — A gate combines the values on the wires it touches by a fixed linear map, and a terminal is an input or output end of a wire where the network's values enter or leave. Needs: linear-network-frames. (507 words, used by 4)
- `incidence`: [Incidence](incidence.md) — The relation that a gate and a wire have when the wire touches the gate. Needs: network-gate-terminal, linear-network-frames. (417 words, used by 1)
- `tensor-product`: [Tensor product](tensor-product.md) — The Kronecker product of two matrices, whose m-fold power applies one operator to m independent coordinates at once. Needs: linear-algebra-basics, butterfly. (560 words, used by 4)
- `carry-propagation`: [Carry propagation](carry-propagation.md) — Converting the recovered integer radix-digit coefficients into a binary string by adding each coefficient to a carry from the previous position. Needs: radix-digit-convolution, ceiling-function, base-two-logarithm. (894 words, used by 4)
- `congruence-modulo`: [Congruence](congruence-modulo.md) — Two integers are congruent modulo m when their difference is divisible by m; a residue is the class of an integer modulo m. Needs: carry-propagation, integer. (472 words, used by 7)
- `schonhage-strassen`: [Schönhage–Strassen multiplication](schonhage-strassen.md) — The fast integer multiplication method of Schönhage and Strassen, which multiplies n-bit integers in O(n log n log log n) time. Needs: exact-integer-multiplication, order-of-element, congruence-modulo. (266 words, used by 3)
- `ring`: [Ring](ring.md) — A set with addition and multiplication that satisfy the usual axioms, with addition forming a commutative group. Needs: array, schonhage-strassen. (331 words, used by 3)
- `polynomial-ring-mod-yr-plus-1`: [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md) — The ring of polynomials with complex coefficients in which y^r is identified with −1, so that y has order 2r and wrap-around flips a sign. Needs: synthetic-transforms, ring. (778 words, used by 3)
- `limit-inferior`: [Limit inferior](limit-inferior.md) — The smallest value that a sequence approaches infinitely often; its limit inferior is zero when it has subsequences that tend to zero. Needs: schonhage-strassen, extended-reals. (657 words, used by 2)
- `n-log-n-conjecture`: [The n log n optimality conjecture](n-log-n-conjecture.md) — The conjecture that n log n is the optimal order of growth of the time needed to multiply two n-bit integers. Needs: exact-integer-multiplication, limit-inferior. (572 words, used by 2)
- `fixed-tape-model`: [Fixed-tape machine model](fixed-tape-model.md) — A Turing machine with one fixed finite alphabet and one fixed finite number of one-dimensional tapes, whose size does not grow with the input. Needs: limit-inferior, schonhage-strassen, n-log-n-conjecture, big-omega-notation. (600 words, used by 2)
- `binary-field`: [Binary field](binary-field.md) — The field with two elements 0 and 1, where addition is exclusive or and multiplication is AND. Needs: congruence-modulo. (377 words, used by 3)
- `modular-inverse`: [Modular inverse](modular-inverse.md) — An integer a has an inverse modulo q when some integer b makes ab congruent to 1 modulo q; this holds exactly when a and q are coprime. Needs: congruence-modulo, coprime, bezout-identity, cyclic-group, radix-digit-convolution. (597 words, used by 2)
- `binary-change-of-basis`: [Binary change of basis](binary-change-of-basis.md) — An invertible change of basis of the selected address bits over the binary field, realised by row additions on bit positions. Needs: linear-algebra-basics, binary-field, address-field. (327 words, used by 2)
- `bit-network`: [Bit network](bit-network.md) — A linear network whose wires carry bits over the binary field and which realises a binary change of basis. Needs: binary-change-of-basis, linear-network-frames. (871 words, used by 3)
- `phase-factor`: [Phase factor](phase-factor.md) — A complex number of modulus one, such as a power of i, multiplied into coefficients; a scalar correction is a fixed constant factor of this kind. Needs: ring, root-of-unity, network-gate-terminal. (422 words, used by 2)
- `gaussian-dyadics`: [Gaussian dyadics](gaussian-dyadics.md) — Complex numbers whose real and imaginary parts are integers divided by a power of two, with the Gaussian integer part also an integer. Needs: phase-factor, butterfly. (337 words, used by 6)
- `two-point-kernel`: [Two-point kernel](two-point-kernel.md) — The two-by-two operator aI + bX, with X the bit flip, applied along one direction of a binary address; its coefficients are Gaussian dyadics. Needs: linear-algebra-basics, gaussian-dyadics, phase-factor. (409 words, used by 2)
- `gaussian-integer`: [Gaussian integer](gaussian-integer.md) — A complex number whose real and imaginary parts are both integers. Needs: discrete-fourier-transform, two-point-kernel. (244 words, used by 1)
- `polynomial-ring`: [Polynomial ring](polynomial-ring.md) — The ring of polynomials in an indeterminate with complex coefficients, with the usual addition and multiplication, here reduced modulo a fixed polynomial. Needs: ring. (427 words, used by 2)
- `grid-numerator`: [Grid numerator](grid-numerator.md) — For a fixed precision, a grid value is an integer multiple of a fixed negative power of two, and its numerator is the integer multiplier. Needs: gaussian-dyadics, carry-propagation. (324 words, used by 1)
- `chinese-remainder-theorem`: [Chinese remainder theorem](chinese-remainder-theorem.md) — For pairwise coprime moduli, a system of congruences has a solution, unique modulo the product of the moduli. Needs: congruence-modulo, coprime. (561 words, used by 2)
- `cyclic-convolution`: [Cyclic convolution](cyclic-convolution.md) — The product of two sequences in which indices wrap around modulo the sequence length. Needs: chinese-remainder-theorem, modular-inverse. (668 words, used by 6)
- `ring-homomorphism`: [Ring homomorphism and isomorphism](ring-homomorphism.md) — A map between rings that preserves addition and multiplication; it is an isomorphism when it is also bijective, so that the two rings have the same structure. Needs: cyclic-convolution, linear-algebra-basics. (605 words, used by 1)
- `chinese-remainder-map`: [Chinese-remainder map](chinese-remainder-map.md) — A relabeling of coefficient positions by mixed-radix digits for pairwise coprime lengths, which turns one cyclic convolution into a multidimensional cyclic convolution. Needs: cyclic-convolution, radix-digit-convolution, mixed-radix-digits, ring-homomorphism. (980 words, used by 3)
- `forward-transform`: [Forward transform](forward-transform.md) — The discrete Fourier transform with the standard sign in its exponent, applied first in a convolution. Needs: discrete-fourier-transform. (348 words, used by 2)
- `pointwise-product`: [Pointwise product](pointwise-product.md) — The product of two sequences computed entry by entry, with each output entry the product of the two entries at that index. Needs: convolution, forward-transform, polynomial-ring-mod-yr-plus-1. (278 words, used by 1)
- `opposite-transform`: [Opposite transform](opposite-transform.md) — The discrete Fourier transform with the opposite sign in its exponent, which inverts the forward transform up to a normalizing factor. Needs: discrete-fourier-transform, frequency-domain, pointwise-product, array. (413 words, used by 3)
- `iverson-bracket`: [Iverson bracket](iverson-bracket.md) — The value 1 when a stated condition is true and 0 when it is false. (208 words, used by 1)
- `axis-line`: [Axis line](axis-line.md) — The set of entries of a multidimensional array that vary along one chosen axis while all other coordinates stay fixed. Needs: transform-axis. (247 words, used by 1)
- `near-linear-time`: [Near-linear time](near-linear-time.md) — A running time of the form n times a polylogarithmic factor in n, such as n log n or n (log n) squared. Needs: logarithm. (244 words, used by 1)
- `negacyclic-convolution`: [Negacyclic convolution](negacyclic-convolution.md) — A convolution in which indices that wrap around the sequence length pick up a minus sign. Needs: cyclic-convolution. (366 words, used by 1)
- `neumann-series`: [Neumann series](neumann-series.md) — The series of powers of an operator with alternating signs, which inverts I plus a small operator when that operator has norm below one. Needs: linear-algebra-basics, array-norm. (567 words, used by 1)
- `probability`: [Probability](probability.md) — A number between 0 and 1 assigned to each event, additive over disjoint events, with 1 for the certain event. (289 words, used by 1)
- `independence`: [Independence of events](independence.md) — Two events are independent when the probability that both occur equals the product of their probabilities. Needs: probability. (240 words, used by 1)
- `radix-two-factorization`: [Radix-two factorization](radix-two-factorization.md) — The factorization of a Fourier transform of length 2 to the power k into k levels of butterflies. Needs: butterfly, discrete-fourier-transform. (509 words, used by 1)
- `multidimensional-transform`: [Multidimensional transform](multidimensional-transform.md) — A Fourier transform over several axes at once, computed by transforming along each axis in turn. Needs: discrete-fourier-transform, transform-axis, cyclic-shift, radix-two-factorization, synthetic-transforms. (640 words, used by 3)
- `gaussian-resampling`: [Gaussian resampling](gaussian-resampling.md) — A technique that replaces a Fourier transform of arbitrary length by transforms whose axis lengths are powers of two, using Gaussian weights to move between the two sets of frequencies. Needs: discrete-fourier-transform, radix-digit-convolution, synthetic-transforms, multidimensional-transform, coprime, array-norm. (533 words, used by 5)
- `standard-basis-vector`: [Standard basis vector](standard-basis-vector.md) — A vector with entry 1 in one fixed coordinate and 0 in every other coordinate. Needs: linear-algebra-basics. (312 words, used by 1)
- `matrix-rank`: [Matrix rank](matrix-rank.md) — The number of linearly independent rows or columns of a matrix, taken over the rational numbers in the present context. Needs: linear-algebra-basics, linear-network-frames, standard-basis-vector. (558 words, used by 2)
- `symmetric-matrix`: [Symmetric matrix](symmetric-matrix.md) — A square matrix equal to its own transpose. Needs: linear-algebra-basics. (287 words, used by 1)
- `eigenvalue`: [Eigenvalue](eigenvalue.md) — A scalar λ for which a linear operator maps some nonzero vector v to λv. Needs: linear-algebra-basics, symmetric-matrix. (386 words, used by 2)
- `bilinear-form`: [Bilinear form](bilinear-form.md) — A bilinear map from a vector space and itself to its scalars; a space with such a form is nondegenerate when the form has no nonzero vector orthogonal to everything, and two vectors are orthogonal when the form vanishes on them. Needs: bilinear-map, linear-algebra-basics, eigenvalue, bit-network. (568 words, used by 7)
- `orthogonal-complement`: [Orthogonal complement](orthogonal-complement.md) — The set of all vectors that are orthogonal to every vector of a given subspace. Needs: bilinear-form. (253 words, used by 1)
- `indicator-vector`: [Indicator vector](indicator-vector.md) — The 0-1 vector whose entries mark which elements of a ground set belong to a given subset. Needs: ground-set, bilinear-form. (324 words, used by 3)
- `line-spanned-by-vector`: [Line spanned by a vector](line-spanned-by-vector.md) — The set of all scalar multiples of one nonzero vector, a one-dimensional subspace. Needs: linear-algebra-basics, bilinear-form, tensor-product, orthogonal-complement, linear-network-frames. (575 words, used by 1)
- `subspace-labels`: [Subspace labels](subspace-labels.md) — Nondegenerate subspaces of a fixed bilinear space attached to each wire of a network, whose inclusions control how much work a change of representation costs. Needs: bilinear-form, network-gate-terminal, gaussian-integer, ground-set, indicator-vector, line-spanned-by-vector, projection-along-subspace, bit-network, linear-functional. (797 words, used by 2)
- `subset-intersection-network`: [Subset-intersection network](subset-intersection-network.md) — A linear network on the three-element subsets of a ground set, whose wires carry scalars and whose gates combine them by intersection size, so that it swaps two banks while cancelling arbitrary scratch values. Needs: subspace-labels, linear-network-frames, bilinear-form, eigenvalue, dual-space. (1519 words, used by 6)
- `scratch-storage`: [Scratch storage](scratch-storage.md) — Auxiliary storage that a procedure may overwrite during its work but must restore to its starting contents, whatever those contents were. Needs: address-field, subset-intersection-network. (571 words, used by 2)
- `address-interchange`: [Address-field interchange](address-interchange.md) — A tape procedure that swaps two disjoint contiguous address fields of an array in time that grows like a power of the field width, rather than linearly. Needs: fixed-tape-model, linear-network-frames, scratch-storage. (600 words, used by 9)
- `xor`: [Exclusive or](xor.md) — The bitwise sum modulo 2 of two bits, which is 1 exactly when the bits differ. Needs: address-interchange, permutation, bit-network, network-gate-terminal. (320 words, used by 1)
- `gram-matrix`: [Gram matrix](gram-matrix.md) — The matrix whose entries are the values of a bilinear form on all pairs of a list of vectors. Needs: bilinear-form, linear-algebra-basics. (544 words, used by 1)
- `complex-phase-network`: [Complex phase network](complex-phase-network.md) — A subset-intersection network whose frame change on each edge is a product of two-point kernels aI + bX on Gaussian dyadic values. Needs: subset-intersection-network, gaussian-dyadics, subspace-labels, binary-field, tensor-product, gram-matrix. (1151 words, used by 1)
- `simultaneous-butterfly-layer`: [Simultaneous butterfly layer](simultaneous-butterfly-layer.md) — The tensor product of the two-point map H0 applied to several selected address bits at once, computed exactly in one pass rather than one axis at a time. Needs: complex-phase-network, gaussian-dyadics, address-interchange, discrete-fourier-transform, tensor-product, butterfly, transform-axis, truncation, binary-change-of-basis, two-point-kernel. (797 words, used by 5)
- `guard-width-bound`: [Guard-width bound](guard-width-bound.md) — An explicit number of extra fractional and integer bits that makes every intermediate coefficient of a butterfly layer exact, so that a single final truncation suffices. Needs: simultaneous-butterfly-layer, gaussian-dyadics, linear-contraction, tensor-product, little-o-notation, big-theta-notation. (684 words, used by 2)
- `numerical-layer`: [Numerical layer](numerical-layer.md) — A layer of the transform calculation in which a simultaneous butterfly is applied to a chosen set of selected axes. Needs: simultaneous-butterfly-layer, payload. (461 words, used by 1)
- `union-bound`: [Union bound](union-bound.md) — The probability that at least one of several events occurs is at most the sum of their probabilities; in counting form, the size of a union is at most the sum of the sizes. Needs: independence, address, guard-width-bound. (640 words, used by 1)
- `transform-round`: [Transform round](transform-round.md) — One step of a multidimensional transform in which a butterfly is applied on the participating axes at once, followed by the corresponding twiddle. Needs: multidimensional-transform, simultaneous-butterfly-layer. (615 words, used by 3)
- `tape-procedure`: [Tape procedure](tape-procedure.md) — A procedure that moves the contents of a Turing machine's tapes, such as the address fields of an array, in a bounded number of passes. Needs: address-interchange, transform-round. (412 words, used by 3)
- `stream`: [Stream](stream.md) — A sequence of records that a procedure reads or writes in order, one position at a time, on a tape. Needs: near-linear-time, tape-procedure, mixed-radix-digits, linear-network-frames. (532 words, used by 4)
- `bit-procedure`: [Bit procedure](bit-procedure.md) — The first tape procedure, which interchanges two address fields by a shear built from the bit network over the binary field. Needs: address-interchange, tape-procedure, running-time-cost, matrix-rank. (718 words, used by 2)
- `endpoint-operator`: [Endpoint operator](endpoint-operator.md) — The operator that a network realises on each role's array once all intermediate frames have cancelled, so that it depends only on the endpoint frames. Needs: linear-network-frames, bit-procedure, logical-array, subset-intersection-network, address-interchange. (520 words, used by 1)
- `address-shear`: [Address shear](address-shear.md) — The map that updates two address fields H, D to H + D, D, which is implemented by a small number of field interchanges. Needs: address-interchange, linear-network-frames, modular-inverse, linear-algebra-basics, matrix-rank, bit-procedure, endpoint-operator. (639 words, used by 1)
- `stable-radix-sort`: [Stable radix sort](stable-radix-sort.md) — Sorting by successive passes over key digits from least to most significant, each pass stable so that equal keys keep their earlier order. Needs: mathematical-induction, stream, base-two-logarithm, exceptional-set. (878 words, used by 3)
- `destination-rank`: [Destination rank](destination-rank.md) — The position a record takes in the final order after a move, given by its rank among the records in that order. Needs: stable-radix-sort, stream. (669 words, used by 2)
- `transform-identity`: [Transform identity with retained permutations](transform-identity.md) — The Gaussian resampling identity in which the source and target coordinate permutations are kept as part of the formula, so that they cancel across a convolution instead of being executed as sorts. Needs: gaussian-resampling, congruence-modulo, coprime, linear-algebra-basics, opposite-transform, bijection, diagonal-scaling, stable-radix-sort, neumann-series. (637 words, used by 5)
- `transform-layout`: [Transform layout](transform-layout.md) — A permutation of address bits that places the selected bits of all participating axes at a common offset in consecutive chunks, so that a simultaneous butterfly layer applies to each transform round. Needs: address-interchange, simultaneous-butterfly-layer, synthetic-transforms, opposite-transform, permutation, polynomial-ring, forward-transform, transform-identity, transform-axis, address. (717 words, used by 2)
- `padded-transform-box`: [Padded transform box](padded-transform-box.md) — The full array of transform entries after every axis has been padded to its chosen length, with zero entries outside the valid region. Needs: multidimensional-transform, transform-identity, radix-digit-convolution, axis-line. (548 words, used by 3)
- `cyclic-coordinate`: [Cyclic coordinate](cyclic-coordinate.md) — One of the axes of a multidimensional cyclic convolution, with its own cyclic length. Needs: cyclic-convolution, padded-transform-box. (380 words, used by 2)
- `prime-number`: [Prime number](prime-number.md) — An integer greater than one whose only positive divisors are one and itself. Needs: integer, chinese-remainder-map, radix-digit-convolution, cyclic-coordinate. (258 words, used by 1)
- `logical-bit-volume`: [Logical bit volume](logical-bit-volume.md) — The number of bits in a padded transform box, counting every entry of the box at its record width. Needs: padded-transform-box. (182 words, used by 2)
- `cost-table`: [Cost table](cost-table.md) — The list of separate running-time terms of an algorithm, each a power of the input size, whose sum bounds the total time. Needs: running-time-cost, transform-layout, destination-rank, transform-round, chinese-remainder-theorem, gaussian-resampling, logical-bit-volume. (976 words, used by 2)
- `established-multiplier`: [Established O(n log n) multiplier](established-multiplier.md) — The known fixed-tape integer multiplier running in O(n log n) time, used here only as a black-box subroutine. Needs: exact-integer-multiplication, cost-table. (241 words, used by 1)
- `signed-packing`: [Signed coefficient packing](signed-packing.md) — Encoding polynomial coefficients, including negative ones, as one large integer by fixed-width blocks, so that polynomial multiplication becomes integer multiplication. Needs: established-multiplier, polynomial-ring, congruence-modulo. (624 words, used by 2)
- `schoolbook-multiplication`: [Schoolbook multiplication](schoolbook-multiplication.md) — Multiplication of two integers digit by digit by the grade-school method, which takes quadratic time in the number of digits. Needs: exact-integer-multiplication, logical-bit-volume. (441 words, used by 1)
- `centered-residue`: [Centered residue](centered-residue.md) — The representative of a residue class modulo B that lies in the interval from −B/2 to B/2, used to recover a signed coefficient. Needs: congruence-modulo, signed-packing. (313 words, used by 1)
- `polynomial-ring-convolution`: [Convolution over the polynomial ring](polynomial-ring-convolution.md) — The normalized product of two arrays of records in the polynomial ring, computed by two forward synthetic transforms, a pointwise product, and an opposite transform. Needs: polynomial-ring-mod-yr-plus-1, synthetic-transforms, signed-packing, centered-residue, carry-propagation, transform-axis, fixed-width-digit-blocks. (835 words, used by 2)
- `normalized-cyclic-convolution`: [Normalized cyclic convolution](normalized-cyclic-convolution.md) — A cyclic convolution divided by the transform length, the normalization for which a Fourier transform turns convolution into pointwise product. Needs: cyclic-convolution, discrete-fourier-transform, transform-identity, gaussian-resampling, root-of-unity. (552 words, used by 2)
- `bluestein-chirp-identity`: [Bluestein's chirp identity](bluestein-chirp-identity.md) — An identity that rewrites a Fourier transform as a cyclic convolution multiplied by chirp factors, so that it can be computed with convolution. Needs: discrete-fourier-transform, cyclic-convolution, transform-identity, normalized-cyclic-convolution, logarithm, negacyclic-convolution. (661 words, used by 2)
- `normalization-scales`: [Normalization scales](normalization-scales.md) — The known powers of two and transform lengths by which a computed product is multiplied to undo the normalizing factors of the transforms and the digit scaling. Needs: normalized-cyclic-convolution. (708 words, used by 1)
- `middle-transform`: [Middle transform](middle-transform.md) — The transform on the target lengths that sits between the two Gaussian resampling maps, which Bluestein's identity turns into a cyclic convolution. Needs: gaussian-resampling, bluestein-chirp-identity. (428 words, used by 1)
- `phase-twist`: [Phase twist](phase-twist.md) — A coefficientwise multiplication by roots of unity that converts the last cyclic coordinate into a polynomial ring, so its wrap-around becomes the negative wrap of that ring. Needs: bluestein-chirp-identity, polynomial-ring-mod-yr-plus-1, cyclic-coordinate, middle-transform. (557 words, used by 2)
- `prime-source-lengths`: [Prime source lengths](prime-source-lengths.md) — Distinct odd primes chosen close to the powers of two that are the padded axis lengths, so that their product fills a fixed fraction of the padded box. Needs: chinese-remainder-map, gaussian-resampling, mixed-radix-digits, coprime, prime-number. (916 words, used by 2)
- `recovery-and-error`: [Exact coefficient recovery](recovery-and-error.md) — The error analysis showing that the computed convolution coefficients are within a half of their true integer values, so rounding recovers them exactly. Needs: polynomial-ring-convolution, guard-width-bound, phase-twist, array-norm, bilinear-map, opposite-transform, padded-transform-box, prime-source-lengths, little-o-notation, normalization-scales, grid-numerator, complex-disk. (905 words, used by 1)
- `schedule`: [Schedule](schedule.md) — An ordered sequence of tape procedures applied one after another; the inverse schedule applies the inverses in reverse order. Needs: tape-procedure. (228 words, used by 1)
- `bit-construction`: [Bit construction](bit-construction.md) — The construction of a subset-intersection network whose scalars lie in the binary field, with neighbours chosen by intersection size one. Needs: indicator-vector, binary-field, subset-intersection-network, iverson-bracket, schedule. (981 words, used by 2)
- `complex-construction`: [Complex construction](complex-construction.md) — The construction of a subset-intersection network whose scalars are Gaussian dyadics, with neighbours chosen among distinct triples. Needs: indicator-vector, gaussian-dyadics, subset-intersection-network, bit-construction. (734 words, used by 1)
- `rank-saving-recursion`: [Rank-saving recursion](rank-saving-recursion.md) — The recursion in which each call splits into s smaller calls on streams of 1/W of the volume, where s < W m, so that the cost grows by the strictly smaller factor s/W per level. Needs: subset-intersection-network, address-interchange, numerical-layer, stream, incidence, complex-construction, bit-construction, bilinear-form. (910 words, used by 2)
- `family-parameter`: [Family parameter](family-parameter.md) — A parameter that indexes a family of constructions and controls their sizes. Needs: rank-saving-recursion. (275 words, used by 1)
- `packed-bit-addition`: [Packed selected-bit addition](packed-bit-addition.md) — An operation that adds one selected bit position across several address chunks at once, using cyclic shifts and a small deterministic correction for exceptional addresses. Needs: simultaneous-butterfly-layer, address-interchange, address-shear, cyclic-shift, xor, address-field, scratch-storage, transform-round, cost-table, union-bound, stable-radix-sort, destination-rank, payload, stream, family-parameter. (1128 words, used by 1)
- `main-theorem`: [Integer multiplication below n log n](main-theorem.md) — A deterministic fixed-tape machine that multiplies two n-bit integers exactly in O(n (lg n)^(1−κ)) time with κ = 2^−182, which disproves the n log n optimality conjecture in this model. Needs: n-log-n-conjecture, fixed-tape-model, radix-digit-convolution, chinese-remainder-map, rank-saving-recursion, transform-layout, transform-identity, prime-source-lengths, phase-twist, polynomial-ring-convolution, packed-bit-addition, recovery-and-error, carry-propagation, schoolbook-multiplication, running-time-cost, logarithm. (1166 words, used by 0)

## The argument's main steps

- Exact multiplication of two $n$-bit integers reduces to a convolution of short integer coefficients obtained by splitting each input into radix digits. Pages: `radix-digit-convolution`.
- The Fourier transforms of this convolution are replaced by multidimensional transforms whose axis lengths are powers of two. Pages: `gaussian-resampling`.
- After a further conversion to convolution, one coordinate of the array is stored as the coefficient list of a polynomial modulo $y^r + 1$, with $r$ a power of two. Pages: `polynomial-ring-mod-yr-plus-1`.
- The transforms are synthetic polynomial transforms whose roots of unity are powers of $y$. Pages: `synthetic-transforms`.
- Two disjoint contiguous address fields of $u$ bits in an array can be interchanged in $O(V u^{\tau})$ time for a fixed $\tau<1$, where $V$ is the stored bit volume. Pages: `address-interchange`.
- A butterfly layer on the selected coordinate bits of several axes is applied at once, in a single tape procedure. Pages: `simultaneous-butterfly-layer`.
- Each tape procedure is a fixed linear network that exchanges two banks of values and restores its scratch values. Pages: `linear-network-frames`.
- A linear network on the three-element subsets of a ground set exchanges two banks of values and restores its scratch wires. Pages: `subset-intersection-network`.
- The total number $s$ of smaller calls satisfies $s < Wm$, so each recursive level saves a strict power. Pages: `rank-saving-recursion`.
- The radix-digit coefficients are placed on distinct prime cyclic axes by a Chinese-remainder map that preserves convolution. Pages: `chinese-remainder-map`.
- Gaussian resampling expresses each source Fourier transform through a power-of-two tensor transform, with the source and target coordinate permutations kept in the transform identity. Pages: `transform-identity`.
- The middle transform, including its target permutation, becomes a normalized cyclic convolution. Pages: `bluestein-chirp-identity`.
- A phase twist turns the last cyclic coordinate into a coordinate of the polynomial ring modulo $y^r + 1$. Pages: `phase-twist`.
- Convolution on the remaining axes over the polynomial ring is computed by two forward synthetic transforms, a pointwise product, an opposite transform, and packed integer products. Pages: `polynomial-ring-convolution`.
- The recovered coefficient error is strictly below $1/2$, so rounding returns the exact integer coefficients. Pages: `recovery-and-error`.
- Carries across the radix digits turn the recovered integer coefficients into the exact binary product. Pages: `carry-propagation`.
- The parameters can be chosen so that every term in the cost table is $O(n(\lg n)^{1-\kappa})$ for $\kappa = 2^{-182}$, which gives the bound of the theorem.

The page bodies are in `exegenius/pages/<id>.md`; read them if the glosses are not enough to write the overview.

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Part": {
      "additionalProperties": false,
      "properties": {
        "intro": {
          "description": "What the part covers and why the reader needs it, as markdown.",
          "type": "string"
        },
        "pages": {
          "description": "Ids of the pages in this part.",
          "items": {
            "type": "string"
          },
          "type": "array"
        },
        "title": {
          "description": "Short title, plain text, no numbering.",
          "type": "string"
        }
      },
      "required": [
        "title",
        "intro",
        "pages"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "glossary": {
      "default": [],
      "description": "Ids of minor pages to move to the glossary.",
      "items": {
        "type": "string"
      },
      "type": "array"
    },
    "overview": {
      "description": "The front page, as markdown, with no headings.",
      "type": "string"
    },
    "parts": {
      "description": "The parts, in reading order.",
      "items": {
        "$ref": "#/$defs/Part"
      },
      "type": "array"
    }
  },
  "required": [
    "overview",
    "parts"
  ],
  "title": "OutlineAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0616-outline.answer.json`, then run `exegenius submit 0616-outline` in the project directory. If submit rejects the answer, fix the answer and submit again.
