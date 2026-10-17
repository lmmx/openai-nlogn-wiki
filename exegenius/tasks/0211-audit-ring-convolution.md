# exegenius task 0211-audit-ring-convolution

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
- Simultaneous butterfly layer (also: parallel butterfly layer)
- Tape layout for synthetic transforms
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
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the grid on which stored values lie.
- $Q_p$ (truncation), bound on `fixed-point`: The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $h$ (ground-set size), bound on `exchange-network`: The size of the ground set [h] whose three-element subsets index the data.
- $\mathcal T$ (triple set), bound on `exchange-network`: The set of three-element subsets of [h].
- $v$ (number of triples), bound on `exchange-network`: The number of three-element subsets of [h].
- $\mathcal R$ (scatter map), bound on `exchange-network`: The linear map scattering central wires into the target.
- $I$ (number of invocations), bound on `exchange-network`: The number of invocations in the three stages.
- $R$ (scalar ring), bound on `array-frames`: The ring of scalars carried by the wires.
- $t$ (gate input count), bound on `array-frames`: The number of input arrays of a gate.
- $d$ (axis count), bound on `convolution`: The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $t_i$ (axis length), bound on `convolution`: The length of cyclic axis i.
- $M$ (address count), bound on `convolution`: The number of cyclic addresses of an array, the product of the axis lengths.
- $T$ (coefficient count), bound on `convolution`: The total number of complex coefficients in an array.
- $u$ (first input), bound on `radix-digit-reduction`: The first of the two integers being multiplied.
- $v$ (second input), bound on `radix-digit-reduction`: The second of the two integers being multiplied.
- $T$ (padded length), bound on `radix-digit-reduction`: A power of two with 4n/b <= T < 8n/b.
- $f$ (first array), bound on `phase-twist`: The first complex array being convolved.
- $g$ (second array), bound on `phase-twist`: The second complex array being convolved with f.
- $d$ (axis count), bound on `phase-twist`: The number of axes of the arrays.
- $\mathcal R_r$ (negacyclic ring), bound on `phase-twist`: The ring of polynomials modulo y^r+1.
- $h$ (wrap indicator), bound on `phase-twist`: Zero or one according to whether k+l wrapped past r.
- $\mathcal M_r$ (ring convolution), bound on `phase-twist`: Normalized convolution of the first d-1 axes over R_r, including division by T.
- $\|f\|$ (sup norm), bound on `phase-twist`: The largest modulus of a scalar coefficient of f.
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to be transformed.
- $t$ (transform length), bound on `butterfly`: The number of positions in the sequence being transformed, a power of two.
- $h$ (remaining index), bound on `butterfly`: The output index m with its lowest bit removed.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis, a power of two dividing 2r.
- $P$ (prefix values), bound on `stream-ops`: The number of prefix values indexing the first axis of the array.
- $R$ (row count), bound on `stream-ops`: The number of rows in the array of item 4.
- $B$ (entries per row), bound on `stream-ops`: The number of entries in each row.
- $Q$ (target permutation), bound on `chirp`: The permutation reordering the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $Q$ (field value count), bound on `controlled-shifts`: The number of values a field can take, q^b.
- $B$ (suffix bit count), bound on `controlled-shifts`: The number of bits following the target field.
- $I$ (identity matrix), bound on `phase-kernel`: The 2 by 2 identity matrix.
- $C$ (two-point kernel), bound on `phase-kernel`: The 2 by 2 matrix aI+bX.
- $L$ (linear map), bound on `contraction-maps`: A linear map whose norm bound is being defined.
- $\mathcal M$ (bilinear map), bound on `contraction-maps`: A map linear in each of its two operands.
- $f$ (first operand), bound on `contraction-maps`: The first operand of the bilinear map.
- $g$ (second operand), bound on `contraction-maps`: The second operand of the bilinear map.
- $i$ (axis index), bound on `multidim-transform`: The index of an axis of the array, from 1 to d.
- $\delta$ (time-bound slack), bound on `multidim-transform`: A fixed constant with 0<delta<1/8 that sets the slack in the exponent 3/2+delta of p in the time bound.
- $R$ (source permutation), bound on `multidim-transform`: The tensor product of the source index permutations P_{s_i}; here not the scalar ring.
- $Q$ (padded permutation), bound on `multidim-transform`: The tensor product of the index permutations P_{t_i}.
- $d$ (number of axes), bound on `crt-map`: The number of axes of the target ring.
- $i$ (axis index), bound on `crt-map`: The index of an axis, from 1 to d.
- $t_i$ (padded axis length), bound on `crt-map`: The padded length of axis i, either r/2 or r.
- $\ell$ (address bits), bound on `crt-map`: The base-2 logarithm of the record length r, the number of address bits of a full-width axis.
- $\tau$ (chunk-swap exponent), bound on `crt-map`: A fixed exponent below 1 in the cost of a chunk interchange.
- $T$ (padded record count), bound on `crt-map`: The number of padded records, the product of the t_i.
- $C$ (coordinate selection), bound on `gaussian-resampling`: The map from C^t to C^s that selects coordinate q_j into position j.
- $\delta$ (exponent slack), bound on `gaussian-resampling`: A fixed constant 0 < delta < 1/8 that is the slack in the exponents of the time bounds.
- $t$ (target length), bound on `gaussian-resampling`: The larger length, a power of two in the application, of the transform used instead of the length-s one.
- $z$ (vector), bound on `retained-permutations`: A vector of q complex entries being transformed.
- $h$ (summation index), bound on `retained-permutations`: The index of summation in the Fourier sum, substituted by ck.
- $g$ (setup degree), bound on `retained-permutations`: A fixed exponent such that setup work per line is O(p^g).
- $u$ (first array), bound on `retained-permutations`: A complex array (not an integer) in the resampling and convolution identities of this page.
- $v$ (second array), bound on `retained-permutations`: A complex array (not an integer) in the resampling and convolution identities of this page.
- $L$ (log of padded length), bound on `precision-recovery`: The base-2 logarithm of the padded length $T$.
- $u$ (scaled digit array), bound on `precision-recovery`: The array of scaled radix digits of the first input, each stored as its value times $2^{-b-2}$ (not the integer).
- $v$ (scaled digit array), bound on `precision-recovery`: The array of scaled radix digits of the second input (not the integer).
- $\tau$ (chunk-interchange exponent), bound on `parameter-choice`: The exponent in the cost of a chunk interchange.
- $\lambda$ (overhead exponent), bound on `parameter-choice`: The per-node overhead exponent.
- $\lambda'$ (final cost exponent), bound on `parameter-choice`: The final exponent of the cost V d^lambda' on bit volume V.
- $\delta$ (resampling slack), bound on `parameter-choice`: The slack in the exponent of the resampling cost.
- $K$ (chunk width), bound on `parameter-choice`: The width in bits of an address chunk.
- $\eta$ (prime window offset), bound on `parameter-choice`: The smallest relative distance at which a prime s_i may lie below t_i.
- $C$ (second ambient space), bound on `tensor-product-of-spaces`: A finite-dimensional space with a nondegenerate form, containing the subspace Q.
- $P$ (subspace of A), bound on `tensor-product-of-spaces`: A subspace of A, later taken nondegenerate.
- $Q$ (subspace of C), bound on `tensor-product-of-spaces`: A subspace of C.
- $B$ (orthogonal complement), bound on `tensor-product-of-spaces`: The orthogonal complement of P in A.
- $F$ (base space), bound on `tensor-product-of-spaces`: A space of dimension h with a nondegenerate form, whose triple power is the label space.
- $F$ (one-factor label space), bound on `subspace-labels`: The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $y$ (vector of F), bound on `subspace-labels`: A vector of $F$, the second argument of the bilinear form.
- $T$ (a triple), bound on `subspace-labels`: A three-element subset of $[h]$ (not the padded size used on other pages).
- $L$ (total dimension loss), bound on `subspace-labels`: The total number of dimensions lost on decreasing edges.
- $P$ (earlier tensor line), bound on `subspace-labels`: The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on `subspace-labels`: The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on `subspace-labels`: The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $f$ (call parameter), bound on `rank-recurrence`: The size parameter of a call: the number of digits in each interchanged chunk, or the number of selected axes of a layer.
- $F$ (time per unit volume), bound on `rank-recurrence`: The running time of a call at a given parameter divided by the volume of its stream.
- $\eta$ (relative deficit), bound on `rank-recurrence`: The relative rank deficit (Wm - s)/(Wm) of a network, the fraction by which the number of smaller calls falls short of Wm.
- $u$ (chunk width), bound on `address-interchange`: The number of bits in each of the two interchanged address chunks.
- $\tau$ (saving exponent), bound on `address-interchange`: The fixed exponent below 1 in the cost, equal to 1 - 2^{-50}.
- $p$ (prefix), bound on `address-interchange`: The part of an address before the first chunk.
- $h$ (first chunk), bound on `address-interchange`: The first of the two address chunks being interchanged.
- $g$ (gap), bound on `address-interchange`: The part of an address between the two chunks.
- $d$ (second chunk), bound on `address-interchange`: The second of the two address chunks being interchanged.
- $z$ (suffix), bound on `address-interchange`: The part of an address after the second chunk.
- $M$ (vertex matrix), bound on `address-interchange`: The rational m by m matrix carried by a terminal or gate of the network.
- $i$ (edge index), bound on `address-interchange`: The index of an edge of the network.
- $v$ (binary vector), bound on `phase-frames`: A vector of F_2^m; in the main argument a basis vector of an edge residual. Here v does not mean the triple count.
- $Z$ (sign matrix), bound on `phase-frames`: The diagonal matrix diag(1,-1).
- $u$ (first integer), bound on `packed-bit-addition`: The integer updated by lines 1, 3, 6 and 8 of the eight additions.
- $R$ (record bits), bound on `packed-bit-addition`: The number of bits in the record at each address.
- $L$ (chunk bits), bound on `packed-bit-addition`: The number of bits in each of the chunks x, y, z, equal to fK.
- $K$ (segment spacing), bound on `packed-bit-addition`: The spacing between selected positions, at least 6, which is the length of each segment.
- $f$ (selected bit count), bound on `packed-bit-addition`: The number of selected bits per chunk.
- $M$ (address count), bound on `packed-bit-addition`: The number of addresses.
- $g$ (guard value), bound on `packed-bit-addition`: The guard value of a segment, any g_i or h_i: its high K-1 bits.
- $z$ (array), bound on `simultaneous-layer`: The array of records that the operators act on.
- $h$ (slot index), bound on `simultaneous-layer`: The index of a slot and of the residual basis vector placed in it.
- $B$ (level factor), bound on `simultaneous-layer`: The number s+E by which each recursion level multiplies the chain bound.
- $\ell$ (depth), bound on `simultaneous-layer`: The depth of a value, the number of operations in sequence that produced it.
- $K$ (chunk width), bound on `transform-layout`: The number of bits in an address chunk.
- $\tau$ (interchange exponent), bound on `transform-layout`: The fixed exponent below 1 in the cost of the chunk interchange.
- $\lambda'$ (layer exponent), bound on `transform-layout`: The fixed exponent below 1 in the cost of the simultaneous layer.
- $\ell$ (long-axis address bits), bound on `transform-layout`: The base-2 logarithm of r, the number of address bits of a long axis.
- $B$ (bit reversal), bound on `transform-layout`: The bit-reversal permutation applied along every axis.
- $L$ (layout permutation), bound on `transform-layout`: The record permutation made by the prefix moves and chunk exchanges.
- $z$ (round input), bound on `transform-layout`: The array entering a round.

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

