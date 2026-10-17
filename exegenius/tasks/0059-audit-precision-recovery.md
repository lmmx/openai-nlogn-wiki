# exegenius task 0059-audit-precision-recovery

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
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Phase twist
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
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
- $h$ (ground-set size), bound on `exchange-network`: The size of the ground set $[h]$ whose three-element subsets index the banks.
- $v$ (number of triples), bound on `exchange-network`: The number of three-element subsets of $[h]$.
- $s$ (number of smaller calls), bound on `subspace-labels`: The total number of smaller calls that the network's edges cost.
- $h$ (ground-set size), bound on `subspace-labels`: The size of the ground set whose three-element subsets index the network, $h=100$.
- $F$ (one-factor label space), bound on `subspace-labels`: The space $\mathbb Q^h$ (bit network) or $\mathbb F_2^h$ (complex network) with its bilinear form.
- $L$ (total dimension loss), bound on `subspace-labels`: The total dimension lost on decreasing edges.
- $j$ (stage number), bound on `subspace-labels`: The stage, 1, 2 or 3, whose invocations vary coordinate $a_j$.
- $B$ (complement of P), bound on `subspace-labels`: The orthogonal complement of $P$ inside $A$.
- $\gamma$ (central wires per invocation), bound on `subspace-labels`: The number of central wires in one invocation: 100 in the bit network, 101 in the complex one.
- $f$ (call parameter), bound on `rank-recurrence`: The parameter of a call: the number of digits in each of the two interchanged chunks, or the number of axes the butterfly layer acts on.
- $V$ (volume), bound on `rank-recurrence`: The volume of a call: the number of data symbols it processes.
- $s$ (number of smaller calls), bound on `rank-recurrence`: The number of calls at parameter f made by a call at parameter mf: the total rank of the frame changes over all edges of the network.
- $F$ (normalized cost), bound on `rank-recurrence`: F(f) is the running time of a call at parameter f divided by its volume.
- $k$ (recursion depth), bound on `rank-recurrence`: The number of levels of recursion: the number of factors m in a parameter m^k.
- $n$ (bit length), bound on `conjecture`: The number of bits in each of the two integers being multiplied.
- $V$ (array volume), bound on `stream-ops`: The number of radix-q digits stored in the array.
- $q$ (radix), bound on `stream-ops`: The number of values one digit can take.
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the stored grid, so values are integers divided by 2^p.
- $k$ (operation count), bound on `fixed-point`: The number of operations applied since the layer began.
- $Q_p$ (truncation), bound on `fixed-point`: The single truncation that drops the bits below 2^{-p} in each real and imaginary part.
- $p$ (precision bits), bound on `signed-packing`: The number of fractional bits in each coefficient component.
- $q$ (prime), bound on `controlled-shifts`: The prime base of the field arithmetic.
- $b$ (field digits), bound on `controlled-shifts`: The number of base-$q$ digits of a field.
- $Q$ (field size), bound on `controlled-shifts`: The number of values a field can hold, Q = q^b.
- $V$ (array volume), bound on `controlled-shifts`: The number of stored data bits in the array.
- $a$ (offset), bound on `controlled-shifts`: The offset added to the target field, prepared from the control values.
- $B$ (suffix length), bound on `controlled-shifts`: The number of bits following the target field.
- $c$ (scaling integer), bound on `controlled-shifts`: A fixed positive integer prime to q by which the target is multiplied.
- $a$ (rank), bound on `matrix-shear`: The rank of the matrix A.
- $q$ (base prime), bound on `matrix-shear`: A fixed odd prime; fields are residues modulo q^b.
- $b$ (digits per field), bound on `matrix-shear`: The number of base-q digits in a field.
- $V$ (data volume), bound on `matrix-shear`: The volume of data being processed.
- $i$ (row index), bound on `matrix-shear`: The row of a one of Pi.
- $j$ (column index), bound on `matrix-shear`: The column of a one of Pi.
- $h$ (value of H_i), bound on `matrix-shear`: The initial value of the field H_i.
- $d$ (value of D_j), bound on `matrix-shear`: The initial value of the field D_j.
- $u$ (chunk width), bound on `address-interchange`: The number of bits in each of the two address chunks.
- $V$ (volume), bound on `address-interchange`: The number of entries of the array.
- $q$ (radix), bound on `address-interchange`: The fixed prime used as digit radix.
- $e$ (chunk digits), bound on `address-interchange`: The number of radix-q digits in each chunk.
- $k$ (levels), bound on `address-interchange`: The number of recursion levels, with e = m^k.
- $b$ (field width), bound on `address-interchange`: The number of digits in each field.
- $s$ (total edge rank), bound on `address-interchange`: The sum of the ranks of the edge matrices.
- $M$ (vertex matrix), bound on `address-interchange`: The matrix attached to a network vertex, determining its frame.
- $d$ (chunk bound), bound on `packed-bit-addition`: Maximum number of chunks a layer acts on.
- $c$ (control), bound on `packed-bit-addition`: Boolean control of the eight additions.
- $u$ (target integer), bound on `packed-bit-addition`: Integer whose parity is flipped by the eight additions.
- $w$ (auxiliary integer), bound on `packed-bit-addition`: Arbitrary auxiliary integer restored by the eight additions.
- $L$ (bits per chunk), bound on `packed-bit-addition`: Number of bits in each address chunk.
- $f$ (selected bits), bound on `packed-bit-addition`: Number of selected bits in each chunk.
- $M$ (address count), bound on `packed-bit-addition`: Number of addresses.
- $V$ (volume), bound on `packed-bit-addition`: Total number of bits, M times R.
- $\mathcal B$ (exceptional set), bound on `packed-bit-addition`: Set of addresses where some guard fails the interval test.
- $p$ (coefficient precision), bound on `packed-bit-addition`: Bit precision of the record coefficients.
- $q$ (sequence length), bound on `convolution`: The number of entries in each of the two sequences being convolved.
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
- $c_j$ (product coefficient), bound on `radix-digit-reduction`: The coefficient of x^j in the product of the digit polynomials.
- $d$ (number of axes), bound on `phase-twist`: The number of axes of the array f.
- $T$ (total entries), bound on `phase-twist`: The number of entries of the array f in all.
- $M$ (number of records), bound on `phase-twist`: The number of lines along the last axis, T/r.

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

