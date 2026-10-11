# exegenius task 0186-audit-discrete-fourier-transform

Project directory: `/mnt/openai-nlogn` (paths below are relative to it)

Audit one page of an explanatory wiki on behalf of a specific reader. Use only this task file: do not read the sources, other pages or any other file.

The reader knows exactly the concepts listed as known, together with what the reader profile states. Everything else that you know, the reader does not know: treat it as unknown to them, however elementary it seems to you. You are simulating that reader's lack of knowledge, so use your own knowledge only to recognise what the reader is missing.

Symbols: account for every symbol in the page's mathematics, each once, saying where the reader learns what it denotes:
- `here`: the page says what it denotes; quote the sentence that says it. A use in an example ("take $r = 4$") or a range ("a power of two $r$") does not say what $r$ denotes or counts. If the page uses the symbol before that sentence, submit records that the meaning comes too late.
- `page`: an earlier page binds it, as listed under "Symbols bound on earlier pages".
- `concept`: the name of a known concept contains it and binds it, as listed under that concept. A symbol in a known concept's name that is listed with no meaning is not known.
- `background`: standard notation the reader profile covers; say what covers it.
- `unbound`: nothing tells the reader what it denotes.
Submit checks that each symbol is in the page's mathematics, that each quote is on the page and contains the symbol, and that the named page or concept binds it.

Terms and steps: a term or step is followable if the reader knows it, the page explains it, or the page links it to another wiki page. Report every term or step on the page that the reader cannot follow:
- term: a named concept the reader does not know, which the page neither explains nor links.
- step: an inference, calculation or claim the reader cannot check from what the page gives.

Copy each quote from the page exactly, character for character, and keep it short: submit rejects quotes it cannot find on the page. Do not report anything the reader can follow. Answer with an empty list of gaps if the reader can follow the whole page.

## Reader profile

Undergraduate computer science: big-O notation, polynomials, complex numbers, basic Turing machines and tapes

## Known concepts

- Big-O notation
- Polynomials
- Complex numbers
- Turing machines and tapes (also: multitape Turing machine)
- Fixed-tape machine model (also: fixed finite-tape model)
- Exact integer multiplication
- The n log n optimality conjecture (also: Schönhage–Strassen conjecture)
- Established O(n log n) multiplier (also: Harvey–van der Hoeven multiplier)
- Linear networks and frames (also: roles, frames)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Gaussian dyadics
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Binary field (also: finite field F2, F_2, finite field F_2)
- Binary change of basis
- Bit procedure
- Cyclic shift (also: controlled cyclic shift)
- Convolution
- Running time cost (also: cost)
- Cost table
- Stable radix sort
- Destination rank
- Endpoint operator
- Gate and terminal of a network
- Gaussian integer
- Ground set
- Indicator vector
- Limit inferior
- Line spanned by a vector
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Matrix rank (also: rational rank)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $j$ (input position in b), bound on `convolution`: The position of an entry of b in a product a_i b_j.
- $u$ (field width), bound on `address-field`: The number of address bits in each of the two fields being interchanged, a count.
- $F$ (field), bound on `linear-algebra-basics`: The field of scalars over which vector spaces are taken.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $m$ (starting position), bound on `limit-inferior`: A position in the sequence from which a tail infimum is taken.
- $\ell$ (log axis length), bound on `cost-table`: The base-2 logarithm of $r$.
- $L$ (block length), bound on `cyclic-shift`: The number of positions in the block that a cyclic shift rotates.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $u$ (field width), bound on `address-interchange`: The number of bits in each field.
- $m$ (recursion base), bound on `address-interchange`: A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $j$ (level depth), bound on `address-interchange`: The number of levels below the top call.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $m$ (number of factors), bound on `tensor-product`: The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $m$ (matrix size), bound on `matrix-rank`: The number of rows of a square matrix M, which is also its number of columns.
- $m$ (number of subsets), bound on `union-bound`: The number of subsets $E_1, \dots, E_m$ of $\Omega$ whose union is bounded.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $q$ (address before the move), bound on `destination-rank`: The address of a record before the move.
- $m$ (selected bit count), bound on `binary-change-of-basis`: The number of selected address bits that the change acts on, which is also the size of the square matrix M.

