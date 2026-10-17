# exegenius task 0204-audit-subspace-labels

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
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
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

- $y$ (ring variable), bound on `ring-y`: The indeterminate of the polynomials; it satisfies y^r = -1 in the ring.
- $r$ (record length), bound on `ring-y`: The number of complex coefficients in a polynomial of the ring, always a power of two.
- $n$ (bit length), bound on `conjecture`: The number of bits in each of the two integers being multiplied.
- $c$ (machine constant), bound on `conjecture`: A positive constant, depending on the machine, in the lower bound c n log n.
- $k$ (depth), bound on `fixed-point`: The number of operations in sequence since the layer began that produced a value.
- $h$ (ground-set size), bound on `exchange-network`: The size of the ground set [h] whose three-element subsets index the data.
- $v$ (number of triples), bound on `exchange-network`: The number of three-element subsets of [h].
- $X$ (bank X), bound on `exchange-network`: The first data bank, with entries X_a.
- $Y$ (bank Y), bound on `exchange-network`: The second data bank, with entries Y_a.
- $a$ (bank index), bound on `exchange-network`: A triple of three-element subsets of [h] indexing the bank entries (not a shift exponent here).
- $N$ (bank size), bound on `exchange-network`: The number of entries in each data bank.
- $m$ (label dimension), bound on `exchange-network`: The dimension of the label space used on later pages.
- $S$ (slice index), bound on `exchange-network`: A three-element subset of [h]: the varying coordinate of a within a slice.
- $I$ (number of invocations), bound on `exchange-network`: The number of invocations in the three stages.
- $z_{\rm b}$ (bit neighbour count), bound on `exchange-network`: The number of neighbours of a fixed triple in the bit construction.
- $c_{\rm b}$ (bit central wires), bound on `exchange-network`: The number of central wires per invocation in the bit network.
- $c_{\rm c}$ (complex central wires), bound on `exchange-network`: The number of central wires per invocation in the complex network.
- $W_{\rm b}$ (bit wire count), bound on `exchange-network`: The total number of wires in the bit network.
- $W_{\rm c}$ (complex wire count), bound on `exchange-network`: The total number of wires in the complex network.
- $t$ (gate input count), bound on `array-frames`: The number of input arrays of a gate.
- $d$ (axis count), bound on `convolution`: The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $T$ (coefficient count), bound on `convolution`: The total number of complex coefficients in an array.
- $u$ (first input), bound on `radix-digit-reduction`: The first of the two integers being multiplied.
- $v$ (second input), bound on `radix-digit-reduction`: The second of the two integers being multiplied.
- $n$ (input bit length), bound on `radix-digit-reduction`: The number of bits in each input.
- $b$ (digit width), bound on `radix-digit-reduction`: The number of bits in one radix digit.
- $T$ (padded length), bound on `radix-digit-reduction`: A power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on `radix-digit-reduction`: The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $x$ (polynomial variable), bound on `radix-digit-reduction`: The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $g$ (second array), bound on `phase-twist`: The second complex array being convolved with f.
- $d$ (axis count), bound on `phase-twist`: The number of axes of the arrays.
- $k$ (coefficient index), bound on `phase-twist`: An index of a coefficient (not an operation count).
- $l$ (second coefficient index), bound on `phase-twist`: An index of a coefficient of the second factor.
- $j$ (wrapped position), bound on `phase-twist`: The position k+l reduced modulo r.
- $h$ (wrap indicator), bound on `phase-twist`: Zero or one according to whether k+l wrapped past r.
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to be transformed.
- $t$ (transform length), bound on `butterfly`: The number of positions in the sequence being transformed, a power of two.
- $m$ (output index), bound on `butterfly`: The index of an output of the transform.
- $b$ (lowest bit), bound on `butterfly`: The lowest bit of the output index m.
- $h$ (remaining index), bound on `butterfly`: The output index m with its lowest bit removed.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis, a power of two dividing 2r.
- $e$ (two-adic exponent), bound on `synthetic-transform`: The exponent of 2 in j when j is written as 2^e times an odd number.
- $V$ (array volume), bound on `stream-ops`: The number of radix-q digits an array stores.
- $P$ (prefix values), bound on `stream-ops`: The number of prefix values indexing the first axis of the array.
- $B$ (entries per row), bound on `stream-ops`: The number of entries in each row.
- $W$ (stream count), bound on `stream-ops`: The fixed number of streams the rows are dealt into.
- $Q$ (target permutation), bound on `chirp`: The permutation reordering the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $a$ (chirp), bound on `chirp`: The chirp, a phase quadratic in the index.
- $a$ (round count), bound on `frequency-order`: The number of rounds of the transform, a=log_2 t.
- $j$ (output index), bound on `frequency-order`: The position of an output of the transform.
- $s$ (completed rounds), bound on `frequency-order`: The number of rounds completed so far.
- $N$ (factor bit length), bound on `hvdh-multiplier`: The number of bits in each of the two integers given to the established multiplier.
- $b$ (field digit count), bound on `controlled-shifts`: The number of base-$q$ digits of a field.
- $Q$ (field value count), bound on `controlled-shifts`: The number of values a field can take, q^b.
- $a$ (offset), bound on `controlled-shifts`: The offset in [Q] added to the target field, prepared from the control values.
- $B$ (suffix bit count), bound on `controlled-shifts`: The number of bits following the target field.
- $c$ (scaling integer), bound on `controlled-shifts`: A fixed positive integer prime to q by which the target field is multiplied; not the machine constant.
- $j$ (wrap count), bound on `controlled-shifts`: The integer part of cy/Q, counting how often cy wraps past Q.
- $m$ (fields per group), bound on `matrix-shear`: The number of fields in each of the groups H and D.
- $a$ (rank of A), bound on `matrix-shear`: The rank of the rational matrix A.
- $A$ (shear matrix), bound on `matrix-shear`: A rational m by m matrix, taken from a fixed finite set, that the shear applies.
- $a$ (kernel coefficient a), bound on `phase-kernel`: The complex constant (1+i)/2, the coefficient of the identity in C.
- $b$ (kernel coefficient b), bound on `phase-kernel`: The complex constant (1-i)/2, the coefficient of the bit flip in C.
- $I$ (identity matrix), bound on `phase-kernel`: The 2 by 2 identity matrix.
- $X$ (bit flip), bound on `phase-kernel`: The 2 by 2 matrix swapping the two entries of a pair.
- $L$ (linear map), bound on `contraction-maps`: A linear map whose norm bound is being defined.
- $g$ (second operand), bound on `contraction-maps`: The second operand of the bilinear map.
- $i$ (axis index), bound on `multidim-transform`: The index of an axis of the array, from 1 to d.
- $j$ (index tuple), bound on `multidim-transform`: The tuple of coordinates (j_1,...,j_d) of an entry of the array.
- $k$ (output index tuple), bound on `multidim-transform`: An output index tuple shaped like j.
- $Q$ (padded permutation), bound on `multidim-transform`: The tensor product of the index permutations P_{t_i}.
- $S$ (convolution length), bound on `crt-map`: The length of the cyclic convolution, the product of the s_i.
- $d$ (number of axes), bound on `crt-map`: The number of axes of the target ring.
- $i$ (axis index), bound on `crt-map`: The index of an axis, from 1 to d.
- $x_i$ (axis variable), bound on `crt-map`: The polynomial variable of axis i, with x_i^{s_i}=1.
- $a_j$ (mixed-radix digit), bound on `crt-map`: The j-th digit of k in mixed radix, 0 <= a_j < s_j.
- $V$ (stream volume), bound on `crt-map`: The volume of the stream being moved, Tp bits.
- $T$ (padded record count), bound on `crt-map`: The number of padded records, the product of the t_i.
- $k$ (coefficient index), bound on `crt-map`: The index of a coefficient of the length-S sequence.
- $s$ (source length), bound on `gaussian-resampling`: The length of the Fourier transform to be replaced.
- $k$ (output coordinate index), bound on `gaussian-resampling`: A coordinate index of a vector in C^t, taken modulo t.
- $t$ (target length), bound on `gaussian-resampling`: The larger length, a power of two in the application, of the transform used instead of the length-s one.
- $z$ (vector), bound on `retained-permutations`: A vector of q complex entries being transformed.
- $c$ (unit), bound on `retained-permutations`: An integer that is a unit modulo q, used to permute coordinates by z_{cj}.
- $h$ (summation index), bound on `retained-permutations`: The index of summation in the Fourier sum, substituted by ck.
- $g$ (setup degree), bound on `retained-permutations`: A fixed exponent such that setup work per line is O(p^g).
- $u$ (first array), bound on `retained-permutations`: A complex array (not an integer) in the resampling and convolution identities of this page.
- $v$ (second array), bound on `retained-permutations`: A complex array (not an integer) in the resampling and convolution identities of this page.
- $L$ (log of padded length), bound on `precision-recovery`: The base-2 logarithm of the padded length $T$.
- $u$ (scaled digit array), bound on `precision-recovery`: The array of scaled radix digits of the first input, each stored as its value times $2^{-b-2}$ (not the integer).
- $v$ (scaled digit array), bound on `precision-recovery`: The array of scaled radix digits of the second input (not the integer).
- $j$ (coefficient index), bound on `precision-recovery`: The index of the product coefficient being processed during carry propagation.
- $V$ (bit volume), bound on `parameter-choice`: The number of bits of the logical array the layer acts on.
- $c$ (chunk-width exponent), bound on `parameter-choice`: The exponent of the address-chunk width (a new meaning of c).
- $K$ (chunk width), bound on `parameter-choice`: The width in bits of an address chunk.
- $A$ (ambient space), bound on `tensor-product-of-spaces`: A finite-dimensional space with a nondegenerate form, containing the subspace P.
- $P$ (subspace of A), bound on `tensor-product-of-spaces`: A subspace of A, later taken nondegenerate.
- $Q$ (subspace of C), bound on `tensor-product-of-spaces`: A subspace of C.
- $B$ (orthogonal complement), bound on `tensor-product-of-spaces`: The orthogonal complement of P in A.
- $F$ (base space), bound on `tensor-product-of-spaces`: A space of dimension h with a nondegenerate form, whose triple power is the label space.

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

