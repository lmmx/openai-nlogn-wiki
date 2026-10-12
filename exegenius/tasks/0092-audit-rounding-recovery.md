# exegenius task 0092-audit-rounding-recovery

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

For these sources: The reader has an undergraduate computer science degree: big-O notation and worst-case time of Turing machines, polynomials and complex numbers, and the calculus the degree requires (limits, convergence of sequences and series, basic integrals). The same degree is taken to include introductory discrete mathematics (modular arithmetic, primes, induction, sets, graphs, recurrences) and a first course in linear algebra over the reals (vectors, subspaces, matrices, elimination, dot products), each at introductory depth. Fields in the abstract sense, tensor products, bilinear forms over general fields, Gaussian integers and the Chinese remainder theorem are not assumed.

## Known concepts

- Big-O notation (also: O-notation)
- Multitape Turing machine (also: fixed-tape model)
- Complex numbers
- Polynomials
- Schönhage–Strassen n log n conjecture (also: n log n optimality conjecture)
- Harvey–van der Hoeven O(n log n) multiplication (also: Harvey and van der Hoeven multiplier)
- Matrix rank (also: rank)
- Discrete Fourier transform (also: Fourier transform, DFT, transform of length n)
- Primitive roots of unity (also: root of unity)
- Cyclic convolution (also: normalized cyclic convolution)
- Multiplication as convolution of digits (also: radix-digit convolution)
- Chinese-remainder address map (also: Chinese remainder map)
- Gaussian resampling (also: Gaussian gridding)
- Bluestein's chirp identity (also: chirp identity, Bluestein conversion)
- Polynomial ring modulo yʳ + 1 (also: negacyclic ring, signed shift)
  - $y$ (ring indeterminate): The variable of the polynomial ring whose powers serve as roots of unity in the remaining axes.
  - $r$ (coefficient count): The number of coefficients in the coefficient list of one polynomial record, a power of two.
- Synthetic polynomial transform (also: Nussbaumer polynomial transform, synthetic transform)
- Signed Kronecker packing (also: Kronecker substitution, signed packing)
- Butterfly operation (also: two-point butterfly, H_0)
- Simultaneous butterfly layer (also: butterfly layer)
- Linear network with restored auxiliary values (also: linear network, frame)
- Lower-triangular factorization (also: Bruhat factorization with reversed order)
- Address shear (also: matrix shear)
- Fast address interchange (also: bit interchange procedure, bit procedure)
- Recursive power saving (also: recursive saving)
- Modular arithmetic (also: congruence, congruence modulo c, residue class, mod c arithmetic, integers modulo n)
- Prime numbers and greatest common divisors (also: primes, prime, gcd, greatest common divisor, coprime, relatively prime)
- Arithmetic modulo 2 and XOR (also: F_2, GF(2), Z/2Z, binary field, two-element field, exclusive or, parity, bitwise XOR)
- Dyadic rationals (also: binary fractions, numbers with power-of-two denominators, dyadic numbers, fixed-point binary fractions)
- Vector spaces, subspaces, bases and dimension (also: linear space, subspace, span, linear independence, basis, dimension, ordered basis)
- Linear maps, matrix operations and invertibility (also: linear transformation, linear operator, matrix product, transpose, invertible matrix, nonsingular matrix, inverse matrix, kernel, null space)
- Gaussian elimination (also: row reduction, Gauss-Jordan elimination, elimination, pivot)
- Triangular matrices (also: lower-triangular matrix, upper-triangular matrix, unit triangular matrix)
- Dot product and orthogonality in R^n (also: inner product, scalar product, orthogonal vectors, orthonormal basis, orthogonal complement)
- Permutations of a finite set (also: permutation, rearrangement, bijection of an index set, permutation matrix)
- Finite sets, subsets and intersections (also: set intersection, cardinality, subset, k-subset, binomial coefficient, power set)
- Graphs (also: undirected graph, vertices and edges, adjacency, neighbours, intersection graph, source and sink vertices of the network)
- Mathematical induction (also: induction, inductive proof, strong induction, proof by induction on n)
- Recurrence relations and divide-and-conquer recursion (also: recurrence, recursion equation, divide and conquer, recursive algorithm, cost recurrence, T(n) recurrence)
- Floor and ceiling functions (also: integer part, floor, ceiling, ⌊x⌋, ⌈x⌉)
- Logarithms base 2 (also: lg, log base 2, binary logarithm, log_2)
- Big-Omega and big-Theta notation (also: Omega notation, Theta notation, Ω, Θ, asymptotic lower bound, asymptotic tight bound)
- Limits and convergence of sequences and series (also: limit of a sequence, convergent sequence, convergent series, sum of a series, n tends to infinity)
- Geometric series (also: geometric sum, geometric progression sum, sum of powers of a ratio)
- Newton's method (also: Newton iteration, Newton-Raphson method, Newton reduction, Newton's root-finding iteration)
- Worst-case time complexity of a Turing machine (also: running time, worst-case running time, time bound, T_A(n), time on n-bit inputs)
- Tensor product