## Page to audit (`ring-convolution`)

````markdown
# Convolution from the retained transform layout

Convolution over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ on the remaining axes is computed by transforming both operands, multiplying records pointwise and transforming back.

Arrays are indexed by $\prod_i\mathbb Z/t_i\mathbb Z$ over the $d-1$ remaining axes, with values in $\mathcal R_r$. Let $M=\prod_i t_i$ be the number of records, $T=rM$ the number of complex coefficients, and $*$ cyclic convolution. $\|\cdot\|_\infty$ is the largest coefficient modulus in the array. A disk array has norm at most $1$; a disk grid array also has parts that are multiples of $2^{-p}$. Multiplying by a power of $y$ permutes coefficients and changes signs, so it preserves the norm.

For arrays over $\mathcal R_r$ define $\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}$. A fixed output coefficient averages $rM$ signed scalar products (cited), so $\mathcal M_r$ is a bilinear contraction, $\|\mathcal M_r(f,g)\|_\infty\le\|f\|_\infty\|g\|_\infty$.

Let $F^-$, $F^+$ be the forward and opposite synthetic transforms. Each output entry is an average of images of the inputs under powers of $y$, so both are contractions (cited) Expansion of the finite sums gives $F^-(f*g)=M(F^-f)(F^-g)$. With $F^+F^-=I/M$ ([Discrete Fourier transform](dft.md)), it follows that $MF^+\bigl((F^-f)(F^-g)/r\bigr)=f*g/(rM)$. Write $P(u,v)=uv/r$ for the pointwise product. Each coefficient of $uv$ in $\mathcal R_r$ is a signed sum of $r$ products of coefficients, so $\|P(u,v)\|_\infty\le\|u\|_\infty\|v\|_\infty$, and $P$ is bilinear.

