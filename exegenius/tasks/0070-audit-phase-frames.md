# exegenius task 0070-audit-phase-frames

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
- Packed selected-bit addition
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

- $r$ (record length), bound on `ring-y`: The number of complex coefficients in a polynomial of the ring, always a power of two.
- $v$ (number of triples), bound on `exchange-network`: The number of three-element subsets of $[h]$.
- $N$ (bank size), bound on `exchange-network`: The number of wires in each data bank.
- $m$ (label-space dimension), bound on `exchange-network`: The dimension of the label space used later.
- $I$ (invocation count), bound on `exchange-network`: The number of invocations.
- $W_{\rm c}$ (complex wire count), bound on `exchange-network`: The total number of wires in the complex network.
- $m$ (label-space dimension), bound on `subspace-labels`: The dimension of the ambient label space, $m=h^3=10^6$.
- $W$ (wire count), bound on `subspace-labels`: The number of wires of the network under consideration.
- $s$ (number of smaller calls), bound on `subspace-labels`: The total number of smaller calls that the network's edges cost.
- $F$ (one-factor label space), bound on `subspace-labels`: The space $\mathbb Q^h$ (bit network) or $\mathbb F_2^h$ (complex network) with its bilinear form.
- $N$ (bank size), bound on `subspace-labels`: The number of index tuples $a$ of triples, so the number of wires in each data bank.
- $U_a$ (terminal line), bound on `subspace-labels`: The line spanned by $t_{a_1}\otimes t_{a_2}\otimes t_{a_3}$, the source label of $X_a$.
- $L$ (total dimension loss), bound on `subspace-labels`: The total dimension lost on decreasing edges.
- $P$ (earlier tensor line), bound on `subspace-labels`: The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on `subspace-labels`: The orthogonal complement of $P$ inside $A$.
- $I$ (invocation count), bound on `subspace-labels`: The number of invocations over all three stages.
- $f$ (call parameter), bound on `rank-recurrence`: The parameter of a call: the number of digits in each of the two interchanged chunks, or the number of axes the butterfly layer acts on.
- $V$ (volume), bound on `rank-recurrence`: The volume of a call: the number of data symbols it processes.
- $m$ (block count), bound on `rank-recurrence`: The number of size-f blocks into which a call at parameter mf cuts its parameter, equal to 10^6 (also the dimension of the label space).
- $W$ (wire count), bound on `rank-recurrence`: The number of wires of the fixed network, and so the number of streams a call splits its data into.
- $s$ (number of smaller calls), bound on `rank-recurrence`: The number of calls at parameter f made by a call at parameter mf: the total rank of the frame changes over all edges of the network.
- $F$ (normalized cost), bound on `rank-recurrence`: F(f) is the running time of a call at parameter f divided by its volume.
- $k$ (recursion depth), bound on `rank-recurrence`: The number of levels of recursion: the number of factors m in a parameter m^k.
- $V$ (array volume), bound on `stream-ops`: The number of radix-q digits stored in the array.
- $q$ (radix), bound on `stream-ops`: The number of values one digit can take.
- $W$ (number of streams), bound on `stream-ops`: The fixed number of streams into which whole rows are dealt cyclically.
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the stored grid, so values are integers divided by 2^p.
- $k$ (operation count), bound on `fixed-point`: The number of operations applied since the layer began.
- $N$ (bit length), bound on `hvdh-multiplier`: The number of bits in each of the two integers being multiplied.
- $p$ (precision bits), bound on `signed-packing`: The number of fractional bits in each coefficient component.
- $q$ (prime), bound on `controlled-shifts`: The prime base of the field arithmetic.
- $b$ (field digits), bound on `controlled-shifts`: The number of base-$q$ digits of a field.
- $V$ (array volume), bound on `controlled-shifts`: The number of stored data bits in the array.
- $a$ (offset), bound on `controlled-shifts`: The offset added to the target field, prepared from the control values.
- $B$ (suffix length), bound on `controlled-shifts`: The number of bits following the target field.
- $c$ (scaling integer), bound on `controlled-shifts`: A fixed positive integer prime to q by which the target is multiplied.
- $m$ (fields per group), bound on `matrix-shear`: The number of fields in each of the groups H and D.
- $a$ (rank), bound on `matrix-shear`: The rank of the matrix A.
- $H$ (H group), bound on `matrix-shear`: The ordered group of m fields H_1..H_m that receives the update.
- $q$ (base prime), bound on `matrix-shear`: A fixed odd prime; fields are residues modulo q^b.
- $b$ (digits per field), bound on `matrix-shear`: The number of base-q digits in a field.
- $V$ (data volume), bound on `matrix-shear`: The volume of data being processed.
- $i$ (row index), bound on `matrix-shear`: The row of a one of Pi.
- $d$ (value of D_j), bound on `matrix-shear`: The initial value of the field D_j.
- $u$ (chunk width), bound on `address-interchange`: The number of bits in each of the two address chunks.
- $V$ (volume), bound on `address-interchange`: The number of entries of the array.
- $q$ (radix), bound on `address-interchange`: The fixed prime used as digit radix.
- $H$ (first chunk), bound on `address-interchange`: The value of the first chunk.
- $m$ (fields per chunk), bound on `address-interchange`: The number of fields each chunk is split into.
- $k$ (levels), bound on `address-interchange`: The number of recursion levels, with e = m^k.
- $b$ (field width), bound on `address-interchange`: The number of digits in each field.
- $W$ (wires), bound on `address-interchange`: The number of wires of the exchange network.
- $s$ (total edge rank), bound on `address-interchange`: The sum of the ranks of the edge matrices.
- $d$ (chunk bound), bound on `packed-bit-addition`: Maximum number of chunks a layer acts on.
- $c$ (control), bound on `packed-bit-addition`: Boolean control of the eight additions.
- $u$ (target integer), bound on `packed-bit-addition`: Integer whose parity is flipped by the eight additions.
- $w$ (auxiliary integer), bound on `packed-bit-addition`: Arbitrary auxiliary integer restored by the eight additions.
- $L$ (bits per chunk), bound on `packed-bit-addition`: Number of bits in each address chunk.
- $f$ (selected bits), bound on `packed-bit-addition`: Number of selected bits in each chunk.
- $V$ (volume), bound on `packed-bit-addition`: Total number of bits, M times R.
- $\mathcal B$ (exceptional set), bound on `packed-bit-addition`: Set of addresses where some guard fails the interval test.
- $p$ (coefficient precision), bound on `packed-bit-addition`: Bit precision of the record coefficients.
- $q$ (sequence length), bound on `convolution`: The number of entries in each of the two sequences being convolved.
- $u$ (first input), bound on `radix-digit-reduction`: The first of the two integers being multiplied.
- $v$ (second input), bound on `radix-digit-reduction`: The second of the two integers being multiplied.
- $b$ (digit width), bound on `radix-digit-reduction`: The number of bits in one radix digit.
- $q$ (digit count), bound on `radix-digit-reduction`: The number of radix-2^b digits in each input.
- $x$ (polynomial variable), bound on `radix-digit-reduction`: The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $d$ (number of axes), bound on `phase-twist`: The number of axes of the array f.
- $b$ (digit width), bound on `precision-recovery`: The number of bits in a radix digit.
- $p$ (fractional bits), bound on `precision-recovery`: The number of fractional bits of the fixed-point grid, equal to $6b$.
- $L$ (log of T), bound on `precision-recovery`: The base-2 logarithm of $T$.
- $d$ (axis count), bound on `precision-recovery`: The number of transform axes.
- $q$ (digit count), bound on `precision-recovery`: The number of radix digits of an $n$-bit input.
- $q$ (sequence length), bound on `dft`: The number of complex entries in the sequences the transform acts on.
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to which the transform is applied.
- $t$ (transform length), bound on `butterfly`: The number of values in the transform, a power of two.
- $k$ (input position), bound on `butterfly`: The position of an input value, 0 <= k < t.
- $b$ (lowest output bit), bound on `butterfly`: The lowest bit of the output index, 0 or 1.
- $d$ (number of axes), bound on `multidim-transform`: The number of axes (coordinates) of the array.
- $N$ (number of entries), bound on `multidim-transform`: The number of entries of the array, the product of the axis lengths.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis of the transform, a power of two dividing 2r.
- $d$ (number of axes), bound on `crt-map`: The number of axes.
- $p$ (record precision), bound on `crt-map`: The number of bits of precision per record.
- $s$ (prime length), bound on `gaussian-resampling`: The prime length of the Fourier transform to be resampled, the number of complex coordinates it acts on.
- $t$ (power-of-two length), bound on `gaussian-resampling`: The power-of-two length of the nearby transform, the number of complex coordinates it acts on.
- $p$ (precision bits), bound on `gaussian-resampling`: The number of bits of precision of each real and imaginary component.
- $k$ (coordinate index), bound on `gaussian-resampling`: An index of a coordinate of a vector in C^t, taken modulo t.
- $d$ (number of axes), bound on `chirp`: The number of axes (coordinates) of an index.
- $a$ (chirp), bound on `chirp`: The chirp, a quadratic-phase array exp(-pi i sum s_i j_i^2/t_i).
- $d$ (number of axes), bound on `retained-permutations`: The number of coordinate axes.
- $p$ (bit precision), bound on `retained-permutations`: The number of bits of precision of each coordinate.
- $w$ (chunk width), bound on `retained-permutations`: The width in bits of the chunks swapped.
- $V$ (total bits), bound on `retained-permutations`: The total number of bits within which chunks are swapped.
- $t$ (transform length), bound on `frequency-order`: The number of ring elements transformed along one axis, a power of two dividing 2r.
- $a$ (number of rounds), bound on `frequency-order`: The number log_2 t of rounds of the fast algorithm.
- $X$ (bit flip), bound on `phase-kernel`: The 2x2 matrix that swaps the two entries of a pair.
- $a$ (kernel coefficient a), bound on `phase-kernel`: The complex constant (1+i)/2, the coefficient of I in C.
- $b$ (kernel coefficient b), bound on `phase-kernel`: The complex constant (1-i)/2, the coefficient of X in C.
- $C$ (two-point kernel), bound on `phase-kernel`: The matrix aI + bX, a square root of the bit flip.

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

