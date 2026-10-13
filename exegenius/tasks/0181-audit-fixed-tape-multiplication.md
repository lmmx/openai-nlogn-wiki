# exegenius task 0181-audit-fixed-tape-multiplication

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
- Fast interchange of address chunks (also: chunk interchange, address chunks, linear-cost address update, address fields, address field, bit procedure)
- Gaussian dyadic numbers (also: Gaussian dyadics, Z[i,1/2] (Gaussian dyadic numbers))
- Simultaneous butterfly layer H₀ (also: H_0 layer)
- Polynomial ring modulo yʳ + 1 (also: C[y]/(y^r+1), reduced polynomial)
  - $y$ (polynomial variable): The formal variable whose powers act as roots of unity on the remaining axes.
  - $r$ (coefficient count): The number of complex coefficients in each polynomial record, which is a power of two.
- Root of unity (also: primitive root of unity)
- Synthetic polynomial transform (also: synthetic transform, polynomial transform, twiddle multiplication, transform method)
- Discrete Fourier transform (also: Fourier transform, twiddle step)
- Multidimensional transform with power-of-two axes (also: power-of-two tensor transform)
- Gaussian resampling (also: Gaussian gridding, target permutation)
- Cyclic convolution (also: convolution modulo x^S - 1, normalized cyclic convolution)
- Bluestein's chirp identity (also: chirp identity)
- Chinese-remainder axis map (also: Chinese-remainder address map)
- Radix-digit convolution (also: radix-2^b digit polynomials)
- Signed coefficient packing (also: Kronecker substitution)
- Established fast multiplier (also: Harvey-van der Hoeven multiplier)
- Exact recovery by rounding and carries (also: carry propagation)
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
- Operator norm of a linear map
- Order of an element
- Quotient ring by several relations
- Source, sink and terminal of a network (also: terminal, source and sink of the network)

## Symbols bound on earlier pages

