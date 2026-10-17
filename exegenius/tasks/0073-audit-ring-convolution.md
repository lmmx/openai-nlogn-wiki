# exegenius task 0073-audit-ring-convolution

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
- $r$ (record length), bound on `ring-y`: The number of complex coefficients in a polynomial of the ring, always a power of two.
- $v$ (number of triples), bound on `exchange-network`: The number of three-element subsets of $[h]$.
- $I$ (invocation count), bound on `exchange-network`: The number of invocations.
- $R$ (scalar ring), bound on `array-frames`: The ring of scalars carried by the wires.
- $F$ (one-factor label space), bound on `subspace-labels`: The space $\mathbb Q^h$ (bit network) or $\mathbb F_2^h$ (complex network) with its bilinear form.
- $L$ (total dimension loss), bound on `subspace-labels`: The total dimension lost on decreasing edges.
- $P$ (earlier tensor line), bound on `subspace-labels`: The line spanned by $t_{a_1}\otimes\cdots\otimes t_{a_{j-1}}$ inside $A$.
- $B$ (complement of P), bound on `subspace-labels`: The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on `subspace-labels`: The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $I$ (invocation count), bound on `subspace-labels`: The number of invocations over all three stages.
- $f$ (call parameter), bound on `rank-recurrence`: The parameter of a call: the number of digits in each of the two interchanged chunks, or the number of axes the butterfly layer acts on.
- $F$ (normalized cost), bound on `rank-recurrence`: F(f) is the running time of a call at parameter f divided by its volume.
- $\tau$ (saving exponent), bound on `rank-recurrence`: A fixed exponent below 1 with s/W < m^tau, which makes a call cost O(V f^tau); here tau = 1 - 2^{-50}.
- $\eta$ (relative deficit), bound on `rank-recurrence`: The fraction (Wm - s)/(Wm) by which the number of smaller calls s falls short of Wm.
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the stored grid, so values are integers divided by 2^p.
- $Q_p$ (truncation), bound on `fixed-point`: The single truncation that drops the bits below 2^{-p} in each real and imaginary part.
- $p$ (precision bits), bound on `signed-packing`: The number of fractional bits in each coefficient component.
- $Q$ (field size), bound on `controlled-shifts`: The number of values a field can hold, Q = q^b.
- $B$ (suffix length), bound on `controlled-shifts`: The number of bits following the target field.
- $i$ (row index), bound on `matrix-shear`: The row of a one of Pi.
- $d$ (value of D_j), bound on `matrix-shear`: The initial value of the field D_j.
- $u$ (chunk width), bound on `address-interchange`: The number of bits in each of the two address chunks.
- $\tau$ (time exponent), bound on `address-interchange`: The fixed exponent below 1 in the time bound, 1-2^{-50}.
- $M$ (vertex matrix), bound on `address-interchange`: The matrix attached to a network vertex, determining its frame.
- $R$ (row range), bound on `address-interchange`: The range of the row field formed by the two high parts.
- $d$ (chunk bound), bound on `packed-bit-addition`: Maximum number of chunks a layer acts on.
- $u$ (target integer), bound on `packed-bit-addition`: Integer whose parity is flipped by the eight additions.
- $L$ (bits per chunk), bound on `packed-bit-addition`: Number of bits in each address chunk.
- $f$ (selected bits), bound on `packed-bit-addition`: Number of selected bits in each chunk.
- $K$ (spacing), bound on `packed-bit-addition`: Spacing between consecutive selected positions, which is also the bit length of a segment.
- $M$ (address count), bound on `packed-bit-addition`: Number of addresses.
- $R$ (record length), bound on `packed-bit-addition`: Number of bits in a record.
- $\tau$ (interchange exponent), bound on `packed-bit-addition`: Fixed exponent below one in the cost of the chunk interchange.
- $p$ (coefficient precision), bound on `packed-bit-addition`: Bit precision of the record coefficients.
- $t_i$ (axis length), bound on `convolution`: The length of axis i of the array.
- $M$ (cyclic addresses), bound on `convolution`: The number of cyclic addresses on the first d-1 axes, the product of t_i for i<d.
- $T$ (total coefficients), bound on `convolution`: The total number of complex coefficients in an array, rM.
- $u$ (first input), bound on `radix-digit-reduction`: The first of the two integers being multiplied.
- $v$ (second input), bound on `radix-digit-reduction`: The second of the two integers being multiplied.
- $T$ (padded length), bound on `radix-digit-reduction`: A power of two with 4n/b <= T < 8n/b.
- $d$ (number of axes), bound on `phase-twist`: The number of axes of the array f.
- $T$ (total entries), bound on `phase-twist`: The number of entries of the array f in all.
- $M$ (number of records), bound on `phase-twist`: The number of lines along the last axis, T/r.
- $\mathcal M_r$ (ring convolution), bound on `phase-twist`: The ring convolution that convolves the first d-1 axes over the negacyclic ring and includes the division by T.
- $p$ (fractional bits), bound on `precision-recovery`: The number of fractional bits of the fixed-point grid, equal to $6b$.
- $T$ (padded array size), bound on `precision-recovery`: The number of records in the padded array.
- $L$ (log of T), bound on `precision-recovery`: The base-2 logarithm of $T$.
- $d$ (axis count), bound on `precision-recovery`: The number of transform axes.
- $\ell$ (log of r), bound on `precision-recovery`: The base-2 logarithm of the record length $r$.
- $M$ (ring record count), bound on `precision-recovery`: The ratio $T/r$, the number of ring records.
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to which the transform is applied.
- $t$ (transform length), bound on `butterfly`: The number of values in the transform, a power of two.
- $d$ (number of axes), bound on `multidim-transform`: The number of axes (coordinates) of the array.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis of the transform, a power of two dividing 2r.
- $d$ (number of axes), bound on `crt-map`: The number of axes.
- $t_i$ (padded length), bound on `crt-map`: The padded length of axis i, a power of two at least s_i.
- $\ell$ (axis bit width), bound on `crt-map`: The number of bits of the widest axis.
- $T$ (padded array size), bound on `crt-map`: The number of records in the padded array.
- $p$ (record precision), bound on `crt-map`: The number of bits of precision per record.
- $\tau$ (chunk-swap exponent), bound on `crt-map`: The fixed exponent in (0,1) governing the cost of a chunk interchange.
- $t$ (power-of-two length), bound on `gaussian-resampling`: The power-of-two length of the nearby transform, the number of complex coordinates it acts on.
- $p$ (precision bits), bound on `gaussian-resampling`: The number of bits of precision of each real and imaginary component.
- $d$ (number of axes), bound on `chirp`: The number of axes (coordinates) of an index.
- $t_i$ (axis length), bound on `chirp`: The even number of entries along axis i.
- $T$ (total entries), bound on `chirp`: The total number of entries, the product of the t_i.
- $Q$ (target permutation), bound on `chirp`: The target permutation, reading frequency (-s_i j_i)_i at output position j.
- $d$ (number of axes), bound on `retained-permutations`: The number of coordinate axes.
- $t_i$ (power-of-two length), bound on `retained-permutations`: The power-of-two length of axis i.
- $T$ (padded box size), bound on `retained-permutations`: The number of entries in the padded box, the product of the power-of-two lengths.
- $p$ (bit precision), bound on `retained-permutations`: The number of bits of precision of each coordinate.
- $\delta$ (time exponent), bound on `retained-permutations`: A fixed exponent in the time bound.
- $R$ (source permutation), bound on `retained-permutations`: The source coordinate permutation, tensor product of the one-axis permutations P_{s_i}.
- $Q$ (target permutation), bound on `retained-permutations`: The target coordinate permutation, tensor product of the one-axis permutations P_{t_i}.
- $\tau$ (chunk-swap exponent), bound on `retained-permutations`: The fixed exponent below 1 in the chunk-swap time bound.
- $t$ (transform length), bound on `frequency-order`: The number of ring elements transformed along one axis, a power of two dividing 2r.
- $C$ (two-point kernel), bound on `phase-kernel`: The matrix aI + bX, a square root of the bit flip.
- $K$ (chunk width), bound on `simultaneous-layer`: The number of bits in an address chunk.
- $p$ (fractional bits), bound on `simultaneous-layer`: The number of fractional bits of each coefficient.
- $d$ (chunk bound), bound on `simultaneous-layer`: The maximum number of chunks, D at most d.
- $f$ (slot width), bound on `simultaneous-layer`: The number of bits in each slot.
- $\ell$ (address bits per record), bound on `transform-layout`: The number of address bits within a record, log base 2 of r.
- $d$ (size parameter), bound on `transform-layout`: A size parameter one more than the number of axes, with d times ell of order p.
- $t_i$ (axis length), bound on `transform-layout`: The length of axis i, either 2^(ell-1) or 2^ell.
- $M$ (record count), bound on `transform-layout`: The number of polynomial records, the product of the axis lengths.
- $T$ (coefficient count), bound on `transform-layout`: The number of complex coefficients, r times M.
- $p$ (precision), bound on `transform-layout`: The precision in bits: coefficient parts are multiples of 2^-p.
- $K$ (chunk width), bound on `transform-layout`: The width in bits of an address chunk.
- $\tau$ (interchange exponent), bound on `transform-layout`: The fixed exponent below 1 in the cost of chunk interchange.
- $\lambda'$ (layer exponent), bound on `transform-layout`: The fixed exponent below 1 in the cost of the simultaneous layer.
- $B$ (bit reversal), bound on `transform-layout`: The bit-reversal order in which forward outputs are written.
- $L$ (layout permutation), bound on `transform-layout`: The permutation of records built by the prefix moves and chunk exchanges.
- $Q_p$ (truncation), bound on `transform-layout`: Truncation toward zero of real and imaginary parts to the 2^-p grid.

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

