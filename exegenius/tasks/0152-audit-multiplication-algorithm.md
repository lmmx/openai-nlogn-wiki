# exegenius task 0152-audit-multiplication-algorithm

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
- Fast address-chunk interchange (also: chunk swap, tape interchange)
- Two-point kernel C (also: phase network kernel)
- Binary phase frames
- Packed selected-bit addition (also: exceptional addresses)
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Tape layout for synthetic transforms
- Convolution from the retained transform layout
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

- $y$ (ring variable), bound on `ring-y`: The indeterminate of the polynomials; it satisfies y^r = -1 in the ring.
- $j$ (excess degree), bound on `ring-y`: The number of places a term's degree exceeds r-1.
- $a$ (shift exponent), bound on `ring-y`: An integer exponent of y by which an element is multiplied.
- $n$ (bit length), bound on `conjecture`: The number of bits in each of the two integers being multiplied.
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the grid on which stored values lie.
- $Q_p$ (truncation), bound on `fixed-point`: The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $v$ (triple count), bound on `exchange-network`: The number of three-element subsets of [h].
- $S$ (triple), bound on `exchange-network`: A three-element subset of [h], indexing a value in a bank.
- $x$ (source vector), bound on `exchange-network`: The vector of all values x_S.
- $y$ (target vector), bound on `exchange-network`: The vector of all values y_S.
- $a$ (bank index), bound on `exchange-network`: The index of a value in a data bank, a triple of triples.
- $\gamma$ (central scratch vector), bound on `exchange-network`: The initial values of the central scratch wires.
- $R$ (scalar ring), bound on `array-frames`: The ring of scalars carried by the wires.
- $t$ (gate input count), bound on `array-frames`: The number of input arrays of a gate.
- $q$ (sequence length), bound on `convolution`: The number of entries in each sequence being convolved.
- $t_i$ (axis length), bound on `convolution`: The length of cyclic axis i.
- $M$ (cyclic address count), bound on `convolution`: The number of addresses on the cyclic axes of an array.
- $T$ (total coefficient count), bound on `convolution`: The total number of complex coefficients in an array.
- $u$ (first input), bound on `radix-digit-reduction`: The first of the two integers being multiplied.
- $v$ (second input), bound on `radix-digit-reduction`: The second of the two integers being multiplied.
- $n$ (input bit length), bound on `radix-digit-reduction`: The number of bits in each input.
- $b$ (digit width), bound on `radix-digit-reduction`: The number of bits in one radix digit.
- $T$ (padded length), bound on `radix-digit-reduction`: A power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on `radix-digit-reduction`: The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $q$ (digit count), bound on `radix-digit-reduction`: The number of radix-2^b digits in each input.
- $x$ (polynomial variable), bound on `radix-digit-reduction`: The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $f$ (first array), bound on `phase-twist`: The first complex array being convolved.
- $g$ (second array), bound on `phase-twist`: The second complex array being convolved with f.
- $j$ (wrapped position), bound on `phase-twist`: The position k+l reduced modulo r.
- $\mathcal M_{\mathbb C}$ (complex convolution), bound on `phase-twist`: The normalized complex cyclic convolution of two arrays.
- $q$ (sequence length), bound on `dft`: The number of entries of a sequence.
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to be transformed.
- $t$ (transform length), bound on `butterfly`: The number of positions in the sequence being transformed, a power of two.
- $b$ (lowest bit), bound on `butterfly`: The lowest bit of the output index m.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis, a power of two dividing 2r.
- $q$ (radix), bound on `stream-ops`: The number of values one digit can take.
- $R$ (row count), bound on `stream-ops`: The number of rows in the array of item 4.
- $B$ (entries per row), bound on `stream-ops`: The number of entries in each row.
- $\boldsymbol j$ (output index), bound on `chirp`: The index tuple (j_1,...,j_d) of an entry of the data and of the output position.
- $s_i$ (source length), bound on `chirp`: An integer coprime to t_i attached to axis i, the multiplier of the frequency read.
- $Q$ (target permutation), bound on `chirp`: The permutation of the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $a$ (chirp), bound on `chirp`: The array of phases a_j = exp(-pi i sum s_i j_i^2/t_i), quadratic in the index.
- $a$ (number of rounds), bound on `frequency-order`: The number of rounds, log base 2 of the transform length t.
- $s$ (completed rounds), bound on `frequency-order`: The number of rounds completed so far.
- $i$ (axis index), bound on `frequency-order`: Index of an axis of the array.
- $v$ (two-adic exponent), bound on `frequency-order`: The exponent of 2 in j, with 0<=v<a.
- $p$ (fractional bits), bound on `signed-packing`: The number of fractional bits of each coefficient component.
- $f$ (first polynomial), bound on `signed-packing`: A polynomial of the ring with coefficients 2^{-p} times Gaussian integers.
- $a$ (integer polynomial), bound on `signed-packing`: Integer-coefficient polynomial, real part numerator of f (similarly b, c, e).
- $B_0$ (packing base), bound on `signed-packing`: The base 2^{4p} at which polynomials are evaluated.
- $q$ (prime), bound on `controlled-shifts`: The prime base of the digits of a field.
- $b$ (digits per field), bound on `controlled-shifts`: The number of base-q digits of a field.
- $Q$ (field values), bound on `controlled-shifts`: The number of values a field can take, q^b.
- $y$ (target value), bound on `controlled-shifts`: The value of the target field, in [Q].
- $a$ (offset), bound on `controlled-shifts`: The offset added to the target, prepared from the control values.
- $B$ (suffix bits), bound on `controlled-shifts`: The number of bits following the target field.
- $j$ (piece index), bound on `controlled-shifts`: The index of the increasing piece of y -> cy mod Q containing y.
- $A$ (shear matrix), bound on `matrix-shear`: The fixed rational matrix whose product with D is added to H.
- $a$ (rank), bound on `matrix-shear`: The rank of the rational matrix A.
- $a$ (kernel coefficient a), bound on `phase-kernel`: The complex constant (1+i)/2, the coefficient of the identity in C.
- $b$ (kernel coefficient b), bound on `phase-kernel`: The complex constant (1-i)/2, the coefficient of the bit flip in C.
- $C$ (two-point kernel), bound on `phase-kernel`: The 2 by 2 matrix aI+bX.
- $\mathcal M$ (bilinear map), bound on `contraction-maps`: A map linear in each of its two operands.
- $f$ (first operand), bound on `contraction-maps`: The first operand of the bilinear map.
- $g$ (second operand), bound on `contraction-maps`: The second operand of the bilinear map.
- $j$ (index tuple), bound on `multidim-transform`: The index tuple of an entry of the array, with 0 <= j_i < q_i.
- $\gamma$ (scalar exponent), bound on `multidim-transform`: The exponent 2d alpha^2 of the scalar in the tensored identity.
- $R$ (source permutation product), bound on `multidim-transform`: The tensor product of the permutations P_{s_i}; here R is not the scalar ring.
- $Q$ (target permutation product), bound on `multidim-transform`: The tensor product of the permutations P_{t_i}.
- $\mathcal A$ (tensored input map), bound on `multidim-transform`: The tensor product of the maps A_i.
- $\mathcal B_0$ (tensored output map), bound on `multidim-transform`: The tensor product of the maps B_{0,i}.
- $S$ (convolution length), bound on `crt-map`: The length of the cyclic convolution, the product of the s_i.
- $i$ (axis index), bound on `crt-map`: The index of an axis, from 1 to d.
- $s_i$ (axis source length), bound on `crt-map`: The length of axis i, pairwise coprime with the others; unrelated to the s_i of the chirp page.
- $\Phi$ (Chinese-remainder map), bound on `crt-map`: The ring isomorphism sending x to the product of x_i^{mu_i}.
- $a_j$ (mixed-radix digit), bound on `crt-map`: The j-th digit of k in mixed radix, 0 <= a_j < s_j.
- $t_i$ (padded axis length), bound on `crt-map`: The padded length of axis i, either r/2 or r.
- $T$ (padded record count), bound on `crt-map`: The number of padded records, the product of the t_i.
- $s$ (source length), bound on `gaussian-resampling`: The length of the Fourier transform to be replaced.
- $C$ (coordinate selection), bound on `gaussian-resampling`: The map from C^t to C^s that selects coordinate q_j into position j.
- $t$ (target length), bound on `gaussian-resampling`: The larger length, a power of two in the application, of the transform used instead of the length-s one.
- $\boldsymbol s$ (axis-length tuple), bound on `retained-permutations`: The tuple $(s_1,\dots,s_d)$ of prime axis lengths, one per axis.
- $\boldsymbol t$ (padded-length tuple), bound on `retained-permutations`: The tuple $(t_1,\dots,t_d)$ of power-of-two axis lengths.
- $u$ (complex array), bound on `retained-permutations`: Here a complex array, not an integer; changes meaning from the multiplication page.
- $v$ (complex array), bound on `retained-permutations`: Here a complex array, not an integer; changes meaning from the multiplication page.
- $R$ (source permutation), bound on `retained-permutations`: The tensor product of the source permutations P_{s_i}; a permutation, not the scalar ring.
- $\gamma$ (power-of-two exponent), bound on `retained-permutations`: The exponent 2 d alpha^2 of the total scalar factor 2^gamma.
- $g$ (setup exponent), bound on `retained-permutations`: A fixed exponent bounding per-line setup work by p^g.
- $\boldsymbol j$ (entry multi-index), bound on `retained-permutations`: The index (j_1,...,j_d) of an entry of the array.
- $z$ (complex vector), bound on `retained-permutations`: A vector of q complex entries.
- $\boldsymbol t$ (axis lengths), bound on `precision-recovery`: The tuple of axis lengths.
- $F_{\boldsymbol t}$ (exact Fourier transform), bound on `precision-recovery`: The exact Fourier transform with axis lengths t.
- $\gamma$ (source scale exponent), bound on `precision-recovery`: The exponent of the source scale 2^gamma.
- $u$ (scaled digit array), bound on `precision-recovery`: The array of scaled digits of the first input.
- $v$ (scaled digit array), bound on `precision-recovery`: The array of scaled digits of the second input.
- $x$ (real argument), bound on `parameter-choice`: A real number, the length at which the prime interval is taken.
- $q$ (integer in interval), bound on `parameter-choice`: An integer, in the prime interval.
- $s$ (number of smaller calls), bound on `subspace-labels`: The total number of smaller calls that the edges of the network cost.
- $F$ (one-factor label space), bound on `subspace-labels`: The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $S$ (a triple), bound on `subspace-labels`: A three-element subset of $[h]$, used with $T$ to state the indicator inner products.
- $T$ (a triple), bound on `subspace-labels`: A three-element subset of $[h]$ (not the padded size used on other pages).
- $a$ (triple tuple), bound on `subspace-labels`: A tuple $(a_1,a_2,a_3)$ of triples indexing one data wire in each bank.
- $j$ (stage number), bound on `subspace-labels`: The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
- $A$ (exposed factor space), bound on `subspace-labels`: The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
- $B$ (complement of P), bound on `subspace-labels`: The orthogonal complement of $P$ inside $A$.
- $f$ (call parameter), bound on `rank-recurrence`: The parameter of a recursive call: the number of digits per interchanged chunk, or the number of selected axes in a butterfly layer.
- $s$ (number of smaller calls), bound on `rank-recurrence`: The number of calls at parameter f made by a call at parameter mf: the total rank of the frame changes over all edges of the network.
- $F$ (cost per unit volume), bound on `rank-recurrence`: F(f) is the running time of a call at parameter f divided by the volume of its data.
- $j$ (recursion depth), bound on `rank-recurrence`: The number of recursion levels between the top call and the nodes considered.
- $u$ (chunk width), bound on `address-interchange`: The number of bits in each of the two address chunks.
- $p$ (prefix), bound on `address-interchange`: The address field before the first chunk.
- $g$ (gap), bound on `address-interchange`: The address field between the chunks.
- $z$ (suffix), bound on `address-interchange`: The address field after the second chunk.
- $q$ (radix), bound on `address-interchange`: The fixed prime used as digit radix.
- $b$ (field digits), bound on `address-interchange`: The number of digits in each of the m fields of a chunk.
- $M$ (vertex matrix), bound on `address-interchange`: The rational m by m matrix assigned to a terminal or gate.
- $i$ (edge index), bound on `address-interchange`: Index of an edge of the network.
- $w$ (wire index), bound on `address-interchange`: The index of a wire of the network, 1 to W.
- $x$ (stream row), bound on `address-interchange`: The row number within a role stream.
- $j$ (level), bound on `address-interchange`: Index of a level of the unrolled recurrence.
- $a_j$ (piece count), bound on `address-interchange`: The number of pieces of width m^j, the j-th base-m digit of e minus nu.
- $u$ (vector), bound on `phase-frames`: A vector of F_2^m on this page.
- $v$ (vector), bound on `phase-frames`: A vector of F_2^m on this page.
- $w$ (vector), bound on `phase-frames`: A vector of F_2^m on this page.
- $z$ (vector), bound on `phase-frames`: A vector of F_2^m on this page.
- $x$ (address), bound on `phase-frames`: An address, an element of F_2^m indexing the arrays.
- $\mathcal B$ (residual basis), bound on `phase-frames`: An orthonormal basis of the residual E.
- $x$ (source chunk), bound on `packed-bit-addition`: The address chunk whose selected bits are XORed into y.
- $y$ (target chunk), bound on `packed-bit-addition`: The address chunk that receives the XORs (not the ring variable).
- $z$ (scratch chunk), bound on `packed-bit-addition`: The third address chunk, used as scratch and restored.
- $R$ (record bits), bound on `packed-bit-addition`: The number of bits in a record (not the scalar ring).
- $f$ (selected bits), bound on `packed-bit-addition`: The number of selected bit positions in a chunk.
- $j_i$ (selected position), bound on `packed-bit-addition`: The position j_i = rho + iK of the i-th selected bit.
- $M$ (address count), bound on `packed-bit-addition`: The number of addresses.
- $u$ (first integer), bound on `packed-bit-addition`: The integer on which the parity-conditioned additions act first (a segment of y).
- $w$ (second integer), bound on `packed-bit-addition`: The auxiliary integer to be restored (a segment of z).
- $\mathcal B$ (exceptional set), bound on `packed-bit-addition`: The addresses where some guard of y or z lies outside [10, 2^{K-1}-11].
- $p$ (precision), bound on `packed-bit-addition`: The number of precision bits of the records.
- $z$ (record array), bound on `simultaneous-layer`: The array of records, a function of the address x.
- $x$ (address), bound on `simultaneous-layer`: An address of the array, with selected bits x_1,...,x_D.
- $q$ (row quotient), bound on `simultaneous-layer`: The quotient of a row index on division by W.
- $w$ (row remainder), bound on `simultaneous-layer`: The remainder of a row index modulo W, which is the wire role.
- $\gamma$ (step ratio), bound on `simultaneous-layer`: The ratio s/W, at most m^sigma.
- $j$ (level index), bound on `simultaneous-layer`: The index of a recursion level, counted from 0.
- $u$ (leaf chunks), bound on `simultaneous-layer`: The number of active chunks in a leaf at level j, e/m^j.
- $a_j$ (piece digit), bound on `simultaneous-layer`: The base-m digit of D-q_0 at position j, the number of pieces of m^j chunks.
- $A$ (chain bound), bound on `simultaneous-layer`: A(e) bounds the number of arithmetic operations on a chain from an input to an intermediate coefficient in a group of e axes.
- $B$ (recurrence base), bound on `simultaneous-layer`: The sum s+E.
- $\boldsymbol t$ (axis lengths), bound on `transform-layout`: The tuple (t_1,...,t_D) of the axis lengths.
- $B$ (bit reversal), bound on `transform-layout`: The bit-reversal permutation applied along every axis.
- $b$ (leftover low bits), bound on `transform-layout`: The number of low address bits of an axis left over after whole K-bit chunks.
- $q$ (whole chunks), bound on `transform-layout`: The number of whole K-bit chunks per axis.
- $z$ (round input), bound on `transform-layout`: The array entering a round.
- $M$ (number of records), bound on `ring-convolution`: The number of polynomial records, one per cyclic address of the remaining axes.
- $T$ (number of coefficients), bound on `ring-convolution`: The number of complex coefficients in an array, T = rM.
- $F^+$ (opposite transform), bound on `ring-convolution`: The opposite synthetic transform.
- $B$ (bit-reversal order), bound on `ring-convolution`: The bit-reversal order in which forward outputs are written.

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

