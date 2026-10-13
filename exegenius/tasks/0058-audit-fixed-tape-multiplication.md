# exegenius task 0058-audit-fixed-tape-multiplication

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
- Directed graph (also: digraph, vertex, edge, head and tail, directed acyclic graph, DAG)
- Vector space, subspace, basis and dimension (also: linear space, subspace, span, linearly independent, basis, direct sum, dimension)
- Linear map and matrix (also: linear transformation, matrix, invertible matrix, nonsingular matrix, transpose, identity matrix, diagonal matrix)
- Matrix rank (also: column rank, row rank, rational rank, rank over a field)
- Gaussian elimination and triangular matrices (also: row reduction, elementary row operations, echelon form, lower triangular matrix, upper triangular matrix)
- Dot product and orthogonal complement (also: standard inner product, scalar product, orthogonal complement, perpendicular space, U perp)
- Vector norm and maximum norm (also: norm, maximum norm, sup norm, infinity norm, max norm, triangle inequality)
- Complex conjugate, modulus and polar form (also: conjugate, modulus, absolute value of a complex number, argument, unit circle, Euler's formula, polar form)

## Symbols bound on earlier pages

- $n$ (input length), bound on `schonhage-strassen-conjecture`: The number of bits in each of the two integers being multiplied.
- $n$ (input bit length), bound on `power-saving`: The number of bits in each input integer.
- $\kappa$ (saving exponent), bound on `power-saving`: A fixed number with $\kappa > 0$ that sets the size of the power saving.
- $u$ (input vector), bound on `fourier-transform`: The vector of complex numbers to be transformed, with entries $u_0, \dots, u_{q-1}$.
- $y$ (polynomial variable), bound on `polynomial-ring`: The formal variable whose powers act as roots of unity on the remaining axes.
- $r$ (coefficient count), bound on `polynomial-ring`: The number of complex coefficients in each polynomial record, which is a power of two.
- $u$ (first input), bound on `gaussian-dyadic`: A Gaussian dyadic number, the first input to the butterfly.
- $V$ (node volume), bound on `role-streams`: The number of bits the node holds after its rows are padded.
- $u$ (tail vertex), bound on `frame`: The vertex at which an edge starts, a source, gate or sink of the network.
- $u$ (first input value), bound on `butterfly-layer`: The value at one of the two addresses that differ only in the selected bit.
- $V$ (logical volume), bound on `butterfly-layer`: The number of stored data bits in the array.
- $V$ (fixed space), bound on `subspace-labels`: The fixed space in which all labels lie.
- $y$ (neighbouring vertex), bound on `subspace-labels`: The vertex at the other end of an edge from x.
- $u$ (field width), bound on `tape-interchange`: The number of bits in each address field being swapped.
- $V$ (stored volume), bound on `tape-interchange`: The total number of data units held in the array.
- $\tau$ (cost exponent), bound on `tape-interchange`: The fixed exponent, below one, in the interchange's cost bound.
- $n$ (integer bit length), bound on `multiplier-subroutine`: The bit length of each integer being multiplied, counting the bits the running time is measured against.
- $V$ (second digit polynomial), bound on `radix-digit-convolution`: The polynomial in t whose coefficients are the digits of the second input.
- $u$ (input vector), bound on `bluestein`: The vector of length $q$ whose transform is taken.

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

## Page to audit (`fixed-tape-multiplication`)

````markdown
# Fixed-tape integer multiplication with a power saving

Fixed-tape integer multiplication with a power saving is a deterministic algorithm that multiplies two integers exactly. It is the main result that disproves the [Schonhage-Strassen optimality conjecture](schonhage-strassen-conjecture.md) in the fixed-tape model. It runs on one [Fixed-tape machine model](fixed-tape-model.md) with a fixed finite alphabet and a fixed number of tapes.

Let $n$ be the number of bits in each input. The constant $\kappa$ is a fixed positive exponent. The worst-case time is $O(n(\lg n)^{1-\kappa})$, and the bound holds with $\kappa=2^{-182}$ (cited). It achieves a [Power saving in the logarithmic factor](power-saving.md), so its time is smaller than $n\log n$ by a power of $\lg n$.

It reduces multiplication to convolution through [Radix-digit convolution](radix-digit-convolution.md), so the reduction is exact and only its cost needs bounding. It places its coefficients on axes by the [Chinese-remainder axis map](crt-axis-map.md), which preserves the convolution. It rewrites its prime-length transforms by [Gaussian resampling](gaussian-resampling.md). It reduces the middle transform by [Bluestein's chirp identity](bluestein.md) to cyclic convolution. It computes its transforms by a [Synthetic polynomial transform](synthetic-transform.md) over the ring $\mathbb C[y]/(y^r+1)$. Each transform is built from simultaneous layers of [Simultaneous butterfly layer H₀](butterfly-layer.md) on polynomial records. It packs signed coefficients by [Signed coefficient packing](signed-packing.md), so that polynomial products become integer products. It calls the [Established fast multiplier](multiplier-subroutine.md) as a black box on shorter integers. It recovers the exact binary product by [Exact recovery by rounding and carries](exact-recovery.md), since the coefficient error is below $1/2$.

The tape cost comes from address rearrangements. It carries out its address rearrangements by [Fast interchange of address chunks](tape-interchange.md). Here $u$ is the number of bits in each interchanged address field. The exponent $\tau$ is a fixed number below one. Here $V$ is the stored volume of data on the tapes. A swap costs $O(Vu^{\tau})$ time (cited).

Each tape procedure costs a power $u^{\tau}$ of its width, not a linear factor, and the parameters are chosen so that this strict gap survives every layer and every level of recursion. Summing the layers gives $O(V(\lg n)^{1-\kappa})$ tape operations in total, with stored volume $V=\Theta(n)$. Since the reduction is exact, this gives the stated time $O(n(\lg n)^{1-\kappa})$.
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

Write the answer to `exegenius/tasks/0058-audit-fixed-tape-multiplication.answer.json`, then run `exegenius submit 0058-audit-fixed-tape-multiplication` in the project directory. If submit rejects the answer, fix the answer and submit again.
