# exegenius task 0209-audit-simultaneous-layer

Project directory: `/home/user/e2e-run` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file and the paper at `sources/paper.tex`: do not read other pages or any other file.

The reader knows the concepts listed as known, and everything the reader profile covers: what anyone with that background has been taught, whether or not the profile names it (a profile of undergraduate computer science covers logarithms and proof by induction without naming them). Anything outside that, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: report what would stop this reader at this point on the page. A term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. A claim marked "(cited)" is attributed to the source. A citation lets the reader check a result, not follow an argument: a cited result the page uses is followable if the page says what it states and why it applies where it is used, and its proof can be left to the source. A cited claim that stands in for how the page's own concept works, or whose content or role the page does not say, is a step.
- term: a named concept the reader does not know, which the page neither explains nor links. References to the documents themselves (the paper, the sources, the target result) are not terms.
- step: an inference, calculation or claim that the page presents as following from what it gives, which the reader cannot check from what the page gives. A claim about an identity, construction or definition that the page never states is a step.

Fidelity: also check that the page's mathematics is right, and report what is wrong even where this reader could follow it. For each claim that states a definition, a hypothesis, a step of a proof, a value or a conclusion, work out what it assumes and what it concludes, and check it against everything this task file gives: the page's definitions, its other claims and its quotations. Report as a `step` any claim that is false, inconsistent with another statement on the page, stated more strongly or more widely than what supports it, or missing a hypothesis it needs. Quote the claim, and say in the note what is wrong and what the correct statement is.