## Page to audit (`phase-frames`)

````markdown
# Binary phase frames

A binary phase frame attaches to each label of [Nested subspace labels and rank deficit](subspace-labels.md) a basis for arrays of binary addresses, so that the change of basis along an edge is a product of two-point kernels. Here $m$ is the number of binary coordinates of an address $x$, and a label $U$ is a subspace of $\mathbb F_2^m$.

Write $\operatorname{wt}(x)$ for Hamming weight, $[b]\in\{0,1\}$ for the integer representative of $b\in\mathbb F_2$, and $P_U$ for the projection onto $U$ over $\mathbb F_2$. Put $q_U(x)=\operatorname{wt}(P_Ux)\bmod 4$. With $H=\tfrac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, the phase frame is $\mathcal C_U=H^{\otimes m}\operatorname{diag}_x(i^{q_U(x)})H^{\otimes m}$, with Gaussian-dyadic entries. (cited) Let $C=H\operatorname{diag}(1,i)H=aI+bX$, with $a=\frac{1+i}{2}$, $b=\frac{1-i}{2}$, $X$ the coordinate swap, and $X_v$ the translation $(X_vf)(x)=f(x+v)$.

## One edge

For binary vectors $z,w$, $\operatorname{wt}(z+w)=\operatorname{wt}(z)+\operatorname{wt}(w)-2|\operatorname{supp}(z)\cap\operatorname{supp}(w)|$. The dot product $z\cdot w$ is that intersection size mod $2$. If $z\cdot w=0$ the intersection cardinality is even, so weight is additive modulo four on orthogonal vectors.

