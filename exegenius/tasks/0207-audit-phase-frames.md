# exegenius task 0207-audit-phase-frames

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

- $r$ (record length), bound on `ring-y`: The number of complex coefficients in a polynomial of the ring, always a power of two.
- $c$ (machine constant), bound on `conjecture`: A positive constant, depending on the machine, in the lower bound c n log n.
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on `fixed-point`: The number of operations in sequence since the layer began that produced a value.
- $v$ (number of triples), bound on `exchange-network`: The number of three-element subsets of [h].
- $X$ (bank X), bound on `exchange-network`: The first data bank, with entries X_a.
- $Y$ (bank Y), bound on `exchange-network`: The second data bank, with entries Y_a.
- $a$ (bank index), bound on `exchange-network`: A triple of three-element subsets of [h] indexing the bank entries (not a shift exponent here).
- $N$ (bank size), bound on `exchange-network`: The number of entries in each data bank.
- $m$ (label dimension), bound on `exchange-network`: The dimension of the label space used on later pages.
- $I$ (number of invocations), bound on `exchange-network`: The number of invocations in the three stages.
- $W_{\rm c}$ (complex wire count), bound on `exchange-network`: The total number of wires in the complex network.
- $t$ (gate input count), bound on `array-frames`: The number of input arrays of a gate.
- $q$ (sequence length), bound on `convolution`: The number of entries in each of the two sequences being convolved.
- $d$ (axis count), bound on `convolution`: The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $u$ (first input), bound on `radix-digit-reduction`: The first of the two integers being multiplied.
- $v$ (second input), bound on `radix-digit-reduction`: The second of the two integers being multiplied.
- $b$ (digit width), bound on `radix-digit-reduction`: The number of bits in one radix digit.
- $q$ (digit count), bound on `radix-digit-reduction`: The number of radix-2^b digits in each input.
- $x$ (polynomial variable), bound on `radix-digit-reduction`: The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $f$ (first array), bound on `phase-twist`: The first complex array being convolved.
- $g$ (second array), bound on `phase-twist`: The second complex array being convolved with f.
- $d$ (axis count), bound on `phase-twist`: The number of axes of the arrays.
- $k$ (coefficient index), bound on `phase-twist`: An index of a coefficient (not an operation count).
- $j$ (wrapped position), bound on `phase-twist`: The position k+l reduced modulo r.
- $q$ (sequence length), bound on `dft`: The number of entries of a sequence.
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to be transformed.
- $t$ (transform length), bound on `butterfly`: The number of positions in the sequence being transformed, a power of two.
- $m$ (output index), bound on `butterfly`: The index of an output of the transform.
- $b$ (lowest bit), bound on `butterfly`: The lowest bit of the output index m.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis, a power of two dividing 2r.
- $V$ (array volume), bound on `stream-ops`: The number of radix-q digits an array stores.
- $q$ (radix), bound on `stream-ops`: The number of values one digit can take.
- $P$ (prefix values), bound on `stream-ops`: The number of prefix values indexing the first axis of the array.
- $B$ (entries per row), bound on `stream-ops`: The number of entries in each row.
- $W$ (stream count), bound on `stream-ops`: The fixed number of streams the rows are dealt into.
- $a$ (chirp), bound on `chirp`: The chirp, a phase quadratic in the index.
- $a$ (round count), bound on `frequency-order`: The number of rounds of the transform, a=log_2 t.
- $j$ (output index), bound on `frequency-order`: The position of an output of the transform.
- $s$ (completed rounds), bound on `frequency-order`: The number of rounds completed so far.
- $N$ (factor bit length), bound on `hvdh-multiplier`: The number of bits in each of the two integers given to the established multiplier.
- $q$ (prime modulus base), bound on `controlled-shifts`: A fixed prime; on this page it is not a sequence length.
- $b$ (field digit count), bound on `controlled-shifts`: The number of base-$q$ digits of a field.
- $a$ (offset), bound on `controlled-shifts`: The offset in [Q] added to the target field, prepared from the control values.
- $B$ (suffix bit count), bound on `controlled-shifts`: The number of bits following the target field.
- $c$ (scaling integer), bound on `controlled-shifts`: A fixed positive integer prime to q by which the target field is multiplied; not the machine constant.
- $j$ (wrap count), bound on `controlled-shifts`: The integer part of cy/Q, counting how often cy wraps past Q.
- $m$ (fields per group), bound on `matrix-shear`: The number of fields in each of the groups H and D.
- $a$ (rank of A), bound on `matrix-shear`: The rank of the rational matrix A.
- $H$ (target group), bound on `matrix-shear`: The first group of m fields, which receives AD.
- $a$ (kernel coefficient a), bound on `phase-kernel`: The complex constant (1+i)/2, the coefficient of the identity in C.
- $b$ (kernel coefficient b), bound on `phase-kernel`: The complex constant (1-i)/2, the coefficient of the bit flip in C.
- $I$ (identity matrix), bound on `phase-kernel`: The 2 by 2 identity matrix.
- $X$ (bit flip), bound on `phase-kernel`: The 2 by 2 matrix swapping the two entries of a pair.
- $C$ (two-point kernel), bound on `phase-kernel`: The 2 by 2 matrix aI+bX.
- $H$ (normalized Hadamard matrix), bound on `phase-kernel`: The matrix sqrt(2) H_0, symmetric with H squared equal to the identity.
- $L$ (linear map), bound on `contraction-maps`: A linear map whose norm bound is being defined.
- $f$ (first operand), bound on `contraction-maps`: The first operand of the bilinear map.
- $g$ (second operand), bound on `contraction-maps`: The second operand of the bilinear map.
- $i$ (axis index), bound on `multidim-transform`: The index of an axis of the array, from 1 to d.
- $j$ (index tuple), bound on `multidim-transform`: The tuple of coordinates (j_1,...,j_d) of an entry of the array.
- $k$ (output index tuple), bound on `multidim-transform`: An output index tuple shaped like j.
- $d$ (number of axes), bound on `crt-map`: The number of axes of the target ring.
- $i$ (axis index), bound on `crt-map`: The index of an axis, from 1 to d.
- $V$ (stream volume), bound on `crt-map`: The volume of the stream being moved, Tp bits.
- $k$ (coefficient index), bound on `crt-map`: The index of a coefficient of the length-S sequence.
- $s$ (source length), bound on `gaussian-resampling`: The length of the Fourier transform to be replaced.
- $C$ (coordinate selection), bound on `gaussian-resampling`: The map from C^t to C^s that selects coordinate q_j into position j.
- $k$ (output coordinate index), bound on `gaussian-resampling`: A coordinate index of a vector in C^t, taken modulo t.
- $t$ (target length), bound on `gaussian-resampling`: The larger length, a power of two in the application, of the transform used instead of the length-s one.
- $z$ (vector), bound on `retained-permutations`: A vector of q complex entries being transformed.
- $c$ (unit), bound on `retained-permutations`: An integer that is a unit modulo q, used to permute coordinates by z_{cj}.
- $g$ (setup degree), bound on `retained-permutations`: A fixed exponent such that setup work per line is O(p^g).
- $u$ (first array), bound on `retained-permutations`: A complex array (not an integer) in the resampling and convolution identities of this page.
- $v$ (second array), bound on `retained-permutations`: A complex array (not an integer) in the resampling and convolution identities of this page.
- $L$ (log of padded length), bound on `precision-recovery`: The base-2 logarithm of the padded length $T$.
- $u$ (scaled digit array), bound on `precision-recovery`: The array of scaled radix digits of the first input, each stored as its value times $2^{-b-2}$ (not the integer).
- $v$ (scaled digit array), bound on `precision-recovery`: The array of scaled radix digits of the second input (not the integer).
- $j$ (coefficient index), bound on `precision-recovery`: The index of the product coefficient being processed during carry propagation.
- $V$ (bit volume), bound on `parameter-choice`: The number of bits of the logical array the layer acts on.
- $c$ (chunk-width exponent), bound on `parameter-choice`: The exponent of the address-chunk width (a new meaning of c).
- $E$ (first space), bound on `tensor-product-of-spaces`: The first of the two finite-dimensional vector spaces being tensored.
- $C$ (second ambient space), bound on `tensor-product-of-spaces`: A finite-dimensional space with a nondegenerate form, containing the subspace Q.
- $P$ (subspace of A), bound on `tensor-product-of-spaces`: A subspace of A, later taken nondegenerate.
- $B$ (orthogonal complement), bound on `tensor-product-of-spaces`: The orthogonal complement of P in A.
- $F$ (base space), bound on `tensor-product-of-spaces`: A space of dimension h with a nondegenerate form, whose triple power is the label space.
- $s$ (number of smaller calls), bound on `subspace-labels`: The total number of smaller calls that the edges of the network cost.
- $W$ (wire count), bound on `subspace-labels`: The number of wires of the network under consideration.
- $U$ (a label subspace), bound on `subspace-labels`: A subspace of the label space, such as the label of a vertex.
- $F$ (one-factor label space), bound on `subspace-labels`: The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $x$ (vector of F), bound on `subspace-labels`: A vector of $F$, the first argument of the bilinear form.
- $\mathcal F$ (ambient label space), bound on `subspace-labels`: The space $F^{\otimes3}$, of dimension $m=h^3$, in which all labels lie.
- $X$ (X bank), bound on `subspace-labels`: The bank of data wires $X_a$.
- $Y$ (Y bank), bound on `subspace-labels`: The bank of data wires $Y_a$.
- $U_a$ (terminal line), bound on `subspace-labels`: The line spanned by $t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, the source label of $X_a$.
- $L$ (total dimension loss), bound on `subspace-labels`: The total number of dimensions lost on decreasing edges.
- $j$ (stage number), bound on `subspace-labels`: The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
- $P$ (earlier tensor line), bound on `subspace-labels`: The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on `subspace-labels`: The orthogonal complement of $P$ inside $A$.
- $L_{\rm c}$ (complex dimension loss), bound on `subspace-labels`: The total dimension lost on decreasing edges of the complex network.
- $V$ (larger label), bound on `subspace-labels`: A label containing the label $U$ at the other end of an edge.
- $s_{\rm c}$ (complex smaller calls), bound on `subspace-labels`: The number of smaller calls, the total number of phase kernels, in the complex network.
- $m$ (label dimension), bound on `rank-recurrence`: The dimension of the label space, 10^6, which is also the number of slots a chunk is split into, so a parameter grows by the factor m per recursion level.
- $s$ (number of smaller calls), bound on `rank-recurrence`: The number of calls at parameter f that one call at parameter mf makes, equal to the total rank of the frame changes over the network's edges.
- $f$ (call parameter), bound on `rank-recurrence`: The size parameter of a call: the number of digits in each interchanged chunk, or the number of selected axes of a layer.
- $F$ (time per unit volume), bound on `rank-recurrence`: The running time of a call at a given parameter divided by the volume of its stream.
- $j$ (recursion depth), bound on `rank-recurrence`: The number of recursion levels between the top call and a given call.
- $u$ (chunk width), bound on `address-interchange`: The number of bits in each of the two interchanged address chunks.
- $V$ (array volume), bound on `address-interchange`: The number of bits stored in the array.
- $p$ (prefix), bound on `address-interchange`: The part of an address before the first chunk.
- $g$ (gap), bound on `address-interchange`: The part of an address between the two chunks.
- $d$ (second chunk), bound on `address-interchange`: The second of the two address chunks being interchanged.
- $z$ (suffix), bound on `address-interchange`: The part of an address after the second chunk.
- $q$ (digit radix), bound on `address-interchange`: The fixed prime that is the radix of the digits.
- $k$ (recursion levels), bound on `address-interchange`: The number of recursion levels, with e = m^k.
- $i$ (edge index), bound on `address-interchange`: The index of an edge of the network.
- $w$ (wire index), bound on `address-interchange`: The index of an input wire of the network.
- $x$ (stream row), bound on `address-interchange`: The row number within a role stream.
- $j$ (recursion level), bound on `address-interchange`: The index of a recursion level in the unrolled recurrence.

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

