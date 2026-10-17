# exegenius task 0146-audit-address-interchange

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
- $j$ (excess degree), bound on `ring-y`: The number of places a term's degree exceeds r-1.
- $a$ (shift exponent), bound on `ring-y`: An integer exponent of y by which an element is multiplied.
- $n$ (bit length), bound on `conjecture`: The number of bits in each of the two integers being multiplied.
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on `fixed-point`: The number of operations in sequence since the layer began that produced a value.
- $h$ (ground-set size), bound on `exchange-network`: The size of the ground set [h] whose three-element subsets index the values.
- $m$ (label dimension), bound on `exchange-network`: The dimension of the label space used later.
- $x$ (source vector), bound on `exchange-network`: The vector of all values x_S.
- $a$ (bank index), bound on `exchange-network`: The index of a value in a data bank, a triple of triples.
- $I$ (invocation count), bound on `exchange-network`: The number of invocations.
- $t$ (gate input count), bound on `array-frames`: The number of input arrays of a gate.
- $q$ (sequence length), bound on `convolution`: The number of entries in each sequence being convolved.
- $d$ (axis count), bound on `convolution`: One more than the number of cyclic axes of an array.
- $M$ (cyclic address count), bound on `convolution`: The number of addresses on the cyclic axes of an array.
- $u$ (first input), bound on `radix-digit-reduction`: The first of the two integers being multiplied.
- $n$ (input bit length), bound on `radix-digit-reduction`: The number of bits in each input.
- $b$ (digit width), bound on `radix-digit-reduction`: The number of bits in one radix digit.
- $q$ (digit count), bound on `radix-digit-reduction`: The number of radix-2^b digits in each input.
- $x$ (polynomial variable), bound on `radix-digit-reduction`: The variable of the digit polynomials, evaluated at 2^b to recover the integers.
- $f$ (first array), bound on `phase-twist`: The first complex array being convolved.
- $g$ (second array), bound on `phase-twist`: The second complex array being convolved with f.
- $d$ (axis count), bound on `phase-twist`: The number of axes of the arrays.
- $k$ (coefficient index), bound on `phase-twist`: An index of a coefficient (not an operation count).
- $l$ (second coefficient index), bound on `phase-twist`: An index of a coefficient of the second factor.
- $j$ (wrapped position), bound on `phase-twist`: The position k+l reduced modulo r.
- $h$ (wrap indicator), bound on `phase-twist`: Zero or one according to whether k+l wrapped past r.
- $q$ (sequence length), bound on `dft`: The number of entries of a sequence.
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to be transformed.
- $t$ (transform length), bound on `butterfly`: The number of positions in the sequence being transformed, a power of two.
- $m$ (output index), bound on `butterfly`: The index of an output of the transform.
- $b$ (lowest bit), bound on `butterfly`: The lowest bit of the output index m.
- $h$ (remaining index), bound on `butterfly`: The output index m with its lowest bit removed.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis, a power of two dividing 2r.
- $e$ (two-adic exponent), bound on `synthetic-transform`: The exponent of 2 in j when j is written as 2^e times an odd number.
- $V$ (array volume), bound on `stream-ops`: The number of radix-q digits an array stores.
- $q$ (radix), bound on `stream-ops`: The number of values one digit can take.
- $W$ (stream count), bound on `stream-ops`: The fixed number of streams the rows are dealt into.
- $a$ (chirp), bound on `chirp`: The array of phases a_j = exp(-pi i sum s_i j_i^2/t_i), quadratic in the index.
- $a$ (number of rounds), bound on `frequency-order`: The number of rounds, log base 2 of the transform length t.
- $s$ (completed rounds), bound on `frequency-order`: The number of rounds completed so far.
- $i$ (axis index), bound on `frequency-order`: Index of an axis of the array.
- $p$ (fractional bits), bound on `signed-packing`: The number of fractional bits of each coefficient component.
- $f$ (first polynomial), bound on `signed-packing`: A polynomial of the ring with coefficients 2^{-p} times Gaussian integers.
- $a$ (integer polynomial), bound on `signed-packing`: Integer-coefficient polynomial, real part numerator of f (similarly b, c, e).
- $Z$ (product integer), bound on `signed-packing`: One of the four product integers, equal to the sum of h_j B_0^j for its ordinary product h.
- $q$ (prime), bound on `controlled-shifts`: The prime base of the digits of a field.
- $b$ (digits per field), bound on `controlled-shifts`: The number of base-q digits of a field.
- $a$ (offset), bound on `controlled-shifts`: The offset added to the target, prepared from the control values.
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
- $H$ (normalized Hadamard matrix), bound on `phase-kernel`: The matrix sqrt(2) H_0, symmetric with H squared equal to the identity.
- $f$ (first operand), bound on `contraction-maps`: The first operand of the bilinear map.
- $g$ (second operand), bound on `contraction-maps`: The second operand of the bilinear map.
- $f'$ (perturbed first operand), bound on `contraction-maps`: A perturbed replacement for the operand f.
- $j$ (index tuple), bound on `multidim-transform`: The index tuple of an entry of the array, with 0 <= j_i < q_i.
- $k$ (output index tuple), bound on `multidim-transform`: An output index tuple of the same shape as j.
- $A_i$ (input resampling map), bound on `multidim-transform`: A linear contraction from sequences of length s_i to length t_i.
- $d$ (number of axes), bound on `crt-map`: The number of axes of the target ring.
- $i$ (axis index), bound on `crt-map`: The index of an axis, from 1 to d.
- $\Phi$ (Chinese-remainder map), bound on `crt-map`: The ring isomorphism sending x to the product of x_i^{mu_i}.
- $k$ (coefficient index), bound on `crt-map`: The index of a coefficient of the length-S sequence.
- $a_j$ (mixed-radix digit), bound on `crt-map`: The j-th digit of k in mixed radix, 0 <= a_j < s_j.
- $V$ (stream volume), bound on `crt-map`: The volume of the stream being moved, Tp bits.
- $\tau$ (chunk-swap exponent), bound on `crt-map`: A fixed exponent below 1 in the cost of a chunk interchange.
- $s$ (source length), bound on `gaussian-resampling`: The length of the Fourier transform to be replaced.
- $k$ (output coordinate index), bound on `gaussian-resampling`: A coordinate index of a vector in C^t, taken modulo t.
- $t$ (target length), bound on `gaussian-resampling`: The larger length, a power of two in the application, of the transform used instead of the length-s one.
- $u$ (complex array), bound on `retained-permutations`: Here a complex array, not an integer; changes meaning from the multiplication page.
- $g$ (setup exponent), bound on `retained-permutations`: A fixed exponent bounding per-line setup work by p^g.
- $z$ (complex vector), bound on `retained-permutations`: A vector of q complex entries.
- $u$ (scaled digit array), bound on `precision-recovery`: The array of scaled digits of the first input.
- $\tau$ (chunk-swap exponent), bound on `parameter-choice`: An exponent bounding the cost of an equal-width chunk interchange.
- $V$ (bit volume), bound on `parameter-choice`: The logical bit volume of the data the layer acts on.
- $x$ (real argument), bound on `parameter-choice`: A real number, the length at which the prime interval is taken.
- $q$ (integer in interval), bound on `parameter-choice`: An integer, in the prime interval.
- $s$ (number of smaller calls), bound on `subspace-labels`: The total number of smaller calls that the edges of the network cost.
- $W$ (wire count), bound on `subspace-labels`: The number of wires of the network under consideration.
- $F$ (one-factor label space), bound on `subspace-labels`: The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $a$ (triple tuple), bound on `subspace-labels`: A tuple $(a_1,a_2,a_3)$ of triples indexing one data wire in each bank.
- $j$ (stage number), bound on `subspace-labels`: The stage, 1, 2 or 3, whose invocations act on coordinate $a_j$.
- $A$ (exposed factor space), bound on `subspace-labels`: The tensor product $F^{\otimes(j-1)}$ of the factors exposed before stage $j$.
- $f$ (call parameter), bound on `rank-recurrence`: The parameter of a recursive call: the number of digits per interchanged chunk, or the number of selected axes in a butterfly layer.
- $m$ (slot count), bound on `rank-recurrence`: The number of size-f slots into which a call at parameter mf cuts its parameter, equal to 10^6, the label-space dimension.
- $s$ (number of smaller calls), bound on `rank-recurrence`: The number of calls at parameter f made by a call at parameter mf: the total rank of the frame changes over all edges of the network.
- $F$ (cost per unit volume), bound on `rank-recurrence`: F(f) is the running time of a call at parameter f divided by the volume of its data.
- $j$ (recursion depth), bound on `rank-recurrence`: The number of recursion levels between the top call and the nodes considered.
- $\tau$ (saving exponent), bound on `rank-recurrence`: A fixed exponent below 1 with s/W < m^tau, which makes an interchange cost O(V f^tau); here tau = 1 - 2^{-50}.

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

