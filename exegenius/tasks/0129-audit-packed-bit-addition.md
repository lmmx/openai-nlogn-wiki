# exegenius task 0129-audit-packed-bit-addition

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
- Convolution over the polynomial ring
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network)
- Address-field interchange (also: power-width interchange)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity)
- Simultaneous butterfly layer (also: butterfly layers)
- Guard-width bound
- Transform layout (also: transform layers, selected bits, layouts of the multiplication algorithm)
- Exact coefficient recovery
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
- $x$ (first input), bound on `exact-integer-multiplication`: The first binary string input, of length n.
- $y$ (second input), bound on `exact-integer-multiplication`: The second binary string input, of length n.
- $z$ (integer to encode), bound on `exact-integer-multiplication`: A nonnegative integer less than 2^{2n} whose binary representation is taken.
- $V$ (stored volume), bound on `address-interchange`: The number of bits the array stores.
- $\tau$ (cost exponent), bound on `address-interchange`: A fixed constant less than 1 in the cost bound $O(V u^{\tau})$.
- $f$ (polynomial), bound on `signed-packing`: A polynomial with integer coefficients, packed into the integer $F$.
- $B$ (bilinear form), bound on `bilinear-form`: The function that takes two vectors of U and returns a scalar, linear in each argument.
- $x$ (first argument), bound on `subspace-labels`: A vector of F, the first argument of the bilinear form.
- $y$ (second argument), bound on `subspace-labels`: A vector of F, the second argument of the bilinear form.
- $V$ (larger label), bound on `subspace-labels`: The larger of the two labels on an edge, containing the smaller label U.
- $R$ (orthogonal residual), bound on `subspace-labels`: The orthogonal residual of an edge, the orthogonal complement of the smaller label inside the larger one.
- $f$ (recursion parameter), bound on `rank-saving-recursion`: The recursion parameter: the number of field digits for address interchange, or of selected axes for a numerical layer.
- $a$ (kernel scalar a), bound on `complex-phase-network`: The coefficient of the identity in a two-point kernel $aI+bX$.
- $b$ (kernel scalar b), bound on `complex-phase-network`: The coefficient of the swap in a two-point kernel $aI+bX$.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with i squared equal to -1.
- $f$ (basis vector of Q), bound on `tensor-product`: A basis vector of the second factor Q, paired with a basis vector e of P to form a basis vector of the tensor product.
- $a$ (first input sequence), bound on `cyclic-convolution`: The first sequence of t complex numbers, indexed from 0 to t-1.
- $b$ (second input sequence), bound on `cyclic-convolution`: The second sequence of t complex numbers, indexed from 0 to t-1.
- $i$ (index into a), bound on `cyclic-convolution`: The index of an entry of a, ranging over 0 to t-1.
- $j$ (index into b), bound on `cyclic-convolution`: The index of an entry of b, ranging over 0 to t-1.
- $x$ (input vector), bound on `discrete-fourier-transform`: The input vector of q complex numbers, indexed from 0 to q-1.
- $j$ (input index), bound on `discrete-fourier-transform`: The index of an input entry, ranging over 0 to q-1.
- $i$ (second input index), bound on `discrete-fourier-transform`: A second index of an input entry, used when the sums are exchanged.
- $d$ (digit width), bound on `radix-digit-convolution`: The number of bits in each radix-2^d digit.
- $L$ (digit count), bound on `radix-digit-convolution`: The number of radix-2^d digits in each input.
- $x_j$ (digit of x), bound on `radix-digit-convolution`: The j-th radix-2^d digit of x, an integer in [0, 2^d), with index 0 the least significant.
- $y_j$ (digit of y), bound on `radix-digit-convolution`: The j-th radix-2^d digit of y, defined in the same way as the digits of x.
- $y$ (ring variable), bound on `synthetic-transforms`: The variable of the ring C[y]/(y^r+1), where y^r equals -1; the letter changes meaning from the multiplication page's second input.
- $a$ (input records), bound on `synthetic-transforms`: The input vector of q records a_0 through a_{q-1}; the letter changes meaning from the cyclic convolution page.
- $y$ (polynomial variable), bound on `polynomial-ring-mod-yr-plus-1`: The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $d$ (number of axes), bound on `chinese-remainder-map`: The number of cyclic axes, a count of the lengths m_i.
- $N$ (number of positions), bound on `chinese-remainder-map`: The product of the axis lengths, counting the coefficient positions.
- $x$ (position), bound on `chinese-remainder-map`: A coefficient position, an integer from 0 to N-1.
- $z$ (target position), bound on `chinese-remainder-map`: The position of the convolution output whose sum is being formed.
- $B$ (twisted second input), bound on `phase-twist`: The polynomial in $y$ obtained from the sequence $b$ by multiplying its $j$-th entry by $\theta^j$.
- $N$ (record count), bound on `polynomial-ring-convolution`: The number of records in each of the two arrays, so each array has N entries.
- $d$ (chunk count bound), bound on `simultaneous-butterfly-layer`: The maximum number of equal-width address chunks that carry the selected bit position.
- $S$ (diagonal phase), bound on `simultaneous-butterfly-layer`: The diagonal $2\times 2$ matrix with diagonal entries $1$ and $i$, a phase.
- $z$ (example values), bound on `simultaneous-butterfly-layer`: The stored values in the $D=2$ example, indexed by the two selected bits.
- $K$ (chunk width), bound on `transform-layout`: The number of address bits in one chunk.

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

