# exegenius task 0075-audit-multiplication-algorithm

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
- Butterflies and the fast transform
- Multidimensional transforms
- Chinese-remainder address map (also: Agarwal–Cooley map)
- Gaussian resampling
- Bluestein chirp identity
- Retained permutation cancellation
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Synthetic polynomial transform (also: polynomial transform)
- Retained frequency order
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records
- Error tracking and exact recovery
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
- Two-point kernel C (also: phase network kernel)
- Binary phase frames
- Packed selected-bit addition
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
- Cartesian products and multi-index arrays (also: multidimensional arrays, row-major order, lexicographic order, mixed-radix index, index tuples, array stored on a tape)
- Directed acyclic graphs and networks of gates (also: circuit, DAG, wire, gate, edges and vertices, fan-in)
- Summation, geometric series and induction (also: geometric sum, proof by induction, summation notation, telescoping sum)
- Rounding to the nearest integer and exactness (also: rounding, truncation, round to nearest, rational numbers, dyadic rational)
- Multitape Turing machine running time (also: tape head movement, scanning a tape, linear-time pass over a tape, time complexity of a Turing machine, worst-case running time)
- Integer exponentials and tuple notation (also: powers of two, tensor power notation, exponent of a constant, fixed rational exponents)

## Symbols bound on earlier pages

