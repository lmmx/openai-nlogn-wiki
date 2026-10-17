# exegenius task 0140-audit-retained-permutations

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

- $j$ (excess degree), bound on `ring-y`: The number of places a term's degree exceeds r-1.
- $a$ (shift exponent), bound on `ring-y`: An integer exponent of y by which an element is multiplied.
- $c$ (machine constant), bound on `conjecture`: A positive constant, depending on the machine, in the lower bound c n log n.
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on `fixed-point`: The number of operations in sequence since the layer began that produced a value.
- $h$ (ground-set size), bound on `exchange-network`: The size of the ground set [h] whose three-element subsets index the values.
- $v$ (triple count), bound on `exchange-network`: The number of three-element subsets of [h].
- $S$ (triple), bound on `exchange-network`: A three-element subset of [h], indexing a value in a bank.
- $a$ (bank index), bound on `exchange-network`: The index of a value in a data bank, a triple of triples.
- $\gamma$ (central scratch vector), bound on `exchange-network`: The initial values of the central scratch wires.
- $I$ (invocation count), bound on `exchange-network`: The number of invocations.
- $R$ (scalar ring), bound on `array-frames`: The ring of scalars carried by the wires.
- $t$ (gate input count), bound on `array-frames`: The number of input arrays of a gate.
- $q$ (sequence length), bound on `convolution`: The number of entries in each sequence being convolved.
- $d$ (axis count), bound on `convolution`: One more than the number of cyclic axes of an array.
- $t_i$ (axis length), bound on `convolution`: The length of cyclic axis i.
- $T$ (total coefficient count), bound on `convolution`: The total number of complex coefficients in an array.
- $u$ (first input), bound on `radix-digit-reduction`: The first of the two integers being multiplied.
- $v$ (second input), bound on `radix-digit-reduction`: The second of the two integers being multiplied.
- $T$ (padded length), bound on `radix-digit-reduction`: A power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on `radix-digit-reduction`: The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $q$ (digit count), bound on `radix-digit-reduction`: The number of radix-2^b digits in each input.
- $g$ (second array), bound on `phase-twist`: The second complex array being convolved with f.
- $d$ (axis count), bound on `phase-twist`: The number of axes of the arrays.
- $k$ (coefficient index), bound on `phase-twist`: An index of a coefficient (not an operation count).
- $j$ (wrapped position), bound on `phase-twist`: The position k+l reduced modulo r.
- $h$ (wrap indicator), bound on `phase-twist`: Zero or one according to whether k+l wrapped past r.
- $q$ (sequence length), bound on `dft`: The number of entries of a sequence.
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to be transformed.
- $t$ (transform length), bound on `butterfly`: The number of positions in the sequence being transformed, a power of two.
- $h$ (remaining index), bound on `butterfly`: The output index m with its lowest bit removed.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis, a power of two dividing 2r.
- $q$ (radix), bound on `stream-ops`: The number of values one digit can take.
- $P$ (prefix values), bound on `stream-ops`: The number of prefix values indexing the first axis of the array.
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
- $a$ (integer polynomial), bound on `signed-packing`: Integer-coefficient polynomial, real part numerator of f (similarly b, c, e).
- $B_0$ (packing base), bound on `signed-packing`: The base 2^{4p} at which polynomials are evaluated.
- $j_1$ (first-factor index), bound on `signed-packing`: The index of a coefficient of the first factor.
- $q$ (prime), bound on `controlled-shifts`: The prime base of the digits of a field.
- $Q$ (field values), bound on `controlled-shifts`: The number of values a field can take, q^b.
- $a$ (offset), bound on `controlled-shifts`: The offset added to the target, prepared from the control values.
- $B$ (suffix bits), bound on `controlled-shifts`: The number of bits following the target field.
- $c$ (multiplier), bound on `controlled-shifts`: A fixed positive integer prime to q by which the target is multiplied.
- $j$ (piece index), bound on `controlled-shifts`: The index of the increasing piece of y -> cy mod Q containing y.
- $A$ (shear matrix), bound on `matrix-shear`: The fixed rational matrix whose product with D is added to H.
- $a$ (rank), bound on `matrix-shear`: The rank of the rational matrix A.
- $a$ (kernel coefficient a), bound on `phase-kernel`: The complex constant (1+i)/2, the coefficient of the identity in C.
- $I$ (identity matrix), bound on `phase-kernel`: The 2 by 2 identity matrix.
- $X$ (bit flip), bound on `phase-kernel`: The 2 by 2 matrix swapping the two entries of a pair.
- $g$ (second operand), bound on `contraction-maps`: The second operand of the bilinear map.
- $F_q$ (normalized transform), bound on `contraction-maps`: The normalized discrete Fourier transform on sequences of q entries.
- $q_i$ (axis length), bound on `multidim-transform`: The number of positions along axis i of the array.
- $j$ (index tuple), bound on `multidim-transform`: The index tuple of an entry of the array, with 0 <= j_i < q_i.
- $F_{q_i}$ (one-axis transform), bound on `multidim-transform`: The one-dimensional normalized discrete Fourier transform of length q_i.
- $F_{\boldsymbol q}$ (multidimensional transform), bound on `multidim-transform`: The tensor product of the one-axis transforms F_{q_i}.
- $k$ (output index tuple), bound on `multidim-transform`: An output index tuple of the same shape as j.
- $\alpha$ (resampling parameter), bound on `multidim-transform`: An integer parameter of the Gaussian resampling with 2 <= alpha < sqrt p.
- $\delta$ (time exponent slack), bound on `multidim-transform`: A fixed constant with 0 < delta < 1/8 in the exponent of the running time.
- $P_{s_i}$ (source permutation), bound on `multidim-transform`: The index permutation on length s_i sequences in the resampling identity.
- $A_i$ (input resampling map), bound on `multidim-transform`: A linear contraction from sequences of length s_i to length t_i.
- $B_{0,i}$ (output resampling map), bound on `multidim-transform`: A linear contraction from sequences of length t_i to length s_i.
- $\gamma$ (scalar exponent), bound on `multidim-transform`: The exponent 2d alpha^2 of the scalar in the tensored identity.
- $R$ (source permutation product), bound on `multidim-transform`: The tensor product of the permutations P_{s_i}; here R is not the scalar ring.
- $Q$ (target permutation product), bound on `multidim-transform`: The tensor product of the permutations P_{t_i}.
- $\mathcal A$ (tensored input map), bound on `multidim-transform`: The tensor product of the maps A_i.
- $\mathcal B_0$ (tensored output map), bound on `multidim-transform`: The tensor product of the maps B_{0,i}.
- $X_i$ (axis operator), bound on `multidim-transform`: An operator on axis i in the mixed-product rule.
- $Y_i$ (axis operator), bound on `multidim-transform`: A second operator on axis i in the mixed-product rule.
- $S$ (convolution length), bound on `crt-map`: The length of the cyclic convolution, the product of the s_i.
- $d$ (number of axes), bound on `crt-map`: The number of axes of the target ring.
- $i$ (axis index), bound on `crt-map`: The index of an axis, from 1 to d.
- $s_i$ (axis source length), bound on `crt-map`: The length of axis i, pairwise coprime with the others; unrelated to the s_i of the chirp page.
- $k$ (coefficient index), bound on `crt-map`: The index of a coefficient of the length-S sequence.
- $t_i$ (padded axis length), bound on `crt-map`: The padded length of axis i, either r/2 or r.
- $\ell$ (address bits), bound on `crt-map`: The base-2 logarithm of the record length r, the number of address bits of a full-width axis.
- $T$ (padded record count), bound on `crt-map`: The number of padded records, the product of the t_i.
- $\tau$ (chunk-swap exponent), bound on `crt-map`: A fixed exponent below 1 in the cost of a chunk interchange.
- $s$ (source length), bound on `gaussian-resampling`: The length of the Fourier transform to be replaced.
- $\alpha$ (Gaussian width parameter), bound on `gaussian-resampling`: An integer, with 2 <= alpha < sqrt p, that is the width parameter of the Gaussian weights.
- $\delta$ (exponent slack), bound on `gaussian-resampling`: A fixed constant 0 < delta < 1/8 that is the slack in the exponents of the time bounds.
- $k$ (output coordinate index), bound on `gaussian-resampling`: A coordinate index of a vector in C^t, taken modulo t.
- $t$ (target length), bound on `gaussian-resampling`: The larger length, a power of two in the application, of the transform used instead of the length-s one.

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