## Page to audit (`phase-frames`)

````markdown
# Binary phase frames

Binary phase frames are operators attached to the labels of [Nested subspace labels and rank deficit](subspace-labels.md) in the complex network, chosen so that every edge difference splits into one two-point kernel per dimension of change, which makes each residual dimension one smaller call of a butterfly-type operation, as the recursion needs.

Labels are subspaces of $\mathbb F_2^m$ ($m$ the label dimension), and $u,v,w,z$ are vectors of $\mathbb F_2^m$ here. The support $\operatorname{supp}(z)$ of a vector is the set of coordinates where it is $1$. Write $\operatorname{wt}(x)=|\operatorname{supp}(x)|$ for the Hamming weight, $[b]\in\{0,1\}$ for the integer representative of $b\in\mathbb F_2$, $P_U$ for projection onto a label $U$, and $z\cdot w$ for the dot product, both over $\mathbb F_2$. A vector $v$ has binary norm one when $v\cdot v=1$, equivalently $\operatorname{wt}(v)$ is odd; a basis is orthonormal when its vectors have norm one and are pairwise orthogonal. Let $X_v$ be the translation $(X_vf)(x)=f(x+v)$, and $C=H\operatorname{diag}(1,i)H=aI+bX$ with $a=\frac{1+i}{2}$, $b=\frac{1-i}{2}$, where $H=\tfrac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$.