- $y$ (ring variable), bound on `ring-y`: The indeterminate of the polynomials, satisfying y^r = -1 in the ring.
- $v$ (number of triples), bound on `exchange-network`: The number of three-element subsets of $[h]$.
- $R$ (scalar ring), bound on `array-frames`: The ring of scalars carried by the wires.
- $s$ (number of smaller calls), bound on `subspace-labels`: The total number of smaller calls that the network's edges cost.
- $F$ (one-factor label space), bound on `subspace-labels`: The space $\mathbb Q^h$ (bit network) or $\mathbb F_2^h$ (complex network) with its bilinear form.
- $j$ (stage number), bound on `subspace-labels`: The stage, 1, 2 or 3, whose invocations vary coordinate $a_j$.
- $A$ (exposed factor space), bound on `subspace-labels`: The tensor product $F^{\otimes(j-1)}$ of the factors already exposed before stage $j$.
- $B$ (complement of P), bound on `subspace-labels`: The orthogonal complement of $P$ inside $A$.
- $\gamma$ (central wires per invocation), bound on `subspace-labels`: The number of central wires in one invocation: 100 in the bit network, 101 in the complex one.
- $f$ (call parameter), bound on `rank-recurrence`: The parameter of a call: the number of digits in each of the two interchanged chunks, or the number of axes the butterfly layer acts on.
- $s$ (number of smaller calls), bound on `rank-recurrence`: The number of calls at parameter f made by a call at parameter mf: the total rank of the frame changes over all edges of the network.
- $F$ (normalized cost), bound on `rank-recurrence`: F(f) is the running time of a call at parameter f divided by its volume.
- $n$ (bit length), bound on `conjecture`: The number of bits in each of the two integers being multiplied.
- $q$ (radix), bound on `stream-ops`: The number of values one digit can take.
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the stored grid, so values are integers divided by 2^p.
- $Q_p$ (truncation), bound on `fixed-point`: The single truncation that drops the bits below 2^{-p} in each real and imaginary part.
- $p$ (precision bits), bound on `signed-packing`: The number of fractional bits in each coefficient component.
- $B_0$ (packing base), bound on `signed-packing`: The power of two $2^{4p}$ at which the polynomials are evaluated.
- $q$ (prime), bound on `controlled-shifts`: The prime base of the field arithmetic.
- $b$ (field digits), bound on `controlled-shifts`: The number of base-$q$ digits of a field.
- $Q$ (field size), bound on `controlled-shifts`: The number of values a field can hold, Q = q^b.
- $a$ (offset), bound on `controlled-shifts`: The offset added to the target field, prepared from the control values.
- $B$ (suffix length), bound on `controlled-shifts`: The number of bits following the target field.
- $A$ (shear matrix), bound on `matrix-shear`: The fixed rational m by m matrix whose action AD is added to H.
- $a$ (rank), bound on `matrix-shear`: The rank of the matrix A.
- $q$ (base prime), bound on `matrix-shear`: A fixed odd prime; fields are residues modulo q^b.
- $b$ (digits per field), bound on `matrix-shear`: The number of base-q digits in a field.
- $i$ (row index), bound on `matrix-shear`: The row of a one of Pi.
- $j$ (column index), bound on `matrix-shear`: The column of a one of Pi.
- $u$ (chunk width), bound on `address-interchange`: The number of bits in each of the two address chunks.
- $q$ (radix), bound on `address-interchange`: The fixed prime used as digit radix.
- $b$ (field width), bound on `address-interchange`: The number of digits in each field.
- $s$ (total edge rank), bound on `address-interchange`: The sum of the ranks of the edge matrices.
- $M$ (vertex matrix), bound on `address-interchange`: The matrix attached to a network vertex, determining its frame.
- $R$ (row range), bound on `address-interchange`: The range of the row field formed by the two high parts.
- $a_j$ (piece count), bound on `address-interchange`: The number of pieces of width m^j in the base-m expansion of e minus rho.
- $u$ (target integer), bound on `packed-bit-addition`: Integer whose parity is flipped by the eight additions.
- $w$ (auxiliary integer), bound on `packed-bit-addition`: Arbitrary auxiliary integer restored by the eight additions.
- $f$ (selected bits), bound on `packed-bit-addition`: Number of selected bits in each chunk.
- $M$ (address count), bound on `packed-bit-addition`: Number of addresses.
- $R$ (record length), bound on `packed-bit-addition`: Number of bits in a record.
- $\mathcal B$ (exceptional set), bound on `packed-bit-addition`: Set of addresses where some guard fails the interval test.
- $p$ (coefficient precision), bound on `packed-bit-addition`: Bit precision of the record coefficients.
- $q$ (sequence length), bound on `convolution`: The number of entries in each of the two sequences being convolved.
- $t_i$ (axis length), bound on `convolution`: The length of axis i of the array.
- $M$ (cyclic addresses), bound on `convolution`: The number of cyclic addresses on the first d-1 axes, the product of t_i for i<d.
- $T$ (total coefficients), bound on `convolution`: The total number of complex coefficients in an array, rM.
- $u$ (first input), bound on `radix-digit-reduction`: The first of the two integers being multiplied.
- $v$ (second input), bound on `radix-digit-reduction`: The second of the two integers being multiplied.
- $n$ (input bit length), bound on `radix-digit-reduction`: The number of bits in each input.
- $b$ (digit width), bound on `radix-digit-reduction`: The number of bits in one radix digit.
- $T$ (padded length), bound on `radix-digit-reduction`: A power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on `radix-digit-reduction`: The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $q$ (digit count), bound on `radix-digit-reduction`: The number of radix-2^b digits in each input.
- $x$ (polynomial variable), bound on `radix-digit-reduction`: The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $T$ (total entries), bound on `phase-twist`: The number of entries of the array f in all.
- $M$ (number of records), bound on `phase-twist`: The number of lines along the last axis, T/r.
- $\mathcal M_{\mathbb C}$ (normalized cyclic convolution), bound on `phase-twist`: The composite D_-\iota^{-1}\mathcal M_r(\iota D_+ f,\iota D_+ g), equal to f*g/T.
- $b$ (digit width), bound on `precision-recovery`: The number of bits in a radix digit.
- $p$ (fractional bits), bound on `precision-recovery`: The number of fractional bits of the fixed-point grid, equal to $6b$.
- $T$ (padded array size), bound on `precision-recovery`: The number of records in the padded array.
- $S$ (convolution length), bound on `precision-recovery`: The length of the cyclic convolution.
- $\gamma$ (source scale exponent), bound on `precision-recovery`: The exponent of the source-transform scale $2^\gamma$.
- $M$ (ring record count), bound on `precision-recovery`: The ratio $T/r$, the number of ring records.
- $q$ (digit count), bound on `precision-recovery`: The number of radix digits of an $n$-bit input.
- $q$ (sequence length), bound on `dft`: The number of complex entries in the sequences the transform acts on.
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to which the transform is applied.
- $t$ (transform length), bound on `butterfly`: The number of values in the transform, a power of two.
- $b$ (lowest output bit), bound on `butterfly`: The lowest bit of the output index, 0 or 1.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis of the transform, a power of two dividing 2r.
- $S$ (convolution length), bound on `crt-map`: The length of the cyclic convolution, the product of the axis lengths.
- $s_i$ (axis length), bound on `crt-map`: The length of axis i; the lengths are pairwise coprime.
- $a_j$ (mixed-radix digit), bound on `crt-map`: The j-th mixed-radix digit of the index k.
- $t_i$ (padded length), bound on `crt-map`: The padded length of axis i, a power of two at least s_i.
- $T$ (padded array size), bound on `crt-map`: The number of records in the padded array.
- $p$ (record precision), bound on `crt-map`: The number of bits of precision per record.
- $s$ (prime length), bound on `gaussian-resampling`: The prime length of the Fourier transform to be resampled, the number of complex coordinates it acts on.
- $t$ (power-of-two length), bound on `gaussian-resampling`: The power-of-two length of the nearby transform, the number of complex coordinates it acts on.
- $p$ (precision bits), bound on `gaussian-resampling`: The number of bits of precision of each real and imaginary component.
- $t_i$ (axis length), bound on `chirp`: The even number of entries along axis i.
- $s_i$ (coprime integer), bound on `chirp`: An integer coprime to t_i, scaling the frequency read along axis i.
- $T$ (total entries), bound on `chirp`: The total number of entries, the product of the t_i.
- $Q$ (target permutation), bound on `chirp`: The target permutation, reading frequency (-s_i j_i)_i at output position j.
- $a$ (chirp), bound on `chirp`: The chirp, a quadratic-phase array exp(-pi i sum s_i j_i^2/t_i).
- $s_i$ (prime length), bound on `retained-permutations`: The prime length of axis i.
- $t_i$ (power-of-two length), bound on `retained-permutations`: The power-of-two length of axis i.
- $S$ (product of prime lengths), bound on `retained-permutations`: The product of the prime lengths.
- $T$ (padded box size), bound on `retained-permutations`: The number of entries in the padded box, the product of the power-of-two lengths.
- $p$ (bit precision), bound on `retained-permutations`: The number of bits of precision of each coordinate.
- $R$ (source permutation), bound on `retained-permutations`: The source coordinate permutation, tensor product of the one-axis permutations P_{s_i}.
- $Q$ (target permutation), bound on `retained-permutations`: The target coordinate permutation, tensor product of the one-axis permutations P_{t_i}.
- $w$ (chunk width), bound on `retained-permutations`: The width in bits of the chunks swapped.
- $t$ (transform length), bound on `frequency-order`: The number of ring elements transformed along one axis, a power of two dividing 2r.
- $a$ (number of rounds), bound on `frequency-order`: The number log_2 t of rounds of the fast algorithm.
- $a$ (kernel coefficient a), bound on `phase-kernel`: The complex constant (1+i)/2, the coefficient of I in C.
- $b$ (kernel coefficient b), bound on `phase-kernel`: The complex constant (1-i)/2, the coefficient of X in C.
- $C$ (two-point kernel), bound on `phase-kernel`: The matrix aI + bX, a square root of the bit flip.
- $p$ (fractional bits), bound on `simultaneous-layer`: The number of fractional bits of each coefficient.
- $f$ (slot width), bound on `simultaneous-layer`: The number of bits in each slot.
- $s$ (child count), bound on `simultaneous-layer`: The number of children, the total of residual dimensions over the network.
- $t_i$ (axis length), bound on `transform-layout`: The length of axis i, either 2^(ell-1) or 2^ell.
- $M$ (record count), bound on `transform-layout`: The number of polynomial records, the product of the axis lengths.
- $T$ (coefficient count), bound on `transform-layout`: The number of complex coefficients, r times M.
- $p$ (precision), bound on `transform-layout`: The precision in bits: coefficient parts are multiples of 2^-p.
- $B$ (bit reversal), bound on `transform-layout`: The bit-reversal order in which forward outputs are written.
- $j$ (frequency address), bound on `transform-layout`: A frequency address of an output entry.
- $b$ (low-bit remainder), bound on `transform-layout`: (ell-1) mod K, the number of low bits per axis beyond whole chunks.
- $q$ (chunks per axis), bound on `transform-layout`: The number of whole K-bit chunks in ell-1 bits.
- $Q_p$ (truncation), bound on `transform-layout`: Truncation toward zero of real and imaginary parts to the 2^-p grid.
- $M$ (number of records), bound on `ring-convolution`: The number of polynomial records, one per cyclic address of the remaining axes.
- $T$ (number of coefficients), bound on `ring-convolution`: The number of complex coefficients in an array, T = rM.
- $n$ (input bits), bound on `parameter-choice`: The number of bits of each of the two input integers.
- $T$ (padded box size), bound on `parameter-choice`: The number of positions of the padded box.
- $t_i$ (axis length), bound on `parameter-choice`: The length of axis i of the padded box.
- $b$ (bit length), bound on `parameter-choice`: The bit length of n.
- $p$ (precision), bound on `parameter-choice`: The precision in bits, setting the 2^{-p} grid of the fixed-point records.
- $\gamma$ (total scaling), bound on `parameter-choice`: The total scaling of the Gaussian weights over the axes.
- $x$ (interval scale), bound on `parameter-choice`: A real number, the scale of the prime interval.
- $q$ (candidate), bound on `parameter-choice`: An integer in the prime interval.
- $s_i$ (prime axis length), bound on `parameter-choice`: The prime axis length of axis i near t_i.
- $S$ (convolution length), bound on `parameter-choice`: The product of the s_i, the cyclic convolution length.

