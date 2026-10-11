# exegenius task 0182-audit-destination-rank

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
- $n$ (sequence length), bound on `convolution`: The number of entries in each input sequence.
- $k$ (output position), bound on `convolution`: The position of an entry of the output sequence c.
- $c$ (convolution), bound on `convolution`: The convolution of a and b, a sequence of length 2n-1.
- $a$ (input bit), bound on `xor`: The first of the two bits that an XOR combines.
- $c$ (scalar), bound on `linear-algebra-basics`: A scalar, an element of the field $F$.
- $A$ (matrix), bound on `linear-algebra-basics`: An $m\times m$ matrix with entries in $F$.
- $M$ (matrix of a frame), bound on `linear-algebra-basics`: A matrix that determines the frame $\Phi_M$.
- $t$ (gate input count), bound on `linear-network-frames`: The number of input arrays a gate takes.
- $r$ (output role), bound on `linear-network-frames`: An output role of the network.
- $a$ (path start vertex), bound on `endpoint-operator`: The first of three vertices on a path through the network.
- $c$ (path end vertex), bound on `endpoint-operator`: The last of three vertices on a path through the network.
- $k$ (term index), bound on `limit-inferior`: The position of a term in the sequence $x$.
- $n$ (input length), bound on `limit-inferior`: The number of bits in each input, which is the index of the running-time function.
- $A$ (fixed machine), bound on `limit-inferior`: A fixed multiplication machine whose running time is studied.
- $c$ (positive constant), bound on `limit-inferior`: A positive real constant in the lower bound and its negation.
- $n$ (input bit length), bound on `fixed-tape-model`: The number of bits in each of the two input integers.
- $A$ (multiplication machine), bound on `fixed-tape-model`: A fixed Turing machine that multiplies two integers, whose running time is T_A.
- $k$ (padded length), bound on `exact-integer-multiplication`: The number of bits in the padded binary string, so it counts the bit positions of the representation.
- $r$ (longest axis length), bound on `cost-table`: The number of cells along the longest axis of the padded box.
- $c$ (chunk exponent), bound on `cost-table`: A fixed positive rational exponent that sets $K$ relative to $d$.
- $k$ (offset), bound on `cyclic-shift`: The integer, taken modulo L, by which the cyclic shift rotates the block.
- $h$ (ground set size), bound on `ground-set`: The number of elements of the ground set $[h]$.
- $a$ (first field), bound on `address-interchange`: The first of the two fields being interchanged.
- $k$ (level count), bound on `address-interchange`: The number of recursion levels, log base m of the field width.
- $h$ (ground-set size), bound on `indicator-vector`: The number of elements in the ground set $[h] = \{1, \dots, h\}$, which is 100 in the construction.
- $a$ (real part), bound on `gaussian-integer`: The real part of a Gaussian integer, which is an integer.
- $M$ (rational matrix), bound on `matrix-rank`: A rational matrix with m rows and m columns.
- $M$ (record count), bound on `stable-radix-sort`: The number of records being sorted.
- $k$ (key), bound on `stable-radix-sort`: The key of a record, written as a string of $w$ bits.

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

## Page to audit (`destination-rank`)

````markdown
# Destination rank

A destination rank is the position a record takes in the final order after a move, given by its rank among the records in that order. It is the key that lets displaced records return to their places in one pass over the stream.

Each destination rank is the key on which the extracted records are sorted by [Stable radix sort](stable-radix-sort.md).

Each record is stored at an address made of three chunks, named $1$, $2$ and $3$ on this page. Let $q$ be the address of a record before the move, and let $q'$ be its address after the move.

The position of the record at $q$ among the records in stream order is its rank, written $\operatorname{rank}(q)$. A counter that moves through the stream computes it:.

For chunk $h \in \{1,2,3\}$, let $q_h$ and $q'_h$ be the current and destination values of chunk $h$, and let $\sigma_h$ be the record stride of chunk $h$, the amount by which the rank changes when chunk $h$ rises by one with the other chunks fixed.

The destination rank follows from the current rank by a signed sum over the chunks:

$$\operatorname{rank}(q') = \operatorname{rank}(q) + \sum_{h=1}^{3} (q'_h - q_h)\,\sigma_h.$$

 A chunk can therefore lower the rank as well as raise it.

For example, take strides $\sigma_1 = 1$, $\sigma_2 = 4$ and $\sigma_3 = 12$, as for chunks with 4 and 3 values. In this example the rank of $(a_1, a_2, a_3)$ is $a_1 \cdot 1 + a_2 \cdot 4 + a_3 \cdot 12$. The record at $q = (1, 2, 0)$ has rank $1 \cdot 1 + 2 \cdot 4 = 9$, and its destination is $q' = (3, 0, 1)$. The formula gives $\operatorname{rank}(q') = 9 + (3-1)\cdot 1 + (0-2)\cdot 4 + (1-0)\cdot 12 = 15$, which agrees with the direct count $3 \cdot 1 + 0 \cdot 4 + 1 \cdot 12 = 15$.

Here $M$ is the number of records in the stream, and $A_{\mathrm{rect}}$ is a bit-size bound for the integers the rectangular routine handles..

The algorithm attaches this destination rank, padded to $\lceil \log_2 M \rceil \le A_{\mathrm{rect}}$ bits, to each extracted record.

Each extracted record also marks its hole, the position it returns to, on a fixed track of the stream:. Since the move permutes the exceptional addresses, the destination ranks are distinct and are exactly the ranks of the marked holes:. Sorting the records by destination rank therefore puts each record into its own hole.

The sort runs one pass per bit of the key, and bound how many passes there are, so the width of the rank sets the number of passes in the cost bound.
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

Write the answer to `exegenius/tasks/0182-audit-destination-rank.answer.json`, then run `exegenius submit 0182-audit-destination-rank` in the project directory. If submit rejects the answer, fix the answer and submit again.
