# exegenius task 0055-audit-packed-bit-addition

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
- Polynomial ring modulo y^r + 1 (also: negacyclic ring)
  - $y$ (ring variable): The indeterminate of the polynomials; it satisfies y^r = −1 in the ring.
  - $r$ (record length): The number of complex coefficients in a polynomial of the ring, always a power of two.
- Signed packing (also: Kronecker substitution)
- Fixed-point Gaussian dyadic records
- Linear exchange network with restored scratch wires (also: finite network, motif)
- Frames on wire arrays
- Nested subspace labels and rank deficit (also: rank saving)
- Recursive power saving
- Matrix shear by triangular factorization (also: Bruhat factorization, lower triangular factorization)
- Fast address-chunk interchange (also: chunk swap, tape interchange)
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
- $h$ (ground-set size), bound on `exchange-network`: The size of the ground set $[h]$ whose three-element subsets index the banks.
- $R$ (scalar ring), bound on `array-frames`: The ring of scalars carried by the wires.
- $\rho$ (role permutation), bound on `array-frames`: The map sending each input role to its output role in a signed role permutation.
- $h$ (ground-set size), bound on `subspace-labels`: The size of the ground set whose three-element subsets index the network, $h=100$.
- $L$ (total dimension loss), bound on `subspace-labels`: The total dimension lost on decreasing edges.
- $j$ (stage number), bound on `subspace-labels`: The stage, 1, 2 or 3, whose invocations vary coordinate $a_j$.
- $A$ (exposed factor space), bound on `subspace-labels`: The tensor product $F^{\otimes(j-1)}$ of the factors already exposed before stage $j$.
- $B$ (complement of P), bound on `subspace-labels`: The orthogonal complement of $P$ inside $A$.
- $K$ (later tensor line), bound on `subspace-labels`: The line spanned by $t_{a_{j+1}}\otimes\cdots\otimes t_{a_3}$, tensored onto every label of stage $j$.
- $f$ (call parameter), bound on `rank-recurrence`: The parameter of a call: the number of digits in each of the two interchanged chunks, or the number of axes the butterfly layer acts on.
- $V$ (volume), bound on `rank-recurrence`: The volume of a call: the number of data symbols it processes.
- $\tau$ (saving exponent), bound on `rank-recurrence`: A fixed exponent below 1 with s/W < m^tau, which makes a call cost O(V f^tau); here tau = 1 - 2^{-50}.
- $V$ (array volume), bound on `stream-ops`: The number of radix-q digits stored in the array.
- $p$ (fractional bits), bound on `fixed-point`: The number of fractional bits of the stored grid, so values are integers divided by 2^p.
- $p$ (precision bits), bound on `signed-packing`: The number of fractional bits in each coefficient component.
- $b$ (field digits), bound on `controlled-shifts`: The number of base-$q$ digits of a field.
- $V$ (array volume), bound on `controlled-shifts`: The number of stored data bits in the array.
- $a$ (offset), bound on `controlled-shifts`: The offset added to the target field, prepared from the control values.
- $B$ (suffix length), bound on `controlled-shifts`: The number of bits following the target field.
- $c$ (scaling integer), bound on `controlled-shifts`: A fixed positive integer prime to q by which the target is multiplied.
- $A$ (shear matrix), bound on `matrix-shear`: The fixed rational m by m matrix whose action AD is added to H.
- $a$ (rank), bound on `matrix-shear`: The rank of the matrix A.
- $b$ (digits per field), bound on `matrix-shear`: The number of base-q digits in a field.
- $V$ (data volume), bound on `matrix-shear`: The volume of data being processed.
- $i$ (row index), bound on `matrix-shear`: The row of a one of Pi.
- $j$ (column index), bound on `matrix-shear`: The column of a one of Pi.
- $h$ (value of H_i), bound on `matrix-shear`: The initial value of the field H_i.
- $d$ (value of D_j), bound on `matrix-shear`: The initial value of the field D_j.
- $u$ (chunk width), bound on `address-interchange`: The number of bits in each of the two address chunks.
- $V$ (volume), bound on `address-interchange`: The number of entries of the array.
- $\tau$ (time exponent), bound on `address-interchange`: The fixed exponent below 1 in the time bound, 1-2^{-50}.
- $e$ (chunk digits), bound on `address-interchange`: The number of radix-q digits in each chunk.
- $b$ (field width), bound on `address-interchange`: The number of digits in each field.
- $M$ (vertex matrix), bound on `address-interchange`: The matrix attached to a network vertex, determining its frame.
- $\rho$ (high digits), bound on `address-interchange`: The number of top digits of each chunk interchanged first.
- $R$ (row range), bound on `address-interchange`: The range of the row field formed by the two high parts.

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

## Page to audit (`packed-bit-addition`)

````markdown
# Packed selected-bit addition