## Page to audit (`subspace-labels`)

````markdown
# Nested subspace labels and rank deficit

Nested subspace labels give each vertex of the [exchange network](exchange-network.md) a subspace of an $m$-dimensional space, nested along every edge, whose dimension changes count each edge's *smaller calls*, recursive calls at an $m$ times smaller parameter. The labelling chooses the frames of [Frames on wire arrays](array-frames.md) so that $W$ wires cost $s<Wm$ smaller calls, the saving the recursion needs.

A subspace $U$ is *nondegenerate* when the form restricted to it is, so the space is $U\perp U^\perp$. Bit labels live in $F=\mathbb Q^h$, where $h=100$ (cited), with the form $\langle x,y\rangle=x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for vectors $x,y\in F$. Its matrix fixes zero-sum vectors and scales the all-ones vector by $1-h/9=-91/9\neq0$, so it is nondegenerate. Complex labels live in $F=\mathbb F_2^h$ with the dot product. For *triples* (three-element subsets of $[h]$) $S,T$, indicator vectors $t_S,t_T$ have integer dot product $|S\cap T|$ and entry sum $3$, so $\langle t_S,t_T\rangle=|S\cap T|-1$; over $\mathbb F_2$, $t_S\cdot t_T=|S\cap T|\bmod 2$. Each line $\langle t_T\rangle$ is thus nondegenerate ($\langle t_T,t_T\rangle\in\{2,1\}$), and *neighbours* (bit: sharing one element; complex: distinct with even intersection) are orthogonal.