The source: the paper this page explains is at `sources/paper.tex` (LaTeX). For each such claim, also find the passage of the paper that states, defines or proves it (search the file for the claim's terms and symbols, then read the passage around each match) and compare: every hypothesis present, the same scope and quantifiers, the same constants, signs, exponents and inequality directions, a conclusion no stronger than the paper's, and the right result, lemma or author credited. Report any mismatch as a `step` in the same way, and give the paper's line number in the note.

What counts as an error: report a claim as wrong only if, as this page states it, it is false; inconsistent with the page; stated more strongly or more widely than what supports it; missing a hypothesis without which it is false; given a wrong value, sign, exponent, constant, quantifier or credit; or presented as following from something it does not follow from. Do not report a correct statement as wrong because it is informal, abbreviated or simplified, uses a word in the paper's own sense, or leaves a technical precondition to another page or to the paper. If the paper's own summary of the same step states it the same way, it is not an error.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is a computer science undergraduate: they have taken discrete mathematics, an algorithms course (asymptotics, divide and conquer, schoolbook and Karatsuba multiplication, sorting), a first linear algebra course (vector spaces, subspaces, dimension, rank, matrices as linear maps, inverses, triangular matrices, orthogonality, bilinear forms at a basic level), calculus, elementary number theory (primes, gcd, modular arithmetic) and basic machine-level binary representation (XOR, two's complement). They have seen Turing machines with tapes only at an introductory level. They have not been taught the discrete Fourier transform or FFT as such, abstract algebra beyond basic definitions (quotient rings, finite fields as a theory), tensor products, numerical error analysis, or the specific literature on fast integer multiplication.

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes
- Fixed finite-tape machine model (also: multitape Turing machine, fixed-tape model)
- Elementary stream operations
- Controlled shifts and rational scalings
- Schönhage–Strassen optimality conjecture (also: n log n conjecture)
- Established O(n log n) multiplier
- Cyclic convolution
- Multiplication as radix-digit convolution
- Discrete Fourier transform (also: Fourier transform, DFT)
- Butterflies and the fast transform (also: transform levels)
- Multidimensional transforms
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Gaussian resampling
- Bluestein chirp identity (also: chirp transform)
- Retained permutation cancellation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Retained frequency order
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records (also: Z[i,1/2])
- Error tracking and exact recovery (also: synthetic transform error, source transform error)
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange, costly recursive primitive)
- Two-point kernel C (also: phase network kernel)
- Binary phase frames
- Packed selected-bit addition (also: exceptional addresses)
- Parameter and prime-length choice
- Schoolbook and Karatsuba multiplication (also: long multiplication, grade-school multiplication, Karatsuba, O(n^2) multiplication, n^{log_2 3} multiplication)
- Divide-and-conquer recurrences (also: master theorem, recurrence relations, recursion tree)
- Binary and radix representation (also: base-b digits, positional notation, binary expansion, bit string, most significant bit, padding with leading zeros, carry propagation)
- Two's complement integers (also: two's-complement, signed binary integers, signed fixed-width addition)
- Bitwise XOR and arithmetic mod 2 (also: XOR, exclusive or, addition in F_2, GF(2), parity, bit flip)
- Logarithms and floors/ceilings (also: lg, log base 2, ceiling, floor, iterated logarithm, log log n)
- Modular arithmetic and primes (also: congruence, residues mod n, gcd, coprime, relatively prime, prime numbers, Z/nZ, modular inverse, units mod n)
- Roots of unity (also: nth roots of unity, primitive root of unity, e^{2 pi i/n}, Euler's formula)
- Vector spaces, subspaces, dimension and rank (also: linear subspace, basis, span, linear independence, dimension, matrix rank, kernel, linear map, linear operator, direct sum)
- Matrices and linear operators (also: matrix multiplication, invertible matrix, matrix inverse, identity matrix, commuting operators, diagonal matrix, triangular matrix, lower triangular, permutation matrix)
- Gaussian elimination and triangular factorization (also: row reduction, LU decomposition, back substitution)
- Orthogonality and inner products (also: orthonormal basis, dot product, orthogonal complement, bilinear form, nondegenerate form, Euclidean norm)
- Norms and the triangle inequality (also: sup norm, max norm, infinity norm, modulus bounds, absolute value bounds)
- Permutations and bijections (also: permutation of indices, sorting a permutation, bit-reversal permutation, bijective map, inverse permutation)
- Cartesian products and multi-index arrays (also: multidimensional arrays, row-major order, lexicographic order, mixed-radix index, index tuples, array stored on a tape, rectangle, columns)
- Directed acyclic graphs and networks of gates (also: circuit, DAG, wire, gate, edges and vertices, fan-in)
- Summation, geometric series and induction (also: geometric sum, proof by induction, summation notation, telescoping sum)
- Rounding to the nearest integer and exactness (also: rounding, truncation, round to nearest, rational numbers, dyadic rational)
- Multitape Turing machine running time (also: tape head movement, scanning a tape, linear-time pass over a tape, time complexity of a Turing machine, worst-case running time)
- Integer exponentials and tuple notation (also: powers of two, tensor power notation, exponent of a constant, fixed rational exponents)
- Contractions and bilinear contractions (also: contraction, bilinear contraction)
- Tensor products of subspaces (also: tensor product of subspaces, tensor product)

## Symbols bound on earlier pages

- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the grid on which stored values lie.
- $\Delta$ (reserved extra bits), bound on `fixed-point`: The number of extra bits reserved, at least the maximal depth reached in the layer.
- $Q_p$ (truncation), bound on `fixed-point`: The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $h$ (ground-set size), bound on `exchange-network`: The size of the ground set [h] whose three-element subsets index the data.
- $v$ (number of triples), bound on `exchange-network`: The number of three-element subsets of [h].
- $X$ (bank X), bound on `exchange-network`: The first data bank, with entries X_a.
- $a$ (bank index), bound on `exchange-network`: A triple of three-element subsets of [h] indexing the bank entries (not a shift exponent here).
- $m$ (label dimension), bound on `exchange-network`: The dimension of the label space used on later pages.
- $S$ (slice index), bound on `exchange-network`: A three-element subset of [h]: the varying coordinate of a within a slice.
- $\sigma$ (initial side values), bound on `exchange-network`: The initial values of the side wires.
- $I$ (number of invocations), bound on `exchange-network`: The number of invocations in the three stages.
- $q$ (sequence length), bound on `convolution`: The number of entries in each of the two sequences being convolved.
- $d$ (axis count), bound on `convolution`: The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $v$ (second input), bound on `radix-digit-reduction`: The second of the two integers being multiplied.
- $b$ (digit width), bound on `radix-digit-reduction`: The number of bits in one radix digit.
- $S$ (convolution length), bound on `radix-digit-reduction`: The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $q$ (digit count), bound on `radix-digit-reduction`: The number of radix-2^b digits in each input.
- $x$ (polynomial variable), bound on `radix-digit-reduction`: The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $f$ (first array), bound on `phase-twist`: The first complex array being convolved.
- $g$ (second array), bound on `phase-twist`: The second complex array being convolved with f.
- $d$ (axis count), bound on `phase-twist`: The number of axes of the arrays.
- $\Theta$ (twist map), bound on `phase-twist`: The ring isomorphism from the cyclic ring to the negacyclic ring sending x_d to zeta y.
- $l$ (second coefficient index), bound on `phase-twist`: An index of a coefficient of the second factor.
- $j$ (wrapped position), bound on `phase-twist`: The position k+l reduced modulo r.
- $h$ (wrap indicator), bound on `phase-twist`: Zero or one according to whether k+l wrapped past r.
- $q$ (sequence length), bound on `dft`: The number of entries of a sequence.
- $m$ (output index), bound on `butterfly`: The index of an output of the transform.
- $b$ (lowest bit), bound on `butterfly`: The lowest bit of the output index m.
- $h$ (remaining index), bound on `butterfly`: The output index m with its lowest bit removed.
- $e$ (two-adic exponent), bound on `synthetic-transform`: The exponent of 2 in j when j is written as 2^e times an odd number.
- $V$ (array volume), bound on `stream-ops`: The number of radix-q digits an array stores.
- $q$ (radix), bound on `stream-ops`: The number of values one digit can take.
- $P$ (prefix values), bound on `stream-ops`: The number of prefix values indexing the first axis of the array.
- $B$ (entries per row), bound on `stream-ops`: The number of entries in each row.
- $W$ (stream count), bound on `stream-ops`: The fixed number of streams the rows are dealt into.
- $Q$ (target permutation), bound on `chirp`: The permutation reordering the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $a$ (chirp), bound on `chirp`: The chirp, a phase quadratic in the index.
- $a$ (round count), bound on `frequency-order`: The number of rounds of the transform, a=log_2 t.
- $j$ (output index), bound on `frequency-order`: The position of an output of the transform.
- $s$ (completed rounds), bound on `frequency-order`: The number of rounds completed so far.
- $\mathcal H$ (parallel butterfly), bound on `frequency-order`: The parallel butterfly applying H_0 on every participating axis in one round.
- $q$ (prime modulus base), bound on `controlled-shifts`: A fixed prime; on this page it is not a sequence length.
- $b$ (field digit count), bound on `controlled-shifts`: The number of base-$q$ digits of a field.
- $Q$ (field value count), bound on `controlled-shifts`: The number of values a field can take, q^b.
- $a$ (offset), bound on `controlled-shifts`: The offset in [Q] added to the target field, prepared from the control values.
- $B$ (suffix bit count), bound on `controlled-shifts`: The number of bits following the target field.
- $j$ (wrap count), bound on `controlled-shifts`: The integer part of cy/Q, counting how often cy wraps past Q.
- $m$ (fields per group), bound on `matrix-shear`: The number of fields in each of the groups H and D.
- $a$ (rank of A), bound on `matrix-shear`: The rank of the rational matrix A.
- $A$ (shear matrix), bound on `matrix-shear`: A rational m by m matrix, taken from a fixed finite set, that the shear applies.
- $H$ (target group), bound on `matrix-shear`: The first group of m fields, which receives AD.
- $D$ (source group), bound on `matrix-shear`: The second group of m fields, which is left unchanged by the shear.
- $a$ (kernel coefficient a), bound on `phase-kernel`: The complex constant (1+i)/2, the coefficient of the identity in C.
- $b$ (kernel coefficient b), bound on `phase-kernel`: The complex constant (1-i)/2, the coefficient of the bit flip in C.
- $I$ (identity matrix), bound on `phase-kernel`: The 2 by 2 identity matrix.
- $X$ (bit flip), bound on `phase-kernel`: The 2 by 2 matrix swapping the two entries of a pair.
- $C$ (two-point kernel), bound on `phase-kernel`: The 2 by 2 matrix aI+bX.
- $\mathsf S$ (phase matrix), bound on `phase-kernel`: The diagonal matrix diag(1,i) multiplying the second entry of a pair by i.
- $H$ (normalized Hadamard matrix), bound on `phase-kernel`: The matrix sqrt(2) H_0, symmetric with H squared equal to the identity.
- $H_0$ (two-point butterfly), bound on `phase-kernel`: The matrix (1/2)[[1,1],[1,-1]] of the averaging and differencing step on a pair.
- $f$ (first operand), bound on `contraction-maps`: The first operand of the bilinear map.
- $g$ (second operand), bound on `contraction-maps`: The second operand of the bilinear map.
- $i$ (axis index), bound on `multidim-transform`: The index of an axis of the array, from 1 to d.
- $j$ (index tuple), bound on `multidim-transform`: The tuple of coordinates (j_1,...,j_d) of an entry of the array.
- $Q$ (padded permutation), bound on `multidim-transform`: The tensor product of the index permutations P_{t_i}.
- $S$ (convolution length), bound on `crt-map`: The length of the cyclic convolution, the product of the s_i.
- $d$ (number of axes), bound on `crt-map`: The number of axes of the target ring.
- $i$ (axis index), bound on `crt-map`: The index of an axis, from 1 to d.
- $\ell$ (address bits), bound on `crt-map`: The base-2 logarithm of the record length r, the number of address bits of a full-width axis.
- $V$ (stream volume), bound on `crt-map`: The volume of the stream being moved, Tp bits.
- $\tau$ (chunk-swap exponent), bound on `crt-map`: A fixed exponent below 1 in the cost of a chunk interchange.
- $s$ (source length), bound on `gaussian-resampling`: The length of the Fourier transform to be replaced.
- $C$ (coordinate selection), bound on `gaussian-resampling`: The map from C^t to C^s that selects coordinate q_j into position j.
- $z$ (vector), bound on `retained-permutations`: A vector of q complex entries being transformed.
- $h$ (summation index), bound on `retained-permutations`: The index of summation in the Fourier sum, substituted by ck.
- $g$ (setup degree), bound on `retained-permutations`: A fixed exponent such that setup work per line is O(p^g).
- $v$ (second array), bound on `retained-permutations`: A complex array (not an integer) in the resampling and convolution identities of this page.
- $v$ (scaled digit array), bound on `precision-recovery`: The array of scaled radix digits of the second input (not the integer).
- $j$ (coefficient index), bound on `precision-recovery`: The index of the product coefficient being processed during carry propagation.
- $\tau$ (chunk-interchange exponent), bound on `parameter-choice`: The exponent in the cost of a chunk interchange.
- $\sigma$ (recursion growth exponent), bound on `parameter-choice`: An exponent bounding the growth of the number of recursive calls.
- $\beta$ (active-chunk threshold exponent), bound on `parameter-choice`: The exponent in the threshold d^beta below which active chunks are handled singly.
- $\lambda$ (overhead exponent), bound on `parameter-choice`: The per-node overhead exponent.
- $\lambda'$ (final cost exponent), bound on `parameter-choice`: The final exponent of the cost V d^lambda' on bit volume V.
- $V$ (bit volume), bound on `parameter-choice`: The number of bits of the logical array the layer acts on.
- $\epsilon$ (axis-count exponent), bound on `parameter-choice`: The exponent of the axis count.
- $C_1$ (guard-bit exponent), bound on `parameter-choice`: The exponent of the guard bits.
- $K$ (chunk width), bound on `parameter-choice`: The width in bits of an address chunk.
- $\eta$ (prime window offset), bound on `parameter-choice`: The smallest relative distance at which a prime s_i may lie below t_i.
- $E$ (first space), bound on `tensor-product-of-spaces`: The first of the two finite-dimensional vector spaces being tensored.
- $G$ (second space), bound on `tensor-product-of-spaces`: The second of the two finite-dimensional vector spaces being tensored.
- $A$ (ambient space), bound on `tensor-product-of-spaces`: A finite-dimensional space with a nondegenerate form, containing the subspace P.
- $C$ (second ambient space), bound on `tensor-product-of-spaces`: A finite-dimensional space with a nondegenerate form, containing the subspace Q.
- $P$ (subspace of A), bound on `tensor-product-of-spaces`: A subspace of A, later taken nondegenerate.
- $Q$ (subspace of C), bound on `tensor-product-of-spaces`: A subspace of C.
- $B$ (orthogonal complement), bound on `tensor-product-of-spaces`: The orthogonal complement of P in A.
- $F$ (base space), bound on `tensor-product-of-spaces`: A space of dimension h with a nondegenerate form, whose triple power is the label space.
- $s$ (number of smaller calls), bound on `subspace-labels`: The total number of smaller calls that the edges of the network cost.
- $W$ (wire count), bound on `subspace-labels`: The number of wires of the network under consideration.
- $F$ (one-factor label space), bound on `subspace-labels`: The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $x$ (vector of F), bound on `subspace-labels`: A vector of $F$, the first argument of the bilinear form.
- $X$ (X bank), bound on `subspace-labels`: The bank of data wires $X_a$.
- $j$ (stage number), bound on `subspace-labels`: The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
- $A$ (exposed factor space), bound on `subspace-labels`: The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
- $P$ (earlier tensor line), bound on `subspace-labels`: The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on `subspace-labels`: The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on `subspace-labels`: The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $V$ (larger label), bound on `subspace-labels`: A label containing the label $U$ at the other end of an edge.
- $m$ (label dimension), bound on `rank-recurrence`: The dimension of the label space, 10^6, which is also the number of slots a chunk is split into, so a parameter grows by the factor m per recursion level.
- $s$ (number of smaller calls), bound on `rank-recurrence`: The number of calls at parameter f that one call at parameter mf makes, equal to the total rank of the frame changes over the network's edges.
- $f$ (call parameter), bound on `rank-recurrence`: The size parameter of a call: the number of digits in each interchanged chunk, or the number of selected axes of a layer.
- $F$ (time per unit volume), bound on `rank-recurrence`: The running time of a call at a given parameter divided by the volume of its stream.
- $j$ (recursion depth), bound on `rank-recurrence`: The number of recursion levels between the top call and a given call.
- $\eta$ (relative deficit), bound on `rank-recurrence`: The relative rank deficit (Wm - s)/(Wm) of a network, the fraction by which the number of smaller calls falls short of Wm.
- $V$ (array volume), bound on `address-interchange`: The number of bits stored in the array.
- $\tau$ (saving exponent), bound on `address-interchange`: The fixed exponent below 1 in the cost, equal to 1 - 2^{-50}.
- $p$ (prefix), bound on `address-interchange`: The part of an address before the first chunk.
- $h$ (first chunk), bound on `address-interchange`: The first of the two address chunks being interchanged.
- $g$ (gap), bound on `address-interchange`: The part of an address between the two chunks.
- $d$ (second chunk), bound on `address-interchange`: The second of the two address chunks being interchanged.
- $z$ (suffix), bound on `address-interchange`: The part of an address after the second chunk.
- $q$ (digit radix), bound on `address-interchange`: The fixed prime that is the radix of the digits.
- $e$ (chunk digit count), bound on `address-interchange`: The number of radix-q digits in a chunk.
- $i$ (edge index), bound on `address-interchange`: The index of an edge of the network.
- $x$ (stream row), bound on `address-interchange`: The row number within a role stream.
- $j$ (recursion level), bound on `address-interchange`: The index of a recursion level in the unrolled recurrence.
- $\nu$ (high digit count), bound on `address-interchange`: The number of top digits of each chunk set aside to form the row field.
- $v$ (binary vector), bound on `phase-frames`: A vector of F_2^m; in the main argument a basis vector of an edge residual. Here v does not mean the triple count.
- $X_v$ (translation), bound on `phase-frames`: The operator shifting an array by the vector v: (X_v f)(x)=f(x+v).
- $E$ (edge residual), bound on `phase-frames`: The subspace added to U to reach V, orthogonal to U; here E is not the first space of a tensor product.
- $Z$ (sign matrix), bound on `phase-frames`: The diagonal matrix diag(1,-1).
- $K$ (segment spacing), bound on `packed-bit-addition`: The spacing between selected positions, at least 6, which is the length of each segment.
- $f$ (selected bit count), bound on `packed-bit-addition`: The number of selected bits per chunk.
- $g$ (guard value), bound on `packed-bit-addition`: The guard value of a segment, any g_i or h_i: its high K-1 bits.
- $q$ (address), bound on `packed-bit-addition`: An address of a record after S_0; q' is its destination T_0 S_0^{-1}(q).

## Pages in the wiki

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Elementary stream operations](stream-ops.md)
- [Bluestein chirp identity](chirp.md)
- [Retained frequency order](frequency-order.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Two-point kernel C](phase-kernel.md)
- [Contractions and bilinear contractions](contraction-maps.md)
- [Multidimensional transforms](multidim-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [Tensor products of subspaces](tensor-product-of-spaces.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Binary phase frames](phase-frames.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Page to audit (`simultaneous-layer`)

````markdown
# Simultaneous butterfly layer

The simultaneous butterfly layer applies $H_0$ coefficientwise to one bit of each of $D\le d$ selected address chunks of $K$ bits, at a common offset, in time $O(Vd^{\lambda'}),$ $\lambda'<1,$ instead of $D$ passes.

With $\mathsf S=\operatorname{diag}(1,i),$ the [Two-point kernel C](phase-kernel.md) $C=aI+bX$ satisfies $H_0=b\,\mathsf SC\mathsf S,$ $C^2=X$ and $C^4=I$ (cited). With $x_1,\dots,x_D$ the selected bits of an address $x,$ this gives $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D,$ where the diagonal operator $\mathcal S_D$ acts on an array $z$ by $(\mathcal S_Dz)(x)=i^{x_1+\dots+x_D}z(x).$ Phases and $b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}$ are exact Gaussian dyadic, leaving $C^{\otimes D}.$

A group of $e=mf$ axes has $m$ slots of $f$ axes; a column holds one bit per slot, in $\mathbb F_2^m.$ $C^{\otimes e}$ is computed by the network of [Binary phase frames](phase-frames.md), with $W$ wires and $s$ smaller calls. Each edge changes the frame on every column by $\prod_hC_{v_h}^{\eta_h},$ with residual basis vectors $v_h$ indexed by $h,$ $\eta_h=\pm1,$ $C_v=aI+bX_v$ and $X_v$ shifting a column by $v.$ Let $G$ be an invertible $\mathbb F_2$-matrix with first columns $v_h$ and $\mathcal P_G:x\mapsto Gx$ an address permutation. Then $\mathcal P_GX_v\mathcal P_G^{-1}=X_{Gv}$ (cited), so the edge change is $\mathcal P_G(\prod_hC_{e_h}^{\eta_h})\mathcal P_G^{-1},$ $e_h$ the $h$-th standard basis vector. Apply $\mathcal P_G^{-1},$ then $(C^{\eta_h})^{\otimes f}$ to the $f$ bits of slot $h,$ then $\mathcal P_G:$ one child on $f=e/m$ axes per residual vector, exactly $s$ in all. Negative powers add no child: $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f}$ with $Z=\operatorname{diag}(1,-1).$

Elimination writes $G$ as at most $m(m-1)+3m$ row additions (a swap is three). Each XORs selected bits of one slot into another; [Packed selected-bit addition](packed-bit-addition.md) XORs selected bits by cyclic shifts of whole chunk ranges plus a repair of exceptional addresses. Their number is fixed, so the basis change and its inverse on $e$ axis chunks cost $O(V((eK)^\tau+1))$ (cited) $(\tau<1)$ on a stream of volume $V.$

Rows go to the $W$ wire roles by index mod $W,$ so children have volume $V/W$ if the row count stays divisible by $W$ through $\lceil\log_md\rceil$ levels. So the first $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ chunks get individual $C$ kernels, in $O(V\log d),$ and their bits form a row index of range at least $W^{\lceil\log_md\rceil}.$ Zero rows pad each block to a multiple of that, making the row count at depth $j$ divisible by $W^{\lceil\log_md\rceil-j};$ fewer rows are added than the block holds, so the volume at most doubles. With $\beta=\tfrac12$ and $F(e)$ the time divided by volume,
$$F(e)\le \tfrac sW F(e/m)+O((eK)^\tau+1)\ (e\ge d^\beta),\qquad F(e)=O(e)\ (e<d^\beta),$$
the recursion of [Recursive power saving](rank-recurrence.md). As $s/W\le m^\sigma,$ $\sigma<1,$ internal levels sum geometrically, leaves add $O(e^\sigma d^{\beta(1-\sigma)}),$ and $\log d$ pieces give $O(d^{\lambda'}).$ The paper's choice $\lambda'=1-2^{-54}$ (cited), barely beats $D$ passes.

The layer is evaluated in [Fixed-point Gaussian dyadic records](fixed-point.md). Let $A(e)$ bound the operations on a chain from an input to an intermediate coefficient. An invocation has at most $12W$ gates, each taking at most $2W^2$ operations (each output sums at most $W$ terms); inverse-child corrections take at most $4s,$ other corrections $4W+4.$ As $s<Wm,$ the total $24W^3+4s+4W+4$ is below $E=64(W+m+1)^3.$ Chains concatenate the $s$ children; a leaf pair takes eight operations:
$$A(e)\le sA(e/m)+E,\qquad A(e)\le8e\ (\text{leaf}).$$
With $B=s+E,$ $s\varphi+E\le B\varphi$ for any bound $\varphi\ge1,$ so $A(e)\le8dB^{\lceil\log_md\rceil+1}.$ With $\nu=\min\{j\ge1:m^j\ge B\},$ $B^{\lceil\log_md\rceil+1}\le B^{\log_md+2}=B^2d^{\log_mB}\le B^2d^\nu,$ so $A(e)\le8B^2d^{\nu+1}.$ The at most $md$ pieces add $8mB^2d^{\nu+2},$ individual kernels $8d,$ diagonals and $b^D$ at most $\lfloor D/2\rfloor+9.$ The total is at most $8mB^2d^{\nu+2}+18d<128mB^2d^{\nu+3}\le\Delta=\lceil C_0d^{C_1}\rceil,$ with $C_0=128mB^2,$ $C_1=\max\{20,\nu+3\}.$

A depth-$\ell$ value lies in $2^{-(p+\ell)}\mathbb Z[i]$ with modulus at most $2^\ell,$ since addition at most doubles modulus and halving adds a denominator bit. So $p+\Delta$ fractional and $\Delta+3$ integer and sign bits per real component represent every intermediate coefficient exactly (cited). As $d=\Theta(p^\epsilon)$ and $\epsilon C_1<1,$ $\Delta=o(p):$ the width is $O(p).$

Absolute row sums multiply under tensor products, so each row of $\mathcal H=H_0^{\otimes D}$ has absolute row sum one (cited) Hence $\mathcal H$ maps disk arrays to disk arrays. Truncation toward zero cannot increase a component's absolute value and changes it by less than $2^{-p},$ so $Q_p$ keeps the disk, with $\|Q_p(\mathcal Hz)-\mathcal Hz\|_\infty<\sqrt2\,2^{-p}$ (cited).
````

## Answer

The answer is one JSON object following this schema:

```json
{
  "$defs": {
    "Anchor": {
      "description": "Where the reader learns what a symbol denotes.",
      "oneOf": [
        {
          "additionalProperties": false,
          "description": "This page says what the symbol denotes. A use in an example (\"take $r = 4$\") does not.",
          "properties": {
            "kind": {
              "const": "here",
              "type": "string"
            },
            "quote": {
              "description": "The sentence that says it, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "An earlier page binds it: one listed under \"Symbols bound on earlier pages\".",
          "properties": {
            "kind": {
              "const": "page",
              "type": "string"
            },
            "page": {
              "description": "Id of that page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "page"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "The name of a known concept contains it and binds it, as listed under the known\nconcepts.",
          "properties": {
            "concept": {
              "description": "Id of that concept.",
              "type": "string"
            },
            "kind": {
              "const": "concept",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "concept"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Standard notation the reader profile covers, such as $n$ for an input size.",
          "properties": {
            "kind": {
              "const": "background",
              "type": "string"
            },
            "note": {
              "description": "What in the reader profile covers it.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "note"
          ],
          "type": "object"
        },
        {
          "additionalProperties": false,
          "description": "Nothing tells the reader what it denotes.",
          "properties": {
            "kind": {
              "const": "unbound",
              "type": "string"
            },
            "note": {
              "description": "What the reader cannot tell.",
              "type": "string"
            },
            "quote": {
              "description": "Where it is first used, copied exactly from the page.",
              "type": "string"
            }
          },
          "required": [
            "kind",
            "quote",
            "note"
          ],
          "type": "object"
        }
      ]
    },
    "Gap": {
      "additionalProperties": false,
      "properties": {
        "kind": {
          "$ref": "#/$defs/GapKind"
        },
        "note": {
          "description": "Why this reader cannot follow it.",
          "type": "string"
        },
        "quote": {
          "description": "The passage on the page where the gap occurs, copied exactly (a phrase or one sentence).",
          "type": "string"
        },
        "term": {
          "description": "The term, or a short label for the step.",
          "type": "string"
        }
      },
      "required": [
        "term",
        "quote",
        "kind",
        "note"
      ],
      "type": "object"
    },
    "GapKind": {
      "oneOf": [
        {
          "const": "term",
          "description": "A named concept the reader does not know, which the page neither explains nor links.",
          "type": "string"
        },
        {
          "const": "step",
          "description": "An inference, calculation or claim the reader cannot check from what the page gives.",
          "type": "string"
        }
      ]
    },
    "SymbolUse": {
      "additionalProperties": false,
      "properties": {
        "anchor": {
          "$ref": "#/$defs/Anchor"
        },
        "symbol": {
          "description": "The symbol in LaTeX, as it appears in the page's mathematics, without dollar signs.",
          "type": "string"
        }
      },
      "required": [
        "symbol",
        "anchor"
      ],
      "type": "object"
    }
  },
  "additionalProperties": false,
  "properties": {
    "gaps": {
      "description": "Every term or step the reader cannot follow; empty if the reader can follow them all.",
      "items": {
        "$ref": "#/$defs/Gap"
      },
      "type": "array"
    },
    "symbols": {
      "description": "Every symbol in the page's mathematics, each once, with where the reader learns what\nit denotes. Empty only if the page has no mathematics.",
      "items": {
        "$ref": "#/$defs/SymbolUse"
      },
      "type": "array"
    }
  },
  "required": [
    "symbols",
    "gaps"
  ],
  "title": "AuditAnswer",
  "type": "object"
}
```

Write the answer to `exegenius/tasks/0209-audit-simultaneous-layer.answer.json`, then run `exegenius submit 0209-audit-simultaneous-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0209-audit-simultaneous-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
