# exegenius task 0210-audit-transform-layout

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
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the grid on which stored values lie.
- $Q_p$ (truncation), bound on `fixed-point`: The truncation that drops the bits below 2^{-p} in each real and imaginary part, returning a record to the p-bit grid.
- $t$ (gate input count), bound on `array-frames`: The number of input arrays of a gate.
- $q$ (sequence length), bound on `convolution`: The number of entries in each of the two sequences being convolved.
- $d$ (axis count), bound on `convolution`: The number of axes of an array, counting the d-1 cyclic axes plus the coefficient axis.
- $t_i$ (axis length), bound on `convolution`: The length of cyclic axis i.
- $T$ (coefficient count), bound on `convolution`: The total number of complex coefficients in an array.
- $b$ (digit width), bound on `radix-digit-reduction`: The number of bits in one radix digit.
- $T$ (padded length), bound on `radix-digit-reduction`: A power of two with 4n/b <= T < 8n/b.
- $q$ (digit count), bound on `radix-digit-reduction`: The number of radix-2^b digits in each input.
- $d$ (axis count), bound on `phase-twist`: The number of axes of the arrays.
- $\Theta$ (twist map), bound on `phase-twist`: The ring isomorphism from the cyclic ring to the negacyclic ring sending x_d to zeta y.
- $q$ (sequence length), bound on `dft`: The number of entries of a sequence.
- $t$ (transform length), bound on `butterfly`: The number of positions in the sequence being transformed, a power of two.
- $b$ (lowest bit), bound on `butterfly`: The lowest bit of the output index m.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis, a power of two dividing 2r.
- $q$ (radix), bound on `stream-ops`: The number of values one digit can take.
- $B$ (entries per row), bound on `stream-ops`: The number of entries in each row.
- $\boldsymbol t$ (axis lengths), bound on `chirp`: The tuple (t_1,...,t_d) of axis lengths, where t_i is the even number of entries along axis i.
- $F_{\boldsymbol t}$ (normalized transform), bound on `chirp`: The normalized multidimensional discrete Fourier transform with axis lengths t.
- $Q$ (target permutation), bound on `chirp`: The permutation reordering the output so that position j holds the entry of frequency (-s_i j_i)_i.
- $\mathcal H$ (parallel butterfly), bound on `frequency-order`: The parallel butterfly applying H_0 on every participating axis in one round.
- $J_E$ (recordwise monomial), bound on `frequency-order`: The recordwise operation multiplying each record by y^E.
- $q$ (prime modulus base), bound on `controlled-shifts`: A fixed prime; on this page it is not a sequence length.
- $b$ (field digit count), bound on `controlled-shifts`: The number of base-$q$ digits of a field.
- $Q$ (field value count), bound on `controlled-shifts`: The number of values a field can take, q^b.
- $B$ (suffix bit count), bound on `controlled-shifts`: The number of bits following the target field.
- $H$ (target group), bound on `matrix-shear`: The first group of m fields, which receives AD.
- $D$ (source group), bound on `matrix-shear`: The second group of m fields, which is left unchanged by the shear.
- $b$ (kernel coefficient b), bound on `phase-kernel`: The complex constant (1-i)/2, the coefficient of the bit flip in C.
- $H$ (normalized Hadamard matrix), bound on `phase-kernel`: The matrix sqrt(2) H_0, symmetric with H squared equal to the identity.
- $L$ (linear map), bound on `contraction-maps`: A linear map whose norm bound is being defined.
- $i$ (axis index), bound on `multidim-transform`: The index of an axis of the array, from 1 to d.
- $\boldsymbol t$ (padded lengths), bound on `multidim-transform`: The tuple of padded power-of-two axis lengths (t_1,...,t_d).
- $Q$ (padded permutation), bound on `multidim-transform`: The tensor product of the index permutations P_{t_i}.
- $d$ (number of axes), bound on `crt-map`: The number of axes of the target ring.
- $i$ (axis index), bound on `crt-map`: The index of an axis, from 1 to d.
- $t_i$ (padded axis length), bound on `crt-map`: The padded length of axis i, either r/2 or r.
- $\ell$ (address bits), bound on `crt-map`: The base-2 logarithm of the record length r, the number of address bits of a full-width axis.
- $\tau$ (chunk-swap exponent), bound on `crt-map`: A fixed exponent below 1 in the cost of a chunk interchange.
- $T$ (padded record count), bound on `crt-map`: The number of padded records, the product of the t_i.
- $t$ (target length), bound on `gaussian-resampling`: The larger length, a power of two in the application, of the transform used instead of the length-s one.
- $\boldsymbol t$ (padded length tuple), bound on `retained-permutations`: The tuple of the power-of-two axis lengths $t_i$.
- $z$ (vector), bound on `retained-permutations`: A vector of q complex entries being transformed.
- $L$ (log of padded length), bound on `precision-recovery`: The base-2 logarithm of the padded length $T$.
- $\boldsymbol t$ (axis lengths), bound on `precision-recovery`: The tuple of padded axis lengths of the array.
- $\tau$ (chunk-interchange exponent), bound on `parameter-choice`: The exponent in the cost of a chunk interchange.
- $\lambda$ (overhead exponent), bound on `parameter-choice`: The per-node overhead exponent.
- $\lambda'$ (final cost exponent), bound on `parameter-choice`: The final exponent of the cost V d^lambda' on bit volume V.
- $K$ (chunk width), bound on `parameter-choice`: The width in bits of an address chunk.
- $E$ (first space), bound on `tensor-product-of-spaces`: The first of the two finite-dimensional vector spaces being tensored.
- $Q$ (subspace of C), bound on `tensor-product-of-spaces`: A subspace of C.
- $B$ (orthogonal complement), bound on `tensor-product-of-spaces`: The orthogonal complement of P in A.
- $F$ (base space), bound on `tensor-product-of-spaces`: A space of dimension h with a nondegenerate form, whose triple power is the label space.
- $F$ (one-factor label space), bound on `subspace-labels`: The space $\mathbb Q^h$ with the form $x\cdot y-\frac19(\sum_ix_i)(\sum_iy_i)$ for the bit network, or $\mathbb F_2^h$ with the dot product for the complex network.
- $T$ (a triple), bound on `subspace-labels`: A three-element subset of $[h]$ (not the padded size used on other pages).
- $L$ (total dimension loss), bound on `subspace-labels`: The total number of dimensions lost on decreasing edges.
- $B$ (complement of P), bound on `subspace-labels`: The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on `subspace-labels`: The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $F$ (time per unit volume), bound on `rank-recurrence`: The running time of a call at a given parameter divided by the volume of its stream.
- $\tau$ (saving exponent), bound on `address-interchange`: The fixed exponent below 1 in the cost, equal to 1 - 2^{-50}.
- $p$ (prefix), bound on `address-interchange`: The part of an address before the first chunk.
- $d$ (second chunk), bound on `address-interchange`: The second of the two address chunks being interchanged.
- $z$ (suffix), bound on `address-interchange`: The part of an address after the second chunk.
- $q$ (digit radix), bound on `address-interchange`: The fixed prime that is the radix of the digits.
- $i$ (edge index), bound on `address-interchange`: The index of an edge of the network.
- $E$ (edge residual), bound on `phase-frames`: The subspace added to U to reach V, orthogonal to U; here E is not the first space of a tensor product.
- $L$ (chunk bits), bound on `packed-bit-addition`: The number of bits in each of the chunks x, y, z, equal to fK.
- $K$ (segment spacing), bound on `packed-bit-addition`: The spacing between selected positions, at least 6, which is the length of each segment.
- $q$ (address), bound on `packed-bit-addition`: An address of a record after S_0; q' is its destination T_0 S_0^{-1}(q).
- $D$ (selected chunk count), bound on `simultaneous-layer`: The number of address chunks, at most d, on which the layer acts.
- $z$ (array), bound on `simultaneous-layer`: The array of records that the operators act on.
- $E$ (per-invocation bound), bound on `simultaneous-layer`: The bound 64(W+m+1)^3 on the operations added by one invocation of the network.
- $B$ (level factor), bound on `simultaneous-layer`: The number s+E by which each recursion level multiplies the chain bound.
- $\ell$ (depth), bound on `simultaneous-layer`: The depth of a value, the number of operations in sequence that produced it.

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

