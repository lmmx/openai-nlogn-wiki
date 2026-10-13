# exegenius task 0114-audit-crt-axis-map

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
- Linear network (also: fixed linear network, network, pointwise linear gate, wires)
- Frame of a vertex (also: frame)
- Role streams from a cyclic row split (also: roles)
- Subset-intersection finite network (also: three-element subset network, gather and scatter wires)
- Nested subspace labels
- Address shear (also: H + D shear, endpoint operator)
- Rank-saving recursion (also: recursive saving, recursive scheme, edge matrix)
- Fast interchange of address chunks (also: chunk interchange, address chunks, linear-cost address update, address fields, address field)
- Gaussian dyadic numbers (also: Gaussian dyadics, Z[i,1/2] (Gaussian dyadic numbers))
- Simultaneous butterfly layer H₀ (also: H_0 layer)
- Polynomial ring modulo yʳ + 1 (also: C[y]/(y^r+1))
  - $y$ (polynomial variable): The formal variable whose powers act as roots of unity on the remaining axes.
  - $r$ (coefficient count): The number of complex coefficients in each polynomial record, which is a power of two.
- Root of unity (also: primitive root of unity)
- Synthetic polynomial transform (also: synthetic transform, polynomial transform, twiddle multiplication)
- Discrete Fourier transform (also: Fourier transform, twiddle step)
- Multidimensional transform with power-of-two axes (also: power-of-two tensor transform)
- Gaussian resampling (also: Gaussian gridding, target permutation)
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
- Directed graph (also: digraph, vertex, edge, head and tail, directed acyclic graph, DAG, node)
- Vector space, subspace, basis and dimension (also: linear space, subspace, span, linearly independent, basis, direct sum, dimension)
- Linear map and matrix (also: linear transformation, matrix, invertible matrix, nonsingular matrix, transpose, identity matrix, diagonal matrix)
- Matrix rank (also: column rank, row rank, rational rank, rank over a field)
- Gaussian elimination and triangular matrices (also: row reduction, elementary row operations, echelon form, lower triangular matrix, upper triangular matrix)
- Dot product and orthogonal complement (also: standard inner product, scalar product, orthogonal complement, perpendicular space, U perp)
- Vector norm and maximum norm (also: norm, maximum norm, sup norm, infinity norm, max norm, triangle inequality)
- Complex conjugate, modulus and polar form (also: conjugate, modulus, absolute value of a complex number, argument, unit circle, Euler's formula, polar form)
- Tensor product

## Symbols bound on earlier pages

- $a$ (real part), bound on `gaussian-dyadic`: The real part of the Gaussian dyadic number $z$, a dyadic rational.
- $b$ (imaginary part), bound on `gaussian-dyadic`: The imaginary part of the Gaussian dyadic number $z$, a dyadic rational.
- $k$ (denominator exponent), bound on `gaussian-dyadic`: The non-negative integer exponent such that $2^k$ is the denominator of a dyadic rational $m/2^k$.
- $x$ (first bank value), bound on `linear-network`: The value of the first bank, held on one wire in the example.
- $i$ (row index), bound on `role-streams`: The position of a row among the rows that share its prefix, counted from 0.
- $i$ (input index), bound on `frame`: The index of an input array of a pointwise linear gate, running from 1 to t.
- $S$ (triple), bound on `subset-network`: A three-element subset of $[h]$ in $\mathcal T$, which indexes one bank-X scalar and one bank-Y scalar.
- $x$ (vertex), bound on `subspace-labels`: A vertex of the network, which is a gate or terminal.
- $s$ (smaller call count), bound on `subspace-labels`: The total number of smaller calls, which is the sum of the drops over all edges.
- $a$ (edge rank), bound on `recursive-saving`: The rank of an edge matrix, which counts the smaller calls that edge costs.
- $s$ (smaller call count), bound on `recursive-saving`: The total number of smaller calls over all roles, which is the count the recursion's cost is measured by.
- $d$ (recursion depth), bound on `tape-interchange`: The number of levels of recursion below the top call, so that the width is $m^d$.
- $x$ (formal variable), bound on `signed-packing`: The formal variable in which the polynomial $A(x)$ is written.
- $i$ (coefficient index), bound on `signed-packing`: The index of a coefficient, running from $0$ to $m-1$.
- $b$ (slot width), bound on `signed-packing`: The number of bits in each slot, which holds one coefficient.
- $a_i$ (coefficient), bound on `signed-packing`: The integer coefficient of $x^i$ in $A(x)$.
- $S$ (linear map on E), bound on `tensor-product`: A linear map of E, the factor that S acts on in the tensor product.
- $d$ (chunk count), bound on `butterfly-layer`: The number of equal-width address chunks on which the layer acts, each with one selected bit.
- $x$ (formal variable), bound on `cyclic-convolution`: A formal variable, the symbol whose powers mark the positions of the coefficients of a list.
- $S$ (list length), bound on `cyclic-convolution`: The number of coefficients in each list, which counts the coefficient positions and sets the wraparound modulus.
- $i$ (first index), bound on `cyclic-convolution`: An index of the first list's coefficients, running over $\{0,\dots,S-1\}$.
- $j$ (second index), bound on `cyclic-convolution`: An index of the second list's coefficients, running over $\{0,\dots,S-1\}$.
- $k$ (output index), bound on `cyclic-convolution`: An index of the cyclic product's coefficients, running over $\{0,\dots,S-1\}$.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each radix digit.
- $k$ (transform index), bound on `fourier-transform`: The index of an entry of the transform $\hat u$, running from $0$ to $q-1$.
- $j$ (input index), bound on `fourier-transform`: The index of an entry of $u$, running from $0$ to $q-1$.
- $d$ (number of axes), bound on `multidim-transform`: The number of axes of the array, which counts the coordinates it is indexed by.
- $j$ (input index), bound on `multidim-transform`: The index along an axis of the input array, $j_\ell$ being the index along axis $\ell$.
- $k$ (output index), bound on `multidim-transform`: The index along an axis of the transformed array, $k_\ell$ being the index along axis $\ell$.
- $a_i$ (ring coefficient), bound on `polynomial-ring`: The i-th complex coefficient of an element of the ring, the coefficient of y^i.
- $i$ (coefficient index), bound on `polynomial-ring`: The index of a coefficient of a ring element, running from 0 to r-1.
- $k$ (shift amount), bound on `polynomial-ring`: The number of places each coefficient moves when the element is multiplied by y^k.
- $j$ (twiddle exponent), bound on `synthetic-transform`: The exponent of a twiddle factor $y^j$, an integer ranging over $0,\dots,2r-1$.
- $s$ (source length), bound on `gaussian-resampling`: The length of the source transform, the number of coordinates it acts on.
- $C$ (selection map), bound on `gaussian-resampling`: The map from length $t$ to length $s$ that selects the coordinates $v_{q_j}$.

## Pages in the wiki

- [Fixed-tape machine model](fixed-tape-model.md)
- [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Power saving in the logarithmic factor](power-saving.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Linear network](linear-network.md)
- [Role streams from a cyclic row split](role-streams.md)
- [Frame of a vertex](frame.md)
- [Address shear](address-shear.md)
- [Subset-intersection finite network](subset-network.md)
- [Nested subspace labels](subspace-labels.md)
- [Rank-saving recursion](recursive-saving.md)
- [Fast interchange of address chunks](tape-interchange.md)
- [Signed coefficient packing](signed-packing.md)
- [Established fast multiplier](multiplier-subroutine.md)
- [Tensor product](tensor-product.md)
- [Simultaneous butterfly layer H₀](butterfly-layer.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Multidimensional transform with power-of-two axes](multidim-transform.md)
- [Root of unity](roots-of-unity.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md)

## Page to audit (`crt-axis-map`)

````markdown
# Chinese-remainder axis map

The Chinese-remainder axis map is a bijection that places the coefficients of a [cyclic convolution](cyclic-convolution.md) on the axes of a product of cyclic rings, so that the convolution becomes multidimensional.

Let $d$ be the number of axes and $s_i$ the length of axis $i$, with $s_1,\ldots,s_d$ pairwise coprime. Let $S=s_1\cdots s_d$ be the number of coefficients, and let $x$ be the variable of $\mathbb C[x]/(x^S-1)$.

Let $P_i=s_1\cdots s_{i-1}$, so $P_1=1$. Since $P_i$ is coprime to $s_i$, it has an inverse $\mu_i$ modulo $s_i$, so $\mu_iP_i\equiv1\pmod{s_i}$.

Let $x_i$ be the variable of axis $i$, and let $\Phi$ be the algebra map (a function respecting sums, products and complex scalars) with $\Phi(x)=\prod_i x_i^{\mu_i}$, from $\mathbb C[x]/(x^S-1)$ to $\mathbb C[x_1,\ldots,x_d]/(x_1^{s_1}-1,\ldots,x_d^{s_d}-1)$. Since each $s_i$ divides $S$, $\Phi(x)^S=1$ in the target, so $\Phi$ is well defined.

For $0\le k<S$, let $b_i$ be the exponent of $x_i$ in $\Phi(x^k)$, reduced so that $0\le b_i<s_i$; then $b_i\equiv\mu_ik\pmod{s_i}$. If $k$ and $k'$ give the same $b_i$ for every $i$, each $s_i$ divides $k-k'$. By the Chinese remainder theorem, which says that congruences with pairwise coprime moduli combine into one modulo their product, $S$ divides $k-k'$, so $k=k'$. Hence the powers $\Phi(x)^0,\ldots,\Phi(x)^{S-1}$ reach each of the $S$ target monomials once. So $\Phi$ is an isomorphism: a bijective algebra map whose inverse is also one.

Because $\Phi$ is an isomorphism, it preserves [cyclic convolution](cyclic-convolution.md): the product of two lists in the source maps to the product of their images. In the target, multiplying monomials adds exponents on each axis modulo $s_i$, so the convolution becomes a $d$-dimensional cyclic convolution.

Let $k$ be a coefficient index with $0\le k<S$. Its mixed-radix expansion $k=\sum_{j=1}^d a_jP_j$, with $0\le a_j<s_j$, is unique, and $a_j$ is the digit of $k$ on axis $j$. Then $b_i\equiv a_i+\mu_i\sum_{j<i}a_jP_j\pmod{s_i}$, because $\mu_ik=\sum_j\mu_ia_jP_j$, terms with $j>i$ are multiples of $s_i$, and $\mu_iP_i\equiv1\pmod{s_i}$.

So for fixed earlier digits, the map sends $a_i$ to $b_i$ by a cyclic shift of axis $i$ by $\mu_i\sum_{j<i}a_jP_j$, an amount controlled by earlier axes. Applying these controlled cyclic shifts from axis $d$ down to axis $1$ reorders the coefficients.

Take $S=6$, $s_1=2$, $s_2=3$. Then $\mu_1=1$, $\mu_2=2$, so $\Phi(x)=x_1x_2^2$. For $k=3=1+1\cdot2$, the digits are $a_1=1$ and $a_2=1$, giving $b_1=1$ and $b_2\equiv0\pmod 3$. Directly, $(x_1x_2^2)^3=x_1$ in the target ring.

This is the Chinese-remainder split of Agarwal and Cooley (cited).
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

Write the answer to `exegenius/tasks/0114-audit-crt-axis-map.answer.json`, then run `exegenius submit 0114-audit-crt-axis-map` in the project directory. If submit rejects the answer, fix the answer and submit again.