## Page to audit (`precision-recovery`)

````markdown
# Error tracking and exact recovery

Error tracking and exact recovery shows the error is below $1/2,$ so rounding is exact.

The computation runs on [Fixed-point Gaussian dyadic records](fixed-point.md). Let $b$ be the bits per radix digit, $p=6b$ the fractional bits, $T$ the padded array size, $S\le T$ the convolution length, $L=\log_2T,$ $\gamma$ the source scale exponent, $d$ the axis count.

Use $h_p=2^{-p}$ and the sup norm throughout; an error of $a$ means error less than $ah_p.$ Each synthetic transform has error less than $\sqrt2\ell\,2^{-p}<L2^{-p}$ with $L=\log_2T,$ where $\ell=\log_2r.$

Replacing the operands of a bilinear contraction $\mathcal B$ by $f',g'$ changes the output by at most $\|f'-f\|\|g'\|+\|f\|\|g'-g\|,$ since $\mathcal B(f',g')-\mathcal B(f,g)=\mathcal B(f'-f,g')+\mathcal B(f,g'-g).$ Hence, for disk operands, the two input errors add.

A computed phase product satisfies $\|Q_p(\widetilde ex)-ex\|<(2\|x\|+\sqrt2)h_p<4h_p$ and $\|Q_p(\widetilde ex)\|\le\|x\|,$ for unit phase $e,$ approximation $\widetilde e,$ disk operand $x.$

With $M=T/r$ the ring record count, the ring convolution error is $E_{\rm ring}:=M(3L+2)<5TL,$ and its output has norm below $.701$ when one operand has norm at most $.7.$ Here $3L+2$ is three transforms and a truncation.

The computed complex convolution has error less than $(E_{\rm ring}+4+4+4)h_p<6TLh_p:$ two input twists, the ring approximation and the output untwist. The chirp transform has error $\|\widetilde{\mathscr C}(x)-QF_{\boldsymbol t}x\|<(6TL+2+4+4)h_p<8TLh_p.$

The source transform (error $2dp^2+8TL$ before scaling, then multiplied by $2^\gamma$) has error less than $E_sh_p$ with $E_s=9\cdot2^\gamma TL,$ using $2dp^2<TL$ eventually.

For scaled digit arrays $u,v$ with exact transforms $U,V_1$ and computed $\widetilde U,\widetilde V_1.$ The computed product $z=Q_p(\widetilde U\cdot\widetilde V_1)$ has $\|z-U\cdot V_1\|<(2E_s+2)h_p:$ two terms of norm below $E_sh_p$ each, plus truncation. Use $\widetilde U\cdot\widetilde V_1-U\cdot V_1=(\widetilde U-U)\cdot\widetilde V_1+U\cdot(\widetilde V_1-V_1).$ The opposite transform gives error less than $(3E_s+2)h_p$ relative to $G(U\cdot V_1)=(u*v)/S^2,$ with $G$ exact.

After the first exact multiplication by $S:$ $\widetilde w$ approximates $w=(u*v)/S$ with error less than $E_wh_p,$ $E_w:=S(3E_s+2)<28\cdot2^\gamma T^2L.$ After the second scaling by $2^{2b+4}S,$ undoing $1/S$ and the input scales, the absolute error is $2^{2b+4}S\cdot28\cdot2^\gamma T^2L\cdot2^{-6b}.$ Using $S\le T<2^b,$ $L<b$ it is less than $448b\,2^{-b+\gamma}.$ Since $\gamma\le b/4$ for $b\ge2^{24}$ it is at most $448b\,2^{-3b/4}<1/2.$ (cited) With $p=6b,$ $4b$ spare bits remain; scaling spends $3b+4.$

The true coefficients are integers, so the strict error below $1/2$ makes the nearest integer to the represented value the unique correct coefficient.

We recover the coefficients $c_j$ of the [Multiplication as radix-digit convolution](radix-digit-reduction.md), which satisfy $c_j\le q(2^b-1)^2,$ with $q=\lceil n/b\rceil$ the digits in an $n$-bit input. The carries obey $k_0=0,$ $d_j=(c_j+k_j)\bmod Q_0,$ $k_{j+1}=\lfloor(c_j+k_j)/Q_0\rfloor$ with $Q_0=2^b.$

The carries satisfy $0\le k_j\le q(Q_0-1)<Q_0^2:$ if this holds at $j,$ then $c_j+k_j\le q(Q_0-1)^2+q(Q_0-1)=qQ_0(Q_0-1).$ Dividing by $Q_0$ and $q\le n\le Q_0$ finish the step.

The invariant $\sum_{h<j}c_hQ_0^h=\sum_{h<j}d_hQ_0^h+k_jQ_0^j$ shows the first $j$ radix digits are fixed. It holds at $j=0,$ and each step adds $c_jQ_0^j=(d_j+Q_0k_{j+1})Q_0^j;$ unprocessed terms are multiples of $Q_0^j.$

The exact product is less than $2^{2n},$ so all bits above position $2n-1$ are zero and exactly $2n$ bits are output.
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

Write the answer to `exegenius/tasks/0059-audit-precision-recovery.answer.json`, then run `exegenius submit 0059-audit-precision-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0059-audit-precision-recovery`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
