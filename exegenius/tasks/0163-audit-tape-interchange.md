# exegenius task 0163-audit-tape-interchange

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
- Linear network (also: fixed linear network, network, pointwise linear gate, wires, bank and forward invocation)
- Frame of a vertex (also: frame)
- Role streams from a cyclic row split (also: roles, wire streams)
- Subset-intersection finite network (also: three-element subset network, gather and scatter wires)
- Nested subspace labels
- Address shear (also: H + D shear, endpoint operator)
- Rank-saving recursion (also: recursive saving, recursive scheme, edge matrix)
- Gaussian dyadic numbers (also: Gaussian dyadics, Z[i,1/2] (Gaussian dyadic numbers))
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
- Source, sink and terminal of a network (also: terminal, source and sink of the network)

## Symbols bound on earlier pages

- $a$ (real part), bound on `gaussian-dyadic`: The real part of the Gaussian dyadic number $z$.
- $m$ (integer numerator), bound on `gaussian-dyadic`: The integer numerator of a dyadic rational written as $m/2^k$.
- $u$ (first input value), bound on `gaussian-dyadic`: The first value of an input pair to the butterfly map $H_0$.
- $x$ (first bank value), bound on `linear-network`: The value of the first bank, held on one wire.
- $y$ (second bank value), bound on `linear-network`: The value of the second bank, held on one wire.
- $W$ (number of roles), bound on `role-streams`: The number of roles, the fixed wire places of the network.
- $V$ (node volume), bound on `role-streams`: The number of bits the node holds once its rows are padded.
- $S$ (triple), bound on `subset-network`: A three-element subset of $[h]$, one element of $\mathcal T$.
- $X$ (first bank), bound on `subset-network`: The bank holding the scalar $x_S$ for each triple $S$.
- $Y$ (second bank), bound on `subset-network`: The bank holding the scalar $y_S$ for each triple $S$.
- $u$ (tail vertex), bound on `frame`: The vertex at which an edge starts, so that the frame change $D_vD_u^{-1}$ starts from its frame $D_u$.
- $s$ (route length), bound on `frame`: The number of edges in a route, so that the route has $s+1$ vertices.
- $H$ (first address field), bound on `address-shear`: The first address field, a vector whose entries lie in the residue ring Z/qZ.
- $D$ (second address field), bound on `address-shear`: The second address field, a vector whose entries lie in the residue ring Z/qZ, which the shear leaves unchanged.
- $m$ (space dimension), bound on `subspace-labels`: The dimension of the space E, which counts the basis vectors of E.
- $x$ (tail vertex), bound on `subspace-labels`: A vertex of the network, a gate or terminal; it is the tail of an edge from x to y.
- $y$ (head vertex), bound on `subspace-labels`: A vertex at the head of the edge from x, the vertex the edge enters.
- $s$ (smaller call count), bound on `subspace-labels`: The total number of smaller calls, which counts the smaller operations over all edges.
- $a$ (edge rank), bound on `recursive-saving`: The rank of one edge matrix, which is summed over all edges to give the total number of smaller calls.
- $s$ (smaller call count), bound on `recursive-saving`: The total number of smaller calls, counted as the sum of the edge ranks over all edges.

## Pages in the wiki

- [Fixed-tape machine model](fixed-tape-model.md)
- [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md)
- [Power saving in the logarithmic factor](power-saving.md)
- [Gaussian dyadic numbers](gaussian-dyadic.md)
- [Linear network](linear-network.md)
- [Role streams from a cyclic row split](role-streams.md)
- [Subset-intersection finite network](subset-network.md)
- [Established fast multiplier](multiplier-subroutine.md)
- [Source, sink and terminal of a network](network-terminal.md)
- [Frame of a vertex](frame.md)
- [Address shear](address-shear.md)
- [Nested subspace labels](subspace-labels.md)
- [Rank-saving recursion](recursive-saving.md)
- [Fast interchange of address chunks](tape-interchange.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Tensor product](tensor-product.md)
- [Multidimensional transform with power-of-two axes](multidim-transform.md)
- [Simultaneous butterfly layer H₀](butterfly-layer.md)
- [Order of an element](order-of-element.md)
- [Root of unity](roots-of-unity.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Signed coefficient packing](signed-packing.md)
- [Exact recovery by rounding and carries](exact-recovery.md)
- [Operator norm of a linear map](operator-norm.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein.md)
- [Quotient ring by several relations](quotient-ring.md)
- [Chinese-remainder axis map](crt-axis-map.md)
- [Fixed-tape integer multiplication with a power saving](fixed-tape-multiplication.md)

