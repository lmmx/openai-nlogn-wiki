# exegenius task 0148-audit-packed-bit-addition

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
- $r$ (record length), bound on `ring-y`: The number of complex coefficients in a polynomial of the ring, always a power of two.
- $j$ (excess degree), bound on `ring-y`: The number of places a term's degree exceeds r-1.
- $a$ (shift exponent), bound on `ring-y`: An integer exponent of y by which an element is multiplied.
- $c$ (machine constant), bound on `conjecture`: A positive constant, depending on the machine, in the lower bound c n log n.
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the grid on which stored values lie.
- $h$ (ground-set size), bound on `exchange-network`: The size of the ground set [h] whose three-element subsets index the values.
- $S$ (triple), bound on `exchange-network`: A three-element subset of [h], indexing a value in a bank.
- $x$ (source vector), bound on `exchange-network`: The vector of all values x_S.
- $y$ (target vector), bound on `exchange-network`: The vector of all values y_S.
- $a$ (bank index), bound on `exchange-network`: The index of a value in a data bank, a triple of triples.
- $R$ (scalar ring), bound on `array-frames`: The ring of scalars carried by the wires.
- $t$ (gate input count), bound on `array-frames`: The number of input arrays of a gate.
- $d$ (axis count), bound on `convolution`: One more than the number of cyclic axes of an array.
- $M$ (cyclic address count), bound on `convolution`: The number of addresses on the cyclic axes of an array.
- $T$ (total coefficient count), bound on `convolution`: The total number of complex coefficients in an array.
- $u$ (first input), bound on `radix-digit-reduction`: The first of the two integers being multiplied.
- $b$ (digit width), bound on `radix-digit-reduction`: The number of bits in one radix digit.
- $T$ (padded length), bound on `radix-digit-reduction`: A power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on `radix-digit-reduction`: The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $u_i$ (digit of u), bound on `radix-digit-reduction`: The i-th radix-2^b digit of u, an integer below 2^b.
- $x$ (polynomial variable), bound on `radix-digit-reduction`: The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $f$ (first array), bound on `phase-twist`: The first complex array being convolved.
- $g$ (second array), bound on `phase-twist`: The second complex array being convolved with f.
- $d$ (axis count), bound on `phase-twist`: The number of axes of the arrays.
- $l$ (second coefficient index), bound on `phase-twist`: An index of a coefficient of the second factor.
- $j$ (wrapped position), bound on `phase-twist`: The position k+l reduced modulo r.
- $h$ (wrap indicator), bound on `phase-twist`: Zero or one according to whether k+l wrapped past r.
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to be transformed.
- $t$ (transform length), bound on `butterfly`: The number of positions in the sequence being transformed, a power of two.
- $b$ (lowest bit), bound on `butterfly`: The lowest bit of the output index m.
- $h$ (remaining index), bound on `butterfly`: The output index m with its lowest bit removed.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis, a power of two dividing 2r.
- $e$ (two-adic exponent), bound on `synthetic-transform`: The exponent of 2 in j when j is written as 2^e times an odd number.
- $V$ (array volume), bound on `stream-ops`: The number of radix-q digits an array stores.
- $P$ (prefix values), bound on `stream-ops`: The number of prefix values indexing the first axis of the array.
- $R$ (row count), bound on `stream-ops`: The number of rows in the array of item 4.
- $B$ (entries per row), bound on `stream-ops`: The number of entries in each row.
- $a$ (chirp), bound on `chirp`: The array of phases a_j = exp(-pi i sum s_i j_i^2/t_i), quadratic in the index.
- $a$ (number of rounds), bound on `frequency-order`: The number of rounds, log base 2 of the transform length t.
- $i$ (axis index), bound on `frequency-order`: Index of an axis of the array.
- $u_i$ (current axis length), bound on `frequency-order`: The current length of axis i.
- $b_i$ (new bit), bound on `frequency-order`: The bit newly written by the latest round on axis i.
- $j_0$ (odd part), bound on `frequency-order`: The odd part of j, so j=2^v j_0.
- $p$ (fractional bits), bound on `signed-packing`: The number of fractional bits of each coefficient component.
- $f$ (first polynomial), bound on `signed-packing`: A polynomial of the ring with coefficients 2^{-p} times Gaussian integers.
- $a$ (integer polynomial), bound on `signed-packing`: Integer-coefficient polynomial, real part numerator of f (similarly b, c, e).
- $b$ (digits per field), bound on `controlled-shifts`: The number of base-q digits of a field.
- $y$ (target value), bound on `controlled-shifts`: The value of the target field, in [Q].
- $a$ (offset), bound on `controlled-shifts`: The offset added to the target, prepared from the control values.
- $B$ (suffix bits), bound on `controlled-shifts`: The number of bits following the target field.
- $c$ (multiplier), bound on `controlled-shifts`: A fixed positive integer prime to q by which the target is multiplied.
- $j$ (piece index), bound on `controlled-shifts`: The index of the increasing piece of y -> cy mod Q containing y.
- $V$ (array volume), bound on `controlled-shifts`: The number of stored data bits in the array.
- $A$ (shear matrix), bound on `matrix-shear`: The fixed rational matrix whose product with D is added to H.
- $a$ (rank), bound on `matrix-shear`: The rank of the rational matrix A.
- $a$ (kernel coefficient a), bound on `phase-kernel`: The complex constant (1+i)/2, the coefficient of the identity in C.
- $b$ (kernel coefficient b), bound on `phase-kernel`: The complex constant (1-i)/2, the coefficient of the bit flip in C.
- $L$ (linear map), bound on `contraction-maps`: A linear map whose norm bound is being defined.
- $f$ (first operand), bound on `contraction-maps`: The first operand of the bilinear map.
- $g$ (second operand), bound on `contraction-maps`: The second operand of the bilinear map.
- $u'$ (computed input), bound on `contraction-maps`: A computed approximation replacing the exact input u.
- $j$ (index tuple), bound on `multidim-transform`: The index tuple of an entry of the array, with 0 <= j_i < q_i.
- $\delta$ (time exponent slack), bound on `multidim-transform`: A fixed constant with 0 < delta < 1/8 in the exponent of the running time.
- $R$ (source permutation product), bound on `multidim-transform`: The tensor product of the permutations P_{s_i}; here R is not the scalar ring.
- $S$ (convolution length), bound on `crt-map`: The length of the cyclic convolution, the product of the s_i.
- $d$ (number of axes), bound on `crt-map`: The number of axes of the target ring.
- $i$ (axis index), bound on `crt-map`: The index of an axis, from 1 to d.
- $b_i$ (axis coordinate), bound on `crt-map`: The axis-i coordinate of Phi(x^k).
- $T$ (padded record count), bound on `crt-map`: The number of padded records, the product of the t_i.
- $V$ (stream volume), bound on `crt-map`: The volume of the stream being moved, Tp bits.
- $\tau$ (chunk-swap exponent), bound on `crt-map`: A fixed exponent below 1 in the cost of a chunk interchange.
- $\delta$ (exponent slack), bound on `gaussian-resampling`: A fixed constant 0 < delta < 1/8 that is the slack in the exponents of the time bounds.
- $t$ (target length), bound on `gaussian-resampling`: The larger length, a power of two in the application, of the transform used instead of the length-s one.
- $\delta$ (time exponent), bound on `retained-permutations`: The fixed exponent in the time bound of Gaussian resampling.
- $u$ (complex array), bound on `retained-permutations`: Here a complex array, not an integer; changes meaning from the multiplication page.
- $R$ (source permutation), bound on `retained-permutations`: The tensor product of the source permutations P_{s_i}; a permutation, not the scalar ring.
- $g$ (setup exponent), bound on `retained-permutations`: A fixed exponent bounding per-line setup work by p^g.
- $c$ (unit), bound on `retained-permutations`: An integer that is a unit (invertible) modulo q.
- $z$ (complex vector), bound on `retained-permutations`: A vector of q complex entries.
- $L$ (log of padded size), bound on `precision-recovery`: The base-2 logarithm of T.
- $u$ (scaled digit array), bound on `precision-recovery`: The array of scaled digits of the first input.
- $\tau$ (chunk-swap exponent), bound on `parameter-choice`: An exponent bounding the cost of an equal-width chunk interchange.
- $c$ (chunk-width exponent), bound on `parameter-choice`: The exponent giving the chunk width K = floor(d^c).
- $\delta$ (resampling-cost exponent), bound on `parameter-choice`: The exponent delta in the cost of the Gaussian resampling maps.
- $V$ (bit volume), bound on `parameter-choice`: The logical bit volume of the data the layer acts on.
- $K$ (chunk width), bound on `parameter-choice`: The number of bits in an address chunk.
- $x$ (real argument), bound on `parameter-choice`: A real number, the length at which the prime interval is taken.
- $S$ (a triple), bound on `subspace-labels`: A three-element subset of $[h]$, used with $T$ to state the indicator inner products.
- $T$ (a triple), bound on `subspace-labels`: A three-element subset of $[h]$ (not the padded size used on other pages).
- $a$ (triple tuple), bound on `subspace-labels`: A tuple $(a_1,a_2,a_3)$ of triples indexing one data wire in each bank.
- $L$ (total dimension loss), bound on `subspace-labels`: The total number of dimensions lost on decreasing edges.
- $j$ (stage number), bound on `subspace-labels`: The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
- $A$ (exposed factor space), bound on `subspace-labels`: The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
- $P$ (earlier tensor line), bound on `subspace-labels`: The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on `subspace-labels`: The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on `subspace-labels`: The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $f$ (call parameter), bound on `rank-recurrence`: The parameter of a recursive call: the number of digits per interchanged chunk, or the number of selected axes in a butterfly layer.
- $j$ (recursion depth), bound on `rank-recurrence`: The number of recursion levels between the top call and the nodes considered.
- $\tau$ (saving exponent), bound on `rank-recurrence`: A fixed exponent below 1 with s/W < m^tau, which makes an interchange cost O(V f^tau); here tau = 1 - 2^{-50}.
- $u$ (chunk width), bound on `address-interchange`: The number of bits in each of the two address chunks.
- $V$ (volume), bound on `address-interchange`: The number of stored bits of the array.
- $\tau$ (time exponent), bound on `address-interchange`: The fixed exponent below 1 in the time bound, 1-2^{-50}.
- $p$ (prefix), bound on `address-interchange`: The address field before the first chunk.
- $h$ (first chunk), bound on `address-interchange`: The address field of the first chunk.
- $d$ (second chunk), bound on `address-interchange`: The address field of the second chunk.
- $g$ (gap), bound on `address-interchange`: The address field between the chunks.
- $z$ (suffix), bound on `address-interchange`: The address field after the second chunk.
- $e$ (chunk digits), bound on `address-interchange`: The number of radix-q digits in each chunk.
- $b$ (field digits), bound on `address-interchange`: The number of digits in each of the m fields of a chunk.
- $M$ (vertex matrix), bound on `address-interchange`: The rational m by m matrix assigned to a terminal or gate.
- $i$ (edge index), bound on `address-interchange`: Index of an edge of the network.
- $w$ (wire index), bound on `address-interchange`: The index of a wire of the network, 1 to W.
- $x$ (stream row), bound on `address-interchange`: The row number within a role stream.
- $j$ (level), bound on `address-interchange`: Index of a level of the unrolled recurrence.
- $u$ (vector), bound on `phase-frames`: A vector of F_2^m on this page.
- $w$ (vector), bound on `phase-frames`: A vector of F_2^m on this page.
- $z$ (vector), bound on `phase-frames`: A vector of F_2^m on this page.
- $x$ (address), bound on `phase-frames`: An address, an element of F_2^m indexing the arrays.
- $\mathcal B$ (residual basis), bound on `phase-frames`: An orthonormal basis of the residual E.

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