Labels are built as [tensor products of subspaces](tensor-product-of-spaces.md) inside $\mathcal F=F^{\otimes3}$, of dimension $m=h^3=10^6$, whose form multiplies factorwise. Banks $X$ and $Y$ hold data wires $X_a,Y_a$, indexed by the $N=v^3$ tuples $a=(a_1,a_2,a_3)$ of triples ($v=\binom h3=161700$). With $U_a=\langle t_{a_1}\otimes t_{a_2}\otimes t_{a_3}\rangle$ the terminal labels are

$$
\begin{array}{c|cc}&\text{source}&\text{sink}\\\hline X_a&U_a&\mathcal F\\ Y_a&0&U_a^\perp\\ \text{scratch}&0&\mathcal F\end{array}
$$

Source dimensions total $N$ and sink dimensions $Nm+N(m-1)+(W-2N)m=Wm-N$. A wire enters and leaves each gate with that gate's label, so its signed changes telescope to sink minus source dimension; over all wires they total $Wm-2N$. If decreasing edges lose $L$ dimensions, absolute changes total $Wm-2N+2L$, so labels must keep $L$ small.

In one invocation of stage $j$, which acts on coordinate $a_j$, put $A=F^{\otimes(j-1)},\ P=\langle t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}\rangle,\ B=P^\perp\cap A,\ K=\langle t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}\rangle$ (empty products are scalars). Data labels move

$$
X:\ A\otimes\langle t_{a_j}\rangle\otimes K\to A\otimes F\otimes K,\qquad Y:\ B\otimes\langle t_{a_j}\rangle\otimes K\to\bigl((B\otimes F)\perp(P\otimes t_{a_j}^\perp)\bigr)\otimes K.
$$

