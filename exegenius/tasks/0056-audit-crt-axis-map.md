# exegenius task 0056-audit-crt-axis-map

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

Terms and steps: report what would stop this reader at this point on the page. A term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. A claim marked "(cited)" is attributed to the source. A citation lets the reader check a result, not follow an argument: a cited result the page uses is followable if the page says what it states and why it applies where it is used, and its proof can be left to the source. A cited claim that stands in for how the page's own concept works, or whose content or role the page does not say, is a step.
- term: a named concept the reader does not know, which the page neither explains nor links. References to the documents themselves (the paper, the sources, the target result) are not terms.
- step: an inference, calculation or claim that the page presents as following from what it gives, which the reader cannot check from what the page gives. A claim about an identity, construction or definition that the page never states is a step.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

For these sources: The reader is an undergraduate computer scientist who has studied discrete mathematics (integers, modular arithmetic, gcd and primes at the basic level, sets, bijections, binomial coefficients), undergraduate linear algebra (vector spaces, matrices, rank, Gaussian elimination, dot products, norms), the single-variable calculus a CS degree requires (limits, convergence of sequences and series, basic integrals, logarithms and exponentials), algorithms and complexity (big-O together with Omega and Theta, recurrences, schoolbook multiplication, worst-case running time of Turing machines), and binary arithmetic with basic complex numbers. This covers the sources' integer, bit, linear-algebra, limit and asymptotic bookkeeping, but not prime-number density results, tensor products, operator norms and contractions, Gaussian integers, or the quotient-ring and Fourier machinery beyond the existing concepts.

## Known concepts

- Big-O notation (also: O(n))
- Polynomials
- Complex numbers (also: Gaussian integers)
- Multitape Turing machine
- Fixed-tape machine model (also: fixed finite-tape model)
- Schonhage-Strassen optimality conjecture (also: n log n optimality conjecture)
- Power saving in the logarithmic factor (also: (lg n)^(1-kappa) saving)
- Linear network (also: fixed linear network)
- Frame of a vertex (also: frame)
- Role streams from a cyclic row split (also: roles)
- Subset-intersection finite network (also: three-element subset network)
- Nested subspace labels
- Address shear (also: H + D shear)
- Rank-saving recursion (also: recursive saving)
- Fast interchange of address chunks (also: chunk interchange)
- Gaussian dyadic numbers (also: Gaussian dyadics)
- Simultaneous butterfly layer H₀ (also: H_0 layer)
- Polynomial ring modulo yʳ + 1 (also: C[y]/(y^r+1))
  - $y$ (polynomial variable): The formal variable whose powers act as roots of unity on the remaining axes.
  - $r$ (coefficient count): The number of complex coefficients in each polynomial record, which is a power of two.
