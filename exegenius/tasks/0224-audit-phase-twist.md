# exegenius task 0224-audit-phase-twist

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
- Cyclic convolution
- Gaussian resampling (also: Harvey–van der Hoeven resampling, Gaussian weights)
- Bluestein's chirp identity (also: chirp identity)
- Synthetic polynomial transforms (also: Nussbaumer polynomial transforms, polynomial transforms, Nussbaumer and Quandalle)
- Polynomial ring modulo y^r + 1 (also: negacyclic polynomial ring)
  - $y$ (polynomial variable): The indeterminate of the polynomial ring, whose powers act as roots of unity.
  - $r$ (record length): The number of complex coefficients in a polynomial record, a power of two.
- Signed coefficient packing (also: Kronecker substitution)
- Subspace labels
- Linear networks and frames (also: roles, frames)
- Subset-intersection network (also: three-element subset network, subset-intersection network and complex phase network)
- Address-field interchange (also: power-width interchange, tape procedure for interchanging address chunks)
- Address shear
- Rank-saving recursion (also: recursive saving)
- Gaussian dyadics
- Complex phase network (also: phase-frame identity, complex variant)
- Simultaneous butterfly layer
- Packed selected-bit addition
- Guard-width bound
- Transform layout
- Transform identity with retained permutations (also: target permutation)
- Address field (also: address chunk, chunk, target chunk)
- Transform axis (also: axis, remaining axes)
- Linear algebra basics (also: linear algebra: invertible linear operator, matrix, inverse, matrix, linear map)
- Bilinear map (also: bilinear product)
- Bilinear form (also: bilinear space, orthogonality, bilinear form and orthogonality, bilinear space and bilinear form)
- Binary field (also: finite field F2, F_2, finite field F_2)
- Binary change of basis
- Bit procedure
- Butterfly
- Congruence (also: congruence modulo B, modulo)
- Centered residue
- Linear contraction (also: contraction)
- Cyclic shift (also: controlled cyclic shift)
- Convolution
- Coprime (also: gcd, pairwise coprime, coprime (gcd))
- Running time cost (also: cost)
- Cost table
- Stable radix sort
- Destination rank
- Endpoint operator
- Gate and terminal of a network
- Gaussian integer
- Grid numerator (also: grid numerators)
- Ground set
- Indicator vector
- Modular inverse (also: invertible modulo q)
- Cyclic coordinate (also: last cyclic coordinate)
- Limit inferior
- Line spanned by a vector
- Little-o notation
- Multidimensional transform (also: multidimensional transforms with power-of-two axes)
- Array norm (also: norm of an array)
- Normalized cyclic convolution
- Normalization scales (also: normalizations and known scales)
- Numerical layer
- Opposite transform (also: opposite-sign transform)
- Padded transform box
- Payload
- Phase factor (also: phase factors and scalar corrections)
- Polynomial ring
- Matrix rank (also: rational rank)
- Schoolbook multiplication
- Scratch storage (also: scratch values, scratch chunk, scratch wires)
- Tensor product (also: tensor power)
- Transform round
- Truncation
- Union bound
- Exclusive or (also: XOR)

## Symbols bound on earlier pages

- $k$ (output position), bound on `convolution`: The position of an entry of the output sequence c.
- $i$ (input position in a), bound on `convolution`: The position of an entry of a in a product a_i b_j.
- $j$ (input position in b), bound on `convolution`: The position of an entry of b in a product a_i b_j.
- $y$ (vector), bound on `linear-algebra-basics`: A second vector in a vector space over $F$.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $k$ (term index), bound on `limit-inferior`: The position of a term in the sequence $x$.
- $y$ (tail infimum), bound on `limit-inferior`: The smallest term of the sequence at or after position $m$, written $y_m$.
- $y$ (second input), bound on `exact-integer-multiplication`: The second input, a binary string of length n.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in the padded binary string, so it counts the bit positions of the representation.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $i$ (position index), bound on `cyclic-shift`: A position in the block, numbered from 0 to L-1.
- $k$ (offset), bound on `cyclic-shift`: The integer, taken modulo L, by which the cyclic shift rotates the block.
- $k$ (level count), bound on `address-interchange`: The number of recursion levels, log base m of the field width.
- $j$ (level depth), bound on `address-interchange`: The number of levels below the top call.
- $i$ (imaginary unit), bound on `gaussian-integer`: The number whose square is $-1$.
- $k$ (key), bound on `stable-radix-sort`: The key of a record, written as a string of $w$ bits.
- $i$ (bit index), bound on `stable-radix-sort`: The position of a key bit, counting from 0 at the least significant end; pass $i$ sorts by bit $k_i$.
- $\zeta$ (phase factor), bound on `phase-factor`: A complex number of modulus one, the factor multiplied into coefficients.
- $k$ (denominator power), bound on `gaussian-dyadics`: The number of factors of two in the denominator of an element of $\mathbb{D}$.
- $l$ (second denominator power), bound on `gaussian-dyadics`: The number of factors of two in the denominator of the second element $b/2^l$.
- $j$ (input index), bound on `discrete-fourier-transform`: An integer index of input coordinates, running from 0 to q-1.
- $i$ (digit position), bound on `radix-digit-convolution`: The position of a digit in an input, running from 0 to m-1.
- $r$ (record length), bound on `synthetic-transforms`: The number of complex coefficients in a record, a power of two at least 2.
- $y$ (polynomial variable), bound on `synthetic-transforms`: The formal variable of the polynomial ring $R_r$.
- $k$ (coefficient position), bound on `polynomial-ring-mod-yr-plus-1`: The position of a coefficient in a record, running from 0 to r-1.
- $\zeta$ (root of unity), bound on `polynomial-ring-mod-yr-plus-1`: A complex number that some positive integer power of it equals 1.
- $e$ (integer), bound on `congruence-modulo`: An integer, the other of the two integers compared by congruence.
- $i$ (imaginary unit), bound on `complex-phase-network`: The imaginary unit, with $i^2 = -1$.
- $\cdot$ (dot product), bound on `complex-phase-network`: The parity of the number of coordinates where two binary vectors are both 1.
- $i$ (axis index), bound on `transform-round`: The index of a participating axis, running over the D participating axes.
- $i$ (row index), bound on `address-shear`: The row of a one in $\Pi$, which names an $H$ field.
- $j$ (column index), bound on `address-shear`: The column of a one in $\Pi$, which names a $D$ field.
- $\zeta$ (stream address length), bound on `packed-bit-addition`: The number of bits needed to write a position in the stream, ceiling of log base 2 of 2V.
- $\cdot$ (entrywise product), bound on `transform-identity`: The product of two vectors of the same length taken entry by entry.

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