## Page to audit (`tape-interchange`)

````markdown
# Fast interchange of address chunks

Fast interchange of address chunks is a procedure that runs on a [Fixed-tape machine model](fixed-tape-model.md) and swaps two disjoint, equal-width address fields of an array. The multiplication algorithm uses it so that tape cost per unit of stored data is sublinear in the field width.

Let $H$ and $D$ be the two fields, each of $u$ bits, and let $V$ be the stored volume, the number of data units in the array. Here $u$ and $V$ are rebound. The exponent $\tau$ is a fixed number below 1 that sets the saving. The interchange costs $O(Vu^{\tau})$ (cited).

The interchange reduces to three updates, and the middle one is the [Address shear](address-shear.md), which replaces $H$ by $H+D$ and leaves $D$ fixed. The updates are $D\leftarrow D-H$, $H\leftarrow H+D$, $D\leftarrow H-D$, where $\leftarrow$ is assignment: the field on its left takes the value on its right. The outer two cost linear time.

The shear is carried by a bit network, a [Linear network](linear-network.md) whose wires each carry one bit. Each vertex holds a rational $m\times m$ matrix, where $m$ is its number of rows. An edge matrix, the head's matrix minus the tail's, of rank $a$ costs $a$ smaller calls, so $s$ is the sum of these ranks. Each smaller call acts on one of the $W$ [wire streams](role-streams.md), each of volume $V/W$. The paper's explicit network satisfies $s<Wm$ (cited).

The shear is computed by a [Rank-saving recursion](recursive-saving.md) on that network. Let $F_d$ be the time per unit volume of a width-$m^d$ interchange, where $d$ is the recursion depth. Width one ($d=0$) is a single-digit operation, so $F_0=O(1)$. At depth $d$, the $s$ smaller calls are interchanges of width $m^{d-1}$ on streams of volume $V/W$, which costs $(s/W)F_{d-1}$ per unit volume. Splitting, merging and gates are a fixed number of linear passes, $O(1)$ per unit volume. So $F_d\le\lambda F_{d-1}+O(1)$, with $\lambda=s/W$, and unrolling gives $F_d=O(1+\lambda+\cdots+\lambda^d)$.

The bound needs $\lambda<m^{\tau}$ for one fixed $\tau<1$, not merely $\lambda<m$. Write $\eta=(Wm-s)/(Wm)$, so $\lambda=m(1-\eta)$. For the explicit network the paper computes $\eta>20\cdot2^{-50}$ (cited) Take $\tau=1-2^{-50}$. Since $m<2^{20}$, $\ln m<20$, so $m^{-2^{-50}}=\exp(-2^{-50}\ln m)>1-20\cdot2^{-50}>1-\eta$, and hence $\lambda<m^{\tau}$. If $\lambda\le1$ the sum is at most $d+1$. If $\lambda>1$ it is $O(\lambda^d)$, and $\lambda^d<m^{d\tau}$. As $m\ge2$, $F_d=O(m^{d\tau})$, which for width $u=m^d$ is $O(u^{\tau})$ per unit volume.

For any initial auxiliary values, a forward invocation from $X$ to $Y$ adds $x_S$ into $y_S$ and changes no other value (cited). The shear is such an invocation, with $D$ as $X$ and $H$ as $Y$, so it is exact for any initial auxiliary contents. A forward, inverse, forward schedule of these invocations exchanges the two banks and returns every auxiliary wire to its starting value (cited).
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

Write the answer to `exegenius/tasks/0163-audit-tape-interchange.answer.json`, then run `exegenius submit 0163-audit-tape-interchange` in the project directory. If submit rejects the answer, fix the answer and submit again.
