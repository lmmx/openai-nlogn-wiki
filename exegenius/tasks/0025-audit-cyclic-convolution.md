# exegenius task 0025-audit-cyclic-convolution

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows the concepts listed as known, and everything the reader profile covers: what anyone with that background has been taught, whether or not the profile names it (a profile of undergraduate computer science covers logarithms and proof by induction without naming them). Anything outside that, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: report what would stop this reader at this point on the page. A term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. A claim marked "(cited)" is attributed to the source, which the reader can consult: it is followable by reference, so do not report it as a step.
- term: a named concept the reader does not know, which the page neither explains nor links. References to the documents themselves (the paper, the sources, the target result) are not terms.
- step: an inference, calculation or claim that the page presents as following from what it gives, which the reader cannot check from what the page gives.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader has completed an undergraduate computer science degree, so they know big-O and related asymptotic notation, polynomials, complex numbers (roots of unity, polar form), and Turing machines with tapes. They also know the discrete mathematics and first linear algebra that every such degree teaches: modular arithmetic, gcd and primes, sets, permutations, binary and radix notation, XOR over GF(2), induction, recurrences and geometric sums, and vector spaces, matrices and Gaussian elimination over a field, with basic sorting. They have not met the Chinese remainder theorem, the FFT, tensor products, bilinear forms, Gaussian integers, prime-number estimates, or operator norms and Neumann series.

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform)
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Big-Theta, big-Omega and little-o notation (also: Theta notation, Omega notation, little-o, asymptotic tight bound, asymptotic lower bound, Θ, Ω, o-notation)
- Logarithms (also: log, log2, binary logarithm, lg, natural logarithm, ln, change of base)
- Floor and ceiling (also: integer part, floor function, ceiling function, round down, round up)
- Mathematical induction (also: induction, proof by induction, strong induction, inductive step)
- Recurrence relations (also: recurrence, recursive inequality, unrolling a recurrence, divide-and-conquer recurrence)
- Geometric series (also: geometric sum, finite geometric sum, geometric progression)
- Sets, intersections and indicator vectors (also: set intersection, intersection size, indicator vector, characteristic vector, k-subsets, three-element subsets)
- Permutations (also: bijection of a finite set, reordering, permutation of coordinates, cyclic shift)
- Lexicographic order (also: dictionary order, lexicographic order on tuples, lexicographic order)
- Positional (radix) notation (also: radix representation, base-b expansion, binary representation, mixed-radix representation, digits, bits, binary string)
- Hamming weight (also: popcount, number of ones, population count, weight of a binary string)
- Two's complement and signed binary (also: twos complement, signed binary numbers, sign extension, sign bit)
- Fixed-point binary numbers (also: fixed-point arithmetic, binary point, fractional bits, guard bits, fixed-width arithmetic)
- Modular arithmetic (also: congruence, congruent modulo n, integers modulo n, Z/nZ, residues, modulo, modular inverse)
- Greatest common divisor and coprimality (also: gcd, coprime, relatively prime, pairwise coprime, Euclid's algorithm, Euclidean algorithm)
- Prime numbers (also: primes, prime factorization, trial division, primality)
- Binary field GF(2) and XOR (also: F2, GF(2), binary field, XOR, exclusive or, addition modulo 2, parity)
- Roots of unity (also: n-th roots of unity, primitive root of unity, primitive n-th root of unity, omega)
- Polar form and Euler's formula (also: modulus and argument, Euler's identity, complex exponential, complex conjugate, unit circle, argument of a complex number)
- Vector spaces over a field (also: linear space, vector space, subspace, span, basis, dimension, linear independence, field)
- Matrices, rank and invertibility (also: matrix inverse, invertible matrix, nonsingular matrix, rank, identity matrix, matrix product, linear map, linear transformation)
- Gaussian elimination and triangular factorization (also: row reduction, elementary row operations, pivot, lower triangular matrix, upper triangular matrix, LU decomposition)
- Eigenvalues and eigenvectors (also: eigenvalue, eigenvector, characteristic polynomial, spectrum)
- Newton's method (also: Newton iteration, Newton-Raphson method, Newton's root-finding method)
- Stable sorting and radix sort (also: stable sort, stable sorting, radix sort, least-significant-digit radix sort, LSD radix sort, counting sort)

## Symbols bound on earlier pages

