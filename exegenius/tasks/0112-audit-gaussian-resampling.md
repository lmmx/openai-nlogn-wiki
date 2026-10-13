# exegenius task 0112-audit-gaussian-resampling

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
- Cyclic convolution (also: convolution modulo x^S - 1)
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
- $m$ (numerator), bound on `gaussian-dyadic`: The integer numerator of a dyadic rational $m/2^k$.
- $k$ (denominator exponent), bound on `gaussian-dyadic`: The non-negative integer exponent such that $2^k$ is the denominator of a dyadic rational $m/2^k$.
- $u$ (first input), bound on `gaussian-dyadic`: A Gaussian dyadic number used as the first input of the butterfly $H_0$.
- $v$ (second input), bound on `gaussian-dyadic`: A Gaussian dyadic number used as the second input of the butterfly $H_0$.
- $i$ (row index), bound on `role-streams`: The position of a row among the rows that share its prefix, counted from 0.
- $R$ (padded row count), bound on `role-streams`: The number of rows of one prefix after padding, a multiple of W.
- $u$ (edge tail vertex), bound on `frame`: A vertex at the tail of an edge, where the edge goes from u to v.
- $v$ (edge head vertex), bound on `frame`: A vertex at the head of an edge, where the edge goes from u to v.
- $t$ (gate input count), bound on `frame`: The number of input arrays of a pointwise linear gate.
- $i$ (input index), bound on `frame`: The index of an input array of a pointwise linear gate, running from 1 to t.
- $q$ (modulus), bound on `address-shear`: The fixed modulus q of the residue ring Z/qZ in which the entries of H and D lie.
- $T$ (triple), bound on `subset-network`: A three-element subset of $[h]$ in the family $\mathcal T$, used as an index of scalars.
- $E$ (fixed label space), bound on `subspace-labels`: The fixed space in which every label lies, a space of dimension m.
- $m$ (label space dimension), bound on `subspace-labels`: The dimension of E, the number of independent directions in E.
- $L$ (label), bound on `subspace-labels`: The label L(x), a subspace of E attached to the vertex x.
- $q$ (address field width), bound on `subspace-labels`: The number of bits in each of the two equal address fields being interchanged.
- $s$ (smaller call count), bound on `subspace-labels`: The total number of smaller calls, which is the sum of the drops over all edges.
- $a$ (edge rank), bound on `recursive-saving`: The rank of an edge matrix, which counts the smaller calls that edge costs.
- $s$ (smaller call count), bound on `recursive-saving`: The total number of smaller calls over all roles, which is the count the recursion's cost is measured by.
- $u$ (field width), bound on `tape-interchange`: The common width of the two address fields, the number of bits in each.
- $i$ (coefficient index), bound on `signed-packing`: The index of a coefficient, running from $0$ to $m-1$.
- $m$ (coefficient count), bound on `signed-packing`: The number of coefficients of $A$.
- $E$ (first vector space), bound on `tensor-product`: The first vector space, the first factor of the tensor product.
- $F$ (second vector space), bound on `tensor-product`: The second vector space, the second factor of the tensor product.
- $q$ (dimension of F), bound on `tensor-product`: The number of basis vectors of F, so F has dimension q.
- $T$ (linear map on F), bound on `tensor-product`: A linear map of F, the factor that T acts on in the tensor product.
- $i$ (first index), bound on `cyclic-convolution`: An index of the first list's coefficients, running over $\{0,\dots,S-1\}$.
- $j$ (second index), bound on `cyclic-convolution`: An index of the second list's coefficients, running over $\{0,\dots,S-1\}$.
- $k$ (output index), bound on `cyclic-convolution`: An index of the cyclic product's coefficients, running over $\{0,\dots,S-1\}$.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of radix digits in each input, $\lceil n/b \rceil$.
- $t$ (formal variable), bound on `radix-digit-convolution`: A formal variable whose powers mark the coefficient positions of the digit polynomials.
- $u$ (input vector), bound on `fourier-transform`: The complex vector $u=(u_0,\dots,u_{q-1})$ whose transform is taken.
- $q$ (vector length), bound on `fourier-transform`: The length of $u$, which counts the entries of $u$ and of its transform.
- $k$ (transform index), bound on `fourier-transform`: The index of an entry of the transform $\hat u$, running from $0$ to $q-1$.
- $j$ (input index), bound on `fourier-transform`: The index of an entry of $u$, running from $0$ to $q-1$.
- $\alpha$ (even-entry transform), bound on `fourier-transform`: The normalized transform, of length $q/2$, of the even-indexed entries of $u$.
- $\beta$ (odd-entry transform), bound on `fourier-transform`: The normalized transform, of length $q/2$, of the odd-indexed entries of $u$.
- $T$ (operation count), bound on `fourier-transform`: The number of operations the transform takes on a vector of length $q$.
- $j$ (input index), bound on `multidim-transform`: The index along an axis of the input array, $j_\ell$ being the index along axis $\ell$.
- $k$ (output index), bound on `multidim-transform`: The index along an axis of the transformed array, $k_\ell$ being the index along axis $\ell$.
- $i$ (coefficient index), bound on `polynomial-ring`: The index of a coefficient of a ring element, running from 0 to r-1.
- $k$ (shift amount), bound on `polynomial-ring`: The number of places each coefficient moves when the element is multiplied by y^k.
- $j$ (twiddle exponent), bound on `synthetic-transform`: The exponent of a twiddle factor $y^j$, an integer ranging over $0,\dots,2r-1$.

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