## Page to audit (`ring-convolution`)

````markdown
# Convolution from the retained transform layout

Convolution over $\mathcal R_r=\mathbb C[y]/(y^r+1)$ on the remaining axes is computed by transforming both operands, multiplying records pointwise and transforming back.

Arrays are indexed by $\prod_i\mathbb Z/t_i\mathbb Z$ over the $d-1$ remaining axes, with values in $\mathcal R_r$. Let $M=\prod_i t_i$ be the number of records, $T=rM$ the number of complex coefficients, and $*$ cyclic convolution. A disk array has coefficients of modulus below $1$; $\|\cdot\|_\infty$ is the largest coefficient modulus.

For arrays over $\mathcal R_r$ define $\mathcal M_r(f,g)=\frac{f*g}{rM}=\frac{f*g}{T}$. A fixed output coefficient averages $rM$ signed scalar products (cited): each of the $M$ first addresses determines one second address, each of the $r$ first polynomial indices determines one second index modulo $r$, and the negacyclic wrap supplies the sign. So $\mathcal M_r$ is a bilinear contraction, $\|\mathcal M_r(f,g)\|_\infty\le\|f\|_\infty\|g\|_\infty$.

Let $F^-$, $F^+$ be the forward and opposite synthetic transforms. Expansion of the finite sums gives $F^-(f*g)=M(F^-f)(F^-g)$. With $F^+F^-=I/M$ ([Discrete Fourier transform](dft.md)), it follows that $MF^+\bigl((F^-f)(F^-g)/r\bigr)=f*g/(rM)$. Write $P(u,v)=uv/r$ for the pointwise product.