## Pages in the wiki

- [Polynomial ring modulo y^r + 1](ring-y.md)
- [Linear exchange network with restored scratch wires](exchange-network.md)
- [Frames on wire arrays](array-frames.md)
- [Nested subspace labels and rank deficit](subspace-labels.md)
- [Recursive power saving](rank-recurrence.md)
- [Fixed finite-tape machine model](machine-model.md)
- [Schönhage–Strassen optimality conjecture](conjecture.md)
- [Elementary stream operations](stream-ops.md)
- [Fixed-point Gaussian dyadic records](fixed-point.md)
- [Established O(n log n) multiplier](hvdh-multiplier.md)
- [Signed packing](signed-packing.md)
- [Controlled shifts and rational scalings](controlled-shifts.md)
- [Matrix shear by triangular factorization](matrix-shear.md)
- [Fast address-chunk interchange](address-interchange.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Cyclic convolution](convolution.md)
- [Multiplication as radix-digit convolution](radix-digit-reduction.md)
- [Phase twist](phase-twist.md)
- [Error tracking and exact recovery](precision-recovery.md)
- [Discrete Fourier transform](dft.md)
- [Butterflies and the fast transform](butterfly.md)
- [Multidimensional transforms](multidim-transform.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Chinese-remainder address map](crt-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein chirp identity](chirp.md)
- [Retained permutation cancellation](retained-permutations.md)
- [Retained frequency order](frequency-order.md)
- [Two-point kernel C](phase-kernel.md)
- [Binary phase frames](phase-frames.md)
- [Simultaneous butterfly layer](simultaneous-layer.md)
- [Tape layout for synthetic transforms](transform-layout.md)
- [Convolution from the retained transform layout](ring-convolution.md)
- [Parameter and prime-length choice](parameter-choice.md)
- [The multiplication algorithm](multiplication-algorithm.md)
- [Cost accounting and the exponent κ](cost-accounting.md)
- [Power-saving integer multiplication](main-result.md)