## Page to audit (`transform-layout`)

````markdown
# Tape layout for synthetic transforms

The tape layout arranges the address bits so that each round of a [synthetic polynomial transform](synthetic-transform.md) runs as one [simultaneous butterfly layer](simultaneous-layer.md) instead of one pass per axis.

Write $\ell=\log_2 r$, the address bits of a long axis, and $D=d-1$, the number of transformed axes. $K$ is the chunk width in bits; $\tau,\lambda'<1$ are the interchange and layer exponents. Axis $i$ has length $t_i\in\{2^{\ell-1},2^\ell\}$. With $\boldsymbol t=(t_1,\dots,t_D)$, $F_{\boldsymbol t}^-$ is the forward synthetic transform along all $D$ axes and $F_{\boldsymbol t}^+$ its opposite. Records are [fixed-point Gaussian dyadic records](fixed-point.md) with $\Theta(p)$ bits per coefficient and $d\ell=O(p)$, so a pass costs $O(Tp)$. Outputs keep the bit-reversed order of [retained frequency order](frequency-order.md), written $B$ along every axis.

A simultaneous layer needs a round's selected bits at a common offset in consecutive $K$-bit chunks (cited).

Call an axis long if it has $\ell$ address bits and short if $\ell-1$. Put $b=(\ell-1)\bmod K$ and $q=\lfloor(\ell-1)/K\rfloor$, so $\ell-1=qK+b$ (new meanings: $b$ counts leftover low bits of an axis, $q$ its whole chunks). Move to a prefix one at a time the top bit of each long axis and the $b$ lowest bits of each axis. At most $D(b+1)=O(dK)$ slots move, so the moves cost $O(TpdK)$ (cited)