- $k$ (padded bit width), bound on `exact-integer-multiplication`: The number of bits of the padded binary representation.
- $d$ (digit count), bound on `radix-digit-convolution`: The number of radix-B digits of each input, a count.
- $u$ (digit vector of x), bound on `radix-digit-convolution`: The vector (x_0, ..., x_{d-1}) of the digits of x.
- $v$ (digit vector of y), bound on `radix-digit-convolution`: The vector (y_0, ..., y_{d-1}) of the digits of y.
- $u\ast v$ (convolution of digit vectors), bound on `radix-digit-convolution`: The convolution of u and v, whose m-th entry is the sum of u_i v_j over i+j=m.
- $j$ (input index), bound on `discrete-fourier-transform`: The index of an input entry, running over the input positions 0 to q-1.
- $k$ (output index), bound on `discrete-fourier-transform`: The index of an output entry, running over the output positions 0 to q-1; on this page it replaces the padded width.
- $s$ (source length), bound on `gaussian-resampling`: The number of coordinates of a source vector.
- $F_s$ (source transform), bound on `gaussian-resampling`: The normalized Fourier transform of length s.
- $P_s$ (source permutation), bound on `gaussian-resampling`: The coordinate permutation on vectors of length s, sending g to the vector with j-th entry g_{tj}.
- $j$ (coordinate index), bound on `gaussian-resampling`: An index of a coordinate of a vector.
- $m$ (target coordinate index), bound on `gaussian-resampling`: An index of a coordinate of a target-length vector.
- $I$ (identity map), bound on `gaussian-resampling`: The identity map, which leaves every vector unchanged.
- $S$ (source Gaussian map), bound on `gaussian-resampling`: A Gaussian-weighted map from vectors of length s to vectors of length t.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Transform identity with retained permutations](transform-identity.md)

## Page to audit (`cyclic-convolution`)

````markdown
# Cyclic convolution

Cyclic convolution is the product of two sequences in which indices wrap around modulo the sequence length, and it is the operation the permutation step below works with.

For vectors $u$ and $v$ of length $s$, index the entries by $i,j,m \in \mathbb{Z}/s\mathbb{Z}$, that is, by $0,\dots,s-1$ with sums taken modulo $s$. Here $u$ and $v$ are any vectors, not necessarily digit vectors. The cyclic convolution of $u$ and $v$, written $u\ast v$, has entries

$$(u\ast v)_m=\sum_{i+j\equiv m \pmod s} u_i v_j .$$

Cyclic convolution is the wrap-around form of the [convolution of digit vectors](radix-digit-convolution.md), in which an index $i+j \ge s$ is reduced to $i+j-s$.

For example, take $s=3$, $u=(1,2,0)$ and $v=(0,1,1)$. The ordinary convolution has entries $(0,1,3,2,0)$ at indices $0$ to $4$. The entries at indices $3$ and $4$ wrap onto $0$ and $1$, so $u\ast v=(2,1,3)$.

For arrays indexed by tuples $(i_1,\dots,i_d)$ with $i_k\in\mathbb{Z}/s_k\mathbb{Z}$, the wrap-around applies in each axis separately, and the source uses $\ast$ this way (cited). Let $S=s_1s_2\cdots s_d$, the number of entries of such an array (so $S=s$ when $d=1$). Here $S$ means this product, not the Gaussian map $S$ of the earlier page.

Cyclic convolution is turned into pointwise products by the [discrete Fourier transform](discrete-fourier-transform.md), which is the normalized convolution rule:

$$F_s(u\ast v)=S\,(F_su)\cdot(F_sv),$$

where $F_s$ is the normalized Fourier transform, and $\cdot$ is the entrywise product. The inverse transform $F_s^{+}$ satisfies $F_s^{+}F_s=I/S$.

Write $R$ for the retained source permutation, the $P_s$ of the resampling identity, with inverse $R^{-1}$. The claim $RF_s^{+}R(F_su\cdot F_sv)=(u\ast v)/S^2$ follows in three steps:

- $F_s^{+}R=R^{-1}F_s^{+}$, so $RF_s^{+}R=F_s^{+}$.
- A permutation commutes with pointwise products, so $(RF_su)\cdot(RF_sv)=R(F_su\cdot F_sv)$. This moves $R$ through the product, so the two copies of $R$ can meet across the inverse transform.
- By the convolution rule and $F_s^{+}F_s=I/S$, we get $S\,F_s^{+}(F_su\cdot F_sv)=F_s^{+}F_s(u\ast v)=(u\ast v)/S$, hence $F_s^{+}(F_su\cdot F_sv)=(u\ast v)/S^2$.

The permutation $R$ disappears exactly because the inverse transform carries $R$ to $R^{-1}$, so the two copies cancel. Nothing remains to reorder the result, because permuting before or after a pointwise product gives the same output. The output is $u\ast v$ in its own order, so no sort is executed.
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

Write the answer to `exegenius/tasks/0025-audit-cyclic-convolution.answer.json`, then run `exegenius submit 0025-audit-cyclic-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