## Page to audit (`retained-permutations`)

````markdown
# Retained permutation cancellation

Retained permutation cancellation computes the prime-length Fourier transforms of the integer product through power-of-two ones without executing any coordinate permutation as a sort: the permutations of Gaussian resampling stay inside the transform identity, where one is absorbed by a convolution and the other cancels.

Take $d$ axes with pairwise coprime prime lengths $s_i$ and power-of-two lengths $t_i>s_i$, with $\gcd(s_i,t_i)=1$ (automatic for odd $s_i$). Write $\boldsymbol s=(s_1,\dots,s_d)$, $\boldsymbol t=(t_1,\dots,t_d)$, $S=\prod_is_i$, $T=\prod_it_i$. For operators $X_i$ acting on vectors of length $q_i$, $\bigotimes_iX_i$ acts on a $d$-axis array by applying $X_i$ along every line of axis $i$. Operators on different axes touch different indices, so for further operators $Y_i$, $\bigl(\bigotimes_iX_i\bigr)\bigl(\bigotimes_iY_i\bigr)=\bigotimes_iX_iY_i$. For a tuple $\boldsymbol q$ of axis lengths, $F_{\boldsymbol q}=\bigotimes_iF_{q_i}$ is the normalized [discrete Fourier transform](dft.md) along every axis, and $F_{\boldsymbol q}^+$ its opposite.

