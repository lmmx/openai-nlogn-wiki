# exegenius task 0124-audit-polynomial-ring-convolution

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

For these sources: The reader has completed an undergraduate computer science degree: big-O analysis, polynomials and complex numbers, and Turing machines with tapes, plus the discrete mathematics and first linear algebra course that such a degree requires. For the paper this means modular arithmetic, gcd and primes, roots of unity, binary arithmetic over F2 with Hamming weight, and basic vector-space and matrix facts (subspaces, rank, projections, dot product, eigenvalues) at first-course depth. Bilinear forms, tensor products, finite-field and ring theory, the Chinese remainder theorem, Newton iteration and the Fourier and convolution machinery beyond the basics are treated as not known.

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model, fixed-tape machine)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transforms)
- Cyclic convolution (also: convolution, normalized cyclic convolution, cyclic product (cyclic convolution))
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Chinese-remainder map (also: Agarwal–Cooley map)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Phase twist
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network)
- Address-field interchange (also: power-width interchange)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity)
- Mathematical induction (also: induction, proof by induction, inductive proof)
- Logarithms and floor and ceiling functions (also: floor function, ceiling function, integer part, log base 2, lg)
- Binary representation of integers (also: binary string, bit string, base-2 representation, binary digits, bits)
- Dyadic rationals (also: binary fractions, dyadic numbers)
- Modular arithmetic (also: congruence modulo m, residues modulo m, integers modulo m, remainder arithmetic)
- Greatest common divisor and coprimality (also: gcd, relatively prime, coprime, Euclidean algorithm)
- Prime numbers (also: primes, primality, prime factorization)
- Roots of unity (also: n-th roots of unity, primitive root of unity, unit roots, powers of a root of unity)
- Binary field F2 and XOR arithmetic (also: GF(2), field of two elements, mod-2 arithmetic, exclusive or, XOR, Boolean addition)
- Hamming weight (also: popcount, number of ones, weight of a binary vector, wt(x))
- Vector spaces and subspaces (also: linear subspace, span, basis, linear independence, dimension)
- Matrices and linear maps (also: matrix multiplication, matrix inverse, transpose, identity matrix, linear transformation)
- Matrix rank (also: rank, rank of a linear map, column rank, row rank)
- Projection onto a subspace (also: projection matrix, idempotent linear map, orthogonal projection)
- Dot product and orthogonality (also: inner product, scalar product, orthogonal vectors, perpendicular vectors, orthogonal complement)
- Eigenvalues and eigenvectors (also: eigenvalue, eigenvector, spectrum, characteristic polynomial)
- Bilinear form (also: bilinear space, nondegenerate form)
- Tensor product (also: tensor product of spaces)

## Symbols bound on earlier pages