## Page to audit (`address-interchange`)

````markdown
# Fast address-chunk interchange

Fast address-chunk interchange, a tape primitive for the main result, swaps two disjoint $u$-bit address fields of an array of $V$ bits (volume) in $O(Vu^\tau)$ time on fixed tapes (cited), with $\tau=1-2^{-50}$. Its steps XOR data.

An address is $(p,h,g,d,z)$: prefix $p$, chunks $h,d$, gap $g$, suffix $z$; the goal is $(p,h,g,d,z)\mapsto(p,d,g,h,z)$. Letters $u,p,h,d$ change meaning here. Digits are radix $q$ (a fixed prime).

For chunk values $H,D$, $D\gets D-H$, $H\gets H+D$, $D\gets H-D$ send $(H,D)$ to $(H,D-H)$, $(D,D-H)$, $(D,H)$. Only the middle shear needs the circuit.

Let each chunk have $e=m^k$ digits ($k$ recursion levels). Cut it into $m$ fields of $b=e/m$ digits, so $H,D$ are vectors over $\mathbb Z/q^b\mathbb Z$. The [exchange network](exchange-network.md) has $W$ wires; each terminal and gate carries a rational $m\times m$ matrix $M$, and edge $i$ carries $A_i=M_{\mathrm{head}(i)}-M_{\mathrm{tail}(i)}$, with $s=\sum_i\operatorname{rank}A_i$. The shear contract: input wire $w$ ends at output role $\rho(w)$, with $M_{\mathrm{out}(\rho(w))}-M_{\mathrm{in}(w)}=I_m$ (the identity), and $s<Wm$ ([rank deficit](subspace-labels.md)); take $\tau$ with $s/W<m^\tau$.

