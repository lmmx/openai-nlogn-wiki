# exegenius task 0149-audit-simultaneous-layer

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

- $j$ (excess degree), bound on `ring-y`: The number of places a term's degree exceeds r-1.
- $a$ (shift exponent), bound on `ring-y`: An integer exponent of y by which an element is multiplied.
- $c$ (machine constant), bound on `conjecture`: A positive constant, depending on the machine, in the lower bound c n log n.
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the grid on which stored values lie.
- $\Delta$ (reserved extra bits), bound on `fixed-point`: The number of extra bits reserved, at least the maximal depth reached in the layer.
- $Q_p$ (truncation), bound on `fixed-point`: The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $h$ (ground-set size), bound on `exchange-network`: The size of the ground set [h] whose three-element subsets index the values.
- $v$ (triple count), bound on `exchange-network`: The number of three-element subsets of [h].
- $m$ (label dimension), bound on `exchange-network`: The dimension of the label space used later.
- $S$ (triple), bound on `exchange-network`: A three-element subset of [h], indexing a value in a bank.
- $x$ (source vector), bound on `exchange-network`: The vector of all values x_S.
- $a$ (bank index), bound on `exchange-network`: The index of a value in a data bank, a triple of triples.
- $\sigma$ (side scratch vector), bound on `exchange-network`: The initial values of the side scratch wires.
- $\gamma$ (central scratch vector), bound on `exchange-network`: The initial values of the central scratch wires.
- $I$ (invocation count), bound on `exchange-network`: The number of invocations.
- $q$ (sequence length), bound on `convolution`: The number of entries in each sequence being convolved.
- $d$ (axis count), bound on `convolution`: One more than the number of cyclic axes of an array.
- $u$ (first input), bound on `radix-digit-reduction`: The first of the two integers being multiplied.
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
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to be transformed.
- $m$ (output index), bound on `butterfly`: The index of an output of the transform.
- $b$ (lowest bit), bound on `butterfly`: The lowest bit of the output index m.
- $h$ (remaining index), bound on `butterfly`: The output index m with its lowest bit removed.
- $e$ (two-adic exponent), bound on `synthetic-transform`: The exponent of 2 in j when j is written as 2^e times an odd number.
- $V$ (array volume), bound on `stream-ops`: The number of radix-q digits an array stores.
- $q$ (radix), bound on `stream-ops`: The number of values one digit can take.
- $P$ (prefix values), bound on `stream-ops`: The number of prefix values indexing the first axis of the array.
- $B$ (entries per row), bound on `stream-ops`: The number of entries in each row.
- $W$ (stream count), bound on `stream-ops`: The fixed number of streams the rows are dealt into.
- $Q$ (target permutation), bound on `chirp`: The permutation of the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $a$ (chirp), bound on `chirp`: The array of phases a_j = exp(-pi i sum s_i j_i^2/t_i), quadratic in the index.
- $a$ (number of rounds), bound on `frequency-order`: The number of rounds, log base 2 of the transform length t.
- $H_0$ (two-point butterfly), bound on `frequency-order`: The 2x2 butterfly matrix (1/2)[[1,1],[1,-1]].
- $s$ (completed rounds), bound on `frequency-order`: The number of rounds completed so far.
- $i$ (axis index), bound on `frequency-order`: Index of an axis of the array.
- $\mathcal H$ (parallel butterfly), bound on `frequency-order`: The operation applying H_0 on every participating axis at once.
- $E$ (combined exponent), bound on `frequency-order`: The exponent of y by which the record at an address is multiplied, determined by that address.
- $v$ (two-adic exponent), bound on `frequency-order`: The exponent of 2 in j, with 0<=v<a.
- $p$ (fractional bits), bound on `signed-packing`: The number of fractional bits of each coefficient component.
- $f$ (first polynomial), bound on `signed-packing`: A polynomial of the ring with coefficients 2^{-p} times Gaussian integers.
- $a$ (integer polynomial), bound on `signed-packing`: Integer-coefficient polynomial, real part numerator of f (similarly b, c, e).
- $Z$ (product integer), bound on `signed-packing`: One of the four product integers, equal to the sum of h_j B_0^j for its ordinary product h.
- $q$ (prime), bound on `controlled-shifts`: The prime base of the digits of a field.
- $b$ (digits per field), bound on `controlled-shifts`: The number of base-q digits of a field.
- $Q$ (field values), bound on `controlled-shifts`: The number of values a field can take, q^b.
- $a$ (offset), bound on `controlled-shifts`: The offset added to the target, prepared from the control values.
- $B$ (suffix bits), bound on `controlled-shifts`: The number of bits following the target field.
- $c$ (multiplier), bound on `controlled-shifts`: A fixed positive integer prime to q by which the target is multiplied.
- $j$ (piece index), bound on `controlled-shifts`: The index of the increasing piece of y -> cy mod Q containing y.
- $V$ (array volume), bound on `controlled-shifts`: The number of stored data bits in the array.
- $A$ (shear matrix), bound on `matrix-shear`: The fixed rational matrix whose product with D is added to H.
- $a$ (rank), bound on `matrix-shear`: The rank of the rational matrix A.
- $m$ (fields per group), bound on `matrix-shear`: The number of fields in each of the groups H and D.
- $H$ (target group), bound on `matrix-shear`: The ordered group of m fields that receives the sum.
- $D$ (source group), bound on `matrix-shear`: The ordered group of m fields that is added in and left unchanged.
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
- $j$ (index tuple), bound on `multidim-transform`: The index tuple of an entry of the array, with 0 <= j_i < q_i.
- $\gamma$ (scalar exponent), bound on `multidim-transform`: The exponent 2d alpha^2 of the scalar in the tensored identity.
- $Q$ (target permutation product), bound on `multidim-transform`: The tensor product of the permutations P_{t_i}.
- $S$ (convolution length), bound on `crt-map`: The length of the cyclic convolution, the product of the s_i.
- $d$ (number of axes), bound on `crt-map`: The number of axes of the target ring.
- $i$ (axis index), bound on `crt-map`: The index of an axis, from 1 to d.
- $a_j$ (mixed-radix digit), bound on `crt-map`: The j-th digit of k in mixed radix, 0 <= a_j < s_j.
- $\ell$ (address bits), bound on `crt-map`: The base-2 logarithm of the record length r, the number of address bits of a full-width axis.
- $V$ (stream volume), bound on `crt-map`: The volume of the stream being moved, Tp bits.
- $\tau$ (chunk-swap exponent), bound on `crt-map`: A fixed exponent below 1 in the cost of a chunk interchange.
- $s$ (source length), bound on `gaussian-resampling`: The length of the Fourier transform to be replaced.
- $C$ (coordinate selection), bound on `gaussian-resampling`: The map from C^t to C^s that selects coordinate q_j into position j.
- $u$ (complex array), bound on `retained-permutations`: Here a complex array, not an integer; changes meaning from the multiplication page.
- $v$ (complex array), bound on `retained-permutations`: Here a complex array, not an integer; changes meaning from the multiplication page.
- $\gamma$ (power-of-two exponent), bound on `retained-permutations`: The exponent 2 d alpha^2 of the total scalar factor 2^gamma.
- $g$ (setup exponent), bound on `retained-permutations`: A fixed exponent bounding per-line setup work by p^g.
- $c$ (unit), bound on `retained-permutations`: An integer that is a unit (invertible) modulo q.
- $z$ (complex vector), bound on `retained-permutations`: A vector of q complex entries.
- $\gamma$ (source scale exponent), bound on `precision-recovery`: The exponent of the source scale 2^gamma.
- $u$ (scaled digit array), bound on `precision-recovery`: The array of scaled digits of the first input.
- $v$ (scaled digit array), bound on `precision-recovery`: The array of scaled digits of the second input.
- $G$ (exact opposite transform), bound on `precision-recovery`: The exact opposite source transform.
- $\tau$ (chunk-swap exponent), bound on `parameter-choice`: An exponent bounding the cost of an equal-width chunk interchange.
- $\sigma$ (recursion exponent), bound on `parameter-choice`: An exponent bounding the growth of the layer's recursion.
- $\beta$ (threshold exponent), bound on `parameter-choice`: The exponent of the threshold d^beta of active chunks handled singly.
- $\lambda$ (node overhead exponent), bound on `parameter-choice`: The exponent of the per-node overhead in the butterfly layer.
- $\lambda'$ (layer cost exponent), bound on `parameter-choice`: The exponent in the final layer cost O(V d^lambda').
- $c$ (chunk-width exponent), bound on `parameter-choice`: The exponent giving the chunk width K = floor(d^c).
- $\epsilon$ (axis-count exponent), bound on `parameter-choice`: The exponent giving the axis count d = floor(b^epsilon).
- $C_1$ (guard-bit exponent), bound on `parameter-choice`: The exponent of d in the number of reserved guard bits.
- $V$ (bit volume), bound on `parameter-choice`: The logical bit volume of the data the layer acts on.
- $K$ (chunk width), bound on `parameter-choice`: The number of bits in an address chunk.
- $\eta$ (relative distance), bound on `parameter-choice`: The relative distance 1/(4d) of each prime s_i below t_i.
- $x$ (real argument), bound on `parameter-choice`: A real number, the length at which the prime interval is taken.
- $q$ (integer in interval), bound on `parameter-choice`: An integer, in the prime interval.
- $E$ (first space), bound on `tensor-product-of-spaces`: The first of the two vector spaces being tensored.
- $G$ (second space), bound on `tensor-product-of-spaces`: The second of the two vector spaces being tensored.
- $\xi$ (vector in E), bound on `tensor-product-of-spaces`: A vector of the first space E.
- $\eta$ (vector in G), bound on `tensor-product-of-spaces`: A vector of the second space G.
- $s$ (number of smaller calls), bound on `subspace-labels`: The total number of smaller calls that the edges of the network cost.
- $W$ (wire count), bound on `subspace-labels`: The number of wires of the network under consideration.
- $F$ (one-factor label space), bound on `subspace-labels`: The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $S$ (a triple), bound on `subspace-labels`: A three-element subset of $[h]$, used with $T$ to state the indicator inner products.
- $X$ (X bank), bound on `subspace-labels`: The bank of data wires $X_a$.
- $a$ (triple tuple), bound on `subspace-labels`: A tuple $(a_1,a_2,a_3)$ of triples indexing one data wire in each bank.
- $j$ (stage number), bound on `subspace-labels`: The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
- $A$ (exposed factor space), bound on `subspace-labels`: The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
- $P$ (earlier tensor line), bound on `subspace-labels`: The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on `subspace-labels`: The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on `subspace-labels`: The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $f$ (call parameter), bound on `rank-recurrence`: The parameter of a recursive call: the number of digits per interchanged chunk, or the number of selected axes in a butterfly layer.
- $m$ (slot count), bound on `rank-recurrence`: The number of size-f slots into which a call at parameter mf cuts its parameter, equal to 10^6, the label-space dimension.
- $s$ (number of smaller calls), bound on `rank-recurrence`: The number of calls at parameter f made by a call at parameter mf: the total rank of the frame changes over all edges of the network.
- $F$ (cost per unit volume), bound on `rank-recurrence`: F(f) is the running time of a call at parameter f divided by the volume of its data.
- $j$ (recursion depth), bound on `rank-recurrence`: The number of recursion levels between the top call and the nodes considered.
- $\tau$ (saving exponent), bound on `rank-recurrence`: A fixed exponent below 1 with s/W < m^tau, which makes an interchange cost O(V f^tau); here tau = 1 - 2^{-50}.
- $\eta$ (relative rank deficit), bound on `rank-recurrence`: The fraction (Wm - s)/(Wm) by which the number of smaller calls s falls short of Wm.
- $u$ (chunk width), bound on `address-interchange`: The number of bits in each of the two address chunks.
- $V$ (volume), bound on `address-interchange`: The number of stored bits of the array.
- $\tau$ (time exponent), bound on `address-interchange`: The fixed exponent below 1 in the time bound, 1-2^{-50}.
- $p$ (prefix), bound on `address-interchange`: The address field before the first chunk.
- $h$ (first chunk), bound on `address-interchange`: The address field of the first chunk.
- $d$ (second chunk), bound on `address-interchange`: The address field of the second chunk.
- $g$ (gap), bound on `address-interchange`: The address field between the chunks.
- $z$ (suffix), bound on `address-interchange`: The address field after the second chunk.
- $q$ (radix), bound on `address-interchange`: The fixed prime used as digit radix.
- $H$ (first chunk value), bound on `address-interchange`: The value of the first chunk, a vector of m fields.
- $D$ (second chunk value), bound on `address-interchange`: The value of the second chunk, a vector of m fields.
- $e$ (chunk digits), bound on `address-interchange`: The number of radix-q digits in each chunk.
- $b$ (field digits), bound on `address-interchange`: The number of digits in each of the m fields of a chunk.
- $i$ (edge index), bound on `address-interchange`: Index of an edge of the network.
- $w$ (wire index), bound on `address-interchange`: The index of a wire of the network, 1 to W.
- $x$ (stream row), bound on `address-interchange`: The row number within a role stream.
- $j$ (level), bound on `address-interchange`: Index of a level of the unrolled recurrence.
- $\nu$ (top digits), bound on `address-interchange`: The number of top digits of each chunk interchanged first.
- $a_j$ (piece count), bound on `address-interchange`: The number of pieces of width m^j, the j-th base-m digit of e minus nu.
- $u$ (vector), bound on `phase-frames`: A vector of F_2^m on this page.
- $v$ (vector), bound on `phase-frames`: A vector of F_2^m on this page.
- $w$ (vector), bound on `phase-frames`: A vector of F_2^m on this page.
- $z$ (vector), bound on `phase-frames`: A vector of F_2^m on this page.
- $x$ (address), bound on `phase-frames`: An address, an element of F_2^m indexing the arrays.
- $E$ (residual), bound on `phase-frames`: The part of V orthogonal to U on an edge from U to V.
- $Z$ (sign matrix), bound on `phase-frames`: The diagonal matrix diag(1,-1).
- $x$ (source chunk), bound on `packed-bit-addition`: The address chunk whose selected bits are XORed into y.
- $z$ (scratch chunk), bound on `packed-bit-addition`: The third address chunk, used as scratch and restored.
- $d$ (chunk count), bound on `packed-bit-addition`: The number of address chunks the butterfly layer acts on.
- $K$ (segment length), bound on `packed-bit-addition`: The number of bits in a segment, and the spacing of selected positions.
- $f$ (selected bits), bound on `packed-bit-addition`: The number of selected bit positions in a chunk.
- $V$ (volume), bound on `packed-bit-addition`: The number of bits stored, MR.
- $c$ (control), bound on `packed-bit-addition`: A Boolean control.
- $u$ (first integer), bound on `packed-bit-addition`: The integer on which the parity-conditioned additions act first (a segment of y).
- $w$ (second integer), bound on `packed-bit-addition`: The auxiliary integer to be restored (a segment of z).
- $\tau$ (swap exponent), bound on `packed-bit-addition`: The fixed exponent below 1 in the chunk interchange cost.
- $p$ (precision), bound on `packed-bit-addition`: The number of precision bits of the records.

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