- $a$ (real numerator part), bound on `gaussian-dyadics`: The integer real part of the numerator $a + bi$ of a Gaussian dyadic.
- $b$ (imaginary numerator part), bound on `gaussian-dyadics`: The integer imaginary part of the numerator $a + bi$ of a Gaussian dyadic.
- $k$ (denominator exponent), bound on `gaussian-dyadics`: The non-negative integer exponent that sets the common denominator $2^k$.
- $u$ (first coefficient), bound on `gaussian-dyadics`: The first coefficient of a pair on which the two-point map $H_0$ acts.
- $v$ (second coefficient), bound on `gaussian-dyadics`: The second coefficient of a pair on which the two-point map $H_0$ acts.
- $u$ (field size), bound on `fixed-tape-model`: The number of cells in each of two disjoint fields, which counts the cells of a field.
- $n$ (input length), bound on `exact-integer-multiplication`: The number of bits in each of the two inputs, the common length of x and y.
- $y$ (second input), bound on `exact-integer-multiplication`: The second binary string input, of length n.
- $u$ (field width), bound on `address-interchange`: The number of bits in each address field.
- $n$ (input length), bound on `established-multiplier`: The number of bits in each of the two binary input strings.
- $F$ (packed integer of f), bound on `signed-packing`: The integer $f(2^w)$ obtained by packing the coefficients of $f$ into blocks of width $w$.
- $G$ (packed integer of g), bound on `signed-packing`: The integer $g(2^w)$ obtained by packing the coefficients of $g$ into blocks of width $w$.
- $u$ (first vector), bound on `bilinear-form`: A vector of U, the first argument of the form.
- $v$ (second vector), bound on `bilinear-form`: A vector of U, the second argument of the form.
- $F$ (fixed bilinear space), bound on `subspace-labels`: The fixed bilinear space on which all subspace labels are based.
- $y$ (second argument), bound on `subspace-labels`: A vector of F, the second argument of the bilinear form.
- $m$ (label space dimension), bound on `subset-intersection-network`: The dimension of the fixed space from which the subspace labels are drawn, a count of its basis vectors.
- $X$ (two-point swap), bound on `complex-phase-network`: The swap of the two points, a 2 by 2 swap matrix.
- $a$ (kernel scalar a), bound on `complex-phase-network`: The coefficient of the identity in a two-point kernel $aI+bX$.
- $b$ (kernel scalar b), bound on `complex-phase-network`: The coefficient of the swap in a two-point kernel $aI+bX$.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with i squared equal to -1.
- $t$ (sequence length), bound on `cyclic-convolution`: The number of entries in each of the two sequences, a positive integer.
- $a$ (first input sequence), bound on `cyclic-convolution`: The first sequence of t complex numbers, indexed from 0 to t-1.
- $b$ (second input sequence), bound on `cyclic-convolution`: The second sequence of t complex numbers, indexed from 0 to t-1.
- $i$ (index into a), bound on `cyclic-convolution`: The index of an entry of a, ranging over 0 to t-1.
- $j$ (index into b), bound on `cyclic-convolution`: The index of an entry of b, ranging over 0 to t-1.
- $k$ (index into c), bound on `cyclic-convolution`: The index of an entry of the output sequence c, ranging over 0 to t-1.
- $c$ (cyclic convolution), bound on `cyclic-convolution`: The output sequence a \ast b of length t, whose k-th entry is the sum of a_i b_j over all pairs with i+j congruent to k modulo t.
- $\omega$ (root of unity), bound on `discrete-fourier-transform`: A primitive q-th root of unity, a complex number whose powers are all different from 1 below q.
- $X$ (transform vector), bound on `discrete-fourier-transform`: The transform of x, the vector of q outputs computed from x.
- $j$ (input index), bound on `discrete-fourier-transform`: The index of an input entry, ranging over 0 to q-1.
- $k$ (output index), bound on `discrete-fourier-transform`: The index of an output entry, ranging over 0 to q-1.
- $i$ (second input index), bound on `discrete-fourier-transform`: A second index of an input entry, used when the sums are exchanged.
- $m$ (integer exponent), bound on `discrete-fourier-transform`: An integer whose divisibility by q decides whether the root-of-unity sum vanishes.
- $t$ (indeterminate), bound on `radix-digit-convolution`: The indeterminate of the digit polynomials P(t) and Q(t).
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two.
- $y$ (ring variable), bound on `synthetic-transforms`: The variable of the ring C[y]/(y^r+1), where y^r equals -1; the letter changes meaning from the multiplication page's second input.
- $a$ (input records), bound on `synthetic-transforms`: The input vector of q records a_0 through a_{q-1}; the letter changes meaning from the cyclic convolution page.
- $y$ (polynomial variable), bound on `polynomial-ring-mod-yr-plus-1`: The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $r$ (record length), bound on `polynomial-ring-mod-yr-plus-1`: The number of complex coefficients in a polynomial record, a power of two.
- $k$ (power exponent), bound on `polynomial-ring-mod-yr-plus-1`: The exponent of a power y^k, a non-negative integer.
- $N$ (number of positions), bound on `chinese-remainder-map`: The product of the axis lengths, counting the coefficient positions.
- $t$ (reduced index), bound on `bluestein-chirp-identity`: The index $(k-j) \bmod q$ in $\{0,\ldots,q-1\}$ at which the chirp sequence $b$ is evaluated.

## Pages in the wiki