## Page to audit (`multiplication-algorithm`)

````markdown
# The multiplication algorithm

The multiplication algorithm chains the reductions to turn two $n$-bit integers into their exact $2n$-bit product.

It takes its sizes from [Parameter and prime-length choice](parameter-choice.md): $b=\lceil\log_2 n\rceil$ is the digit width, $p=6b$ is the number of fractional bits, $s_i$ are distinct odd prime axis lengths with product $S$, and $t_i$ are power-of-two axis lengths with product $T$. Each input splits into $q=\lceil n/b\rceil$ radix-$2^b$ digits $a_j$, and the product is their convolution modulo $x^S-1$, as in [Multiplication as radix-digit convolution](radix-digit-reduction.md). The convolution is placed on the prime axes by the [Chinese-remainder address map](crt-map.md) $\Phi$.

## The source transform

Let $F_{\boldsymbol s}$ be the discrete Fourier transform on the axes $s_i$, normalized by $1/S$. $F_{\boldsymbol s}^+$ is the same with the opposite sign in the exponent, and $F_{\boldsymbol t}$ is the transform on the axes $t_i$, normalized by $1/T$.

Let $\mathcal M_{\mathbb C}(f,g)=f*g/T$ be the normalized cyclic convolution, computed through the [Phase twist](phase-twist.md) and [Convolution from the retained transform layout](ring-convolution.md). With the chirp array $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$ and the target permutation $Q$, the [Bluestein chirp identity](chirp.md) gives $QF_{\boldsymbol t}x=\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)$: phase, convolution with the chirp, phase. The computed version uses an approximation $\widetilde a$ of $a$ and truncation $Q_p$ to $p$ fractional bits. It forms the operand $x_0=Q_p(\overline{\widetilde a}\cdot x)$ after the first phase, then $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$, the computed convolution, and returns $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$. The computed source transform $\widetilde{\mathscr F}$ applies the [Gaussian resampling](gaussian-resampling.md) map $\mathcal A$, then $\widetilde{\mathscr C}$, then the map $\mathcal B_0$, then multiplies exactly by $2^\gamma$, where $\gamma$ is the resampling scale exponent; its exact counterpart $\mathscr F$ replaces each numerical routine by the exact map it approximates, giving $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, where $R$ is a retained permutation. For an array $z$, the opposite-sign procedure is $\widetilde{\mathscr F}^{+}(z)=\overline{\widetilde{\mathscr F}(\overline z)}$; $R$ is real and conjugation flips the exponent sign, so its exact counterpart is $RF_{\boldsymbol s}^{+}$.