For a label $U$ put $q_U(x)=\operatorname{wt}(P_Ux)\bmod 4$, with the projection taken over $\mathbb F_2$. The phase frame is $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$, with Gaussian-dyadic entries. (cited)

## Weight modulo four

For binary vectors $z,w$, $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|$, since a coordinate in both supports holds $1+1=0$. If $z\cdot w=0$ the intersection cardinality is even, so weight is additive modulo four on orthogonal vectors.

Take an edge from $U$ to $V=U\perp E$, where $E$, the edge residual, has orthonormal basis $\mathcal B$. Then $P_Vx=P_Ux+\sum_{v\in\mathcal B}[v\cdot x]\,v$, a sum of pairwise orthogonal vectors. So $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod 4$, negated on a decreasing edge, and each $\operatorname{wt}(v)$ is odd. Each term is therefore $\varepsilon[v\cdot x]$ with $\varepsilon=\pm1$ modulo four, the sign including the edge direction. The function $i^{\varepsilon[v\cdot x]}$ equals $\frac{1+i^\varepsilon}2+\frac{1-i^\varepsilon}2(-1)^{v\cdot x}$, as checking $v\cdot x=0,1$ shows.

## From phases to kernels

Since $H^2=I$, $\mathcal C_V\mathcal C_U^{-1}=H^{\otimes m}\operatorname{diag}(i^{q_V-q_U})H^{\otimes m}$, a product over $\mathcal B$. The character $(-1)^{v\cdot x}$ is $\operatorname{diag}(1,-1)$ on the coordinates in $\operatorname{supp}(v)$. Since $H\operatorname{diag}(1,-1)H=X$, the character $(-1)^{v\cdot x}$ becomes the translation $X_v$, so the phase becomes $aI+bX_v$ or its inverse. For $\varepsilon=-1$ the coefficients swap, giving $bI+aX_v$, the inverse because $a^2+b^2=0$ and $2ab=1$. Each edge factor is a translate $aI+bX_v$ of [Two-point kernel C](phase-kernel.md), one per basis vector.

