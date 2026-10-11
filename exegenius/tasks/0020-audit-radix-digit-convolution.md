# exegenius task 0020-audit-radix-digit-convolution

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

For these sources: This reader has an undergraduate computer science degree: discrete mathematics (modular arithmetic, gcd and primes, binomial counting, induction), linear algebra over the reals and small fields (subspaces, rank, elimination, eigenvalues, dot-product orthogonal complements and projections), and algorithms (divide-and-conquer recurrences, Karatsuba multiplication, and the DFT and cyclic convolution as used for FFT-based polynomial multiplication). Complex numbers are known as far as roots of unity and Gaussian integers, Turing machines are known with multiple tapes, and basic probability reaches the union bound. Tensor products, bilinear forms beyond the dot product, quotient rings and the sources' network and address constructions are not part of this background.

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Exact integer multiplication
- Discrete Fourier transform (also: normalized Fourier transform)
- Cyclic convolution
- Carry propagation
- Vector spaces, subspaces, bases and dimension (also: linear subspace, span, basis, linear independence, dimension of a vector space)
- Rank of a matrix (also: row rank, column rank, dimension of the column space)
- Invertible matrices and inverses (also: nonsingular matrix, matrix inverse, identity matrix, diagonal matrix)
- Gaussian elimination and triangular matrices (also: row reduction, elementary row operations, elementary matrix, lower triangular matrix, upper triangular matrix)
- Eigenvalues and diagonalization (also: eigenvector, eigendecomposition, characteristic polynomial, diagonalizable matrix)
- Dot product, orthogonal complement and projection (also: inner product, orthogonal projection, perpendicular subspace, orthogonal complement)
- Permutations and permutation matrices (also: permutation of coordinates, reordering of indices, permutation matrix)
- Modular arithmetic (also: congruence modulo q, residue classes, clock arithmetic, Z/qZ, residue ring)
- Greatest common divisor and coprimality (also: gcd, relatively prime, Euclid's algorithm, extended Euclidean algorithm, Bezout identity)
- Prime numbers (also: primes, odd prime, prime factorization)
- Chinese remainder theorem (also: CRT, Chinese remainder theorem for coprime moduli)
- Binary field GF(2) (also: F2, F_2, Z/2Z, XOR arithmetic, binary field)
- Hamming weight (also: popcount, number of ones, weight of a binary string, Hamming norm)
- Indicator vector of a set (also: characteristic vector, characteristic function, incidence vector, indicator function)
- Binomial coefficients (also: n choose k, binomial coefficient, number of k-element subsets)
- Positional and mixed-radix notation (also: radix representation, base-b expansion, mixed radix, mixed-radix digits, place value)
- Dyadic rationals (also: binary fractions, binary fixed-point numbers, dyadic numbers)
- Gaussian integers (also: Z[i], ring of Gaussian integers)
- Roots of unity (also: nth root of unity, primitive nth root of unity, complex roots of unity)
- Mathematical induction (also: induction, strong induction, proof by induction)
- Recurrence relations and geometric sums (also: recursion unrolling, divide-and-conquer recurrence, recursion tree, geometric series, geometric sum)
- Iterated logarithm (also: log star, log*, iterated log)
- Logarithms, floor and ceiling (also: lg, log base 2, log2, floor function, ceiling function)
- Union bound (also: Boole's inequality, sum of probabilities bound)
- Karatsuba multiplication (also: Karatsuba's algorithm, Karatsuba-Ofman multiplication, three-product splitting)

## Symbols bound on earlier pages

- $x$ (first input), bound on `exact-integer-multiplication`: A binary string of length n, the first factor of the product.
- $y$ (second input), bound on `exact-integer-multiplication`: A binary string of length n, the second factor of the product.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in the padded binary representation bin_k, that is, the length it pads to.
- $m$ (padded integer), bound on `exact-integer-multiplication`: The nonnegative integer, below 2^k, whose binary representation is taken.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)

## Page to audit (`radix-digit-convolution`)

````markdown
# Radix-digit convolution

Radix-digit convolution reduces [exact integer multiplication](exact-integer-multiplication.md) to a convolution of short integer coefficients, which fast convolution methods can evaluate. Splitting each input into radix digits turns the product into a convolution of short coefficients. (cited).

Fix a digit width $k$, the number of bits in one digit. The letter $k$ changes meaning here, from the padded length on the earlier page. Let $B = 2^k$ be the radix. Pad both inputs to $d$ digits, where $d$ is a count: the number of digit positions in each input. Here $x$ and $y$ denote the integers that the two input strings represent.

Let $x_j$ and $y_j$ be the $j$th digits of $x$ and $y$, each in $\{0,\dots,B-1\}$, where $j$ is a digit position running over $0,\dots,d-1$. Then
$$x=\sum_{j=0}^{d-1}x_jB^j,\qquad y=\sum_{j=0}^{d-1}y_jB^j.$$
Here $l$ is a second digit position running over $0,\dots,d-1$, and $m$ is a coefficient position running over $0,\dots,2d-2$; the letter $m$ changes meaning here. The product polynomial has coefficient $c_m$ at each position $m$, the convolution of the two digit sequences:
$$c_m=\sum_{j+l=m} x_j y_l,\qquad xy=\sum_m c_m B^m.$$

The convolution is the expensive part, and fast transform methods compute it. The coefficients are short: each term $x_j y_l$ is at most $(B-1)^2 < 2^{2k}$, and $c_m$ has at most $d$ terms, so $c_m < d\,2^{2k}$, about $2k + \lg d$ bits.

Carry propagation recovers the integer from the $c_m$. Take $k=2$, so $B=4$, with $x=11$ and $y=6$. The digits are $x_0=3$, $x_1=2$, $y_0=2$, $y_1=1$, giving $c_0=6$, $c_1=7$, $c_2=2$. From the lowest position, $6=1\cdot 4+2$ writes $2$ and carries $1$; $7+1=8=2\cdot 4$ writes $0$ and carries $2$; $2+2=4=1\cdot 4$ writes $0$ and carries $1$, which is the top digit. The digits $2,0,0,1$ give $66=11\cdot 6$.
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

Write the answer to `exegenius/tasks/0020-audit-radix-digit-convolution.answer.json`, then run `exegenius submit 0020-audit-radix-digit-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