- $n$ (input length in bits), bound on `fixed-tape-model`: The count of bits in each input of the machine, the length in bits of each input.
- $\kappa$ (fixed exponent saving), bound on `fixed-tape-model`: A fixed constant equal to $2^{-182}$, the same for every input length $n$.
- $n$ (input length), bound on `schonhage-strassen-conjecture`: The number of bits in each of the two integers being multiplied, which is the length the worst-case time is measured against.
- $\kappa$ (power-saving constant), bound on `schonhage-strassen-conjecture`: A fixed constant greater than 0 that does not depend on $n$.
- $b$ (imaginary part), bound on `gaussian-dyadic`: The imaginary part of the Gaussian dyadic number $z$.
- $m$ (integer numerator), bound on `gaussian-dyadic`: The integer numerator of a dyadic rational written as $m/2^k$.
- $u$ (first input value), bound on `gaussian-dyadic`: The first value of an input pair to the butterfly map $H_0$.
- $p$ (fractional bit count), bound on `gaussian-dyadic`: The number of fractional bits in a stored coefficient, so each stored part is a multiple of $2^{-p}$.
- $y$ (second bank value), bound on `linear-network`: The value of the second bank, held on one wire.
- $W$ (number of roles), bound on `role-streams`: The number of roles, the fixed wire places of the network.
- $V$ (node volume), bound on `role-streams`: The number of bits the node holds once its rows are padded.
- $u$ (tail vertex), bound on `frame`: The vertex at which an edge starts, so that the frame change $D_vD_u^{-1}$ starts from its frame $D_u$.
- $j$ (input index), bound on `frame`: The position of an input array of a gate, counted from 1.
- $s$ (route length), bound on `frame`: The number of edges in a route, so that the route has $s+1$ vertices.
- $m$ (space dimension), bound on `subspace-labels`: The dimension of the space E, which counts the basis vectors of E.
- $y$ (head vertex), bound on `subspace-labels`: A vertex at the head of the edge from x, the vertex the edge enters.
- $s$ (smaller call count), bound on `subspace-labels`: The total number of smaller calls, which counts the smaller operations over all edges.
- $s$ (smaller call count), bound on `recursive-saving`: The total number of smaller calls, counted as the sum of the edge ranks over all edges.
- $u$ (field width), bound on `tape-interchange`: The number of bits in each of the two address fields, their common width.
- $V$ (stored volume), bound on `tape-interchange`: The number of data units in the array, the stored volume.
- $\tau$ (saving exponent), bound on `tape-interchange`: A fixed number below 1 that sets the size of the saving in the cost bound.
- $m$ (matrix size), bound on `tape-interchange`: The number of rows of each rational matrix held at a vertex of the network, and the parameter of the recursion.
- $d$ (recursion depth), bound on `tape-interchange`: The number of levels of recursion below the top call, so that the width of the interchange is m^d.
- $j$ (second index), bound on `cyclic-convolution`: An index into the second list, running over 0 to S-1.
- $b$ (second coefficient list), bound on `cyclic-convolution`: The second input list, whose j-th coefficient is b_j.
- $b$ (digit width), bound on `radix-digit-convolution`: The number of bits in each radix digit.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of radix digits in each input, $\lceil n/b \rceil$.
- $V$ (second digit polynomial), bound on `radix-digit-convolution`: The polynomial $V(t)$ whose coefficients are the digits of the second input.
- $W$ (product polynomial), bound on `radix-digit-convolution`: The product $U(t)V(t)$, whose value at $t = 2^b$ is the integer product of the inputs.
- $u$ (input vector), bound on `fourier-transform`: A complex vector of length q, the input of the transform.
- $j$ (input index), bound on `fourier-transform`: An index running over the entries of u, from 0 to q-1.
- $b$ (second vector), bound on `fourier-transform`: A vector of length q, the second input of the convolution.
- $r$ (summation index), bound on `fourier-transform`: A second summation index running over the entries of b, from 0 to q-1.
- $e$ (general vector of E), bound on `tensor-product`: A general vector of $E$.
- $p$ (basis count of E), bound on `tensor-product`: The number of basis vectors of $E$, its dimension.
- $j$ (basis index of F), bound on `tensor-product`: The index of a basis vector $f_j$, running from $1$ to $q$.
- $d$ (number of axes), bound on `multidim-transform`: The number of axes of the array, which counts the coordinates each entry is indexed by.
- $d$ (chunk count), bound on `butterfly-layer`: The number of equal-width chunks, each with one selected bit, on which the layer acts.
- $r$ (record length), bound on `butterfly-layer`: The number of complex coefficients in each polynomial record stored at an address.
- $e$ (chunk length), bound on `butterfly-layer`: The number of positions in each of the two chunks being interchanged.
- $y$ (polynomial variable), bound on `roots-of-unity`: The formal variable of the polynomial ring modulo y^r+1, whose powers are the roots used here.
- $r$ (reduced length), bound on `roots-of-unity`: The number of complex coefficients of a reduced polynomial, a power of two.
- $p$ (exponent of y), bound on `roots-of-unity`: The exponent with 0 <= p < r such that a power of y equals plus or minus y^p.
- $y$ (polynomial variable), bound on `polynomial-ring`: The formal variable of the ring, whose powers act as roots of unity on the remaining axes.
- $r$ (coefficient count), bound on `polynomial-ring`: The number of complex coefficients in each polynomial record, which is a power of two.
- $s$ (source length), bound on `gaussian-resampling`: The number of coordinates of the source transform.
- $\tau$ (phase twist), bound on `bluestein`: The phase twist $\tau_p=\exp(\pi i p/q)$ at an integer $p$, a unit complex number with $\tau_{p+q}=-\tau_p$.
- $j$ (axis index), bound on `crt-axis-map`: A second index of an axis, running from 1 to d, used in the digit sums.

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

## Page to audit (`fixed-tape-multiplication`)

````markdown
# Fixed-tape integer multiplication with a power saving

Fixed-tape integer multiplication with a power saving is a deterministic algorithm that runs on one [Fixed-tape machine model](fixed-tape-model.md) and multiplies two $n$-bit integers exactly.

Its worst-case time is $O(n(\lg n)^{1-\kappa})$, with $\kappa=2^{-182}$ (cited). It achieves a [Power saving in the logarithmic factor](power-saving.md), which puts its time below $n\log n$ by a power of $\lg n$. It disproves the [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md) in this model.

