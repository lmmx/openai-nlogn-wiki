# exegenius task 0178-audit-bluestein

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
- Source, sink and terminal of a network (also: terminal, source and sink of the network)

## Symbols bound on earlier pages

- $k$ (power-of-two exponent), bound on `gaussian-dyadic`: The exponent of the power of two in the denominator of a dyadic rational $m/2^k$.
- $u$ (first input value), bound on `gaussian-dyadic`: The first value of an input pair to the butterfly map $H_0$.
- $p$ (fractional bit count), bound on `gaussian-dyadic`: The number of fractional bits in a stored coefficient, so each stored part is a multiple of $2^{-p}$.
- $i$ (row index), bound on `role-streams`: The position of a row among the rows that share its prefix, counted from 0.
- $u$ (tail vertex), bound on `frame`: The vertex at which an edge starts, so that the frame change $D_vD_u^{-1}$ starts from its frame $D_u$.
- $j$ (input index), bound on `frame`: The position of an input array of a gate, counted from 1.
- $q$ (modulus), bound on `address-shear`: The fixed modulus q, whose residue ring Z/qZ contains the entries of H and D.
- $u$ (field width), bound on `tape-interchange`: The number of bits in each of the two address fields, their common width.
- $\tau$ (saving exponent), bound on `tape-interchange`: A fixed number below 1 that sets the size of the saving in the cost bound.
- $i$ (first index), bound on `cyclic-convolution`: An index into the first list, running over 0 to S-1.
- $j$ (second index), bound on `cyclic-convolution`: An index into the second list, running over 0 to S-1.
- $k$ (output index), bound on `cyclic-convolution`: The index of an output coefficient c_k, running over 0 to S-1.
- $u$ (input vector), bound on `fourier-transform`: A complex vector of length q, the input of the transform.
- $q$ (transform length), bound on `fourier-transform`: The number of entries of u, which is the length of the transform.
- $\hat u$ (transform of u), bound on `fourier-transform`: The vector of Fourier coefficients of u, with entries given by the transform formula.
- $j$ (input index), bound on `fourier-transform`: An index running over the entries of u, from 0 to q-1.
- $k$ (output index), bound on `fourier-transform`: An index running over the entries of the transform, from 0 to q-1.
- $p$ (basis count of E), bound on `tensor-product`: The number of basis vectors of $E$, its dimension.
- $q$ (basis count of F), bound on `tensor-product`: The number of basis vectors of $F$, its dimension.
- $i$ (basis index of E), bound on `tensor-product`: The index of a basis vector $e_i$, running from $1$ to $p$.
- $j$ (basis index of F), bound on `tensor-product`: The index of a basis vector $f_j$, running from $1$ to $q$.
- $\nu$ (number of lengths), bound on `order-of-element`: The number of pairwise coprime lengths $s_1,\dots,s_\nu$ of the source, a count.
- $p$ (exponent of y), bound on `roots-of-unity`: The exponent with 0 <= p < r such that a power of y equals plus or minus y^p.
- $i$ (coefficient position), bound on `polynomial-ring`: The position of a coefficient in a coefficient list, running from 0 to r-1.
- $k$ (shift count), bound on `polynomial-ring`: The number of places a coefficient is shifted when the element is multiplied by y^k, with 0 \le k < r.
- $\mu$ (twiddle exponent), bound on `synthetic-transform`: The exponent of the twiddle factor $y^\mu$, an integer from 0 to 2r-1.
- $\nu$ (power exponent), bound on `gaussian-resampling`: The positive integer exponent with t = 2^nu in the application.

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

## Page to audit (`bluestein`)

````markdown
# Bluestein's chirp identity

Bluestein's chirp identity rewrites the [discrete Fourier transform](fourier-transform.md) of a vector and computes it by a [cyclic convolution](cyclic-convolution.md) placed between two pointwise multiplications.

Bluestein's chirp identity acts on the middle transform of the paper's multiplication algorithm, including its [target permutation](gaussian-resampling.md). The identity performs that permutation inside its multiplications, so no separate pass is needed, and it turns the transform into (cited).

Take one coordinate of length $q$, so $\hat u_k=\frac1q\sum_j u_j\exp(-2\pi i jk/q)$. Let $\chi_p=\exp(-\pi i p^2/q)$ be the chirp value at an integer $p$. Since $2jk=j^2+k^2-(k-j)^2$,

$$\exp\left(-\frac{2\pi i\, jk}{q}\right)=\chi_j\,\chi_k\,\overline{\chi_{k-j}},$$

so $q\,\hat u_k=\chi_k\sum_j (u_j\chi_j)\,\overline{\chi_{k-j}}$. The factors $\chi_j$ and $\chi_k$ are pointwise multiplications, and the sum is a convolution in the index $k-j$.

For even $q$, $\chi_{p+q}=\chi_p$, so $\overline{\chi_{k-j}}$ may be read at the residue $(k-j)\bmod q$, and the sum is already a cyclic convolution.

For odd $q$, $\chi_{p+q}=-\chi_p$, so each wrapped term would carry a sign $-1$ that a cyclic convolution lacks. The phase twist removes it. Let $\tau_p=\exp(\pi i p/q)$ be the phase twist at an integer $p$, which satisfies $\tau_{p+q}=-\tau_p$. The twisted sequences are $\mu_j=u_j\chi_j\tau_j$ and $\nu_p=\overline{\chi_p}\,\tau_p$ for $0\le j,p<q$. Each product $\mu_j\nu_{(k-j)\bmod q}$ equals $\tau_k\,u_j\chi_j\overline{\chi_{k-j}}$: at a wrap the two sign changes cancel, and $\tau_j\tau_{k-j}=\tau_k$. Therefore

$$q\,\hat u_k=\chi_k\,\overline{\tau_k}\sum_j \mu_j\,\nu_{(k-j)\bmod q}.$$

The paper's own phase twist does this on its last cyclic coordinate, and (cited).
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

Write the answer to `exegenius/tasks/0178-audit-bluestein.answer.json`, then run `exegenius submit 0178-audit-bluestein` in the project directory. If submit rejects the answer, fix the answer and submit again.