- Root of unity (also: primitive root of unity)
- Synthetic polynomial transform (also: synthetic transform, polynomial transform)
- Discrete Fourier transform (also: Fourier transform)
- Multidimensional transform with power-of-two axes (also: power-of-two tensor transform)
- Gaussian resampling (also: Gaussian gridding)
- Cyclic convolution (also: convolution modulo x^S - 1)
- Bluestein's chirp identity (also: chirp identity)
- Radix-digit convolution (also: radix-2^b digit polynomials)
- Signed coefficient packing (also: Kronecker substitution)
- Established fast multiplier (also: Harvey-van der Hoeven multiplier)
- Modular arithmetic (also: congruence, residue classes, integers modulo m, Z/mZ, modular inverse, division with remainder)
- Greatest common divisor and coprimality (also: gcd, relatively prime, pairwise coprime, Euclidean algorithm)
- Prime number (also: prime, primality, prime factorization)
- Binary field and exclusive or (also: F_2, GF(2), Z/2Z, XOR, exclusive or, bitwise XOR)
- Hamming weight (also: weight, popcount, number of ones)
- Two's-complement representation (also: two's complement, signed binary integer, signed fixed-width integer)
- Positional notation and binary representation (also: radix representation, base-b digits, binary representation, binary expansion, carries)
- Dyadic rational (also: dyadic fraction, binary fraction, finite binary expansion, power-of-two denominator)
- Floor and ceiling functions (also: integer part, round down, round up, floor, ceiling)
- Binomial coefficient (also: n choose k, binomial, binom(n,k))
- Finite sets, subsets and intersections (also: subset, intersection, intersection size, indicator vector, characteristic vector, k-element subset)
- Bijection and permutation (also: one-to-one correspondence, bijective function, permutation map, permutation of a set)
- Cartesian product (also: product set, direct product, product of index sets)
- Lexicographic order (also: lex order, dictionary order, row-major order)
- Logarithm and exponential function (also: lg, log base 2, natural logarithm, ln, exp, e^x)
- Limits (also: limit of a sequence, limit of a function, lim, tends to, approaches)
- Convergence of sequences and series (also: convergent sequence, convergent series, divergence, partial sums, sum of an infinite series, convergence)
- Basic integrals (also: definite integral, indefinite integral, antiderivative, Riemann integral, fundamental theorem of calculus, integration by substitution)
- Geometric series (also: geometric sum, sum of powers)
- Big-Omega, big-Theta and little-o notation (also: Omega notation, Theta notation, o-notation, asymptotic lower bound, tight bound, asymptotic equivalence)
- Worst-case running time of a Turing machine (also: time complexity, step count, worst-case time, running time)
- Recurrence relation (also: recurrence, divide-and-conquer recurrence, unrolling, T(n) recurrence)
- Schoolbook multiplication (also: grade-school multiplication, long multiplication, naive multiplication)
- Directed graph (also: digraph, vertex, edge, head and tail, directed acyclic graph, DAG)
- Vector space, subspace, basis and dimension (also: linear space, subspace, span, linearly independent, basis, direct sum, dimension)
- Linear map and matrix (also: linear transformation, matrix, invertible matrix, nonsingular matrix, transpose, identity matrix, diagonal matrix)
- Matrix rank (also: column rank, row rank, rational rank, rank over a field)
- Gaussian elimination and triangular matrices (also: row reduction, elementary row operations, echelon form, lower triangular matrix, upper triangular matrix)
- Dot product and orthogonal complement (also: standard inner product, scalar product, orthogonal complement, perpendicular space, U perp)
- Vector norm and maximum norm (also: norm, maximum norm, sup norm, infinity norm, max norm, triangle inequality)
- Complex conjugate, modulus and polar form (also: conjugate, modulus, absolute value of a complex number, argument, unit circle, Euler's formula, polar form)

## Symbols bound on earlier pages

- $j$ (input index), bound on `fourier-transform`: The index running over the entries of $u$, from $0$ to $q-1$.
- $k$ (output index), bound on `fourier-transform`: The index running over the entries of the transform, from $0$ to $q-1$.
- $d$ (number of axes), bound on `multidim-transform`: The number of axes of the array, which is the number of coordinates it is indexed by.
- $a_i$ (coefficient), bound on `polynomial-ring`: The i-th entry of a coefficient list, the coefficient of y^i in the polynomial.
- $a$ (real part), bound on `gaussian-dyadic`: The real part of $z$, a dyadic rational.
- $b$ (imaginary part), bound on `gaussian-dyadic`: The imaginary part of $z$, a dyadic rational.
- $k$ (denominator exponent), bound on `gaussian-dyadic`: The nonnegative integer exponent $k$ such that the denominator of a dyadic rational is $2^k$.
- $a$ (first bank value), bound on `linear-network`: The value of the first bank, held on one wire.
- $b$ (second bank value), bound on `linear-network`: The value of the second bank, held on one wire.
- $d$ (chunk bound), bound on `butterfly-layer`: An upper bound on the number of equal-width address chunks in a layer.
- $x$ (vertex), bound on `subspace-labels`: A gate or terminal of the network, at the tail of an edge.
- $a$ (edge matrix rank), bound on `recursive-saving`: The rank of an edge matrix, which counts the smaller calls that edge costs.
- $s$ (smaller call total), bound on `recursive-saving`: The total number of smaller calls summed over all roles.
- $s$ (source length), bound on `gaussian-resampling`: The length of the source transform, which is the number of coordinates it acts on.
- $x$ (formal variable), bound on `signed-packing`: The formal variable of the polynomial A, whose powers mark the coefficient positions.
- $b$ (slot width), bound on `signed-packing`: The number of bits in each slot, the bit spacing between consecutive coefficients of the packed integer.
- $a_i$ (coefficient), bound on `signed-packing`: The i-th integer coefficient of A, bounded in absolute value by 2^(b-1).
- $x$ (formal variable), bound on `cyclic-convolution`: A formal variable whose powers are the monomials of the polynomials being multiplied.
- $S$ (list length), bound on `cyclic-convolution`: The number of coefficients in each list, which is also the modulus of the exponent wraparound.
- $a$ (first coefficient list), bound on `cyclic-convolution`: The first input list, whose entries are the coefficients $a_0,\dots,a_{S-1}$ of $a(x)$.
- $b$ (second coefficient list), bound on `cyclic-convolution`: The second input list, whose entries are the coefficients $b_0,\dots,b_{S-1}$ of $b(x)$.
- $k$ (output position), bound on `cyclic-convolution`: An index of an output coefficient, ranging over $0,\dots,S-1$.
- $i$ (first input index), bound on `cyclic-convolution`: An index of a coefficient of the first list, ranging over $0,\dots,S-1$.
- $j$ (second input index), bound on `cyclic-convolution`: An index of a coefficient of the second list, ranging over $0,\dots,S-1$.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each radix digit.
- $j$ (input index), bound on `bluestein`: An index from $0$ to $q-1$ labelling the entries of the input vector.
- $k$ (output index), bound on `bluestein`: An index from $0$ to $q-1$ labelling the entries of the transform.

## Pages in the wiki

- [Fixed-tape machine model](fixed-tape-model.md)
- [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Power saving in the logarithmic factor](power-saving.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Multidimensional transform with power-of-two axes](multidim-transform.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Root of unity](roots-of-unity.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Linear network](linear-network.md)
- [Role streams from a cyclic row split](role-streams.md)
- [Frame of a vertex](frame.md)
- [Simultaneous butterfly layer H₀](butterfly-layer.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Address shear](address-shear.md)
- [Subset-intersection finite network](subset-network.md)
- [Nested subspace labels](subspace-labels.md)
- [Rank-saving recursion](recursive-saving.md)
- [Fast interchange of address chunks](tape-interchange.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Signed coefficient packing](signed-packing.md)
- [Established fast multiplier](multiplier-subroutine.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Bluestein's chirp identity](bluestein.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md)

## Page to audit (`crt-axis-map`)

````markdown
# Chinese-remainder axis map

The Chinese-remainder axis map is a bijection that places the coefficients of a [cyclic convolution](cyclic-convolution.md) on the axes of a product of cyclic rings, so that the convolution becomes multidimensional. The radix-digit coefficient list is laid out this way, with each axis of distinct prime length.

Let $d$ be the number of axes. Let $s_i$ be the length of axis $i$, a count of positions on that axis, and assume $s_1,\ldots,s_d$ are pairwise coprime. Let $S=s_1s_2\cdots s_d$ be the total number of coefficients. Let $x$ be the variable of the ring $\mathbb C[x]/(x^S-1)$.

Let $P_i=s_1\cdots s_{i-1}$ be the product of the lengths before axis $i$, with $P_1=1$. Let $\mu_i$ be the inverse of $P_i$ modulo $s_i$, so that $\mu_iP_i\equiv1\pmod{s_i}$; it exists because $P_i$ is coprime to $s_i$.

Let $\Phi$ be the algebra map sending $x$ to $\prod_i x_i^{\mu_i}$. It maps $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1)$. Since each $\mu_i$ is a unit modulo $s_i$, the Chinese remainder theorem makes the exponents of $\Phi(x)^0,\ldots,\Phi(x)^{S-1}$ pairwise distinct, so these powers run through all $S$ target monomials once. Hence $\Phi$ is an isomorphism. The map $\Phi$ is an isomorphism that preserves [cyclic convolution](cyclic-convolution.md), so a product of two lists is computed axis by axis.

Let $k$ be a coefficient index with $0\le k<S$. It has a unique mixed-radix expansion $k=\sum_{j=1}^d a_jP_j$ with $0\le a_j<s_j$, and $a_j$ is the mixed-radix digit of $k$ on axis $j$. Let $b_i$ be the exponent of $x_i$ in $\Phi(x^k)$, reduced so that $0\le b_i<s_i$. Then $b_i\equiv a_i+\mu_i\sum_{j<i}a_jP_j \pmod{s_i}$. This follows from $\mu_ik=\sum_j\mu_ia_jP_j$: terms with $j>i$ are multiples of $s_i$, and $\mu_iP_i\equiv1\pmod{s_i}$.

Take $S=6$, $s_1=2$, $s_2=3$. Then $P_1=1$, $P_2=2$, $\mu_1=1$, $\mu_2=2$, so $\Phi(x)=x_1x_2^2$. For $k=3=1+1\cdot2$, the digits are $a_1=1$ and $a_2=1$, giving $b_1=1$ and $b_2\equiv1+2\cdot1\equiv0\pmod 3$. Directly, $(x_1x_2^2)^3=x_1^3x_2^6=x_1$ in the target ring.

This is the Chinese-remainder split of Agarwal and Cooley (cited). Its point is that reordering the coefficients becomes a sequence of controlled cyclic shifts on the axes.
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

Write the answer to `exegenius/tasks/0056-audit-crt-axis-map.answer.json`, then run `exegenius submit 0056-audit-crt-axis-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