Let $\Phi_M$ move the entry at address $(H,D)$ to $(H+MD,D)$. For another matrix $M'$, $\Phi_{M'}\Phi_M=\Phi_{M'+M}$. The [frame](array-frames.md) at a vertex with matrix $M$ is $\Phi_M$; an edge to a vertex with matrix $M'$ changes it by $\Phi_{M'-M}=\Phi_{A_i}$. A common address permutation commutes with every pointwise bit gate. [Matrix shear by triangular factorization](matrix-shear.md) performs each $\Phi_{A_i}$: rank $a$ costs $a$ interchanges of $b$-digit fields (cited), so there are exactly $s$ smaller calls (cited).

Suppose a row field ahead of both chunks has length divisible by $W^k$. Within each prefix, rows are split into role streams by [stream scans](stream-ops.md): row $Wx+w-1$ goes to stream $w$ as row $x$. Each stream has volume $V/W$ and row count divisible by $W^{k-1}$. Read wire $w$'s input $f_w$ as the logical array $\Phi_{-M_{\mathrm{in}(w)}}f_w$. By the composition rule and the contract, the output is $f'_{\rho(w)}=\Phi_{M_{\mathrm{out}(\rho(w))}}\Phi_{-M_{\mathrm{in}(w)}}f_w=\Phi_{I_m}f_w$. Merging rows back undoes $\rho$, giving $H\gets H+D$ on every original row.

Each call acts on volume $V/W$; other work is $O(V)$. The time per unit volume $F_k$ at width $m^k$ obeys $F_0=O(1)$, $F_k\le(s/W)F_{k-1}+O(1)$, the recurrence of [Recursive power saving](rank-recurrence.md). Unrolled over levels $j$, $F_k=O(\sum_{j=0}^k (s/W)^j)$. If $s/W\le1$ this is at most $k+1=O(m^{k\tau})$; otherwise it is $O((s/W)^k)$, below $m^{k\tau}$. So $F_k=O(e^\tau)$. As $s/W$ nears $m$, $\tau\approx1$.

For large $e$, put $k'=\lceil\log_m e\rceil$ and $\nu=\lceil k'\log W/(2\log q)\rceil$, so $q^{2\nu}\ge W^{k'}$, $1\le\nu<e$ and $\nu=O(\log 2e)$; small $e$ use single-digit interchanges. Split each chunk into top $\nu$ digits and rest, $h^+,h^-$ and $d^+,d^-$. Interchange the high digits and move $h^+$ next to $d^+$: $(h^+,h^-,g,d^+,d^-)$ becomes $(d^+,h^+,h^-,g,d^-)$. Now $d^+,h^+$ form a row field of range $\Lambda=q^{2\nu}\ge W^{k'}$ before both remaining chunks. Pad with zero rows to $\Lambda'=W^{k'}\lceil \Lambda/W^{k'}\rceil<2\Lambda$ rows (volume below $2V$). Write $e-\nu=\sum_{j=0}^{k'}a_jm^j$, $0\le a_j<m$. Split each remaining chunk into $a_j$ pieces of width $m^j$ and interchange corresponding pieces as above. The total $O(V)\sum_ja_jm^{j\tau}\le O(V)\,m\sum_jm^{j\tau}=O(Ve^\tau)$, since $m^{k'}<me$. Scan away padded rows and reverse the joining, giving $(d^+,d^-,g,h^+,h^-)$ at cost $O(V\nu)=O(Ve^\tau)$.

For $u$-bit chunks, pad $[2^u]$ to $[q^e]$, $e$ least with $q^e\ge2^u$, and scan the padding away. Since $e=O(u)$ the cost is $O(Vu^\tau)$ (cited).
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

Write the answer to `exegenius/tasks/0146-audit-address-interchange.answer.json`, then run `exegenius submit 0146-audit-address-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0146-audit-address-interchange`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