## Page to audit (`gaussian-resampling`)

````markdown
# Gaussian resampling

Gaussian resampling rewrites a Fourier transform of length $s$, the number of its coordinates, as a transform with target length $t>s$ and power-of-two axis lengths, keeping the source and target coordinate permutations inside the identity. It is needed because the integer product's transform lengths are pairwise coprime, while the synthetic transforms use powers of two. (cited)

Gaussian resampling rewrites each [Discrete Fourier transform](fourier-transform.md) of length $s$ as follows. Let $F_q$ be the normalized transform of length $q$, $(F_q u)_k=\frac1q\sum_{j=0}^{q-1}u_j e^{-2\pi i jk/q}$.

Let $\alpha\ge2$ be a fixed integer, the Gaussian width.

$P_s$ and $P_t$ are the maps $(P_su)_j=u_{tj}$ and $(P_tv)_k=v_{-sk}$, where $u$ has length $s$, $v$ has length $t$ (here $v$ is new, not its earlier meaning), and indices are taken modulo $s$ and $t$. With $\gcd(s,t)=1$, both only rearrange coordinates.

A linear map $L$ is a *contraction* if $\|Lu\|\le\|u\|$ for every $u$, where $\|u\|$ is the largest modulus of an entry of $u$.

$G$ is the map whose $k$-th output is a Gaussian-weighted sum centred at $sk/t$, and $T$ weights each input $u_j$ by a Gaussian centred at $tj/s$:
$$(Gu)_k=\frac1\alpha\sum_{j\in\mathbb Z}e^{-\pi\alpha^{-2}(j-sk/t)^2}u_j,\qquad (Tu)_k=\sum_{j\in\mathbb Z}e^{-\pi\alpha^{2}(tj/s-k)^2}u_j,$$
with $u_j$ read modulo $s$. Harvey and van der Hoeven prove the exact identity $TP_sF_s=P_tF_tG$ (their Theorem 4.2), but $T$ is not square, so we build a left inverse.

Let $E$ multiply entry $j$ by $e^{\pi\alpha^2\beta_j^2}$, where $q_j=\lfloor tj/s+\tfrac12\rfloor$ is the integer nearest $tj/s$ (ties rounded up) and $\beta_j=tj/s-q_j$, so $|\beta_j|\le\tfrac12$. Let $C$ map $\mathbb C^t$ to $\mathbb C^s$ by $(Cv)_j=v_{q_j}$, and let $N=CTE$, a map from $\mathbb C^s$ to itself.

In $(Nu)_j$ the term with index $j$ is exactly $u_j$, since $E$ cancels the Gaussian factor at $q_j$. The Neumann series $\sum_{m\ge0}(I-N)^m$, where $I$ is the identity map, converges to $N^{-1}$ when $\|I-N\|<\tfrac12$, so $\|N^{-1}\|\le2$. The other terms are small: $\|I-N\|<2^{-\alpha^2(t/s-1)}<\tfrac12$ under the sources' hypotheses.

Since $CT=NE^{-1}$, we have $EN^{-1}CT=I$, so multiplying the identity by $EN^{-1}C$ on the left gives $P_sF_s=EN^{-1}CP_tF_tG$. Let $R=\tfrac12G$ and $Q=2^{1-2\alpha^2}EN^{-1}C$, with $R$ mapping $\mathbb C^s$ to $\mathbb C^t$ and $Q$ mapping back. Then $P_sF_s=2^{2\alpha^2}QP_tF_tR$: the factor $2^{2\alpha^2}$ undoes the constants in $R$ and $Q$.

Both are contractions. $\|R\|<\tfrac34$ by the bound in Harvey and van der Hoeven's Proposition 4.7(i), and $\|Q\|\le1$, since $\|C\|\le1$, $\|N^{-1}\|\le2$ and $\|E\|\le e^{\pi\alpha^2/4}\le2^{2\alpha^2-2}$ for $\alpha\ge2$.

The usual implementation sorts coordinates twice. (cited)

In the application $t=2^a$ is a power of two, so $F_t$ has power-of-two length. Thus Gaussian resampling expresses each source transform through a [Multidimensional transform with power-of-two axes](multidim-transform.md).
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

Write the answer to `exegenius/tasks/0112-audit-gaussian-resampling.answer.json`, then run `exegenius submit 0112-audit-gaussian-resampling` in the project directory. If submit rejects the answer, fix the answer and submit again.