## Page to audit (`multiplication-algorithm`)

````markdown
# The multiplication algorithm

The multiplication algorithm chains the earlier reductions to turn two $n$-bit integers into their exact $2n$-bit product.

It takes its sizes from [Parameter and prime-length choice](parameter-choice.md). Here $b=\lceil\log_2 n\rceil$ is the digit width in bits and $p=6b$ is the number of fractional bits kept. Axis lengths are primes $s_i$ with product $S$, and padded lengths $t_i$ with product $T$.

Each input splits into $q=\lceil n/b\rceil$ radix-$2^b$ digits $a_j$, and the product is their convolution modulo $x^S-1$, as in [Multiplication as radix-digit convolution](radix-digit-reduction.md). The convolution is addressed on the prime axes by the [Chinese-remainder address map](crt-map.md) $\Phi$.

Let $a_{\boldsymbol j}=\exp(-\pi i\sum_i s_ij_i^2/t_i)$ be the chirp array. The [Bluestein chirp identity](chirp.md) gives $QF_{\boldsymbol t}x=\overline a\cdot\mathcal M_{\mathbb C}(a,\overline a\cdot x)$: phase, convolution with the chirp, phase. Here $F_{\boldsymbol t}$ is the transform on the axes $t_i$, and $\mathcal M_{\mathbb C}(f,g)=f*g/T$ is computed through the [Phase twist](phase-twist.md) and [Convolution from the retained transform layout](ring-convolution.md). With $\widetilde a$ the approximation of $a$ and $Q_p$ truncation to $p$ fractional bits, the computed version forms $x_0=Q_p(\overline{\widetilde a}\cdot x)$, the data operand after the first endpoint phase. The computed chirp transform is $\widetilde{\mathscr C}(x)=Q_p(\overline{\widetilde a}\cdot y_0)$ with $y_0=\widetilde{\mathcal M}_{\mathbb C}(\widetilde a,x_0)$. The source transform $\widetilde{\mathscr F}$ applies the [Gaussian resampling](gaussian-resampling.md) map $\mathcal A$, then $\widetilde{\mathscr C}$, then the resampling map $\mathcal B_0$, then multiplies exactly by $2^\gamma$, where $\gamma$ counts the zero bits appended to each word. Replacing each numerical subroutine by the exact map it approximates, the exact counterpart is $\mathscr F=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A=RF_{\boldsymbol s}$, with $R$ a retained permutation.