## The algorithm

Digit $a_j$ is stored as the grid value $a_j2^{-b-2}$, padded with zero records to length $S$. Then:

1. Apply $\Phi$ to obtain source arrays $u,v$ (not integers).
2. Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.
3. Multiply corresponding coefficients and truncate to $p$ fractional bits, obtaining $z$.
4. Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply by $S$, obtaining $\widetilde w$, approximating the exact array $w=(u*v)/S$.
5. Multiply by $2^{2b+4}S$, round to the nearest integers, and apply $\Phi^{-1}$.
6. Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits.

The two scalings by $S$ undo different normalizations: each of $F_{\boldsymbol s}$ and $F_{\boldsymbol s}^{+}$ carries $1/S$, so $F_{\boldsymbol s}(u*v)=S\,F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v$ and $F_{\boldsymbol s}^{+}F_{\boldsymbol s}$ is the identity divided by $S$; hence $F_{\boldsymbol s}^{+}(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=(u*v)/S^2$. Permutations commute with pointwise products, and $RF_{\boldsymbol s}^{+}R=F_{\boldsymbol s}^{+}$ by [Retained permutation cancellation](retained-permutations.md), so $R$ drops out. Steps 2 to 4 have exact counterpart $(u*v)/S^2$, and after the scale in step 4 it is $w$. Step 5 gives $2^{2b+4}(u*v)$. Each stored operand carries $2^{-b-2}$, so $u*v$ carries $2^{-2b-4}$, which the factor $2^{2b+4}$ cancels; $\Phi^{-1}$ then returns the integer digit convolution (cited).

Exactness is shown by [Error tracking and exact recovery](precision-recovery.md): the error on these coefficients is below $1/2$, so rounding is exact.
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

Write the answer to `exegenius/tasks/0152-audit-multiplication-algorithm.answer.json`, then run `exegenius submit 0152-audit-multiplication-algorithm` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0152-audit-multiplication-algorithm`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