To group chunk 1 of every axis, then chunk 2, etc., scan target positions left to right, exchanging the chunk there with the required one if different. This needs at most $Dq-1$ exchanges, each made by the [fast address-chunk interchange](address-interchange.md) at cost $O(TpK^\tau)$, even for nonadjacent chunks (cited). Since $DqK\le d\ell=O(p)$, the exchanges cost $O(Tp\,DqK^\tau)=O(Tp\,(DqK)K^{\tau-1})=O(Tp\,pK^{\tau-1})$. The prefix moves and exchanges define the record permutation $L$; reversing them gives $L^{-1}$.

There are $b+1$ rounds on prefix slots and $qK$ on chunks, $\ell$ in all. A chunk round's selected bits share an offset in $D$ consecutive chunks, so one layer does it at cost $O(Tpd^{\lambda'})$; the chunk rounds cost $O(Tp\ell d^{\lambda'})$ in total (cited) A prefix round handles at most $D$ bits individually at $O(Tp)$ each, so costs $O(Tpd)$; at most $b+1\le K$ such rounds cost $O(TpdK)$.

Each round is the contraction $\mathcal H$ (norm-nonincreasing), the signed coefficient permutation $J_E$, and one truncation $Q_p$. Truncation toward zero is odd and acts separately on each real and imaginary part, so for the array $z$ entering a round $J_EQ_p(\mathcal Hz)=Q_p(J_E\mathcal Hz)$: one truncation follows the exact round. The exact round does not increase the norm of the computed-versus-exact difference, and truncation moves each entry by less than $\sqrt2\,2^{-p}$; the permutations in $L$ are isometries and add no error. By the triangle inequality each round raises the error by less than $\sqrt2\,2^{-p}$, so from zero error the $\ell$ rounds leave error below $\sqrt2\,\ell\,2^{-p}$ (cited).

Arithmetic on named slots after $L$ is conjugated by it. The forward procedure moves records by $L$ and then runs $BF_{\boldsymbol t}^-$, giving $(LBF_{\boldsymbol t}^-L^{-1})L=LBF_{\boldsymbol t}^-$. The opposite procedure runs its arithmetic and restores by $L^{-1}$, giving $L^{-1}(LF_{\boldsymbol t}^+B^{-1}L^{-1})=F_{\boldsymbol t}^+B^{-1}L^{-1}$. Both cost $O(Tp[dK+pK^{\tau-1}+\ell d^{\lambda'}])$.
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

Write the answer to `exegenius/tasks/0210-audit-transform-layout.answer.json`, then run `exegenius submit 0210-audit-transform-layout` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0210-audit-transform-layout`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
