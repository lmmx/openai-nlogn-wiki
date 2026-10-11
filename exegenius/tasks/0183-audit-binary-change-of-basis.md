# exegenius task 0183-audit-binary-change-of-basis

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
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Binary field (also: finite field F2, F_2, finite field F_2)
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
- Matrix rank (also: rational rank)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $a$ (first input sequence), bound on `convolution`: The first input sequence, of length n.
- $b$ (second input sequence), bound on `convolution`: The second input sequence, of length n.
- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $a$ (input bit), bound on `xor`: The first of the two bits that an XOR combines.
- $b$ (input bit), bound on `xor`: The second of the two bits that an XOR combines.
- $\oplus$ (exclusive or), bound on `xor`: The XOR operation: $a \oplus b$ is the bitwise sum modulo 2 of the bits $a$ and $b$, which is 1 exactly when they differ.
- $F$ (field), bound on `linear-algebra-basics`: The field of scalars over which vector spaces are taken.
- $x$ (vector), bound on `linear-algebra-basics`: A vector in a vector space over $F$.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $I$ (identity matrix), bound on `linear-algebra-basics`: The matrix with ones on the diagonal and zeros elsewhere.
- $M$ (matrix of a frame), bound on `linear-algebra-basics`: A matrix that determines the frame $\Phi_M$.
- $G$ (pointwise linear gate), bound on `linear-network-frames`: A gate that combines its input arrays separately at each address.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $a$ (path start vertex), bound on `endpoint-operator`: The first of three vertices on a path through the network.
- $b$ (path middle vertex), bound on `endpoint-operator`: The middle of three vertices on a path through the network.
- $x$ (sequence), bound on `limit-inferior`: A sequence of real numbers $x_1, x_2, x_3, \dots$ whose $k$-th term is $x_k$.
- $m$ (starting position), bound on `limit-inferior`: A position in the sequence from which a tail infimum is taken.
- $x$ (first input), bound on `exact-integer-multiplication`: The first input, a binary string of length n.
- $b$ (log-length parameter), bound on `cost-table`: The rounded-up base-2 logarithm of the input length $n$.
- $p$ (working precision), bound on `cost-table`: The precision parameter $p = 6b$, which sets the coefficient width up to a constant factor.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $L$ (block length), bound on `cyclic-shift`: The number of positions in the block that a cyclic shift rotates.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $a$ (first field), bound on `address-interchange`: The first of the two fields being interchanged.
- $b$ (second field), bound on `address-interchange`: The second of the two fields being interchanged.
- $\oplus$ (XOR operator), bound on `address-interchange`: Bitwise exclusive or.
- $m$ (recursion base), bound on `address-interchange`: A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $\mathbb{F}_2$ (binary field), bound on `binary-field`: The field with the two elements 0 and 1, where addition is exclusive or and multiplication is AND.
- $a$ (real part), bound on `gaussian-integer`: The real part of a Gaussian integer, which is an integer.
- $b$ (imaginary part), bound on `gaussian-integer`: The imaginary part of a Gaussian integer, which is an integer.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $P$ (matrix), bound on `tensor-product`: A matrix whose entry in row i and column j is p_{ij}.
- $m$ (number of factors), bound on `tensor-product`: The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $m$ (matrix size), bound on `matrix-rank`: The number of rows of a square matrix M, which is also its number of columns.
- $M$ (rational matrix), bound on `matrix-rank`: A rational matrix with m rows and m columns.
- $p$ (fractional precision), bound on `truncation`: The number of fractional binary places kept, so the grid spacing is $2^{-p}$.
- $m$ (number of subsets), bound on `union-bound`: The number of subsets $E_1, \dots, E_m$ of $\Omega$ whose union is bounded.
- $M$ (record count), bound on `stable-radix-sort`: The number of records being sorted.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $M$ (record count), bound on `destination-rank`: The number of records in the stream.

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

## Page to audit (`binary-change-of-basis`)

````markdown
# Binary change of basis

A binary change of basis is an invertible linear change of coordinates on a block of selected address bits, built over the [binary field](binary-field.md). On the way to the main result it is the step that puts a residual basis of directions into coordinate positions, which the [rank-saving recursion](rank-saving-recursion.md) then uses. The paper describes this step as

Let $m$ be the number of selected address bits the change acts on. Write $\mathbf b=(b_1,\dots,b_m)$ for the column of those bits, each $b_i\in\mathbb F_2$. A binary change of basis is specified by an invertible matrix in [Linear algebra basics](linear-algebra-basics.md): a matrix $M$ with an inverse $M^{-1}$, so that $M^{-1}M=I$. We write $\mathrm{GL}(m,\mathbb F_2)$ for the set of invertible $m\times m$ matrices over $\mathbb F_2$. The change sends the bits $\mathbf b$ to $M\mathbf b$. Only invertibility is needed:

Here $\mathbf a\in\mathbb F_2^m$ denotes an address of the $m$ selected bits. For $M\in\mathrm{GL}(m,\mathbb F_2)$, $P_M$ is the address permutation that moves the value at each address $\mathbf a$ to $M\mathbf a$. The paper's wording is

**Elementary row additions.** The basic move is adding one row of $M$ to another. For example, take $m=3$ and
$$M=\begin{pmatrix}1&1&0\\0&1&0\\0&0&1\end{pmatrix}.$$
This is the identity with an extra 1 in row 1, column 2, so it adds the second bit into the first. For $\mathbf b=(1,1,0)$,
$$M\mathbf b=(1\oplus 1,\;1,\;0)=(0,1,0).$$
Adding row 2 to row 1 a second time restores the original matrix, so $M^{-1}=M$.

Every $M\in\mathrm{GL}(m,\mathbb F_2)$ is a product of row additions.. For $m=3$ this is at most $15$ row additions. The inverse of such a product is the same row additions in reverse order:
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

Write the answer to `exegenius/tasks/0183-audit-binary-change-of-basis.answer.json`, then run `exegenius submit 0183-audit-binary-change-of-basis` in the project directory. If submit rejects the answer, fix the answer and submit again.