## Pages in the wiki

- [Convolution](convolution.md)
- [Transform axis](transform-axis.md)
- [Address field](address-field.md)
- [Exclusive or](xor.md)
- [Linear algebra basics](linear-algebra-basics.md)
- [Linear networks and frames](linear-network-frames.md)
- [Endpoint operator](endpoint-operator.md)
- [Limit inferior](limit-inferior.md)
- [Fixed-tape machine model](fixed-tape-model.md)
- [Running time cost](running-time-cost.md)
- [Exact integer multiplication](exact-integer-multiplication.md)
- [The n log n optimality conjecture](n-log-n-conjecture.md)
- [Cost table](cost-table.md)
- [Established O(n log n) multiplier](established-multiplier.md)
- [Cyclic shift](cyclic-shift.md)
- [Ground set](ground-set.md)
- [Gate and terminal of a network](network-gate-terminal.md)
- [Scratch storage](scratch-storage.md)
- [Address-field interchange](address-interchange.md)
- [Bit procedure](bit-procedure.md)
- [Binary field](binary-field.md)
- [Indicator vector](indicator-vector.md)
- [Line spanned by a vector](line-spanned-by-vector.md)
- [Gaussian integer](gaussian-integer.md)
- [Tensor product](tensor-product.md)
- [Matrix rank](matrix-rank.md)
- [Truncation](truncation.md)
- [Payload](payload.md)
- [Union bound](union-bound.md)
- [Schoolbook multiplication](schoolbook-multiplication.md)
- [Stable radix sort](stable-radix-sort.md)
- [Destination rank](destination-rank.md)
- [Binary change of basis](binary-change-of-basis.md)
- [Phase factor](phase-factor.md)
- [Gaussian dyadics](gaussian-dyadics.md)
- [Discrete Fourier transform](discrete-fourier-transform.md)
- [Radix-digit convolution](radix-digit-convolution.md)
- [Multidimensional transform](multidimensional-transform.md)
- [Synthetic polynomial transforms](synthetic-transforms.md)
- [Gaussian resampling](gaussian-resampling.md)
- [Polynomial ring modulo y^r + 1](polynomial-ring-mod-yr-plus-1.md)
- [Butterfly](butterfly.md)
- [Opposite transform](opposite-transform.md)
- [Polynomial ring](polynomial-ring.md)
- [Array norm](array-norm.md)
- [Grid numerator](grid-numerator.md)
- [Linear contraction](linear-contraction.md)
- [Congruence](congruence-modulo.md)
- [Signed coefficient packing](signed-packing.md)
- [Centered residue](centered-residue.md)
- [Cyclic convolution](cyclic-convolution.md)
- [Cyclic coordinate](cyclic-coordinate.md)
- [Bilinear map](bilinear-map.md)
- [Bilinear form](bilinear-form.md)
- [Subspace labels](subspace-labels.md)
- [Subset-intersection network](subset-intersection-network.md)
- [Complex phase network](complex-phase-network.md)
- [Simultaneous butterfly layer](simultaneous-butterfly-layer.md)
- [Transform layout](transform-layout.md)
- [Numerical layer](numerical-layer.md)
- [Rank-saving recursion](rank-saving-recursion.md)
- [Transform round](transform-round.md)
- [Padded transform box](padded-transform-box.md)
- [Normalized cyclic convolution](normalized-cyclic-convolution.md)
- [Normalization scales](normalization-scales.md)
- [Little-o notation](little-o-notation.md)
- [Guard-width bound](guard-width-bound.md)
- [Coprime](coprime.md)
- [Modular inverse](modular-inverse.md)
- [Address shear](address-shear.md)
- [Packed selected-bit addition](packed-bit-addition.md)
- [Transform identity with retained permutations](transform-identity.md)
- [Bluestein's chirp identity](bluestein-chirp-identity.md)
- [Phase twist](phase-twist.md)
- [Ring homomorphism and isomorphism](ring-homomorphism.md)
- [Mixed-radix digits](mixed-radix-digits.md)
- [Chinese-remainder map](chinese-remainder-map.md)
- [Prime source lengths](prime-source-lengths.md)
- [Carry propagation](carry-propagation.md)
- [Convolution over the polynomial ring](polynomial-ring-convolution.md)
- [Exact coefficient recovery](recovery-and-error.md)
- [Integer multiplication below n log n](main-theorem.md)

## Page to audit (`discrete-fourier-transform`)

````markdown
# Discrete Fourier transform

The discrete Fourier transform is needed for [convolution](convolution.md). The argument uses its normalized form:. The page on [Gaussian resampling](gaussian-resampling.md) replaces these transforms by transforms whose lengths are powers of two, and the page on [Synthetic polynomial transforms](synthetic-transforms.md) replaces their roots of unity by powers of a polynomial variable.

Let $q$ be the length of the transform, the number of coordinates of each vector it acts on. A $q$-th root of unity is a complex number whose $q$-th power is $1$. Let $\omega = e^{-2\pi i/q}$ be the primitive $q$-th root of unity, a complex number with $\omega^q = 1$ and no smaller positive power of it equal to $1$.

Let $u = (u_0, u_1, \ldots, u_{q-1})$ be a vector of $q$ complex numbers. Let $j$, $\ell$ and $m$ be integer indices running over $0, 1, \ldots, q-1$, where $j$ and $m$ index input coordinates and $\ell$ indexes output coordinates. The discrete Fourier transform of length $q$ is the map $F_q$ sending $u$ to the vector $F_q u$ with coordinates

$$
(F_q u)_\ell = \frac{1}{q} \sum_{j=0}^{q-1} u_j\, \omega^{j\ell} = \frac{1}{q} \sum_{j=0}^{q-1} u_j\, e^{-2\pi i\, j\ell/q}.
$$

The discrete Fourier transform $F_q$ is a [linear map](linear-algebra-basics.md) of $q$-vectors. Each output $(F_q u)_\ell$ is a weighted sum of all $q$ inputs, with weights $\omega^{j\ell}$ of modulus one, and the factor $1/q$ is the normalization. The exponent carries a negative sign. The paper *Integer multiplication below n log n* uses the same sign:.

$F_q^+$ is the same map with the positive sign, which replaces $\omega$ by $\omega^{-1}$. Applying it after $F_q$ returns the input divided by $q$:

$$
(F_q^+ F_q u)_\ell = \frac{1}{q^2} \sum_{m=0}^{q-1} u_m \sum_{j=0}^{q-1} \omega^{j(m-\ell)} = \frac{u_\ell}{q}.
$$

The inner sum over $j$ is $q$ when $m = \ell$. Otherwise $\omega^{m-\ell} \ne 1$, since $m-\ell$ is a nonzero integer that is not a multiple of $q$. Also $(\omega^{m-\ell})^q = 1$, so the geometric sum $\sum_{j=0}^{q-1} (\omega^{m-\ell})^j = \frac{(\omega^{m-\ell})^q - 1}{\omega^{m-\ell} - 1}$ is $0$.

The vector norm used for bounds is of its coordinates, so $\|u\| = \max_j |u_j|$. A linear map $L$ is a contraction when $\|Lu\| \le \|u\|$ for every $u$. The paper gives the reason for the normalized transforms: by complex numbers of modulus one. Concretely, $|(F_q u)_\ell| \le \frac{1}{q}\sum_j |u_j| \le \max_j |u_j|$.

Worked example. Take $q = 4$. Then $\omega = e^{-2\pi i/4} = -i$, so $\omega^0 = 1$, $\omega^1 = -i$, $\omega^2 = -1$ and $\omega^3 = i$. For $u = (1, 2, 3, 4)$,

$$
(F_4 u)_0 = \tfrac{1}{4}(1+2+3+4) = \tfrac{5}{2}, \qquad (F_4 u)_1 = \tfrac{1}{4}(1-2i-3+4i) = \tfrac{-1+i}{2},
$$

$$
(F_4 u)_2 = \tfrac{1}{4}(1-2+3-4) = -\tfrac{1}{2}, \qquad (F_4 u)_3 = \tfrac{1}{4}(1+2i-3-4i) = \tfrac{-1-i}{2}.
$$
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

Write the answer to `exegenius/tasks/0186-audit-discrete-fourier-transform.answer.json`, then run `exegenius submit 0186-audit-discrete-fourier-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
