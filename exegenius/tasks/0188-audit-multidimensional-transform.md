# exegenius task 0188-audit-multidimensional-transform

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
- Radix-digit convolution
- Discrete Fourier transform (also: normalized Fourier transform, transform)
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
- $D$ (number of axes), bound on `transform-axis`: The number of axes of an array, which is the number of coordinates in each address.
- $u$ (field width), bound on `address-field`: The number of address bits in each of the two fields being interchanged, a count.
- $F$ (field), bound on `linear-algebra-basics`: The field of scalars over which vector spaces are taken.
- $m$ (coordinate count), bound on `linear-algebra-basics`: The number of coordinates in each vector of $F^m$, which is the dimension of $F^m$.
- $M$ (matrix of a frame), bound on `linear-algebra-basics`: A matrix that determines the frame $\Phi_M$.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $m$ (starting position), bound on `limit-inferior`: A position in the sequence from which a tail infimum is taken.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $h$ (ground set size), bound on `ground-set`: The number of elements of the ground set $[h]$.
- $u$ (field width), bound on `address-interchange`: The number of bits in each field.
- $m$ (recursion base), bound on `address-interchange`: A fixed base in which the field width is written, so that each recursion level divides the width by m.
- $s$ (child call count), bound on `address-interchange`: The number of calls that one call makes on smaller fields.
- $h$ (ground-set size), bound on `indicator-vector`: The number of elements in the ground set $[h] = \{1, \dots, h\}$, which is 100 in the construction.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $\otimes$ (tensor product), bound on `tensor-product`: The operation that forms the block matrix P \otimes Q, also called the Kronecker product.
- $m$ (number of factors), bound on `tensor-product`: The number of copies of P in the power P^{\otimes m}, which is also the number of address coordinates the operator acts on.
- $m$ (matrix size), bound on `matrix-rank`: The number of rows of a square matrix M, which is also its number of columns.
- $M$ (rational matrix), bound on `matrix-rank`: A rational matrix with m rows and m columns.
- $m$ (number of subsets), bound on `union-bound`: The number of subsets $E_1, \dots, E_m$ of $\Omega$ whose union is bounded.
- $M$ (record count), bound on `stable-radix-sort`: The number of records being sorted.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $h$ (chunk index), bound on `destination-rank`: The index of one of the three address chunks, taking values 1, 2 or 3.
- $M$ (record count), bound on `destination-rank`: The number of records in the stream.
- $m$ (selected bit count), bound on `binary-change-of-basis`: The number of selected address bits that the change acts on, which is also the size of the square matrix M.
- $M$ (change matrix), bound on `binary-change-of-basis`: The invertible m-by-m matrix over the binary field that specifies the change of basis.
- $u$ (input vector), bound on `discrete-fourier-transform`: A vector of q complex numbers, the input of the transform.
- $m$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $m$ (digit count), bound on `radix-digit-convolution`: The number of digits in each input, the count of blocks of b bits.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $t$ (product coefficient position), bound on `radix-digit-convolution`: The position of a coefficient of the product polynomial, running from 0 to 2m-2.

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

## Page to audit (`multidimensional-transform`)

````markdown
# Multidimensional transform

A multidimensional transform is a Fourier transform taken over several [transform axes](transform-axis.md) at once, computed by transforming along each axis in turn. [Gaussian resampling](gaussian-resampling.md) uses it in place of the ordinary Fourier transforms of the convolution: the reduction axis lengths are powers of two.

Let $D \ge 1$ be the number of axes, a positive integer. The transform acts over the [transform axes](transform-axis.md) $1,\dots,D$. Write $s$ for the index of an axis, running from $1$ to $D$. Write $t_s$ for the length of axis $s$, the number of coordinates along it, which is a power of two in the argument. Write $M = t_1 t_2 \cdots t_D$ for the number of entries of the array. Write $X$ for the input array and $Y$ for the output array. Write $m=(m_1,\dots,m_D)$ for a position in $X$ and $h=(h_1,\dots,h_D)$ for a position in $Y$, each with $0\le m_s<t_s$ for every $s$. The multidimensional transform $\mathcal F$ sends $X$ to $Y = \mathcal F X$ by the formula below.

$$
Y_h = \frac{1}{M}\sum_{m}\Big(\prod_{s=1}^{D} e^{-2\pi i\, m_s h_s/t_s}\Big)\, X_m
$$

The sum runs over all positions $m$. The transform $\mathcal F$ is built from the [discrete Fourier transforms](discrete-fourier-transform.md) $F_{t_1},\dots,F_{t_D}$ by tensor product, one on each axis: $\mathcal F = F_{t_1}\otimes\cdots\otimes F_{t_D}$. Each factor carries its own normalization $1/t_s$, and their product is the $1/M$ in the formula.

A line along axis $s$ is the set of positions that agree in every coordinate except $m_s$. Each factor $F_{t_s}$ acts only on the coordinate $m_s$, so the factors commute. Hence $\mathcal F X$ is found in one pass per axis: transform every line along axis 1, then every line along axis 2, and so on. The sources compute it the same way:

## Worked example

Take $D=2$ and $t_1=t_2=2$, so $M=4$. For length $2$ the root is $e^{-2\pi i/2}=-1$, so the one-dimensional transform sends $(u_0,u_1)$ to $\big((u_0+u_1)/2,\ (u_0-u_1)/2\big)$. Let $X_{0,0}=1$, $X_{0,1}=2$, $X_{1,0}=3$ and $X_{1,1}=4$.

Along axis 2, each row is transformed: the row $(1,2)$ becomes $(3/2,\,-1/2)$ and the row $(3,4)$ becomes $(7/2,\,-1/2)$. Along axis 1, each column is then transformed: $(3/2,\,7/2)$ becomes $(5/2,\,-1)$ and $(-1/2,\,-1/2)$ becomes $(-1/2,\,0)$. So $Y_{0,0}=5/2$, $Y_{0,1}=-1/2$, $Y_{1,0}=-1$ and $Y_{1,1}=0$. The formula agrees at $h=(0,1)$: $\frac14(1-2+3-4)=-\frac12$.

## Why axis lengths are powers of two

A two-point butterfly replaces a pair of entries by their sum and their difference, up to a scalar. When every $t_s$ is a power of two, each one-dimensional transform is a sequence of such butterflies with multiplications by roots of unity between them. In the sources' representation, Restricting the axis lengths to powers of two is what makes the roots of unity signed shifts.
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

Write the answer to `exegenius/tasks/0188-audit-multidimensional-transform.answer.json`, then run `exegenius submit 0188-audit-multidimensional-transform` in the project directory. If submit rejects the answer, fix the answer and submit again.