Digit $a_j$ is stored as the exact grid numerator $a_j2^{p-b-2}$ in a signed real word, representing $a_j2^{-b-2}$; $S-q$ zero records are appended. Then:

1. Apply $\Phi$ to obtain source arrays $u,v$ of norm less than $1/4$.
2. Compute $\widetilde{\mathscr F}(u)$ and $\widetilde{\mathscr F}(v)$.
3. Multiply corresponding coefficients and truncate to $p$ fractional bits, obtaining $z$.
4. Compute $\widetilde{\mathscr F}^{+}(z)$ and multiply its grid numerators by $S$, obtaining $\widetilde w$.
5. Multiply by $2^{2b+4}S$, round to the nearest integers, and apply $\Phi^{-1}$.
6. Propagate radix-$2^b$ carries in increasing coefficient order and output exactly $2n$ bits (cited)

The two scalings by $S$ undo different normalizations (cited). By [Retained permutation cancellation](retained-permutations.md), $R$ is never executed as a sort and the counterpart after the three transforms is $(u*v)/S^2$. So after the first scale it is $w=(u*v)/S$, and the second scale gives $2^{2b+4}(u*v)$, cancelling the factor $2^{-b-2}$.

Exactness is justified by [Error tracking and exact recovery](precision-recovery.md): the error on the recovered integer coefficients is below $1/2$.
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

Write the answer to `exegenius/tasks/0075-audit-multiplication-algorithm.answer.json`, then run `exegenius submit 0075-audit-multiplication-algorithm` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0075-audit-multiplication-algorithm`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