The digit width is $b=\lceil\log_2 n\rceil$ and the precision is $p=6b$ (cited), the number of bits kept after each rounding. The digit width must grow for the rounding error to fall (see below), yet only as $\lg n$, so $p$ is of order $\lg n$. The stored volume $V=\Theta(n)$ holds about $n/b$ records of $p$ bits each.

It reduces multiplication to convolution through [Radix-digit convolution](radix-digit-convolution.md), with $\lceil n/b\rceil$ digits per input. It places the coefficients on axes by the [Chinese-remainder axis map](crt-axis-map.md). It rewrites its prime-length transforms by [Gaussian resampling](gaussian-resampling.md). It reduces the middle transform by [Bluestein's chirp identity](bluestein.md). It computes its transforms by a [Synthetic polynomial transform](synthetic-transform.md) over $\mathbb C[y]/(y^r+1)$. Each transform is built from simultaneous layers of [Simultaneous butterfly layer H₀](butterfly-layer.md) on polynomial records.

It packs signed coefficients by [Signed coefficient packing](signed-packing.md), so that polynomial products become integer products. It computes its shorter products by the [Established fast multiplier](multiplier-subroutine.md), used as a black box. It recovers the exact binary product by [Exact recovery by rounding and carries](exact-recovery.md). It carries out its address rearrangements by [Fast interchange of address chunks](tape-interchange.md), which swaps two equal-width address fields of width $u$. A swap costs $O(Vu^{\tau})$ time (cited), a power of the width.

Rounding errors are a fixed multiple of $2^{-p}$, times a factor growing with the sizes. Undoing the digit scales gives a final coefficient error of at most a constant times

$$2^{2b+4}\cdot 2^{b}\cdot 2^{2b}\cdot 2^{-6b}\cdot 2^{b/4}\cdot b=O(b\,2^{-3b/4}).$$

Here $2^{2b+4}$ reverses the digit scales, $2^{b}$ and $2^{2b}$ bound the record count and its square, $2^{-6b}=2^{-p}$ is the resolution of stored values, and $2^{b/4}$ bounds the remaining factor once $b\ge 2^{24}$. The factor $b$ counts carries. The error is at most $448b\,2^{-3b/4}$, which is below $1/2$ for $b$ beyond a fixed cutoff (cited). The true coefficients are integers, so the nearest integer to each computed value is the true coefficient (cited).

The paper's table bounds the power of $p$ in each of seven dominant costs $V p^{e}$ by $1-2\kappa$ (cited). The margin $1-e$ is smallest, $2\kappa$, for the chunk-exchange row (cited). So the seven terms sum to $O(Vp^{1-2\kappa}(\log p)^{O(1)})$, and since $(\log p)^{O(1)}\le p^{\kappa}$ for large $p$, the cost is $O(Vp^{1-\kappa})=O(n(\lg n)^{1-\kappa})$.

The width falls by a factor $m$ at each recursion level: at depth $d$ the width is $m^{d}$, where $m$, a fixed integer, is that factor; this letter changes meaning here. Each recursive call acts on one role stream of volume $V/W$, and there are $s$ smaller calls, so each level multiplies the cost per unit volume by $s/W$. This factor is below the swap's gain $m^{\tau}$: $s/W<m^{\tau}$ (cited). Summing over the levels gives

$$\sum_{j=0}^{d}(s/W)^{j}\,m^{(d-j)\tau}=m^{d\tau}\sum_{j=0}^{d}\bigl((s/W)m^{-\tau}\bigr)^{j}.$$

The ratio $(s/W)m^{-\tau}$ stays below $1$ by a fixed margin, which the paper checks. So the sum is at most a constant times its first term, and the cost per unit volume at depth $d$ is $O(m^{d\tau})=O(u^{\tau})$, where $u=m^{d}$ is the width.
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

Write the answer to `exegenius/tasks/0181-audit-fixed-tape-multiplication.answer.json`, then run `exegenius submit 0181-audit-fixed-tape-multiplication` in the project directory. If submit rejects the answer, fix the answer and submit again.