## Page to audit (`phase-twist`)

````markdown
# Phase twist

A phase twist multiplies each coefficient of a record by a root of unity. It acts on the last [cyclic coordinate](cyclic-coordinate.md) of a convolution, changing that coordinate so that its wrap-around carries the sign of a polynomial ring. It is the step of [Integer multiplication below n log n](main-theorem.md) that lets the remaining convolution be computed over that ring.

A record is a list of $r$ complex coefficients, where $r$ is the record length. The phase twist is applied after [Bluestein's chirp identity](bluestein-chirp-identity.md) has rewritten the middle transform as a cyclic convolution. The source states the twist's effect in one sentence: modulo $y^r + 1$, and

Write $\zeta = e^{\pi i/r}$ for a root of unity of order $2r$: $\zeta^{2r} = 1$, no smaller positive power of $\zeta$ equals $1$, and $\zeta^r = -1$. Here $j$ is the position of a coefficient in the record, counted from $0$. The phase twist multiplies the coefficient in position $j$ by $\zeta^j$, for every $j$ from $0$ to $r-1$. The inverse twist, called the untwist, multiplies it by $\zeta^{-j}$ instead.

The reason for the twist is that a plain cyclic convolution wraps a term back with a plus sign, while the polynomial ring wraps it with a minus sign. The twist supplies the missing sign. Let $k$ denote the position of the coefficient from the first record, and $l$ the position of the coefficient from the second. Their product carries the twist factor $\zeta^k \zeta^l = \zeta^{k+l}$. A cyclic convolution of length $r$ sends a term with $k+l \ge r$ back to position $k+l-r$ with a plus sign. In $\mathbb{C}[y]/(y^r+1)$ the same term is $y^{k+l} = -y^{k+l-r}$, because $y^r = -1$, so it arrives with a minus sign. The untwist at position $k+l-r$ multiplies the wrapped term by $\zeta^{-(k+l-r)}$, so the total factor is $\zeta^{k+l}\zeta^{-(k+l-r)} = \zeta^r = -1$. That is the minus sign of the ring, so the wrap is negative. A term with $k+l < r$ gets the factor $\zeta^{k+l}\zeta^{-(k+l)} = 1$ and is unchanged.

The phase twist turns the last cyclic coordinate into a coefficient list of the [polynomial ring modulo $y^r + 1$](polynomial-ring-mod-yr-plus-1.md).

Take $r = 2$. Then $\zeta = e^{\pi i/2} = i$ and $\zeta^{-1} = -i$. Consider the records $(1, 2)$ and $(3, 4)$, which stand for $1 + 2y$ and $3 + 4y$ in $\mathbb{C}[y]/(y^2+1)$. Their twists are $(1, 2i)$ and $(3, 4i)$. The cyclic convolution of length $2$ of the twisted records has position $0$ equal to $1 \cdot 3 + (2i)(4i) = -5$ and position $1$ equal to $1 \cdot 4i + 2i \cdot 3 = 10i$. The untwist multiplies position $1$ by $-i$, giving $10$, so the result is $(-5, 10)$. Computing directly in the ring, $(1+2y)(3+4y) = 3 + 10y + 8y^2 = -5 + 10y$, the same record.
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

Write the answer to `exegenius/tasks/0224-audit-phase-twist.answer.json`, then run `exegenius submit 0224-audit-phase-twist` in the project directory. If submit rejects the answer, fix the answer and submit again.