The transforms are laid out as in [Tape layout for synthetic transforms](transform-layout.md). Perform both forward transforms and retain their common $LB$ order, with $L$ the layout permutation of records and $B$ the bit-reversal order. Their exact counterparts are $LBF^-$ and the opposite map $\mathcal T_+=F^+B^{-1}L^{-1}$; permuting records preserves the norm, so $\mathcal T_+$ is a contraction. With $\ell=\log_2r$, each procedure maps disk grid arrays to disk grid arrays with error less than $\delta=\sqrt2\ell\,2^{-p}$ (cited). Multiply the $M$ record pairs pointwise there, apply the opposite procedure to that order, and multiply by $M$. Since $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so $\mathcal T_+$ applied to the pointwise product of the stored forward outputs equals $F^+P(F^-f,F^-g)$; its scaling by $M$ is $\mathcal M_r(f,g)$. The procedure keeps the retained order of [Retained frequency order](frequency-order.md), passing the product to the opposite transform without reordering.

Each record product is formed by [Signed packing](signed-packing.md) in $O(rp\log(rp))$ time, truncated by $Q_p$ to $p$ bits of precision, which changes it by less than $\eta=\sqrt2\,2^{-p}$ without raising the norm. There are $M=T/r$ products, so their total cost is $O(Tp\log(rp))$,. Each transform, and the final linear scaling, costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$, with $K$ the layout chunk width and $\tau,\lambda'$ exponents from the cost lemma.

Let $u,v$ be the exact stored forward outputs and $\widetilde u,\widetilde v$ the returned ones, all disk arrays. By bilinearity, $P(\widetilde u,\widetilde v)-P(u,v)=P(\widetilde u-u,\widetilde v)+P(u,\widetilde v-v)$. By the contraction bound for $P$, and norm at most $1$ of $\widetilde v$ and $u$, each term is less than $\delta$, so $\|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty<2\delta$. With $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$, truncation gives $\|\widetilde z-z_*\|_\infty<2\delta+\eta$, and $\widetilde z$ is a disk grid array. The opposite procedure returns $\widetilde h$ with $\|\widetilde h-\mathcal T_+\widetilde z\|_\infty<\delta$, and $\|\mathcal T_+(\widetilde z-z_*)\|_\infty\le\|\widetilde z-z_*\|_\infty$ since $\mathcal T_+$ is a contraction. The triangle inequality gives $\|\widetilde h-\mathcal T_+z_*\|_\infty<3\delta+\eta$. The exact multiplication by $M$ gives total error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$ (cited)
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

Write the answer to `exegenius/tasks/0211-audit-ring-convolution.answer.json`, then run `exegenius submit 0211-audit-ring-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0211-audit-ring-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