## Page to audit (`packed-bit-addition`)

````markdown
# Packed selected-bit addition

Packed selected-bit addition is a fixed multitape procedure that performs many binary row additions in one pass. Packed selected-bit addition supplies the binary basis changes for the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), whose exact computation needs them.

A binary row addition adds one row of a matrix into another in every column, so it changes the selected bits of two whole address chunks at once. The procedure performs all the XORs of one such addition together rather than one bit position at a time.

The record's address is split into three chunks named $x$, $y$, and $z$; here these letters name chunks, so $y$ no longer means the polynomial variable. Here $f$ is the number of selected positions in each chunk. $K$ is the spacing between them, not the chunk width used on the transform layout page. Each chunk has $L$ bits, the chunk width, with $L = fK$.

The selected positions start at offset $\rho$, with $0 \le \rho < K$. Here $i$ indexes selected positions, not the convolution indices of earlier pages. The $i$-th selected position is $j_i = \rho + iK$ for $0 \le i < f$, counted from the least significant bit. The procedure computes

$$y_{j_i} \leftarrow y_{j_i} \oplus x_{j_i} \qquad (0 \le i < f),$$

so the selected bits of $x$ are XORed into the same positions of $y$, where $\oplus$ is exclusive or.

For example, take $f=2$, $K=6$, $L=12$ and $\rho=1$, so $j_0=1$ and $j_1=7$. If the $x$ bits there are $1$ and $0$, and the $y$ bits are $1$ and $1$, the procedure leaves the $y$ bits as $0$ and $1$.

Packed selected-bit addition is built from three streaming operations: an [address-field interchange](address-interchange.md) of equal-width chunks, cyclic shifts of chunk ranges, and a fixed permutation of two-bit values. A streaming operation is a fixed multitape procedure whose time grows with the volume it processes. A coordinate range is the finite set of values one address coordinate takes, and a cyclic shift of a chunk range adds an offset, set by the other chunks, to that chunk's value modulo $2^L$. Packed selected-bit addition is a restricted form of the [address shear](address-shear.md) that changes only the selected positions.

Each record has $R$ bits, a bit count, not the orthogonal residual $R$ of earlier pages. Let $N_0,\dots,N_3$ be the sizes of the four other coordinate ranges, so $M = 2^{3L}N_0N_1N_2N_3$ counts the records, and $V = MR$ is the total number of bits.

The construction first applies a constant number of cyclic shifts, whose composition is $S_0$. Outside a set $B$ of exceptional addresses, $S_0$ agrees with the exact map $T_0$ that performs the XORs. The fraction $\delta_{\text{bad}} = \min\{1, 80(f-1)2^{-K}\}$ is small when $K$ is large. The exceptions are few: $|B| \le \delta_{\text{bad}} M$ (cited).

The exact map $T_0$ preserves $B$ (cited). Since $S_0$ and $T_0$ agree outside $B$ and both are bijections, $T_0S_0^{-1}$ fixes every address outside $B$ and permutes $B$. Applying this correction after the shifts therefore gives $T_0$ exactly.

Under the asymptotic conditions of the lemma, the time is $O(V(L^\tau+1))$ (cited).
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

Write the answer to `exegenius/tasks/0129-audit-packed-bit-addition.answer.json`, then run `exegenius submit 0129-audit-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.