## Symbols bound on earlier pages

- $k$ (power exponent), bound on `roots-of-unity`: An integer exponent of the root, marking which power of $\omega$ is meant.
- $j$ (earlier exponent), bound on `roots-of-unity`: An integer exponent of the root, the smaller of two powers compared in the distinctness argument.
- $j$ (input index), bound on `fourier-transform`: An index running from $0$ to $n-1$ over the input entries.
- $k$ (output index), bound on `fourier-transform`: An index running from $0$ to $n-1$ over the output entries.
- $p$ (coefficient polynomial), bound on `fourier-transform`: The polynomial whose coefficient list is $a$, so that $a_j$ is the coefficient of $x^j$.
- $b$ (second input sequence), bound on `cyclic-convolution`: The second input sequence, a list of r complex numbers.
- $c$ (cyclic convolution), bound on `cyclic-convolution`: The length-r sequence a convolved with b cyclically, whose k-th entry is the sum over j of a_j b_((k-j) mod r).
- $b$ (digit width), bound on `convolution-reduction`: The number of bits in one digit, so that digits are taken in radix $2^b$.
- $z$ (second sequence), bound on `synthetic-transform`: A second sequence of ring elements, transformed by the same rule as $x$.
- $h$ (convolution position), bound on `synthetic-transform`: The output position of the cyclic convolution $x\ast z$, taken modulo $2r$.
- $j$ (coefficient index), bound on `kronecker-packing`: The index running over the $r$ coefficient positions of a polynomial in the ring, $0 \le j < r$.
- $F$ (packed integer of f), bound on `kronecker-packing`: The integer obtained by evaluating $f$ at the packing base $B$.
- $h$ (unreduced product), bound on `kronecker-packing`: The product $fg$ of $f$ and $g$ as polynomials, before reduction modulo $y^r+1$.
- $k$ (product power), bound on `kronecker-packing`: The power of $y$ indexing a coefficient $h_k$ of the unreduced product.
- $p$ (pivot), bound on `matrix-rank`: The nonzero pivot entry, the top-left entry after reordering rows and columns.
- $S$ (smaller matrix), bound on `matrix-rank`: The matrix left after the pivot's row and column are deleted, which is smaller than the original.
- $\rho$ (output role map), bound on `linear-network-exchange`: The map sending an input role to the output role where its value leaves the network.
- $c$ (width reduction factor), bound on `address-interchange`: The fixed integer, at least 2, by which each level divides the field width.
- $z$ (input sequence), bound on `gaussian-resampling`: The length-q sequence of complex numbers to which the transform F_q is applied.
- $c$ (identity constant), bound on `gaussian-resampling`: A fixed power of two, the scalar factor in the identity.
- $\beta$ (basis vector of X), bound on `tensor-product`: A basis vector of the space X.
- $S$ (linear map on X), bound on `tensor-product`: A linear map on the space X, the first factor of a tensor product of linear maps.
- $k$ (number of levels), bound on `recursive-power-saving`: The number of recursion levels, so that the top call has parameter m^k.
- $j$ (level index), bound on `recursive-power-saving`: The index of a recursion level, counting levels from the top.

## Pages in the wiki