Each prime-length transform is computed through a power-of-two one by [Gaussian resampling](gaussian-resampling.md), whose usual implementation sorts twice on each coordinate (cited). For one axis, with $p$ and $\alpha$ as there and $\delta$ the fixed exponent in its time bound, let $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$ ($u,v$ are complex arrays here, not integers). That page gives linear contractions $A$, $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$, computed in time $O(tp^{3/2+\delta}\alpha)$ without executing $P_s$ or $P_t$.

Tensor this identity over the axes. Put $R=\bigotimes_iP_{s_i}$ (a permutation, not a ring), $Q=\bigotimes_iP_{t_i}$, $\mathcal A=\bigotimes_iA_i$, $\mathcal B_0=\bigotimes_iB_{0,i}$. By the product rule the left sides combine to $RF_{\boldsymbol s}$, and the right sides to $\mathcal B_0QF_{\boldsymbol t}\mathcal A$ times $d$ factors $2^{2\alpha^2}$, so $RF_{\boldsymbol s}=2^\gamma\mathcal B_0QF_{\boldsymbol t}\mathcal A$ with $\gamma=2d\alpha^2$. Both $\mathcal A$ and $\mathcal B_0$ are contractions, applied one line at a time in a padded box of $T$ entries. Errors and times add over the $d$ passes: error below $dp^2$, time $O(dTp^{3/2+\delta}\alpha)$ with a constant independent of $d$. Each axis is exposed as the innermost field by the [fast address-chunk interchange](address-interchange.md). With $t_i\in\{t_{\max}/2,t_{\max}\}$, $t_{\max}=2^\ell$, at most $2dT/t_{\max}$ lines occur, since $t_i\ge t_{\max}/2$, so setup $O(p^g)$ per line ($g$ a fixed exponent) totals $O(dTp^g/t_{\max})=o(Tp)$ when $t_{\max}$ outgrows every power of $p$ and $d$ is polynomially bounded in $p$. With entries of $O(p)$ bits, exposing and restoring all lines costs $O(Tp\,d^2(1+\ell^\tau))$ (cited).

The target permutation $Q$ is absorbed by the [Bluestein chirp identity](chirp.md): for even $t_i$ and $a_{\boldsymbol j}=\exp(-\pi i\sum_is_ij_i^2/t_i)$, where $\boldsymbol j=(j_1,\dots,j_d)$ indexes the entries, $QF_{\boldsymbol t}u=\overline a\cdot\bigl(a*(\overline a\cdot u)\bigr)/T$, with $*$ the [cyclic convolution](convolution.md) and a dot coordinatewise multiplication. So $Q$ is part of a convolution of length $T$ and never executed.

The source permutation $R$ cancels: $(RF_{\boldsymbol s}^+)[(RF_{\boldsymbol s}u)\cdot(RF_{\boldsymbol s}v)]=u*v/S^2$. For a unit $c$ modulo $q$ and a vector $z$ of $q$ entries, let $(R_cz)_j=z_{cj}$. Substituting $h=ck$ in the Fourier sum gives $F_q^+R_c=R_c^{-1}F_q^+$. Each $t_i$ is a unit modulo $s_i$ by the coprimality assumed, and $R$ applies $R_{t_i}$ on axis $i$, so tensoring gives $RF_{\boldsymbol s}^+R=F_{\boldsymbol s}^+$. A permutation commutes with pointwise products, so the left side is $RF_{\boldsymbol s}^+R(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)=F_{\boldsymbol s}^+(F_{\boldsymbol s}u\cdot F_{\boldsymbol s}v)$. The normalized convolution rule is $F_{\boldsymbol s}(u*v)=S(F_{\boldsymbol s}u)\cdot(F_{\boldsymbol s}v)$ and $F_{\boldsymbol s}^+F_{\boldsymbol s}=I/S$, so this equals $\frac1SF_{\boldsymbol s}^+F_{\boldsymbol s}(u*v)=u*v/S^2$.
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

Write the answer to `exegenius/tasks/0140-audit-retained-permutations.answer.json`, then run `exegenius submit 0140-audit-retained-permutations` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0140-audit-retained-permutations`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