The transforms are laid out as in [Tape layout for synthetic transforms](transform-layout.md). Perform both forward transforms and retain their common $LB$ order, with $L$ the layout and $B$ the frequency permutation. Multiply the $M$ pairs of records pointwise there, apply the opposite procedure to that order, and multiply by $M$. Since $LB$ permutes records and leaves polynomial suffixes intact, $P(LBu,LBv)=LBP(u,v)$, so the opposite transform $\mathcal T_+=F^+B^{-1}L^{-1}$ applied to the pointwise product of the stored forward outputs equals $F^+P(F^-f,F^-g)$. The procedure keeps the retained order of [Retained frequency order](frequency-order.md), forming the product there and passing it to the opposite transform. Each record product is formed by [Signed packing](signed-packing.md) in $O(rp\log(rp))$ time, truncated by $Q_p$ to $p$ bits of precision. There are $M=T/r$ pointwise products, so their total cost is $O(Tp\log(rp))$, and the final exact scaling is linear in $Tp$. Each transform costs $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$, where $\ell=\log_2r$, $K$ is the layout chunk width, and $\tau,\lambda'$ are exponents from the cost lemma. Put $\delta=\sqrt2\ell\,2^{-p}$ for each forward transform error and $\eta=\sqrt2\,2^{-p}$ for one truncation. Let $u,v$ be the exact stored forward outputs, $\widetilde u,\widetilde v$ the returned ones. By bilinearity of $P$ and the disk bound on both operands, $\|P(\widetilde u,\widetilde v)-P(u,v)\|_\infty<2\delta$. After truncation, $\|\widetilde z-z_*\|_\infty<2\delta+\eta$, where $\widetilde z=Q_p(P(\widetilde u,\widetilde v))$ and $z_*=P(u,v)$. Since the opposite transform $\mathcal T_+$ is a contraction with its own error $\delta$, the output error is less than $3\delta+\eta$. The exact multiplication by $M$ gives total error less than $M(3\delta+\eta)=\sqrt2\,M(3\ell+1)2^{-p}$ (cited).
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

Write the answer to `exegenius/tasks/0073-audit-ring-convolution.answer.json`, then run `exegenius submit 0073-audit-ring-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0073-audit-ring-convolution`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