- [Schönhage–Strassen n log n conjecture](nlogn-conjecture.md)
- [Harvey–van der Hoeven O(n log n) multiplication](harvey-hoeven-multiplier.md)
- [Primitive roots of unity](roots-of-unity.md)
- [Discrete Fourier transform](fourier-transform.md)
- [Butterfly operation](butterfly-operation.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Multiplication as convolution of digits](convolution-reduction.md)
- [Polynomial ring modulo yʳ + 1](polynomial-ring-y.md)
- [Synthetic polynomial transform](synthetic-transform.md)
- [Signed Kronecker packing](kronecker-packing.md)
- [Matrix rank](matrix-rank.md)
- [Linear network with restored auxiliary values](linear-network-exchange.md)
- [Lower-triangular factorization](lower-triangular-factorization.md)
- [Address shear](address-shear.md)
- [Fast address interchange](address-interchange.md)
- [Chinese-remainder address map](chinese-remainder-address-map.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Bluestein's chirp identity](bluestein-chirp.md)
- [Tensor product](tensor-product.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Recursive power saving](recursive-power-saving.md)
- [Exact recovery by rounding](rounding-recovery.md)
- [Integer multiplication in O(n(lg n)^(1-κ)) time](integer-multiplication-target.md)

## Page to audit (`rounding-recovery`)

````markdown
# Exact recovery by rounding

Exact recovery by rounding turns the approximate convolution coefficients into the exact binary product. It cancels a retained coordinate permutation, removes known scales, rounds each coefficient to an integer, and propagates carries.

Exact recovery by rounding works on the output of the [Synthetic polynomial transform](synthetic-transform.md) run in the opposite direction. Exact recovery by rounding is based on the normalized cyclic convolution that [Bluestein's chirp identity](bluestein-chirp.md) produces.

Let $\alpha$ and $\beta$ be the arrays of radix-$2^b$ digits of the two integers, each digit scaled by $2^{-b-2}$ and zero-padded to $S$ entries, where $S$ is the number of points of the source transform.

Resampling retains a coordinate permutation $R$, which reindexes an array by $(Rz)_j=z_{cj}$ for a unit $c$ modulo the length. Let $F_S$ be the normalized Fourier transform of length $S$ and $F_S^+$ the transform with the opposite sign. Substituting $h=ck$ in the Fourier sum gives $RF_S^+R=F_S^+$. Since $R$ commutes with pointwise products, the permutation cancels:

$$RF_S^+(RF_S\alpha\cdot RF_S\beta)=F_S^+(F_S\alpha\cdot F_S\beta).$$

The rule $F_S(\alpha*\beta)=S(F_S\alpha\cdot F_S\beta)$ and $F_S^+F_S$ multiplies by $1/S$ give $F_S^+(F_S\alpha\cdot F_S\beta)=(\alpha*\beta)/S^2$, where $*$ is cyclic convolution. Multiplying by $S$, then by $2^{2b+4}S$, gives $2^{2b+4}(\alpha*\beta)$. The factor $2^{2b+4}$ cancels the two digit scales. The integer coefficient of the digit convolution at position $j$ is $\rho_j$, so the integer product is $\sum_j\rho_j2^{bj}$.

Each truncation keeps $p=6b$ fractional bits, so it adds error below $2^{-p}$. Exact recovery by rounding inherits its error from each [simultaneous butterfly layer](simultaneous-butterfly-layer.md), which ends with one truncation. Tracking these errors through the transforms, the product and the scales, the error of each recovered coefficient is strictly below $1/2$ for large $b$ (cited).

Since the $\rho_j$ are integers, a value strictly within $1/2$ of $\rho_j$ has $\rho_j$ as its unique nearest integer, so rounding returns $\rho_j$. At distance exactly $1/2$ two integers are equally near, and rounding can pick the wrong one.

Exact recovery by rounding inverts the [Signed Kronecker packing](kronecker-packing.md), which evaluates the coefficients at $2^b$. Here $\delta_j$ is the $j$-th radix-$2^b$ digit of the product and $\sigma_j$ is the carry into position $j$. Set $\sigma_0=0$ and, for each $j$, $\rho_j+\sigma_j=\delta_j+2^b\sigma_{j+1}$ with $0\le\delta_j<2^b$. Multiplying the $j$-th relation by $2^{bj}$ and summing, the carries cancel in pairs, so the digits $\delta_j$ represent the same integer, with the final carry written as further digits.

Example in base $2$: computed values $2.9$ and $5.2$ round to $(3,5)$, which stands for $13$. Then $3=1+2\cdot 1$ gives digit $1$ and carry $1$; $5+1=0+2\cdot 3$ gives digit $0$ and carry $3$; $3=1+2\cdot 1$ gives digit $1$ and carry $1$, written as digit $1$. The digits $1101_2$ equal $13$.
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

Write the answer to `exegenius/tasks/0092-audit-rounding-recovery.answer.json`, then run `exegenius submit 0092-audit-rounding-recovery` in the project directory. If submit rejects the answer, fix the answer and submit again.