Packed selected-bit addition XORs selected bits of chunk $x$ into chunk $y$, using chunk $z$ as restored scratch; the [simultaneous butterfly layer](simultaneous-layer.md), acting on up to $d$ chunks, needs it for changes of basis.

Let $c$ be a Boolean control and $u,w$ integers; do these eight additions in order:

$$\begin{array}{cccc} u\mathrel{-}=c[w\%2=0] & w\mathrel{-}=c[u\%2=0] & u\mathrel{+}=c[w\%2=0] & w\mathrel{+}=c[u\%2=0]\\ w\mathrel{+}=c[u\%2=1] & u\mathrel{+}=c[w\%2=1] & w\mathrel{-}=c[u\%2=1] & u\mathrel{-}=c[w\%2=1]\end{array}$$

For $c=1$ the first four induce the cycle $(00\ 01\ 10)$ on the parities of $(u,w)$ and the last four induce $(01\ 10\ 11),$ so their composition is $(00\ 10)(01\ 11):$ it flips the parity of $u$ and restores $w.$ Tracing $(0,0),(0,1),(1,0),(1,1)$ gives $(1,0),(1,1),(0,0),(0,1),$ since predicates depend only on parities, so the complete output is $(u',w')=(u+c(1-2(u\%2)),w):$ $u$ keeps its quotient by two and $w$ is restored.

A chunk has $L=fK$ bits: $f$ selected bits spaced $K$ apart, at positions $j_i=\rho+iK.$ Let $M$ be the number of addresses, $R$ the bits per record, $V=MR$ the volume, and $A_{\rm rect}$ the bit length of counters, $\log_2(2V)$ rounded up. The packed map performs its rotations as [controlled shifts](controlled-shifts.md) costing $O(V).$ It swaps chunks using the [chunk interchange](address-interchange.md), costing $O(VL^\tau)$ for fixed $\tau<1.$

For $0\le i<f-1,$ the $K$ bits of $y$ from position $j_i$ form a segment $u_i=2g_i+a_i,$ and those of $z$ give $w_i=2h_i+b_i,$ with bits $a_i,b_i.$ The guard values satisfy $0\le g_i,h_i<2^{K-1},$ and the control is $c_i=x_{j_i}.$

One line on all segments is a cyclic shift of a whole chunk by an offset independent of the target chunk, hence a bijection of the rectangle. Let $S_0$ be the eight lines' composition. It uses at most sixteen swaps and eight rotations (cited)

Let $\mathcal B$ be the addresses where a guard of $y$ or $z$ fails $10\le g\le2^{K-1}-11.$ Elsewhere each segment lies in $[20,2^K-21],$ so displacement eight stays in $[0,2^K-1]$ and no segment carries into or borrows from its neighbour. Then $S_0$ equals the ideal XOR map $T_0.$

There are exactly twenty excluded values for each guard among $2^{K-1}.$ A union bound over the $2(f-1)$ guards, with the same guard distribution at every choice of other coordinates, bounds the bad addresses. Hence $|\mathcal B|\le\delta_{\rm bad}M$ with $\delta_{\rm bad}=\min\{1,80(f-1)2^{-K}\},$ whatever the records.

Both $T_0$ and $S_0$ are bijections agreeing off $\mathcal B,$ and $T_0$ preserves $\mathcal B,$ so $T_0S_0^{-1}$ fixes $\mathcal B^c$ and permutes $\mathcal B.$

The repair extracts the records at $\mathcal B$ with destination-rank keys, stably radix-sorts them, and reinserts them in one scan. The keys are distinct because $T_0S_0^{-1}$ permutes $\mathcal B.$

The time is $O(V(L^\tau+1)+MA_{\rm rect}^3+\delta_{\rm bad}MA_{\rm rect}(R+A_{\rm rect})):$ movement costs $O(V(L^\tau+1)),$ record scans $O(MA_{\rm rect}^3+V),$ radix passes $O(|\mathcal B|A_{\rm rect}(R+A_{\rm rect})).$ With coefficient precision $p,$ dividing the extra terms by $V$ gives $A_{\rm rect}^3/R\to0$ and $80(f-1)2^{-K}A_{\rm rect}(1+A_{\rm rect}/R)=o(1)$ when $A_{\rm rect}=O(p),$ $R$ exceeds every polynomial in $p,$ $f\le d\le p$ and $K/\log p\to\infty.$ So the cost is $O(V(L^\tau+1)).$
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

Write the answer to `exegenius/tasks/0055-audit-packed-bit-addition.answer.json`, then run `exegenius submit 0055-audit-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.

Keep any other files you make, such as scripts, in `exegenius/tasks/0055-audit-packed-bit-addition`. Other tasks run at the same time on this machine, and files elsewhere (in /tmp, for example) can be overwritten or run by them. For the same reason, never stop processes by name or pattern (`pkill`, `killall`), which would stop other tasks' commands too: stop a command of your own by its process id.