## Page to audit (`packed-bit-addition`)

````markdown
# Packed selected-bit addition

Packed selected-bit addition XORs chosen bits of a chunk $x$ into chunk $y$ (chunks here), restoring a scratch chunk $z$; the [simultaneous butterfly layer](simultaneous-layer.md) on $d$ address chunks needs it.

For a Boolean control $c$ and integers $u,w$, $c[P]$ is $c$ if $P$ holds, else $0$. Do, in order:

$$\begin{array}{llll}
(1)\ u\leftarrow u-c[w\bmod2=0] & (2)\ w\leftarrow w-c[u\bmod2=0] & (3)\ u\leftarrow u+c[w\bmod2=0] & (4)\ w\leftarrow w+c[u\bmod2=0]\\
(5)\ w\leftarrow w+c[u\bmod2=1] & (6)\ u\leftarrow u+c[w\bmod2=1] & (7)\ w\leftarrow w-c[u\bmod2=1] & (8)\ u\leftarrow u-c[w\bmod2=1]
\end{array}$$

For $c=1$, substituting the four parity pairs shows the first four lines induce $(00\ 01\ 10)$ on the parities of $(u,w)$ and the last four induce $(01\ 10\ 11)$, composing to $(00\ 10)(01\ 11)$: it flips the parity of $u$ and restores $w$'s. So $(u',w')=(u+c(1-2(u\bmod2)),w)$, keeping quotients by two. Each variable is changed four times by at most one, so moves at most four, hence eight.

