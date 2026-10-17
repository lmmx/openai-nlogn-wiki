# exegenius task 0141-audit-precision-recovery

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
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Two-point kernel C (also: phase network kernel)
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

## Symbols bound on earlier pages

- $r$ (record length), bound on `ring-y`: The number of complex coefficients in a polynomial of the ring, always a power of two.
- $j$ (excess degree), bound on `ring-y`: The number of places a term's degree exceeds r-1.
- $a$ (shift exponent), bound on `ring-y`: An integer exponent of y by which an element is multiplied.
- $n$ (bit length), bound on `conjecture`: The number of bits in each of the two integers being multiplied.
- $c$ (machine constant), bound on `conjecture`: A positive constant, depending on the machine, in the lower bound c n log n.
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on `fixed-point`: The number of operations in sequence since the layer began that produced a value.
- $Q_p$ (truncation), bound on `fixed-point`: The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $h$ (ground-set size), bound on `exchange-network`: The size of the ground set [h] whose three-element subsets index the values.
- $v$ (triple count), bound on `exchange-network`: The number of three-element subsets of [h].
- $S$ (triple), bound on `exchange-network`: A three-element subset of [h], indexing a value in a bank.
- $x$ (source vector), bound on `exchange-network`: The vector of all values x_S.
- $a$ (bank index), bound on `exchange-network`: The index of a value in a data bank, a triple of triples.
- $\gamma$ (central scratch vector), bound on `exchange-network`: The initial values of the central scratch wires.
- $I$ (invocation count), bound on `exchange-network`: The number of invocations.
- $t$ (gate input count), bound on `array-frames`: The number of input arrays of a gate.
- $q$ (sequence length), bound on `convolution`: The number of entries in each sequence being convolved.
- $d$ (axis count), bound on `convolution`: One more than the number of cyclic axes of an array.
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
- $c_j$ (product coefficient), bound on `radix-digit-reduction`: The coefficient of x^j in the product of the digit polynomials.
- $f$ (first array), bound on `phase-twist`: The first complex array being convolved.
- $g$ (second array), bound on `phase-twist`: The second complex array being convolved with f.
- $d$ (axis count), bound on `phase-twist`: The number of axes of the arrays.
- $k$ (coefficient index), bound on `phase-twist`: An index of a coefficient (not an operation count).
- $j$ (wrapped position), bound on `phase-twist`: The position k+l reduced modulo r.
- $h$ (wrap indicator), bound on `phase-twist`: Zero or one according to whether k+l wrapped past r.
- $\mathcal M_r$ (ring convolution), bound on `phase-twist`: Normalized convolution of the first d-1 axes over R_r, including division by T.
- $\|f\|$ (sup norm), bound on `phase-twist`: The largest modulus of a scalar coefficient of f.
- $q$ (sequence length), bound on `dft`: The number of entries of a sequence.
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to be transformed.
- $t$ (transform length), bound on `butterfly`: The number of positions in the sequence being transformed, a power of two.
- $b$ (lowest bit), bound on `butterfly`: The lowest bit of the output index m.
- $h$ (remaining index), bound on `butterfly`: The output index m with its lowest bit removed.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis, a power of two dividing 2r.
- $e$ (two-adic exponent), bound on `synthetic-transform`: The exponent of 2 in j when j is written as 2^e times an odd number.
- $V$ (array volume), bound on `stream-ops`: The number of radix-q digits an array stores.
- $q$ (radix), bound on `stream-ops`: The number of values one digit can take.
- $Q$ (target permutation), bound on `chirp`: The permutation of the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $a$ (chirp), bound on `chirp`: The array of phases a_j = exp(-pi i sum s_i j_i^2/t_i), quadratic in the index.
- $a$ (number of rounds), bound on `frequency-order`: The number of rounds, log base 2 of the transform length t.
- $s$ (completed rounds), bound on `frequency-order`: The number of rounds completed so far.
- $i$ (axis index), bound on `frequency-order`: Index of an axis of the array.
- $E$ (combined exponent), bound on `frequency-order`: The exponent of y by which the record at an address is multiplied, determined by that address.
- $v$ (two-adic exponent), bound on `frequency-order`: The exponent of 2 in j, with 0<=v<a.
- $p$ (fractional bits), bound on `signed-packing`: The number of fractional bits of each coefficient component.
- $f$ (first polynomial), bound on `signed-packing`: A polynomial of the ring with coefficients 2^{-p} times Gaussian integers.
- $a$ (integer polynomial), bound on `signed-packing`: Integer-coefficient polynomial, real part numerator of f (similarly b, c, e).
- $d_j$ (packed block), bound on `signed-packing`: The j-th block of 4p bits of the encoding of A_u, in [0,B_0).
- $q$ (prime), bound on `controlled-shifts`: The prime base of the digits of a field.
- $b$ (digits per field), bound on `controlled-shifts`: The number of base-q digits of a field.
- $Q$ (field values), bound on `controlled-shifts`: The number of values a field can take, q^b.
- $a$ (offset), bound on `controlled-shifts`: The offset added to the target, prepared from the control values.
- $c$ (multiplier), bound on `controlled-shifts`: A fixed positive integer prime to q by which the target is multiplied.
- $j$ (piece index), bound on `controlled-shifts`: The index of the increasing piece of y -> cy mod Q containing y.
- $V$ (array volume), bound on `controlled-shifts`: The number of stored data bits in the array.
- $a$ (rank), bound on `matrix-shear`: The rank of the rational matrix A.
- $a$ (kernel coefficient a), bound on `phase-kernel`: The complex constant (1+i)/2, the coefficient of the identity in C.
- $b$ (kernel coefficient b), bound on `phase-kernel`: The complex constant (1-i)/2, the coefficient of the bit flip in C.
- $I$ (identity matrix), bound on `phase-kernel`: The 2 by 2 identity matrix.
- $C$ (two-point kernel), bound on `phase-kernel`: The 2 by 2 matrix aI+bX.
- $L$ (linear map), bound on `contraction-maps`: A linear map whose norm bound is being defined.
- $\mathcal M$ (bilinear map), bound on `contraction-maps`: A map linear in each of its two operands.
- $f$ (first operand), bound on `contraction-maps`: The first operand of the bilinear map.
- $g$ (second operand), bound on `contraction-maps`: The second operand of the bilinear map.
- $f'$ (perturbed first operand), bound on `contraction-maps`: A perturbed replacement for the operand f.
- $g'$ (perturbed second operand), bound on `contraction-maps`: A perturbed replacement for the operand g.
- $j$ (index tuple), bound on `multidim-transform`: The index tuple of an entry of the array, with 0 <= j_i < q_i.
- $k$ (output index tuple), bound on `multidim-transform`: An output index tuple of the same shape as j.
- $\gamma$ (scalar exponent), bound on `multidim-transform`: The exponent 2d alpha^2 of the scalar in the tensored identity.
- $Q$ (target permutation product), bound on `multidim-transform`: The tensor product of the permutations P_{t_i}.
- $S$ (convolution length), bound on `crt-map`: The length of the cyclic convolution, the product of the s_i.
- $d$ (number of axes), bound on `crt-map`: The number of axes of the target ring.
- $i$ (axis index), bound on `crt-map`: The index of an axis, from 1 to d.
- $k$ (coefficient index), bound on `crt-map`: The index of a coefficient of the length-S sequence.
- $T$ (padded record count), bound on `crt-map`: The number of padded records, the product of the t_i.
- $V$ (stream volume), bound on `crt-map`: The volume of the stream being moved, Tp bits.
- $s$ (source length), bound on `gaussian-resampling`: The length of the Fourier transform to be replaced.
- $C$ (coordinate selection), bound on `gaussian-resampling`: The map from C^t to C^s that selects coordinate q_j into position j.
- $k$ (output coordinate index), bound on `gaussian-resampling`: A coordinate index of a vector in C^t, taken modulo t.
- $t$ (target length), bound on `gaussian-resampling`: The larger length, a power of two in the application, of the transform used instead of the length-s one.
- $\boldsymbol t$ (padded-length tuple), bound on `retained-permutations`: The tuple $(t_1,\dots,t_d)$ of power-of-two axis lengths.
- $u$ (complex array), bound on `retained-permutations`: Here a complex array, not an integer; changes meaning from the multiplication page.
- $v$ (complex array), bound on `retained-permutations`: Here a complex array, not an integer; changes meaning from the multiplication page.
- $\gamma$ (power-of-two exponent), bound on `retained-permutations`: The exponent 2 d alpha^2 of the total scalar factor 2^gamma.
- $g$ (setup exponent), bound on `retained-permutations`: A fixed exponent bounding per-line setup work by p^g.
- $c$ (unit), bound on `retained-permutations`: An integer that is a unit (invertible) modulo q.
- $z$ (complex vector), bound on `retained-permutations`: A vector of q complex entries.

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

