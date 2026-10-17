# exegenius task 0139-audit-gaussian-resampling

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
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the grid on which stored values lie.
- $k$ (depth), bound on `fixed-point`: The number of operations in sequence since the layer began that produced a value.
- $v$ (triple count), bound on `exchange-network`: The number of three-element subsets of [h].
- $N$ (bank size), bound on `exchange-network`: The size of each data bank.
- $S$ (triple), bound on `exchange-network`: A three-element subset of [h], indexing a value in a bank.
- $S'$ (other triple), bound on `exchange-network`: A second triple, the index of a source value x_{S'}.
- $I$ (invocation count), bound on `exchange-network`: The number of invocations.
- $t$ (gate input count), bound on `array-frames`: The number of input arrays of a gate.
- $q$ (sequence length), bound on `convolution`: The number of entries in each sequence being convolved.
- $T$ (total coefficient count), bound on `convolution`: The total number of complex coefficients in an array.
- $u$ (first input), bound on `radix-digit-reduction`: The first of the two integers being multiplied.
- $v$ (second input), bound on `radix-digit-reduction`: The second of the two integers being multiplied.
- $T$ (padded length), bound on `radix-digit-reduction`: A power of two with 4n/b <= T < 8n/b.
- $S$ (convolution length), bound on `radix-digit-reduction`: The length of the cyclic convolution, a product of distinct odd primes with T/2 < S < T.
- $q$ (digit count), bound on `radix-digit-reduction`: The number of radix-2^b digits in each input.
- $k$ (coefficient index), bound on `phase-twist`: An index of a coefficient (not an operation count).
- $j$ (wrapped position), bound on `phase-twist`: The position k+l reduced modulo r.
- $q$ (sequence length), bound on `dft`: The number of entries of a sequence.
- $u$ (input sequence), bound on `dft`: A sequence of q complex numbers to be transformed.
- $t$ (transform length), bound on `butterfly`: The number of positions in the sequence being transformed, a power of two.
- $t$ (transform length), bound on `synthetic-transform`: The number of ring elements along one axis, a power of two dividing 2r.
- $e$ (two-adic exponent), bound on `synthetic-transform`: The exponent of 2 in j when j is written as 2^e times an odd number.
- $q$ (radix), bound on `stream-ops`: The number of values one digit can take.
- $P$ (prefix values), bound on `stream-ops`: The number of prefix values indexing the first axis of the array.
- $B$ (entries per row), bound on `stream-ops`: The number of entries in each row.
- $s$ (completed rounds), bound on `frequency-order`: The number of rounds completed so far.
- $i$ (axis index), bound on `frequency-order`: Index of an axis of the array.
- $E$ (combined exponent), bound on `frequency-order`: The exponent of y by which the record at an address is multiplied, determined by that address.
- $v$ (two-adic exponent), bound on `frequency-order`: The exponent of 2 in j, with 0<=v<a.
- $N$ (factor bit length), bound on `hvdh-multiplier`: The number of bits in each of the two integers of one product given to the established multiplier (not the bank size).
- $p$ (fractional bits), bound on `signed-packing`: The number of fractional bits of each coefficient component.
- $B_0$ (packing base), bound on `signed-packing`: The base 2^{4p} at which polynomials are evaluated.
- $u_j$ (coefficient of u), bound on `signed-packing`: The coefficient of y^j in u.
- $q_j$ (block of Z), bound on `signed-packing`: The j-th block of Z in sign-extended two's complement, in [0,B_0).
- $q$ (prime), bound on `controlled-shifts`: The prime base of the digits of a field.
- $B$ (suffix bits), bound on `controlled-shifts`: The number of bits following the target field.
- $j$ (piece index), bound on `controlled-shifts`: The index of the increasing piece of y -> cy mod Q containing y.
- $A$ (shear matrix), bound on `matrix-shear`: The fixed rational matrix whose product with D is added to H.
- $D$ (source group), bound on `matrix-shear`: The ordered group of m fields that is added in and left unchanged.
- $I$ (identity matrix), bound on `phase-kernel`: The 2 by 2 identity matrix.
- $C$ (two-point kernel), bound on `phase-kernel`: The 2 by 2 matrix aI+bX.
- $\mathsf S$ (phase matrix), bound on `phase-kernel`: The diagonal matrix diag(1,i) multiplying the second entry of a pair by i.
- $L$ (linear map), bound on `contraction-maps`: A linear map whose norm bound is being defined.
- $F_q$ (normalized transform), bound on `contraction-maps`: The normalized discrete Fourier transform on sequences of q entries.
- $j$ (index tuple), bound on `multidim-transform`: The index tuple of an entry of the array, with 0 <= j_i < q_i.
- $k$ (output index tuple), bound on `multidim-transform`: An output index tuple of the same shape as j.
- $\alpha$ (resampling parameter), bound on `multidim-transform`: An integer parameter of the Gaussian resampling with 2 <= alpha < sqrt p.
- $\delta$ (time exponent slack), bound on `multidim-transform`: A fixed constant with 0 < delta < 1/8 in the exponent of the running time.
- $S$ (convolution length), bound on `crt-map`: The length of the cyclic convolution, the product of the s_i.
- $i$ (axis index), bound on `crt-map`: The index of an axis, from 1 to d.
- $k$ (coefficient index), bound on `crt-map`: The index of a coefficient of the length-S sequence.
- $T$ (padded record count), bound on `crt-map`: The number of padded records, the product of the t_i.

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