Let $L_{\rm c}$ be the total dimension lost on decreasing edges, $N$ the bank size and $W_{\rm c}$ the wire count. The number of translation-kernel factors over the network is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}=1873807244636671267308000000<W_{\rm c}m$. (cited) The deficit of $s_{\rm c}$ from $W_{\rm c}m$ is $2N-2L_{\rm c}>0$, since $L_{\rm c}/N<\frac12$.

## Terminal pairs

Source and sink labels are $U_a\to\mathcal F$ on $X_a$, $0\to U_a^\perp$ on $Y_a$ and $0\to\mathcal F$ on scratch, with $U_a$ the line spanned by $u_a=t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$. For $k$ columns (an address is a $k$-tuple; $k$ changes meaning from the fixed-point page), [Frames on wire arrays](array-frames.md) gives each role the $k$th tensor power of the sink frame times the inverse source frame, with $X_a,Y_a$ exchanged. Label $0$ has frame $I$. For $\mathcal F$, $q_{\mathcal F}(x)=\operatorname{wt}(x)$ and $i^{\operatorname{wt}(x)}=\prod_ji^{x_j}$, so its frame is $C^{\otimes m}$. Only $X_a\to Y_a$ differs.

For it take $u=u_a$, with $3^3=27$ ones, so $u\cdot u=1$ and $P_{U_a}x=[u\cdot x]u$. Orthogonality of $P_{U_a}x$ and $P_{U_a^\perp}x$ gives $\operatorname{wt}(x)\equiv q_{U_a}+q_{U_a^\perp}$, hence $q_{U_a^\perp}-q_{U_a}=\operatorname{wt}(x)-2\operatorname{wt}(u)[u\cdot x]=\operatorname{wt}(x)+2[u\cdot x]\pmod 4$. As $2[u\cdot x]\equiv2\sum_{j\in\operatorname{supp}(u)}x_j$, the phase per coordinate is $i^{-x_j}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $i^{x_j}$ elsewhere, so the operator is $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $C$ elsewhere.

With $Z=\operatorname{diag}(1,-1)$ we have $ZXZ=-X$ and $C^{-1}=bI+aX$; since $ib=a$ and $ia=-b$, $C=iZC^{-1}Z$. Let $Z_{a,k}$ be $Z$ on those 27 coordinates in every column. Apply $Z_{a,k}$ before the network at $X_a$ and $i^{27k}Z_{a,k}$ after it at $Y_a$. The identity $C=iZC^{-1}Z$ turns each of the $27k$ inverse factors into $C$, so every role, including scratch roles, receives $C^{\otimes mk}$ once the physical $X$ outputs, which carry the minus sign of the scalar exchange, are negated and outputs are renamed to input roles.
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

Write the answer to `exegenius/tasks/0207-audit-phase-frames.answer.json`, then run `exegenius submit 0207-audit-phase-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0207-audit-phase-frames`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