The simultaneous butterfly layer applies $H_0$ coefficientwise to one bit of each of $D\le d$ address chunks of $K$ bits $(d$ bounds their number) in time $O(Vd^{\lambda'}),$ $\lambda'<1,$ instead of $D$ passes.

The [two-point kernel $C$](phase-kernel.md), $C=aI+bX,$ satisfies $H_0=b\,\mathsf SC\mathsf S,\ C^2=X,\ C^4=I$ for $\mathsf S=\operatorname{diag}(1,i)$ (cited). For records $z$ at addresses $x$ with selected bits $x_1,\dots,x_D,$ $H_0^{\otimes D}=b^D\mathcal S_DC^{\otimes D}\mathcal S_D$ with $(\mathcal S_Dz)(x)=i^{x_1+\dots+x_D}z(x),$ all exact Gaussian dyadic: $b^D=(-i/2)^{\lfloor D/2\rfloor}b^{D\bmod2}$ is a shift, a phase and at most one factor $b.$

A group of $e=mf$ axes has $m$ slots of $f$ axes; a column holds one bit per slot, in $\mathbb F_2^m.$ On the group, $C^{\otimes e}$ is computed by the network of [Binary phase frames](phase-frames.md). Each edge changes frame by $\prod_hC_{v_h}^{\eta_h}$ per column (residual basis $v_h,$ $\eta_h=\pm1,$ $C_v=aI+bX_v,$ $X_v$ shifting a column by $v).$ For invertible $G$ with first columns $v_h$ and $\mathcal P_G:x\mapsto Gx,$ $\mathcal P_GX_v\mathcal P_G^{-1}=X_{Gv}$ (cited), so the edge change is $\mathcal P_G(\prod_hC_{e_h}^{\eta_h})\mathcal P_G^{-1}$ $(e_h$ standard basis). Gaussian elimination writes $G$ as at most $m(m-1)+3m$ row additions XORing selected bits of two slots, performed by [Packed selected-bit addition](packed-bit-addition.md). So apply $\mathcal P_G^{-1},$ then $(C^{\eta_h})^{\otimes f}$ to the $f$ bits of slot $h,$ then $\mathcal P_G:$ one child on $f=e/m$ axes per residual vector, $s$ in all. As $(C^{-1})^{\otimes f}=(-i)^fZ^{\otimes f}C^{\otimes f}Z^{\otimes f},$ $Z=\operatorname{diag}(1,-1),$ inverse children need only signs and phases.

So the complete basis change and its inverse on $e$ axis chunks cost $O(V((eK)^\tau+1))$ (cited) $(\tau<1).$

Row $Wq+w$ (quotient $q,$ remainder $w<W)$ goes to wire role $w,$ so children have volume $V/W.$ The first $q_0=\lceil\log_2W\rceil\lceil\log_m(2d)\rceil$ chunks, $q_0$ counting chunks, are done individually in $O(V\log d)$ (all chunks if $D\le q_0);$ their bits form a row index of range $2^{q_0K}\ge W^{\lceil\log_md\rceil},$ zero-padded at most doubling volume. With $\beta=\frac12$ and $F(e)$ the time divided by volume,
$$F(e)\le \tfrac sW F(e/m)+O((eK)^\tau+1)\ (e\ge d^\beta),\qquad F(e)=O(e)\ (e<d^\beta).$$
It saves power as in [Recursive power saving](rank-recurrence.md).

Take $\sigma<1$ with $\gamma=s/W\le m^\sigma,$ $K\le d^c$ $(c>0$ fixed), and $\lambda$ with $\max\{\tau,\sigma\}<\lambda<1,$ $\tau(1+c/\beta)<\lambda.$ For $e\ge d^\beta,$ $K\le e^{c/\beta},$ so overhead is $O(e^\lambda).$ Levels indexed by $j\ge0$ sum to $O(e^\lambda)\sum_{j\ge0}(\gamma/m^\lambda)^j=O(e^\lambda).$ A leaf at level $j$ has $u=e/m^j<d^\beta$ chunks and $\gamma^j\le(e/u)^\sigma,$ so leaves add $O(\gamma^ju)\le O(e^\sigma d^{\beta(1-\sigma)}).$ Writing $D-q_0=\sum_ja_jm^j,$ $0\le a_j<m,$ gives $a_j$ pieces of $m^j$ chunks, at most $(m-1)(1+\lfloor\log_md\rfloor),$ hence a $\log(2d)$ factor:
$$O(\log(2d)[d^\lambda+d^{\sigma+\beta(1-\sigma)}+1])=O(d^{\lambda'})$$
for $\max\{\lambda,\sigma+\beta(1-\sigma)\}<\lambda'<1.$ The paper's $\tau=\sigma=1-2^{-50},$ $c=2^{-56},$ $\lambda=1-2^{-52}$ allow $\lambda'=1-2^{-54}$ (cited), barely below $D$ passes.

The layer is evaluated exactly in [fixed-point Gaussian dyadic records](fixed-point.md). Let $A(e)$ bound operations along a chain from an input to an intermediate coefficient. One invocation adds fewer than $E=64(W+m+1)^3$ (gates, corrections, $s<Wm),$ and chains concatenate the $s$ children:
$$A(e)\le sA(e/m)+E,\qquad A(e)\le8e\ (\text{leaf}).$$
Since $s\xi+E\le B\xi$ for $\xi\ge1,$ $B=s+E,$ over at most $\lceil\log_md\rceil$ levels, with $\nu=\min\{j\ge1:m^j\ge B\},$ $A(e)\le8B^2d^{\nu+1}.$ Adding pieces, diagonals and $b^D$ stays below $\Delta=\lceil C_0d^{C_1}\rceil,$ $C_0=128mB^2,$ $C_1=\max\{20,\nu+3\}=20$ here.

For disk inputs on $2^{-p}\mathbb Z[i]$ and chain depth $\ell,$ values lie in $2^{-(p+\ell)}\mathbb Z[i]$ with modulus at most $2^\ell,$ by induction: addition doubles modulus, halving adds a denominator bit. So $p+\Delta$ fractional and $\Delta+3$ integer and sign bits per real component represent every intermediate coefficient exactly (cited). For $d=\Theta(p^\epsilon),$ fixed $\epsilon$ with $\epsilon C_1<1,$ $\Delta=o(p):$ width $O(p).$

Each row of $H_0$ has absolute row sum one, and absolute row sums multiply under tensor products, so every row of $\mathcal H=H_0^{\otimes D}$ has absolute row sum one (cited) Hence $\mathcal H$ maps disk arrays to disk arrays. Truncation toward zero cannot increase either component's absolute value, so $Q_p$ keeps the disk, changing each component by less than $2^{-p}:$ $\|Q_p(\mathcal Hz)-\mathcal Hz\|_\infty<\sqrt2\,2^{-p}$ (cited).
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

Write the answer to `exegenius/tasks/0149-audit-simultaneous-layer.answer.json`, then run `exegenius submit 0149-audit-simultaneous-layer` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0149-audit-simultaneous-layer`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