## Page to audit (`precision-recovery`)

````markdown
# Error tracking and exact recovery

Error tracking and exact recovery shows the computed coefficients lie within $1/2$ of the integers, so rounding is exact.

The computation runs on [Fixed-point Gaussian dyadic records](fixed-point.md) with $p=6b$ fractional bits; $b=\lceil\log_2n\rceil$ is the digit width. Let $h_p=2^{-p}$, $L=\log_2T$, $S\le T$; for large $n$, $T<8n/b$ gives $T<2^b$ and $L<b$. Error $a$ means sup-norm error under $ah_p$; arrays stay in the disk (norm $\le1$). Each [Synthetic polynomial transform](synthetic-transform.md) has error below $L$ (cited).

It adds errors through the [Contractions and bilinear contractions](contraction-maps.md) making up each transform and product. A bilinear $\mathcal M$ with $\|\mathcal M(f,g)\|\le\|f\|\|g\|$ satisfies
$$\|\mathcal M(f',g')-\mathcal M(f,g)\|=\|\mathcal M(f'-f,g')+\mathcal M(f,g'-g)\|\le\|f'-f\|\|g'\|+\|f\|\|g'-g\|,$$
so for disk operands input errors add.

For a unit phase $e$, a disk-grid approximation $\widetilde e$ with $|\widetilde e-e|<2h_p$ and a disk operand $x$, truncation $Q_p$ adds under $\sqrt2h_p$, so $\|Q_p(\widetilde ex)-ex\|<(2\|x\|+\sqrt2)h_p<4h_p$; and $|\widetilde e|\le1$ gives $\|Q_p(\widetilde ex)\|\le\|x\|$.

The ring convolution $\mathcal M_r$ of [Phase twist](phase-twist.md) returns $(f*g)/T$. Its transforms and truncation err by under $3L+2$ before a final exact multiplication by $M=T/r$, giving $E_{\rm ring}:=M(3L+2)<5TL$.
If an operand has norm at most $.7$, so does the exact output, by contraction; adding error $5TLh_p<10^{-3}$ gives norm below $.701$. Two twists and an untwist add $4$ each, so the complex convolution errs by under
$$(E_{\rm ring}+4+4+4)h_p<6TLh_p.$$

The chirp transform $\widetilde{\mathscr C}$ evaluates the [Bluestein chirp identity](chirp.md), with $\boldsymbol t$ the axis lengths, $F_{\boldsymbol t}$ the exact Fourier transform and $Q$ the target permutation:
$$\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<(6TL+2+4+4)h_p<8TLh_p.$$

A source transform applies [Gaussian resampling](gaussian-resampling.md) maps and a chirp transform (error under $2dp^2+8TL$), then scales exactly by the source scale $2^\gamma$ ($b\ge2^{24}$ gives $\gamma\le b/4$ (cited)). As $2dp^2<TL$ eventually, error is under $E_sh_p$, $E_s=9\cdot2^\gamma TL$.

Here $u,v$ denote the scaled digit arrays (letters redefined): a digit $a$ is stored as $a2^{-b-2}$, norm under $1/4$. Let $U,V_1$ be their exact source transforms and $\widetilde U,\widetilde V_1$ the computed ones, of norm under $.26$. Then $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has norm under $.5$, and
$$\widetilde U\cdot\widetilde V_1-U\cdot V_1=(\widetilde U-U)\cdot\widetilde V_1+U\cdot(\widetilde V_1-V_1)$$
has two terms under $E_sh_p$; truncation adds under $2h_p$. So $\|z-U\cdot V_1\|<(2E_s+2)h_p$.

Both source Fourier transforms, $F$ and $F^+$, carry $1/S$, so $F(u*v)=S\,Fu\cdot Fv$ and $F^+F=I/S$; the retained permutation cancels ([Retained permutation cancellation](retained-permutations.md)), so the exact opposite transform $G$ gives $G(U\cdot V_1)=(u*v)/S^2$ (cited) The computed one is within $E_sh_p$ of $Gz$, and $G$ is a contraction, so the total is under $(3E_s+2)h_p$. Multiplying exactly by $S$, $\widetilde w$ approximates $w=(u*v)/S$ within $E_wh_p$:
$$E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L.$$

The integer coefficients are $2^{2b+4}Sw$, undoing digit scales and $1/S$. With $S\le T<2^b$ and $L<b$ the absolute error is under
$$2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}<448b\,2^{-b+\gamma}\le448b\,2^{-3b/4}<\tfrac12.$$
Here $p=6b$ leaves margin $2^{-b}$ against amplification up to $2^{5b+4}$. The coefficients are integers, so error below $1/2$ makes the nearest integer to the represented value correct.

Carry propagation rebuilds the binary product from the coefficients $c_j$ of the [Multiplication as radix-digit convolution](radix-digit-reduction.md), where $c_j\le q(2^b-1)^2$ and $q=\lceil n/b\rceil\le2^b$. With $Q_0=2^b$ and $k_0=0$, output digit $d_j$ and carry $k_j$ satisfy
$$d_j=(c_j+k_j)\bmod Q_0,\qquad k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor.$$
Then $0\le k_j\le q(Q_0-1)<Q_0^2$: if so at $j$, then $c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1)$. As $c_j+k_j=d_j+Q_0k_{j+1}$, adding $c_jQ_0^j$ carries the invariant
$$\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$$
from $j$ to $j+1$. Unprocessed terms are multiples of $Q_0^j$, so the first $j$ radix digits are fixed. The product is below $2^{2n}$, so bits above position $2n-1$ are zero and $2n$ bits are output.
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

Write the answer to `exegenius/tasks/0141-audit-precision-recovery.answer.json`, then run `exegenius submit 0141-audit-precision-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0141-audit-precision-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