## Page to audit (`gaussian-resampling`)

````markdown
# Gaussian resampling

Gaussian resampling expresses a Fourier transform of length $s$ through one of a nearby larger length $t$ (a power of two there), so that only power-of-two transforms need a fast algorithm. Some earlier letters are reused here.

Let $s<t<2^p$ be coprime integers, where $p>100$ counts the fractional bits of each real and imaginary component, and let $\alpha$, the width parameter of the Gaussian weights below, be an integer with $2\le\alpha<\sqrt p$. Assume $\theta:=t/s-1>p/\alpha^4$. Here $F_q$ is the normalised [Discrete Fourier transform](dft.md) of length $q$, and the resampling expresses $F_s$ through $F_t$. Define the permutations $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$ (coordinate indices $j$, $k$ taken modulo $s$, $t$), which stay in the identity, never executed as sorts. There are linear contractions $A$, $B_0$ with $P_sF_s=2^{2\alpha^2}B_0P_tF_tA$. Applied along each axis of a [Multidimensional transforms](multidim-transform.md), it replaces $s$ by $t$.

## Exact construction

Harvey and van der Hoeven's maps $\mathsf S,\mathsf T$ from length-$s$ to length-$t$ complex vectors are, for $0\le k<t$, with $u$ extended periodically and $j$ over all integers,
$$(\mathsf Su)_k=\frac1\alpha\sum_j e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (\mathsf Tu)_k=\sum_j e^{-\pi\alpha^2(tj/s-k)^2}u_j.$$
They satisfy $\mathsf TP_sF_s=P_tF_t\mathsf S$ (cited).

To undo $\mathsf T$, let $q_j$ be the integer nearest $tj/s$ and $\beta_j=tj/s-q_j$. Let $C$ select coordinates from length-$t$ to length-$s$ vectors, $(Cv)_j=v_{q_j}$, and $(\mathsf Du)_j=e^{\pi\alpha^2\beta_j^2}u_j$. Put $N=C\mathsf T\mathsf D$. In $(Nu)_j$, the summand with index $j$ is exactly $u_j$: the factor in $\mathsf D$ cancels the Gaussian factor at the selected coordinate $q_j$, because $tj/s-q_j=\beta_j$. The other summands form $((N-I)u)_j$, and the cited estimate gives $\|N-I\|<2.01e^{-\pi\alpha^2\theta/2}<2^{-\alpha^2\theta}$ (cited).