Splitting $A=B\perp P$ and $F=\langle t_{a_j}\rangle\perp t_{a_j}^\perp$ cuts $A\otimes F$ into four orthogonal nondegenerate pieces; the complement of $P\otimes\langle t_{a_j}\rangle$ is the other three: $(P\otimes\langle t_{a_j}\rangle)^\perp_{A\otimes F}=(B\otimes F)\perp(P\otimes t_{a_j}^\perp)$. It is the next stage's $B'$, for $A'=A\otimes F$ and $P'=P\otimes\langle t_{a_j}\rangle$; with $K=\langle t_{a_{j+1}}\rangle\otimes K'$ the outputs $A'\otimes\langle t_{a_{j+1}}\rangle\otimes K'$ and $B'\otimes\langle t_{a_{j+1}}\rangle\otimes K'$ are stage $j+1$'s inputs. Stage $1$ starts at $U_a,0$ ($B=0$) and stage $3$ ends at $\mathcal F,U_a^\perp$.

Gates act at times $0,\dots,7$, each giving all its wires one label. Suppressing $K$, with $t_X,t_Y$ the indicators of the $X$- and $Y$-bank triples involved (neighbours, for a side wire), wire labels (times bracketed) are

$$
\begin{aligned}\text{centre: }&0\to B\otimes F\,(1)\to A\otimes F\,(3)\to B\otimes F\,(4)\to A\otimes F\,(6)\to\mathcal F\\ \text{side: }&0\to B\otimes\langle t_Y\rangle\,(0)\to(B\otimes F)\perp(P\otimes\langle t_X\rangle)\,(2)\to(B\otimes F)\perp(P\otimes t_Y^\perp)\,(5)\to A\otimes F\,(7)\to\mathcal F\\ X:\ &A\otimes\langle t_X\rangle\to(B\otimes F)\perp(P\otimes\langle t_X\rangle)\,(2)\to A\otimes F\,(3,6,7)\\ Y:\ &B\otimes\langle t_Y\rangle\,(0)\to B\otimes F\,(1,4)\to(B\otimes F)\perp(P\otimes t_Y^\perp)\,(5)\end{aligned}
$$

The same splitting shows every arrow is an inclusion except centre $3\to4$, dropping $P\otimes F$ of dimension $h$; side $2\to5$ needs $\langle t_X\rangle\subset t_Y^\perp$, true as $t_X\perp t_Y$. Each of the $I=3v^2$ invocations ($v^2$ per stage) has one such edge per centre wire, so the losses are $L_{\rm b}=Ic_{\rm b}h$ and $L_{\rm c}=Ic_{\rm c}h$, with $c_{\rm b}=100$ (bit) and $c_{\rm c}=101$ (complex) centre wires per invocation (cited). As $N=v^3$, $L_{\rm b}/N=3c_{\rm b}h/v=30000/161700=100/539$; likewise $L_{\rm c}/N=30300/161700=101/539$. Both are below $1/2$.

Bit-network edges cost one smaller call per unit of rank of their endpoints' rational matrix difference (cited). A vertex labelled $U$ gets the projection $\Pi_U$ onto $U$ along $U^\perp$, except sources: $-\Pi_{U_a}$ at $X_a$, else $0$. For $U\subset V$, $\Pi_V-\Pi_U$ (identity on $V\cap U^\perp$, zero on $U\perp V^\perp$) has rank $\dim V-\dim U$, as does its negative. Only $X_a$'s first edge differs: at stage $1$ its first gate has label $U_a$, so $2\Pi_{U_a}$ has rank one where the dimension change is zero. Endpoint differences ($\Pi_{U_a^\perp}+\Pi_{U_a}$ from source $X_a$ to sink $Y_a$, else $\mathrm{Id}-0$) all equal $\mathrm{Id}$, giving every role the same shear. So $s_{\rm b}=(W_{\rm b}m-2N+2L_{\rm b})+N=W_{\rm b}m-(N-2L_{\rm b})<W_{\rm b}m$ (cited). [Binary phase frames](phase-frames.md) give the complex network $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}<W_{\rm c}m$.

The deficit $W_{\rm b}m-s_{\rm b}=N-2L_{\rm b}=\frac{339}{539}N$ is positive because $L_{\rm b}/N<1/2$, but tiny beside $W_{\rm b}m$. Each invocation also has $vz_{\rm b}$ side wires, one per ordered neighbour pair, where $z_{\rm b}=3\binom{97}2=13968$ counts a triple's neighbours (one shared element, two of the other $97$). Since $Iv=3N$ and $Ic_{\rm b}=N/539$, $W_{\rm b}=2N+I(vz_{\rm b}+c_{\rm b})=N(2+3z_{\rm b}+\frac1{539})=\frac{22587335}{539}N$ (cited), so the relative deficit is $\frac{339}{22587335\,m}=\frac{339}{22587335000000}\approx1.5\cdot10^{-11}$ (cited).
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

Write the answer to `exegenius/tasks/0204-audit-subspace-labels.answer.json`, then run `exegenius submit 0204-audit-subspace-labels` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0204-audit-subspace-labels`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