- [Gaussian dyadics](gaussian-dyadics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Address-field interchange](address-interchange.md)
- [Address shear](address-shear.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Complex phase network](complex-phase-network.md)
- [Tensor product](tensor-product.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Transform layout](transform-layout.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`polynomial-ring-convolution`)

````markdown
# Convolution over the polynomial ring

Convolution over the polynomial ring is the [cyclic product](cyclic-convolution.md) of two arrays of records, and it computes convolution on the remaining axes by transforms and one pointwise product. Convolution over the polynomial ring takes its records from the [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md).

Let $a = (a_0, \dots, a_{N-1})$ and $b = (b_0, \dots, b_{N-1})$ be arrays of $N$ records, where $N$ is the number of records in each array. Here $a$, $b$ and $c$ are arrays of records. The indices $i$, $j$ and $k$ run from $0$ to $N-1$. The convolution is the array $c$ with
$$c_k = \sum_{\substack{0 \le i,j < N \\ i + j \equiv k \pmod{N}}} a_i\, b_j,$$
so $c_k$ sums the products $a_i b_j$ over pairs whose indices add to $k$ modulo $N$. Computing $c$ directly takes $N^2$ record products.

Let $\omega = y^{2r/N}$, the synthetic root of unity of order $N$, so that $\omega^N = 1$. Let $F$ be the forward synthetic transform, $F(a)_m = \sum_j a_j\,\omega^{jm}$, and let $G$ be the opposite transform, $G(X)_k = \frac{1}{N}\sum_m X_m\,\omega^{-km}$, which uses the inverse root $\omega^{-1}$ and divides by $N$. Here $F$ and $G$ are transforms. The index $m$ labels the frequency of an entry. The two forward transforms keep the same frequency order (cited), so one index $m$ pairs $F(a)_m$ with $F(b)_m$.

$$c = G\big(F(a) \odot F(b)\big).$$

Here $\odot$ multiplies two arrays entrywise in the ring. Both inputs must be transformed, and the pointwise product needs only $N$ record products. The $k$-th entry of the right side is
$$\frac{1}{N}\sum_{m=0}^{N-1}\Big(\sum_i a_i\omega^{im}\Big)\Big(\sum_j b_j\omega^{jm}\Big)\omega^{-km} = \sum_{i,j} a_i b_j\cdot\frac{1}{N}\sum_{m=0}^{N-1}\omega^{(i+j-k)m}.$$
The inner sum is $N$ when $i+j \equiv k \pmod{N}$. Otherwise $t = i+j-k$ is not a multiple of $N$, so $\omega^t - 1$ is nonzero at every root of $y^r+1$ and invertible in the ring. Multiplying the inner sum by $\omega^t-1$ gives $\omega^{tN}-1 = 0$, so the sum is $0$. Only pairs with $i+j \equiv k$ survive, and the factor $1/N$ in $G$ is the normalization, so $c$ is exact.

Take $N = 2$, so $\omega = y^r = -1$. Then $F(a) = (a_0+a_1,\ a_0-a_1)$, and $F(b)$ is the same with $b$. Their pointwise product is $\big((a_0+a_1)(b_0+b_1),\ (a_0-a_1)(b_0-b_1)\big)$. With $G(u,v) = \big(\tfrac{u+v}{2}, \tfrac{u-v}{2}\big)$, where $u$ and $v$ are the two entries of the argument pair, this gives $c_0 = a_0 b_0 + a_1 b_1$ and $c_1 = a_0 b_1 + a_1 b_0$, the cyclic product for $N=2$.

Multiplying by a power of $y$ is a signed shift of coefficients. Convolution over the polynomial ring computes its transforms with [Synthetic polynomial transforms](synthetic-transforms.md), so the transforms need only signed shifts and additions.

The pointwise products are polynomial products. Convolution over the polynomial ring computes its products with [Signed coefficient packing](signed-packing.md), which turns each record product into one integer product, computed by the [established $O(n\log n)$ multiplier](established-multiplier.md).
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

Write the answer to `exegenius/tasks/0124-audit-polynomial-ring-convolution.answer.json`, then run `exegenius submit 0124-audit-polynomial-ring-convolution` in the project directory. If submit rejects the answer, fix the answer and submit again.
