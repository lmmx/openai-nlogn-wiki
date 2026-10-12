# exegenius task 0058-audit-packed-bit-addition

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
- Fixed-tape machine model (also: fixed finite-tape model)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform)
- Gaussian resampling (also: Harvey–van der Hoeven resampling)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
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
- Simultaneous butterfly layer
- Guard-width bound
- Transform layout
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

## Symbols bound on earlier pages

- $x$ (first input), bound on `exact-integer-multiplication`: The first binary input string, of length n.
- $y$ (second input), bound on `exact-integer-multiplication`: The second binary input string, of length n.
- $x_j$ (input digit), bound on `radix-digit-convolution`: The j-th radix-2^k digit of the first input x, with x_0 the least significant.
- $y_j$ (input digit), bound on `radix-digit-convolution`: The j-th radix-2^k digit of the second input y.
- $a$ (numerator real part), bound on `gaussian-dyadics`: The integer real part of the numerator a + bi of a Gaussian dyadic.
- $b$ (numerator imaginary part), bound on `gaussian-dyadics`: The integer imaginary part of the numerator a + bi of a Gaussian dyadic.
- $f$ (packed polynomial), bound on `signed-packing`: A polynomial with integer coefficients that is packed into an integer.
- $V$ (stored volume), bound on `address-interchange`: The number of bits the array stores.
- $\tau$ (cost exponent), bound on `address-interchange`: A fixed exponent less than 1 in the cost bound.
- $V$ (larger label), bound on `subspace-labels`: The label on the edge that contains the smaller label $U$.
- $R$ (orthogonal residual), bound on `subspace-labels`: The orthogonal complement of the smaller label inside the larger one, on an edge.
- $V$ (stored volume), bound on `rank-saving-recursion`: The volume of stored data that one call acts on.
- $f$ (recursion parameter), bound on `rank-saving-recursion`: The recursion parameter, counting field digits for address interchange or selected axes for a numerical layer.
- $a$ (kernel scalar a), bound on `complex-phase-network`: One of the two scalars of a two-point kernel $aI+bX$.
- $b$ (kernel scalar b), bound on `complex-phase-network`: The other scalar of a two-point kernel $aI+bX$.
- $x$ (input vector), bound on `discrete-fourier-transform`: The vector of $q$ complex numbers that the transform takes as input.
- $j$ (input index), bound on `discrete-fourier-transform`: An index running from $0$ to $q-1$ over the input entries $x_j$.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record; it is a power of two.
- $y$ (ring variable), bound on `synthetic-transforms`: The variable of the ring $\mathbb{C}[y]/(y^r+1)$, whose powers serve as roots of unity.
- $y$ (polynomial variable), bound on `polynomial-ring-mod-yr-plus-1`: The indeterminate of the polynomial ring, whose powers act as roots of unity.
- $r$ (record length), bound on `polynomial-ring-mod-yr-plus-1`: The number of complex coefficients in a polynomial record, a power of two.
- $a$ (first input array), bound on `polynomial-ring-convolution`: The first array of N records, whose entries a_0, ..., a_{N-1} are multiplied in the convolution.
- $b$ (second input array), bound on `polynomial-ring-convolution`: The second array of N records, whose entries b_0, ..., b_{N-1} are multiplied in the convolution.
- $N$ (array length), bound on `polynomial-ring-convolution`: The number of records in each array, which is the number of index positions the convolution wraps over.
- $d$ (selected chunk count), bound on `simultaneous-butterfly-layer`: The largest number of equal-width address chunks in which the same bit position is selected.
- $V$ (stored volume), bound on `simultaneous-butterfly-layer`: The logical bit volume of the stored array.
- $d$ (size parameter), bound on `guard-width-bound`: The size parameter of the network, which bounds the number of selected address bits.
- $K$ (chunk width), bound on `transform-layout`: The number of address bits in one chunk.

## Pages in the wiki

- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Signed coefficient packing](signed-packing.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Address-field interchange](address-interchange.md)
- [Address shear](address-shear.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Complex phase network](complex-phase-network.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Guard-width bound](guard-width-bound.md)
- [Transform layout](transform-layout.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`packed-bit-addition`)

````markdown
# Packed selected-bit addition

Packed selected-bit addition is a fixed multitape procedure that performs many binary row additions in one pass. It supplies the binary basis changes for the [simultaneous butterfly layer](simultaneous-butterfly-layer.md), whose exact computation needs them.

A binary row addition adds one row of a matrix into another in every column, so it changes the selected bits of two whole address chunks at once. The procedure performs the XORs of one such addition together, rather than one bit position at a time.

The record's address is split into three chunks, named $x$, $y$, and $z$; in this page these letters name chunks, so $y$ no longer means the polynomial variable. Each chunk is $L$ bits wide, with $L = fK$, where $f$ is the number of selected positions in each chunk and $K$ is the spacing between them.

The selected positions start at offset $\rho$, with $0 \le \rho < K$. The $i$-th selected position is $j_i = \rho + iK$ for $0 \le i < f$, counted from the least significant bit. The procedure computes

$$y_{j_i} \leftarrow y_{j_i} \oplus x_{j_i} \qquad (0 \le i < f),$$

so the selected bits of $x$ are XORed into the same positions of $y$, where $\oplus$ is exclusive or.

For example, take $f=2$, $K=6$, $L=12$ and $\rho=1$, so the selected positions are $j_0=1$ and $j_1=7$. If the $x$ bits there are $1$ and $0$, and the $y$ bits are $1$ and $1$, the procedure leaves the $y$ bits as $0$ and $1$.

The construction applies a constant number of cyclic shifts of whole chunk ranges, and these shifts have the required effect away from a small set of addresses. The procedure then corrects exactly that set. The construction is built from three streaming operations: an [address-field interchange](address-interchange.md) of equal-width chunks, cyclic shifts of chunk ranges, and a fixed permutation of two-bit values. It is a restricted form of the [address shear](address-shear.md) that changes only the selected positions.

The correction term in the time is scaled by $\delta_{\text{bad}} = \min\{1, 80(f-1)2^{-K}\}$, which is small when $K$ is large.

Each record has $R$ bits, a bit count distinct from the coefficient count $r$. Let $N_0,\dots,N_3$ be the sizes of the four other coordinate ranges, so $M = 2^{3L}N_0N_1N_2N_3$ counts the records, and $V = MR$ is the total number of bits. Here $\tau$ is a fixed exponent with $0<\tau<1$. Under the asymptotic conditions of the lemma, the time is $O(V(L^\tau+1))$ (cited).
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

Write the answer to `exegenius/tasks/0058-audit-packed-bit-addition.answer.json`, then run `exegenius submit 0058-audit-packed-bit-addition` in the project directory. If submit rejects the answer, fix the answer and submit again.