Take an edge from $U$ to $V=U\perp E$, with residual $E$ orthogonal to $U$ and orthonormal basis $\mathcal B$ (distinct vectors have dot product $0$, and $v\cdot v=1$). Then $P_Vx=P_Ux+\sum_{v\in\mathcal B}[v\cdot x]\,v$ so $q_V(x)-q_U(x)=\sum_{v\in\mathcal B}\operatorname{wt}(v)[v\cdot x]\pmod 4$, negated on a decreasing edge, and each $\operatorname{wt}(v)$ is odd.

Odd weight is $\pm1$ modulo four, so each term is $\varepsilon[v\cdot x]$, $\varepsilon=\pm1$. The function $i^{\varepsilon[v\cdot x]}$ with $\varepsilon=\pm1$ equals $\frac{1+i^\varepsilon}2+\frac{1-i^\varepsilon}2(-1)^{v\cdot x}$.

Since $H^2=I$, $\mathcal C_V\mathcal C_U^{-1}=H^{\otimes m}\operatorname{diag}(i^{q_V-q_U})H^{\otimes m}$, one phase per $v$. The character $(-1)^{v\cdot x}$ is $\operatorname{diag}(1,-1)$ on $\operatorname{supp}(v)$. Since $H\operatorname{diag}(1,-1)H=X$, the character $(-1)^{v\cdot x}$ becomes the translation $X_v$, so the phase becomes $aI+bX_v$ or its inverse ($\varepsilon=-1$).

Each edge factor is built as a translate $aI+bX_v$ of [Two-point kernel C](phase-kernel.md), combining only $f(x)$ and $f(x+v)$, a butterfly-type operation. A residual of dimension $d$ costs $d$ such calls, one smaller call per dimension, as the recursion needs.

## Counting

Here $W_{\rm c}$ is the number of wires of the complex network, and $N$, $L_{\rm c}$ are constants of the labels page. Over the network the number of translation-kernel factors is $s_{\rm c}=W_{\rm c}m-2N+2L_{\rm c}=1873807244636671267308000000<W_{\rm c}m$. (cited) The deficit of $s_{\rm c}$ from $W_{\rm c}m$ is $2N-2L_{\rm c}>0$. (cited)

## The exceptional pair

For the pair $X_a\to Y_a$, take $u=u_a$ of binary norm one and weight $27$. Orthogonal additivity gives $\operatorname{wt}(x)-2\operatorname{wt}(u)[u\cdot x]$, and $27$ is odd, so $q_{U_a^\perp}-q_{U_a}=\operatorname{wt}(x)+2[u\cdot x]\pmod 4$, so the operator is $C^{-1}$ on the 27 coordinates of $\operatorname{supp}(u)$ and $C$ elsewhere.

Let $Z=\operatorname{diag}(1,-1)$; then $C=iZC^{-1}Z$. For $k$ columns, let $Z_{a,k}$ be $Z$ on those 27 coordinates in every column. The identity $C=iZC^{-1}Z$ turns each of the $27k$ inverse factors into $C$ after applying $Z_{a,k}$ before and $i^{27k}Z_{a,k}$ after, so every role, scratch roles included, receives $C^{\otimes mk}$.
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

Write the answer to `exegenius/tasks/0070-audit-phase-frames.answer.json`, then run `exegenius submit 0070-audit-phase-frames` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0070-audit-phase-frames`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