Since $\alpha^2<p$ and $\theta>p/\alpha^4$, $\alpha^2\theta>p/\alpha^2>1$, so $\|N-I\|<1/2$ and $N$ is invertible by the Neumann series $N^{-1}=\sum_i(-1)^i(N-I)^i$.

Set $\mathsf S'=\mathsf S/2$, $\mathsf J'=N^{-1}/2$, $\mathsf D'=2^{-(2\alpha^2-2)}\mathsf D$, and put $A=\mathsf S'$ and $B_0=\mathsf D'\mathsf J'C$. These are contractions, since $\|C\|=1$ and the three factors have norms below $3/4$, $7/8$, $1$ (cited).

As $C\mathsf T=N\mathsf D^{-1}$, the map $\mathsf DN^{-1}C$ is a left inverse of $\mathsf T$; applying it to the identity gives $\mathsf DN^{-1}CP_tF_t\mathsf S=P_sF_s$. The normalizations multiply to $2^{-(2\alpha^2-2)}2^{-1}2^{-1}=2^{-2\alpha^2}$, so $B_0P_tF_tA=2^{-2\alpha^2}P_sF_s$.

## Computing it

Let $\mathbb D_p$ be the grid of [Fixed-point Gaussian dyadic records](fixed-point.md). An approximation $\widetilde L$ of a contraction $L$ has error below a bound if $2^p\|\widetilde Lu-Lu\|$ is less than it for all inputs $u\in\mathbb D_p$; composing approximations adds errors. Fix $0<\delta<1/8$, the time-exponent slack. The cited algorithms give approximations $\widetilde{\mathsf S}'$, $\widetilde{\mathsf J}'$, $\widetilde{\mathsf D}'$ with errors $16p$, $3p^2/4$, $4$ and times $O(tp^{3/2+\delta}\alpha)$, $O(tp^{3/2+\delta}\alpha)$, $O(tp^{1+\delta})$ (cited) (cited) (cited).

The selection $C$ picks an ordered subsequence (since $t/s>1$), and the indices are generated in order with $O(p)$ work each, so $C$ takes $O(tp)$ time with zero error (cited).

Take $\widetilde A=\widetilde{\mathsf S}'$ and $\widetilde B_0=\widetilde{\mathsf D}'\widetilde{\mathsf J}'C$. Contraction of the exact maps yields errors less than $16p<p^2$ and $4+3p^2/4<p^2$ (as $p>100$), and the costs add to $O(tp^{3/2+\delta}\alpha)$.

Let $E=N-I$ and $k=\lceil p/(\alpha^2\theta)\rceil$, the number of series terms kept (a new meaning of $k$). As $\|E\|<2^{-\alpha^2\theta}$ and $\alpha^2\theta>1$, the omitted terms sum to less than $2\cdot2^{-p}$. Let $\widetilde E$ be the approximation of $E$ on $\mathbb D_p$ from the cited Lemma 4.11: for every $z\in\mathbb D_p^s$ $\widetilde Ez\in\mathbb D_p^s$ and $\|\widetilde Ez\|<0.42\|z\|+(p/3)2^{-p}<1$ (cited). Start from $\widetilde v^{(0)}$, the rounding of $u/2$, and set $\widetilde v^{(j)}=\widetilde E\widetilde v^{(j-1)}$. The Neumann series with $E=N-I$ and $k=\lceil p/(\alpha^2\theta)\rceil$ is evaluated as $\widetilde{\mathsf J}'u=\sum_{j=0}^{k-1}(-1)^j\widetilde v^{(j)}$ with every iterate kept in $\mathbb D_p$.
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

Write the answer to `exegenius/tasks/0139-audit-gaussian-resampling.answer.json`, then run `exegenius submit 0139-audit-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0139-audit-gaussian-resampling`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