Records have $R$ bits. A chunk has $L=fK$ bits (segment length $K\ge6$); the $f$ selected bits lie at $j_i=\rho+iK$, $0\le i<f$, with offset $\rho<K$; the goal is $y_{j_i}\leftarrow y_{j_i}\oplus x_{j_i}$. Let $M$ count addresses, $V=MR$, and $A_{\rm rect}=\lceil\log_2(2V)\rceil$ bound counter lengths.

Omit $j_{f-1}$ first. For $0\le i<f-1$, the $K$ bits of $y$ from $j_i$ give a segment $u_i=2g_i+a_i$ and those of $z$ give $w_i=2h_i+b_i$, with bits $a_i,b_i$, guard values $g_i,h_i\in\{0,\dots,2^{K-1}-1\}$, and control $c_i=x_{j_i}$. Line (1) on all segments is
$$y\leftarrow y-\sum_{i=0}^{f-2}2^{j_i}[x_{j_i}=1][z_{j_i}=0]\pmod{2^L}.$$
Other lines vary the sign, tested parity or roles of $y,z$. Each is a cyclic shift of a whole chunk by an offset independent of the target chunk, hence a bijection of the addresses; $S_0$ composes the eight.

Let $\mathcal B$ (exceptional addresses) be those where a guard of $y$ or $z$ fails $10\le g\le2^{K-1}-11$. Off $\mathcal B$ each segment lies in $[20,2^K-21]$, so displacement eight stays in $[0,2^K-1]$: no segment carries into or borrows from a neighbour, and $S_0$ equals the ideal map $T_0$ XORing at $j_0,\dots,j_{f-2}$.

Ten values fall on each side of the interval ($2^{K-1}\ge32$): twenty per guard (cited). Guards are equidistributed at every spectator choice, so a union bound over $2(f-1)$ guards gives $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\}$.

$T_0$ flips only the bits $a_i$, preserving guards and so $\mathcal B$. Two bijections agreeing off $\mathcal B$ give $S_0(\mathcal B^c)=T_0(\mathcal B^c)=\mathcal B^c$ and $S_0(\mathcal B)=\mathcal B$, so $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B$.

A scan extracts records at $\mathcal B$, computing each destination $T_0S_0^{-1}$ by reversing the eight additions; its rank (current rank plus signed chunk differences times strides) is the key, and its hole is marked. As $T_0S_0^{-1}$ permutes $\mathcal B$, the keys are exactly the holes' ranks, so a stable radix sort and one scan refilling holes in order apply $T_0$. $j_{f-1}$ is then XORed by an [elementary stream operation](stream-ops.md), $O(V)$.

$S_0$ has at most eight rotations and sixteen swaps (cited). It performs rotations as [controlled shifts](controlled-shifts.md) costing $O(V)$ and swaps as [chunk interchanges](address-interchange.md) costing $O(VL^\tau)$ for fixed exponent $\tau<1$. Schoolbook arithmetic on counters costs $O(A_{\rm rect}^3)$ per record; at most $A_{\rm rect}$ radix passes sort $|\mathcal B|$ records of $R+A_{\rm rect}$ bits. The time is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect}))$ (cited).

Per $V$ the extra terms are $A_{\rm rect}^3/R$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)$. With $p$ the precision bits, both vanish when $A_{\rm rect}=O(p)$, $R$ exceeds every polynomial in $p$, $f\le d\le p$ and $K/\log p\to\infty$, so the cost is $O(V(L^\tau+1))$.
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

Write the answer to `exegenius/tasks/0148-audit-packed-bit-addition.answer.json`, then run `exegenius submit 0148-audit-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0148-audit-packed-bit-addition`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
